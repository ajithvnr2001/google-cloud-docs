---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-changelog/
title: Change log for WORKDAY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:50.801283+00:00
---

# Change log for WORKDAY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKDAY

Date | Changes  
---|---  
2025-06-05 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `body.event.Actual_Completed_Date_and_Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field. Implemented a grok filter to parse the date and time string, and a date filter to map it to the timestamp.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `body.time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field. Implemented a date filter to parse the epoch time.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `body.event.Submitted_By` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `body.event.Integration_System` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `body.event.Integration_Event` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `body.event.Event_Type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `body.event.Integration_Event_Status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `body.event.Messages` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `body.event.Response_Message` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `body.event.Actual_Start_Date_and_Time`, `body.event.Scheduled_Start_Date_and_Time`, `body.event.By_Person`, `body.event.Sent_On`, `body.event.Items_Processed`, `body.event.Percent_Complete`, `body.event.Processing_Time`, `body.event.Total_Duration`, `body.event.Created_From_Trigger` and `body.event.Background_Process_Is_Running` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `target.user.userid` or `principal.user.userid` is present.   
2024-06-25 |  Enhancement:  
\- Added support for UDM event.  
\- Added a Grok pattern over `href` to extract the field `entity_host_name`.  
\- Mapped `entity_host_name` to `entity.entity.asset.hostname`.  
\- Mapped `href` to `entity.entity.url`.   
2024-06-24 |  Enhancement:  
\- Added support for the CSV logs.   
2022-09-15 |  \- Migrated to default parser.   
2022-05-11 |  \- Migrated to default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
