---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wireless-changelog/
title: Change log for CISCO_WIRELESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:52:11.046092+00:00
---

# Change log for CISCO_WIRELESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-wireless-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_WIRELESS

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- Added new grok pattern to parse new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.target.mac`: Removed mapping of `target_mac` from `event.idm.read_only_udm.target.mac` since the MAC address represents the principal reporting device rather than the target.  
\- `event.idm.read_only_udm.principal.mac`: Mapped `target_mac` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- Renamed the field name from `description` to `desc` for better naming convention.  
\- Modified conditional logic for assigning `event.idm.read_only_udm.metadata.event_type` for events with mnemonic `PARSE_ERROR` to promote more accurate UDM categorization.   
2026-06-17 |  Enhancement:  
\- Added new grok pattern to parse logs with event_type `SEC_LOGIN-5-LOGIN_SUCCESS`.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field when `srcip` is not a valid IP.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.last_login_time`: Newly mapped `last_login_time` raw log field with `event.idm.read_only_udm.target.user.last_login_time` UDM field.   
2026-05-27 |  Enhancement:  
\- Modified `event.idm.read_only_udm.metadata.event_type` from `NETWORK_CONNECTION` to `STATUS_UPDATE` as previously it was wrongly flagged `has_target == `true`` for `event.idm.read_only_udm.target.mac` mapping.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `line` and `taskName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `cFile` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `wlc_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.   
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `target_port_1` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added new grok pattern to parse new pattern of SYSLOG logs.   
2026-04-03 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `mnemonic` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `urlHolder` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Added support for new date format for `event_ts` log field.  
\- Added a grok pattern to parse new format SYSLOG logs.   
2026-04-01 |  Enhancement:  
\- Added support for syslog format.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `ap_name` raw log field to `event.idm.read_only_udm.observer.hostname`.  
\- `event.idm.read_only_udm.observer.mac`: Newly mapped `bssid` raw log field to `event.idm.read_only_udm.observer.mac`.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `principal_mac_cisco` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `program` raw log field to `event.idm.read_only_udm.principal.process.file.names`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `uid` raw log field to `event.idm.read_only_udm.target.user.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `by_username` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `module_details` and `reason_1` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `module` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `by_uid` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `username` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `module_id` and `facility` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `device_type` raw log field to `event.idm.read_only_udm.target.resource.resource_subtype`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_name` raw log field to `event.idm.read_only_udm.principal.process.file.full_path`.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `chassis_id` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id`.   
2026-01-23 |  Enhancement:  
\- Added support for a new syslog header.  
\- Added support for the event `SISF-4-EXCESS_ARP_ACTIVITY` and relevant corresponding raw log fields.  
\- For `SISF-4-EXCESS_ARP_ACTIVITY` events, added a grok pattern to extract `obs_host`, `obs_desc`, `target_mac`, `summary`, and `description` from the message. The extracted `target_mac` is transformed into a standard MAC address format.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary` raw log field to `event.idm.read_only_udm.security_result.summary`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `description` raw log field to `event.idm.read_only_udm.security_result.description`.   
2025-12-22 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_sequence` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `syslog_sequence` from `event.idm.read_only_udm.principal.hostname` UDM field,as it was not the appropriate UDM for this field.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `syslog_sequence` from `event.idm.read_only_udm.principal.asset.hostname` UDM field,as it was not the appropriate UDM for this field.  
\- A new grok pattern has been introduced to accommodate an additional log format.   
2025-12-05 |  Enhancement:  
\- Handled timestamps with the IST timezone by converting them to a UTC offset  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `principal_mac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `obs_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.observer.labels: Newly mapped `obs_desc` raw log field with `event.idm.read_only_udm.observer.labels` UDM field.   
2025-11-27 |  Enhancement:  
\- Added grok patterns to parse new pattern of syslog logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_sequence` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `addr`, `component_status`, `ecc`, `multipleErrorsDetected`, `rep[0]`, `rep[1]`, `rep[2]`, `suppressed_times`, `valid`, `interface` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- Added KV filter to parse the `kv_data` field.   
2025-07-08 |  Enhancement:  
\- Added grok pattern to parse unparsed fields.  
\- Updated `event.idm.read_only_udm.metadata.event_type` from `STATUS_UPDATE` to `NETWORK_CONNECTION`.  
\- Updated `event.idm.read_only_udm.metadata.event_type` from `USER_RESOURCE_ACCESS` to `STATUS_UPDATE`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.detection_fields` to utilize a generalized map for fields `certificate`, `expiry_date`, `interface`, `auth_failure_reason`, `failure_reason`, `ssid`, `xid`, `slot`, `current_version`, `latest_version`.  
\- Removed redundant mapping of `event.idm.is_significant`, `event.idm.is_alert`, `security_result.category`, `security_result.action`, `security_result.summary`, `event.idm.read_only_udm.network.ip_protocol`, `event.idm.read_only_udm.metadata.event_type`.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.mac` and used common field `target_mac` and mapped it to `event.idm.read_only_udm.target.mac`.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.port` and used common field `target_port` and mapped it to `event.idm.read_only_udm.target.port`.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.ip` and used common field `target_ip` and mapped it to `event.idm.read_only_udm.target.ip`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.mac` and used common field `principal_mac` and mapped it to `event.idm.read_only_udm.principal.mac`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.port` and used common field `principal_port` and mapped it to `event.idm.read_only_udm.principal.port`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.ip` and used common field `principal_ip` and mapped it to `event.idm.read_only_udm.principal.ip`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.hostname` and used common field `principal_hostname` and mapped it to `event.idm.read_only_udm.principal.hostname`.  
\- Removed redundant code for field `wlc_controller`.   
2025-04-15 |  Enhancement:  
\- Added Gsub to replace `\\n` with ` ` on `message` to parse the logs.  
\- Added GROK patterns to parse new pattern of syslog logs.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname,event.idm.read_only_udm.target.asset.hostname: Removed mapping of `wlc_controller` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `mnemonic`is `USER_NAME_CREATED` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Mapped `wlc_controller` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field when `mnemonic` is `USER_NAME_CREATED` in include file `cisco_wireless.include`.  
\- Added GROK patterns to parse dropped logs when `mnemonic` is `RADIUS_IN_GLOBAL_LIST` in include file `cisco_wireless.include`.  
\- Added `else if` conditional check when `mnemonic` is `CLIENT_MOVED_TO_RUN_STATE` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip_1` raw log field with `event.idm.read_only_udm.principal.ip` UDM field when `mnemonic` is `CLIENT_MOVED_TO_RUN_STATE` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip_2` raw log field with `event.idm.read_only_udm.principal.ip` UDM field when `mnemonic` is `CLIENT_MOVED_TO_RUN_STATE` in include file `cisco_wireless.include`.  
\- Added `else if` conditional check when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac1` raw log field with `event.idm.read_only_udm.principal.mac` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac2` raw log field with `event.idm.read_only_udm.principal.mac` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `slot` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ssid` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- event.idm.read_only_udm.metadata.event_type: if `has_principal_user` is true set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`, else if `has_principal` is true set it to `STATUS_UPDATE` otherwise set it to `GENERIC_EVENT` when `mnemonic` is `AUTHENTICATION_TRAP` in include file `cisco_wireless.include`.  
\- Added `on_error` when mapping `ap_mac` to `event.idm.read_only_udm.target.mac` in include file `cisco_wireless.include`.   
2024-09-25 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2024-05-28 |  Enhancement -  
\- Mapped `MessageSourceAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `SourceModuleName` and `SourceModuleType` to `principal.resource.attribute.labels`.  
\- Mapped `intermediary_hostname` to `intermediary.hostname`.   
2024-03-18 |  Enhancement -  
\- Added new Grok patterns to support new pattern of syslog logs.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `client_host`, and `hostname` to `principal.hostname`.  
\- Mapped `client_ip` to `principal.ip`.  
\- Mapped `client_mac` to `principal.mac`.  
\- Mapped `ap_ip` to `target.ip`.  
\- Mapped `ap_mac` to `target.mac`.  
\- Mapped `messageToProcess` and `description` to `metadata.description`.  
\- Mapped `inter_url` to `intermediary.url`.  
\- Mapped `inter_ip` to `intermediary.ip`.  
\- Mapped `sec_desc` to `security_result.description`.  
\- Mapped `latest_version`, `current_version`, `certificate`, `expiry_date`, `clostest_sensor`, `ssid`, `client`, `xid`, `failure_reason`, `auth_failure_reason`, and `interface` to `security_result.detection_fields`.  
\- Aligned mappings for `principal.hostname` and `principal.asset.hostname`.  
\- Aligned mappings for `target.hostname` and `target.asset.hostname`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.  
\- Mapped `action_data` to `security_result.acion_details`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `vendor`, and `RSSI` to `principal.resource.attribute.labels`.  
\- Mapped `vendor`, `security_setting`, `channel`, `protocol`, and `RSSI` to `target.resource.attribute.labels`.   
2024-01-10 |  Enhancement -  
\- Added Grok patterns to parse newly ingested unparsed logs.  
\- Handled logs when the value of `mnemonic` is not null and the value is `SEC_LOGIN-5-LOGIN_SUCCESS` and `CRL_LDAP_QUERY`.  
\- Mapped `msg1` to `metadata.description`.  
\- Mapped `messageToProcess` to `metadata.description`.   
2023-02-09 |  Enhancement -  
\- Supported new logs which has field `PARSE_ERROR`.  
\- Added grok pattern to support new logs.   
2022-09-08 |  Fix -  
\- Corrected a typo error: On line 1239 in include file added comment marker `#` proceeding to the word `security`.   
2022-08-22 |  Enhancement  
\- Moved customer specific parser changes to default parser  
\- Added grok patterns to parse the drop logs  
\- Removed drop tags to enhance the parser  
\- Changed the field mapping of `event.idm.read_only_udm.metadata.event_type` from `GENERIC_EVENT` to `STATUS_UNCATEGORIZED` and `STATUS_UPDATE`  
\- Mapped `messageToProcess` field to `event.idm.read_only_udm.metadata.description`  
\- Mapped `src_ip` field to `event.idm.read_only_udm.principal.ip`  
\- Mapped `wlc_controller` to `event.idm.read_only_udm.principal.hostname`  
\- Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
