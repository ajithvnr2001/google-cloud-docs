---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-xdome-changelog/
title: Change log for CLAROTY_XDOME \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:57.461255+00:00
---

# Change log for CLAROTY_XDOME  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claroty-xdome-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLAROTY_XDOME

Date | Changes  
---|---  
2026-08-14 |  Enhancement:  
\- Added a new grok pattern to support CEF logs without syslog header format.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field when `observer_hostname` is empty.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `proc_id`, `facility`, `priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field when `syslog_pid` is empty.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `evnt_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `ot_activity_evnt_type` and `ot_activity_event_type` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ot_activity_mode`, `ot_activity_source_username`, `other_device_name`, `other_device_connection_type_list`, `other_device_managed_device`, `other_device_labels`, and `protocol` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `other_device_asset_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `other_device_uid` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `other_device_mac_list` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields with Grok regex validation.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `other_device_ip_list` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields with Grok regex validation.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `other_device_site_name` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.asset.category`: Newly mapped `other_device_category` raw log field with `event.idm.read_only_udm.target.asset.category` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `other_device_subcategory`, `other_device_type`, `other_device_model`, `other_device_type_family`, and `other_device_retired` raw log fields with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `other_device_manufacturer` and `other_device_network_list`, raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.   
2026-07-27 |  Enhancement:  
\- Added Grok regex validation for `comm_tuple_dst_mac`, `comm_tuple_src_mac`, `evnt_extra_info.other_device.mac_list`, `side_a_mac`, `side_b_mac`, `affected_device.mac_list`, `device_mac_list`, `device_name`, `dstMAC`, `dst_mac`, `srcMAC`, and `src_mac` raw log fields before mapping to `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`, `event.idm.read_only_udm.target.mac`, and `event.idm.read_only_udm.target.asset.mac` UDM fields to prevent strict regular expression validation errors.  
\- Added Grok regex validation for `affected_device.ip_list`, `comm_tuple_dst_ip`, `comm_tuple_src_ip`, `evnt_extra_info.other_device.ip_list`, `side_a_ip`, `side_b_ip`, `device_ip_list`, `device_name`, `dst`, `dst_ip`, `ip_list`, `src`, and `src_ip` raw log fields before mapping to `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.target.ip`, and `event.idm.read_only_udm.target.asset.ip` UDM fields to prevent strict regular expression validation errors.   
2026-07-14 |  Enhancement:  
\- Added a grok pattern to support the new format of Syslog+KV logs.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `platform_version` field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.   
2026-06-16 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_pid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `evnt_extra_info.file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.file_type`: Newly mapped `evnt_extra_info.file_type` raw log field with `event.idm.read_only_udm.target.file.file_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `evnt_extra_info.sender_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `comm_tuple.protocol` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when the `comm_tuple.protocol` is not a predefined protocol.   
2026-05-22 |  Enhancement:  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `ip_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `device_ip_list`, `device_mac_list`, `domain`, `server_port`, `signature_name`, `event_alert_id`, `event_timestamp`, `direction` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `dst_mac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `src_mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `geo_location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `event_alert_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `event_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `alert_type_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-05-19 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `evnt_extra_info.policy_info.policy_pair` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as the current structure is unsuitable because it cannot accommodate the list of values required for the `policy_pair`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `evnt_extra_info.policy_info.policy_pair` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Changed mapping of `affected_device.assignees` such that each item in the `affected_device.assignees` array is now mapped as an individual label.  
\- Added a grok pattern before mapping `evnt_extra_info.other_device.ip_list` to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.   
2026-04-02 |  Enhancement:  
\- Added a new grok pattern for the raw log field `signature_content` to extract the `msg_content`, `flow`, `content`, `body_content`, `distance`, `reference`, `reference_url`, `classtype`, `sid`, `rev` and `metadata_description`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `signature_tag`, `management_status`, `certificate_type`, `signature_severity_description`, `policy_pair`, `communication_type`, `flow`, `body_content`, `distance`, `reference`, `sid`, `rev` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `link` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `asset_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.mac`: Newly mapped `mac` raw log field with `event.idm.read_only_udm.target.asset.mac` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `ip`, `side_b_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.category`: Newly mapped `device_category_data` raw log field with `event.idm.read_only_udm.target.asset.category` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `other_device_device_subcategory`, `other_device_device_type`, `other_device_device_type_family`, `other_device_risk_score` raw log fields with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `site_name` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `other_device_device_name`, `other_device_connection_type_list`, `thumbprint`, `expiry_date`, `start_date`, `OU`, `O`, `C`, `ST`, `L`, `mode`, `side_b_port`, `evnt_extra_info_direction`, `side_a_port` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `manufacturer`, `network_list`, `other_device_os` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `CN`, `affected_device_management_status`, `assignees`, `affected_device_os` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `sender_id`, `source_username` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `comm_tuple_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `side_a_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `side_a_mac`, `affectedmac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `evnt_type`, `msg_content` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `side_b_mac` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policy_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `evnt_extra_info_direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `content` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `reference_url` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `classtype` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `metadata_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-02-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset_id`: Removed mapping of `device_asset_id` from `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Removed mapping of `device_asset_id` from `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.network_domain`: Newly Mapped `device_asset_id` raw log field to `event.idm.read_only_udm.principal.asset.network_domain` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alert_type_name`, `firmware_device_type` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- The parsing logic for `firmware_latest_known_versions` was improved to correctly handle list values for the software_version field.  
\- The parsing logic for the `device_name` field was enhanced to conditionally extract IP addresses, MAC addresses, or hostnames.  
\- The `firmware_device_type` field is now transformed by replacing single quotes with double quotes to ensure it is valid JSON before parsing.   
2025-12-19 |  Enhancement:  
\- Added support for CEF log format.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `device_retired` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `device_note` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.software.version: Newly mapped `device_app_version` raw log field with `event.idm.read_only_udm.principal.asset.software.version` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `device_vulnerability_relevance`, `device_vulnerability_overall_cvss_v3_score`, `device_vulnerability_manufacturer_remediation_info_source`, `vulnerability_type`, `vulnerability_affected_products`, `vulnerability_is_known_exploited`, `vulnerability_known_exploits` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `vulnerability_note` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `device_managed_device`, `device_vulnerability_relevance_source`, `device_vulnerability_manufacturer_remediation_info` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.extensions.vulns.vulnerabilities.name: Newly mapped `vulnerability_name` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities.name` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `device_risk_score` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-10-10 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.confidence_score`: Newly mapped `alert_info_signature_confidence` and `evnt_extra_info_ids_signature_info_signature_confidence` raw log field with `event.idm.read_only_udm.security_result.confidence_score` UDM field.  
\- Modified the value of `event.idm.read_only_udm.metadata.product_name` from `CLAROTY_XDOME` to `xDome`.  
\- Modified the value of `event.idm.read_only_udm.metadata.vendor_name` from `CLAROTY_XDOME` to `Claroty`.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `evnt_extra_info.ids_signature_info.signature_active_rev` and `alert_info_signature_active_rev` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `evnt_extra_info.ids_signature_info.signature_severity_description`, `alert_info.signature_severity_description` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `evnt_extra_info.geo_location` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped evnt_extra_info.ip_protocol raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `affected_device.management_status`, `affected_device.note`, `evnt_extra_info.domain`, `evnt_extra_info.src_domain`, `evnt_extra_info.src_geo_location`, `evnt_extra_info.ids_signature_info.signature_powered_by`, `evnt_extra_info.other_device` and `alert.note`and `affected_device.labels` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert_info.signature_severity_description`, `evnt_extra_info.ids_signature_info.signature_first_released`, `evnt_extra_info.ids_signature_info.signature_last_updated`, `evnt_extra_info.ids_signature_info.signature_last_updated_by_system` and `alert.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-09-05 |  \- `event.idm.read_only_udm.alert_info.signature_name`: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.alert_info.signature_name` UDM field.  
\- `event.idm.read_only_udm.alert_info.signature_severity`: Newly mapped `risk_severity` raw log field with `event.idm.read_only_udm.alert_info.signature_severity` UDM field.   
2025-08-12 |  \- Newly added gsub for the `message` field to parse logs in proper manner.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `affected_device.retired` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- Corrected the mapping for `vulnerability_info.name` raw log field and mapped it to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip` : Newly mapped `management_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `time` data field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-31 |  \- `event.idm.read_only_udm.security_result.rule_id`: Removed `alert_id` raw log field from `event.idm.read_only_udm.security_result.rule_id` UDM field alert_id represents a unique identifier for the alert, and it doesn't fit to be mapped to rule_id.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `alert_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping for `attack data` from `event.idm.read_only_udm.additional.fields` UDM field because the security_result.attack_details field is specifically designed to store details about an attack.  
\- `event.idm.read_only_udm.security_result.attack_details`: Mapped `attack data` raw log field with `event.idm.read_only_udm.security_result.attack_details` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping for `observer_hostname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields because it incorrectly associates the observer's information with the principal.  
\- `event.idm.read_only_udm.observer.hostname`: Mapped `observer_hostname` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- Changed `event.idm.read_only_udm.metadata.product_event_type` to include both `type` and `category` raw log fields.  
\- Utilized SCAN_VULN_HOST for vulnerability_affected_device product event type  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed `Vulnerabilities` raw log field from `event.idm.read_only_udm.security_result.detection_fields` UDM field because it is having detailed vulnerability information.  
\- `event.idm.read_only_udm.extensions.vulns.vulnerabilities`: Mapped `vulnerabilities` raw log field with `event.idm.read_only_udm.extensions.vulns.vulnerabilities` UDM field.  
\- Changed the `host` field to `observer_hostname` in order to create `observer` UDM.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping for `client_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field because `client_id` is not a userid.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Mapped `client_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping for `device_asset_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field because it refers to the asset that performed the action.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Mapped `device_asset_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- Improved logic on app protocol and IP's using libs.  
\- Extracted signature information from nested json to security_result.rule_name and security result.rule_id.   
2025-01-29 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
