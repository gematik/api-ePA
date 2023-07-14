# Elektronische Patientenakte (ePA) 2.5

<img src="images/gematik_logo.jpg" alt="gematik_logo" width="35%"/>



Dieser Branch gehört zu ePA-Release 2.6 EU-Pilot - Einbindung NCPeH für Zugriffe aus dem EU-Ausland

## Pilotierung des ePA-Zugriffs für Leistungserbringer aus dem EU-Ausland
Dieser Release ist ausschließlich im Kontext der Pilotierung des EU-Zugriffs relevant.

Inhaltlich basiert dieser Branch auf der letzten offiziellen Version der ePA (2.6.0-2) und erweitert diese
um die Funktionalität der Generierung und Anzeige eines AccessCodes im FdV für den Leistungserbringer im EU-Ausland, den Transport des AccessCodes via NCPeH im SOAP-Header ausgewählter IHE Operationen und ein Policy-Template mit Regeln für die Prüfung des AccesCode.
Der pilotierte Zugriff beschränkt sich auf das MIO ePKA, bzw. die Inhalte des Ordners "nfd". Für die ePKA wurde eine Implementation-Guide mit den erforderlichen Metadaten ergänzt.

## Allgemeines

Dieses Repository stellt begleitende Dokumentation zur aktuellen Spezifikation der Elektronischen Patientenakte, Implementierungsartefakte sowie die Schnittstellen des ePA-Aktensystems zur Verfügung.

Der vorliegende Branch korrespondiert mit einem bestimmten ePA Spezifikations-Release (normative Spezifikationen, Produkt- und Anbietersteckbriefe) zur elektronischen Patientenakte 2.5. Diese Spezifikationen werden auf dem Fachportal der gematik veröffentlicht. (siehe auch [Branchinformation.md](Branchinformation.md)) 

Im Pfad /src des vorliegenden Branches befinden sich Inhalte, die im Kontext der Anforderungen der Spezififikationen normativ und Bestandteil von Zulassungen sind. Die Veröffentlichungen hier und die zugehörige Veröffentlichung der Spezifikationen über das Fachportal bilden einen vollständigen Release zur elektronischen Patientenakte 2.5. 
Die normativ betroffenen Produkttypsteckbriefe sind **ePA-Aktensystem** und **ePA-Frontend des Versicherten**.</br></br>
Die Bereitstellung der ePA-Resourcen für die Produkttypen **Konnektor** und **KTR-Consumer** (ePA-Fachmodule) erfolgt über das gematik-Repository [api-telematik](https://github.com/gematik/api-telematik/tree/OPB5). Offizielle Veröffentlichungen und Releases dieser Produktypen und der darin verwendeten Resourcen der ePA erfolgen jedoch unabhängig von ePA-Releases (siehe "Konnektor" und "KTR-Consumer" auf www.gematik.de/fachportal)

## Ordnerstruktur

Im Folgenden ist die Organisation der Inhalte des vorliegenden Branches dargestellt.
<code><pre>
api-epa
|- [docs](docs) (weitergehende Informationen)
|- [images](images) (Bildarchiv)
|- [samples](samples) (Beispiele)
|     |-- [epa 1 Beispielnachrichten PS - Konnektor](samples/epa%201%20Beispielnachrichten%20PS%20-%20Konnektor)
|     |-- [epa 2 Beispielnachrichten PS - Konnektor](samples/epa%202%20Beispielnachrichten%20PS%20-%20Konnektor)
|     └-- [policies](samples/policies) (Policy Beispiele)
|- [src](src) (technische Artefakte)
|     |-- [implementation_guides](src/implementation_guides) (Metadatenvorgabe strukturierte Dokumente)
|     |-- [openapi](src/openapi) (Schnittstellen REST)
|     |-- [policies](src/policies) (Policy Vorlagen)
|     |-- [schema](src/schema) (Schnittstellen SOAP)
|     |     |-- [tel](src/schema/tel) (Telematik Error Schemas)
|     |     |-- [ext](src/schema/ext) (externe Schemas)
|     |     └-- [fd/phr](src/schema/fd/phr) (Schnittstellen ePA Aktensystem)
|     └-- [vocabulary](src/vocabulary) (Terminologien)
|- [Readme.md](Readme.md) (diese Information)
└- [Branchinformation.md](Branchinformation.md) (Informationen zu Releasebezug und -Status)
</pre>
</code>

## Weiterführende Seiten
Die folgenden Seiten enthalten zusätzliche Informationen im Kontext ePA 2.5

+ Referenzimplementierung zum Aktenumzug (<https://github.com/gematik/ref-ePA-HealthRecordMigration.git>)</br>
+ Beispielimplementierung zur Nutzung der Schnittstellen für die Forschungsdatenfreigabe (https://github.com/gematik/poc-ePA-Forschungsdatenfreigabe)</br>
+ Referenzimplementierung einer Antiviruslösung für das Krankenhausumfeld (https://github.com/gematik/ref-ePA-AV-Gate)</br>
+ weitere Schnittstellen der TI (Konnektor, Consumer) (https://github.com/gematik/api-telematik/tree/OPB5)</br></br>
+ Inhalte zu älteren ePA-Releases (Releases 1, 2 und 2.1) (https://github.com/gematik/api-ePA/tree/epa_2_maintenance)</br>(Navigation über die History oder die Tags 1.0.X-Y, 2.0.X-Y und 2.1.X-Y)
+ Inhalte zu älteren Veröffentlichungen ePA 2.5 (vor Release 2.5.2) (https://github.com/gematik/api-ePA/tree/master)</br>(Navigation über die History oder die Tags 2.5.X-Y)

</br>


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
