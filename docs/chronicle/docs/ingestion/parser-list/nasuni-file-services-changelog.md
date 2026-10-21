---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nasuni-file-services-changelog/
title: Change log for NASUNI_FILE_SERVICES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:48:36.122060+00:00
---

# Change log for NASUNI_FILE_SERVICES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nasuni-file-services-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NASUNI_FILE_SERVICES

Date | Changes  
---|---  
2025-03-24 |  \- Added support for `csv` format.  
\- event.idm.read_only_udm.section_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.section_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped `group_identifiers` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ipaddr` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- Added grok pattern in order to map `ipaddr` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields only if it is a valid IP.   
2022-08-21 |  \- Mapped `newpath` to `additional.fields`.   
2022-08-08 |  Enhancement:  
\- Added a Grok pattern to handle new SYSLOG logs.  
\- Added conditonal check for `event_type` `FILE_UNCATEGORIZED`.  
\- Added `event_type` `STATUS_UPDATE`  
\- Mapped `application` to `target.application`.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `proc_id` to `principal.process.pid`.   
2022-07-07 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
