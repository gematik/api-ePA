# Hinweise zu Value Sets und Code Systemen

## OID mit / ohne URN Schema

Die Value Sets und Code Systeme im vorliegenden Verzeichnis werden gemäß FHIR Standard strukturiert. Dieses erfordert eine Kodierung von OIDs für referenzierte Code Systeme mit Angabe des OID URN scheme/namespaces (siehe HL7/fhir uri type und rfc3986).

Beispiel: Value Set IHE XDS typeCode 

```
<system value="urn:oid:1.3.6.1.4.1.19376.3.276.1.5.9"/>
```

In den XDS Metadaten entspricht diese Darstellung in URN Syntax für OIDs dem Datentyp __OID URN__.
Für den XDS Datentyp __OID__ ist lediglich der ISO Object Identifier anzuwenden. 

Beispiel: typeCode codingScheme (XDS Datentyp OID) in DocumentEntry Metadaten 

```
<ns5:Slot name="codingScheme">
    <ns5:ValueList>
        <ns5:Value>1.3.6.1.4.1.19376.3.276.1.5.9</ns5:Value>
    </ns5:ValueList>
</ns5:Slot>
<ns5:Name>
    <ns5:LocalizedString xml:lang="de-DE" charset="UTF-8" value="Arztberichte"/>
</ns5:Name>
```