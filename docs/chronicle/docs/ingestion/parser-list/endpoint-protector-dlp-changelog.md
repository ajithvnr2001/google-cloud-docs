---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/endpoint-protector-dlp-changelog/
title: Change log for ENDPOINT_PROTECTOR_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:13:48.730675+00:00
---

# Change log for ENDPOINT_PROTECTOR_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/endpoint-protector-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ENDPOINT_PROTECTOR_DLP

Date | Changes  
---|---  
2025-09-26 |  \- `event.idm.read_only_udm.additional.fields`: Newly mapped `Date/Time(Server)`, `Date/Time(Client)`, `Date/Time(Server UTC)`, `Date/Time(Client UTC)` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `epp_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.observer.hostname` UDM field.  
\- Added Grok patterns and json filter in order to parse new format logs.   
2025-09-21 |  Enhancement:  
\- Added Grok pattern to support new pattern of logs.  
\- event.idm.read_only_udm.metadata.ingestion_labels: Removed `Destination`, and `Matched Item` raw log fields from `event.idm.read_only_udm.metadata.ingestion_labels` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `Destination` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `Matched Item` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `server_date`, `client_date`, `server_date_utc`, `client_date_utc` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `OS` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `SCAN_UNCATEGORIZED` if `has_principal` is `true` else set to `GENERIC_EVENT`.   
2023-04-17 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
