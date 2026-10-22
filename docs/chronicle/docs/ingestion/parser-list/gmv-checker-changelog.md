---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmv-checker-changelog/
title: Change log for GMV_CHECKER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:56.743171+00:00
---

# Change log for GMV_CHECKER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmv-checker-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GMV_CHECKER

Date | Changes  
---|---  
2025-11-07 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `description` raw log field(s) with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Changed mapping for `event.idm.read_only_udm.metadata.product_event_type` from `event_code` to `product_event_type` when the product_event_type raw field is available.  
\- The date parsing logic for the ts raw log field was refactored to handle multiple date formats with improved error handling and failover.  
\- Added Grok patterns to parse new patterns of logs.   
2024-08-27 |  Enhancement:  
\- When both `agent_hostname` and `atm_hostname` are not null, then mapped `atm_hostname` to `intermediary.hostname`.  
\- Added support for KV format logs.   
2024-03-13 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Mapped `user_disp_name` to `principal.user.user_display_name`.  
\- Mapped `user_role` to `principal.user.user_role`.  
\- If `field2` is present, then mapped `field2` to `principal.user.attribute.permission.description`.  
\- If value of the field `field2` is `R`, then set `principal.user.attribute.permission.type` to `DATA_READ`.  
\- If value of the field `field2` is `W`, then set `principal.user.attribute.permission.type` to `DATA_WRITE`.  
\- If `field3` is present, then mapped `field3` to `principal.user.attribute.permission.description`.  
\- If value of the field `field3` is `R`, then set `principal.user.attribute.permission.type` to `DATA_READ`.  
\- If value of the field `field3` is `W`, then set `principal.user.attribute.permission.type` to `DATA_WRITE`.   
2022-04-20 |  Bug - Removed host-specific condition.   
2022-03-28 |  Enhancement-Mapped the following fields:  
collected_timestamp, event_timestamp, host, type, Event type, ip, user, description.   
2022-03-23 |  Feature Request-Mapped agent_hostname to principal.hostname.  
Added mapping for a new unique log.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
