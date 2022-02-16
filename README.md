# Elektronische Patientenakte (ePA)

<img src="images/gematik_logo.jpg" alt="gematik_logo" width="35%"/>

## Allgemeines

Dieses Repository stellt begleitende Dokumentation zur aktuellen Spezifikation der Elektronischen Patientenakte, Implementierungsartefakte sowie die Schnittstellen des ePA-Aktensystems zur Verfügung.

## Release-Übersicht

Die nachstehende Tabelle dokumentiert Hinweise zu Änderungen an den ePA-Spezifikationen sowie dieses Repository.<br/>


| Tag | Gültig ab | Information / Betroffene Spezifikationen/Steckbriefe im Fachportal | Vorabveröffentlichungen | Betroffene GitHub-Artefakte |
|---|---|---|---|---|
|MIO_20220216||Implementation Guides und ValueSet Updates für MIOs, Stand: 16. Februar 2022<br/>(Nachtrag zu MIO_20220211) || - [ig-prescription_V_1_0_2.json](\src\implementation_guides\ig-prescription_V_1_0_2.json)<br/> - [vs-format-code.xml](\src\vocabulary\value_sets\vs-format-code.xml)
|MIO_20220211||Implementation Guides und ValueSet Updates für MIOs, Stand: 11. Februar 2022 || - [implemenation_guides](\src\implementation_guides)<br/> - [value_sets](\src\vocabulary\value_sets)
|2.1.0|2022-01-31|alle Dokumente zu ePA Release 2.1.0 verfügar unter fachportal.gematik.de|| - [request.xml](\samples\ePA%202%20Beispielnachrichten%20PS%20-%20Konnektor\requestFacilityAuthorization\request.xml)<br/> - [response.xml](\samples\ePA%202%20Beispielnachrichten%20PS%20-%20Konnektor\requestFacilityAuthorization\response.xml)<br/> - [berechtigungskonzept.adoc](\docs\berechtigungskonzept.adoc)|
|2.1.0-Pre1|2022-01-13|---|Alle Änderungen gemäß ePA_Maintenance 21.4 und 21.5| - [healthcare-security-audit.xsd](\src\schema\ext\IHE\healthcare-security-audit.xsd)<br/>- [AccountManagementService.xsd](\src\schema\fd\phr\AccountManagementService.xsd) <br/>- [AuthenticationService.xsd](\src\schema\fd\phr\AuthenticationService.xsd)<br/>- [AuthorizationService.xsd](\src\schema\fd\phr\AuthorizationService.xsd)|
| 2.0.6-Pre2 | 2021-12-16 |  |  | - [KBV_PR_MIO_CMR_Practitioner](/src/implementation_guides/KBV_PR_MIO_CMR_Practitioner_Dummy_Value.xml) |
|  |  |  |  |  |
|  |  |  |  |  |



(Legende zu 'Tag': X.Y.Z = gematik/epa Release X.Y.Z;   X.Y.Z-PreA = Vorveröffentlichung Nr. A zu Release X.Y.Z;   XXX_Datum = Veröffentlichung ohne gematik Releasebezug) )

## Ordnerstruktur

Im Folgenden ist die Organisation der Ordnerstruktur dargestellt.

    api-ePA
    ├─ docs
    ├─ images
    ├─ samples
    │   ├──── ePA 1 Beispielnachrichten PS - Konnektor   
    │   │    ├── Requests
    │   │    └── Responses
    │   ├──── ePA 2 Beispielnachrichten PS - Konnektor   
    │   └──── policies
    ├─ src
    │   ├──── implementation_guides
    │   ├──── openapi
    │   ├──── policies    
    │   ├──── schema
    │   │    ├── tel
    │   │    ├── ext
    │   │    │   ├── ebRS
    │   │    │   ├── HL7V3
    │   │    │   └── IHE
    │   │    └── fd
    │   │        └── phr
    │   └──── vocabulary
    │        ├── code_systems
    │        └── value_sets 
    ├── README.md
    └── ReleaseNotes.md

### Hinweis zum Umzug der Schnittstelle des ePA-Aktensystems

Die Schnittstellen des ePA-Aktensystems wurden aus dem Repository <https://github.com/gematik/api-telematik.git> in dieses Repository verlagert und werden dort nicht weiter gepflegt.

Der Pfad `/api-ePA/src/schema/fd/phr` enthält vollständig die Artefakte der SOAP-Schnittstelle des ePA-Aktensystems (d.h. WSDL- und Schemadateien) sowie notwendige XML Schemata aus Standards (`/api-ePA/src/schema/ext`, bzw. `/api-ePA/src/schema/tel`).

### Hinweis zum Umzug der Implementierung "Schutz des Export-Pakets beim Aktensystem-/Anbieterwechsel"

Die Referenzimplementierung (bisher hier unter `/api-epa/as-wechsel` veröffentlicht) ist in das eigene Repository <https://github.com/gematik/ref-ePA-HealthRecordMigration.git> umgezogen.

## Weiterführende Seiten

[Leitfaden für Primärsystemhersteller](docs/epa-1-implementierungshinweise-ps.adoc)

[Berechtigungskonzept für ePA 2.0](docs/berechtigungskonzept.adoc)

## Lizenzbedingungen

Copyright (c) 2022 gematik GmbH

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
