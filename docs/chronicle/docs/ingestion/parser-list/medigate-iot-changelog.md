---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/medigate-iot-changelog/
title: Change log for MEDIGATE_IOT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:38.425643+00:00
---

# Change log for MEDIGATE_IOT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/medigate-iot-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MEDIGATE_IOT

Date | Changes  
---|---  
2025-08-08 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `events.id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `affected_device.device_name` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `affected_device.device_name` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `management_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `management_ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `updated_by` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `affected_device.os` raw log field(s) with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `affected_device.management_status`, `affected_device.labels` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `events_extra_info.direction` raw log field(s) with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `events_extra_info.ip_protocol` raw log field(s) with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `events.alert_id` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `affected_device.risk_score` raw log field(s) with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `events_extra_info.communication_type` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_user is `true`, updated to USER_UNCATEGORIZED.  
\- The parser now supports `Claroty` as a log_type in addition to `Medigate`.   
2025-03-06 |  Enhancement:  
\- Mapped `vulnerability_info.name`, `vulnerability_info.type`, `vulnerability_info.release_date`, `cve`, `vulnerability_info.cvssv3_base_score`, `vulnerability_info.description`, `vulnerability_info.affected_products`, `vulnerability_info.is_known_exploited`, `vulnerability_device_info.relevance`, `vulnerability_device_info.relevance_source`, `vulnerability_info.cvssv2_base_score`, `affected_device.device_subcategory`, `affected_device.retired`, and `affected_device.app_version` to `security_result.detection_fields`.  
\- Mapped `affected_device.risk_score` to `security_result.severity`.   
2025-01-21 |  Enhancement:  
\- Mapped `alert.id` to security_result.rule_id".  
\- Mapped `alert.type_name`, `alert.device_status`, `alert_info.certificate_thumbprint`, `alert_info.certificate_expiry_date`, `alert_info.certificate_start_date`, and `alert_info.certificate_type` to `security_result.detection_fields`.  
\- Mapped `alert.name` to `security_result.rule_name`.  
\- Mapped `alert.category` to `security_result.category_details`.  
\- Mapped `alert.description` to `security_result.description`.  
\- Mapped `alert.mitre_technique_ids`, `alert.mitre_technique_names`, `alert.mitre_technique_enterprise_ids`, `alert.mitre_technique_enterprise_names`, `affected_device.device_type_family`, `affected_device.connection_type_list`, and `affected_device.network_list` to `additional.fields`.  
\- Mapped `affected_device.mac_list` to `principal.mac`.  
\- Mapped `affected_device.ip_list` to `principal.ip`.  
\- If `alert_info.certificate_thumbprint` is valid sha256, then mapped to `network.tls.server.certificate.sha256` else mapped to `additional.fields`.   
2024-04-03 |  Enhancement:  
\- Mapped `location` to `principal.location.country_or_region`.  
\- Mapped `server_name` to `network.tls.client.server_name`.  
\- Mapped `incident_id` to `metadata.product_log_id`.  
\- Mapped `incident_type` to `metadata.description`.  
\- Mapped `msg_category`, `interface_name`, `interface_type`, and `status` to `additional.fields`.   
2023-12-08 |  Enhancement-  
\- Mapped `event_extra_info.malicious_ip_info.confidence` to `security_result.confidence_details`.  
\- Mapped `event_extra_info.malicious_ip_info.last_update` to `target.file.mime_type`.  
\- Mapped `event_extra_info.malicious_ip_info.tags` to `security_result.detection_fields`.  
\- Mapped `event_extra_info.malicious_ip_info.type` to `security_result.category_details`.  
\- Added mapping of `event_extra_info.malicious_ip_info.threat_type` to `security_result.about.labels`.  
\- Added gsub function to remove invalid characters from `inner_message`.  
\- Added a MAC address check to `comm_tuple.src_mac` and `comm_tuple.dst_mac`.  
\- Added a Grok pattern to parse new pattern of `comm_tuple.protocol`.   
2023-11-08 |  Enhancement-  
\- Mapped `events_extra_info.file_name` to `target.file.full_path`.  
-Mapped `events_extra_info.file_type` to `target.file.mime_type`.  
-Mapped `events_extra_info.sender_id` to `principal.user.userid`.   
2022-07-08 |  Enhancement-  
-Mapped `events.timestamp` to `metadata.event_timestamp`.  
-Mapped `events.description` to `metadata.description`.  
-Mapped `events_extra_info.domain` to `principal.administrative_domain`.  
-Mapped `events_extra_info.malicious_ip_info.source` to `security_result.about.labels`.  
-Mapped `events_extra_info.malicious_ip_info.threat_type` to `security_result.threat_name`.  
-Mapped `events_extra_info.malicious_ip_info.malicious_ip` to `intermediary.ip`.  
-Mapped `events_extra_info.malicious_ip_info.severity` to `security_result.severity`.  
-Mapped `events_extra_info.geo_location` to `target.location.country_or_region`.  
-Mapped `events_extra_info.client_id` and `affected_device.site_name` to `additional_fields`.  
-Mapped `comm_tuple.src_port` to `principal.port`.  
-Mapped `comm_tuple.dst_port` to `target.port`.  
-Mapped `comm_tuple.src_ip` to `principal.ip`.  
-Mapped `comm_tuple.dst_ip` to `target.ip`.  
-Mapped `comm_tuple.src_mac` to `principal.mac`.  
-Mapped `comm_tuple.dst_mac` to `target.mac`.  
-Mapped `affected_device.asset_id` to `principal.asset.asset_id`.  
-Mapped `affected_device.device_category` to `principal.resource.resource_subtype`.  
-Mapped `affected_device.device_type` to `principal.resource.name`.  
-Mapped `events.type` to `metadata.product_event_type`.  
-Mapped `affected_device.manufacturer` to `hardware.manufacturer`.  
-Mapped `affected_device.model` to `hardware.model`.  
-Mapped `version` to `network.tls.version`.  
-Mapped `proto` to `tls.version_protocol`.  
-Mapped `metadata.event_type` to `NETWORK_HTTP` where `comm_tuple.protocol` is `HTTP`.  
-Mapped `metadata.event_type` to `NETWORK_FTP` where `comm_tuple.protocol` is `FTP`.  
-Mapped `security_category` to `NETWORK_MALICIOUS` where `events.type` is `Malicious Internet Communication`.  
-Mapped `metadata.event_type` to `USER_LOGIN`, `events_extra_info.username` to `target.user.userid`and `extensions.auth.type` to `AUTHTYPE_UNSPECIFIED` where `events.type` is `Weak/Default Password`.  
-Mapped `events_extra_info.username` to `principal.user.userid`.  
-Mapped `events_extra_info.certificate_info.ST` to `principal.location.state`.  
-Mapped `events_extra_info.certificate_info.CN` to `principal.hostname`.  
-Mapped `events_extra_info.certificate_info.C` to `principal.location.country_or_region`.  
-Mapped `events_extra_info.certificate_info.L` to `principal.location.city`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
