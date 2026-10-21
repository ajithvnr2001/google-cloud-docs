---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyber-2-ids-changelog/
title: Change log for CYBER_2_IDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:33:40.527437+00:00
---

# Change log for CYBER_2_IDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyber-2-ids-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBER_2_IDS

Date | Changes  
---|---  
2025-09-04 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `DB`, `NewApps`, `UniqueApps`, `Computers`, `Duration` log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.about.application: Newly mapped `app_name` log field(s) with `event.idm.read_only_udm.about.application` UDM field.  
\- event.idm.read_only_udm.about.file.md5: Newly mapped `md5_value` log field(s) with `event.idm.read_only_udm.about.file.md5` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Newly mapped `app_version and md5_value` log field(s) with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip` log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `principal_ip` log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `Groups` log field(s) with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `hostname` log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `prod_event_type` log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- Refactored the mapping of detection fields and additional fields into security_result.detection_fields and additional.fields respectively, using a loop for dynamic processing.  
\- Added support for parsing timestamps that include Hebrew month names by converting them to numeric representations.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time1`, `monthnum`, `day`, `time2` log field(s) with event.idm.read_only_udm.metadata.event_timestamp UDM field.   
2024-11-28 |  \- Added a Grok pattern to parse new logs.   
2024-08-21 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
