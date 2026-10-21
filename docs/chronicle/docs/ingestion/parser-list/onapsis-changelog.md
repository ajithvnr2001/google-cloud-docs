---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onapsis-changelog/
title: Change log for ONAPSIS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:15:55.061342+00:00
---

# Change log for ONAPSIS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onapsis-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONAPSIS

Date | Changes  
---|---  
2026-07-07 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `metadata_data.capacity`, `event_id`, `incident_detail`, `appliancesStates`, `task`, `related_to.tag.list`, `related_to.tag.operator`, `conditions` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `metadata_data.name`, `data.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `data.vendors`, `data.fields_to_keep`, `data.filters.names_regex`, `data_cadence`, `enabled` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `leef_version` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `metadata_data.type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `metadata_data.description`, `reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `anomaly_score` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `devTime`, `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `logline` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msgid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `metadata_data.severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly Mapped `username` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field when username consists of numeric values.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `erp_host` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-11-25 |  Enhancement:  
\- Added support for a new log format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `conditions.condition_id`, `conditions.eval_value.success`, `conditions.matched`, `erp_event_source`, `erp_time`, `protocol` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.confidence_details: Newly mapped `confidence` raw log field with `event.idm.read_only_udm.security_result.confidence_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `success` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- event.idm.read_only_udm.metadata.event_type: If `event_type` is `UserLogin` and `has_target` is `true`, updated to `USER_LOGIN`.  
\- The `created_at` field now supports `RFC 3339` and `ISO8601` date formats.  
\- The logic for populating `principal.ip`, `principal.asset.ip`, `principal.hostname`, and `principal.asset.hostname` has been updated to check if the source fields (`host`, `src`, `terminal_source`) are valid IP addresses.   
2023-12-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
