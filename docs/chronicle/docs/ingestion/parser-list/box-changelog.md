---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/box-changelog/
title: Change log for BOX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:52.592782+00:00
---

# Change log for BOX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/box-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BOX

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `entry.source.item_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `entry.source.item_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Newly mapped `entry.source.parent.name` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.product_object_id`: Newly mapped `entry.source.parent.id` raw log field with `event.idm.read_only_udm.target.resource_ancestors.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.resource_subtype`: Newly mapped `entry.source.parent.type` raw log field with `event.idm.read_only_udm.target.resource_ancestors.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `entry.source.owned_by.id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `entry.source.owned_by.name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `entry.source.owned_by.login` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `entry.source.classification.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `entry.source.owned_by.type` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `entry.created_by.type` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.   
2026-01-12 |  Enhancement:  
\- Added support for the event `SHIELD_DOWNLOAD_BLOCKED` and relevant corresponding raw log fields.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_address` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip_address` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `created_by.id` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `created_by.name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `created_by.login` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `additional_details.shield_download_enforcement.item.name` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `additional_details.shield_download_enforcement.item.id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `additional_details.shield_download_enforcement.item.size` raw log field to `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.target.file.sha1: Newly mapped `additional_details.shield_download_enforcement.item.sha1` raw log field to `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `additional_details.service_name` and `additional_details.shield_download_enforcement.service.name` raw log fields to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `additional_details.shield_download_enforcement.classification` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.target.labels: Newly mapped `additional_details.shield_download_enforcement.service.service` raw log field to `event.idm.read_only_udm.target.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `additional_details.shield_download_enforcement.controlMode`, `additional_details.shield_download_enforcement.access_user.type`, `additional_details.shield_download_enforcement.access_user.id`, `additional_details.shield_download_enforcement.access_user.name`, and `additional_details.shield_download_enforcement.access_user.login` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `additional_details.service_id`, `chunk_size`, and `next_stream_position` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `additional_details.shield_download_enforcement.item.type` raw log field to `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `additional_details.shield_download_enforcement.item.file_version_id` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2024-03-11 |  Enhancement -  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.event_type` to `metadata.product_event_type`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.city_name` to `principal.location.city`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.country_code` to `principal.location.country_or_region`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.latitude` to `principal.location.region_coordinates.latitude`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.longitude` to `principal.location.region_coordinates.longitude`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.region_name` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.ip` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.ip_info.registrant` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.item_id` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.item_name` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.item_path` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.item_type` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.alert_activities.0.occurred_at` to `additional_fields`.  
\- Mapped `entry.additional_details.shield_alert.priority` to `security_result.severity`.  
\- Mapped `entry.additional_details.shield_alert.alert_id` to `security_result.rule_id`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.static_scan_result.family` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.static_scan_result.scan_result` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.static_scan_result.scanned_at` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.threat_info.description` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.threat_info.scanned_at` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.threat_info.source` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.threat_info.status` to `security_result.detection_fields`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.threat_info.threat_name` to `security_result.detection_fields`.  
\- Mapped session details carrying two activities details in the raw logs.  
\- Mapped additional fields for `Anomalous Downloads` type of logs.   
2024-01-12 |  Enhancement -  
\- Mapped additional fields when `metadata.product_event_type` is `DOWNLOAD`.  
\- Mapped additional fields when `metadata.product_event_type` is `SHIELD_DOWNLOAD_BLOCKED`.   
2023-12-04 |  Enhancement -  
\- Mapped additional fields when `metadata.product_event_type` is `SHIELD_ALERT`.  
\- Mapped `entry.additional_details.shield_alert.user.email` to `principal.user.email_addresses`.  
\- Mapped `entry.additional_details.shield_alert.user.id` to `principal.user.userid`.  
\- Mapped `entry.additional_details.shield_alert.user.name` to `principal.user.user_display_name`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.file_info.name` to `target.file.names`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.file_info.size` to `target.file.size`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.malware_info.file_info.hash` to `target.file.sha1`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.upload_activity.item_path` to `target.file.full_path`.  
\- Mapped `entry.additional_details.shield_alert.rule_category` to `security_result.category_details`.  
\- Mapped `entry.additional_details.shield_alert.rule_id` to `security_result.rule_id`.  
\- Mapped `entry.additional_details.shield_alert.rule_name` to `security_result.rule_name`.  
\- Mapped `entry.additional_details.shield_alert.risk_score` to `security_result.risk_score`.  
\- Mapped `entry.additional_details.shield_alert.alert_summary.description` to `security_result.description`.   
2022-09-16 |  Enhancement - Migrated to default parser.   
2022-07-29 |  Enhancement -  
\- Modified the mapping for `source.folder_id`, `source.file_id` and `source.item_id` from `target.resource.id` to `target.resource.product_object_id`.  
\- Added conditional checks for the fields `created_by.login`, `source.login`, `source.user_email`, `source.owned_by.login` and `accessible_by.login`.  
\- Changed `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` for `DEVICE_TRUST_CHECK_FAILED`, `USER_AUTHENTICATE_OAUTH2_ACCESS_TOKEN_CREATE`, `SHARED_LINK_REDIRECT_OUT_OF_SHARED_CONTEXT`, `TERMS_OF_SERVICE_ACCEPT`,`OAUTH2_ACCESS_TOKEN_REVOKE`, `ADD_DEVICE_ASSOCIATION`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
