---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avaya-aura-changelog/
title: Change log for AVAYA_AURA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:14.958885+00:00
---

# Change log for AVAYA_AURA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avaya-aura-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AVAYA_AURA

Date | Changes  
---|---  
2026-07-09 |  Enhancement:  
\- Added new grok patterns to parse new format of Syslog logs.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `UID`, `target_id` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `group_display_name` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `target_file` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `GID`, `home` and `shell` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PASSWORD` when event_name is `change user` and target machine data is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `USER_CREATION` when event_name is `new user` and user, principal and target machine data is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `FILE_SYNC` when target related file and principal machine data is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `GROUP_MODIFICATION` when user, principal and target machine data is present.   
2026-06-17 |  Enhancement:  
\- Added new grok patterns to parse new format of Syslog logs.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `received_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `file_size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.   
2026-05-11 |  Enhancement:  
\- Added a new grok pattern to parse new format of logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `principal_application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `network_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `application_protocol_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.community_id`: Newly mapped `community_id` raw log field with `event.idm.read_only_udm.network.community_id` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `security_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device_uptime`, `cmg_trap_subsystem`, `cmg_trap_onboard`, `cmg_trap_location` and `syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2022-12-30 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
