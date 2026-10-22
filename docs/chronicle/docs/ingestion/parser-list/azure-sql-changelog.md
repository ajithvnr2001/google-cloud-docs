---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-sql-changelog/
title: Change log for AZURE_SQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:55.401262+00:00
---

# Change log for AZURE_SQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-sql-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_SQL

Date | Changes  
---|---  
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pooled_connection`, `client_options`, `client_options1`, `connect_options`, `packet_data_size` and `is_dac` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.about.ip`: Newly mapped `address` raw log field with `event.idm.read_only_udm.security_result.about.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `properties.action_name` is `login succeeded`, set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: If `category` is `SQLSecurityAuditEvents`, removed static mapping to `USER_LOGIN`.  
\- `event.idm.read_only_udm.extensions.auth.type`: if `category` is `SQLSecurityAuditEvents`, removed static mapping to `MACHINE`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `location` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `properties.database_principal_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.target_database_principal_id` and `properties.target_server_principal_id` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `properties.action_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.duration_milliseconds` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.object_id`, `properties.class_type_description`, `properties.ledger_start_sequence_number`, `properties.database_transaction_id`, `properties.user_defined_event_id`, `properties.transaction_id`, `properties.server_principal_id`, `properties.securable_class_type`, `properties.client_tls_version`, `properties.response_rows`, `PartitionId`, `operationName`, `properties.permission_bitmask`, `properties.affected_rows`, `properties.audit_schema_version`, `properties.object_name`, `properties.is_local_secondary_replica`, `properties.session_server_principal_name`, `properties.class_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `properties.action_name` is `audit session changed`, updated the value of event.idm.read_only_udm.metadata.event_type to `SETTING_MODIFICATION`.  
\- `event.idm.read_only_udm.target.resource.type`: If `properties.action_name` is `audit session changed`, updated the value of event.idm.read_only_udm.target.resource.type to `SETTING`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_target_resource`and `has_principal`are `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` and `has_target` are `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2024-12-04 |  Enhancement:  
\- Mapped `statement` to `additional.fields`.   
2024-11-07 |  Enhancement:  
\- Mapped `properties.server_principal_sid` to `principal.asset_id`.  
\- Mapped `properties.database_principal_name` to `target.resource.attribute.labels`.   
2024-11-06 |  Enhancement:  
\- Added `properties.client_ip` to the statedata.  
\- Mapped `count`, `total`, `maximum`, `minimum`, `average`, `timeGrain` and `metric_name` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
