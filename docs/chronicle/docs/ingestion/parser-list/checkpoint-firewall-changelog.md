---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-firewall-changelog/
title: Change log for CHECKPOINT_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:49:07.721275+00:00
---

# Change log for CHECKPOINT_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHECKPOINT_FIREWALL

Date | Changes  
---|---  
2026-07-14 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `leef_version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Modified the date filter to parse the `devTime` raw log field as UNIX timestamp.  
\- `event.idm.read_only_udm.principal.asset.attribute.creation_time`: Modified the date filter to parse the `creation_time` raw log field as UNIX timestamp.   
2026-06-26 |  Enhancement:  
\- Modified the conditional check for mapping the `from` field to `event.idm.read_only_udm.network.email.from`. The mapping now only occurs if `from` matches the regex pattern.   
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: When `device_message` is `discard`, set the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `helo`,`inner_syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Modified a grok pattern to parse the syslog raw log fields.   
2026-04-13 |  Enhancement:  
\- Added a grok pattern on `message` to extract `syslog_priority`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-27 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/checkpoint-firewall   
2026-02-13 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `creation_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `last_hit_time` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `update_count`, `devTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `queue_id` , `process` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `from_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `from_host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `from_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `from_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `email_from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `email_to` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- Added support for new format of SYSLOG logs.  
\- Added gsubs to update field name for accurate KV parsing.  
\- Added `warning` to the list of severity values that map to MEDIUM severity.   
2026-01-21 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `program` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `syslog_host` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `icmp_type` and `icmp_code` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `precise_error` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action_reason`, `alert`, `message_type`, `UP_match_table`, `UP_match_table_2`, `ROW_START`, `ROW_START_2`, `match_id_2`, `ROW_END`, `ROW_END_2`, `layer_uuid_2`, `layer_name_2`, `rule_uid_2`, and `rule_name_2` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added gsub to fully parse the `reason` and `web_client_type` fields.  
\- Added a new grok pattern to parse logs with multiple fields matches.   
2025-12-30 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `deviceInboundInterface` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Grok filter added to extract IP from `origin`.  
\- New intermediate fields `objectname` and `deviceInboundInterface` were added.  
\- A previously commented-out block for merging `objecttable` into `_sr.category_details` was uncommented.   
2025-12-19 |  Enhancement:  
\- Modified the grok pattern to extract the full intermediary.hostname from the CN value, eliminating partial hostname extractions.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `dst_dynobj_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dst_object_type` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-12-15 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.intermediary.platform_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.intermediary.platform_version` UDM field.  
\- The conditional logic was updated to allow a value of `0` for `parent_rule` and `logid`.   
2025-12-11 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referrer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `scope`,`frequency`, `log_id`,`snid`,`suppressed_logs` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `dlp_incident_uid`, `https_inspection_action`, `usercheck`, `usercheck_confirmation_level`, `usercheck_incident_uid`,`usercheck_interaction_name` and `vendor_list` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-11-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `administrator` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `machine` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `machine` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `machine` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `machine` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `objectname` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.id`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` is set to `USER_RESOURCE_UPDATE_CONTENT` when the `product` is `SmartConsole` and `operation` is `Install Policy`.  
\- `event.idm.read_only_udm.security_result.action` is set to `ALLOW` if `audit_status` is `Success` and `BLOCK` otherwise for `SmartConsole` product events.   
2025-10-10 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `match_id`, `rule_uid`,`rule_name`,`parent_rule` and `layer_uuid` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-03 |  Enhancement:  
\- Added conditional check to prevent duplicate mapping of `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.hostname`.  
\- Added a grok pattern to extract `pid` from `header` field.   
2025-09-25 |  Enhancement:  
\- Added a gsub function for the `decision` field to transform `#decision=` into ` decision: `.  
\- Consolidated redundant code for `"event.idm.read_only_udm.security_result.detection_fields`, `event.idm.read_only_udm.additional.fields`, `event.idm.read_only_udm.principal.resource.attribute.labels`, and `event.idm.read_only_udm.target.resource.attribute.labels`.   
2025-09-11 |  Enhancement:  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac_address` raw log field(s) with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary2` field(s) with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mgmt_value` and `date_value` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary: Extracted hostname from `origin_sic_name` or `originsicname` and mapped with `event.idm.read_only_udm.intermediary` UDM field.  
\- Added a new grok pattern to parse `mgmt_value` and `date_value` from the __policy_id_tag field.   
2025-07-24 |  Enhancement:  
\- Added a gsub on `message` field to replace `Layer Name` with `layer_name`, `Policy Names` with `policy_name` and `Srcs.srcs` with `srcs_srcs`.  
\- Added a grok pattern to parse the raw log fields correctly.  
\- Used kv filter on `logic_changes_msg` and `field_changes_msg` extract the raw log fields.  
\- event.idm.read_only_udm.metadata.id: Newly mapped `uid` raw log field with `event.idm.read_only_udm.metadata.id`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_uid` raw log field with `event.idm.read_only_udm.network.session_id`.  
\- Added a grok pattern on`Source` to extract `srv_ip`  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Newly mapped `srv_ip` field with `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip` UDM fields if on_error flag `no_srv_ip_found` is false else map is to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Added a grok pattern on `logicchanges.Srcs_srcs` to extract `prod_id`.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `prod_id` field with `event.idm.read_only_udm.target.resource.product_object_id` if on_error flag `no_prod_id_found` is false else map is to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- Added gsub on `fieldschanges` and `logic_changes` to replace `\\\`` with `".  
\- event.idm.read_only_udm.additional.fields: Newly mapped `objectname` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `FollowUp`,`Protection`, `logic_changes_FollowUp`, `logic_changes_Protection` fields with `event.idm.read_only_udm.security_result.detection_fields`.   
2025-06-19 |  \- intermediary[1].ip: Removed mapping of `origin` from `intermediary[1].ip`.  
\- intermediary[0].ip: Mapped `origin` raw log field with `intermediary[0].ip` because `origin` raw log field corresponds to `CN` raw log field, which maps to intermediary[0].hostname.  
\- Added a Grok pattern to extract ip from raw log field `origin`.  
\- event.idm.read_only_udm.intermediary1.ip: Newly mapped `origin` raw log field with `event.idm.read_only_udm.intermediary1.ip` UDM field if `origin` and `originsicname` is not equals to null and `no_hostnameCN` flag is equals to false.  
\- Set the value of `origin_value_Set` field to `true` if `origin` is mapped to `event.idm.read_only_udm.intermediary1.ip` UDM field.  
\- Added a conditional check if `origin_value_Set` is equals to `false` before mapping `origin` raw log field with `event.idm.read_only_udm._intermediary.ip` UDM field.  
\- Modified a Grok pattern to extract `db_tag` raw log field from `__policy_id_tag` raw log field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `logid` and `db_tag` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-04-08 |  Enhancement:  
\- event.idm.read_only_udm.network.http.user_agent: Removed mapping of `web_client_type` from `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `web_client_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-03-27 |  Enhancement:  
\- Added a JSON block to parse the unparsed logs.  
\- Mapped `acks_total`, `attachments_num`, `arrival_time`,`attack_status`, `attack_traffic_bps`, `attack_traffic_pps`, `audit_status`, `auth_method`, `bandwidth`, `best_practice_id`, `blade_name`, `cb_rate`, `cb_recommendation`, `cb_relevantobjectname`, `cb_relevantobjectstatus`, `file_count`, `cb_scan_id`, `from`, `to`, `cb_status`, `cb_bp_blade`, `controller`, `delivery_time`, `device_identification`, `direction`, `discard_traffic_bps`, `discard_traffic_pps`, `dlp_data_type_name`, `dlp_relevant_data_types`, `dlp_rule_name`, `dlp_transport`, `dns_query_type`, `failure_reason`, `file_size`, `file_type` and `file_direction` to `additional.fields`.  
\- Mapped `client_name`, `d_name`, `data_type_name`, `email_queue_id`, `email_status`, `email_queue_name`, `user_status` and `vendor_list` to security_result.detection_fields".  
\- Mapped `destination_dns_hostname` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `email_content` to `security_result.description`.  
\- Mapped `email_subject` to `network.email.subject`.  
\- Mapped `event_name` to `metadata.description`.  
\- Mapped `web_client_type` to `network.http.user_agent`.  
\- Mapped `file_size` to `target.file_size`.  
\- Mapped `from` to `network.email.from`  
\- Mapped `to` to `network.email.to`.   
2025-03-24 |  Enhancement:  
\- Modified `security_result.severity` from `LOW` to `INFORMATIONAL` when `severity` is `0`.   
2025-03-10 |  Enhancement:  
\- Changed mapping of `contract_name` from `security_result.description` to `security_result.detection_fields` to prevent overriding in `security_result.description`.  
\- Added a condition check to remove the duplicate mapping of intermediary.ip.   
2025-03-06 |  Enhancement:  
\- Mapped `verdict` to `security_result.verdict_response`.  
\- Mapped `file_name` to `target.file.names`.  
\- Mapped `file_md5` to `target.file.md5`.  
\- Mapped `file_sha1` to `target.file.sha1`.  
\- Mapped `file_sha256` to `target.file.sha256`.   
2025-02-28 |  Enhancement:  
\- If Severity is `0`, `1`, and `2` then set `security_result.severity` to `LOW`.  
\- If Severity is `3` then set `security_result.severity` to `MEDIUM`.  
\- If Severity is `4` then set `security_result.severity` to `HIGH`.  
\- If Severity is `5` then set `security_result.severity` to `CRITICAL`.   
2025-02-26 |  Enhancement:  
\- Mapped `description` to `security_result.description`.   
2025-02-13 |  Enhancement:  
\- Removed conditional check for `Severity` and `severity`.   
2025-02-11 |  Enhancement:  
\- Added Grok patterns to parse `Severity`.  
\- Mapped `Name` to `security_result.detection_fields` and `security_result.about.resource.attribute.labels`.  
\- Mapped `Level` to `security_result.confidence_details`.  
\- Mapped `Impact` to `additional.fields`.  
\- Added a new Grok pattern including a conditional check for `Reference`.   
2025-02-07 |  Enhancement:  
\- Mapped `security_result.action` to `BLOCK` when `additional_info` is `Administrator failed to log`.  
\- Changed `origin` mapping from `principal.ip` and `principal.asset.ip` to `intermediary.ip` and `intermediary.asset.ip`.  
\- Changed `administrator` mapping from `security_result.detection_fields` to `target.user.userid`.  
\- Mapped `machine` to `target.hostname` and `target.asset.hostname`.   
2025-02-06 |  Enhancement:  
\- When `severity` is `5` then set `security_result.severity` to `HIGH`.   
2025-01-31 |  Enhancement:  
\- Mapped value of `CN` under `originsicname` to `intermediary.hostname`.   
2025-01-09 |  Enhancement:  
\- Removed extra space from `principal.ip`.  
\- Mapped `user` to `principal.user.user_display_name`.   
2025-01-08 |  Enhancement:  
\- Mapped `src` to `principal.hostname` when `src` is not a valid IP.   
2025-01-01 |  Enhancement:  
\- Mapped `security_result.action` to `ALLOW` when `_action` is `Bypass,bypass`.   
2024-11-27 |  Enhancement:  
\- Mapped `operation_number` to `security_result.detection_fields`.  
\- Mapped `client_ip` to `principal.ip` and `principal.asset.ip`.   
2024-11-26 |  Enhancement:  
\- Mapped `src` to `principal.hostname` and `principal.asset.hostname`.   
2024-11-21 |  Enhancement:  
\- Added a Grok pattern to map `resource` to `target.url`.   
2024-11-04 |  Enhancement:  
\- Mapped `cu_rule_category` value to `security_result.rule_name`.   
2024-10-30 |  Enhancement:  
\- Modified the Grok pattern to extract correct `service` data.   
2024-10-14 |  Enhancement:  
\- Mapped `log Update` value to `additional.fields`.  
\- Mapped `log_sys_message` to `metadata.description`.   
2024-09-18 |  Enhancement:  
\- When `Action` is equal to `Prevent`, then mapped `security_result.action` to `BLOCK`.   
2024-08-30 |  Enhancement:  
\- Mapped `layer_name` to `security_result.detection_fields`.   
2024-08-28 |  Enhancement:  
\- Modified the condition to parse new format of SYSLOG + KV logs.   
2024-08-14 |  Enhancement:  
\- Added a `gsub` for field `service`.   
2024-08-13 |  Enhancement:  
\- Removed `target.ip` and `target.asset.ip` mappings for `origin`.   
2024-08-02 |  Enhancement:  
\- Mapped `feature_name` and `securexl_message` to `additional.fields`.   
2024-07-30 |  Enhancement:  
\- Mapped `emailSubject` to `network.email.subject`.  
\- Mapped `cat` to `security_result.detection_fields`.  
\- Mapped `url` to `principal.url`.  
\- Mapped `srcPostNAT` to `principal.nat_ip`.  
\- Mapped `dstPostNAT` to `target.nat_ip`.  
\- Mapped `srcPostNATPort` to `principal.nat_port`.  
\- Mapped `dstPostNATPort` to `target.nat_port`.  
\- Removed mapping for field `origin` from `target.ip`.   
2024-07-18 |  Enhancement:  
\- Added support for some of the unmapped fields for product `Application Control`  
2024-07-11 |  Reviewer-suggested edit  
Enhancement:  
\- Mapped svc to the target port.  
\- Added if block for the `action.details` value `0`.  
\- Added null check for `security_result.detection_fields`.   
2024-06-26 |  Enhancement:  
\- Added support for some of the unmapped fields(CEF format logs) for product `VPN-1 & FireWall-1`  
\- list of fields added:  
\- fw_subproduct  
\- src_user_dn  
\- hll_key  
\- nat_rulenum  
\- security_inzone  
\- security_outzone  
\- snid  
\- drop_reason  
\- reason  
\- match_id  
\- parent_rule  
\- ifname  
\- logid  
\- sequencenum  
\- version  
\- service_id  
\- community  
\- lastupdatetime  
\- vpn_feature_name  
\- conn_direction  
\- contextnum  
\- context_num  
\- certificate_validity  
\- nat_addtnl_rulenum  
\- nat_rule_uid  
\- needs_browse_time  
\- sig_id  
\- sni  
\- tls_server_host_name  
\- log_delay  
\- dst_user_dn  
\- rpc_interface_uuid  
\- icmp   
2024-06-14 |  Enhancement:  
\- If `Action` is `Detect` or `detect`, then changed the mapping of `security_result.action` from `QUARANTINE` to `ALLOW`.   
2024-06-11 |  Enhancement:  
\- Mapped `dns_query` to `network.dns.questions`.   
2024-05-29 |  Enhancement:  
\- Mapped `layer_uuid_rule_uuid` to `security_result.rule_id`.  
\- Mapped `domain` to `principal.administrative_domain`.  
\- Mapped `fservice`, `appi_name`, `app_risk`, and `policy_name` to `security_result.detection_fields`.  
\- Mapped `packets`, `__id`, `dedup_time`, `browse_time`, `bytes`, `product_family`, `hll_key`, and `calc_service` to `additional.fields`.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `orig_log_server` to `principal.resource.product_object_id`.  
\- Mapped `environment_id` to `target.resource.product_object_id`.  
\- Mapped `client_outbound_packets` and `client_inbound_packets` to `principal.resource.attribute.labels`.  
\- Mapped `server_outbound_bytes` and `server_inbound_bytes` to `target.resource.attribute.labels`.  
\- Mapped `orig` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `orig_log_server_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `proto` to `network.ip_protocol`.   
2024-05-20 |  Enhancement:  
\- Added a Grok pattern to extract `inter_host`.  
\- Mapped `inter_host` to `intermediary.hostname`.   
2024-04-19 |  Enhancement and Bug-Fix:  
\- Mapped `origin` to `target.ip` and `target.asset.ip`.  
\- Added new Grok patterns to parse new format of SYSLOG logs.  
\- Mapped `smartdefense_profile`, `malware_rule_id`, and `malware_rule_name` to `security_result.detection_fields`.  
\- Mapped `sequencenum`, `description_url`, `industry_reference`, `mitre_execution`, `packet_capture_name`, `packet_capture_unique_id`, `packet_capture_time`, and `performance_impact` to `additional.fields`.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `http_host` to `target.resource.attribute.labels`.  
\- Mapped `log_id` to `metadata.product_log_id`.  
\- Mapped `user_agent` to `network.http.user_agent` and `http.parsed_user_agent`.  
\- Mapped `hostname`, `dvc`, and `principal_hostname` to `target.hostname` and `target.asset.hostname`.  
\- If `has_principal` is `true`, `has_target` is `true`, and `Action`/`action` is `Log In` or `Failed Log In` or `Failed Login` or `Update`, then set `metadata.event_type` to `USER_LOGIN` and `extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- If `has_principal` is `true`, `has_target` is `true`, and `Action`/`act`/`event_type` is `Log Out` or `Logout`, then set `metadata.event_type` to `USER_LOGOUT` and `extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- If `has_principal` is `true`, `has_target` is `true`, then set `metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `has_principal` is `true`, `has_target` is `false`, then set `metadata.event_type` to `STATUS_UPDATE`.   
2024-02-07 |  Enhancement: Added mapping for the following fields:  
\- Mapped `protection_id`, `malware_action`, `malware_family,protection_name`, `protection_type` to `security_result.detection_fields`.  
\- Mapped `confidence_level` to `security_result.confidence` and `security_result.confidence_details`.   
2024-02-05 |  Enhancement: Added mapping for the following fields:  
\- Mapped `method` to `network.http.method`.   
2024-01-24 |  Enhancement: Added mapping for the following fields:  
\- Mapped `method` to `network.http.method`.  
\- Mapped `duration` to `network.session_duration.seconds`.  
\- Mapped `additional_info` to `security_result.description`.  
\- Mapped `operation` to `security_result.summary`.  
\- Mapped `subject` to `metadata.description`.  
\- Mapped `principal_hostname` to `intermediary.hostname`.  
\- Mapped `tcp_packet_out_of_state`, `aggregated_log_count`, `connection_count`, `appi_name`, `src_user_dn`,  
`update_count`, `additional_info`, `administrator`, `operation`, `sendtotrackerasadvancedauditlog`,  
`subject`, `fieldschanges`, `logic_changes`, `objecttype`, `session_description`,  
`session_name` to `security_result.detection_fields`.   
2023-12-27 |  Enhancement: Added mapping for the following fields:  
\- Mapped `flags` to `security_result.detection_fields`.  
\- Mapped `tcp_flags` to `security_result.detection_fields`.  
\- Mapped `tcp_packet_out_of_state` to `security_result.detection_fields`.   
2023-12-11 |  Enhancement:  
\- If `principal_hostname` is a valid ip, mapped it to `principal.ip`.  
\- If `principal_hostname` is not a valid ip, mapped it to `principal.hostname`.  
\- Mapped `sport_svc` to `principal.port`.  
\- Mapped `ProductFamily` to `additional.fields`.  
\- Mapped `mitre_initial_access` to `security_result.detection_fields`.  
\- Mapped `policy_time` to `security_result.detection_fields`.  
\- Mapped `profile` to `security_result.detection_fields`.  
\- Mapped `reject_id_kid` to `security_result.detection_fields`.  
\- Mapped `ser_agent_kid` to `security_result.detection_fields`.   
2023-10-11 |  Enhancement:  
\- If `product` is `New Anti Virus`, then the mapping from `firewall management node` to `principal.hostname` is removed and instead mapped to `security_result.detection_fields`.   
2023-07-06 |  Enhancement: Added mapping for the following fields:  
\- Mapped `app_category` to `security_result.category_details`.  
\- Mapped `matched_category` to `security_result.detection_fields`.  
\- Mapped `app_properties` to `security_result.detection_fields`.   
2023-06-14 |  Enhancement: Added mapping for following fields  
\- Mapped `conn_direction` to `additional.fields`.  
\- Modified gsub's so as not to replace the `:` with `=` from actual values.   
2023-05-12 |  Enhancement: Added mapping for following fields  
\- Mapped `rule_name` to `security_result.rule_name`.  
\- Mapped `rule`,`sub_policy_name`,`sub_policy_uid`,`smartdefense_profile`,`tags`,`flexString2` to `security_result.detection_fields`.  
Enhancement:  
\- Added new Grok pattern to support the new log formats.  
\- Mapped `dvc` to `intermediary.hostname`.  
\- Mapped `hostname` to `intermediary.hostname`.  
\- Mapped `origin_sic_name` to `intermediary.asset_id`.  
\- Mapped `conn_direction` to `network.ip_protocol`.  
\- Mapped `ifname` to `security_result.detection_fields`.  
\- Mapped `security_inzone` to `security_result.detection_fields`.  
\- Mapped `match_id` to `security_result.detection_fields`.  
\- Mapped `parent_rule` to `security_result.detection_fields`.  
\- Mapped `security_outzone` to `security_result.detection_fields`.  
\- Mapped `sub_policy_name` to `security_result.detection_fields`.  
\- Mapped `sub_policy_uid` to `security_result.detection_fields`.  
\- Mapped `drop_reason` to `security_result.summary`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `xlatesport` to `principal.nat_port`.  
\- Mapped `xlatedport` to `target.nat_port`.  
\- Mapped `ipv6_dst` to `target.ip`.  
\- Mapped `ipv6_src` to `principal.ip`.   
2023-04-24 |  Enhancement:  
\- Added support for logs with CEF format.   
2022-11-18 |  Enhancement:  
\- Modified mapping for `service` and mapped it to `target.port`.   
2022-10-27 |  Enhancement:  
\- Added conditional check for `attack`,`attack_info`,`policy_name`.  
\- Added grok pattern to retrieve `principal_hostname`.  
\- Added gsub to change `=` to `:`.  
\- Modified mapping for `service` and mapped it to `target.resource.attribute.labels`.   
2022-10-13 |  Enhancement:  
\- Mapped the field `fw_subproduct` to `metadata.product_name`.  
\- Added grok pattern to extract the ip form the field `src`.   
2022-08-30 |  Enhancement:  
\- Merged the changes of Customer-specific versions to default.  
\- Undropped the logs containing `*****` in UserCheck.   
2022-08-18 |  Enhancement:  
\- Mapped `portal_message` to `security_result.description`.  
\- Mapped `security_result.category` as `SOFTWARE_MALICIOUS` in case `portal_message` contains keywords `malware/malicious`.  
\- Mapped `URL` to `security_result.about.url`.  
\- Mapped `Activity` to `security_result.summary`.  
\- Mapped `Reference` to `security_result.about.resource.attribute.labels`.  
\- Modified `event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` by replicating the value of `intermediary.ip` to `principal.ip`.   
2022-08-12 |  Enhancement:  
\- Mapped `malware_action`, `malware_family,protection_name`, `protection_type` to `security_result.about.resource.attribute.labels`.  
\- Mapped `src_machine_name` to `security_result.detection_fields`.   
2022-06-30 |  Enhancement:  
\- Mapped `message_info` to `metadata.description`.   
2022-06-17 |  Enhancement:  
\- Added conditional checks for fields `nat_rulenum`, `rule`, `sent_bytes`, `received_bytes`, `s_port`, `service`.  
\- Modified event_types for the following cases:  
\- `GENERIC_EVENT` to `NETWORK_CONNECTION` where `principal.ip or principal.hostname` and `target.ip or target.hostname` are not null.  
\- `GENERIC_EVENT` to `STATUS_UNCATEGORIZED` where `principal.ip or principal.hostname` is not null.   
2022-06-14 |  Enhancement:  
\- Modified the parser to parse more logs by removing the condition check for passwd.   
2022-06-07 |  Enhancement:  
\- Mapped src_machine_name to security_result.detection_fields.   
2022-05-19 |  Enhancement:  
\- Mapped inzone, outzone, layer_name, layer_uuid and policy_name to security_result.detection_fields.  
\- Mapped service_id to principal.application.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
