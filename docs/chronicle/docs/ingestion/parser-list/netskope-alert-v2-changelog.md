---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-v2-changelog/
title: Change log for NETSKOPE_ALERT_V2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:38.435132+00:00
---

# Change log for NETSKOPE_ALERT_V2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-alert-v2-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETSKOPE_ALERT_V2

Date | Changes  
---|---  
2026-07-01 |  Enhancement:  
\- `event.idm.read_only_udm.target.administrative_domain`: Removed mapping of `domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field as it represents the hostname not the domain.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `domain` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields as it is a duplicate mapping with principal hostname data.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dom` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.   
2026-06-29 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Mapped `supporting_data.data_values` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when the first element in `supporting_data.data_values` is NOT a valid IP.   
2026-06-04 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`:  
\- When `res_ccl` is `high` or `excellent`, set the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- When `res_ccl` is `poor` or `low`, updated the value of `event.idm.read_only_udm.security_result.severity` to `HIGH`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `res.src_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.type`: Removed mapping of `Device` raw log field from `event.idm.read_only_udm.principal.resource.type` UDM field since the UDM field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.resource_type`: Mapped `Device` raw log field with `event.idm.read_only_udm.principal.resource.resource_type` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id`, `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `res.nsdeviceuid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `res.all_policy_matches` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `res.supporting_data.data_values` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field when the index is `0`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `res.supporting_data.data_values` raw log field with `event.idm.read_only_udm.security_result.description` UDM field when the index is `1`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `res.severity_level raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Added a grok pattern on `Url` to extract `domain_name`.  
\- `event.idm.read_only_udm.target.domain.name`: Newly mapped `domain_name` field with `event.idm.read_only_udm.target.domain.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields: Newly mapped `res.all_policy_matches`, `Severity`, `policy_id`, `threat_source_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields: Newly mapped `res.supporting_data.data_values`, `Browser`, `res.supporting_data.data_type`, `res.suppression_end_time`, `res.num_sessions`, `res.message_size`, `res.suppression_start_time`, `res.total_packets`, `res.tunnel_up_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added a conditional check to to map `event.idm.read_only_udm.metadata.event_timestamp` from `res.src_time` and `res.src_timezone` raw log fields when `src_timezone` is equal to `America/Los_Angeles`.   
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `record_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `access_method` is `GRE`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `bypass_reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `alert_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field when `alert_type` is `ips`.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `signature_id` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field when `alert_type` is `ips`.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field when `alert_type` is `ips`.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dsthost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `type` is `connection`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `incident_id`, `ccl`, `ja3`, `ja3s`, `destination_instance_id`, `zip_file_id`, `bypass_traffic`, `netskope_pop`, `user_generated`, `ssl_decrypt_policy`, `conn_duration`, `conn_starttime`, `conn_endtime`, `req_cnt`, `resp_cnt`, `resp_content_len`, `numbytes` and `os_family` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-12 |  Enhancement:  
\- Added gsub transformations for `dlp_incident_id`, `request_id`, and `dlp_parent_id` to ensure they are treated as strings before JSON parsing, this ensures large numerical values are not truncated.  
\- `event.idm.read_only_udm.about.user.email_addresses`: Newly mapped `res.owner` raw log field with `event.idm.read_only_udm.about.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.file.last_modification_time`: Newly mapped `res.modified` raw log field with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Added `res.dlp_rule_count`, `res.dlp_profile`, `res.dlp_is_unique_count`, `res.scan_type`, `res.dlp_rule_severity` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `res.instance`, `res.file_path`, `res.dst_geoip_src`, `res.dsthost` (if res.dsthost isn't a valid IP address) raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `res.dlp_profile`, `res.dlp_rule_count`, `res.dlp_is_unique_count`, `res.dlp_parent_id`, `res.file_lang`, `res.instance`, `res.scan_type`, `res.external_collaborator_count`, `res.file_path`, `res.dst_geoip_src`, `res.dlp_rule_severity`, `res.internal_collaborator_count` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Added a conditional check for the `os` raw log field. If `os` contains `MAC`, `LINUX`, or `IOS`, it maps to `event.idm.read_only_udm.principal.platform`. Otherwise, `os` is mapped to the `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `res.userkey`,`res.act_user` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-02-02 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `ur_normalized` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `other_categories` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- The logic for setting the timezone offset variable `tz` has been updated. If `month_name` is one of `Nov`, `Dec`, `Jan`, `Feb`, or `Mar` and `res_src_timezone` contains `America/Los_Angeles`, `tz` is set to `-0800`.   
2025-12-11 |  Enhancement:  
\- Added CSV as a supported format.   
2025-09-29 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- Defined all the fields → url, organization_unit, os_version, ur_normalized, browserSessionid, file_size, file_type, file_md5, device, src_region, src_country, src_latitude, src_longitude, dst_latitude, dst_longitude, dst_country, dst_region, dst_zipcode, dsthost, app, access_method, severity, activity, appcategory, browser_session_id, network_session_id, server_bytes, client_bytes, client_packets, and server_packets as "".   
2025-08-06 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `TSS-scan`, `file_id`, `ml_detection`, `scanner_result`, `title`, `tss_mode` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `device_classification` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `detection_engine`, `malware_profile`, `malware_type`, `severity_id` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- Enhanced `event.idm.read_only_udm.metadata.event_timestamp` parsing to utilize the src_timezone field when provided with src_time, including conversions for common timezone names to UTC offsets.  
\- Added support for America/Chicago, America/Los_Angeles, America/New_York and Europe/London timezones.   
2025-08-03 |  Enhancement:  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `assignee`, `dlp_incident_id`, and `status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event1.idm.read_only_udm.security_result1.detection_fields: Newly mapped `action_threshold_met`, `dlp_policy`, `dlp_profile_name`, `dlp_forensic_id`, and `dlp_incident_rule_count` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event1.idm.read_only_udm.security_result1.category_details: Newly mapped `dlp_match_type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event1.idm.read_only_udm.security_result1.rule_name: Newly mapped `dlp_rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event1.idm.read_only_udm.security_result1.severity: Newly mapped `dlp_rule_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event1.idm.read_only_udm.security_result1.action: Newly mapped `dlp_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2025-07-31 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alert` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `res.device_classification` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped res.dst_timezone raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `res.malicious` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `res.notify_template` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `res.page_site` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Modified the condition for mapping `res.session_duration` to `event.idm.read_only_udm.network.session_duration.seconds` to exclude `0` in addition to empty strings.  
\- Modified the condition for mapping `res.file_size` to `event.idm.read_only_udm.target.file.size` to exclude `0` in addition to empty strings.  
\- Updated timestamp mapping logic to prioritize `res.timestamp` over `src_time` for populating `event.idm.read_only_udm.metadata.event_timestamp` using `has_timestamp` flag.  
\- Changed `target` for date filter from `@timestamp` to `event.idm.read_only_udm.metadata.event_timestamp`.   
2025-07-23 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- event.idm.read_only_udm.principal.ip: Newly mapped userip raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped userip raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields, and event.idm.read_only_udm.principal.resource.attribute.labels in for loop.  
\- Removed redundant mapping for `event.idm.read_only_udm.network.http.user_agent` and `ccl`.   
2025-06-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `object`, `appsuite`, `connection_id`, `count`, `evt_src_chnl`, `file_category`, `managed_app`, `object_count`, `page`, `request_id`, `score`, `threshold_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `from_user` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `incident_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `src_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip`and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `userip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added a conditional logic to not map `res_ccl` as `event.idm.read_only_udm.security_result.severity` if `Severity` is present.  
\- Used `alert` to map `event.idm.read_only_udm.security_result.action` UDM field correctly.   
2025-05-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `_id` and `product_id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` and `cs_referer` raw log fields with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `organization_unit` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` and `cs_username` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `useragent` and `cs_user_agent` raw log fields with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `useragent` and `cs_user_agent` raw log fields with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `session_duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `os_version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `os` and `x_c_os` raw log fields with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `ur_normalized` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `browser_session_id`, `network_session_id` and `x_cs_session_id` raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `malware_id` raw log field with `event.idm.read_only_udm..threat_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `src_location`, `src_zipcode` and `src_geoip_src` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.file.size`: Newly mapped `file_size` and `x_rs_file_size` raw log fields with `event.idm.read_only_udm.principal.file.size` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `srcip`, `s_ip`, `c_ip` and `x_cs_src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip`, `s_ip`, `c_ip` and `x_cs_src_ip` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcport` and `x_cs_src_port` raw log fields with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `file_md5` and `x_rs_file_md5` raw log fields with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `computer_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `computer_name` and `cs_dns` and `cs_host` raw log fields with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped `device` raw log field with `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `device` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `device_sn` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `src_region` and `x_c_location` raw log fields with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `src_country` and `x_c_country` raw log fields with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `src_latitude` and `x_c_latitude` raw log fields with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `src_longitude` and `x_c_longitude` raw log fields with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_coordinates.latitude`: Newly mapped `dst_latitude` and `x_s_latitude` raw log fields with `event.idm.read_only_udm.target.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.target.location.region_coordinates.longitude`: Newly mapped `dst_longitude` and `x_s_longitude` raw log fields with `event.idm.read_only_udm.target.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `destination_file_path` and `dlp_file` raw log fields with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dst_country` and `x_s_country` raw log fields with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.location.state`: Newly mapped `x_s_region` raw log field with `event.idm.read_only_udm.target.location.state` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `dst_region` and `x_s_location` raw log fields with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dst_zipcode` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dsthost`, `dstip` and `x_cs_dst_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dsthost`, `dstip` and `x_cs_dst_ip` raw log fields with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dstport` and `x_cs_dst_port` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cci`, `alert_type`, `x_other_category_id`, `x_cs_userip`, `x_ssl_bypass`, `x_cs_ssl_fronting_error`, `x_cs_ssl_handshake_error`, `x_sr_ssl_handshake_error`, `x_sr_ssl_client_certificate_error`, `x_sr_ssl_malformed_ssl`, `x_s_custom_signing_ca_error`, `x_cs_ssl_engine_action`, `x_cs_ssl_engine_action_reason`, `x_sr_ssl_engine_action`, `x_sr_ssl_engine_action_reason`, `x_ssl_policy_src_ip`, `x_ssl_policy_dst_ip`, `x_ssl_policy_dst_host`, `x_ssl_policy_dst_host_source`, `x_ssl_policy_action`, `x_sr_ssl_version`, `x_sr_ssl_cipher`, `x_cs_src_ip_egress`, `x_policy_src_ip`, `x_policy_dst_ip`, `x_policy_dst_host`, `x_policy_dst_host_source`, `x_policy_justification_type`, `x_policy_justification_reason`, `x_sc_notification_name`, `x_cs_http_version`, `x_sr_dst_ip`, and `x_sr_dst_port` raw log fields with `event.idm.read_only_udm..detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `ccl` raw log field with `event.idm.read_only_udm..confidence_details` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence`: Newly mapped `ccl` raw log field with `event.idm.read_only_udm..confidence` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `dlp_profile_name` raw log field with `event.idm.read_only_udm..rule_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `policy_name`, `dlp_fingerprint_classification`, `dlp_fingerprint_match`, `dlp_fingerprint_score`, `dlp_rule_score`, `dlp_unique_count`, `acked`, `app_session_id`, `x_type`, `x_transaction_id`, `x_client_ssl_err`, `x_cs_domain_fronted_sni`, `x_cs_tunnel_id`, `x_request_id`, `x_s_zipcode`, `x_c_zipcode`, `x_c_browser`, `x_c_browser_version`, `x_c_device`, `x_cs_site`, `x_cs_page_id`, `x_cs_traffic_type`, `x_category_id`, `x_category`, `x_r_cert_valid`, `x_r_cert_expired`, `x_r_cert_untrusted_root`, `x_r_cert_incomplete_chain`, `x_r_cert_self_signed`, `x_r_cert_revoked`, `x_rs_file_type`, `x_rs_file_category`, `x_rs_file_language`, `x_r_cert_revocation_check`, `x_cs_app_category`, `x_cs_app_cci`, `x_cs_app_ccl`, `x_cs_app_tags`, `x_cs_app_suite`, `x_cs_app_instance_id`, `x_cs_app_instance_name`, `x_cs_app_instance_tag`, `x_cs_app_activity`, `x_cs_app_from_user`, `x_cs_app_to_user`, `x_cs_app_object_type`, `x_cs_app_object_name`, `x_cs_app_object_id`, `x_cs_uri_path`, `x_r_cert_mismatch`, `x_cs_access_method`, `cs_uri`, `cs_uri_port`, `cs_uri_query`, `cs_content_type` and `sc_content_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `access_method` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` and `x_policy_action` raw log fields with `event.idm.read_only_udm..action` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` and `x_ssl_policy_name` raw log fields with `event.idm.read_only_udm..rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm..severity` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `activity` raw log field with `event.idm.read_only_udm..description` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `appcategory` and `x_ssl_policy_categories` and `x_other_category` raw log fields with `event.idm.read_only_udm..category_details` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `server_bytes` and `sc_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `client_bytes` and `cs_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `client_packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `server_packets` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.   
2025-03-19 |  Enhancement:  
\- Mapped `result.useragent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `result.matched_username` to `additional.fields`.   
2025-03-18 |  Enhancement:  
\- Mapped `alert_name` to `security_result.rule_name`.  
\- Mapped `breach_description` to `security_result.description`.  
\- If `ccl` is `high` then map `security_result.severity` to `HIGH`.  
\- If `ccl` is `medium` then map `security_result.severity` to `MEDIUM`.  
\- If `ccl` is in `poor` , `low` then map `security_result.severity` to `LOW`.  
\- If `ccl` is in `excellent` , `unknown` , `not_defined` then map `security_result.severity` to `UNKNOWN_SEVERITY`.  
\- If `action` is in `block` , `restrictToView` , `disableDownload` and `restrictAccess` then map `security_result.action` to `BLOCK`.  
\- If `action` is in `alert`, `bypass` , `quarantine` , `legalHold` , `useralert` and `Detection` , `expireLink` then map `security_result.action` to `QUARANTINE`.  
\- If `action` is in `none` then map `security_result.action` to `UNKNOWN_ACTION`.   
2025-02-18 |  Enhancement:  
\- Added support for unparsed fields.  
\- Mapped `hostname` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `type` to `additional.fields`.  
\- Mapped `email` to `network.email.from`.  
\- Mapped `severity` to `security_result.severity`.   
2024-09-25 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
