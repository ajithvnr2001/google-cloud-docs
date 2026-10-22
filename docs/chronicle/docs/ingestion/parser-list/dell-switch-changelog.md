---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-switch-changelog/
title: Change log for DELL_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:46.000192+00:00
---

# Change log for DELL_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DELL_SWITCH

Date | Changes  
---|---  
2026-05-27 |  Enhancement:  
\- Added a new grok pattern to extract raw log fields.  
\- Modified a grok pattern to extract `inter_host` from the raw log.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source_file_description`, `message_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `tar_app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `tar_userid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Set `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL` when `severity` is `INFO` in the raw log.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` and `USER_LOGOUT` when necessary raw log fields are present.  
\- `event.idm.read_only_udm.extensions.auth.type`: Set `event.idm.read_only_udm.extensions.auth.type` to `MACHINE` for `USER_LOGIN` and `USER_LOGOUT` events.   
2026-01-29 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `reason_code` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a new grok pattern to parse logs containing `Reason Code`.   
2026-01-09 |  Enhancement:  
\- Added grok patterns to parse the raw log.  
\- `event.idm.read_only_udm.intermediary.hostname`, `event.idm.read_only_udm.intermediary.asset.hostname` : Newly mapped `inter_host` field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `application_task`,`sequence_number`,`MSTID` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new date format to map `datetime` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels` : Newly mapped `interface` field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-06-19 |  Enhancement:  
\- Added grok pattern to support for `SYSLOG` format.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `node` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `log_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `log_message` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2025-04-02 |  Enhancement:  
\- Added support for `JSON` format.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediate.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediate.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `proc_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly Mapped `error_detail` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `error_type` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `mac_address` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `hostname_string` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly Mapped `ipv6`, `ipv4` raw log fields with `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `ipv6`, `ipv4` raw log fields with `event.idm.read_only_udm.target.asset.ip`.   
2024-10-09 |  Enhancement:  
\- Added a Grok pattern to parse a new type of logs.  
\- Mapped `Eventid` to `metadata.product_log_id`.  
\- Mapped `Eventseverity` to `security_result.severity`.  
\- Mapped `Computer` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `Program` to `principal.application`.  
\- Mapped `Description` to `security_result.description`.   
2024-08-20 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.   
2024-04-25 |  Enhancement:  
\- Added Grok patterns to parse a new log type.  
\- Mapped `op` to `metadata.product_event_type`.  
\- Mapped `mac` to `principal.mac`.  
\- Mapped `addr` to `principal.ip`.  
\- Mapped `hostname` to `principal.ip`.  
\- Mapped `server_ip` to `principal.ip`.  
\- Mapped `server_port` to `principal.port`.  
\- Mapped `acct` to `principal.user.userid`.  
\- Mapped `target_ip` to `target.ip`.  
\- Mapped `local_ip` to `target.ip`.  
\- Mapped `local_port` to `target.port`.  
\- Mapped `File` to `target.file.full_path`.  
\- Mapped `target_host` to `target.hostname`.  
\- Mapped `target_user_id` to `target.user.userid`.  
\- Mapped `Server_ID` to `target.resource.product_object_id`.  
\- Mapped `tzknown`, `is_synced` and `exe` to `security_result.detection_fields`.  
\- Mapped `res` to `security_result.summary`.  
\- If value of the field `res` is "`, then mapped `status` to `security_result.summary".  
\- Mapped `uid`, `enterpriseId`, `auid`, `terminal`, `subj`, `grantors`, and `ID` to `principal.resource.attribute.labels`.   
2024-04-04 |  \- Added Grok patterns to parse new log type.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.  
\- Mapped `ip` to `principal.ip`.  
\- Mapped `dest_ip` to `target.ip`.  
\- Mapped `target_url` to `target.url`.  
\- Mapped `sec_description` to `security_result.description`.  
\- Mapped `action_details` to `security_result.action_details`.   
2024-01-04 |  \- Added Grok patterns for newly ingested logs.  
\- Added date block when `datetime` is in `SYSLOGTIMESTAMP` format.  
\- Mapped `softwareName` to `principal.asset.software.name`.  
\- Mapped `swVersion` to `principal.asset.software.version`.  
\- Mapped `port` to `principal_port`.  
\- Mapped `user` to `principal.user.userid` and set `metadata.event_type` to `USER_UNCATEGORIZED` when `user` is present.  
\- Mapped `application` to `principal.application`.  
\- Mapped `ip` to `principal.ip`.  
\- Set `sec_result.severity` to `INFORMATIONAL` when `severity` is `IFMGR-5-OSTATE_DN`.  
\- Mapped `msg` to `metadata.description`.   
2023-11-02 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
