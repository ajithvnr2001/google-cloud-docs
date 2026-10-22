---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nexus-sonatype-changelog/
title: Change log for NEXUS_SONATYPE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:37.639321+00:00
---

# Change log for NEXUS_SONATYPE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nexus-sonatype-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NEXUS_SONATYPE

Date | Changes  
---|---  
2025-11-18 |  \- event.idm.read_only_udm.principal.hostname: Removed `resource_name` of `raw_field` from `event.idm.read_only_udm.principal.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed `resource_name` of `raw_field` from `event.idm.read_only_udm.principal.asset.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.hostname: Mapped `resource_name` of `raw_field` with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Mapped `resource_name` of `raw_field` with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- Added a conditional check before mapping event_type with `NETWORK_HTTP`.   
2025-10-17 |  \- Newly created parser.  
\- Set event.idm.read_only_udm.metadata.vendor_name to `NEXUS_SONATYPE` and event.idm.read_only_udm.metadata.product_name to `NEXUS`.  
\- Modified grok patterns to parse the jsonPayload.message field.  
\- Implemented conditional logic to set event.idm.read_only_udm.metadata.event_type based on the presence of principal, target, and principal user information.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `insertId` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `labels.compute.googleapis.com/resource_name` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `labels.compute.googleapis.com/resource_name` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.log_type: Newly mapped `logName` raw log field to `event.idm.read_only_udm.metadata.log_type` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `receiveTimestamp` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `resource.labels.instance_id` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.cloud.project.name: Newly mapped `resource.labels.project_id` raw log field to `event.idm.read_only_udm.target.cloud.project.name` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `resource.labels.zone` raw log field to `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.type: Newly mapped `resource.type` raw log field to `event.idm.read_only_udm.principal.resource.type` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.ingested_timestamp: Newly mapped `date` raw log field to `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `http_url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `http_protocol` raw log field to `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `response_bytes` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `user_agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels.agent.googleapis.com/log_file_path`, `ident`, `nexus_field_1`, and `request_duration_ms` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `auth` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `thread_id` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
