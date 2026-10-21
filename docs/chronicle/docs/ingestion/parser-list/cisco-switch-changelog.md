---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-switch-changelog/
title: Change log for CISCO_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:29:04.319063+00:00
---

# Change log for CISCO_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_SWITCH

Date | Changes  
---|---  
2026-07-03 |  Enhancement:  
\- Added a Grok pattern to parse new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app` log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `system_process` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `restart_sec`, `bytes_usage` log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-01 |  Enhancement:  
\- Renamed grok variable from `device` to `intermediary_ip` for better naming convention.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `device` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as the field was containing the hostname from the log header (an intermediary device), not the actual principal device.  
\- event.idm.read_only_udm.intermediary.hostname and event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `intermediary_ip` raw log field to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `MessageSourceAddress` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `SourceModuleName` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.observer.application: Newly mapped `SourceModuleType` raw log field to `event.idm.read_only_udm.observer.application` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `server_name` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `server_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- Added a new grok pattern to parse the new `SYSLOG` format logs.   
2026-05-06 |  Enhancement:  
\- Modified `header_data` grok pattern to parse `intermediary_ip` field.  
\- Renamed grok variable from `device_ip` to `intermediary_ip` for better naming convention.  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `device_ip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields, as this IP is now parsed as `intermediary_ip`.  
\- `event.idm.read_only_udm.target.ip`: Removed mapping of `device_ip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields, as this IP is now parsed as `intermediary_ip`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-04-29 |  Enhancement:  
\- `event.idm.read_only_udm.target.url`: Newly mapped `target_url` log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `error_code` and `error_message` log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Modified a grok pattern to parse the correct hostname from the log.  
\- Added a new grok pattern to parse the `description` field.   
2026-04-16 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.intermediary.resource.attribute.labels`: Newly mapped `vlan_data` raw log field with `event.idm.read_only_udm.intermediary.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `source_ip` from `event.idm.read_only_udm.principal.ip` UDM field. As it was incorrectly mapped.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `source_ip` from `event.idm.read_only_udm.principal.asset.ip` UDM field. As it was incorrectly mapped.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.   
2026-04-07 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for all possible timezones to parse the `event.idm.read_only_udm.metadata.event_timestamp` with the correct timezone.  
\- Added a grok pattern to extract `year` from the `message` header to parse the `event.idm.read_only_udm.metadata.event_timestamp` with the correct `year`.   
2026-04-02 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Product_event_id` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added support for date format in time_stamp field.  
\- Added a grok pattern on `description` to extract `state` raw log field.   
2026-03-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `process_name`, `switch_id`, `log_seq_num`, `log_seq_num_2` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `p_interface` raw log field(s) with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `audit_session_id` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `mac` raw log field(s) with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `packets` raw log field(s) with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- Added new grok patterns to parse the logs correctly.  
\- Added new fields to the overwrite list in the main grok filter: intermediary_ip, intermediary_hostname, log_seq_num_2, log_seq_num.  
\- Added a new grok filter to parse fields from the description field.   
2026-03-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `device` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field when `device` contains numerical digit only value. This numerical value is syslog sequence number.  
\- `event.idm.read_only_udm.additional.fields`: If `device` contains numerical digit only value, Set `device` (key: `syslog_sequence_number`) raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a grok pattern on `description` to extract `resource_name`, `target_app`, `target_host`, `session_id`.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `resource_name` log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_app` log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_host` log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` log field to `event.idm.read_only_udm.network.session_id` UDM field.   
2026-03-09 |  Enhancement:  
\- Added an uppercase mutation to the timezone field.  
\- event.idm.read_only_udm.principal.resource.type: Removed mapping of `facility` from `event.idm.read_only_udm.principal.resource.type` UDM field as this field is deprecated.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `facility` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `seq_num` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added handling for `IST` timezone to convert it to `UTC` timezone.   
2026-01-29 |  Enhancement:  
\- Added a new grok pattern to parse the logs correctly.   
2026-01-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `prod_event_type`, `product_event` field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `interface_name` field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new grok pattern to correctly populate link status in `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-12-23 |  Enhancement:  
\- Added new grok patterns to parse the new format of logs.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `device` raw log field to event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname UDM fields if it is a valid MAC address.  
\- event.idm.read_only_udm.principal.mac and event.idm.read_only_udm.principal.asset.mac: Newly mapped `device` raw log field (after transformation) to event.idm.read_only_udm.principal.mac UDM field if it is a valid MAC address.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vlan_port`, `flapping_src_port`, `flapping_dst_port`, `interface`, `state` raw log fields to event.idm.read_only_udm.additional.fields UDM field.   
2025-11-13 |  Enhancement:  
\- Added a grok pattern to parse the `hostname`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `device_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `seq_num` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `log_message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_tag`, `syslog_pri` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT` and `has_principal_user` is true, updated to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT` and `has_principal` is true, updated to `STATUS_UPDATE`.  
\- Normalization percentage is low because of the low log count and the dropped logs are valid.  
\- Sample log: `\x16\x03\x03\x01\xf4\x01\x00\x01\xf0\x03\x03T\xf3\xbe\xdfMc\xe5\x11\xfc{\xed\x8b\x0fh\x00\xb4t\x9c\xbb\xcf\x16d\xf7C\x85)9\x976\xc2O\xca\x00\x01|\x00\x00\x00\x01\x00\x02\x00\x03\x00\x04\x00\x05\x00\x06\x00\x07\x00\x08\x00\t\x00`  
2025-10-31 |  Enhancement:  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `src_mac` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.asset_id`: Newly mapped `device_serial_id` raw log field to `event.idm.read_only_udm.intermediary.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `log_version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `log_subtype` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `device_name` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated logic for setting `NETWORK_CONNECTION` event type. If `event.idm.read_only_udm.metadata.event_type` is not in [`USER_LOGIN`, `USER_LOGOUT`, `NETWORK_DHCP`], updated to `NETWORK_CONNECTION` if `has_principal` is true and `has_target` is true.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `fw_rule_id`, `device_model`, `log_component`, `nat_rule_id`, `fw_rule_type`, `log_type` raw log field(s) to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `qualifier`, `in_interface`, `hb_status`, `app_resolved_by`, `app_is_cloud`, `in_display_interface`, `log_occurrence`, `dst_country`, `ether_type`, `src_country` raw log field(s) to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Modified `kv_data` raw fields by adding a space before key-value pairs and also by removing double quotes.   
2025-10-29 |  Enhancement:  
\- Modified conditional logic for timezone processing:  
\- Previously, `CDT` was grouped with `CST` and mapped to a `-0600` offset.  
\- Now, `CDT` is grouped with `EST` and `EDT`, mapping to a `-0500` offset. `CST` alone maps to `-0600`. This corrects the UTC offset for the Central Daylight Time timezone. This change affects the calculation of event.idm.read_only_udm.metadata.event_timestamp.   
2025-10-21 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appcat`, `applist`, `dstintf`, `dstintfrole`, `mastersrcmac`, `osname`, `poluuid`, `service`, `srchwvendor`, `srcintf`, `srcintfrole`, `srcserver`, `transport`, `trandisp`, `vd`, `vwlid` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.product_object_id`: Newly mapped `devid` raw log field(s) with `event.idm.read_only_udm.intermediary.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `devname` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `logid` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `subtype` raw log field(s) with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `proto` raw log field(s) with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `rcvdbyte` raw log field(s) with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sentbyte` raw log field(s) with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `sentpkt` raw log field(s) with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration` raw log field(s) with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionid` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`, `event.idm.read_only_udm.principal.hostname`: Newly mapped `srcname` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname`, `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.principal.ip`: Newly mapped `srcip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`, `event.idm.read_only_udm.principal.mac`: Newly mapped `srcmac` raw log field(s) with `event.idm.read_only_udm.principal.asset.mac`, `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `osname` raw log field(s) with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field for known OSes (Windows, Linux, Mac).  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `srcswversion` raw log field(s) with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `srccountry` raw log field(s) with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.nat_ip`: Newly mapped `transip` raw log field(s) with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` raw log field(s) with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `policyid` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policyname` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `policytype` raw log field(s) with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `level` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `action` raw log field(s) with `event.idm.read_only_udm.security_result.summary` UDM field when `action` is `timeout`.  
\- `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.target.ip`: Newly mapped `dstip` raw log field(s) with `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dstcountry` raw log field(s) with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dstport` raw log field(s) with `event.idm.read_only_udm.target.port` UDM field.  
\- Removed \" characters from the mac field.  
\- Removed \" characters from the eventSummary and type fields.  
\- Added conditional check for header_data before mapping to event.idm.read_only_udm.metadata.product_log_id.  
\- `event.idm.read_only_udm.metadata.event_type`: If type is traffic or utm and has_principal is true, updated to NETWORK_CONNECTION.  
\- `event.idm.read_only_udm.metadata.event_type`: The condition to set STATUS_UPDATE was changed to require has_principal to be true.  
\- Added a new kv filter to parse key-value formatted log entries from the kv_data field.   
2025-08-13 |  Enhancement:  
\- Added support for new format in the `description` field. This new pattern will extract the description and source IP when they are in the format description.  
\- Added a `grok` pattern to the Logstash configuration to extract the hostname from the `device` field, effectively removing the trailing colon and any other characters after the hostname.   
2025-05-07 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- Modified a regex pattern to parse the logs.  
\- Added a conditional check for `sec_action` to map `sec_action` to `event.idm.read_only_udm.security_result.action`.  
\- Added a Grok pattern on `header_data` to extract device_ip and principal_host.  
\- Added a Grok pattern on `device_ip` field to map `device_ip` to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- Added a Grok pattern on `device_ip` and `principal_host` fields to map `device_ip` to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` and `principal_host` to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.   
2025-02-18 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2025-01-22 |  Enhancement:  
\- If `facility` is `SEC_LOGIN` and `mnemonic` is `LOGIN_SUCCESS`, then mapped `device` to `principle.hostname` and `principal.asset.hostname`.  
\- If `facility` is `SEC_LOGIN` and `mnemonic` is `LOGIN_FAILED`, then mapped `device` to `principal.hostname` and `principal.asset.hostname`.   
2024-11-27 |  Enhancement:  
\- Added new Grok patterns to parse failing syslog logs.  
\- Mapped `username3` to `principal.user.userid`.  
\- Mapped `login_status` to `security_result.summary`.   
2024-11-20 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2024-11-06 |  Enhancement:  
\- Mapped `ecs.version` to `metadata.product_version`.  
\- Mapped `fileset.name`, `flow.locality`, `flow.id`, `input.type`, `netflow.exporter.source_id`, and `netflow.exporter.uptime_millis` to `additional.fields`.  
\- Mapped `network.transport` to `network.ip_protocol`.  
\- Mapped `netflow.post_nat_source_ipv4_address` to `principal.ip`.  
\- Mapped `netflow.source_transport_port` to `principal.port`.  
\- Mapped `network.direction` to `network.direction`.   
2024-10-22 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Mapped `intermediary_ip` to `intermediary.ip`  
\- Mapped `intermediary_hostname` to `intermediary.hostname`  
2024-10-03 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2024-09-24 |  Enhancement:  
\- Added support for a new format of syslog logs.   
2024-08-26 |  Enhancement:  
\- When `principal_host` is empty, then only mapped `device` to `principal.hostname`.   
2024-07-01 |  Enhancement:  
\- Added a Grok pattern to parse valid dropped logs with a new pattern.  
\- In addition, added a Grok pattern to retrieve `target_ip` from the `header_data` field.   
2024-05-29 |  Enhancement:  
\- Added a Grok pattern to parse valid dropped logs with a new pattern.  
\- Added a Grok pattern to retrieve `principal_host` from the field `header_data`.  
\- Added a Grok pattern to retrieve `destination_ip`, `src_mac`, and `hostname` from the field `description`.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Mapped `src_mac` to `principal.mac`.  
\- Mapped `eventSummary` to `metadata.product_event_type`.  
\- Mapped `description` to `security_result.description`.  
\- Mapped `error_msg` to `security_result.detection_fields`.   
2024-05-22 |  Enhancement:  
\- Added a Grok pattern to retrieve hostname.   
2024-05-08 |  Enhancement:  
\- Added a Grok pattern to support uparsed SYSLOG format logs.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `srcPort` to `principal.port`.  
\- Mapped `device_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `srcUser` to `principal.user.userid`.  
\- Mapped `username1` to `target.user.userid`.  
\- Mapped `command` to `target.process.command_line`.  
\- Mapped `PWD` to `target.process.file.full_path`.  
\- Mapped `host_name` to principal.hostname` and `principal.asset.hostname".  
\- Mapped `node_id`, `cluster_id`, `exception`, `UniqueId`, and `app_id` to `additional.fields`.   
2023-12-08 |  Enhancement:  
\- Added support for the new pattern of SYSLOG logs and Key-Value logs.  
\- Mapped `DEVICE` to `principal.mac`.  
\- Mapped `SRC` to `principal.ip`.  
\- Mapped `SPT` to `principal.port`.  
\- Mapped `DST` to `target.ip`.  
\- Mapped `DPT` to `target.port`.  
\- Mapped `ID` to `network.session_id`.  
\- Mapped `LEN` to `network.session_duration.seconds`.  
\- Mapped `PROTO` to `network.ip_protocol`.  
\- Mapped `IN`, `OUT`, `PHYSIN`, `WINDOW`, `RES, `TOS`, `PREC`, `TTL` ,`URGP`, `MAC`, `radio`, `vap`, `auth_type`, `sugg_band`, `ssid_id`, `ssid_profile_name` and `protocol` to `additional.fields".  
\- Mapped `client_mac` to `principal.mac`.  
\- Mapped `aid` to `network.session_id`.  
\- Mapped `rssi` to `intermediary.asset.product_object_id`.  
\- Mapped `channel` to `security_result.detection_fields`.   
2023-11-05 |  Enhancement:  
\- Modified and added new Grok patterns to parse failing syslog logs.  
\- Added KV filter to parse KV logs.  
\- Mapped `eventSummary`, `dhcp_ip`, `client_mac`, `aid` and `ip_src` to `metadata.product_event_type`, `target.ip`, `network.dhcp.chaddr`, `network.session_id` and `principal.ip`, respectively.  
\- Mapped `mac`, `src`, `sport`, `dst`, `dport`, `action`, `protocol`, `url` and `signature` to `principal.mac`, `principal.ip`, `principal.port`, `target.ip`, `target.port`, `security_result.action`, `network.ip_protocol`, `principal.url` and "additional.fields, respectively.  
\- For eventSummary `splash_auth` mapped `metadata.event_type` and `extensions.auth.type` to `USER_LOGIN` and `MACHINE`, respectively.  
\- For eventSummary `association` mapped `eventSummary`, `aid`, `rssi`, `channel`, `last_known_client_ip` and `event_type` to `security_result.summary`, `network.session_id`, `intermediary.asset.product_object_id`, `security_result.detection_fields`, `principal.ip` and `STATUS_UPDATE`, respectively.   
2023-04-27 |  Enhancement:  
\- Reduced generic percentage.  
\- Removed unnecessary Grok patterns.  
\- Added Grok pattern to parse syslog logs.  
\- Added conditional check for `source_ip`, `destination_ip`.  
\- If `source_ip` and `destination_ip` is present then map `event_type` to `NETWORK_CONNECTION`.  
\- If `source_ip` is present and `destination_ip` is not present then map `event_type` to `STATUS_UPDATE`.  
\- Mapped `pid` to `target.process.pid`.  
\- Mapped `app_name` to `target.application`.   
2023-03-24 |  Customer Issue:  
\- Added Grok pattern and mapping for logs where message types are either `FILECPY`, `REJECT`, `CONNECT`, or `DISCONNECT`.   
2023-01-24 |  Enhancement:  
\- Modified Grok patterns to support logs having timezone.  
\- Mapped `ip_address` to `principal.ip`.  
\- When `mnemonic` is `NBR_RESET` and ip_address is present , then `metadata.event_type` is set as `STATUS_UPDATE`.   
2022-07-21 |  Enhancement  
\- Added grok pattern and enhanced the parser to parse the logs that were getting dropped (logs without "%--).  
\- Mapped `hostname` to `principal.hostname`  
\- Mapped `source_ip` to `principal.ip`  
\- Mapped `destination_ip` to `target.ip`  
\- Mapped `ip_protocol` to `network.ip_protocol`.  
\- Mapped `summary` to `security_result.summary`.  
\- Mapped `header_data` to `metadata.product_log_id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
