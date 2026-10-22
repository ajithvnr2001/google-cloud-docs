---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fluentd-changelog/
title: Change log for FLUENTD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:46.423309+00:00
---

# Change log for FLUENTD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fluentd-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FLUENTD

Date | Changes  
---|---  
2025-10-31 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `stream` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `resource` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `kubernetes.pod_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `kubernetes.namespace_name` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `kubernetes.pod_id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `kubernetes.host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `kubernetes.container_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `kubernetes.container_image` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `kubernetes.container_hash` raw log field (specifically the SHA256 part) with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `msg` raw log field (extracted from log) with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `level` raw log field (extracted from log) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `kubernetes.docker_id`, `kubernetes.container_hash` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, then mapped to `STATUS_UPDATE`, else if `has_principal` is `false` then mapped `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.  
\- Added JSON filter for `message` data field to parse the JSON logs in the correct manner.  
\- The drop condition was updated to ensure that the log was only dropped if both `not_in_json` and `not_json_message` were set to `true`.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2022-09-28 |  Promoted parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
