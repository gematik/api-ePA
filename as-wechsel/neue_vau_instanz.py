#! /usr/bin/env python3
# -*- coding: UTF-8 -*-

"""
Das ist die Referenzimplementierung für die Verschlüsselung und Signatur
beim Export der Akte für den AS-Wechsel.

Die ist der Code für die neue (i. S. v. importierende) VAU-Instanz.

Die alte VAU-Instanz stellt das Export-Paket zunächst als ZIP-File zusammen.
Und dann wird es mit dem Kontextschlüssel der Akte via AES/GCM verschlüsselt.
Das Chiffrat wird zusammen mit der Exportzeit und der KVRN der Akte von der
alten VAU signiert. Das Ergebnis wird dann via ECIES-Verschlüsselung für die
neue VAU verschlüsselt. Die neue VAU-Instanz entschlüssel die Daten (ECIES).
Dann überprüft es
    1. die Signatur,
    2. ob das Paket nicht älter als einen Monat ist,
    3. ob die signierte KVNR gleich der aktuellen KVNR (Ausführungskontext
       aktuelle Akte) ist.
Ist alles OK, entschlüssel ich das innere Chiffrat (chiffrat_1) mittels
des vom Nutzer übergebenen Kontextschlüssels (AES/GCM).

"""

import cbor, datetime, sys, os, hashlib

from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.exceptions import InvalidSignature


if __name__ == "__main__":

    # Annahme für das Beispiel hier: Ich lauf als neue VAU-Instanz für den
    # Versicherten:
    aktueller_versicherter_kvrn = b"A123456789"

    # Jetzt hole ich mir das doppeltverschlüsselte Export-Paket.
    # Normaler Weise würde ich (= neue VAU-Instanz) mir das über HTTPS
    # mit dem vom Nutzer übergebenen "PackageURL" holen. Hier im Beispiel
    # lasse ich mir das vom Nutzer als Datei übergeben.

    if len(sys.argv)==1 or not os.path.exists(sys.argv[1]):
        sys.exit("Fehler: ich erwarte den Dateinamen des doppeltverschlüsselen"
                 " Export-Pakets im lokalen Dateisystem.")
    chiffrat_2 = open(sys.argv[1], "rb").read()
    # teste prefix 0x01
    assert chiffrat_2[0] == 1
    # los geht es mit der ECIES-Entschlüsselung
    with open("pki/neue_vau_enc_priv_key.pem", "rb") as f:
        vau_enc_private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend())

    pub_numbers = ec.EllipticCurvePublicNumbers(
        int.from_bytes(chiffrat_2[1:1+32], byteorder='big'),
        int.from_bytes(chiffrat_2[33:33+32], byteorder='big'),
        ec.BrainpoolP256R1())
    message_public_key = pub_numbers.public_key()

    # führe Elliptic-Curve-Diffie-Hellman durch
    shared_secret = vau_enc_private_key.exchange(ec.ECDH(), message_public_key)
    # Nun leite ich einen AES-Schlüssel für AES/GCM aus dem gemeinsamen
    # ECDH-Geheimnis ab.
    hkdf = HKDF(algorithm=hashes.SHA256(), length=32, salt=None,
                info=b'ePA-Export-Paket', backend=default_backend())
    aes_key = hkdf.derive(shared_secret)

    # Die Nachricht wird jetzt mit AES/GCM entschlüsselt.
    iv = chiffrat_2[1+32+32:1+32+32+12]; assert len(iv) == 12
    aes_ciphertext = chiffrat_2[1+32+32+12:]
    plaintext_2 = AESGCM(aes_key).decrypt(iv, aes_ciphertext, associated_data=None)

    # das würde man sicherlich in einer 'try' Umgebung laufen lassen,
    # denn bei Fehlkodierung (was in der Praxis quasi nicht vorkommt
    # würde es hier eine Exception geben.
    list_plaintext_2 = cbor.loads(plaintext_2)
    # Sanity-Checks
    assert len(list_plaintext_2) == 6
    assert list_plaintext_2[0] == 1

    # Jetzt prüfe ich zunächst die Signatur, denn wenn die nicht stimmt
    # gucke ich mir die eigentlichen Daten erst gar nicht an.
    signer_cert_der, signature = list_plaintext_2[-2:]
    # Das signer_cert prüfen: TUC_PKI_018 (oid_epa_vau, FD.SIG)
    # spare ich mir hier mal und prüfe gegen meinen lokalen "trust-store".
    trusted_signer_cert_der = open("pki/alte_vau_sign_cert.der", "rb").read()
    assert signer_cert_der == trusted_signer_cert_der

    signer_cert = x509.load_der_x509_certificate(signer_cert_der, default_backend())
    public_key = signer_cert.public_key()
    dtbs = b""
    for element in list_plaintext_2[1:-2]:
        dtbs += element
    try:
        public_key.verify(signature, dtbs, ec.ECDSA(hashes.SHA256()))
    except InvalidSignature:
        sys.exit("sig-fail")
    except Exception as my_exception:
        sys.exit("hm sig-fail " + str(my_exception))

    # So die Signatur ist OK, damit kommt das Paket von einer gültigen ePA-VAU.
    # Ist das Paket wirklich für den Versicherten für den ich jetzt
    # als VAU-Instanz arbeite?
    assert aktueller_versicherter_kvrn == list_plaintext_2[3]

    export_time = datetime.datetime.fromisoformat(list_plaintext_2[2].decode())
    if export_time + datetime.timedelta(days=30) < datetime.datetime.now():
        sys.exit("Export-Paket ist zu alt -> Abbruch")

    # Sanity-Check
    chiffrat_1 = list_plaintext_2[1]
    assert len(chiffrat_2) > 12+1+16

    # Der Nutzer hat mir bei OpenContext zuvor den Kontext-Schlüssel der Akte
    # gegeben. Hier im Beispiel ist er:
    user_context_key = b'0123456789abcdef'*2
    assert len(user_context_key) == 32

    plaintext_1 = AESGCM(user_context_key).decrypt(chiffrat_1[0:12],
                  chiffrat_1[12:], associated_data=None)

    print("Die Export-Daten (ZIP-File) haben die Größe {} und den Hashwert {}.".format(
            len(plaintext_1), hashlib.sha256(plaintext_1).hexdigest()))

