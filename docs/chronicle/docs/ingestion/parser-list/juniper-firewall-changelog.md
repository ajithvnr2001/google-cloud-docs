---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-firewall-changelog/
title: Change log for JUNIPER_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:39.080336+00:00
---

# Change log for JUNIPER_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUNIPER_FIREWALL

Date | Changes  
---|---  
2026-08-31 |  Enhancement:  
\- `event.idm.read_only_udm.network.dns.response_code`: Newly mapped `dns_response_code` raw log field with `event.idm.read_only_udm.network.dns.response_code` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions`: Newly mapped `dns_domain` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dns_ip`, `remote_ip_val` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `index`, `ike_version`, `vpn_details`, `gateway_name`, `local_ike_id`, `remote_ike_id`, `vr_id`, `role` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc_val` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `local_ip_val` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `local_port_val` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `principal_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `remote_port_val` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `target_pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `application_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the condition to set the fallback event type to `USER_UNCATEGORIZED`.   
2026-04-28 |  Enhancement:  
\- Modified grok pattern to replace `prin_host` label with `inter_host` as the header hostname value corresponds to intermediary details.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `prin_host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field as the header hostname value corresponds to intermediary details.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `inter_host` log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `src_value_zone` from `event.idm.read_only_udm.additional.fields` UDM field as `src_value_zone` field corresponds to principal details.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `source_zone` log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `destinationzone` from `event.idm.read_only_udm.additional.fields` UDM field as `destinationzone` field corresponds to target details.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `destination_zone` log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `ACTION` is `URL Blocked`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- Modified a grok pattern to replace `src_value_zone` and `destinationzone` with `source_zone` and `destination_zone`.  
\- Added a grok pattern on `message` to extract `inter_host`, `username`, `roles`, `application_sub_category`, and `urlcategory_risk` log fields.   
2026-04-10 |  Enhancement:  
\- Updated a grok pattern for message to extract `REASON` log field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `REASON` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-03-30 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `source-zone` from `event.idm.read_only_udm.additional.fields` UDM field as `source-zone` field corresponds to principal details.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `source-zone` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `destination-zone` from `event.idm.read_only_udm.additional.fields` UDM field as `destination-zone` field corresponds to target details.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Mapped `destination-zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `REASON` from `event.idm.read_only_udm.additional.fields` UDM field as `REASON` field corresponds to security details.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `REASON` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `PROFILE` from `event.idm.read_only_udm.additional.fields` UDM field as `PROFILE` field corresponds to security details.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `PROFILE` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `direction` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as `direction` field corresponds to security details.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `direction` log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Updated the key name from `srv_name` to `service_name` for mapping of `srv_name` with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_type` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `prin_host` log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `principal_pid` log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.file.full_path`: Newly mapped `current_directory` log field with `event.idm.read_only_udm.intermediary.file.full_path` UDM field.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- `event.idm.read_only_udm.intermediary.process.product_specific_process_id`: Newly mapped `ppid` raw log field with `event.idm.read_only_udm.intermediary.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg_desc` and `msg_description` log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `CATEGORY` and `type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `sec_summary` log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `URL` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `direction` is `D` or `Discard`, updated the value of `security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: If `ACTION` is `URL Permitted`, updated the value of `security_result.action` to `ALLOW`.  
\- Added a grok pattern on `msg_desc` to extract `sec_summary` and `kv_data4` raw log fields.  
\- Added a grok pattern on `message` to parse new format of SYSLOG+KV logs.   
2026-03-08 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `src_value_zone` (key: `src_value_zone`), `destinationzone` (key: `destinationzone`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `NESTED-APPLICATION` (key: `NESTED-APPLICATION`), raw log field with `event.idm.read_only_udm.additional.fields` UDM field in JSON format logs.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol_value` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SESSIONID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application_value` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `src_mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `nat_src_address` raw log field with `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip` UDM field.  
\- `event.idm.read_only_udm.principal.nat_port`: Newly mapped `nat_src_value_port` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_value_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: Newly mapped `roles_names` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `interface` (key: `interface`), `eth_type` (key: `eth_type`), `direction` (key: `direction`), `packet_info` (key: `packets_info`), `src_rule_type` (key: `src_rule_type`), `src_rule_name` (key: `src_rule_name`), `srv_name` (key: `srv_name`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `srcpolicyname` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dest_address` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `dst_mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM field.  
\- `event.idm.read_only_udm.target.nat_ip`: Newly mapped `nat_dest_address` raw log field with `event.idm.read_only_udm.target.nat_ip` and `event.idm.read_only_udm.target.asset.nat_ip` UDM field.  
\- `event.idm.read_only_udm.target.nat_port`: Newly mapped `nat_dest_port` raw log field with `event.idm.read_only_udm.target.nat_port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `target_user_name` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- Added a Grok pattern to parse the raw log fields.  
\- Added a Grok pattern on `destination-zone` log field to extract `source_ip`, `source_port`, `target_ip`, `target_port` log fields.  
\- Added support for new pattern of SYSLOG logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.intermediary.hostname`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.security_result.action`  
2025-09-19 |  Enhancement:  
\- Modified parser logic to set event.idm.read_only_udm.security_result.action to UNKNOWN_ACTION for forwarding-class events.  
\- Modified grok patterns to handle different spacing in log messages.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `forwarding_class`, `dscp_code_point` and `loss_priority` raw log field to event.idm.read_only_udm.additional.fields.   
2025-09-11 |  Enhancement:  
\- Modified grok patterns to handle various log formats.  
\- Refactored parser logic to extract additional fields from the task_summary and sec_description fields.  
\- Added logic to dynamically set event.idm.read_only_udm.security_result.action based on the value of the parsed action field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped event_time raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.additional.fields: Newly mapped version, junos_tag, level_name, interface-name, routing-instance, uplink-incoming-interface-name, uplink-tx-bytes, uplink-rx-bytes, apbr-policy-name, and multipath-rule-name raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped os, temporary-filename, type, index, roles, sequence-number, profile-name, rule-set-name, message-type, src-vrf-grp, dst-vrf-grp, dscp-value, apbr-rule-type, and length raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped ip_1 raw log field to event.idm.read_only_udm.intermediary.ip.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped ip_1 raw log field to event.idm.read_only_udm.intermediary.asset.ip.  
\- event.idm.read_only_udm.target.ip: Newly mapped name raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped name raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.principal.ip: Newly mapped local_ip raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped local_ip raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.network.session_id: Newly mapped session-id raw log field to event.idm.read_only_udm.network.session_id.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped policy-name raw log field to event.idm.read_only_udm.security_result.rule_name.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped pathname and filename raw log fields to event.idm.read_only_udm.target.file.full_path.  
\- event.idm.read_only_udm.target.url: Newly mapped url raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped category and sub-category raw log fields to event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.target.hostname: Newly mapped object-name raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped object-name raw log field to event.idm.read_only_udm.target.asset.hostname.   
2025-05-07 |  Enhancement:  
\- `event.idm.ready_only_udm.target.user.userid`: Removed mapping of `user_value` if it starts with `RTLOG` , `RT` , `WEBFILTER` , `SNMPD` , `FLOW` , `DH` , `PKID` , `BGP` , `SNMP` , `RPD` , `JTASK` , `KMD` , `APPIDD` and `IFINFO` from `event.idm.ready_only_udm.target.user.userid` UDM field.  
\- `event.idm.ready_only_udm.metadata.product_event_type`: Mapped `user_value` if it starts with `RTLOG` , `RT` , `WEBFILTER` , `SNMPD` , `FLOW` , `DH` , `PKID` , `BGP` , `SNMP` , `RPD` , `JTASK` , `KMD` , `APPIDD` and `IFINFO` raw log field with `event.idm.ready_only_udm.metadata.product_event_type` UDM field  
\- Added a `has_user_value` flag condition to check if `user_value` is already being mapped to `metadata.product_event_type` to avoid overwriting the existing mapping for logs containing message `junos-ldap`.   
2025-04-08 |  Enhancement:  
\- `event.idm.ready_only_udm.target.user.userid`: Removed mapping of `user_value` if it starts with `APPTRACK` from `event.idm.ready_only_udm.target.user.userid` UDM field.  
\- `event.idm.ready_only_udm.metadata.product_event_type`: Mapped `user_value` raw log field with `event.idm.ready_only_udm.metadata.product_event_type` UDM field   
2025-03-12 |  Enhancement:  
\- Changed mapping of `user_value` from `additional.fields` and `security_result.summary` to `metadata.product_event_type`.  
\- If `user_value` is has `UI_` or `cmd:` or `sub-cmd:` then map `msg_data` to `security_result.description`.  
\- Mapped value of `sec_desc` to `security_result.description`.  
\- Mapped value of `auth` to `extensions.auth.auth_details`.  
\- Mapped value of `username` to `target.user.userid`.  
\- Added a `sub_type` conditional check for mapping of `sub_type` to `metadata.product_event_type`.  
\- Mapped value of `rule` and `sub_rule` to `additional.fields`.  
\- Added a Grok pattern to parse the required data from the logs.   
2025-02-20 |  Enhancement:  
\- Modified the mapping of `target.user.userid` to `additional.fields` when `user_value` starts with `RT_FLOW`.   
2025-02-06 |  Enhancement:  
\- If `user_value` is `UI_LOGIN_EVENT`, map it to `additional.fields`.   
2025-01-15 |  Enhancement:  
\- If `user_name` has `RT_FLOW_SESSION_DENY`, map it to `security_result.action` as `BLOCK`, otherwise change the mapping of `user_name` from `target.user.userid` to `security_result.summary`.  
\- Mapped `sec_desc` to `security_result.description`.   
2024-10-31 |  Enhancement:  
\- Added a new Grok pattern to parse unparsed logs.  
\- Mapped `processid` to `target.process.id`  
\- Mapped `TSr` and `TSi` to `additional.fields`.  
\- Added `gsub` function to map `Remote-IP` to `target.ip`.  
\- Added `gsub` function to map `TSi` and `Local_IKE_ID` to `additional.fields`.  
\- Added KV filter to `kv_data1` to parse unparsed fields.   
2024-10-30 |  Enhancement:  
\- Added a new Grok pattern to parse new log pattern.  
\- Mapped `fw` to `intermediary.ip`.  
\- Mapped `msg1` to `security_result.summary`.  
\- Mapped `desc` to `metadata.description`.   
2024-10-24 |  Enhancement:  
\- Added a new Grok pattern to parse logs in the new SYSLOG+KV format.  
\- Mapped `local_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `remote_ip` to `target.ip` and `target.asset.ip`.   
2024-10-11 |  Enhancement:  
\- Mapped `hostn` to `principal.hostname`.  
\- Mapped `app` to `principal.application`.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `event_title` to `metadata.product_event_type`.  
\- Mapped `event_message` to `metadata.description`.  
\- Mapped `Local-ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Gateway_Name`, `vpn`, `tunnel_id`, `tunnel_if`, `Local_IKE_ID`, `Remote_IKE_ID`, `AAA_username`, `VR_id`, `Traffic_selector`, `Traffic_selector_Remote_ID`, `Traffic_selector_local_ID`, `SA_Type`, `Reason`, `threshold`, `time-period`, and `error-message_data` to `observer.resource.attribute.labels`.  
\- Mapped `target_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `data` to `target.ip` and `target.asset.ip`.   
2024-06-28 |  Enhancement:  
\- Modified the Grok patterns to parse unparsed logs.  
\- Added Grok patterns over the field `msg_data` to extract the fields `user_id`, `principal_host`, `file_path`, `pid_2`, and `server_ip`.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Mapped `user_id` to `target.user.userid`.  
\- Mapped `file_path` to `target.file.full_path`.  
\- Mapped `pid_2` to `target.process.pid`.  
\- Mapped `server_ip` to `target.ip`.  
\- Mapped `event_time` to `metadata.event_timestamp` correctly by removing `rebase` if year is present.   
2024-01-22 |  Bug-Fix:  
\- Added new Grok patterns to parse `message` field with key-value data.  
\- Mapped `ACTION` to `security_result.action_details`.  
\- Mapped `SESSION_ID` to `network.session_id`.  
\- Mapped `APPLICATION` to `principal.application`.  
\- Mapped `pingCtlOwnerIndex`, `pingCtlTestName`, `usp_lsys_max_num_rpd`, `usp_lsys_max_num`, `urlcategory_risk`, `application_sub_category`, `source-zone`, `destination-zone`, `NESTED-APPLICATION`, `CATEGORY`, `REASON`, `PROFILE`, `source_rule`, `retrans_timer` and `arp_unicast_mode` to `additional.fields`.  
\- Mapped `time` to `metadata.event_timestamp`.   
2023-12-31 |  Bug-Fix:  
\- Added support for a new pattern of JSON logs.  
\- Mapped `time` to `metadata.event_timestamp`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `ident` to `target.application`.  
\- Mapped `pid` to `target.process.pid`.  
\- Added Grok patterns to parse `message` field.   
2023-12-15 |  Enhancement:  
\- Mapped `internal-protocol` to `network.ip_protocol` .  
\- Mapped `state` to `security_result.detection_fields`.  
\- Mapped `internal-ip` to `principal.ip`.  
\- Mapped `reflexive-ip` to `target.ip`.  
\- Mapped `internal-port` to `principle.port`.  
\- Mapped `reflexive-port` to `target.port`.  
\- Mapped `local-address` to `principal.ip`.  
\- Mapped `remote-address` to `target.ip`.  
\- Added KV filter with source as `task_summary`.  
\- Mapped `dns-server-address` to `principal.ip`.  
\- Mapped `domain-name` to `principal.administrative_domain`.  
\- Mapped `argument1` to `network.direction`.  
\- Mapped `state` to `security_result.detection_fields`.  
\- Mapped `test-owner` to `additional.fields`.  
\- Mapped `local-initiator` to `additional.fields`.  
\- Mapped `test-name` to `additional.fields`.  
\- Mapped `SPI` to `additional.fields`.  
\- Mapped `AUX-SPI` to `additional.fields`.  
\- Mapped `Type` to `additional.fields`.  
\- Mapped `error-message` to `security_result.summary`.   
2023-11-02 |  Enhancement:  
\- Added a new Grok pattern to parse logs of new `SYSLOG+KV` format.   
2023-08-24 |  Enhancement:  
\- Added gsub function to remove special characters.   
2023-08-02 |  Enhancement:  
\- Modified Grok pattern to support new log formats for NetScreen type.  
\- Added support for type `RT_FLOW_SESSION_CREATE_LS`, `RT_FLOW_SESSION_CLOSE_LS` and `RT_FLOW_SESSION_DENY_LS`.  
\- Mapped `sent` to `network.sent_bytes`.  
\- Mapped `rcvd` to `network.received_bytes`.   
2023-05-05 |  Enhancement:  
\- Mapped `rule-name` to `security_result.rule_id`.  
\- Mapped `rulebase-name` to `security_result.detection_fields`.  
\- Mapped `export-id` to `security_result.detection_fields`.  
\- Mapped `repeat-count` to `security_result.detection_fields`.  
\- Mapped `packet-log-id` to `security_result.detection_fields`.  
\- Mapped `alert` to `is_alert` when the value is `yes`.  
\- Mapped `outbound-packets` to `network.sent_packets`.  
\- Mapped `inbound-packets` to `network.received_packets`.  
\- Mapped `outbound-bytes` to `network.sent_bytes`.  
\- Mapped `inbound-bytes` to `network.received_bytes`.   
2023-03-08 |  Enhancement:  
\- Mapped `application` to `target.application`.  
\- Mapped `reason` to `security_result.description`.  
\- Mapped `application-characteristics` to `security_result.summary`.  
\- Mapped `application-risk` to `security_result.severity_details`.  
\- Mapped `application-category` to `security_result.detection_fields`.  
\- Mapped `application-sub-category` to `security_result.detection_fields`.  
\- Mapped `dst-nat-rule-name` to `security_result.detection_fields`.  
\- Mapped `dst-nat-rule-type` to `security_result.detection_fields`.  
\- Mapped `src-nat-rule-name` to `security_result.detection_fields`.  
\- Mapped `src-nat-rule-type` to `security_result.detection_fields`.  
\- Mapped `encrypted` to `security_result.detection_fields`.  
\- Mapped `nested-application` to `security_result.detection_fields`.  
\- Mapped `packet-incoming-interface` to `security_result.detection_fields`.  
\- Mapped `session-id-32` to `network.session_id`.  
\- Mapped `packets-from-client` to `network.sent_packets`.  
\- Mapped `packets-from-server` to `network.received_packets`.  
\- Mapped `bytes-from-client` to `network.sent_bytes`.  
\- Mapped `bytes-from-server` to `network.received_bytes`.  
\- Mapped `elapsed-time` to `network.session_duration.seconds`.  
\- Mapped `nat-destination-address` to `target.nat_ip`.  
\- Mapped `nat-destination-port` to `target.nat_port`.  
\- Mapped `source-destination-address` to `principal.nat_ip`.  
\- Mapped `source-destination-port` to `principal.nat_port`.   
2023-01-18 |  Bug-fix:  
\- Made the condition case insensitive to map `BLOCK` to `security_result.action`, when `action` is `drop/DROP`.  
\- Mapped `msg_data` to `security_result.description` when `no_app_name` is false.  
\- Mapped `threat-severity` to `security_result.severity`.  
\- Mapped the field `message` to `metadata.description`.  
\- Mapped `app_name` to `target.application`.  
\- Mapped `pid` to `target.process.pid`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `command` to `target.process.command_line`.  
\- Mapped `action` to `security_result.action_details`.  
\- Mapped `sec_description` to `security_result.description`.  
\- Mapped `application-name` to `network.application_protocol`.   
2023-01-15 |  Enhancement-  
\- Modified Grok pattern to support unparsed logs containing type `UI_CMDLINE_READ_LINE`, `UI_COMMIT_PROGRESS`, `UI_CHILD_START`,  
`UI_CFG_AUDIT_OTHER`, `UI_LOGIN_EVENT`, `UI_CHILD_STATUS`, `UI_LOGOUT_EVENT`, `UI_LOAD_EVENT`,  
`JTASK_IO_CONNECT_FAILED`, `UI_AUTH_EVENT`, `UI_NETCONF_CMD`, `UI_COMMIT_NO_MASTER_PASSWORD`, `UI_CFG_AUDIT_SET`, `UI_JUNOSCRIPT_CMD`,  
`SNMPD_AUTH_FAILURE`, `UI_CFG_AUDIT_NEW`, `UI_COMMIT` , `LIBJNX_LOGIN_ACCOUNT_LOCKED`, `UI_COMMIT_COMPLETED`,  
`PAM_USER_LOCK_LOGIN_REQUESTS_DENIED`, `RTPERF_CPU_USAGE_OK`, `RTPERF_CPU_THRESHOLD_EXCEEDED`, `LIBJNX_LOGIN_ACCOUNT_UNLOCKED`,  
`JSRPD_SET_OTHER_INTF_MON_FAIL`, `JSRPD_SET_SCHED_MON_FAILURE`, `UI_CHILD_WAITPID`, `UI_DBASE_LOGIN_EVENT`.   
2022-11-07 |  Enhancement-  
\- Mapped `subtype` to `metadata.product_event_type`.  
\- Mapped `attack-name` to `security_result.threat_name`.  
\- Mapped `policy-name` to `security_result.rule_name`.  
\- Mapped `action` to `security_result.action`, where value `drop` is mapped to BLOCK others to ALLOW.  
\- Mapped `source-interface-name` to `security_result.detection_fields`.  
\- Mapped `destination-interface-name` to `security_result.detection_fields`.  
\- Mapped `source-zone-name` to `security_result.detection_fields`.  
\- Mapped `destination-zone-name` to `security_result.detection_fields`.  
\- Mapped `service-name` to `security_result.detection_fields`.  
\- Mapped `application-name` to `security_result.detection_fields`.  
\- Mapped `metadata.product_name`  
\- Mapped `metadata.vendor_name`  
2022-10-04 |  Enhancement- Mapped attack-name to security_result.rule_name.  
\- Converted SDM mappings to following fields of UDM:-  
\- Mapped `source-address` to `principal.ip`.  
\- Mapped `destination-address` to `target.ip`.  
\- Mapped `source-port` to `principal.port`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `bytes-from-server` to `network.received_bytes`.  
\- Mapped `policy-name` to `security_result.rule_name`.  
\- Mapped `protocol-id` to `network.ip_protocol`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
