<img align="right" width="200" height="37" src="images/Gematik_Logo_Flag_With_Background.png"/> <br/>
  
# Electronic Personal Health Record System (ePA)

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-epa">About ePA </a></li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#additional-pages">Additional pages</a></li>
    <li><a href="#release-notes">Release Notes</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contributions">Contributions</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About ePA
This repository offers technical information for the Electronic Personal Health Record Environment (ePA) as part of the Telematic Infrastructure (TI).

This branch relates to a particular release in context of **ePA Version 42.6** 

The provided content comprises normative and supplementary resources and includes implementation guidelines, apis and schemas, examples and additional information.

The current branch accompanies a particular release of specification documents of ePA version 2.6 (a set of normative specification documents for components, producttypes and vendortypes) published on [Fachportal Gematik](https://fachportal.gematik.de/) (see [Branchinformation.md](./Branchinformation.md)  for specific version information and links).

The content in /src is normative in context of requirements defined by those specification docuemnts and is essential for product approvals. Any other content is for information. Normative content here and the documents together form a single product release of the Electronic Personal Health Record system for an approval process.

The affected and covered producttypes are **epa-Aktensystem** and **epa-Frontend des Versicherten**. 

ePA-Resources for produkttypes **Konnektor** "("Fachmodul ePA") and **KTR-Consumer** ("Fachmodul ePA im KTR-Consumer") are also in scope of a particular ePA release version. As these resources are integrated parts of the named producttypes, release cycles follow the roadmap of those producttypes. See [Fachportal Gematik](https://fachportal.gematik.de/) and repository [api-telematik](https://github.com/gematik/api-telematik), path /conn/phr ("Fachmodul ePA") and /consumer ("Fachmodul ePA im KTR-Consumer") for resources and additional information.


## Structure 
The content is organized as shown in the following diagram  

<code><pre>
api-epa
|- [docs](docs) (additional information)
|- [images](images) (images of this page)
|- [samples](samples) (samples)
|     |-- [epa 1 messages PS - Konnektor](samples/epa%201%20Beispielnachrichten%20PS%20-%20Konnektor)
|     |-- [epa 2 messages PS - Konnektor](samples/epa%202%20Beispielnachrichten%20PS%20-%20Konnektor)
|     └-- [policies](samples/policies) (Policy Beispiele)
|- [src](src) (normative resources)
|     |-- [implementation_guides](src/implementation_guides) (metadata for structured documents)
|     |-- [openapi](src/openapi) (interfaces REST)
|     |-- [policies](src/policies) (policy templates)
|     |-- [schema](src/schema) (interfaces SOAP)
|     |     |-- [tel](src/schema/tel) (telematik error scheme)
|     |     |-- [ext](src/schema/ext) (external schemes)
|     |     └-- [fd/phr](src/schema/fd/phr) (interface ePA health record system)
|     └-- [vocabulary](src/vocabulary) (terminologies)
|- [Readme.md](./Readme.md) (this information)
|- [ReleaseNotes.md](./ReleaseNotes.md) (release history)
|- [Branchinformation](./Branchinformation.md) (information about branch status and links)
|- [LICENSE](./LICENSE) (license file)
└- [Security.md](./Security.md) (security policy)
</pre>
</code>

## Additional pages
The following pages provide additional information and resources related to ePA 

+ example implementation health record provider change (<https://github.com/gematik/ref-ePA-HealthRecordMigration.git>)</br>
+ poc implementation research data submission (https://github.com/gematik/poc-ePA-Forschungsdatenfreigabe)</br>
+ reference implementation anti virus gate for hospitals (https://github.com/gematik/ref-ePA-AV-Gate)</br>
+ further modules and interfaces (Konnektor, Consumer) (https://github.com/gematik/api-telematik/tree/OPB5)</br>
+ legacy ePA-Releases (Releases 1, 2 und 2.1) (https://github.com/gematik/api-ePA/tree/epa_2_maintenance)</br>
+ older ePA-Releases (releases of 2.5, except 2.5.2) (https://github.com/gematik/api-ePA/tree/master)</br>(navigate by tags, e.g. 2.5.X-Y)
+ ePA-Releases from version 2.5.2 (https://github.com/gematik/api-ePA)</br>(each release in a branch named equal to a release number, e.g. ePA-2.6)

</br>


## Release Notes
See `ReleaseNotes.md` for all information regarding the (newest) releases.

## License
 
Copyright 2023 gematik GmbH
 
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.
 
See the [LICENSE](./LICENSE) for the specific language governing permissions and limitations under the License.
 
Unless required by applicable law the software is provided "as is" without warranty of any kind, either express or implied, including, but not limited to, the warranties of fitness for a particular purpose, merchantability, and/or non-infringement. The authors or copyright holders shall not be liable in any manner whatsoever for any damages or other claims arising from, out of or in connection with the software or the use or other dealings with the software, whether in an action of contract, tort, or otherwise.
 
The software is the result of research and development activities, therefore not necessarily quality assured and without the character of a liable product. For this reason, gematik does not provide any support or other user assistance (unless otherwise stated in individual cases and without justification of a legal obligation). Furthermore, there is no claim to further development and adaptation of the results to a more current state of the art.
 
Gematik may remove published results temporarily or permanently from the place of publication at any time without prior notice or justification.


## Contributions

This repository is for publication of approved artefacts in context of a specific ePA release. Changes to normative content may be applied in rare exceptional cases but is not intended. Such changes will be covered by follow-up releases in different branches.
Therefor submission of issues and pull requests are not rejected by default but the preferred channel is a contact via gematik website (see <a href="#contact">Contact</a> below) 

## Contact

Please use the contact sheet https://fachportal.gematik.de/kontaktformular and choose "elektronische Patientenakte (ePA)" as request category in drop-down list "Thema der Anfrage/Kategorien".

