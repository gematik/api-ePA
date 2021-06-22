#! /usr/bin/env bash

#openssl ecparam -name prime256v1 -genkey -out alte_vau_sign_priv_key.pem
openssl ecparam -name brainpoolP256r1 -genkey -out alte_vau_sign_priv_key.pem

openssl req -x509 -key alte_vau_sign_priv_key.pem \
    -outform der \
    -out alte_vau_sign_cert.der -days 365 \
    -subj "/C=DE/ST=Berlin/L=Berlin/O=gematik/OU=gematik/CN=alte VAU Content-Signatur"

#openssl ecparam -name prime256v1 -genkey -out neue_vau_enc_priv_key.pem
openssl ecparam -name brainpoolP256r1 -genkey -out neue_vau_enc_priv_key.pem

openssl req -x509 -key neue_vau_enc_priv_key.pem \
    -outform der \
    -out neue_vau_enc_cert.der -days 365 \
    -subj "/C=DE/ST=Berlin/L=Berlin/O=gematik/OU=gematik/CN=neue VAU ENC"

