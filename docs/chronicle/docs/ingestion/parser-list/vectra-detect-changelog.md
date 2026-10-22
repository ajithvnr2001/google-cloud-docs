---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-detect-changelog/
title: Change log for VECTRA_DETECT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:33.282715+00:00
---

# Change log for VECTRA_DETECT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vectra-detect-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VECTRA_DETECT

Date | Changes  
---|---  
2025-12-30 |  \- Added support for inner JSON formatted logs in VECTRA_DETECT.   
2025-06-03 |  \- Added Fallback parser for VECTRA_DETECT to handle log_type other than JSON.   
2025-05-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `detection_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `id`, `entity_id`, `detail.event_id`, `detail.account_id`, `detail.dst_host.id`, `detail.dst_host.session_luid`, `detail.src_account.id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped , `detection_type`, `entity_type`, `entity_uid`, `detail.event_name`, `detail.sensor.count`, `detail.count`, `detail.first_timestamp`, `detail.last_timestamp`, `detail.additional_details.client_name`, `detail.additional_details.cookie`, `detail.additional_details.encrypted`, `detail.additional_details.normal`, `phase1_bytes.sent`, `phase1_bytes.recv`, `phase2_bytes.sent`, `phase2_bytes.recv`, `breadth_contrib`, `entity_importance`, `importance`, `is_prioritized`, `urgency_score`, `velocity_contrib`, `attack_rating`, `active_detection_types`, `last_detection_type`, `last_detection_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `threat` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.confidence`: Newly mapped `certainty` raw log field with `event.idm.read_only_udm.security_result.confidence` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Nelwy mapped `detection_href` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `detail.src_host.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `detail.src_host.name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `detail.dst_host.ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `detail.dst_host.name` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `detail.src_account.name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `detail.dst_account.id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `detail.dst_account.name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `detail.sensor.name` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `detail.dst_port`, `detail.additional_details.dst_ips` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Nelwy mapped `detail.bytes_received` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `last_detection_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses` \- Newly mapped `detail.account_uid` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.   
2025-05-14 |  \- New label VECTARA_XDR created for RUX data and this label support only QUX data.  
\- Updated parser to support only JSON format logs.  
\- Added support for detection, entities, match, lockdown, audit and health log types.   
2025-01-16 |  Enhancement:  
\- Mapped `certainty` to `additional.fields`.   
2024-08-21 |  Enhancement:  
\- Added support for a new pattern of syslog logs.   
2024-07-22 |  Enhancement:  
\- Mapped `threat`, `certainty`, and `score_decreases` to `additional.fields`.   
2024-05-03 |  Enhancement:  
\- Mapped `detection_profile.name`, `detection_profile.vname`, and `detection_profile.scoringDetections` to `security_result.detection_fields`.   
2024-04-18 |  Enhancement:  
\- Mapped `msg.quadrant` to `security_result.priority_details`.   
2024-03-04 |  Enhancement:  
\- Added support for new pattern of `Audit` type logs.  
\- When `suser` is a valid email, then mapped `suser` to `principal.user.email_addresses`.  
\- When `suser` is not a valid email, then mapped `suser` to `principal.user.userid`.  
\- Added a conversion fail check for `flexNumber1` and `flexNumber2`.  
\- When `src` is not empty, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- When `user_present` is `true`, then set `metadata.event_type` to `USER_UNCATEGORIZED`.  
\- When `principal_present` is `true` and `target_present` is `true`, then set `mnetadata.event_type` to `NETWORK_CONNECTION`.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.   
2024-01-11 |  Enhancement:  
\- Added support for `Audit` and `Health` type logs.  
\- Mapped `message` to `security_result.summary`.  
\- Mapped `security_result.action` to `BLOCK` when `result` is `failure`.  
\- Mapped `security_result.action` to `ALLOW` when `result` is `true`.  
\- Mapped `result` to `security_result.detection_fields`.  
\- Mapped `type` to `metadata.product_event_type`.   
2023-10-12 |  Enhancement:  
\- Mapped `quadrant` to `security_result.priority_details`.  
\- Added conditions to map `threat` to `security_result.severity` as `INFORMATIONAL`, `LOW`, `MEDIUM`, `HIGH` and `CRITICAL`.  
\- Added conditions to map `certainty` to `security_result.confidence` as `LOW_CONFIDENCE`, `MEDIUM_CONFIDENCE` and `HIGH_CONFIDENCE`.   
2023-04-14 |  Enhancement -  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `externalId` to `metadata.product_log_id`.  
\- Mapped `event_name` and `device_event_class_id` to `metadata.product_event_type`.  
\- Mapped `cat` to `security_result.category_details`.  
\- Mapped `dvc` to `observer.ip`.  
\- Mapped `dvchost` to `observer.hostname`.  
\- Mapped `shost` to `principal.hostname`.  
\- Mapped `src` to `principal.ip`.  
\- Mapped `dst` to `target.ip`.  
\- Mapped `dhost` to `target.hostname`.  
\- Mapped `cs5` to `additional.fields`.  
\- Mapped `cs4` to `metadata.target.url`.  
\- Mapped `out` to `network.sent_bytes`.  
\- Mapped `in` to `network.received_bytes`.  
\- Mapped `dpt` to `target.port`.  
\- Mapped `cs5` to read_only_udm.alert.  
\- Mapped `severity` to security_result.severity_details.  
\- Mapped `flexNumber1` to security_result.severity.  
\- Mapped `flexNumber2` to security_result.confidence.  
\- Mapped `proto` to `network.ip_protocol`.  
\- Added `on_error` check for `severity` parameter.   
2022-09-26 |  Enhancement -  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `detection_id` to `metadata.product_log_id`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `d_type` to `additional.fields`.  
\- Mapped `d_type_vname` to `additional.fields`.  
\- Mapped `triaged` to `additional.fields`.  
\- Mapped `headend_addr` to `observer.ip`.  
\- Mapped `href` to `metadata.target.url`.  
\- Mapped `dd_bytes_sent` to `network.sent_bytes`.  
\- Mapped `account_uid` to `additional.fields`.   
2022-08-25 |  Enhancement -  
\- Converted the parser from SDM to UDM.  
\- Mapped `triage` to read_only_udm.alert.  
\- Mapped severity to security_result.severity_details.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
