---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-gateway-changelog/
title: Change log for SAP_GATEWAY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:13:58.087487+00:00
---

# Change log for SAP_GATEWAY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-gateway-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_GATEWAY

Date | Changes  
---|---  
2026-04-01 |  Enhancement:  
\- Added new grok patterns and modified existing grok patterns to parse different SYSLOG log formats.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `convid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `req_length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `length`, `bytes_sent` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `lu` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `conn`, `act`, `packages`, `sender`, `type`, `hdl`, `id`, `signal`, `ACTION`, `LOGFILE`, `config_value`, `version`, `secinfo_lines`, `log_severity_indicator_2`, `DEST`, `SOURCE`, `CANCEL`, `ACCESS`, `config_setting`, `new_value`, `result_action`, `mode` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: If the grok on `USER-HOST` fails then mapped `USER-HOST` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-24 |  Enhancement:  
\- Added Grok patterns to parse new SYSLOG and SYSLOG+KV log formats.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp_1`, `year` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_hostname`, `HOST` field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application` field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `MODULE`, `result_filename` field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `VERSION` field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `partner_ip`, `addr` field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `action_value` field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `partner_port` field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `local_ip`, `ip_address_1`, `ip_address_2` field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `local_port`, `PORT` field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `ERROR` field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary` field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `hostname` field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `server_ciphersuites` field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `platform_tag` field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `platform_tag`, `operation`, `host_address_1`, `host_address_2`, `features`, `SECUDIR`, `client_tls_versions`, `build_information`, `initialised_library` field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.network.tls.client.supported_ciphers: Newly mapped `client_cipher`, `client_ciphersuites` field with `event.idm.read_only_udm.network.tls.client.supported_ciphers` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `key1`, `value_1`, `key2`, `value_2`, `key3`, `value_3`, `key4`, `value_4`, `segment_name`, `memory_address`, `allocation_details`, `total_size_bytes`, `module`, `component`, `capacity`, `context`, `source_module_name`, `log_identifier`, `ciphersuites` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `etd_event_sender_ssl_config`, `SECUDIR_environment_variable_status`, `TLS_extension_status`, `crypto_kernel_status`, `function_status`, `gateway_admin_status`, `gw_status` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `user_env_variables` field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `server_info`, `server_tls_versions`, `client_info`, `client_pvflags` field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If both principal and target information are present then set to `NETWORK_CONNECTION`.  
\- Added gsubs to remove `\r\n`, `\\"` and to convert logs into KV format to properly parse the raw logs.   
2026-01-13 |  \- Newly created parser.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `TP` raw log field with `event.idm.read_only_udm.principal.application` UDM field if `event_action` is not `secinfo`  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `TP` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field if `event_action` is `secinfo`  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname`, `hostname1` field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_address`, `ip_address1` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field if `event_action` is `secinfo`  
\- event.idm.read_only_udm.target.ip: Newly mapped `ip_address` raw log field with `event.idm.read_only_udm.target.ip` UDM field if `event_action` is `secinfo`  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `USER` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `message1`, `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `parameter` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result: Newly mapped `security_result` raw log field with `event.idm.read_only_udm.security_result` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_severity_indicator`, `event_action`, `old_kv.ACTION`, `old_kv.LOGFILE`, `old_kv.MAXSIZEKB`, `old_kv.SWITCHTF`, `new_kv.ACTION`, `new_kv.LOGFILE`, `new_kv.MAXSIZEKB`, `new_kv.SWITCHTF`, `sap_host_context`, `old_max_connection_setup_time`, `new_max_connection_setup_time`, `signal_name`, `signal_action`, `level` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `SAP_GATEWAY` static value with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `SAP` static value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true` and has_target_process is `true`, `updated to `PROCESS_LAUNCH`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is `true`, `updated to `USER_UNCATEGORIZED`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true`, `updated to STATUS_UPDATE. Otherwise`, updated to `GENERIC_EVENT`.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `thread_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
