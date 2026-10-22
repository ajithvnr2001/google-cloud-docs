---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/illumio-core-changelog/
title: Change log for ILLUMIO_CORE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:21.923699+00:00
---

# Change log for ILLUMIO_CORE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/illumio-core-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ILLUMIO_CORE

Date | Changes  
---|---  
2026-09-10 |  Enhancement:  
\- Added a conditional check before already existing mapping of `src_ip` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `notify.info.user.username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `notify.info.user.href` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Updated the mapping logic for existing `resource.changes.status.before`, `resource.changes.status.after` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field by appending array indices to the key values to parse fields accurately across multiple entries.  
\- event.idm.read_only_udm.metadata.event_type: Mapped `USER_UNCATEGORIZED` to `event.idm.read_only_udm.metadata.event_type` UDM field when log contains principal machine data and target user data.   
2026-07-17 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `obs_pid` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `action.src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `action.api_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `action.http_status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `created_by.user.username` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `resource.resource.user.username` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `resource.changes.status.before` and `resource.changes.status.after` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `created_by.user.href`, `created_by.agent.href`, `created_by.agent.hostname`, `created_by.ven.href`, `created_by.ven.hostname` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `resource.resource.user.href`, `resource.resource.user.type` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.resource.ven.href`, `resource.resource.agent.href` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action.api_endpoint`, `action.uuid`, `resource.uuid`, `resource.change_type`, `resource.resource.workload.href`, `resource.resource.workload.name`, `resource.resource.workload.hostname`, `resource.changes.local.before`, `resource.changes.local.after`, `resource.changes.password_changed_at.before`, `resource.changes.last_goodbye_at.before`, `resource.changes.last_goodbye_at.after`, `resource.changes.name.after`, `resource.changes.enforcement_mode.before`, `resource.changes.enforcement_mode.after`, `resource.changes.description.after`, `resource.changes.password_changed_at.after`, `label.key`, `label.value`, `label.href` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-29 |  Enhancement:  
\- Added new grok patterns to parse new format of syslog logs.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `outcome` raw log field with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `shost`, `program` raw log fields with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-12-11 |  Enhancement:  
\- Added a new grok pattern to support new format of logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `org_id` raw log field with `org_id` as the key with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `network` raw log field with `network` as the key with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `src.dm` raw log field with `src_dm` as the key with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `src.os` raw log field with `src_os` as the key with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `src.vt_type` raw log field with `src_vt_type` as the key with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Removed explicit mappings for `src_labels.env`, `src_labels.app`, and `src_labels.role` and `src_labels` is handled dynamically using for loop iterating through `src_labels`, mapping each key-value pair (except loc) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field with the key prefixed by `src_`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed explicit mappings for `dst_labels.env`, `dst_labels.app`, and `dst_labels.role` and `dst_labels` is handled dynamically using for loop iterating through `dst_labels`, mapping each key-value pair (except loc) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field with the key prefixed by `dst_`.   
2024-11-14 |  Enhancement:  
\- When there is no principal machine data available, then mapped `metadata.event_type` to `GENERIC_EVENT`.  
\- Mapped `uuid`,`change_type`,`href`,`name`,`hostname` labels to `sec_res.detection_fields`  
2024-04-18 |  Enhancement:  
\- Enhanced parser to additionally support SYSLOG+CEF log formats.   
2024-02-21 |  Enhancement:  
\- Enhanced parser to additionally support SYSLOG and SYSLOG+JSON log formats.   
2023-03-14 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
