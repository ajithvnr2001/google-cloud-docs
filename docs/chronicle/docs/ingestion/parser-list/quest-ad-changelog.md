---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-ad-changelog/
title: Change log for QUEST_AD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:30.245341+00:00
---

# Change log for QUEST_AD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/quest-ad-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for QUEST_AD

Date | Changes  
---|---  
2025-08-13 |  Enhancement:  
\- Added gsub for `message` to parse the logs in proper format.  
\- Added gsub for `kv_data` to parse the logs in proper format.  
\- Added a grok pattern for `message` data field to parse new format of logs.  
\- Added new kv filter for `kv_data` field to parse the logs in proper format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp`.  
\- Modified the drop condition to drop logs only if `not_json` is true and `not_json_error` is true.  
\- Added conditional check for `Source_Network_Address` to not be empty, `N/A`, `null`, or `-`.  
\- Added conditional check for `Source_Port` to not be empty, `N/A`, `null`, or `-`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `ComputerName` raw log field with `event.idm.read_only_udm.target.user.userid` when `description` contains `logged on`.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `Environment` raw log field with `event.idm.read_only_udm.target.user.product_object_id` when `description` contains `logged on`.  
\- event.idm.read_only_udm.metadata.event_type: If `description` contains `logged on`, then set the `event.idm.read_only_udm.metadata.event_type` UDM field as USER_LOGIN.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `Logon_Process` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true, then set as USER_UNCATEGORIZED.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is true, then set as STATUS_UPDATE.   
2024-11-07 |  Enhancement:  
\- Added a Grok pattern to parse `suser` from the log.   
2024-10-21 |  Enhancement:  
\- Added support for new format logs.   
2024-02-09 |  \- Added support for JSON format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
