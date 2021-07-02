#! /bin/bash

if [ "$1" = "" ]; then
    dd if=/dev/urandom of=test-daten.bin bs=1024 count=10
elif [ "$1" = zero ]; then
    dd if=/dev/urandom of=test-daten.bin bs=1024 count=10
elif [ "$1" = a ]; then
    python -c 'print("a"*10240, end="")' >test-daten.bin
elif [ "$1" = 1MiB ]; then
    dd if=/dev/zero of=test-daten.bin bs=1024 count=1024
elif [ "$1" = 10MiB ]; then
    dd if=/dev/zero of=test-daten.bin bs=1024 count=10240
fi

