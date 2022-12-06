# 
## Liesmich
Die Codes der beiden Code-Systeme
- [Internationale statistische Klassifikation der Krankheiten und verwandter Gesundheitsprobleme (ICD), 10. Revision, German Modification ICD-10-GM Version 2022 BfArM, BMG](https://www.bfarm.de/SharedDocs/Downloads/DE/Kodiersysteme/klassifikationen/icd-10-gm/version2022/icd10gm2022syst-claml_zip.html)
- [Operationen- und Prozedurenschlüssel nach §301 SGB V - OPS Internationale Klassifikation der Prozeduren in der Medizin Version 2022; BfArM, BMG](https://www.bfarm.de/SharedDocs/Downloads/DE/Kodiersysteme/klassifikationen/ops/version2022/ops2022syst-claml_zip.html)

können als Event Code in den Dokumentmetadaten verwendet werden. Diese werden vom BfArM im Format der *Classification Markup Language (ClaML)* bereitgestellt. Zur Unterstützung der ePA-Hersteller erfolgt hier eine additive Bereitstellung im FHIR-Format. 

Basis für die Konvertierung ist der [ClaML to FHIR Transformer](https://github.com/aehrc/fhir-claml). Die folgenden beiden Befehle wurden hierzu angewandt:

```
$ java -jar .\target\fhir-claml-0.0.1-SNAPSHOT.jar -i <ABLAGEORT ICD CLAML>\icd10gm2022syst_claml_20210917.xml -designations preferredLong -o <GEWÜNSCHTER OUTPUTNAME>.json -id icd10gm2022 -url  http://fhir.de/CodeSystem/bfarm/icd-10-gm 
```

sowie

```
$ java -jar .\target\fhir-claml-0.0.1-SNAPSHOT.jar -i <ABLAGEORT OPS CLAML>\ops2022syst_claml_20211022.xml -designations preferredLong -o <GEWÜNSCHTER OUTPUTNAME>.json -id ops2022 -url  http://fhir.de/CodeSystem/bfarm/ops
```

**Hinweis:** *Das mit Maven kompilierte Projekt wurde mit Java 11 ausgeführt.*
