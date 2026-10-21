---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airwatch-changelog/
title: Change log for AIRWATCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:15:48.627851+00:00
---

# Change log for AIRWATCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/airwatch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AIRWATCH

Date | Changes  
---|---  
2025-06-05 |  Enhancement:  
\- Modified a grok pattern to parse raw log fields like `Application`,`AdminAccount`,`LocationGroup`,`AdminName`,`LoginSessionID`,`ApplicationType,`ApplicationBundle`,`UserSecurityType".  
\- event.idm.read_only_udm.target.application: Newly mapped `Application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `AdminAccount` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `LocationGroup` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `AdminName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `LoginSessionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ApplicationType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ApplicationBundle` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `UserSecurityType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Placed `FriendlyName` else if condition before `Device` else if condition.  
\- Added conditional checks before mapping `USER_CHANGE_PERMISSIONS` to `event.idm.read_only_udm.metadata.event_type` and `user` to `event.idm.read_only_udm.principal.user.userid`.   
2025-02-11 |  Enhancement:  
\- Added a Grok pattern to map `tuser` to `target.user.userid`.   
2024-12-12 |  Enhancement:  
\- Added condition checks and set `event_type` to `USER_LOGIN` when `vendor_action_category` closely matches to `Login`.  
\- Mapped `LoginSessionID` to `network.session_id`.  
\- Mapped `LoginAttemptNumber` to `additional.fields`.   
2024-11-15 |  Enhancement:  
\- Added Grok patterns for new types of logs.   
2024-10-17 |  Enhancement:  
\- Added support for new types of logs.   
2024-10-07 |  Enhancement:  
\- Added support for new type of logs.   
2024-09-23 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-06-25 |  Enhancement:  
\- Fixed the Grok pattern to map `username` to `principal.user.user_display_name`.  
\- Mapped `device_type` to `additional.fields`.  
\- Added the Grok patterns for new type of logs.   
2023-09-05 |  Bug Fix:  
\- Added a Grok pattern to parse dropped logs.   
2023-05-05 |  Bug Fix-  
\- Modified Grok pattern to parse dropped logs.   
2023-04-26 |  Bug Fix-  
\- Added support for different type of syslog formatted logs.   
2022-12-27 |  Bug Fix-  
\- Added support for different type of Syslog Format logs.  
\- Added specific conditional checks to handle multiple `event_name`.   
2022-09-02 |  Enhancement-  
\- Wrote grok to parse the unparsed ccf format logs.   
2022-06-29 |  Enhancement- Parsed log with event_name as `MergeGroupCompletedEvent`  
\- mapped `GroupManagementData` to `security_result.description`.  
\- mapped `EventSource`, `EventModule` to `event.idm.read_only_udm.additional.fields`.  
\- mapped `cat` to `security_result.category_details`.  
\- modified `event.idm.read_only_udm.metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` in case either of `principal.user.userid` or `target.user.userid` is present.   
2022-06-20 |  Enhancement- Event Category mapped to _udm.additional.fields(event_category)  
Added event type GENERIC_EVENT for SecurityInformation, SecurityInformationConfirmed(event_name) to handle unparsed logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
