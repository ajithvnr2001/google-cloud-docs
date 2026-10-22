---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-casb-changelog/
title: Change log for NETSKOPE_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:38.321660+00:00
---

# Change log for NETSKOPE_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netskope-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETSKOPE_CASB

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- Added support new format of SYSLOG+JSON logs.  
\- Modified a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `allow`, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `nsdeviceuid`, `process_name` and `app_activity` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `device_classification` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Newly mapped `parent_process_name` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `ur_normalized` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.   
2026-09-18 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.outcomes`: Removed mapping of `_category_tags` and `_category_id` raw log fields from `event.idm.read_only_udm.security_result.outcomes` UDM field as it is deprecated.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `_category_tags` and `_category_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `md5` raw log field with `event.idm.read_only_udm.target.file.md5`.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256`.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `file_size` raw log field with `event.idm.read_only_udm.target.file.size`.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.target.file.mime_type`.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `dlp_file` raw log field with `event.idm.read_only_udm.target.file.full_path`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `object`, `file_category`, `file_lang`, `true_filetype`, `true_obj_category`, `true_obj_type`, `_true_obj_type`, `_true_obj_cat`, `_subfile` and `managed_app` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `dlp_rule` raw log field with `event.idm.read_only_udm.security_result.rule_name`.  
\- `event.idm.read_only_udm.security_result.severity`, `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `dlp_rule_severity` raw log field with `event.idm.read_only_udm.security_result.severity` and `event.idm.read_only_udm.security_result.severity_details`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `tags` and `other_categories` raw log fields with `event.idm.read_only_udm.security_result.category_details`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dlp_incident_id`, `dlp_profile`, `dlp_parent_id`, `dlp_is_unique_count`, `dlp_rule_count`, `_ns_protection_type` and `protection_string` raw log fields with `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_doc_type`, `outer_doc_type`, `true_type_id`, `_true_obj_id`, `_nsp_dur_back`, `_nsp_retrans_front`, `_nsp_rtt_back`, `_nsp_rtt_front`, `_dst_service`, `_src_service`, `_src_epoch_now`, `_legacy_access_method`, `page_site`, `appcategory`, `_obj_name`, `_category_name`, `_full_url`, `alert`, `ccl`, and `userkey` raw log fields with `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `os_name` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` when it is Mac device.  
\- `event.idm.read_only_udm.principal.file.mime_type`: Newly mapped `_client_file_type` raw log field with `event.idm.read_only_udm.principal.file.mime_type`.  
\- `event.idm.read_only_udm.principal.file.sha256`: Newly mapped `local_sha256` raw log field with `event.idm.read_only_udm.principal.file.sha256`.   
2025-09-29 |  Enhancement:  
\- Enhanced log processing by using `gsub` to replace d"Azur with d'Azur. This corrects log entries with this pattern, allowing them to be parsed as valid JSON instead of being dropped as malformed.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `device` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `os_name` raw log field to event.idm.read_only_udm.principal.asset.platform_software.platform.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped `os_version` raw log field to event.idm.read_only_udm.principal.asset.platform_software.platform_version.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_appsession_start`, `__buf_len`, `supporting_data.data_values`, `ja3`, `ja3s` , `app_tags`, `src_zipcode`, `dst_zipcode`, `tunnel_id`, `browser_session_id`, `incident_id`, `_content_version`, `_creation_timestamp`, `_ef_received_at`, `_enriched_all`, `_session_begin`, `_skip_geoip_lookup`, `_src_gmt_offset`, `acked`, `connection_id`, `sanctioned_instance`, `src_time`, `telemetry_app`, `_original_destport`, `_raw_event_inserted_at`, `site`, `_partial_file` and `request_id` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referer` raw log field to event.idm.read_only_udm.network.http.referral_url.  
\- event.idm.read_only_udm.principal.location.region_latitude: Newly mapped `src_latitude` raw log field to event.idm.read_only_udm.principal.location.region_latitude.  
\- event.idm.read_only_udm.principal.location.region_longitude: Newly mapped `src_longitude` raw log field to event.idm.read_only_udm.principal.location.region_longitude.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `dst_latitude` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.latitude.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `dst_longitude` raw log field to event.idm.read_only_udm.principal.location.region_coordinates.longitude.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `userip` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `userip` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `src_timezone`, `transaction_id`, `_event_id`, `from_user` and `organization_unit` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dst_timezone`, `_instance_name`, `_service_identifier` and `os_family` raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.intermediary.location.name: Newly mapped `netskope_pop` raw log field to event.idm.read_only_udm.intermediary.location.name.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `page_site` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `page_site` raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.target.domain.name: Newly mapped `domain` raw log field to event.idm.read_only_udm.target.domain.name.  
\- event.idm.read_only_udm.target.ip: Newly mapped `_original_destip` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `_original_destip` raw log field to event.idm.read_only_udm.target.asset.ip.   
2024-02-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
