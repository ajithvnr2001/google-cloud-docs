---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-user-activity-changelog/
title: Change log for WORKDAY_USER_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:50.563313+00:00
---

# Change log for WORKDAY_USER_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/workday-user-activity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WORKDAY_USER_ACTIVITY

Date | Changes  
---|---  
2026-05-21 |  Enhancement:  
\- Added a grok pattern on `systemAccount` to extract `principal_id` and `system_account_target_id`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `system_account_target_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.   
2026-05-07 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `requestTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `activityAction` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `systemAccount` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `taskDisplayName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `target.id` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `target.id`, `desc` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `taskId` from `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `taskId` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Removed mapping of `device` from `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `device` from `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.principal.asset.category`: Newly mapped `device` raw log field to `event.idm.read_only_udm.principal.asset.category` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Removed mapping of `hostname` from `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.user.title`: Removed mapping of `title` from `event.idm.read_only_udm.target.user.title` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `hostname` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `activityAction` is `READ`, `DOWNLOAD`, or `OTHER`, updated to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `activityAction` is `WRITE`, updated to `USER_RESOURCE_UPDATE_CONTENT`.  
\- Updated `event.idm.read_only_udm.metadata.vendor_name` to `Workday` and `event.idm.read_only_udm.metadata.product_name` to `Workday User Activity`.  
\- `event.idm.read_only_udm.target.application`: Set `event.idm.read_only_udm.target.application` UDM field to `Workday`.   
2025-10-03 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `Sign-on_Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `Sign-on_Time` raw log with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `Role` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `User_Name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `awaiting_details` raw log field with `event.idm.read_only_udm.additional.fields` UDM field only when it contains `Approval` or `activities`.   
2025-02-20 |  Enhancement:  
\- Added support to parse the unparsed logs.   
2024-09-05 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
