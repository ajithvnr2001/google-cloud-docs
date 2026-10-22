---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-ontap-changelog/
title: Change log for NETAPP_ONTAP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:40.471000+00:00
---

# Change log for NETAPP_ONTAP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netapp-ontap-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETAPP_ONTAP

Date | Changes  
---|---  
2026-07-22 |  Enhancement:  
\- Added a grok pattern to parse new format of SYSLOG logs.  
\- Added support for the `app_protocol` and `net_app_protocol`.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain_name` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when the `description` is `Logging in` or `Login Attempt`.  
\- Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when the `description` is `Logging out`.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine data and target machine data are present, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.   
2026-07-02 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `url` to extract `network_resource`, `url_kv_data`.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `x_dot_client_app` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `TargetDomainName` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `network_resource` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `vserver`, `fields`, `lookup_names`, `privilege_level` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `day` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: When `has_principal_user` is `true` and `has_target_resource` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`.   
2026-06-05 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `ts` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field as `offset_timestamp` is more accurate.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `offset_timestamp` log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ts` log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_hostname` log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `audit_code` and `audit_details` log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: When `net_app_protocol` is `SSH`, updated the value of `event.idm.read_only_udm.network.application_protocol` to `SSH`.  
\- Added a Grok pattern to parse new format of SYSLOG logs.  
\- Updated the Grok patterns on message to extract `offset_timestamp`.   
2026-03-30 |  Enhancement:  
\- Added grok pattern to parse new format of SYSLOG logs.  
\- Added gsub to remove `\\x05` invalid character from the logs.  
\- Added gsub to replace `mar\\.` with `Mar`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AccessList`, `AccessMask` and `DesiredAccess` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-17 |  Enhancement:  
\- Added a grok pattern to parse SYSLOG+XML format of raw logs.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `collect_time` field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field by implementing a gsub to replace the Spanish abbreviation `ene.` with `Jan`  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `IpAddress` field with event.idm.read_only_udm.principal.ip UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `IpAddress` field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `IpPort` field with event.idm.read_only_udm.principal.port UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `TargetUserSID` field with event.idm.read_only_udm.target.user.windows_sid UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `TargetUserName` field with event.idm.read_only_udm.target.user.userid UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `TargetDomainName` field with event.idm.read_only_udm.target.administrative_domain UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` flag is `true` and `has_target` flag is `true`, updated to NETWORK_CONNECTION.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `xml_namespace`, `IpAddressVersion`, `LogonType` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TargetUserIsLocal` field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AuthenticationPackageName` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- The following fields have been added as a result of providing support to the dropped logs:  
\- event.idm.read_only_udm.additional.fields  
\- event.idm.read_only_udm.intermediary.hostname  
\- event.idm.read_only_udm.metadata.collected_timestamp  
\- event.idm.read_only_udm.metadata.description  
\- event.idm.read_only_udm.metadata.event_timestamp  
\- event.idm.read_only_udm.metadata.event_type  
\- event.idm.read_only_udm.metadata.log_type  
\- event.idm.read_only_udm.metadata.product_event_type  
\- event.idm.read_only_udm.metadata.product_name  
\- event.idm.read_only_udm.metadata.vendor_name  
\- event.idm.read_only_udm.principal.administrative_domain  
\- event.idm.read_only_udm.principal.asset.ip  
\- event.idm.read_only_udm.principal.ip  
\- event.idm.read_only_udm.principal.port  
\- event.idm.read_only_udm.principal.user.attribute.labels  
\- event.idm.read_only_udm.principal.user.userid  
\- event.idm.read_only_udm.principal.user.windows_sid  
\- event.idm.read_only_udm.security_result.action  
\- event.idm.read_only_udm.security_result.description  
\- event.idm.read_only_udm.security_result.detection_fields  
\- event.idm.read_only_udm.security_result.rule_id  
\- event.idm.read_only_udm.security_result.severity  
\- event.idm.read_only_udm.security_result.severity_details  
\- event.idm.read_only_udm.security_result.summary  
\- event.idm.read_only_udm.target.administrative_domain  
\- event.idm.read_only_udm.target.application  
\- event.idm.read_only_udm.target.asset.hostname  
\- event.idm.read_only_udm.target.file.full_path  
\- event.idm.read_only_udm.target.hostname  
\- event.idm.read_only_udm.target.resource.attribute.labels  
\- event.idm.read_only_udm.target.resource.name  
\- event.idm.read_only_udm.target.resource.resource_subtype  
\- event.idm.read_only_udm.target.user.userid  
\- event.idm.read_only_udm.target.user.windows_sid   
2026-02-13 |  Enhancement:  
\- Modified grok pattern to support logs where `app_protocol`, `proto_version`, `response_code`, and `response_status` fields are not present.  
\- Added gsub to remove newline characters from the message field to ensure proper parsing.  
\- Corrected escaping in grok pattern to correctly parse `msg_description`.  
\- `event.idm.read_only_udm.metadata.event_type`: Set to `USER_UNCATEGORIZED` if `principal.user.userid` is present.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `status` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `audit_info`, `internal_timestamp`, `target_service`, `unknown_id1`, and `unknown_id2` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-05 |  Enhancement:  
\- Added support for new syslog format to extract `user_id`, `src_ip`, `src_port`, and `application_protocol` from `msg_description` fields.  
\- Set `has_target` to `true` when `target_hostname` is not empty and `has_principal_user` to `true` when `user_id` is not empty.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal_user` and `has_target` are `true`, updated to `USER_LOGIN`, and `event.idm.read_only_udm.extensions.auth.type` is set to `AUTHTYPE_UNSPECIFIED`.  
\- If `log_level` is `notice`, `event.idm.read_only_udm.security_result.severity` is mapped to `MEDIUM`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Date` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_hostname` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `event_identifier` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_description` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pam_service` and `pam_module` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `application_protocol` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_description` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.   
2026-02-02 |  Enhancement:  
\- Added grok patterns to parse new format of raw logs.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_protocol` field(s) with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `proto_version` field(s) with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response_code` field(s) with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `log_source` field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `status_description` field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `response_status` field(s) with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `header_timestamp` field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nfs_ops`, `cifs_ops`, `http_ops`, `fcp_ops`, `iscsi_ops`, `nvme_fc_ops`, `nvme_tcp_ops`, `nvme_roce_ops`, and `additional_information` fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-01 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped UUID raw log field(s) with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped AVER raw log field(s) with event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped ATYP raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped LOCS, ATIM, AMID, ATID, CBID, BUID, CNID, S3AI, SACC, S3AK, SBAI, VSID, MTME, LKMD, TIME raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped SAIP raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped SAIP raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped SUSR, sudo_user raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped TLIP raw log field(s) with event.idm.read_only_udm.target.ip UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped TLIP raw log field(s) with event.idm.read_only_udm.target.asset.ip UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped PATH raw log field(s) with event.idm.read_only_udm.target.file.full_path UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped CSIZ raw log field(s) with event.idm.read_only_udm.target.file.size UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped S3KY raw log field(s) with event.idm.read_only_udm.target.resource.id UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped S3BK raw log field(s) with event.idm.read_only_udm.target.resource.name UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped SBAC raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped sudo_run_as_user raw log field(s) with event.idm.read_only_udm.target.user.userid UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped sudo_command raw log field(s) with event.idm.read_only_udm.target.process.command_line UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped ANID raw log field(s) with event.idm.read_only_udm.security_result.rule_id UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped RULE raw log field(s) with event.idm.read_only_udm.security_result.rule_name UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped STAT raw log field(s) with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped RSLT raw log field(s) with event.idm.read_only_udm.security_result.action UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped sudo_pwd raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
Type Conversion  
\- CSIZ: Converted type to uinteger with error handling for CSIZ_conversion_failed.  
Event Type Update  
\- event.idm.read_only_udm.metadata.event_type: If sudo_command is present, updated to PROCESS_LAUNCH.  
Other Updates  
\- The kv_message field is transformed to parse key-value pairs.   
2025-10-31 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `message_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `process_name` raw log field to `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_port` raw log field to `event.idm.read_only_udm.principal.port`.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `audit_info`, `target_service`, `internal_timestamp`, `unknown_id1` and `unknown_id2` raw log field to event.idm.read_only_udm.additional.fields.  
\- Added support for additional SYSLOG message formats.  
\- Enhanced Grok patterns to parse new log structures, extracting fields like `process_name`, `pid`, `session_id`, `client_ip`, `client_port`, `user_full`, and `http_method`.  
\- Added support for timestamp format `yyyy-MM-ddTHH:mm:ssZ`.   
2025-10-29 |  Enhancement:  
\- Mapped constant values `STORAGE_OBJECT` and `STORAGE_BUCKET` to `event.idm.read_only_udm.target.resource.type` based on conditions.  
\- Enhanced severity mapping to include `notice` severity level, mapping it to `LOW`.  
\- Updated grok pattern to extract `product_event_type` from an additional log format.  
\- `event.idm.read_only_udm.intermediary.asset.hardware`: Newly mapped `model` raw log field to `event.idm.read_only_udm.intermediary.asset.hardware` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Vserver` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `application` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `vol`, `DISK_ID`, and `rg` raw log fields to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `princ_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `princ_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `princ_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `disk_info` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `UID` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `serialno` raw log field to `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `site` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `duration_ms`, `Failed_auth`, `vendor`, and `errors` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `current_maxdirsize_KB` and `FSID` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `suggested_command`, `type`, `blockNum`, `percentage`, `shelf`, `bay`, `disk_type`, `disk_rpm`, and `default_maxdirsize_KB` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `unowned_disk_count`, `owner`, `app`, `volident`, `run_time`, `firmware_revision`, `carrier`, `Relationship_ID`, `current`, and `duration` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-23 |  Enhancement:  
\- Refactored parser logic to conditionally parse XML or syslog/JSON formats based on the `message` content.  
\- Added Grok pattern to extract `host_part` and `svm_part` from the `computer` field when available.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_id` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `event_name` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `version` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `Version`.  
\- event.idm.read_only_udm.target.application: Newly mapped `source` raw log field to `event.idm.read_only_udm.target.application`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `computer_uuid` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `ComputerUUID`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `SubjectIP` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `SubjectIP` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `SubjectUnixUid` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` with key `SubjectUnixUid`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `SubjectUnixGid` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` with key `SubjectUnixGid`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `SubjectUnixLocal` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` with key `SubjectUnixLocal`.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `SubjectUserSid` raw log field to `event.idm.read_only_udm.principal.user.windows_sid`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `SubjectUserIsLocal` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` with key `SubjectUserIsLocal`.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `SubjectDomainName` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `SubjectUserName` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `ObjectServer` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `ObjectServer`.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `ObjectType` raw log field to `event.idm.read_only_udm.target.resource.resource_subtype`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `HandleID` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` with key `HandleID`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `ObjectName` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `host_part` (derived from `computer`) raw log field to `event.idm.read_only_udm.target.hostname`.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host_part` (derived from `computer`) raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `svm_part` (derived from `computer`) raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- Mapped `InformationRequested` to `event.idm.read_only_udm.security_result.description`.  
\- Mapped `event_id` to `event.idm.read_only_udm.security_result.rule_id`.  
\- Mapped `level` to `event.idm.read_only_udm.security_result.severity` (e.g., `0` to `INFORMATIONAL`) and `event.idm.read_only_udm.security_result.severity_details`.  
\- Mapped `result` to `event.idm.read_only_udm.security_result.summary` and influences `event.idm.read_only_udm.security_result.action` (e.g., `Success` to `ALLOW`, others to `BLOCK`).  
\- Mapped `channel` to `event.idm.read_only_udm.security_result.detection_fields` with key `Channel`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` conditional on other fields.  
\- Mapped `note` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Provider Name` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `Provider Name`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Provider Guid` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `Provider Guid`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Opcode` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `Opcode`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Keywords` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `Keywords`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Security` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `Security`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `IPVersion` raw log field to `event.idm.read_only_udm.additional.fields` with key `IPVersion`.   
2025-06-25 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `accessLocation` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `accessLocation` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `deviceId` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `deviceId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `deviceName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `deviceName` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.administarative_domain: Newly mapped `domain` raw log field with `event.idm.read_only_udm.principal.administarative_domain` UDM field.  
\- event.idm.read_only_udm.target.file.names: Newly mapped `entityName` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `entityPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `entityType`, and `extension` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `entityAccessedTime` and `alertTimestamp` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `userDisplayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `volumeId`, `volumeName`, `alertType`, `attributes.dataDestructionDetectedEntityCount`, and `attributes.changePercentage` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if `has_principal_user` is `true`.   
2025-03-21 |  Enhancement:  
\- Mapped `severity` to `security_result.severity_details`.  
\- Added Grok patterns to support new pattern of Syslog logs.  
\- Mapped `file_extn` to `security_result.detection_fields`.  
\- Added gsubs to avoid new lines in `message`.  
\- Added gsub to avoid additional quotations in `description`.   
2024-08-29 |  \- Added support to parse unparsed logs.  
\- Mapped `descr` to `security_result.summary`.  
\- Mapped `uid` to `metadata.product_log_id`.  
\- Mapped `product_name` to `principal.hostname`.   
2023-04-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
