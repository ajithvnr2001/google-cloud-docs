---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-identity-and-auth-data-changelog/
title: Change log for SAP_IDENTITY_AND_AUTH_DATA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:29.872142+00:00
---

# Change log for SAP_IDENTITY_AND_AUTH_DATA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-identity-and-auth-data-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_IDENTITY_AND_AUTH_DATA

Date | Changes  
---|---  
2026-02-04 |  \- Newly created parser.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `changeUsr`, `uname`, `aname`, `modifier`, `modbe` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `bname`, `username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `agrName` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.about.group.group_display_name: Newly mapped `childAgr` raw log field with `event.idm.read_only_udm.about.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `tcode` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped `class`, `profile` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `repid` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `field`, `struct`, `mandt`, `parentAgr`, `type`, `fromDat`, `toDat`, `ustyp`, `langu`, `ianatzonecode`, `trdat`, `ltime`, `pwdchgdate`, `pwdlgndate`, `pwdlockdate`, `pwdsaltedhash` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `systemid`, `partype` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `direct`, `uflag`, `securityPolicy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `attributes`, `changeDat`, `changeTim`, `createUsr`, `exclude`, `inherited`, `folder`, `colFlag`, `orgFlag`, `pardate`, `parname`, `parvalue`, `parstate`, `gltgv`, `gltgb`, `passcode`, `accnt`, `pwdinitial`, `stcod`, `spld`, `splg`, `dcpfm`, `hdest`, `hmand`, `hname`, `menon`, `menue`, `strtt`, `cattkennz`, `spdb`, `spda`, `datfm`, `timefm`, `bcode`, `ocod1`, `bcda1`, `codv1`, `ocod2`, `bcda2`, `codv2`, `ocod3`, `bcda3`, `codv3`, `ocod4`, `bcda4`, `codv4`, `ocod5`, `bcda5`, `codv5`, `versn`, `codvn`, `tzone`, `zbvmaster`, `pwdstate`, `reserved`, `pwdhistory`, `pwdsetdate`, `moddate`, `modtime`, `createDat`, `createTim`, `createTmp`, `changeTmp`, `changeTst`, `modda`, `modti`, `erdat`, `locnt` raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `SAP` static value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `SAP_IDENTITY_AND_AUTH_DATA` static value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: The event_type is set to `USER_UNCATEGORIZED`, `USER_CHANGE_PASSWORD`, `USER_RESOURCE_UPDATE_CONTENT`, `GROUP_MODIFICATION`, `or `STATUS_UPDATE` based on the presence of fields like `aname`, `bname`, `modifier`, `username`, `and hostname`, defaulting to `GENERIC_EVENT` if the conditions for these types are not met.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
