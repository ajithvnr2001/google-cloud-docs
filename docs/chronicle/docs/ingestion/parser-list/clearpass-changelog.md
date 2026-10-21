---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/clearpass-changelog/
title: Change log for CLEARPASS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:53:39.768982+00:00
---

# Change log for CLEARPASS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/clearpass-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLEARPASS

Date | Changes  
---|---  
2026-08-12 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a Grok pattern to parse the raw log fields  
\- Added a grok pattern on `kv_data3` to extract `event_sequence`, `instance`, `facility`, `syslog_severity`, `event_name`, `event_id`, `module`, `tunnel_type`, `src_ip`, `dst_ip`, `dst_port`, `action_message`  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `roles` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `nas_ip`, `dst_ip` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_sequence` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- `event.idm.read_only_udm.observer.namespace`: Newly mapped `instance` raw log field with `event.idm.read_only_udm.observer.namespace` UDM field  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `action_message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `syslog_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `event_name`, `tunnel_type`, `SyslogPriority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `service_name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `syslog_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `CN` raw log values from `KVData3` with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field using match_all grok parsing.  
\- `event.idm.read_only_udm.principal.user.department`: Newly mapped `OU` raw log values from `KVData3` with `event.idm.read_only_udm.principal.user.department` UDM field using match_all grok parsing.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `DC` raw log values from `KVData3` with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field using match_all grok parsing.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Updated `auth_source`, `Auth.Source`, and `Auth_Source` raw log field mappings to strip the `AD:` prefix before mapping to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.   
2026-06-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `auth_source` raw log field from `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field since it is a hostname.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Mapped `auth_source` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `end_host_id` raw log field from `event.idm.read_only_udm.additional.fields` UDM field to ensure the host identifier is stored in its standard, semantically correct location within the data model.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Mapped `end_host_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `user_name` raw log field from `event.idm.read_only_udm.principal.user.userid` UDM field to accurately capture the user's full or display name, reserving the userid field for system-specific account identifiers.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `status_msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_type` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `action_display_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `status_code`, `request_id` and `action_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` field `with event.idm.read_only_udm.intermediary.hostname` UDM field.   
2026-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `deviceProcessName` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `NAD` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `nas_ip`, `dst` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `service_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `roles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` and `USER_LOGIN` based on required data from the raw logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp`, `rt` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `timestamp` is present.   
2026-05-04 |  Enhancement:  
\- Added support for JSON + SYSLOG format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs1`, `cs2`, `cs3`, `cs4`, `cs5`, `cs6`, `tags`, `cribl_pipe`, `organization.id`, `my_timestamp`, `VAR_TOPIC_ID`, `syslog_pri`, `cef_version`, `cef_vendor`, `cef_product`, `cef_product_version`, `cef_signature_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `dvc`, `syslog_host_ip` raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `cs1` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when cs1Label is `Remote IP`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `cef_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `organization.name` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `kafkaTopic` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `evnt.created` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `cef_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `dpriv` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.   
2026-04-02 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ts`, `id`, `monitor_mode`, `audit_apt`, `spt`, `end_host_id`, `request_status`, `cpu_usage`, `res_mem_usage`, `virt_mem_usage` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped roles raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `enf_profiles`, `auth_source` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for new date format present in `timestamp` field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `service_name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-06 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `LogNumber` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `nas_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `nas_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nas_port_type` (key: `nas_port_type`), `seq_num` (key: `seq_num`), `acct_authentic` (key: `acct_authentic`), `acct_sessionId` (key: `acct_sessionId`), `acct_status_type` (key: `acct_status_type`), `called_station_id` (key: `called_station_id`), `calling_station_id` (key: `calling_station_id`), and `acct_delaytimestamp` (key: `acct_delay_time`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a Grok pattern to parse new format of Syslog and KV logs which resulted in mapping following fields correctly"  
\- `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.hostname`.   
2026-02-05 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Auth.Username` raw log field(s) with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `Auth.Host-MAC-Address` raw log field(s) with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `Auth.Roles` raw log field(s) with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `Auth.Protocol` raw log field(s) with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `Auth.NAS-IP-Address` raw log field(s) with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Auth.NAS-IP-Address` raw log field(s) with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Auth.Service` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Auth.Login-Status` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Mapped `eventId` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `Auth.Host-MAC-Address`: Formatted the MAC address by inserting colons.  
\- `Auth.Roles`: Removed [, ], and \ characters.  
\- `Auth.Enforcement-Profiles`: Removed \ characters.  
\- `kv_data`: Multiple substitutions applied to clean the field when it contains `clearPass`.  
\- Added a new block to parse `kv_data` when it contains `clearPass` using the KV filter.   
2026-01-20 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped intermediary_hostname raw log field(s) with event.idm.read_only_udm.intermediary.asset.hostname UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped intermediary_hostname raw log field(s) with event.idm.read_only_udm.intermediary.hostname UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped msgid raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped dmac raw log field(s) with event.idm.read_only_udm.principal.mac UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.roles: Newly mapped roles_list raw log field(s) with event.idm.read_only_udm.principal.user.attribute.roles UDM field.  
\- Added conditional check for dmac, intermediary_hostname, msgid, roles_list.  
\- Added conditional check for kv_data, message.  
\- Added new grok patterns to extract intermediary_hostname, msgid, swVersion, software, ip, enterpriseId, and kv_data.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped intermediary_ip raw log field(s) with event.idm.read_only_udm.intermediary.ip UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped intermediary_ip raw log field(s) with event.idm.read_only_udm.intermediary.asset.ip UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped ArubaClearpassAuthAuthMethod, ArubaClearpassAuthAuthStatus, ArubaClearpassEndpointSSID, ArubaClearpassEndpointService, ArubaClearpassEndpointSystemPostureToken raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped ArubaClearpassAuthAuthorizationSources, ArubaClearpassAuthErrorCode, cs5Label, ArubaClearpassEndpointSessionEndAt, ArubaClearpassEndpointSessionStartAt, ArubaClearpassEndpointSource, ArubaClearpassEndpointUpdatedAt, ArubaClearpassEndpointUserAuthAt raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.target.mac: Newly mapped ArubaClearpassAuthCalledStationId raw log field(s) with event.idm.read_only_udm.target.mac UDM field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped ArubaClearpassAuthAPName raw log field(s) with event.idm.read_only_udm.observer.hostname UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped ArubaClearpassEndpointUsername, ArubaClearpassAuthAuthUsername raw log field(s) with event.idm.read_only_udm.principal.mac UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped ArubaClearpassEndpointUsername, ArubaClearpassAuthAuthUsername raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.   
2025-12-09 |  Enhancement:  
\- Modified a grok pattern to parse the raw log correctly.  
\- event.idm.read_only_udm.principal.asset.asset_id: Removed mapping of `identifier` field from `event.idm.read_only_udm.principal.asset.asset_id` UDM to prevent wrong mapping of asset_id.  
\- Added a grok pattern on `identifier` field to extract `hostName` field.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Mapped `hostName` field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Common.Connection-Status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern on `ip` field to correctly map valid ip addresses.   
2025-11-18 |  Enhancement:  
\- event.idm.read_only_udm.target.mac: Newly mapped `dmac` raw log field to `event.idm.read_only_udm.target.mac`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `fname` raw log field to `event.idm.read_only_udm.principal.mac`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `rt` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_ip` (extracted from `msg`) raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` (extracted from `msg`) raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `Common.Roles` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers`.  
\- event.idm.read_only_udm.security_result.detection_fields: Added key `system_posture_token` mapped from `Common.System-Posture-Token`.  
\- event.idm.read_only_udm.security_result.detection_fields: Added key `outcome` mapped from `outcome`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `cat` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.principal.user.userid: Consolidated mapping logic to primarily use `Common.Username` or CommonUsername.  
\- event.idm.read_only_udm.additional.fields: Consolidated mapping for the `error_code` key to source from `Common.Error-Code`, `code_error`, or `error_code`.  
\- event.idm.read_only_udm.security_result.description: Consolidated mapping to use the `alerts` field, which is now populated from multiple potential raw fields including `Common.Alerts`.  
\- event.idm.read_only_udm.security_result.detection_fields: Consolidated mapping for the `req_time` key to use the `req_time` field, potentially populated from `Common.Request-Timestamp`.  
\- event.idm.read_only_udm.principal.hostname: Updated mapping logic to include `RADIUS.Auth-Source` as a possible source.  
\- event.idm.read_only_udm.principal.asset.hostname: Updated mapping logic to include `RADIUS.Auth-Source` as a possible source.  
\- event.idm.read_only_udm.principal.application: Updated mapping logic to include `RADIUS.Auth-Method` as a possible source.  
\- Added support for a new Key-Value log format.  
\- The key for enforcement profiles in `event.idm.read_only_udm.security_result.detection_fields` was changed from `profile` to `enforcement_profiles`.  
\- Added logic to parse Key-Value pairs from the `kv_data5` field in CEF formatted logs.  
\- Reorganized and centralized the mapping logic for several common fields (e.g., `error_code`, `alerts`, `service`, `Username`, Auth-`Source`, `Auth-Method`, `Enforcement-Profiles`, `Host-MAC-Address`, `NAS-IP-Address`, `Request-Timestamp`) at the end of the configuration file.   
2025-11-14 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip1` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `identifier` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `log_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `val1`, `val2`, `swap_memory_avail`, `system_memory_avail`, `cpu_raw_user`, `cpu_raw_system`, `cpu_raw_idle`, `cpu_raw_nice`, `mgmt_inf_status`, `data_inf_status`, `swap_size_used`, `slash_size_used` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ingest_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `source_ip2` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.   
2025-10-29 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `vd` from `event.idm.read_only_udm.principal.user.userid` UDM field since it is a virtual domain not user.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `vd` raw log field(s) with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `ui` raw log field(s) with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ui` raw log field(s) with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM field(s).  
\- Renamed from _observer to event.idm.read_only_udm.observer.  
\- ui: Transformed using grok pattern (?\\\w+)\\((?%{IP})\\) to extract proto and ui_ip.  
\- Added conditional check for level: if the value is alert, maps HIGH to event.idm.read_only_udm.security_result.severity.   
2025-10-01 |  Enhancement:  
\- Added a new grok pattern to parse the new format of SYSLOG + KV logs.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `CppmNode.CPPM-Node` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `CppmNode.CPPM-Node` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `Auth.Roles` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- KVData: Changed the key-value pair delimiter from `|` to `;` to correctly parse raw log values that contain a `|` character, such as `Auth.Enforcement-Profiles`.   
2025-09-25 |  Enhancement:  
\- Added a new grok pattern to parse the new format of SYSLOG.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ExporterName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Category` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Remote_IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `Remote_IP_Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `InterIP` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `InterIP` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `sdescription` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `code` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Removed the drop condition where Description is having `No new updates available.` and parsed the log properly into respective UDM fields.   
2025-09-16 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `server` raw log field with `event.idm.read_only_udm_principal.application` UDM field.  
\- Added Grok patterns to parse new log formats.   
2025-09-05 |  Enhancement:  
\- Added new grok patterns to parse new log events.   
2025-08-28 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped logid raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped logdesc, Notice_Type raw log field(s) with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped from a combination of date, time, and tz raw log field(s) with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped from a combination of event_time, event_date raw log field(s) with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped Event_ID raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped devname raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped devname raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped devid raw log field with event.idm.read_only_udm.principal.asset.asset_id UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped vd, User_Name raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped Remote_IP_Address raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped Remote_IP_Address raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped hostname raw log field with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped target_user_userid raw log field with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped msg raw log field with event.idm.read_only_udm.security_result.description UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped level, log_level, severity raw log field(s) with event.idm.read_only_udm.security_result.severity UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped level raw log field with event.idm.read_only_udm.security_result.severity_details UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped action_details raw log field with event.idm.read_only_udm.security_result.action_details UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped log_time, type, status,subtype, eventtime, Config_Method, module, interface, event_label, event_code, trap_name, snmp_oid, log_source raw log field(s) to corresponding keys in event.idm.read_only_udm.additional.fields.  
\- Renamed from Device-Name to Device_Name.  
\- Renamed from Config-Method to Config_Method.  
\- Renamed from Event-ID to Event_ID.  
\- Renamed from Notice-Type to Notice_Type.  
\- Renamed from User-Name to User_Name.  
\- Renamed from Remote-IP-Address to Remote_IP_Address.  
\- The condition for mapping event.idm.read_only_udm.network.application_protocol was updated to include `SSH`.  
\- The condition for setting event.idm.read_only_udm.security_result.severity to `MEDIUM` was updated to include a check for [Level] == `notice`.   
2025-08-20 |  Enhancement:  
\- Added a new grok pattern for `not_json` data field to parse the following drop and unparsed logs.  
\- `event.idm.read_only_udm.metadata.product_version` : Newly mapped `swVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `enterpriseId` and `software` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `CppmNode.CPPM-Node` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields if `CppmNode.CPPM-Node` is not equal to `ip` else mapped `CppmNode.CPPM-Node` raw log fields with `event.idm.read_only_udm.additional.fields` UDM fields.  
\- `event.idm.read_only_udm.security_result.action_details` : Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- Added a new gsub on `_principal_ip` to replace `\\\\` with "".   
2025-07-18 |  Enhancement:  
\- Added a new grok patterns for `not_json` data field to parse the following drop and unparsed logs.  
\- Added a new gsub to parse the following drop and unparsed logs.  
\- `event.idm.read_only_udm.security_result.description` : Newly mapped `messagedetail` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `Thread_id`,`servicename` , and `Req_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `Internalserviceid`, `InternalChallengeID`, `Entityid`, `handlervalue`, and `instanceid` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description` : Newly mapped `threadrequestinfo` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- Modified the mapping of `timestamp` raw log field to correctly map with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-14 |  Enhancement:  
\- Added a gsub to replace `\\r` with "".  
\- Added a Grok pattern to parse the raw log fields.  
\- Removed a gsub to replace `\r\n` with ` `.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `prin_pid` field with `event.idm.read_only_udm.principal.process.pid`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `host_host` field with `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `id1`,`TACACS_Privilege_Level`,`common_login_status` field with `event.idm.read_only_udm.security_result.detection_fields`.  
\- Added a grok pattern on `kv_data_2` field to extract `common_request_timestamp`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `common_request_timestamp` field with `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `Common_Username` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- Added a grok pattern on `TACACS_Remote_Address` to extract valid ip format.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `TACACS_Remote_Address` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.   
2025-06-25 |  Enhancement:  
\- event.idm.read_only_udm.metadata.description: Newly mapped `RADIUS.Acct-Service-Name` raw log field with `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `RADIUS.Acct-NAS-IP-Address` raw log field with `event.idm.read_only_udm.intermediary.ip`.  
\- event.idm.read_only_udm.principal.labels: Newly mapped `RADIUS.Acct-NAS-Port-Type` raw log field with `event.idm.read_only_udm.principal.labels`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `RADIUS.Acct-Session-Id` raw log field with `event.idm.read_only_udm.network.session_id`.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `RADIUS.Acct-Session-Time` raw log field with `event.idm.read_only_udm.network.session_duration.seconds`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `RADIUS.Acct-Input-Pkts` raw log field with `event.idm.read_only_udm.network.sent_bytes`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `RADIUS.Acct-Output-Pkts` raw log field with `event.idm.read_only_udm.network.received_bytes`.  
\- Added Support to the event_type when `acct_service_name` has `Login` then event_type is `USER_LOGIN`, when `acct_service_name` has `Logout` then event_type is `USER_LOGOUT`.   
2025-05-09 |  Enhancement:  
\- Added support to parse new format of SYSLOG + KV logs.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `swVersion` raw log field with `event.idm.read_only_udm.metadata.product_version`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `software` , `code_error` and `enterpriseId` raw log fields with `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `Common.Host-MAC-Address` raw log field with `event.idm.read_only_udm.principal.mac`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Common.Service` , `Common.Enforcement-Profiles` , `req_time` raw log field with `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Common.NAS-IP-Address` and `CppmNode.CPPM-Node` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `RADIUS.Auth-Source` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `roles` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `auth_method` raw log field with `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `alerts` raw log field with `event.idm.read_only_udm.security_result.description`.  
\- If `roles` has value `Authenticated` then map the `event_type` as `USER_LOGIN` else map the `event_type` as `USER_UNCATEGORIZED`.   
2024-09-12 |  Enhancement:  
\- Added support to parse new format of SYSLOG and JSON logs.   
2024-08-08 |  Enhancement:  
\- Mapped `Acct-NAS-IP-Address` to `principal.ip`.  
\- Mapped `Acct-Username` to `principal.user.userid`.  
\- Mapped `Acct-Calling-Station-Id` to `principal.user.product_object_id`.   
2024-05-05 |  Enhancement:  
\- Handled unparsing SYSLOG format logs.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `agent_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `descr` and `eventDescription` to `metadata.description`.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `specificTrap_name`, `uptime`, `enterprise`, `generic_num`, `specificTrap_num`, and `community` to `additional.fields`.   
2024-01-11 |  Enhancement:  
\- Mapped `Common.NAS-IP-Address` to `target.ip`.  
\- Mapped `Common.Service`, `Common.Enforcement-Profiles`, and `Common.Login-Status` to `security_result.detection_fields`.   
2022-08-18 |  Enhancement:  
\- Handled the dropped logs which are in CEF format and unparsed logs to improve the parsing rate.  
\- Mapped `metadata.event_type` to `STATUS_UPDATE` where `principal.hostname/principal.ip` is not null else mapped it as `GENERIC_EVENT`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `_target_user_groupid` from `target.user.groupid` to `target.user.group_identifiers`.  
\- Modified mapping for `Common.Roles` from `principal.user.groupid` to `principal.user.group_identifiers`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
