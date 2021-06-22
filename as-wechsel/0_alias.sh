#! /bin/bash

# diese Datei muss man per 'source' oder '.' in der aktuell
# laufenden bash-Instanz source-n

function da() {

    for file in *; do
        if [ ${#file} -eq 64 ]; then
            rm -v $file
        fi
    done
}
