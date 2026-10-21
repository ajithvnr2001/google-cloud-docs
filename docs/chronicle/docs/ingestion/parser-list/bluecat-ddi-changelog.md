---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecat-ddi-changelog/
title: Change log for BLUECAT_DDI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:12:56.751060+00:00
---

# Change log for BLUECAT_DDI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecat-ddi-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BLUECAT_DDI

Date | Changes  
---|---  
2026-08-12 |  \- Added new grok patterns to support new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `dhcp_server` log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: When log contains `principal` and `target` machine details set event.idm.read_only_udm.metadata.event_type to NETWORK_CONNECTION and when only `principal` machine data is present set event.idm.read_only_udm.metadata.event_type to STATUS_UPDATE.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `principal_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pool_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2022-11-08 |  \- Added grok for newly ingested logs for log_type - `agetty`, `syslog-ng`, `systemd`.  
\- Added grok pattern for log_type - `named`, `systemd`, `CRON`, `agetty`, `syslog-ng` and it's respective mappings for the fields in the log_type mentioned above.   
2022-09-01 |  \- Modified `event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` to reduce generic percentage.   
2022-08-16 |  \- Added udm mapping  
`metadata.vendor_name` to `Bluecat Networks`  
`metadata.product_name` to `Bluecat DDI`  
2022-05-05 |  \- Added checks for query_type field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
