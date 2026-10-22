---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-ctd-changelog/
title: Change log for CLAROTY_CTD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:57.514018+00:00
---

# Change log for CLAROTY_CTD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-ctd-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLAROTY_CTD

Date | Changes  
---|---  
2026-02-05 |  \- Added new grok patterns to extract fields from `msg`.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `reason` field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_address` field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip_address` field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true` and `has_target_hostname` is `true` or `has_target_resource` is `true` and `msg` contains `opened the session` or `connected` or `logged into` or `log into` or `connect` or `open the session`, updated to `USER_LOGIN`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true` and `has_target_hostname` is `true` or `has_target_resource` is `true` and `msg` contains `deleted`, updated to `RESOURCE_DELETION`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true` and `has_target_hostname` is `true` or `has_target_resource` is `true` and `msg` contains `modified`, updated to `SETTING_MODIFICATION`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true` and `has_target_user` is `true` and `msg` contains `enabled`, updated to `USER_CHANGE_PERMISSIONS`.   
2026-01-20 |  \- Added grok patterns to extract fields.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user1` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `user2` field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `server` field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cn3Label` and `cn3` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `update_values` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `groups` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `site`, `site_id` fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `disk_space_threshold_percent`, `partition`, `disk_usage_percent`, `disk_free_space`, `asset_name`, `type` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true and `msg` contains `disconnected the server` or `logged off` or `disconnected`, updated to `USER_LOGOUT`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true and `has_target_user` is true and msg contains `added user`, updated to `GROUP_MODIFICATION`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true or `has_target_user` is true, updated to `USER_UNCATEGORIZED`.   
2025-12-18 |  \- event.idm.read_only_udm.metadata.event_timestamp: Changed mapping for `event.idm.read_only_udm.metadata.event_timestamp` UDM field from `start` to `timestamp`(syslog header timestamp).  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `start` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field because the difference between the event and ingested timestamps should be minimal, with only a delay of a few seconds as expected.  
\- event.idm.read_only_udm.additional.fields: Mapped `start` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `ctdeventtype` is `Online Edit` AND `has_principal_device` is true AND `shost` is empty AND `smac` is empty, the event type is updated to `DEVICE_CONFIG_UPDATE`.  
\- The raw field `rt` is now used as a fallback to populate `event.idm.read_only_udm.metadata.event_timestamp` if the timestamp field is not available.   
2025-11-20 |  \- Added a grok pattern to parse `logging_device_name` and mapped it to `intermediary.hostname`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `CtdAlertsAreCreated`, `CtdScheduledBackups`, `CtdLicense`, `CtdCriticalServices`, `CtdInterfacesBitRate` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-10-09 |  \- `event.idm.read_only_udm.additional.fields`: Newly mapped `cn2`, `cn2Label` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-18 |  \- Added `threat_name` in state data by defining and initializing it at the beginning of the code.   
2024-12-04 |  \- Added additional mappings for logs when `eventclass` is `Event` , `Alert` , `HealthCheck` , and `Insight`.   
2024-11-13 |  \- Added Grok patterns to parse the hostname and the IP address from the syslog header and map it to `observer.hostname` and `observer.ip` respectively.  
\- Added support for unparsed logs.   
2024-10-07 |  \- Added support to parse new format of unparsed KV logs.   
2024-08-28 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
