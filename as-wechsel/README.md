# Schutz des Export-Pakets bei AS-Anbieterwechsel

Wechselt ein Versicherter seinen ePA-Anbieter, werden die Daten seiner Akte vom
alten Anbieter zum neuen Anbieter übertragen. Hierzu wird im Aktensystem des
alten Anbieters ein Export-Paket mit den Daten der Akte erstellt, d. h. von den 
Meta-Daten und E2E-verschlüsselten Dokumenten.
Diese Export-Paket wird vom alten Anbieter dem neuen Anbieter zum Download zur
Verfügung gestellt. Der neue Anbieter kann das Export-Paket laden und die im
Export-Paket befindlichen Daten in das Konto des Versicherten beim neuen
Anbieter importieren.

Das Export-Paket wird innerhalb Vertrauenswürdiger Ausführungsumgebungen (VAU)
erstellt bzw. entpackt, jedoch außerhalb der VAU zum Download zur Verfügung
gestellt. Das Export-Paket wird daher vor unautorisierten Zugriff (insbesondere
auch durch Innentäter beim Betreiber des Aktensystems) durch die folgenden 
hier beschriebenen Maßnahmen zusätzlich geschützt.

## Schlüsselmaterial zum Schutz des Export-Paketes

Zum Schutz des Export-Pakets ist folgendes Schlüsselmaterial erforderlich:

- Kontextschlüssel des Versicherten (KS). Dieser wird dem Verarbeitungskontext
  beim Öffnen des Verarbeitungskontextes übergeben. Alle zu exportierenden
  Daten werden mittels des Kontextschlüssel symmetrisch verschlüsselt.

- Schlüsselmaterial der VAU zur Content-Signatur beim Betreiber
  (VAU-SIG-Zertifikat C.VAU-SIG mit öffentlichem Schlüssel Pub-VAU-SIG, privatem
  Schlüssel Priv-VAU-SIG)). 
  Der private Schlüssel kann nur durch eine VAU verwendet werden.

- Schlüsselmaterial der VAU zur Ver- und Entschlüsselung beim Betreiber
  (VAU-ENC-Zertifikat C.VAU-ENC mit öffentlichem Schlüssel Pub-VAU-ENC, privatem
  Schlüssel Priv-VAU-ENC)). Der private Schlüssel kann nur durch eine VAU 
  verwendet werden.

## Grundsätzlicher Ablauf der Verschlüsselung des Export-Pakets beim alten Anbieter

Das ePA-FdV ruft die Operation I\_Account\_Management\_Insurant::SuspendAccount
auf und übergibt dem Verarbeitungskontext dabei das VAU-ENC-Zertifikat
C.VAU-ENC des neuen Anbieters. Gemäß Anforderung
gemSpec\_Dokumentenverwaltung#A\_14855 wird bei Ausführung der Operation
SuspendAccount eine ZIP-Datei mit den zu übertragenden Daten des Versicherten
erstellt. 

Für den Schutz der ZIP-Datei sind folgende Schritte durchzuführen:

1. Der Verarbeitungskontext prüft das übergebene VAU-ENC-Zertifikat C.VAU-ENC
   gemäß `TUC_PKI_018`(oid\_epa\_vau). Falls die Prüfung fehlschlägt, wird eine
   Fehlermeldung `CERTIFICATE_INVALID`an das ePA-FdV gemeldet. Ansonsten
   wird mit Schritt (2) fortgefahren. 

2. Der Verarbeitungskontext bildet einen 256-Bit-Zufallswert und kodiert diesen
   hexadezimal. Das Ergebnis wird als `export_paket_name` bezeichnet und muss
   der Dateinamen des Exportpakets sein. Dem ePA-FdV wird dann als
   Ausgangsparameter die PackageURL, wobei der Dateiname in dieser URL 
   `export_paket_name` sein muss. Weiterhin darf der Pfadname in der URL
   keine personenbeziehbaren Daten enthalten.

3. Der Verarbeitungskontext verschlüsselt die ZIP-Datei symmetrisch (wie sonst
   auch bei ePA üblich AES/GCM, IV=96-Bit zufällig erzeugt, 128-Bit Auth-Tag)
   mit dem Kontextschlüssel KS und erhält `ciphertext_1`.

4. Der Verarbeitungskontext signiert mit dem privaten VAU-Signaturschlüssel
   Priv-VAU-SIG den Wert `ciphertext_1 ||  export_zeit || KVNR` und erhält als
   Ergebnis die Signatur `signature`. Hierbei ist `export_zeit` die aktuelle
   Zeit (ISO-Format) und `KVNR` die Krankenversichertennummer des Versicherten,
   der seinen Anbieter wechselt.

5. Der Verarbeitungskontext verschlüsselt das Array `plaintext_2 =
   [1, ciphertext_1, export_zeit, KVNR, C.VAU-SIG, signature]` (s.u. für genaues
   Format) hybrid mittels ECIES-Verschlüsselungsverfahren unter Nutzung des
   öffentlichem Schlüssels Pub-VAU-ENC aus dem VAU-ENC-Zertifikats des neuen
   Aktensystems und erhält `ciphertext_2`.

6. Der Verarbeitungskontext stellt `ciphertext_2` unter der erzeugten
   PackageURL (siehe Schritt 2) außerhalb der VAU zum Download für den neuen
   Anbieter bereit. 

## Grundsätzlicher Ablauf der Entschlüsselung des Export-Pakets beim neuen Anbieter
Das ePA-FdV ruft die Operation `I_Account_Management_Insurant::ResumeAccount`
beim neuen Aktenanbieter auf und übergibt dem Verarbeitungskontext dabei die
zuvor erhaltene PackageURL. Gemäß Anforderung
`gemSpec_Dokumentenverwaltung#A_14905` lädt der neue Anbieter das Export-Paket
vom durch PackageURL gegebenen Downloadpunkt und importiert die Daten des
Versicherten in das Aktenkonto beim neuen Anbieter. Hierzu muss das
Export-Paket in der VAU entschlüsselt werden, um die ZIP-Datei mit den Daten
des Versicherten zu erhalten.

Für die Entschlüsselung der ZIP-Datei sind folgende Schritte durchzuführen:

1. Der Verarbeitungskontext entschlüsselt `ciphertext_2` mittels
   ECIES-Verschlüsselungsverfahren unter Nutzung des privaten Schlüssels
   Priv-VAU-ENC und erhält das Array 
   `plaintext_2 = [1, ciphertext_1, export_zeit, KVNR, C.VAU-SIG, signature]`.

2. Der Verarbeitungskontext prüft die Signatur signature mittels des
   mitgelieferten Zertifikats C.VAU-SIG des alten Anbieters. Falls die Prüfung
   fehlschlägt, wird eine Fehlermeldung `CERTIFICATE_INVALID` an das ePA-FdV
   gemeldet. Ansonsten wird mit Schritt 3. fortgefahren.

3. Der Verarbeitungskontext prüft, dass KVNR mit der KVNR des angemeldeten
   Versicherten übereinstimmt und die `export_zeit` nicht mehr als x abweicht.
   Die `export_zeit` soll nicht älter als 30 Tage sein.
   Falls die Prüfung fehlschlägt, wird eine Fehlermeldung `INTERNAL_ERROR` an
   das ePA-FdV gemeldet. Ansonsten wird mit Schritt 3. fortgefahren.

4. Der Verarbeitungskontext entschlüsselt `ciphertext_1` mit dem Kontextschlüssel
   KS und erhält die unverschlüsselte ZIP-Datei für den Import.

## Hinweis zum Sicherheitsziel

Die zusätzliche (also "doppelte") Verschlüsselung des Export-Pakets mit dem
VAU-ENC-Schlüssel des neuen Anbieters erfolgt, um das Export-Paket auch im
Falle eines kompromittierten Akten- und/oder Kontextschlüssels zu sichern. So
können insbesondere auch Innentäter beim Betreiber, die sich das Export-Paket
kopieren und irgendwann an einen kompromittierten Akten- und/oder
Kontextschlüssel gelangen, nicht auf die Daten des Versicherten zugreifen.
Dies bedeutet auch, dass man sich bei einem kompromittierten Kontextschlüssel
nicht auf die Sicherheitsleistung des Kontextschlüssels in Bezug auf den
Integritätsschutz bei `ciphertext_1` verlassen kann. Deshalb erzeugt die
exportierende VAU eine Signatur des verschlüsselten Exportpakets inkl.
Metadaten (Exportzeit, KVNR). Dadurch ist sichergestellt, dass das Export-Paket
von der exportierenden VAU kommt. Dies verhindert insbesondere auch, dass
Innentäter beim Betreiber gültige Export-Pakete beliebig selbst erzeugen
können.

## Formate
### Chiffrat\_2 (eine '\x01' plus das normale ECIES-Chiffrat)

1. ein Byte \x01
2. 32-Byte X-Wert ephemerer Schlüssel 
   (bzw. wenn der Schlüssel in Verschlüsselungszertifikat der neuen VAU
   eine größere Kurve (brainpoolP384R1 etc.) dann sind dies analog viele
   Byte. Soll heissen: die pro-Nachricht-ephemeren Schlüssel hängen natürlich
   von den Verschlüsselungsschlüsseln der VAU aus dem Zertifikat ab.)
3. 32-Byte Y-Wert ephemerer Schlüssel 
4. 12 Byte IV für die AES/GCM-Entschlüsselung zufällig erzeugt
5. AES/GCM Chiffrat plus 16 Byte (= 128 Bit) Authentication-Tag

### Plaintext nach der ersten Entschlüsselung (also von Chiffrat\_2)

Ein [CBOR](https://www.rfc-editor.org/rfc/rfc8949.html)-Array der mit folgenden
sechs Elementen

1. eine 1 (integer) als Versionsnummer (Aufwärtskompatibilität)
2. das chiffrat\_1 als binary string
3. die Exportzeit im ISO-Format als ASCII-String der als binary string in CBOR
   kodiert ist (Beispiel: `2021-06-18T15:56:09.340643`)
4. die KVNR des Versicherten, dem die ePA zugehörig ist, als ASCII-String der als
   binary string in CBOR kodiert ist (Beispiel: `A123456789`)
5. das Signatur-Zertifikat der exportierenden -- also damit hier signierenden
   -- VAU-Instanz (binary string)
6. eine ECDSA-Signatur wie üblich nach TR-3111 kodiert (binary string)

Designüberlegung:

(1) 
Parsing/Deserialisierung ist nie angenehm. Wer lange genug sich mit ASN.1/CMS
geschlagen hat, wird sich etwas einfaches wünschen. CBOR wird u. A. bei
FIDO2/Webauthentication verwendet.

(2)
Das Datenformat soll so einfach wie möglich sein, deshalb wurde ein simples
array verwendet und keine verschachtelten Datenstrukturen.

(3)
Bei Datenformaten gibt es zwei Designrichtungen:

1. Daten nach dem was sie vom Daten-Typ sind zu kodieren, oder
2. Daten passend für die nächst folgenden Verarbeitungsschritte zu
   kodieren.

Bei Erhalt eines `plaintext_2` muss die neue VAU-Instanz zunächst die Signatur
prüfen. Signaturen können nur auf binär-Daten geprüft werden. Deshalb sind die
Exportzeit und die KVNR ebenfalls als binary string kodiert.


### Chiffrat\_1

Das ein AES/GCM-Chiffrat, verschlüsselt mit dem Kontext-Schlüssel und wie
üblich ein Binärstring beginnend:

- mit 12 Byte (= 96 Bit) IV zufällig pro Verschlüsselung erzeugt,
- dem (aus kryptographischer Sicht) eigentlichen AES/GCM-Chiffrat gefolgt von
  16 Byte (= 128 Bit) Authentication Tag.

## Ready-to-Run Docker-Container

Auf einem System, auf dem Docker installiert ist, kann man den Beispiel-Code
in wenigen Sekunden zum Starten bekommen:

    $ docker pull andreashallof/as-wechsel:1.0
    $ docker run -it andreashallof/as-wechsel:1.0 /bin/bash
    root@e29f79a5ae10:/as-wechsel# ./gen-test-daten.sh 10MiB
    10240+0 records in
    10240+0 records out
    10485760 bytes (10 MB, 10 MiB) copied, 0.134014 s, 78.2 MB/s
    root@e29f79a5ae10:/as-wechsel# sha256sum test-daten.bin 
    e5b844cc57f57094ea4585e235f36c78c1cd222262bb89d53c94dcb4d6b3e55d  test-daten.bin
    root@e29f79a5ae10:/as-wechsel# ./alte_vau_instanz.py 
    zu exportierenden Testdaten ("ZIP-Archiv"): 10485760 Bytes
    Export-Paket für den Dowloadpunkt (Name, Größe)=(a0779c88da19e8f5ecd6bca8f10b33a208c8b4eef01896965cc3c77dec14037c, 10486586)
    root@e29f79a5ae10:/as-wechsel# ls -l
    total 20536
    -rw-r--r-- 1 root root      231 Jun 15 11:24 0_alias.sh
    -rw-r--r-- 1 root root      709 Jun 25 06:57 Dockerfile
    -rw-r--r-- 1 root root      445 Jun 25 05:46 README-Dockerfile.md
    -rw-r--r-- 1 root root    10051 Jun 25 06:39 README.md
    -rw-r--r-- 1 root root 10486586 Jun 25 07:51 a0779c88da19e8f5ecd6bca8f10b33a208c8b4eef01896965cc3c77dec14037c
    -rwxr-xr-x 1 root root     4490 Jun 20 16:45 alte_vau_instanz.py
    -rwxr-xr-x 1 root root      435 Jun 24 13:48 gen-test-daten.sh
    -rwxr-xr-x 1 root root     5562 Jun 20 19:59 neue_vau_instanz.py
    drwxr-xr-x 2 root root     4096 Jun 20 08:14 pki
    -rw-r--r-- 1 root root       47 Jun 24 12:34 requirements.txt
    -rw-r--r-- 1 root root 10485760 Jun 25 07:51 test-daten.bin
    root@e29f79a5ae10:/as-wechsel# ./neue_vau_instanz.py a0779c88da19e8f5ecd6bca8f10b33a208c8b4eef01896965cc3c77dec14037c 
    Die Export-Daten (ZIP-File) haben die Größe 10485760 und den Hashwert e5b844cc57f57094ea4585e235f36c78c1cd222262bb89d53c94dcb4d6b3e55d.
    root@e29f79a5ae10:/as-wechsel# 


## Dependencies

Wer nicht den Docker-Container verwenden möchte, muss darauf achten die
notwendigen python-Libraries installiert zu haben. Dies kann man über den für
die verwendete Linux-Distribution üblichen Paket-Manager tun (apt-get, pacman,
emerge etc.) oder über `pip` -- siehe folgend.

### via Linux-Paket-Manager

Die python-Programm benötigen python3 mit den Bibliotheken `cryptography` und
`cbor`. Diese sind bei quasi allen Linux-Distributionen dabei.

Beispiel: 

- Ubuntu `apt install python-cryptography python3-cbor`
- Arch Linux `pacman -S extra/python-cryptography community/python-cbor`

### via pip

Alternativ `pip install -r requirements.txt` starten.


