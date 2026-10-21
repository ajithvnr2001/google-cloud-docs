---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-switch-changelog/
title: Change log for ARUBA_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:26.379433+00:00
---

# Change log for ARUBA_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARUBA_SWITCH

Date | Changes  
---|---  
2026-07-27 |  Enhancement:  
\- Added Grok patterns to parse raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `internal_ts` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-06-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Notice-Type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `res_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `service` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `prin_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `source_file` and `server_type` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Remote-IP-Address` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Device-Name` and `target_hostname` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol_details` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `principal_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `url_details`,`mode_details`,`no_elements_copied`,`session_id_details`, `component`, `local_vid`, `peer_vid`, `function`, `flags`, `syslog_ver`, `msg_type`, `event_code`, `event_tag`, `link_status`, `Event-ID`, `Config-Method`, `terminal`, `ruser`, and `rhost` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `summary_details` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.collection_timestamp`: Newly mapped `time_data` raw log field with `event.idm.read_only_udm.metadata.collection_timestamp` UDM field.   
2026-01-16 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `dal_function`, `return_code`, `error_tag`, `internal_id`, `priority` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-02 |  Enhancement:  
\- Added grok patterns to parse new patterns of syslogs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `neighbor_chassis_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM with key `neighbor_chassis_id`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `neighbor_port_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field, using key `neighbor_port_id`.   
2025-10-29 |  Enhancement:  
\- Added grok patterns to parse new patterns of syslogs.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `prin_mac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `subscriber` raw log field to `event.idm.read_only_udm.additional.fields` as key `subscriber`.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `SSH` when the description contains `SSH`.   
2025-09-03 |  Enhancement:  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `event.idm.read_only_udm.security_result.summary` with `off-line` if the `status_msg` raw log field contains `off-line` else if the `status_msg` raw log field contains `on-line` then mapped with `on-line` else mapped with the value of `status_msg` raw log field.   
2025-08-28 |  Enhancement:  
\- Updated a Grok pattern to support new pattern of logs.  
\- Added Grok patterns to extract port information (`gen_port`) from `description` field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `gen_port` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-08-21 |  Enhancement:  
\- Added a Grok pattern to parse new pattern of logs.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_id`, `priority` and `facility` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified `sys_time` date pattern to support new pattern of timestamp.   
2025-05-26 |  Enhancement:  
\- Added grok patterns to support new pattern of SYSLOG logs.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- Changed `event_type` from `NETWORK_CONNECTION` to `STATUS_UPDATE` when target machine data is not available.  
\- Added support for new pattern of timestamp.  
\- Added a grok pattern to parse new pattern of description field.  
\- Modified the `if` condition for `user_id` raw_field.  
\- Removed the setting of `has_target` as `true`, if there is no target machine data.   
2024-11-14 |  Enhancement:  
\- Mapped `severity` to `security_result.severity`.   
2024-10-29 |  Enhancement:  
\- Modified grok pattern to parse `severity` and `amm` fields.   
2024-10-16 |  Enhancement:  
\- Added support for new format of SYSLOG logs.  
\- Changed mapping of `userid` from `principal.user.userid` to `target.user.userid`.  
\- Based on the log description, set `metadata.event_type` as `USER_LOGIN` or `USER_LOGOUT` or `NETWORK_CONNECTION`.  
\- Based on the log description, set `security_result.action` as `ALLOW` or `BLOCK`.   
2024-09-17 |  Enhancement:  
\- Added support for a new pattern of SYSLOG logs.   
2024-04-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
