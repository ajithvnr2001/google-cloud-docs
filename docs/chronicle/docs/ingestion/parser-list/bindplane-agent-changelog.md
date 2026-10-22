---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bindplane-agent-changelog/
title: Change log for BINDPLANE_AGENT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:53.610360+00:00
---

# Change log for BINDPLANE_AGENT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bindplane-agent-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BINDPLANE_AGENT

Date | Changes  
---|---  
2025-11-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Keywords`, `action_id`, `is_column_permission`, `connection_id`, `permission_bitmask`, `sequence_group_id`, `sequence_number`, `server_principal_name`, `server_principal_sid`, `succeeded`, `system_time`, `user_defined_event_id`, `affected_rows`, `response_rows`, `duration_milliseconds` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `audit_event` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `EventID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `EventRecordID` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `object_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `session_server_principal_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `ProviderName`, `Task`, `Channel` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `statement` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `server_principal_id`, `transaction_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `class_type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `database_principal_id`, `target_server_principal_id`, `target_database_principal_id`, `database_principal_name`, `server_instance_name`, `object_name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `database_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-09-18 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_host` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `interval` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `otelcol.component.id` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `otelcol.component.kind` raw log field to `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `otelcol.signal` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `resource.service.instance.id` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `resource.service.name` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `resource.service.version` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- Modified the spelling of `principal` for correct mapping of the `caller` raw log field.   
2025-03-05 |  Enhancement:  
\- Mapped `ts` to `metadata.event_timestamp`.  
\- Mapped `path` to `target.process.file.full_path`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `name` to `target.process.file.names`.  
\- Mapped `component` to `additional.fields`.   
2024-12-27 |  \- Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
