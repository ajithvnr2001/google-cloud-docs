---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/harness-io-changelog/
title: Change log for HARNESS_IO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:04.688819+00:00
---

# Change log for HARNESS_IO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/harness-io-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HARNESS_IO

Date | Changes  
---|---  
2025-04-16 |  \- Added a JSON block to handle single json logs.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `records.auditModule` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `auditModule` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `records.auditResource.type` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `auditResource.type` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `records.auditResource.identifier` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `auditResource.identifier` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `records.auditResourceScope.accountIdentifier` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `auditResourceScope.accountIdentifier` instead.  
\- event.idm.read_only_udm.metadata.product_event_type: Removed mapping of `records.auditAction` from `event.idm.read_only_udm.metadata.product_event_type` UDM field and mapped `auditAction` instead.  
\- event.idm.read_only_udm.network.http.method: Removed mapping of `records.auditHttpRequestInfo.requestMethod` from `event.idm.read_only_udm.network.http.method` UDM field and mapped `auditHttpRequestInfo.requestMethod` instead.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Removed mapping of `records.auditHttpRequestInfo.clientIP` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and mapped `auditHttpRequestInfo.clientIP` instead.  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `records.auditEventTime` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field and mapped `auditEventTime` instead.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `records.auditEventMetadata.batchId` from `event.idm.read_only_udm.additional.fields` UDM field and mapped `auditEventMetadata.batchId` instead.  
\- If has_principal` is `true` AND `has_user` is `true` then set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`  
\- If `has_principal` is `true` then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`  
\- Initialized `principal`, `target`, `metadata`, `extensions`, `network`, `additional` in the for loop.   
2025-02-05 |  \- Added support to parse the new log format.   
2024-10-17 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
