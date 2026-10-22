---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-fusion-changelog/
title: Change log for ORACLE_FUSION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:25.724664+00:00
---

# Change log for ORACLE_FUSION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-fusion-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ORACLE_FUSION

Date | Changes  
---|---  
2026-07-17 |  \- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Events.eventData.userInternalName`, `userInternalName` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Events.eventData.userName`, `userName` raw log fields with `event.idm.read_only_udm.principal.user.user_display_name` UDM field  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `Events.eventData.description`, `description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Events.eventData.date`, `date` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Events.eventData.type`, `Events.eventData.eventType`, `eventType` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail.attributeInternalName`, `detail.attribute`, `detail.newValue`, `attributeInternalName`, `attribute`, `newValue` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Events.eventData.eventCategory`, `eventCategory` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field  
\- Added support for a new log format where event fields are at the root level.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when the log has user data.  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when the log has principal machine data.   
2024-10-18 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
