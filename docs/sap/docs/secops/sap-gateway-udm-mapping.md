---
url: https://docs.cloud.google.com/sap/docs/secops/sap-gateway-udm-mapping/
title: SAP Gateway UDM mapping \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:28.908152+00:00
---

# SAP Gateway UDM mapping  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/sap-gateway-udm-mapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  SAP Gateway UDM mapping Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The `SAP_GATEWAY` parser monitors access and activities within the SAP Gateway, reflecting communication between external applications and SAP systems.

For information about Google SecOps for SAP, see [Secure SAP applications with Google SecOps](https://docs.cloud.google.com/sap/docs/secops/overview).

## Field mapping reference

The following table describes the mapping between SAP Gateway log fields and Google SecOps UDM fields.

Log field | UDM mapping | Logic  
---|---|---  
`timestamp` | `event.idm.read_only_udm.metadata.event_timestamp` | Initially empty, combined date/time string, then parsed to `event_timestamp`.  
`weekday` | (none) | Day of the week extracted from the log message, used for timestamp parsing.  
`month` | (none) | Month extracted from the log message, used for timestamp parsing.  
`month_day` | (none) | Day of the month extracted from the log message, used for timestamp parsing.  
`year` | (none) | Year extracted from the log message, used for timestamp parsing.  
`time` | (none) | Time extracted from the log message, used for timestamp parsing.  
`description` | `event.idm.read_only_udm.metadata.description` | General description field, often populated from grok.  
`event_action` | `event.idm.read_only_udm.additional.fields` | Key "event_action", value from original `event_action`.  
`parameter` | `event.idm.read_only_udm.target.resource.name` | Parameter associated with the event action.  
`old_kv` | (none) | Source for key-value extraction.  
`new_kv` | (none) | Source for key-value extraction.  
`kv_data` | (none) | General key-value data extracted from the log, used to extract other fields like `HOST`, `USER-HOST`.  
`security_result` | `event.idm.read_only_udm.security_result` | Holds security-related outcomes.  
`TP` | `event.idm.read_only_udm.principal.application`  
OR  
`event.idm.read_only_udm.target.process.file.full_path` | Transaction Program name or Process ID. Mapping depends on `event_action`:  
\- Mapped to `principal.application` if `event_action` is NOT "secinfo".  
\- Mapped to `target.process.file.full_path` if `event_action` is "secinfo".  
`hostname` | `event.idm.read_only_udm.principal.hostname`  
OR  
`event.idm.read_only_udm.target.hostname` | Hostname extracted from `HOST` field. Mapping depends on `event_action`:  
\- Mapped to `principal.hostname` if `event_action` contains "reginfo".  
\- Mapped to `target.hostname` if `event_action` contains "secinfo".  
`ip_address` | `event.idm.read_only_udm.principal.ip`  
OR  
`event.idm.read_only_udm.target.ip` | IP address extracted from `HOST` field. Mapping depends on `event_action`:  
\- Mapped to `principal.ip` if `event_action` contains "reginfo".  
\- Mapped to `target.ip` if `event_action` contains "secinfo".  
`action` | `event.idm.read_only_udm.security_result.action_details` | Specific action within the event (e.g., accepted, denied).  
`security_result_action` | `event.idm.read_only_udm.security_result.action` | Security result action, derived from the `action` field (ALLOW/BLOCK).  
`USER` | `event.idm.read_only_udm.principal.user.userid` | User ID extracted from `USER-HOST` field.  
`hostname1` | `event.idm.read_only_udm.principal.hostname` | Hostname extracted from `USER-HOST` field.  
`ip_address1` | `event.idm.read_only_udm.principal.ip` | IP address extracted from `USER-HOST` field.  
`sap_host_context` | `event.idm.read_only_udm.additional.fields` | Key "sap_host_context", value from original `sap_host_context`.  
`old_max_connection_setup_time` | `event.idm.read_only_udm.additional.fields` | Key "old_max_connection_setup_time", value from original field.  
`new_max_connection_setup_time` | `event.idm.read_only_udm.additional.fields` | Key "new_max_connection_setup_time", value from original field.  
`signal_name` | `event.idm.read_only_udm.additional.fields` | Key "signal_name", value from original `signal_name`.  
`signal_action` | `event.idm.read_only_udm.additional.fields` | Key "signal_action", value from original `signal_action`.  
`level` | `event.idm.read_only_udm.additional.fields` | Key "level", value from original `level`.  
`log_severity_indicator` | `event.idm.read_only_udm.additional.fields` | Key "log_severity_indicator", value from original `log_severity_indicator`.  
`message1` | `event.idm.read_only_udm.metadata.description` | Holds the main message content after initial grok.  
`thread_id` | `event.idm.read_only_udm.principal.process.pid` | Thread ID extracted from the log.  
`has_target_process` | (none) | Boolean flag indicating if target process information is present. Used for `event_type` logic.  
`has_principal` | (none) | Boolean flag indicating if principal information is present. Used for `event_type` logic.  
`has_target` | (none) | Boolean flag indicating if target information is present.  
`has_principal_user` | (none) | Boolean flag indicating if principal user information is present. Used for `event_type` logic.  
`HOST` | (none) | Raw field from KV on `kv_data`, contains host and IP info. Parsed to `hostname`, `ip_address`.  
`USER-HOST` | (none) | Raw field from KV on `kv_data`, contains user and host/IP info. Parsed to `USER`, `hostname1`, `ip_address1`.  
`old_kv.ACTION` | `event.idm.read_only_udm.additional.fields` | Key "old_ACTION", value from original `old_kv.ACTION`.  
`old_kv.LOGFILE` | `event.idm.read_only_udm.additional.fields` | Key "old_LOGFILE", value from original `old_kv.LOGFILE`.  
`old_kv.MAXSIZEKB` | `event.idm.read_only_udm.additional.fields` | Key "old_MAXSIZEKB", value from original `old_kv.MAXSIZEKB`.  
`old_kv.SWITCHTF` | `event.idm.read_only_udm.additional.fields` | Key "old_SWITCHTF", value from original `old_kv.SWITCHTF`.  
`new_kv.ACTION` | `event.idm.read_only_udm.additional.fields` | Key "new_ACTION", value from original `new_kv.ACTION`.  
`new_kv.LOGFILE` | `event.idm.read_only_udm.additional.fields` | Key "new_LOGFILE", value from original `new_kv.LOGFILE`.  
`new_kv.MAXSIZEKB` | `event.idm.read_only_udm.additional.fields` | Key "new_MAXSIZEKB", value from original `new_kv.MAXSIZEKB`.  
`new_kv.SWITCHTF` | `event.idm.read_only_udm.additional.fields` | Key "new_SWITCHTF", value from original `new_kv.SWITCHTF`.  
`(event_type logic)` | `event.idm.read_only_udm.metadata.event_type` | Determined based on `has_principal`, `has_target_process`, `has_principal_user` flags.  
`(hardcoded)` | `event.idm.read_only_udm.metadata.product_name` | Hardcoded to "SAP_GATEWAY".  
`(hardcoded)` | `event.idm.read_only_udm.metadata.vendor_name` | Hardcoded to "SAP".  
`timestamp_1` | `event.idm.read_only_udm.metadata.event_timestamp` | Parsed from `SYSLOGTIMESTAMP` and year.  
`MODULE` | `event.idm.read_only_udm.principal.process.file.full_path` |   
`VERSION` | `event.idm.read_only_udm.metadata.product_version` |   
`partner_ip` | `event.idm.read_only_udm.target.ip` | Extracted from `DETAIL`.  
`partner_port` | `event.idm.read_only_udm.target.port` | Extracted from `DETAIL`.  
`local_ip` | `event.idm.read_only_udm.principal.ip` | Extracted from `DETAIL`.  
`local_port` | `event.idm.read_only_udm.principal.port` | Extracted from `DETAIL`.  
`ERROR` | `event.idm.read_only_udm.security_result.description` |   
`summary` | `event.idm.read_only_udm.security_result.summary` | GwDisconnectClient, client disconnected (403)  
`addr` | `event.idm.read_only_udm.target.ip` |   
`server_ciphersuites` | `event.idm.read_only_udm.network.tls.cipher` | 135:PFS:HIGH::EC_P256:EC_HIGH  
`platform_tag` | `event.idm.read_only_udm.principal.platform` | Mapped to WINDOWS, LINUX, or MAC based on content. Also added to `principal.resource.attribute.labels`.  
`client_cipher` | `event.idm.read_only_udm.network.tls.client.supported_ciphers` | Merged.  
`client_ciphersuites` | `event.idm.read_only_udm.network.tls.client.supported_ciphers` | Merged.  
`PORT` | `event.idm.read_only_udm.principal.port` |   
`HOST (if grok fails)` | `event.idm.read_only_udm.principal.hostname` |   
`result_filename` | `event.idm.read_only_udm.principal.process.file.full_path` |   
`user_id` | `event.idm.read_only_udm.principal.user.userid` |   
`key1, value_1` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array.  
`key2, value_2` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array.  
`key3, value_3` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array.  
`key4, value_4` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array.  
`segment_name` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`memory_address` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`allocation_details` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`total_size_bytes` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`module` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`operation` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Dynamic key/value from item array, key includes index.  
`component` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`capacity` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index (as `entries_capacity`).  
`context` | `event.idm.read_only_udm.additional.fields` | Dynamic key/value from item array, key includes index.  
`ip_address_1` | `event.idm.read_only_udm.principal.ip` | Merged.  
`ip_address_2` | `event.idm.read_only_udm.principal.ip` | Merged.  
`SYSTEM_CALL` | `event.idm.read_only_udm.additional.fields` | Key "SYSTEM_CALL"  
`line_number` | `event.idm.read_only_udm.additional.fields` | Key "line_number"  
`LINE` | `event.idm.read_only_udm.additional.fields` | Key "LINE"  
`COUNTER` | `event.idm.read_only_udm.additional.fields` | Key "COUNTER"  
`TIME` | `event.idm.read_only_udm.additional.fields` | Key "TIME"  
`LOCATION` | `event.idm.read_only_udm.additional.fields` | Key "LOCATION"  
`COMPONENT` | `event.idm.read_only_udm.additional.fields` | Key "COMPONENT"  
`RELEASE` | `event.idm.read_only_udm.additional.fields` | Key "RELEASE"  
`RC` | `event.idm.read_only_udm.additional.fields` | Key "RC"  
`product_information` | `event.idm.read_only_udm.additional.fields` | Key "product_information"  
`product_information_2` | `event.idm.read_only_udm.additional.fields` | Key "product_information_2"  
`library_status` | `event.idm.read_only_udm.additional.fields` | Key "library_status"  
`SECUDIR_environment_variable_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "SECUDIR_environment_variable_status"  
`TLS_extension_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "TLS_extension_status"  
`bind_port_1` | `event.idm.read_only_udm.additional.fields` | Key "bind_port_1"  
`bind_port_2` | `event.idm.read_only_udm.additional.fields` | Key "bind_port_2"  
`bind_port_3` | `event.idm.read_only_udm.additional.fields` | Key "bind_port_3"  
`bind_service_1` | `event.idm.read_only_udm.additional.fields` | Key "bind_service_1"  
`bind_service_2` | `event.idm.read_only_udm.additional.fields` | Key "bind_service_2"  
`bind_service_3` | `event.idm.read_only_udm.additional.fields` | Key "bind_service_3"  
`bind_protocol_1` | `event.idm.read_only_udm.additional.fields` | Key "bind_protocol_1"  
`bind_protocol_2` | `event.idm.read_only_udm.additional.fields` | Key "bind_protocol_2"  
`bind_protocol_3` | `event.idm.read_only_udm.additional.fields` | Key "bind_protocol_3"  
`build_information` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "build_information"  
`calling_module` | `event.idm.read_only_udm.additional.fields` | Key "calling_module"  
`etd_event_sender_enable` | `event.idm.read_only_udm.additional.fields` | Key "etd_event_sender_enable"  
`description1` | `event.idm.read_only_udm.additional.fields` | Key "description1"  
`crypto_kernel_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "crypto_kernel_status"  
`client_info` | `event.idm.read_only_udm.target.resource.attribute.labels` | Key "client_info"  
`client_pvflags` | `event.idm.read_only_udm.target.resource.attribute.labels` | Key "client_pvflags"  
`function_call` | `event.idm.read_only_udm.additional.fields` | Key "function_call"  
`function_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "function_status"  
`gateway_admin_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "gateway_admin_status"  
`gw_status` | `event.idm.read_only_udm.security_result.detection_fields` | Key "gw_status"  
`initialised_library` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "initialised_library"  
`pvflags` | `event.idm.read_only_udm.additional.fields` | Key "pvflags"  
`server_tls_versions` | `event.idm.read_only_udm.target.resource.attribute.labels` | Key "server_tls_versions"  
`client_tls_versions` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "client_tls_versions"  
`etd_event_sender_ssl_config` | `event.idm.read_only_udm.security_result.detection_fields` | Key "etd_event_sender_ssl_config"  
`SECUDIR` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "SECUDIR"  
`features` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "features"  
`user_env_variables` | `event.idm.read_only_udm.principal.user.attribute.labels` | Key "user_env_variables"  
`server_info` | `event.idm.read_only_udm.target.resource.attribute.labels` | Key "server_info"  
`function` | `event.idm.read_only_udm.additional.fields` | Key "function"  
`host_address_1` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "host_address_1"  
`host_address_2` | `event.idm.read_only_udm.principal.resource.attribute.labels` | Key "host_address_2"  
`source_module_name` | `event.idm.read_only_udm.additional.fields` | Key "source_module_name"  
`log_identifier` | `event.idm.read_only_udm.additional.fields` | Key "log_identifier"  
`ciphersuites` | `event.idm.read_only_udm.additional.fields` | Key "ciphersuites"  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
