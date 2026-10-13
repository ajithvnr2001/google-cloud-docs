---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-harmony-changelog/
title: Change log for CHECKPOINT_HARMONY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:32.878347+00:00
---

# Change log for CHECKPOINT_HARMONY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-harmony-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHECKPOINT_HARMONY

Date | Changes  
---|---  
2026-07-24 |  Enhancement:  
\- Added support to parse new format of SYSLOG + JSON logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tenant_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `severity_int`, `confidence_level_int`, `status` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-18 |  Enhancement:  
\- Added support for new CEF and JSON log formats.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `cef_device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `device_id`,`data.device_id` raw log fields with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `upload_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `download_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `device_type`, `json_additional_data.os`, `json_additional_data.os_version`, `json_additional_data.time_zone`, `json_additional_data.architecture`, `json_additional_data.vpn_connected`, `json_additional_data.producer`, `json_additional_data.tenant_id`, `json_additional_data.user_vpn_protocol`, `additional_data.gateway_id`, and `additional_data.user_vpn_protocol` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `json_additional_data.rule_number` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `json_additional_data.user_type` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `categories`, `additional_data.service_name`, `additional_data.service_version` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `additional_data.tenant_id`, `json_additional_data.unique_event_id`, `additional_data.unique_event_id`, `json_additional_data.processing_time`, `additional_data.processing_time`, `json_additional_data.agent_event_time`, `dedup_time`, `json_additional_data.creation_time`, `last_hit_time`, `appi_db_version`, `hll_key`, `_tenant_id`, `cat`, `act`, `json_additional_data.user_vpn_connection_time`, `additional_data.user_vpn_connection_time`, `syslog_priority`, `proc_id`, `rt`, `app_name`, `app_version`, `syslog_version`, `cef_name`, `type`, `cef_version`, and `statusCode` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip`, `json_additional_data.local_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `client_time_zone` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `syslog_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `file_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `data.user_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `email`, `data.email` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `data.rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `cef_signature_id` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `cef_product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2026-03-19 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Changed mapping for `label`. It is now mapped to `event.idm.read_only_udm.security_result.detection_fields` (key: `label`) only if `label` is not a valid email address.  
\- `event.idm.read_only_udm.network.email.to`: If `label` is a valid email address and does not match `senderAddress`, mapped `label` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `entityLink` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `actionType` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: If `product` and `fw_subproduct` are empty, updated the value of `event.idm.read_only_udm.metadata.product_name` to `Checkpoint Harmony`.  
\- Added a conditional check before already existing mapping of `senderAddress` to `event.idm.read_only_udm.network.email.from` UDM field.  
\- Added a conditional check before already existing mapping of `each` to `event.idm.read_only_udm.network.email.to` UDM field.  
\- Added a conditional check before already existing mapping of `vendor_name` to `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- Newly added gsubs for `message` field allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.description`  
2026-02-25 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `time`, origin`, `scrubbed_content` and `event_id` raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with event.idm.read_only_udm.intermediary.hostname UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Mapped `to` raw log field to event.idm.read_only_udm.network.email.to UDM field when it is a valid email address.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `to` raw log field to event.idm.read_only_udm.security_result.detection_fields UDM field when it does not represent a valid email address.  
\- `event.idm.read_only_udm.security_result.detection_fields: Newly mapped `indicator_type`, `max_count_detected`, `dlp_relevant_data_types`, `dlp_categories` and `matchedIndicators` raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Modified the logic for mapping `action` raw log field with event.idm.read_only_udm.security_result.action UDM field to include `Prevent` as a BLOCK action.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `add_spam_header` raw log field with event.idm.read_only_udm.security_result.action_details UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: A Grok pattern is applied to `origin`, and the field is only mapped to event.idm.read_only_udm.intermediary.ip if the Grok successfully extracts a valid IP address.  
\- `event.idm.read_only_udm.principal.asset.ip`: Corrected the spelling of `principal.asset.ip`.  
\- Added a Grok pattern to handle syslog+kv format logs,this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.email.from`  
\- `event.idm.read_only_udm.network.email.reply_to`  
\- `event.idm.read_only_udm.network.email.subject`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.target.file.md5`  
\- `event.idm.read_only_udm.target.file.size`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.security_result.rule_id`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.target.process.file.full_path`  
\- `event.idm.read_only_udm.target.process.file.md5`  
2026-01-30 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventCreated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `act.createTime`, `act.relatedEntityId`, `customerId`, `saas`, `state`, `entityId`, `connectivity_state` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `actions.actionType` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.category and event.idm.read_only_udm.security_result.category_details: If `confidenceIndicator` is similar to `malicious` map to `event.idm.read_only_udm.security_result.category` else map to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `entity_id`, `entity_type`, `disable_link`, `label` from data raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `senderAddress` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.   
2025-01-08 |  \- Added a Grok pattern to handle variations in logs.  
\- Added new fields.   
2024-12-12 |  Enhancement:  
\- Added support for new log patterns.   
2023-11-10 |  Created a new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
