# Docker-Image selber erzeugen

Wenn Sie das Docker-Image nur nutzen wollen, aber nicht selbst erzeugen
(modifizieren) wollen, dann lesen Sie hier *nicht* weiter, sondern lesen
Sie den Abschnitt Docker-Container in [README.md](README.md).

## pipreqs

Merker:
https://www.idiotinside.com/2015/05/10/python-auto-generate-requirements-txt/


## docker build

    docker build -t as-wechsel:1.0 .

## dockerhub push

    [a@h minimal]$ docker login
    Authenticating with existing credentials...
    WARNING! Your password will be stored unencrypted in /home/a/.docker/config.json.
    Configure a credential helper to remove this warning. See
    https://docs.docker.com/engine/reference/commandline/login/#credentials-store

    Login Succeeded
    [a@h minimal]$ docker tag as-wechsel:1.0 andreashallof/as-wechsel:test
    [a@h minimal]$ docker push andreashallof/as-wechsel:test
    The push refers to repository [docker.io/andreashallof/as-wechsel]
    8a953f89eed7: Pushed 
    40f3a87dcb9d: Pushed 
    024062e038fb: Pushed 
    4ffadc7b8b66: Pushed 
    2660e5fd5183: Pushed 
    66884c8fce2c: Pushed 
    28c9049c08eb: Pushed 
    387dcb3d6704: Pushed 
    d7850a46b8f8: Pushed 
    6dfcd44e4d42: Mounted from library/python 
    e03003eb71e4: Mounted from library/python 
    ca3c8e460f97: Mounted from library/python 
    4b4c002ee6ca: Mounted from library/python 
    cdc9dae211b4: Mounted from library/python 
    7095af798ace: Mounted from library/python 
    fe6a4fdbedc0: Mounted from library/python 
    e4d0e810d54a: Mounted from library/python 
    4e006334a6fd: Mounted from library/python 
    test: digest: sha256:8d808b4077041c599b9bf31ad0e0c6416f9186672b33a76d9787372295752e86 size: 4116

## Merker aspell

aspell check ...Input-Datei..


