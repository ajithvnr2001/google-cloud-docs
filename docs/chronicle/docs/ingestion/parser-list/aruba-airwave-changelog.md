---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-airwave-changelog/
title: Change log for ARUBA_AIRWAVE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:43:56.818755+00:00
---

# Change log for ARUBA_AIRWAVE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-airwave-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARUBA_AIRWAVE

Date | Changes  
---|---  
2025-12-11 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.  
\- event.idm.read_only_udm.target.hostname: Newly mapped target_hostname raw log field with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped target_hostname raw log field with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped device_event_class_id, event_name_1 raw log fields with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped version raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped pid1 raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.intermediary.hostname and event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped inter_host raw log field with event.idm.read_only_udm.intermediary.hostname and event.idm.read_only_udm.intermediary.asset.hostname UDM field.   
2025-01-03 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `pid1` to `principal.process.pid`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `target_resource` to `target.resource.id`.  
\- Mapped `column3` to `additional.fields`.  
\- Mapped `column4` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `column6` to `target.resource.name`.   
2023-12-06 |  \- Added a Grok pattern to parse SYSLOG logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
