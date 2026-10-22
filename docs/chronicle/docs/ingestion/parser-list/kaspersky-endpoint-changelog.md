---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-endpoint-changelog/
title: Change log for KASPERSKY_ENDPOINT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:39.516633+00:00
---

# Change log for KASPERSKY_ENDPOINT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-endpoint-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KASPERSKY_ENDPOINT

Date | Changes  
---|---  
2025-09-18 |  \- Added support to parse the kvdata to appropriate UDM fields which were earlier mapped to `metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `Eventtype` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Removed mapping of `ipAddress` from `event.idm.read_only_udm.principal.ip` in order to map it to the respective UDM fields  
\- event.idm.read_only_udm.principal.asset.ip: Removed mapping of `ipAddress` from `event.idm.read_only_udm.principal.asset.ip` in order to map it to the respective UDM fields  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Removed mapping of `objectName` from `event.idm.read_only_udm.principal.process.file.full_path` UDM field and mapped `Objectname` instead.  
\- event.idm.read_only_udm.target.file.full_path: Removed mapping of `pathToObject` from `event.idm.read_only_udm.target.file.full_path` UDM field and mapped `Pathtoobject` instead.  
\- event.idm.read_only_udm.security_result.summary: Removed mapping of `resultDescription` from `event.idm.read_only_udm.security_result.summary` UDM field and mapped `Resultdescription` instead.  
\- event.idm.read_only_udm.principal.process.pid: Removed mapping of `processID` from `event.idm.read_only_udm.principal.process.pid` UDM field and mapped `ProcessID` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `FileName` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `Name` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `applicationPath` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `Applicationpath` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `objectType` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `Objecttype` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `resultDescription` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `Resultdescription` instead.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `ResultOperation` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `Encryptiontype` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `DevicetypeBustype` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `Authenticationtype` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `SSID` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `Devicecategory` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `DeviceID` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `ResultDecision` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `ResultDecision` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.   
2025-02-12 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
