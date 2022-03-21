## Release-Übersicht EPA-2.5

Die nachstehende Tabelle dokumentiert Hinweise zu Änderungen an den ePA-Spezifikationen sowie dieses Repository.<br/>


| Tag | Gültig ab | Information / Betroffene Spezifikationen/Steckbriefe im Fachportal | Vorabveröffentlichungen | Betroffene GitHub-Artefakte |
|---|---|---|---|---|
|2.5.0-Pre1|2022-03-21|Bugfix ||initialer Release Bugfix|
|2.5.0-CC|2022-03-18|alle Dokumente zu ePA Release 2.5.0 verfügar unter fachportal.gematik.de||initialer Release zur Kommentierung|
|2.1.1|2022-03-18|alle Dokumente zu ePA Release 2.1.1 verfügar unter fachportal.gematik.de|| - [hcp-policy-definition.xml](src/policies/hcp-policy-definition.xml)<br/> - [AuthorizationService.xsd](src/schema/fd/phr/AuthorizationService.xsd)|
|2.1.1-Pre1|2022-03-09||alle Änderungen gemäß ePA_Maintenance 22.1| - [vs-format-code.xml](src/vocabulary/value_sets/vs-format-code.xml)<br/> - [KeyManagementService.wsdl](src/schema/fd/phr/KeyManagementService.wsdl)<br/> - [KeyManagementService.xsd](src/schema/fd/phr/KeyManagementService.xsd)<br/> - [AuthenticationService.xsd](src/schema/fd/phr/AuthenticationService.xsd)<br/> - [AuthorizationService.xsd](src/schema/fd/phr/AuthorizationService.xsd)<br/> - [AccountManagementService.xsd](src/schema/fd/phr/AccountManagementService.xsd)|
|MIO_20220216||Implementation Guides und ValueSet Updates für MIOs, Stand: 16. Februar 2022<br/>(Nachtrag zu MIO_20220211) || - [ig-prescription_V_1_0_2.json](src/implementation_guides/ig-prescription_V_1_0_2.json)<br/> - [vs-format-code.xml](src/vocabulary/value_sets/vs-format-code.xml)
|MIO_20220211||Implementation Guides und ValueSet Updates für MIOs, Stand: 11. Februar 2022 || - [implemenation_guides](src/implementation_guides)<br/> - [value_sets](src/vocabulary/value_sets)
|2.1.0|2022-01-31|alle Dokumente zu ePA Release 2.1.0 verfügar unter fachportal.gematik.de|| - [request.xml](samples/ePA%202%20Beispielnachrichten%20PS%20-%20Konnektor/requestFacilityAuthorization/request.xml)<br/> - [response.xml](samples/ePA%202%20Beispielnachrichten%20PS%20-%20Konnektor/requestFacilityAuthorization/response.xml)<br/> - [berechtigungskonzept.adoc](docs/berechtigungskonzept.adoc)|
|2.1.0-Pre1|2022-01-13|---|Alle Änderungen gemäß ePA_Maintenance 21.4 und 21.5| - [healthcare-security-audit.xsd](src/schema/ext/IHE/healthcare-security-audit.xsd)<br/>- [AccountManagementService.xsd](src/schema/fd/phr/AccountManagementService.xsd) <br/>- [AuthenticationService.xsd](src/schema/fd/phr/AuthenticationService.xsd)<br/>- [AuthorizationService.xsd](src/schema/fd/phr/AuthorizationService.xsd)|
| 2.0.6-Pre2 | 2021-12-16 |  |  | - [KBV_PR_MIO_CMR_Practitioner](src/implementation_guides/KBV_PR_MIO_CMR_Practitioner_Dummy_Value.xml) |
|  |  |  |  |  |
|  |  |  |  |  |



(Legende zu 'Tag': X.Y.Z = gematik/epa Release X.Y.Z;   X.Y.Z-PreA = Vorveröffentlichung Nr. A zu Release X.Y.Z;   XXX_Datum = Veröffentlichung ohne gematik Releasebezug) )
