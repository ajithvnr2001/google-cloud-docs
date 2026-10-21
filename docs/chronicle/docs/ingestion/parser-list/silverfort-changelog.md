---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/silverfort-changelog/
title: Change log for SILVERFORT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:30:13.541841+00:00
---

# Change log for SILVERFORT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/silverfort-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SILVERFORT

Date | Changes  
---|---  
2026-04-06 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `server_name` log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `app` log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- Added a grok pattern on temp_data to extract timestamp, inter_host.   
2025-08-01 |  Enhancement:  
\- Removed unnecessary `gsub` function.  
\- Modified the parser to extract JSON from the `message_copy` field using a grok pattern.  
\- Refactored parser logic to extract data from `json_msg` field.  
\- Modified the `auth_count`field mapping to convert the value to string.   
2025-07-08 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id` and `auth_count` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `end_time` log fields with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `start_time` log fields with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `kind` log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `status`, `users.identifierType`, `users.type`, `mainEntities.identifierType` and `mainEntities.type` log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `users.displayName` log fields with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `users.identifier` log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `mainEntities.displayName` log fields with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `mainEntities.identifier` log fields with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `syslog_id` log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2023-12-11 |  Enhancement:  
\- Mapped `cs8`, `cs9`, `cs10`, `cs11`, and `cs12` to `additional.fields`.   
2023-11-29 |  Enhancement:  
\- Added mapping of `severity` to `security_result.detection_fields`.   
2023-10-11 |  Enhancement:  
\- Mapped `email`,`userid` to `target.user.email_addresses`,`target.user.userid`.  
\- When the `target` and `principal` are not present, set `metadata.event_type` to `GENERIC_EVENT`.   
2023-01-09 |  Bugfix-  
-Replaced `\"` with an empty string in the message.  
-Added not null check for cs3 and cs6 fields prior mapping to UDM.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
