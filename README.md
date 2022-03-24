# Elektronische Patientenakte (ePA)

<img src="images/gematik_logo.jpg" alt="gematik_logo" width="35%"/>


## Hinweis
Dieses ist der Branch (epa_2_maintenance) für Veröffentlichungen im Kontext **EPA-2**, bzw. **EPA-2-Maintenance** !<br/>
Für Veröffentlichungen zu EPA-2.5 siehe Branch 'master'
## Allgemeines

Dieses Repository stellt begleitende Dokumentation zur aktuellen Spezifikation der Elektronischen Patientenakte, Implementierungsartefakte sowie die Schnittstellen des ePA-Aktensystems zur Verfügung.

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
    ├── Releaseübersicht.md
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
