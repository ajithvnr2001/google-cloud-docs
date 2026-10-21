---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-ips-changelog/
title: Change log for MCAFEE_IPS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:02:38.983341+00:00
---

# Change log for MCAFEE_IPS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-ips-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_IPS

Date | Changes  
---|---  
2026-09-07 |  Enhancement:  
\- Added support for `SYSLOG+KV` format.  
\- Modified grok patterns to extract `kv_data`, `time_1`, `ts`, and `appname`.  
\- Added IP validation check for `principal_ip` before mapping to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time_1` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ts`, `collection_time` raw log fields to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.administrative_domain`: Newly mapped `admin_domain` raw log field to `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sensor` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `deviceSeverity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `signature_id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category`: Newly mapped `cat` raw log field to `event.idm.read_only_udm.security_result.category` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `sub_cat` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `signature` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `deviceInboundInterface` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `count` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `act` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `direction` raw log field to `event.idm.read_only_udm.network.direction` UDM field.   
2026-07-13 |  Enhancement:  
\- Added support for JSON format of logs.  
\- Added grok patterns to parse the `message` raw log field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `collection_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SRC_IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `GEO` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.user.company_name`: Newly mapped `company_name` raw log field with `event.idm.read_only_udm.principal.user.company_name` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `DST_IP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `target_location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `destination_network_type` raw log field with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `Direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `security_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `threat_id` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `threat_name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity_number` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category_detail` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `priority`, `facility`, `appname`, `interface`, `message_type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `Action` is `deny` or `drop`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.   
2025-08-13 |  \- Newly added grok pattern for `message` data field to parse the `BTP` raw log field.  
\- `event.idm.read_only_udm.security_result.confidence` : Newly mapped `BTP` raw log field with `event.idm.read_only_udm.security_result.confidence` UDM field as `LOW_CONFIDENCE` when `BTP` is `Low` and `MEDIUM_CONFIDENCE` when `BTP` is `Medium` and `HIGH_CONFIDENCE` when `BTP` is `High` and `UNKNOWN_CONFIDENCE` when `BTP` is `Unknown`.  
\- Newly added grok pattern for `timestamp` data field to fetch the `year` data.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `header_timestamp` data field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-02 |  \- Added Grok patterns to parse the unparsed logs.  
\- Added split operation and for loop to convert Ip's into an array of principal_ip.  
\- `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added has_principal and has_target to identify the event type.  
\- Added on_error and if conditional statements wherever required.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
