---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-router-changelog/
title: Change log for CISCO_ROUTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:46:19.548018+00:00
---

# Change log for CISCO_ROUTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-router-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ROUTER

Date | Changes  
---|---  
2026-07-08 |  Enhancement:  
\- Added Grok patterns to parse the raw log fields.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `sec_result_rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- Added support for the `HKT` timezone.   
2026-06-08 |  Enhancement:  
\- Replaced hardcoded timezone conversions with an include file `timezone.include` for dynamic timezone handling.  
\- Modified a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `numeric_intermediary_host` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac`: The value from `src_msg_mac` is now formatted before being mapped to `event.idm.read_only_udm.principal.mac`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tty_session` field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-03 |  Enhancement:  
\- Added new grok patterns to support additional log formats.  
\- Added support for the AEDT timezone by mapping it to the +1100 UTC offset.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `SN`, `P` and `C` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\-   
2026-01-20 |  Enhancement:  
\- Added new grok patterns to support additional log formats.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `dst_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.additional: Newly mapped `packet_count` raw log field with `event.idm.read_only_udm.additional` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2025-11-20 |  Enhancement:  
\- Added support for the IST timezone by mapping it to the +0530 UTC offset.   
2025-11-14 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `username` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- Added grok pattern to parse new format of syslog logs.  
\- Added a grok pattern in order to fetch `tar_user` from the `message_data` field.  
\- Set the event_type to `USER_LOGIN` when the log has login related events.   
2025-10-23 |  Enhancement:  
\- Added support for the event `FMANFP-6-IPACCESSLOGP` and relevant corresponding raw log fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `interface` and `packet_count` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `src_identifier` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `process` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `acl_name` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `status` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `seq_no` raw log field to `event.idm.read_only_udm.metadata.id` UDM field.   
2025-08-25 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `failed_user_id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `failed_client_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `failed_client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth_method` and `service_name` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `intermediary_host` raw log field to `event.idm.read_only_udm.principal.hostname` and event.idm.read_only_udm.principal.asset.hostname when mnemonics is `LOGIN_FAILED` or `AUTHN_FALLBACK`.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Mapped `inter_hostname` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when mnemonics is `LOGIN_FAILED` or `AUTHN_FALLBACK`.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Mapped `inter_hostname` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` when mnemonics is `LOGIN_FAILED` or `AUTHN_FALLBACK`.   
2025-07-17 |  Enhancement:  
\- Added a grok pattern to parse `intermediary.hostname`.  
\- Added grok pattern to parse `sum_data`.  
\- Added gsub to replace `\\r` with "".   
2025-06-05 |  Enhancement:  
\- Added Grok patterns to parse inter_host,src_ip,src_port,dst_ip,dst_port,user_name_,sc_description and packets.  
\- event.idm.read_only_udm.principal.port : Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field if `message_type` is equals to `DMI-5-AUTH_PASSED`.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip : Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field if `message_type` is equals to `DMI-5-AUTH_PASSED`.  
\- event.idm.read_only_udm.principal.user.userid : Newly mapped `user_name_` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field if `message_type` is equals to `DMI-5-AUTH_PASSED`.  
\- event.idm.read_only_udm.security_result.description : Newly mapped `sc_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.network.received_bytes : Newly mapped `packets` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.   
2025-05-26 |  Enhancement:  
\- Added a Grok pattern to parse intermediary hostname.  
\- `event.idm.read_only_udm.target.port` : Newly mapped `tar_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` : Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip` : Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol` : Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.port` : Newly mapped `src_ip_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.   
2025-04-21 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp : Handled new pattern of timestamps for event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `src_ip_msg` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Newly added multiple grok patterns in order to parse the logs with syslog format.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `NETWORK_CONNECTION` when owner `has_principal` and `has_target` are not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `STATUS_UPDATE` when owner `has_principal` is not null.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped event.idm.read_only_udm.metadata.event_type UDM field as `GENERIC_EVENT` when `has_principal` and `has_target` are null.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` : Newly mapped `src_ip_msg_data` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-03-06 |  Enhancement:  
\- Added support for SYSLOG logs.   
2025-02-26 |  Enhancement:  
\- Removed `intermediary.hostname` mapping if the value is numeric.   
2024-12-12 |  Enhancement:  
\- Mapped `intermediary_host` to `intermediary.hostname`.   
2024-12-05 |  Enhancement:  
\- Added a Grok pattern to support new pattern of syslog logs.  
\- Mapped `srcip` to `principal.ip`.   
2024-10-30 |  Enhancement:  
\- Added support for `metadata.event_timestamp` in `BST` timezone.   
2024-10-15 |  Enhancement:  
\- Mapped `inter_hostname` to `intermediary.ip` and `intermediary_host` to `intermediary.hostname`.   
2024-09-12 |  Enhancement:  
\- Added a Grok pattern to map `int_ip` to `intermediary.hostname`.   
2024-06-26 |  Enhancement:  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.   
2024-06-09 |  Enhancement:  
\- Mapped `hostname` from syslog header to `intermediary.hostname`.   
2024-05-20 |  Enhancement:  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.  
\- Mapped `MessageSourceAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `SourceModuleName` and `SourceModuleType` to `principal.resource.attribute.labels`.   
2023-11-10 |  Enhancement:  
\- Added new Grok patterns to parse failing SYSLOG logs.  
\- Added `Unable`, `exceeded`, and `No space left on device` conditions for `AUTH_VIOLATION`.   
2023-10-30 |  Enhancement:  
\- Added new Grok patterns to parse failing syslog logs.  
\- Mapped `resourcename` to `principal.resource.name`.  
\- Mapped `app_protocol` to `network.application.protocol`.  
\- Mapped `app` to `target.application`.  
\- Mapped `source_port` to `principal.port`.  
\- Mapped `source_ip` to `principal.ip`.  
\- Mapped `device_ip` to `target.ip`.  
\- Mapped `username` to `target.user.userid`.  
\- Mapped `intermediary_ip` to `intermediary.ip`.  
\- Mapped `mnemonics` to `metadata.event_type`.  
\- Mapped `sec_action` to `security_result.action`.  
\- Mapped `sec_category` `security_result.category`.  
\- Mapped `sec_summary` to `security_result.summary`.  
\- For authentication type logs, set `metadata.event_type` to `USER_LOGIN`.   
2023-05-09 |  Enhancement-  
\- Logs with value `FMANFP-6-IPACCESSLOGP` are parsed as `NETWORK_CONNECTION` events.   
2022-12-02 |  Enhancement-  
\- Added grok to support unparsed Syslog logs.  
\- If `principal.hostname` changed event_type mapping from GENERIC_EVENT to STATUS_UPDATE.   
2022-11-10 |  Enhancement-  
\- Added support for SYS-5-CONFIG_I event logs.  
\- Modified grok to support logs having timezone.   
2022-10-27 |  Enhancement-  
Parse following syslog fields of log type IOSXE-6-PLATFORM  
-Mapped `ip` to `intermediary.ip`  
-Mapped `src_ip` to `principal.ip`  
-Mapped `src_port` to `principal.port`  
-Mapped `dst_ip` to `target.ip`  
-Mapped `dst_port` to `target.port`  
-Mapped `protocol` to `network.ip_protocol`  
-Mapped `facility` to `principal.resource.type`  
-Mapped `mnemonics` to `metadata.product_event_type`  
-Mapped `sc_summary` to `metadata.description`  
-Mapped `sr_action` to `security_result.action`  
-Mapped `summary` to `security_result.summary`  
2022-08-23 |  Enhancement-  
-Corrected mapping of principal and target ip  
-Mapped `target_ip` to `event.idm.read_only_udm.target.ip`  
-Mapped `src_ip` to `event.idm.read_only_udm.principal.asset.ip`  
2022-07-01 |  Enhancement-  
Fixed an error to parse logs containing product_event_type as SYS-3-LOGGINGHOST_FAIL,SEC_LOGIN-5-LOGIN_SUCCESS,SYS-6-LOGGINGHOST_STARTSTOP,SYS-6-LOGOUT and timestamp is not present.  
Changed metadata.event_type of SYS-3-LOGGINGHOST_FAIL logs to STATUS_UPDATE from GENERIC_EVENT   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
