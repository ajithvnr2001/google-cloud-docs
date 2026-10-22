---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-afm-changelog/
title: Change log for F5_AFM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:10.338034+00:00
---

# Change log for F5_AFM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-afm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_AFM

Date | Changes  
---|---  
2026-08-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `request_status` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` and `X_Forwarded_For` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `client_ip_geo_location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dest_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `client_request_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `virtual_server_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `bigip_mgmt_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `http_protocol_indication` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `http_protocol_info` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `errdefs_msgno` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `User_Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `http_request` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `support_id`, `profile_name`, `configuration_date_time`, `client_type`, `mobile_is_app`, `actual_mitigation_action_reason`, `actual_mitigation_action`, `enforced_by`, `context_type`, `route_domain`, `request_date_time`, `new_request_status`, `configured_mitigation_action_reason`, `class`, `bot_name`, `bot_signature_category`, `bot_signature`, `configured_mitigation_action`, `accept`, `Content_Type`, `context_name` and `Authorization` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-13 |  Enhancement:  
\- Modified the `drop` condition to allow processing of logs where the `process` field is `tmm4`.  
\- Added a grok pattern to extract `attackID` from the `msg_data` field when it's not available as a separate field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `attackID` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.   
2025-12-19 |  Enhancement:  
\- The `process` values `sflow_agent`, `pendsect`, and `sshd` are no longer explicitly dropped.  
\- Added a fallback mechanism to parse `log_msg` as Key-Value pairs if CSV parsing fails for generic messages.  
\- New grok patterns were added to handle additional log formats, extracting fields like `prod_event_type`, `prin_ip`, `tls_ver`, `cipher`.  
\- Logic added to populate kv_data from `log_msg` for processes `sshd(pam_audit)`, `httpd(pam_audit)`, and `rest(pam_audit)`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tls_ver` raw log field to `event.idm.read_only_udm.network.tls.version`.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `cipher` raw log field to `event.idm.read_only_udm.network.tls.cipher`.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `log_msg` raw log field to `event.idm.read_only_udm.security_result.summary` when `process` is `sshd`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `partition`, `level`, `tty`, `attempts`, `start`, `end` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Mapped `BLOCK` to `event.idm.read_only_udm.security_result.action` if `process` is `sshd` and `log_msg` contains `Authentication failure`.  
\- Conditional mapping applied to the `host` raw field: if it contains a valid IP address, `host` is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`. Otherwise, `host` is mapped to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.   
2025-11-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `fd`, `time_reopen`, `slice_info` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg_description`, `error_msg` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- If `msg_description` and `error_msg` both raw log fields present then `msg_description` will be mapped to `event.idm.read_only_udm.security_result.summary` and `error_msg` will be mapped to `event.idm.read_only_udm.security_result.description` UDM field.  
\- If `msg_description` raw log field is not present then `error_msg` will be mapped to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- The grok data type for `acl_rule_uuid` was changed from `DATA` to `INT`.  
\- The `date` filter was updated to support microsecond precision in timestamps.  
\- Log processing is now performed for `syslog-ng` and `systemd` process logs instead of being dropped.  
\- A trailing `a` character is now removed from the `log_msg` field before further processing.   
2025-10-06 |  Enhancement:  
\- Added grok pattern to parse new type of logs.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_hostname` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped `intermediary_pid` field with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `process` field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `internal_tag`,`src_zone`,`dest_zone`,`translated_dest_ip`,`translated_dest_port`,`translated_source_ip`,`translated_source_port`,`syslog_reporter_host`,`sa_translation_pool`,`sa_translation_type`,`translated_route_domain`,`send_to_vs` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `src_zone` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `dest_zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added conditional for when the log is KV format.   
2025-07-24 |  Enhancement:  
\- Added JSON filter to parse new type of logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `acl_policy_name`, `acl_policy_type`, `chronicle_log_type`, `chronicle_namespace`, `flow_id`, `vlan`, `route_domain`, and `partition_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `source_ipint_categories`, `src_geo`, and `source_fqdn` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dest_ipint_categories`, `dst_geo`, and `dest_fqdn` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `acl_rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `acl_rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.intermediary.ip : Newly mapped `bigip_mgmt_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `context_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `context_type` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `dest_ip` and `net.peer.ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dest_port` and `net.peer.port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `drop_reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `ip_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` and `net.host.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `source_port` and `net.host.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `errdefs_msg_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `errdefs_msgno` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `source_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `source_user_group` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_principal_user` is `true`.   
2025-07-10 |  Enhancement:  
\- Added include files of `cef_extraction.include` and `cef_udm_mapping.include` to parse the following `CEF` logs when `cef_data` =~ `CEF` and `message` =~ `CEF`.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` : Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` : Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels` : Newly mapped `c6a2`, `F5SrcZone`, and `F5SrcFqdn` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Newly mapped `F5SrcUser` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `c6a3`, `F5DstZone`, `F5DstVlan` and `F5DstFqdn` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `F5SendToVs`, `F5SrcIpiCategories`, and `F5DstIpiCategories` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-03 |  Enhancement:  
\- Removed `kernel`, `CROND` from the drop condition to parse the valid logs.  
\- Added syslog pattern to extract `cmd_line` from logs.  
\- Added syslog pattern to extract `module`, `tid` and `cpu` value from `msg_data` field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `module`, `tid` and `cpu` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `cmd_line` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.   
2025-06-10 |  Enhancement:  
\- Removed `tmsh`, `tmm1`, `mcpd` from the drop condition to parse the valid logs.  
\- Changed name of `dest_ip` to `target_ip`.  
\- Removed `target` rename block as it is not required.  
\- Modified Grok patterns to parse valid fields.  
\- Added a Grok pattern to parse the unparsed logs.  
\- Added a Grok pattern in `bigip_ip` to parse the valid data.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `msg_data` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `folder_path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `status` and `cmd_data` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field   
2025-03-21 |  Enhancement:  
\- Added Grok patterns to support new log formats.  
\- Removed `icrd_child` and `logger` from conditional check of drop tag.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `target_port` to `target.port`.  
\- Added conditional mapping for `protocol` to `network.ip_protocol` when the value is `TCP`.  
\- Mapped `ts2` to `metadata.event_timestamp`.  
\- Mapped `tls_ver` to `network.tls.version`.  
\- Mapped `cipher` to `network.tls.cipher`.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.  
\- Mapped `path` to `target.url`.  
\- Mapped `response_size` to `network.sent_bytes`.  
\- Mapped `received_size` to `network.received_bytes`.  
\- Mapped `usr` to `principal.user.userid`.  
\- Mapped `schema_version` to `target.resource.attribute.labels`.  
\- Mapped `severity_info` to `security_result.severity_details`.  
\- Mapped `target_pid` to `target.process.pid`.  
\- Mapped `additional1` to `additional.fields`.  
\- Mapped `dvc` to `intermediary.hostname`.  
\- Added a Grok pattern to match IP before mapping `bigip_ip` to `intermediary.ip`.  
\- Mapped `metadata.event_type` to `USER_UNCATEGORIZED` when `has_principal_user` is `true`.  
\- Mapped `prin_ip` to `principal.ip` and `principal.asset.ip`.   
2025-02-27 |  Enhancement:  
\- Added support for CEF format logs.  
\- Mapped `F5FlowID` to `additional.fields`.  
\- Mapped `F5TranslatedVlan` to `additional.fields`.  
\- Mapped `F5SrcTranslationType` to `additional.fields`.  
\- Mapped `F5SrcTranslationPool` to `additional.fields`.  
\- Mapped `F5SrcGeo` to `additional.fields`.  
\- Mapped `F5DstGeo` to `additional.fields`.  
\- Mapped `F5RouteDomain` to `additional.fields`.   
2024-11-07 |  Enhancement:  
\- Added support for CEF format logs.   
2024-04-05 |  Enhancement:  
\- Added support to parse newly ingested unparsed logs.   
2023-09-11 |  Enhancement:  
\- Mapped `Column12` to `security_result.detection_fields`.  
\- Mapped `Column14` to `security_result.action`.   
2023-08-16 |  Enhancement:  
\- Added Grok pattern to support new log formats.   
2023-05-05 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
