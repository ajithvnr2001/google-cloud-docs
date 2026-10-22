---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/watchguard-changelog/
title: Change log for WATCHGUARD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:21.577861+00:00
---

# Change log for WATCHGUARD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/watchguard-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WATCHGUARD

Date | Changes  
---|---  
2026-08-06 |  Enhancement:  
\- Added new grok patterns to extract the `policy_name`, `dst_hostname` and `dst_ip` raw log fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `dst_hostname` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Mapped `src_user` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `src_user` raw log field contains a valid email address.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `src_user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field when `src_user` raw log field contains a username and not a valid email address.   
2026-08-03 |  Enhancement:  
\- Added a grok pattern on `duration` raw log field to extract the `duration_seconds` field.  
\- Added a grok pattern on `tcp_info` to extract the `tcp_seq`, `tcp_window`, `tcp_offset` and `tcp_flag` fields.  
\- `event.idm.read_only_udm.principal.labels`: Removed mapping of `gateway` and `status` fields from `event.idm.read_only_udm.principal.labels` as it is deprecated.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Mapped `gateway` and `status` fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.labels`: Removed mapping of `gateway` and `status` fields from `event.idm.read_only_udm.target.labels` as it is deprecated.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Mapped `gateway` and `status` fields with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.intermediary.labels`: Removed mapping of `endpoint` and `prin_host` fields from `event.idm.read_only_udm.intermediary.labels` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `endpoint` and `prin_host` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Mapped `protocol` field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `policy_name` field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `disposition` field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Mapped `msg` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `botnet`, `tcp_offset`, `tcp_flag`, `tcp_seq`, `tcp_window`, `pkg_len`, `iph_len`, `ttl`, `endpoint`, `priority`, `facility` and `prin_host` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Mapped `appname` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Mapped `proc_id` raw log field with `event.idm.read_only_udm.intermediary.process.pid` UDM field.   
2026-04-02 |  Enhancement:  
\- Added new grok patterns to parse the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `src_post_nat` log field with `event.idm.read_only_udm.principal.nat_ip` UDM field  
\- `event.idm.read_only_udm.target.nat_ip`: Newly mapped `dst_post_nat` log field with `event.idm.read_only_udm.target.nat_ip` UDM field.  
\- `event.idm.read_only_udm.principal.nat_port`: Newly mapped `src_post_nat_port` log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
\- `event.idm.read_only_udm.target.nat_port`: Newly mapped `dst_post_nat_port` log field with `event.idm.read_only_udm.target.nat_port` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `app` log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `app_category` log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `app_behavior` and `route_type` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_description` log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `prod_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `log_file` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `IPS_cat`, `IPS_id`, `IPS_rule` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Added mapping for `UDP` from `proto` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- Modified the grok pattern to ensure that the `syslog_timestamp` raw log field is no longer mapped to `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- Added the grok patterns to ensure inappropriate values are no longer being mapped to `event.idm.read_only_udm.metadata.description` UDM field. Additionally, this is allowing the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.detection_fields.key`  
\- `event.idm.read_only_udm.security_result.detection_fields.value`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.network.received_packets`  
\- `event.idm.read_only_udm.network.sent_packets`  
\- `event.idm.read_only_udm.network.session_duration.seconds`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.target.port`  
2026-02-05 |  Enhancement:  
\- Added a new grok pattern to parse the new format of logs.  
\- event.idm.read_only_udm.about.labels: Newly mapped `app_cat_id`, `app_id`, `tls_profile` raw log field with `event.idm.read_only_udm.about.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cn`, `icmpType`, `in_if`, `ip_TTL`, `ip_len`, `out_if`, `tcp_flag`, `tcp_offset`, `tcp_seq`, `tcp_window` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.network.tls.client.server_name: Newly mapped `sni` raw log field with `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- event.idm.read_only_udm.network.tls.server.certificate.issuer: Newly mapped `cert_issuer` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.issuer` UDM field.  
\- event.idm.read_only_udm.network.tls.server.certificate.subject: Newly mapped `cert_subject` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.subject` UDM field.  
\- event.idm.read_only_udm.network.tls.server.certificate.version: Newly mapped `sig_vers` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.version` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tls_version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `src_user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `proxy_act` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `policy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `ignored_action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `dst_user` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.   
2026-01-30 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description_data` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `devTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.file.full_path`: Newly mapped `intermediary_file_path` raw log field with `event.idm.read_only_udm.intermediary.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `prod_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `MWPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.md5`: Newly mapped `MWHash` (when MWHash is in hex format) and `ChildHash` (when ChildHash is in hex format) raw log fields with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `ThreatType`, `ParentCat`, and `ChildCat` (when ChildCat is different from ParentCat raw log field) raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `ChildPath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `ParentHash` (when ParentHash is in hex format) raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `ParentPath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `MUID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `usrName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `HostName` raw log fields with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `ExecutionStatus` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `devTimeFormat`,`ParentDriveType`,`DriveType`, `DwellTimeSecs`, `product_data`, `vendor_data`, `syslog_version`, `syslog_priority`, `DetId`, `WinningTech`, `ServiceLevel`, `ChildPrevLastDay`, `ChildPrevalence`, `ChildExeType`, `ChildImageType`, `ChildBroken`, `ChildFlags`, `ChildCat` (when ChildCat is same as ParentCat), `ParentPrevLastDay`, `ParentPrevalence`, `ParentExeType`, `ParentImageType`, `ParentBroken`, `ParentFlags`, `Op`, `PandaTimeStatus`, `LocalDateTime`, `identSrc`, and `identHostName`raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `MWHash` (when not in hex format), `ChildValidSig`, `ChildCompany`, and `ChildHash` (when ChildHash is not in hex format) raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `ParentCompany`, `ParentHash` (when ParentHash is not in hex format), and `ParentValidSig` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- `PROCESS_LAUNCH`: Added support for the `PROCESS_LAUNCH` event when the `has_principal` and `has_target_process_file` flags are set to true.  
\- `USER_UNCATEGORIZED`: Added support for the `USER_UNCATEGORIZED` event when the `has_principal_user` flag is set to true.   
2025-12-19 |  Enhancement:  
\- event.idm.read_only_udm.metadata.description: Newly mapped generic_message raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped area raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped user_name raw log field with event.idm.read_only_udm.principal.user.user_display_name UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped src_ip raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped src_ip raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped auth_server raw log field with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped auth_server raw log field with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped reason raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped security_action raw log field with event.idm.read_only_udm.security_result.action UDM field.  
\- Conditional Logic  
\- Added conditional check for event_name, generic_message.  
\- Event Type Update  
\- event.idm.read_only_udm.metadata.event_type: If event_name is wgcgi and generic_message contains was rejected, updated to USER_LOGIN.  
\- The field _extensions.auth.type is set to AUTHTYPE_UNSPECIFIED if event_name is wgcgi and generic_message contains was rejected.   
2025-11-14 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Updated field mapping logic to prioritize the `firewallname` raw log field. Fallback mappings from `auth_server` or `intermediary_host` raw log fields are now conditional and will only be used if `firewallname` raw log field is empty or its initial mapping fails.  
\- Added error handling for the `firewallname` raw log field mapping to intermediary.hostname using a firewallname_intermediary_error flag, which controls the conditional fallback logic.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `firewallname` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- Conditionally mapped the `auth_server` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers` if `firewallname` is present and successfully mapped to intermediary.hostname.  
\- `event.idm.read_only_udm.principal.user.userid`: Conditional mapping applied: Only mapped `user_name` raw log field to `event.idm.read_only_udm.principal.user.userid` if `user_name` raw log field is not empty.   
2025-07-14 |  Enhancement:  
\- Modified existing grok patterns and added new grok patterns to parse logs with eventIDs as `1600-0066`, `1600-0003` and `1600-0002`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `device_name` log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field and set `has_principal` to true.  
\- Added a conditional check to check if `intermediary_host` is an IP and mapped it to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.process_pid: Newly mapped `pid_` log field with `event.idm.read_only_udm.intermediary.process_pid` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `event_name` log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.product_object_id: Newly mapped `firewallname` log field with `event.idm.read_only_udm.intermediary.asset.product_object_id` UDM field.   
2025-06-05 |  Enhancement:  
\- Added gsub to parse the required data in the logs.  
\- event.idm.read_only_udm.network.dns.questions: Newly mapped `question` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers` : Newly mapped `record_type` raw log field with `event.idm.read_only_udm.network.dns.answers` UDM field.   
2025-05-05 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- metadata.product_log_id: Newly mapped `serial` raw log field with `metadata.product_log_id` UDM field.  
\- log_format: Added new grok patterns to support parsing the new log format.  
\- log_parser: Added `gsub` filters to remove extra spaces from the `remaining_data` field.   
2025-01-07 |  Enhancement:  
\- Added a new Grok pattern to map `host` to `additional.fields`.   
2024-09-24 |  Enhancement:  
\- Added JSON pattern to parse the unparsed logs.  
\- Mapped `USERNAME` to `principal.user.userid`.  
\- Mapped `DEST_PORT` to `target.port`.  
\- Mapped `PROTOCOL_TR` to `network.ip_protocol`.  
\- Mapped `DEST_INTERFACE` to `target.resource.attributes.labels`.  
\- Mapped `SOURCE_INTERFACE` to `principal.resource.attributes.labels`.  
\- Mapped `SOURCE_PORT` to `principal.port`.  
\- Mapped `PRIVATE_IP` to `target.ip`.  
\- Mapped `SOURCE_IP` to `principal.ip`.  
\- Mapped `DEST_IP` to `target.ip`.  
\- Mapped `COMMON_REPORT_NAME`, `DOMAIN`, `IENAME`, `FACILITY`, `MESSAGESTART`, `POLICY_ID`, `ARCHIVETYPE`, `MESSAGELEN`, `OPERATION`, `IEGROUP`, `ESID`, and `PACK_HEADER_LEN` to `additional.fields`.  
\- Mapped `SEVERITY` to `security_result.severity_details`.   
2024-07-02 |  Enhancement:  
\- Modified the Grok pattern to parse new fields.  
\- Modified few Grok patterns to parse the new formats of `identified_log`.  
\- Added a Grok pattern to parse `identified_log` with `msg_id` value as `1600-0066`.  
\- Mapped `area`, `interface_name`, and `network_name` to `additional.fields`.  
\- Mapped `virtual_ip` to `intermediary.ip`.  
\- Mapped `flags` to `security_result.detection_fields`.  
\- Mapped `duration` to `network.session_duration.seconds`.  
\- Mapped `sent_pkts` to `network.sent_packets`.  
\- Mapped `rcvd_pkts` to `network.received_packets`.  
\- Removed the mapping of `src_host` to `principal.hostname` and `dst_host` to `target.hostname`.   
2023-12-03 |  Enhancement:  
\- Modified a Grok pattern to parse new fields.  
\- Modified few Grok pattern to parse new patterns of `identified_log`.  
\- Added a new Grok pattern to parse `identified_log` having `msg_id` value as `1600-0066`.   
2023-11-27 |  Enhancement:  
\- Mapped `signature_name` to `additional.fields` for logs having `msg_id` equal to `3000-0150`.  
\- Mapped `signature_id`, `signature_cat` to `additional.fields`.   
2023-11-24 |  Enhancement:  
\- Modified few Grok patterns to parse new fields.  
\- Mapped `firewallname` to `event.idm.read_only_udm.intermediary.hostname`.  
\- Mapped `firewall_id` to `event.idm.read_only_udm.intermediary.asset_id`.  
\- Mapped `prin_host` to `event.idm.read_only_udm.intermediary.labels`  
2023-11-10 |  Enhancement:  
\- Removed redundant code.  
\- Mapped `signature_name` to `additional.fields`.   
2023-09-28 |  Bug-fix:  
\- Modified the `date` filter to support the following formats `yyyy-MM-dd HH:mm:ss`, `MMM d HH:mm:ss`, `MMM dd HH:mm:ss`, `ISO8601`, `yyyy-MM-ddTHH:mm:ss`.   
2023-05-25 |  Bug-fix:  
\- Changed mapping for the field `src_vpn_ip` from `principal.ip` to `target.ip` for event `Received DPD message from target host through gateway`.   
2023-05-04 |  Enhancement - Added Grok patterns to handle unparsed logs with event `dnsmasq`, `dhcpd`, `iked`, `admd`.   
2023-01-20 |  Enhancement - Added grok to handle unparsed logs.  
\- Mapped `dst_port` to target.port.  
\- Mapped `src_port` to principal.port.  
\- Mapped `rcvd_bytes` to network.received_bytes.  
\- Mapped `geo_src` to principal.location.country_or_region.  
\- Mapped `geo_dst` to target.location.country_or_region.  
\- Mapped `prin_host` to `principal.hostname`.  
\- Added conditional check for `dhcp_type`, `intermediary_host`, `protocol`  
\- For `msg_id` equal to `1600-0066`  
\- Added grok pattern for `msg_id` equal to `1600-0066`.  
\- Mapped `description` to `metadeta.description`.  
\- For `msg_id` equal to `2DFF-0000`  
\- Mapped `proxy_act` to `security_result.rule_name`.   
2022-12-17 |  Enhancement - Mapped firewall name to `principal.asset_id` for the logs containing Member1.  
\- Modified `event_type` from `SERVICE_MODIFICATION` to `NETWORK_CONNECTION`.  
\- Mapped `src_user` to `principal.user.email_addresses` if it' an Email, else mapped it to `principal.user.user_display_name`.   
2022-12-16 |  Enhancement -  
\- Added grok to handle unparsed log with event_name `firewall`.  
\- Reduced GENERIC_EVENT type.   
2022-11-16 |  Enhancement - Mapped `reason` field to `security_result.action_details`.  
\- Added grok to handle unparsed log with event_name `firewall`.  
\- Added additional conditional blocks to parse logs with event_name `loggerd`, `sigd`, `sessiond`, `admd`, `iked`.   
2022-11-07 |  Bug-fix:  
\- Mapped path given in the http header from `target.file.full_path` to `target.url` instead.   
2022-06-17 |  Enhancement - Parsed logs with events related to `firewall`, `http-proxy`, `https-proxy`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
