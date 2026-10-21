---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/radware-firewall-changelog/
title: Change log for RADWARE_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:16:12.352010+00:00
---

# Change log for RADWARE_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/radware-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RADWARE_FIREWALL

Date | Changes  
---|---  
2026-05-05 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.application`: Removed mapping of `component` from `event.idm.read_only_udm.intermediary.application` UDM field. As it was not a valid mapping.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `component` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `device_module` from `event.idm.read_only_udm.additional.fields` UDM field. As it was not a valid mapping.  
\- `event.idm.read_only_udm.metadata.product_name`: Mapped `device_module` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.   
2026-04-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Changed mapping of `radware_field_1`, `radware_field_2`, `radware_field_3`, `radware_field_4` raw log fields from `event.idm.read_only_udm.additional.fields.number_value` to `event.idm.read_only_udm.additional.fields.string_value`.   
2026-04-10 |  Enhancement:  
\- Added a Grok pattern on the `message` field to parse new format of SYSLOG logs.  
\- Added a Grok pattern on `kv_data4` to extract key-value pairs.  
\- Added a Grok pattern on `req` to extract `http_version`, `hostip`, `connection`, `user_agent` and `accept_encoding` raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed `SVC` raw log field with `event.idm.read_only_udm.additional.fields` UDM field because, it represents network.ip_protocol rather than additional.fields.  
\- `event.idm.read_only_udm.network.ip_protocol`: Mapped `SVC` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `webappname` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `tunnel` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sport` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `threatcategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field. If `severity` is empty, updated the value of `event.idm.read_only_udm.security_result.severity` to severity_1.  
\- `event.idm.read_only_udm.security_result.detection_fields`: If `vhost` is empty, updated the value of `event.idm.read_only_udm.security_result.detection_fields` to `vhost_1`.  
\- `event.idm.read_only_udm.principal.url`: If `apath` is empty, updated the value of `event.idm.read_only_udm.principal.url` to `apath_1`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: If `lip` is empty, updated the value of `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` to `lip_1`.  
\- `event.idm.read_only_udm.additional.fields`: If `lport`, `milli`, `tmodule` is empty, updated the value of `event.idm.read_only_udm.additional.fields` to `lport_1`, `milli_1`, `tmodule_1`.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `component` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.observer.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `attackname` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- Added a conditional check to map `msg_host` to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` if it is a valid IP address, otherwise map to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.   
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`:  
if `radware_field_1`, `radware_field_2`, `radware_field_3`, `radware_field_4` is a number, then mapped with `event.idm.read_only_udm.additional.fields.number_value` UDM field.  
if `radware_field_1`, `radware_field_2`, `radware_field_3`, `radware_field_4` is a string, then mapped with `event.idm.read_only_udm.additional.fields.string_value` UDM field.   
2026-03-25 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.threat_name`: Removed mapping of `attack_type` log field from `event.idm.read_only_udm.security_result.threat_name` UDM field to introduce a more appropriate UDM field mapping.  
\- `event.idm.read_only_udm.security_result.category_details`: Mapped `attack_type` log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Removed mapping of `description` value (extracted from SYSLOG message) from `event.idm.read_only_udm.security_result.description` UDM field to introduce a more appropriate UDM field mapping.  
\- Renamed a field name in grok patterns from `description` to `threat_name` for better naming convention.  
\- `event.idm.read_only_udm.security_result.threat_name`: Mapped `threat_name` value (extracted from SYSLOG message) with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product_name` log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- Renamed the key name for log field `radware_field_1` from `radware_field_1` to `physical_port`.  
\- Renamed the key name for log field `radware_field_2` from `radware_field_2` to `packet_count`.  
\- Renamed the key name for log field `radware_field_3` from `radware_field_3` to `volume_kbits`.  
\- Renamed the key name for log field `radware_field_4` from `radware_field_4` to `vlan_id`.  
\- `event.idm.read_only_udm.network.ip_protocol`: If `protocol` contains `UDP`, then set `event.idm.read_only_udm.network.ip_protocol` to `UDP`.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `forward`, then set `event.idm.read_only_udm.security_result.action` to `ALLOW`.   
2026-03-12 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- Added a new grok pattern for the `message_description` field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `apath` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version`, `refinecrc_field`, `refine_field`, `Hosts`, `connection`, `access`, `Origin`, `sec_fetch`, `fetch_site`, `fetch_dest`, `Referer`, `accept_encoding`, `req` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `directory` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `request_header` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- The updated grok pattern now allows the fields to parse properly and the following fields are now being mapped correctly:  
\- `event.idm.read_only_udm.intermediary.ip`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.url`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.target.application`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.url`  
2026-03-06 |  Enhancement:  
\- Modified the order of the grok patterns to allow specific DefensePro logs to match correctly, enabling the following UDM fields:  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.category`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.threat_name`  
\- `event.idm.read_only_udm.target.resource.product_object_id`  
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `record_name`, `record_violation_reason` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `record_category`, `record_bot_category` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `record_totalVolume` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `record_totalPackets`, `record_session_cookie`, `record_headers`, `country_Code` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `record_ID`, `record_tid` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record_status`, `record_signature_pattern` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `record_site` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `record_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `record_ip`, `record_sourceIP` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `record_ua` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `record_policy_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `record_destinationIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `record.time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_protocol_output` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `app_protocol_src` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.   
2026-02-11 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `community` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `login_result` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.   
2026-02-06 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `enrichmentContainer_geoLocation_countryCode` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.labels`: Newly mapped `contractId` raw log field with `event.idm.read_only_udm.target.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `applicationId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `record.enrichmentContainer.owaspCategory2021`, `module`, `refinecrcvalue` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host`, `msg_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `externalIp`, raw log fields with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http_version`, `tenant`, `role`, `targetModule`, `security`, `title`, `violationCategory`, `violationType`, `webApp`, `cookie`, `lport`, `pragma`, `cache_control`, `accept_charset` `accept_language`, `accept_header`, `milli`, `devtype`, `act`, `dir`, `attackrisk`, `SVC`, `msg_title`, `min`, `policy`, `protection`, `useraction`, `role`, `user`, `severity_code`, `tmodule`, `uriii`, `vhosts`, `msg_parameter`, `msg_module`, `msg_error_number`, `device_module`, `vhost`, `vhost_field`, `request_uri`, `authenticated_role_name`, `authenticated_role_id`, `user_name`, `user_authentication`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceIp`, `lip_IP`, `extip`, `dip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `violationDetails`, `subj` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `transId`, `evtid` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `applicationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `receivedTimeStamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `apath` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `req` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `engineversion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `et` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `host_ip`, `sip`, `lip`, `dhost` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `cmip`, `sourceIp` raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `lport`, `dport` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `msg_referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `msg_suggestion` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `msg_authenticated_as` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent_val` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.   
2026-01-29 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_level`, `radware_field_1`, `radware_field_2`, `radware_field_3`, `radware_field_4`, `radware_field_5`, `type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2025-11-26 |  Enhancement:  
\- Modified grok patterns to parse raw log fields.  
\- event.idm.read_only_udm.network.sent_bytes: Changed mapping for event.idm.read_only_udm.network.sent_bytes. It was previously mapped from the field at the 16th position in the grok pattern (originally named as sent_bytes, now named Packet_Count). It is now mapped from the field at the 17th position in the grok pattern (originally unnamed,now named sent_bytes), which represents the `sent_bytes` from the raw log.  
\- event.idm.read_only_udm.additional.fields: Newly mapped raw log fields `Physical_port`, `Context`, `VLAN_Tag` and `MPLS_Tag` to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.network.sent_packets: Newly mapped raw log field `Packet_Count` to event.idm.read_only_udm.network.sent_packets.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped raw log fields `Attack_Status` and `MPLS_RD` to event.idm.read_only_udm.security_result.detection_fields.   
2025-10-21 |  Enhancement:  
\- Added a new Grok pattern to parse a newer format of SYSLOG logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `Type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `SourceIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `SourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `WebUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.role_name: Newly mapped `Role` raw log field with `event.idm.read_only_udm.principal.user.role_name` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `WebApp, `application` raw log fields with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `URI` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `TransID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field (extracted from Description) with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `ref_url` raw log field (extracted from Description) with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AppPath, `Resource, `Object, `Tunnel, `ParamName, `ParamValue, `ParamType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `syslog_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `ServerName, `syslog_ip` raw log fields with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `Description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `Title` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `Attackname` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `RuleID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `Threatcategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `Priority` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `IsPassive` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2025-08-18 |  Enhancement:  
\- Added a new Grok pattern to parse a newer format of `DefensePro` logs.  
\- Added a new Grok pattern to enable the extraction of the `threat_id` field.  
\- Enhanced Grok patterns to improve parsing of `login failure` and `access attempt` events from the `description` field.  
\- event.idm.read_only_udm.security_result.threat_id: Newly mapped `threat_id` log field to `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `attack_id` log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2025-06-09 |  Enhancement:  
\- Modified grok pattern to parse `event.idm.read_only_udm.network.sent_bytes`.   
2025-05-28 |  Enhancement:  
\- Added GROK pattern to parse the JSON logs containing malformed characters.  
\- Added a conditional check before mapping `enrichmentContainer.geoLocation.countryCode` to `event.idm.read_only_udm.principal.location.country_or_region` udm field.  
\- Added gsub to replace `\\r\\n`,`\\n`,`\\\\r\\\\n` with ` ` on `request` raw log field.  
\- Added gsub to replace `\\n`,`\\\\n` with ` ` and `\\r` with "` on `violationDetails" raw log field.  
\- Added GROK patterns to extract `msg1`, `http_status_code`, `authenticated_role_name`, `authenticated_role_id`, `user_name`, `user_authentication`,`src_page_details`,`rule_id_`, `details_` ,`description_`, `http_message_base`, `error_number`, `authentication_status`,`severity` from `violationDetails` raw log field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `msg1` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `http_status_code` field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `authenticated_role_name` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `authenticated_role_id` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `user_name` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `user_authentication` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `src_page_details` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `rule_id_` field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `details_` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `description_` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `http_message_base` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `error_number` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `authentication_status` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity_` field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-05-15 |  Enhancement:  
\- Added gsub to replace `\`\\\$\`` with `$` ,(`\\\\\`` and `\`\\..\``) with ``, ``%`` with `\\\\\`%\\\`` , ``=`` with `\\\\\`=\\\"`.  
\- Added a Grok pattern to extract `x_forwarded_for_ip` from `request` raw log field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `x_forwarded_for_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.   
2025-05-14 |  Enhancement:  
\- Added gsub function to replace character to parse the JSON logs `json_message` field.  
\- Replaced ``>` with ``>`.  
\- Replaced `="` with `='`.  
\- Replaced `=',` with `=",`.  
\- Replaced `"""` with ``.  
\- Replaced `\\s"\\s` with ``.  
\- Added GROK pattern to parse the JSON logs containing malformed characters.  
\- Added gsub function to replace `\\\\\\\\r\\\\\\\\n``, ``\\\\r\\\\n"` and `\\r\\n` with `,` on `request_data` field.  
\- Added gsub function to remove `\\"` on `role` field.  
\- Added kv filter on `request` field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `apikey`, `canary`, `client-version`, `content-type`, `client-request-id`, `X-RDWR-APP-ID`, `X-RDWR-IP`, `X-RDWR-PORT`, `X-RDWR-PORT-MM`, `X-RDWR-PORT-MM-ORIG-FE-PORT`, `hpgrequestid`, `accept-language`, `purpose`, `upload-time`, `site` and `headers` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Converted `totalVolume` and `totalPackets` raw log field to string then mapped with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `client-request-id`, `client-id`, `category`, `policy_id`, `signature_pattern`, `status` and `violation_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent,event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `user-agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent,event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `destinationIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `sourceIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `name` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `country_code` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.network.session_id : Newly mapped `session_cookie` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `tid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent, event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `ua` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `sec_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- Set `sec_action` to `ALLOW` if `action` is `(?i)allow`.  
\- Set `sec_action` to `BLOCK` if `action` is `(?i)deny`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `bot_category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- Added a conditional check to drop malformed logs.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `externalIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `Referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referrer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.   
2025-05-07 |  Enhancement:  
\- Added support for new pattern of SYSLOG+KV logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `hostip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `hostip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `time` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `et`, `total_bytes`, `blocked_bytes`, `passive_bytes`, `clean_bytes`, `tunnel_name`, and `tunnel_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-06 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `message_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `rule_id` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.metadata.action_details` UDM field.   
2025-04-25 |  Enhancement:  
\- `JSON`: Added support for `JSON` format.  
\- subevent.idm.read_only_udm.sec_result.action, subevent.idm.read_only_udm.sec_result.action_details: Newly mapped `action` raw log field with `subevent.idm.read_only_udm.sec_result.action` UDM field and `subevent.idm.read_only_udm.sec_result.action_details` UDM field.  
\- subevent.idm.read_only_udm.additional.fields: Newly mapped `application_id`, `accept_language`, `cookie` raw, `request`, `received_timestamp`, `tenant_name`, `x-forwarded-for` raw log field with `subevent.idm.read_only_udm.additional.fields` UDM field.  
\- subevent.idm.read_only_udm.principal.application: Newly mapped `application_name` raw log field with `subevent.idm.read_only_udm.principal.application` UDM field.  
\- subevent.idm.read_only_udm.principal.location.country_or_region: Newly mapped `country_code` raw log field with `subevent.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- subevent.idm.read_only_udm.target.ip, subevent.idm.read_only_udm.target.asset.ip: Newly mapped `destination_ip` raw log field with `subevent.idm.read_only_udm.target.ip and subevent.idm.read_only_udm.target.asset.ip UDM fields.  
\- subevent.idm.read_only_udm.target.port: Newly mapped `destination_port` raw log field with `subevent.idm.read_only_udm.target.port` UDM field.  
\- subevent.idm.read_only_udm.principal.process.file.full_path: Newly mapped `directory` raw log field with `subevent.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- subevent.idm.read_only_udm.principal.hostname, subevent.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field with `subevent.idm.read_only_udm.principal.hostname and subevent.idm.read_only_udm.principal.asset.hostname UDM fields.  
\- subevent.idm.read_only_udm.network.sent_bytes: Newly mapped `http_bytes_in` raw log field with `subevent.idm.read_only_udm.network.sent_bytes` UDM field.  
\- subevent.idm.read_only_udm.network.received_bytes: Newly mapped `http_bytes_out` raw log field with `subevent.idm.read_only_udm.network.received_bytes` UDM field.  
\- subevent.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `subevent.idm.read_only_udm.network.http.method` UDM field.  
\- subevent.idm.read_only_udm.network.application_protocol: Newly mapped `protocol` raw log field with `subevent.idm.read_only_udm.network.application_protocol` UDM field.  
\- subevent.idm.read_only_udm.network.http.referral_url: Newly mapped referrer` raw log field with `subevent.idm.read_only_udm.network.http.referral_url UDM field.  
\- subevent.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field with `subevent.idm.read_only_udm.network.http.response_code` UDM field.  
\- subevent.idm.read_only_udm.principal.ip, subevent.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` raw log field with `subevent.idm.read_only_udm.principal.ip and subevent.idm.read_only_udm.principal.asset.ip UDM fields.  
\- subevent.idm.read_only_udm.principal.port: Newly mapped `source_port` raw log field with `subevent.idm.read_only_udm.principal.port` UDM field.  
\- subevent.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `subevent.idm.read_only_udm.metadata.event_timestamp UDM field, supporting dd/MMM/yyyy:HH:mm:ss.SSS Z and dd/MMMM/yyyy:HH:mm:ss.SSS Z formats.  
\- subevent.idm.read_only_udm.network.http.user_agent: Newly mapped `user_agent` raw log field with `subevent.idm.read_only_udm.network.http.user_agent` UDM field.  
\- subevent.idm.read_only_udm.metadata.vendor_name: Set vendor_name to Radware.  
\- subevent.idm.read_only_udm.metadata.event_type: Implemented logic to set the event_type based on the presence of principal, target and network data.  
\- Added a conditional check to check if the log is a JSON array of events or not.  
\- Added a drop condition to drop malformed logs.   
2025-04-05 |  Enhancement:  
\- Added a Grok pattern to parse SYSLOG logs.   
2025-02-11 |  Enhancement:  
\- Mapped `applicationName` to `principal.application`.  
\- Mapped `action` to `security_result.action_details`.  
\- Mapped `appPath` to `principal.file.full_path`.  
\- Mapped `destinationIp` to `target.ip` and `target.asset.ip`.  
\- Mapped `destinationPort` to `target.port`.  
\- Mapped `directory` to `principal.process.file.full_path`.  
\- Mapped `enrichmentContainer.geoLocation.countryCode` to `principal.location.country_or_region`.  
\- Mapped `enrichmentContainer.contractId` to `additional.fields`.  
\- Mapped `applicationId` to `additional.fields`.  
\- Mapped `tenant` to `additional.fields`.  
\- Mapped `owaspCategory2021` to `additional.fields`.  
\- Mapped `externalIp` to `intermediary.ip`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `passive` to `additional.fields`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `request` to `additional.fields`.  
\- Mapped `role` to `principal.user.role_name`.  
\- Mapped `security` to `additional.fields`.  
\- Mapped `sourceIp` to "`principal.ip` and `principal.asset.ip`.  
\- Mapped `sourcePort` to `principal.port`.  
\- Mapped `targetModule` to `additional.fields`.  
\- Mapped `title` to `metadata.description`.  
\- Mapped `transId` to `additional.fields`.  
\- Mapped `URI` to `target.file.full_path`.  
\- Mapped `user` to `principal.user.role_description`.  
\- Mapped `vhost` to `security_result.detection_fields`.  
\- Mapped `violationCategory` to `additional.fields`.  
\- Mapped `violationDetails` to `security_result.summary`.  
\- Mapped `violationType` to `security_result.description`.  
\- Mapped `webApp` to `additional.fields`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `paramName` to `additional.fields`.  
\- Mapped `paramValue` to `additional.fields`.  
\- Mapped `paramType` to `additional.fields`.  
\- Mapped `receivedTimeStamp` to `metadata.event_timestamp`.   
2024-09-17 |  Enhancement:  
\- Added support to map all `src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Added support to map all `dst_ip` to `target.ip` and `target.asset.ip`.   
2024-07-23 |  Enhancement:  
\- Added Grok patterns to parse a new pattern of syslog logs.   
2024-06-18 |  Enhancement:  
\- Reordered the Grok patterns to optimize the parsing time.   
2024-06-11 |  Enhancement:  
\- Added Grok patterns to parse unparsed logs.   
2023-12-08 |  Enhancement:  
\- Modified a Grok pattern to properly parse `src_ip`.   
2023-11-23 |  Enhancement:  
\- Added new Grok patterns to support new unparsed pattern of SYSLOGS.  
\- Added support for new date pattern of `ts`.  
\- Initialized `attack_type`, `attack_desc`, `protocol_number_src`, `security_result`, `action`, `product` to null.  
\- Added null check to `product` before mapping to `event.idm.read_only_udm.metadata.product_name`.  
\- Added null check to `rule_id` before mapping to `event.idm.read_only_udm.security_result.rule_id`.  
\- Added null check to `attack_desc` before mapping to `event.idm.read_only_udm.security_result.description`.  
\- Added null check to `attack_type` before mapping to `event.idm.read_only_udm.security_result.threat_name`.  
\- Mapped `username` to `event.idm.read_only_udm.principal.user.userid`.  
\- Mapped `command` to `event.idm.read_only_udm.principal.process.command_line`  
\- Mapped `description` to `event.idm.read_only_udm.security_result.description`.  
\- Mapped `intermediary_ip` to `event.idm.read_only_udm.intermediary.ip`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
