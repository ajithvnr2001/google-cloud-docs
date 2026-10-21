---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cato-networks-changelog/
title: Change log for CATO_NETWORKS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:00:49.250226+00:00
---

# Change log for CATO_NETWORKS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cato-networks-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CATO_NETWORKS

Date | Changes  
---|---  
2026-08-05 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`: Updated the conditional logic on `severity` and `risk_level` raw log fields to map only supported enum values to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Updated the conditional logic on `risk_level` raw log field to map only supported enum values to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destination_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `source_country` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `source_site` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `signature_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field with key `signature_id`.   
2026-07-28 |  Enhancement:  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `dns_query` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.type`: Newly mapped `dns_record_type` raw log field with `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `server_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `is_cloud_app`, `application_type`, `flow_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `src_endpoint_type`, `dest_endpoint_type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-11 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `admin.name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: Newly mapped `field.name` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field when index is `0`.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `field.value.name`, `field.value.id` and `field.value.type` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `change_After_publish` and `model_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped operationName raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `flowLogVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `flowLogGUID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `flowLogResourceID` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `macAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `targetResourceID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `flowRecords.flows.aclID`, `flowRecords.flows.flowGroups.rule`, and `flowRecords.flows.flowGroups.flowTuple` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-09 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `creation_date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `admin_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `admin` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `change_type`, `module`, `model_name`, `insertion_date`, `change_After_overrideCategories`, `change_Before_overrideCategories` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `model_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.   
2025-12-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dest_site_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `dest_site_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `connection_origin` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dest_is_site_or_vpn` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Converted type to string with error handling for `application_risk`, `tls_inspection` raw log field(s).   
2025-11-20 |  Enhancement:  
\- event.idm.read_only_udm.src.ip and event.idm.read_only_udm.src.asset.ip: Removed mapping of `sourceIp`, `fieldsMap.src_isp_ip` from `event.idm.read_only_udm.src.ip` and `event.idm.read_only_udm.src.asset.ip` UDM fields inorder to introduce a more accurate mapping.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `sourceIp`, `fieldsMap.src_isp_ip` raw log field(s) to `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `event_type` from `event.idm.read_only_udm.additional.fields` UDM field inorder to introduce a more accurate mapping.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type` raw log field to `event.idm.read_only_udm.metadata.event_type` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `src_site_id`, `logged_in_user.0` raw log field(s) to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `device_name`, `configured_host_name` raw log field(s) to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `client_version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user_name`, `ad_name` raw log field(s) to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `host_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `host_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `host_mac` raw log field to `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `os_version` raw log field to `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `vpn_user_email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `account_name` raw log field to `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `static_host`, `threat_type`, `trust_level`, `application_risk`, `network_rule`, `qos_priority`, `tls_inspection`, `always_on_configuration`, `connect_on_boot`, `device_certificate`, `office_mode`, `pac_file`, `split_tunnel_configuration`, `trusted_networks`, `vpn_lan_access`, `src_or_dest_site_id` raw log field(s) to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `event_message` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `alert_id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `full_path_url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `status` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `threat_name` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `sourceIp`, `fieldsMap.src_isp_ip` raw log field(s) to `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If event.idm.read_only_udm.metadata.event_type is `GENERIC_EVENT`, updated to `NETWORK_CONNECTION` if has_principal is `true` and has_target is `true`.  
\- event.idm.read_only_udm.metadata.event_type: If event.idm.read_only_udm.metadata.event_type is `GENERIC_EVENT`, updated to `USER_UNCATEGORIZED` if has_principal_user is `true`.  
\- event.idm.read_only_udm.metadata.event_type: If event.idm.read_only_udm.metadata.event_type is `GENERIC_EVENT`, updated to `STATUS_UPDATE` if has_principal is `true`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `internal_id`, `link_type`, `tunnel_protocol`, `visible_device_id`, `event_sub_type`, `connector_name`, `connector_type`, `epp_engine_type`, `incident_id`, `title`, `vendor`, `vendor_device_id`, `engine_type`, `recommended_actions`, `device_posture_profile`, `parent_connector_name`, `client_class`, `congestion_algorithm`, `custom_category`, `custom_category_id`, `custom_category_name`, `tcp_acceleration` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `user_sid` raw log field to `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application_id`, `cato_app` raw log field(s) to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_request_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `public_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `threat_verdict` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `traffic_direction` raw log field to `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `user_object_id` raw log field to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.   
2025-02-05 |  \- Mapped If `Risk_level` = "` and `Severity` != `` then `security_result.severity = Severity".  
\- Mapped If `Risk_level` != "` and `Severity` = `` then `security_result.severity = risk_level".  
\- Mapped If `Risk_level` != "` and `Severity` != `` then `security_result.severity= severity` and `Risk` to `security_result.severity_details".   
2024-12-20 |  \- When `action` value is `MONITOR`, `ALERT`, `SUCCEEDED`, `ALLOW`, or `WHITELIST`, then mapped `sr_action` to `ALLOW`.  
\- When `action` value is `BLOCK` and `ACCESS_DENIED`, then mapped `sr_action` to `BLOCK`.  
\- When `action` value is `FAILED`, then mapped `sr_action` to `FAIL`.  
\- When `action` value is `PROMPT`, then mapped `sr_action` to `CHALLENGE`.  
\- When there is no `action` value, then mapped `sr_action` to `UNKNOWN_ACTION`.   
2024-11-15 |  Enhancement -  
\- When `action` value is Monitor`, `Alert`, and `Succeeded`, then mapped `security_result.action` to `ALLOW".  
\- When `action` value is `Block` and `BLOCK`, then mapped `security_result.action` to `BLOCK`.   
2024-01-26 |  Enhancement -  
\- Mapped `dest_port` to `target.port`.  
\- Mapped `os_type` to `principal.platform`.  
\- Mapped `pop_name` to `additional.fields`.  
\- Mapped `domain_name` to `principal.administrative_domain`.  
\- Mapped `account_id` to `target.user.userid`.  
\- Mapped `event_sub_type` to `metadata.description`.  
\- Mapped `rule_name` to `security_result.rule_name`.  
\- Mapped `rule_id` to `security_result.rule_id`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `http_host_name` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `src_site_name`, `event_type`, `event_count`, `dns_name`, `insertionDate`, `action`, `subnet_name`, `internalId`, `src_site`, `categories`, `app_stack`, `custom_categories`, `ISP_name`, and `rule` to `additional.fields`.  
\- Mapped `src_country_code` to `principal.resource.attribute.labels`.  
\- Mapped `dest_country_code` to `target.resource.attribute.labels`.  
\- Mapped `src_is_site_or_vpn`, and `is_sanctioned_app` to `security_result.detection_fields`.  
\- Mapped `src_isp_ip` and `src_ip` to `src.ip` and `src.asset.ip`.  
\- Mapped `application` to `principal.application`.  
\- Mapped `ip_protocol` to `network.ip_protocol`.  
\- Mapped `src_country` and `sourceCountry` to `principal.location.country_or_region`.  
\- Mapped `dest_country` to `target.location.country_or_region`.  
\- Mapped `tar_ip` and `dest_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `prin_ip` to `principal.ip` and `principal.asset.ip`.   
2023-05-19 |  Enhancement -  
\- Added support for new logs by mapping all fields under `fieldsMap`.  
\- Refactored code wherever possible.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
