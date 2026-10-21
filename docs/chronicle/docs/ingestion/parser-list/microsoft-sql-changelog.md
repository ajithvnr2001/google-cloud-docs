---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sql-changelog/
title: Change log for MICROSOFT_SQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:48:08.492567+00:00
---

# Change log for MICROSOFT_SQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-sql-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_SQL

Date | Changes  
---|---  
2026-09-25 |  Enhancement:  
\- Added support to parse XML logs from `ev_data` and `ev_data_2` when `Msg` is not present.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ev_qualifiers`, `ev_binary`, `session_server_principal_name`, `pooled_connection`, `total_cpu`, `reads`, `writes`, `is_dac` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `succeeded` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when `action_id` is `LGO`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Mapped `event.idm.read_only_udm.extensions.auth.type` to `MACHINE` for logout events.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `ev_data` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field when `ev_data_2` contains client IP information.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `user_sid` raw log field to `event.idm.read_only_udm.principal.user.windows_sid` UDM field for XML logs.   
2026-07-24 |  Enhancement:  
\- Added support for new format of JSON and KV logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `audit_file_offset` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `CEST` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-06-11 |  Enhancement:  
\- Added a new grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ActionId`, `SessionSPN`, `ServerInstance`, `AccountType`, `EventType`, `TaskValue`, `RecordNumber`, `pooled_connection`, `client_options`, `client_options1`, `connect_options` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `Domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_id` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field, sets the value to `TCP` when the `protocol` is `TCP`.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `filepath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `target_resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `sqlstate`, `message_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `network_library`, `new_value`, `old_value`, `build_number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added grok patterns to prevent incorrect mapping to `event.idm.read_only_udm.metadata.event_timestamp.nanos` and `event.idm.read_only_udm.metadata.description`. This change also ensures the correct parsing of the following UDM fields:  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.principal.process.pid`  
2026-02-16 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `sql_product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `agent.ephemeral_id`, `product_edition`, `build_timestamp`, `patch_level`, `os_build`, `kb_article` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.cpu_platform`: Newly mapped `architecture` raw log field with `event.idm.read_only_udm.principal.asset.hardware.cpu_platform` UDM field.  
\- `event.idm.read_only_udm.target.platform_version`: Newly mapped `platform_version` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.platform`: Newly mapped `platform_version` raw log field with `event.idm.read_only_udm.target.platform` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `os_architecture`, `virtualization` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- Added the new grok pattern to parse the new format of logs this fixed the parsing issues allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.extensions.auth.type`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.log_type`  
2026-01-30 |  Enhancement:  
\- The `event.idm.read_only_udm.security_result.action` UDM field is now conditionally merged with `_login_result` raw log information, only if `security_result_action` is null then mapping `event.idm.read_only_udm.security_result.action` UDM field to `_login_result` raw log field.  
\- Added JSON filter for `_raw` field to parse the raw log fields in correct format.  
\- Newly added gsub for the `Message` raw log field to parse the raw log fields in correct format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Version`, `Opcode`, `RecordId`, `MachineName`, `ProcessId`, `ThreadId`, `LevelDisplayName`, `KeywordsDisplayNames`, `ledger_start_sequence_number`, `data_sensitivity_information`, `session_context`, `client_tls_version_name`, `external_policy_permissions_checked`, `Qualifiers` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-29 |  Enhancement:  
\- Added support for SYSLOG + XML log format.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `/Event/System/EventRecordID` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `/Event/System/Execution/@ProcessID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `/Event/System/Security/@UserID` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `/Event/System/Execution/@ThreadID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-15 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `extracted_client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `extracted_client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added conditional check for Msg: The new mappings to event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip are only performed if the grok pattern \\\\[CLIENT[=:]\\\s*%{IP:extracted_client_ip}\\\\] successfully matches and extracts extracted_client_ip from the Msg field.   
2025-12-17 |  Enhancement:  
\- Added support for XML log format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Keywords`, `SystemTime`, `action_id`, `affected_rows`, `connection_id`, `duration_milliseconds`, `is_column_permission`, `permission_bitmask`, `response_rows`, `schema_name`, `sequence_group_id`, `sequence_number`, `server_principal_name`, `server_principal_sid`, `succeeded`, `user_defined_event_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `audit_event` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `EventRecordID` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `object_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `session_server_principal_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `ProviderName`, `Task`, `Channel` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `class_type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `statement` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `server_principal_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `database_principal_id`, `target_server_principal_id`, `target_database_principal_id`, `transaction_id`, `database_principal_name`, `server_instance_name`, `object_name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `database_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2025-10-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `security.user_id` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `computer` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `computer` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `provider.name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `DATABASE` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when `provider.name` is equal to `MSSQLSERVER`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `keywords` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TYPE` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `system_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `channel`, `event_data.binary`, `event_id.qualifiers`, `opcode`, `provider.event_source`, `provider.guid`, `record_id`, `task`, `creation_date`, `pages_dumped`, `first_LSN`, `last_LSN`, `number_of_dump_devices`, `device_information` and `FILE` raw log field with event.idm.read_only_udm.additional.fields UDM field.   
2025-08-14 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `winlog.record_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `winlog.user.identifier` raw log field to `event.idm.read_only_udm.principal.user.windows_sid`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `winlog.user.name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped winlog.channel, `winlog.event_id`, `winlog.event_data.Binary`, `winlog.event_data.param1`, `winlog.event_data.param2`, `syslog_facility` and `syslog_facility_code` raw log fields to event.idm.read_only_udm.additional.fields.  
\- Modified a grok pattern to handle logs with [CLIENT: ] at the end of the message.  
\- Modified grok pattern to handle login events without client address.   
2025-04-17 |  Enhancement  
\- Added a Grok to parse a new pattern of logs with SYSLOG + KV format.  
\- Set `has_principal_user` to true where `server_principal_name` is mapped with `event1.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `connection_id` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip and `event1.idm.read_only_udm.principal.asset.ip`: Newly mapped `HOST` raw log field with `event1.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to true.  
\- Added a conditional to check if `host` raw log field is not null before mapping it with `event1.idm.read_only_udm.observer.hostname` UDM field.  
\- Added a conditional to check if `ObjectName` raw log field is not null before mapping it with `event1.idm.read_only_udm.target.resource.name` UDM field.  
\- Added a conditional to check if `SPID` raw log field is not null before mapping it with `event1.idm.read_only_udm.network.session_id` UDM field.   
2025-04-09 |  \- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- event.idm.read_only_udm.principal.ip and principal.asset.ip: Newly mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `Id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `alertWebUrl` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `tenantId` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `detectorId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- USER_UNCATEGORIZED: Removed mapping of `metadata.event_type` from `USER_UNCATEGORIZED` UDM field.  
\- USER_RESOURCE_DELETION: Mapped `metadata.event_type` with `USER_RESOURCE_DELETION` UDM field When the error_code are `118`, `129`, `47`, `73`, `77`, `200`, `131`, `136`, `140`, `201`.  
\- USER_RESOURCE_ACCESS: Mapped `metadata.event_type` with `USER_RESOURCE_ACCESS` UDM field When the error_code are `28`, `29`, `69`, `114`, `30`, `31`.  
\- USER_RESOURCE_UPDATE_CONTENT: Mapped `metadata.event_type` with `USER_RESOURCE_UPDATE_CONTENT` UDM field When the error_code are `176`.  
\- Added a null condition check for `host` raw log field before mapping `event1.idm.read_only_udm.observer.hostname` UDM field   
2025-03-19 |  Enhancement  
\- Added support for csv format logs.  
\- Mapped `column2` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `column3` to `additional.fields`.  
\- Mapped `column4` to `principal.process.file.full_path`.  
\- Added a grok pattern to parse `event_time`, `user`, `msg` from the field `column7`.   
2025-02-26 |  Enhancement  
\- Added support for a new pattern of syslog logs.   
2024-11-28 |  Bug-Fix:  
\- When `action_id` is `LGIF`, then mapped `security_result.action` to `BLOCK`.   
2024-10-29 |  Enhancement:  
\- Added support for a new pattern of SYSLOG + JSON logs.   
2024-10-22 |  Enhancement:  
\- Mapped `event_time` to `metadata.event_timestamp`.   
2024-10-08 |  Enhancement:  
\- Mapped `additional_information` to `additional.fields`.   
2024-09-05 |  Enhancement:  
\- Added support for SYSLOG + JSON logs.   
2024-09-04 |  Enhancement:  
\- Added support to parse KV data in `EventData` field.   
2024-08-26 |  Enhancement:  
\- Added support for a new pattern of KV logs.   
2024-07-23 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-18 |  Enhancement:  
\- Added support to parse key-value data in the `MESSAGE` field.   
2024-05-17 |  Enhancement:  
\- Added support to parse logs when `operationName` is `Microsoft Graph Activity`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `resourceId` to `target.resource.attribute.labels`.  
\- Mapped `operationName` to `metadata.product_event_type`.  
\- Mapped `operationVersion` to `additional.fields`.  
\- Mapped `properties.ipAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `properties.apiVersion` to `metadata.product_version`.  
\- Mapped `properties.appId` to `target.resource.product_object_id`.  
\- Mapped `properties.clientAuthMethod` to `extensions.auth.auth_details`.  
\- Mapped `properties.clientRequestId` to `additional.fields`.  
\- Mapped `properties.signInActivityId` to `network.session_id`.  
\- Mapped `properties.identityProvider` to `security_result.detection_fields`.  
\- Mapped `properties.wids` to `security_result.detection_fields`.  
\- Mapped `properties.roles` to `security_result.detection_fields`.  
\- Mapped `correlationId` to `security_result.detection_fields`.  
\- Mapped `properties.tokenIssuedAt` to `additional.fields`.  
\- Mapped `properties.requestMethod` to `network.http.method`.  
\- Mapped `properties.responseStatusCode` to `network.http.response_code`.  
\- Mapped `properties.tenantId` to `metadata.product_deployment_id`.  
\- Mapped `properties.userAgent` to `network.http.user_agent`.  
\- Mapped `properties.requestUri` to `target.url`.  
\- Mapped `properties.durationMs` to `network.session_duration.seconds`.  
\- Mapped `properties.responseSizeBytes` to `network.received_bytes`.  
\- Mapped `properties.userId` and `properties.servicePrincipalId` to `principal.user.userid`.  
\- Mapped `properties.location` to `principal.location.name`.  
\- Mapped `properties.requestId` to `metadata.product_log_id`.  
\- Mapped `properties.operationId` to `security_result.detection_fields`.   
2024-04-01 |  Enhancement:  
\- Added a Grok pattern to parse unparsed SYSLOG + JSON logs.  
\- Mapped `hostinfo.architecture` to `principal.asset.hardware`.  
\- Mapped `hostinfo.os.kernel` to `principal.platform_patch_level`.  
\- Mapped `hostinfo.os.version` to `principal.platform_version`.  
\- Mapped `hostinfo.os.platform` to `hostinfo.os.platform`.  
\- Mapped `hostinfo.os.name` and `hostinfo.os.build` to `additional.fields`.   
2023-12-20 |  Enhancement -  
\- Decoded the encoded log using gsub.  
\- Mapped `host.ip` to `principal.ip`.  
\- Added a Grok pattern to map additional fields.  
\- Mapped `error` to `security_result.detection_fields`.  
\- Mapped `err_msg` to `security_result.description`.   
2023-10-09 |  Enhancement -  
\- Added a Grok pattern to support the new log formats.  
\- Mapped `SQlINstance` to `principal.hostname` when user information is not available.   
2023-08-17 |  Enhancement -  
\- Provided a check that `event_type` is `STATUS_STARTUP` or `STATUS_SHUTDOWN` if the field `host` is not null.   
2023-07-04 |  Bug-Fix -  
\- Changed `event_type` from `USER_LOGIN` to `USER_UNCATEGORIZED` and from `STATUS_UNCATEFORIZED` to `GENERIC_EVENT` for some logs since fields like `clientip` or `host` are not present.  
\- Initialised `Date` and `Time` to null and provided null check before mapping.  
\- Mapped `AgentDevice`, `AgentLogFile`, `Source`, `ProcessInfo` to `additional.fields`.  
\- Mapped `SQlINstance` to `intermediary.hostname`.   
2023-05-09 |  Enhancement -  
\- Added JSON block to retrieve JSON data.  
\- Mapped `source` to `principal.resource.attribute.labels`.  
\- Mapped `msg` to `metadata.description`.   
2023-01-18 |  Enhancement - Added null conditional check for the following fields: `agent.type`, `agent.id`, `agent.hostname`, `agent.version`, `event.provider`, `event.code`, `log.level`, `ecs.version`, `timestamp`.  
\- Mapped the field `EventID` to `metadata.product_event_type`.  
\- Mapped the field `SourceModuleType` to `observer.application`.  
\- Mapped the field `SourceModuleName` to `additional.fields`.  
\- Mapped the field `Severity` to `security_result.severity`.  
\- Added following mapping when the event is `Audit Event`:  
\- Mapped the field `client_ip` to `principal.ip`.  
\- Mapped the field `database_name` to `target.resource_ancestors.name` and `target.resource_ancestors.resource_type` mapped as `DATABASE`.  
\- Mapped the field `schema_name` to `target.resource_ancestors.resource_subtype`.  
\- Mapped the field `statement` to `target.process.command_line`.  
\- Mapped the field `object_name` to `target.resource.name` and `target.resource.resource_type` mapped as `TABLE`.  
\- Mapped the field `application_name` to `target.application`.  
\- Mapped the field `sequence_number` to `target.resource.attribute.labels`.  
\- Mapped the field `transaction_id` to `target.resource.attribute.labels`.  
\- Added following mapping when the field `Message` contains `Log was backed up`:  
\- Mapped the field `Database` to `target.resource.name` and `target.resource.resource_type` as `DATABASE`.  
\- Mapped the field `first LSN` to `target.resource.attribute.labels`.  
\- Mapped the field `last LSN` to `target.resource.attribute.labels`.  
\- Mapped the field `UserID` to `principal.user.windows_sid`.  
\- Added following mapping when the field `Message` contains `Starting up database`:  
\- Mapped the field `Database` to `target.resource.name` and `target.resource.resource_type` as `DATABASE`.  
\- Mapped the field `AccountName` to `principal.user.userid`.  
\- Mapped the field `UserID` to `principal.user.windows_sid`.   
2022-08-09 |  Enhancement - Modified mapping for the field `winlog.computer_name` from `principal.asset.hostname` to `event.idm.read_only_udm.about.hostname` for logs with JSON format.   
2022-07-01 |  Bug-fix - Mapped `host.name` to `observer.hostname` for logs with JSON format.   
2022-05-31 |  Enhancement - Parsed the new JSON format logs and the logs containing the key-value fields. Also, parsed the syslog logs having `NXLOG`.  
Moved customer-specific version to default.  
Mapped the following new fields :  
For JSON format logs :  
winlog.computer_name, agent.type, agent.version, agent.id, agent.hostname, ecs.version, log.level, event.provider, event.code, host.name, logstash.process.host, message, timestamp.  
For key-value format logs :  
TextData, HostName, ApplicationName, LoginName, ObjectName, ObjectType, DatabaseID,DatabaseName, SPID, SourceModuleName, SourceModuleType.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
