---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-bigip-apm-changelog/
title: Change log for F5_BIGIP_APM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:06:14.880034+00:00
---

# Change log for F5_BIGIP_APM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-bigip-apm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_BIGIP_APM

Date | Changes  
---|---  
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `Tunnel_Type`, `partition` and `priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Client_IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Assigned_PPP_Dynamic_IPv4` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.about.resource.name`: Newly mapped `resource_name` raw log field with `event.idm.read_only_udm.about.resource.name` UDM field.  
\- Added a grok pattern to parse new pattern of SYSLOG logs.   
2026-03-24 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `f5_partition` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `f5_object_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `listener_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `geoContinent` and `reputation` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `f5_object_path` to extract `f5_partition`, `f5_object_name`.   
2025-12-15 |  Enhancement:  
\- Added grok pattern to parse new pattern of logs.  
\- Added kv filter on `http_request` raw log field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `User-Agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `http_protocol_info` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `User-Agent` is not null.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `X-Forwarded-For` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Accept-Encoding` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Accept` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `timestamp1` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.ip` UDM field and `event.idm.read_only_udm.target.asset.ip` UDM field if `host` is an IP address.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `http_protocol_info` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- Added conditional checks for `micro_service_name`, `micro_service_type`, and `application_version` now exclude both empty strings and `N/A`.  
\- event.idm.read_only_udm.metadata.event_type: If `principal_ip` and `dest_ip` are present, updated to `NETWORK_CONNECTION`.   
2025-11-12 |  Enhancement  
\- Added support to parse new format of json logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `source_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `destination_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2025-11-07 |  Enhancement  
\- Added a grok pattern to parse new pattern of logs.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `bigip_mgmt_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `bigip_mgmt_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `bigip_mgmt_ip2` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `bigip_mgmt_ip2` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `client_ip_geo_location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `client_request_uri` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `configuration_date_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `context_name` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `context_type` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dest_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `dest_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `device_product` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `device_version` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `errdefs_msgno` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `http_protocol_info` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `http_protocol_info` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `route_domain` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `captcha_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `browser_verification_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `client_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jailbroken_or_rooted_device` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mobile_debugger_enabled_device` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `imei` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `http_request` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `human_behaviour` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.cloud.vpc.name: Newly mapped `virtual_server_name` raw log field with `event.idm.read_only_udm.principal.cloud.vpc.name` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `request_date_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `profile_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `support_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `request_status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `previous_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `anomaly_categories` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `previous_support_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `configured_mitigation_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `configured_mitigation_action_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `actual_mitigation_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `actual_mitigation_action_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `anomalies` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `browser_configured_verification_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `browser_actual_verification_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `browser_actual_verification_action_reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `previous_request_date_time` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `bot_signature` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `bot_signature_category` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `device_id_status` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `bot_name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `device_id_action` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `previous_initiated_action` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `class` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `previous_initiated_action_status` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `enforced_by` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `additional_bot_signatures` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `headless_signatures` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `micro_service_matched_wildcard_url` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `micro_service_hostname` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `mobile_is_app` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `mobile_in_emulation_mode` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `challenge_failure_reason` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `os_name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `classification_reason` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `new_request_status` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `micro_service_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `micro_service_type` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `application_display_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.platform_version: Newly mapped `application_version` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `http_protocol_indication` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-07-17 |  Enhancement  
\- Added new grok patterns for `tmm` application logs to parse additional log variations containing rule names, application protocols, and file paths.  
\- Implemented conditional logic to map appprotocol to standard values (HTTP, HTTPS, SSH) in event.idm.read_only_udm.network.application_protocol.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rulename` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `filepath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `appprotocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.   
2024-09-11 |  Enhancement  
\- Added support to parse unparsed logs.   
2023-06-06 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
