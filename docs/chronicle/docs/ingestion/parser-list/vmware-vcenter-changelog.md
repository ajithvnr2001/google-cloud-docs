---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vcenter-changelog/
title: Change log for VMWARE_VCENTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:20:18.364183+00:00
---

# Change log for VMWARE_VCENTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vcenter-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_VCENTER

Date | Changes  
---|---  
2026-09-22 |  Enhancement:  
\- Added grok pattern to parse new format of syslogs.  
\- `event.idm.read_only_udm.metadata.product_version`: Removed mapping of `version` from `event.idm.read_only_udm.metadata.product_version` UDM field. As this is a duplicate mapping.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `precise_syslog_event_time`, `syslog_event_time` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `inter_appname` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `container_name`, `cri_stream`, `cri_flag`, `pod-template-hash`, `control-plane`, `deployment.kubernetes.io/pod-name`, `deployment.pinniped.dev`, `kapp.k14s.io/app`, `kapp.k14s.io/association`, `io_app_name`, `err`, `logger`, `VSphereCPIConfig`, `caller`, `reflector`, `log_message` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `cri_json_msg` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-07-20 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/vmware-vcenter`.   
2026-06-30 |  Enhancement:  
\- Added grok pattern to parse new formats of raw log field `msg_1`.  
\- Added grok pattern to parse raw log field `http_request`.  
\- `event.idm.read_only_udm.security_result.severity`: If `level_name` is `warning`, then mapped `event.idm.read_only_udm.security_result.severity` to `WARNING`.  
\- `event.idm.read_only_udm.security_result.severity`: If `level_name` is `error`, then mapped `event.idm.read_only_udm.security_result.severity` to `ERROR`.  
\- `event.idm.read_only_udm.metadata.event_type`: If event is user login event, then set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.   
2026-06-04 |  Enhancement:  
\- Added a grok pattern to parse a new pattern of logs.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `log_timestamp` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `p_vm_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `data_center` raw log field to `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sys_priority`, `sequence_id` and `p_log_id_repeat` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- Added a condition check if `p_vm_name` is null before mapping `user_id` to `event.idm.read_only_udm.target.resource.name`.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `target_userid` from `event.idm.read_only_udm.target.user.userid` UDM field as this is the account initiating the login/action, thus it's the principal user not the target.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `target_userid` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field as this is the account initiating the login/action, thus it's the principal user.  
\- `event.idm.read_only_udm.target.ip`: Removed mapping of `ip` from `event.idm.read_only_udm.target.ip` UDM field as this IP represents the source of the connection/request, hence it`s the principal`s IP not the target's IP.  
\- `event.idm.read_only_udm.principal.ip`: Mapped `ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field as this IP represents the source of the connection/request, hence it`s the principal`s IP.  
\- `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `ip` from `event.idm.read_only_udm.target.asset.ip` UDM field as this IP represents the source of the connection/request, hence it`s the principal`s IP not the target's IP.  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field as this IP represents the source of the connection/request, hence it`s the principal`s IP.  
\- `event.idm.read_only_udm.target.administrative_domain`: Removed mapping of `user_domain` from `event.idm.read_only_udm.target.administrative_domain` UDM field as this is the domain of the principal user, not the target.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Mapped `user_domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain` UDM field as this is the domain of the principal user.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `target_username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.   
2026-02-05 |  Enhancement:  
\- event.idm.read_only_udm.target.application: Newly mapped `appname` raw log field to event.idm.read_only_udm.target.application.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `principal_email` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `auth_user` raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped `auth_mechanism` raw log field to event.idm.read_only_udm.extensions.auth.type.  
\- event.idm.read_only_udm.principal.application: Newly mapped `process` raw log field to event.idm.read_only_udm.principal.application.  
\- event.idm.read_only_udm.target.url: Newly mapped `request_path` raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `bytes_received` raw log field to event.idm.read_only_udm.network.received_bytes.  
\- event.idm.read_only_udm.target.ip: Newly mapped `upstream_ip` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `upstream_ip` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped `upstream_port` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `local_address_1` raw log field to event.idm.read_only_udm.observer.ip.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `local_address_2` raw log field to event.idm.read_only_udm.observer.ip.  
\- event.idm.read_only_udm.observer.port: Newly mapped `local_port_1` raw log field to event.idm.read_only_udm.observer.port.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vpxd_some_id` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `originator` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `request_timestamp` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `response_flags` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `duration_total_ms` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `duration_upstream_connect_ms` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `duration_response_tx_ms` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `local_port_2` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `summary` raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `auth_date`, `auth_time`, and `auth_tz` raw log fields to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_id` raw log field to event.idm.read_only_udm.principal.process.pid.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field to event.idm.read_only_udm.network.http.response_code.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_sent` raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.port: Newly mapped `client_port` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `priority` raw log field to event.idm.read_only_udm.security_result.severity_details.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `level_name` raw log field to event.idm.read_only_udm.security_result.severity.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.metadata.event_type: Added condition check `has_target` before mapping `event.idm.read_only_udm.metadata.event_type` to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `facility` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `originator_id` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `subsystem` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `proc_id` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.network.tls.version_protocol: Newly mapped `http_version` raw log field to event.idm.read_only_udm.network.tls.version_protocol.   
2026-01-02 |  Enhancement:  
\- Added Support for new pattern of SYSLOG logs.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `r_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `ppid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `p_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.port: Newly mapped `i_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `t_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `t_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `o_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- event.idm.read_only_udm.observer.asset.ip: Newly mapped `o_ip` raw log field with `event.idm.read_only_udm.observer.asset.ip` UDM field.  
\- event.idm.read_only_udm.observer.port: Newly mapped `o_port` raw log field with `event.idm.read_only_udm.observer.port` UDM field.  
\- event.idm.read_only_udm.network.tls.version_protocol: Newly mapped `tls_details` raw log field with `event.idm.read_only_udm.network.tls.version_protocol` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `r_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `s_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `response_flag` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `unknown_metric_2` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `unknown_metric_1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `http_path` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `pusername` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `puserid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `http_details` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `http_details` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `t_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `hmethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `p_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `meta_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `p_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `p_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `p_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `c_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.file.mime_type: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM field.   
2026-01-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Modified the logic to set the event type to `USER_LOGIN` if raw log field `user_id` is not empty and raw log field `Event_Type_Str` contains `Login` or raw log field `type` contains `Login`.   
2025-12-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `location` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `eventid_label` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- Expanded an existing grok pattern to extract `location` and `eventid_label` from the raw log.  
\- Expanded an existing grok pattern for `desc` to include an alternative pattern for extracting `target_host`.  
\- Introduced a new field `has_target` and set it to `true` if `target_host` is present.   
2025-12-15 |  Enhancement:  
\- Added a grok pattern to parse a new pattern of logs.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Event_Type_Str` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description_data` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity_data` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Logger_Name` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `prin_pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `Event_Type_Str` contains `login` and `user_id` is not equal to null then updated to `USER_LOGIN` from `USER_UNCATEGORIZED`.   
2025-12-05 |  Enhancement:  
\- Added support for a new SYSLOG format to parse VCenter audit logs.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_app` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource_name` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `api_call_method` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator_id`, `subcomponent`, `op_id`, `vcenter_uuid_1`, `vcenter_uuid_2`, `object_lookup_method` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-11-21 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vc_event_desc` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `vc_event_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `vc_event_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ssh_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ssh_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `vc_username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `user_domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `msg` contains `session was opened`, updated to `USER_LOGIN`.   
2025-11-14 |  Enhancement:  
\- Added a grok pattern to parse a new pattern of logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `uid`, `euid`, `tty`, `ruser` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `rhost` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `logname` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.target.application: Newly mapped `app` log field to `event.idm.read_only_udm.target.application`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `message` contains `authentication failure` and set `event.idm.read_only_udm.security_result.action` to `BLOCK`.   
2025-10-15 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `action` , `conn_id` , `facility` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- New grok patterns were added to parse additional VMWare vCenter log formats, extracting fields such as session_id, conn_id, principal_ip1, principal_port, target_ip1, target_port, action, line_number, and inter_ip.  
\- event.idm.read_only_udm.security_result.severity is set to MEDIUM if the raw log field priority has a value of notice.   
2025-09-12 |  Enhancement:  
\- Added grok pattern to handle new format of syslog.  
\- Added grok pattern to handle domain in `usrName`, `username`, `target_userid`, `user`, `target_user`, `vc_username`, and `Account Name` (e.g., DOMAIN\\\user, DOMAIN\\\\\\\user).  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `process`, `tenant`, `duration_ms`, `provider`and `provider_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `cor_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2025-09-09 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `tls_cipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `event_status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_userid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `open_connections`, `total_connections`, `channel_id` and `line_number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `msg` contains `LOGIN_SUCCESS` or `SESSION_CREATED`, updated to `USER_LOGIN`.  
\- event.idm.read_only_udm.metadata.event_type: If `msg` contains `SESSION_DESTROYED`, updated to `USER_LOGOUT`.  
\- Added new grok pattern to parse new pattern of logs.   
2025-08-19 |  Enhancement:  
\- Added grok pattern to parse unparsed fields.  
\- event.idm.read_only_udm.target.user.userid: Newly Mapped vc_username raw log field to event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped vc_event_type raw log field to event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly Mapped vc_event_obj_id raw log field to event.idm.read_only_udm.target.asset.asset_id UDM field.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields.   
2025-07-15 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- Added KV filter for field kv_msg2.  
\- Removed redundant mapping for user_agent.  
\- `event.idm.read_only_udm.metadata.event_timestamp`:Newly Mapped `timestamps' raw log field with `read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly Mapped `event_name' raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly Mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly Mapped `usrName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly Mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `LEEF_version_label` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly Mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` as `USER_LOGIN` when `usrName` is not equal to null and `event_name` is `UserLoginSessionEvent`.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` as `USER_LOGOUT` when `usrName` is not equal to null and `event_name` is `UserLogoutSessionEvent`.   
2025-07-10 |  Enhancement:  
\- Added a Grok pattern to parse `target.user.userid` without Domain name.  
\- Added a regex check for `sid` to avoid mapping invalid values to `about.group.windows_sid` UDM field.  
\- Added a regex check for `user_id` to avoid mapping invalid values to `principal.user.userid` UDM field.  
\- Added a regex check for `client` to avoid mapping invalid values to `principal.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `opID`, and `sub` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-26 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Removed mapping for `labels.net.peer.ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field as `labels.net.peer.ip` value in the raw logs represents an intermediary system communicating with the host and not the actual target.  
\- `event.idm.read_only_udm.intermediary.ip`: Mapped `labels.net.peer.ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Removed mapping for `labels.net.peer.port` raw log field with `event.idm.read_only_udm.target.port` UDM field as `labels.net.peer.port` value is more accurately representative of an intermediary rather than the actual target of the event.  
\- `event.idm.read_only_udm.intermediary.port`: Mapped `labels.net.peer.port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Removed mapping for `inter_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field as the `event.idm.read_only_udm.intermediary.port` UDM event is already mapped to `labels.net.peer.port` ,this caused the `inter_port` mapping to be overwritten.  
\- `event.idm.read_only_udm.target.port`: Mapped `inter_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `labels.plugin_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Modified event type detection logic to consider the presence of a `target` in the log. This change ensures that `USER_LOGIN`, `USER_LOGOUT`, and `NETWORK_CONNECTION` event types are only assigned when a target is present and the `STATUS_UPDATE` event type is assigned when target is not present, avoiding missclasification of events when a target is not present. This was implemented using the new field `has_target`.   
2025-03-12 |  Enhancement:  
\- When `msg` nearly matches `logged in` , then set metadata.event_type to `USER_LOGIN`.  
\- When `msg` nearly matches `logged out` , then set metadata.event_type to `USER_LOGOUT`.  
\- Added Grok patterns to extract field from `desc`.  
\- Mapped `api_invocations` to `additional.fields`.  
\- Mapped `target_user` to `target.user.userid`.  
\- Mapped `user_agent` to `network.http.user_agent`.   
2024-11-14 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2024-08-27 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-03 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2023-11-13 |  Enhancement:  
\- Added a Grok pattern to parse `url` field.  
\- Mapped `url` to `target.url`.  
\- Mapped `response_details` to `target.resource.attribute.labels`.  
\- Mapped `usr_agnt` to `network.http.user_agent`.  
\- Mapped `ver_proto` to `network.tls.version`.   
2023-09-27 |  Enhancement:  
\- Modified the JSON key name using a `gsub` function from:  
\- `event` to `log_event`.  
\- `host` to `host1`.  
\- `@timestamp` to `timestamp`.  
\- `@version` to `version`.  
\- Added a new Grok pattern to parse the new log type SYSLOG + KV.  
\- Mapped `DeviceUUID` to `metadata.product_log_id`.  
\- Mapped `InstanceId` to `target.asset_id`.  
\- Mapped `EventPriority` to `security_result.severity`.  
\- Mapped `AccessControlRuleAction` to `security_result_action`.  
\- Mapped `SrcIP` to `principal.ip`.  
\- Mapped `DstIP` to `target.ip`.  
\- Mapped `ICMPType`, `ICMPCode`, `IngressInterface`, `EgressInterface`, `WebApplication`, `DNSQuery`, `DNSRecordType`, `DNSResponseType`, `DNS_TTL`, `service.type`, `log.syslog.facility.code`, `log.syslog.facility.name`, `log.syslog.severity.code`,`log.syslog.severity.name`, `log.syslog.priority` to `additional.fields`.  
\- Mapped `Protocol` to `network.ip_protocol`.  
\- Mapped `IngressZone` to `principal.location.name`.  
\- Mapped `EgressZone` to `target.location.name`.  
\- Mapped `ACPolicy` to `security_result.rule_labels`.  
\- Mapped `AccessControlRuleName` to `security_result.rule_name`.  
\- Mapped `NAPPolicy` to `security_result.rule_labels`.  
\- Mapped `InitiatorPackets` to `network.sent_packets`.  
\- Mapped `ResponderPackets` to `network.received_packets`.  
\- Mapped `InitiatorBytes` to `network.sent_bytes`.  
\- Mapped `ResponderBytes` to `network.received_bytes`.  
\- Mapped `FirstPacketSecond` and `ConnectionID` to `security_result.about.labels`.  
\- Mapped `User` to `security_result.summary`.  
\- Mapped `UserAgent` to `network.http.user_agent`.  
\- Mapped `Client` to `target.labels`.  
\- Mapped `ClientVersion` to `target.platform_version`.  
\- Mapped `ReferencedHost` to `target.hostname`.  
\- Mapped `URL` to `target.url`.  
\- Mapped `HTTPResponse` to `network.http.response_code`.  
\- Mapped `ApplicationProtocol` to `network.application_protocol`.  
\- Mapped `host1.ip` to `principal.ip`.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `http_method` to `network.http.method`.  
\- Added Grok patterns to match the `desc`.  
\- Mapped `principal_ip1` to `principal.ip`.  
\- Mapped `principal_ip2` to `principal.ip`.  
\- Mapped `target_ip1` to `target.ip`.  
\- Mapped `target_ip2` to `target.ip`.  
\- Mapped `principal_port` to `principal.port`.  
\- Mapped `target_port` to `target.port`.  
\- Set `metadata.event_type` to `NETWORK_HTTP` when `principal` and `target` are present and `application_protocol` is `HTTP`.  
\- Set `metadata.event_type` to `NETWORK_CONNECTION` when `principal`, `target`, `application_protocol`, and `ip_protocol` are present".   
2023-02-08 |  Enhancement - Parsed the logs containing `eventid`, `Rhttproxy` by adding/modifying some grok patterns.  
\- Mapped `Account Domain` to `principal.administrative_domain`.  
\- Mapped `Client Address` to `principal.ip`.  
\- Mapped `Client port` to `principal.port`.  
\- Mapped `Source port` to `principal.port`.  
\- Mapped `Source Network Address` to `principal.ip`.  
\- Mapped `providername` to `principal.application`.  
\- Mapped `Access Mask` to `principal.process.access_mask`.  
\- Mapped `Logon Account` to `principal.user.userid`.  
\- Mapped `User ID` to `target.user.windows_sid`.  
\- Mapped `Account Name` to `target.user.userid`.  
\- Mapped `Security ID` to `target.user.windows_sid`.  
\- Mapped `Authentication Package` to `security_result.about.resource.name`.  
\- Mapped `Relative Target Name` to `target.file.full_path`.  
\- Mapped `Share Name` to `target.resource.name`.  
\- Mapped `Logon Type` to `extensions.auth.mechanism`.  
\- Mapped `eventid` to `metadata.product_event_type`.   
2023-01-12 |  Enhancement -  
\- Added support to parser logs by adding following mappings.  
\- Mapped `insertId` to `metadata.product_log_id`.  
\- Mapped `labels.log_type` to `metadata.product_event_type`.  
\- Mapped `labels.net.host.ip` to `principal.ip`.  
\- Mapped `labels.net.host.port` to `principal.port`.  
\- Mapped `labels.net.peer.ip` to `target.ip`.  
\- Mapped `labels.net.peer.port` to `target.port`.  
\- Mapped `labels.net.peer.port` to `target.port`.  
\- Mapped `labels.net.transport` to `network.ip_protocol`.  
\- Mapped `logName` to `security_result.category_details`.  
\- Mapped `@fields.host` to `principal.hostname`.  
\- Mapped `@fields.facility` to `principal.resource.type`.  
\- Mapped `@fields.company_name` to `principal.user.company_name`.  
\- Mapped `@fields.privatecloud_id` to `principal.cloud.project.id`.  
\- Mapped `@fields.privatecloud_name` to `principal.cloud.project.name`.  
\- Mapped `@fields.procid` to `principal.process.pid`.  
\- Mapped `@fields.region_id` to `principal.location.country_or_region`.  
\- Mapped `@version` to `principal.platform_version`.  
\- Mapped `basedn_group_iden` to `target.user.group_identifiers`.  
\- Mapped `cipher` to `network.tls.cipher`.  
\- Mapped `version` to `network.tls.version`.  
\- Mapped `msgid` to `network.email.mail_id`.  
\- Mapped `verify` to `security_result.description`.  
\- Mapped `size` to `network.sent_bytes`.  
\- Mapped `stat` to `security_result.summary`.  
\- Mapped `from` to `network.email.from`.  
\- Mapped `to` to `network.email.to`.  
\- Mapped `get_error` to `intermediary.labels`.  
\- Mapped `relay_ip` to `intermediary.ip`.  
\- Mapped `relay_domain` to `intermediary.hostname`.  
\- Mapped `ssh_proto` to `network.application_protocol`.  
\- Mapped `cmd` to `target.process.command_line`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `file_path` to `target.process.file.full_path`.  
\- Mapped `server_name` to `target.hostname`.  
\- Mapped `target_userid` to `target.user.userid`.  
\- Mapped `ip` to `target.ip`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `resource.type` to `src.labels`.  
\- Mapped `upn_name` to `intermediary.url`.  
\- Added drop tags for logs being dropped.   
2022-05-06 |  Moved customer specific parser to default.  
Syslog format logs are handled.  
Added and modified multiple fields to increase log parsing percentage:  
network.http.response_code, file.full_path, network.sent_bytes, http.method,  
application_protocol, severity, port,process.pid,command_line, event_type.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
