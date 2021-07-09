# Release 2.0.4
changes since 2.0.4-pre3 - fixed erroneous DTO for Remove permissionHcpo (testtreiber_fdv.yaml)
 - moved deviceID parameter to header, added new error reponse 412 (DeviceUnknown), removed not used error responses(device_management.yaml)
 - added pagination for protocol, removed in findObjects (testtreiber_fdv.yaml)
 - update comments (hcp-policy-definition.xml)
 - update categjory "psychotherapy" (C_10787, hcp-poliy-2.xml)
 - several fixes (testtreiber_fdv.yaml)


# Release 2.0.4-pre3
- update and bugfix(testtreiber_fdv.yaml)
 - clarifications Dokumentenspezifische Autorisierung (C_10773, berechtigungskonzept.adoc)
 - update reference implementation "Aktensystem Wechsel", now with Docker (as_wechsel)
 - additional comment for deleteDevice (device_management.yaml)


# Release 2.0.4-pre2
- correction DeviceNameType minLength (device_management.yaml)
 - corrections in delta-export-time description (readme in as-wechsel)


# Release 2.0.4-pre1
- replaced "mothersrecord" with "childsrecord" in collection "mixed"
 - added reference implementation "Aktensystem Wechsel"
 - C_10778: modified access rights for midwife refering DVPMG\ - C_10773 - created metadata definitions for structured documents (renamed folder mio to implementation_guides)
 - updated structure for supporting generic documents (not solely mios)


# Release 2.0.3-4
- MIO: Mio Versions updated
 - PS: update implementation guide for PS
 - API: bugfix type AuthenticationAssertion (device_management.yaml)


# Release 2.0.3-3
- API: fixed syntax bugs, added missing parameters to paths, renamed path parameters (device_management.yaml)
 - API: corrections in comments and version history (device_management.yaml)
 - SAMPLES: C_10750 - permit access to very restricted documents added on a whitelist
 - MIO: correction of document cardinality (mr-mio-definition.json)


# Release 2.0.3-2
- new MIO definitions
 - moved testdriver to api-ePA
 - namespace corrections for policies
 - editorial changes


# Release 2.0.3-1
 - Changes - minor changes in HCP policy definition and sample HCP policies (i.e. HL7 namespace fixed)


# Release 2.0.3
 - ePA 2.0.3 - Release Notes Changes - description for access management and policy definitions added - upgrade notes added - device management API added

# Release 1.1.3
 - ePA 1.1.3 - Release Notes Changes - sample IHE messages added - implemention notes added

