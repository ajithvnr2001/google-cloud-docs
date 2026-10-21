---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microstrategy-changelog/
title: Change log for MICROSTRATEGY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:50:06.283638+00:00
---

# Change log for MICROSTRATEGY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microstrategy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSTRATEGY

Date | Changes  
---|---  
2025-03-21 |  Newly created parser.  
Mapped the following fields:  
\- Mapped `Event_start` to `metadata.event_timestamp`.  
\- Mapped `Hostname` to `principal.hostname, principal.asset.hostname`  
\- Mapped `Source_host` to `src.hostname, src.asset.hostname`  
\- Mapped `Source_server` to `principal.application`  
\- Mapped `PID` to `target.process.pid`  
\- Mapped `Thread_ID` to `target.resource.attribute.labels`  
\- Mapped `level` to `principal.platform_patch_level`  
\- Mapped `Log_level` to `security_result.detection_fields`  
\- Mapped `UID` to `target.user.userid`  
\- Mapped `SID` to `target.resource.attribute.labels`  
\- Mapped `OID` to `target.resource.id`  
\- Mapped `module` to `target.application`  
\- Mapped `method` to `target.resource.attribute.labels`  
\- Mapped `Authentication_message` to `metadata.description`  
\- Mapped `id` to `principal.user.userid`  
\- Mapped `server_ip` to `principal.ip, principal.asset.ip`  
\- Mapped `client_ip` to `target.ip, target.asset.ip`  
\- Mapped `Account_Name` to `principal.user.user_display_name`  
\- Mapped `Account_Login` to `principal.user.userid`  
\- Mapped `Account_Creation_Timestamp` to `event.idm.read_only_udm.additional.fields`  
\- Mapped `Account_Modification_Timestamp` to `event.idm.read_only_udm.additional.fields`  
\- Mapped `Account_Status_DESC` to `target.resource.attribute.labels`  
\- Mapped `Object_Owner_Name` to `target.resource.name`  
\- Mapped `User_Group_Name` to `principal.user.group_identifiers`  
\- Mapped `User` to `principal.user.user_display_name`  
\- Mapped `user` to `target.user.user_display_name`  
\- Mapped `Account` to `principal.user.userid`  
\- Mapped `Session` to `network.session_id`  
\- Mapped `Timestamp` to `event.idm.read_only_udm.additional.fields`  
\- Mapped `MICROSTRATEGY` to `metadata.vendor_name` and `metadata.product_name`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
