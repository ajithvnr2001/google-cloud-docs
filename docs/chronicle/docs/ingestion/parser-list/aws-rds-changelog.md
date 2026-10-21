---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-rds-changelog/
title: Change log for AWS_RDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:12:04.899930+00:00
---

# Change log for AWS_RDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-rds-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_RDS

Date | Changes  
---|---  
2026-09-29 |  Enhancement :  
\- `event.idm.read_only_udm.principal.namespace`: Removed mapping of the log field originally named `prin_namespace` (which has been renamed now to `database_name` in the grok pattern) from the `event.idm.read_only_udm.principal.namespace` UDM field as it contains target resource data.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `database_name` log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `src_hostname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, when it contains valid source IP address.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `source_ip` log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Modified a grok pattern to parse the `source_ip`, `src_hostname`, and `database_name` log fields.  
\- Added support for the new format of `CSV` logs.   
2026-09-10 |  Enhancement :  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `audit_command`, `product_type`, `log_level` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `audit_class` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `statement` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `object_type`, `object_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `audit_type`, `statement_id`, `substatement_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `parameter` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `table_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped `product_type` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc`, `message_body` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `log_level`, `logevent.message` raw log fields with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `audit_command`, `statement`, or `message_body` is DROP (when principal user data is present and `database_name`, `table_name`, or `resource_name` is present), updated to `USER_RESOURCE_DELETION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `audit_command`, `statement`, or `message_body` is INSERT (when principal user data is present and `database_name`, `table_name`, or `resource_name` is present), updated to `USER_RESOURCE_CREATION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `audit_command`, `statement`, or `message_body` is SELECT (when principal user data is present and `database_name`, `table_name`, or `resource_name` is present), updated to `USER_RESOURCE_ACCESS`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `src_ip` and `tar_ip` are present, updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal user data is present, updated to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event_type` is empty (default fallback), updated to `GENERIC_EVENT`.   
2026-08-10 |  Enhancement :  
\- Added support for `UNIX_MS` format in `timestamp` parsing.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `app_id` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `src_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id2` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `prod_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `database_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ts`, `query`, `logGroup`, `logStream` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `exitCode` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine data and target machine data are present, set the event type to `NETWORK_CONNECTION`.   
2026-06-04 |  Enhancement :  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp`, `requestTime` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceIp`, `ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol_name` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `protocol_version` field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `topicName`, `routeKey`, `requestId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `clientId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `accountId` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principalId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `traceId` raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `httpMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field when `status` is integer.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field when `status` is string.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `logLevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped to `USER_UNCATEGORIZED` when principal user data is present, else if mapped to `STATUS_UPDATE` when principal data is present, else mapped to `GENERIC_EVENT`.   
2025-12-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `prin_namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `connection` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-09 |  Enhancement:  
\- `substatementId`: Converted `substatementId` to string before mapping to `event.idm.read_only_udm.additional.fields`UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `clientApplication` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `serverHost` raw log field from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields in order to introduce more accurate mappings for the raw log field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `serverHost` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `has_target`: Set `has_target` to `true` if `target.ip` and `target.asset.ip` is not empty.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `commandText` and `command` raw log fields from `event.idm.read_only_udm.additional.fields` UDM field. These changes were made to introduce more accurate mappings for the raw log fields.  
\- `event.idm.read_only_udm.target.process.command_line`: Mapped `commandText` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `objectType` and `objectName` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added support for new format of logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rowCount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `errorMessage` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `command` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `rawData`,`attemptsMade` and `attemptEndingTimestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `errorCode` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `errorMessage` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `lambdaARN` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `arrivalTimestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `exitCode` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-03-28 |  Enhancement:  
\- Added grok patterns inorder to parse the logs with new syslog format.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `prod_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `arn` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `PROTOCOL` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `address_data.HOST` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `address_data.HOST` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `PORT` to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `SID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `USER` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `connect_data.HOST` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `connect_data.HOST` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `PROGRAM` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action_details` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.   
2025-03-13 |  Enhancement:  
\- Added support for a new syslog log format.  
\- Added support to parse the new format of `timestamp`.   
2025-02-20 |  Enhancement:  
\- Added support for a new syslog log format.   
2025-02-18 |  Enhancement:  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `user_name` to `principal.user.user_display_name`.  
\- Mapped `database_name` to `target.resource.name` and set `target.resource.type` to `DATABASE`.  
\- Mapped `description` to `metadata.description`.   
2025-01-30 |  Enhancement:  
\- Added support for new syslog log format.   
2024-12-20 |  Enhancement:  
\- Added support for new log format.  
\- Mapped `owner` to `principal.user.userid`.  
\- Mapped `logGroup` to `security_result.about.resource.name`.  
\- Mapped `logStream` to `security_result.about.resource.attribute.labels`.  
\- Mapped `logevent.id` to `metadata.product_log_id`.  
\- Mapped `logevent.message` to `security_result.description`.  
\- Mapped `resource_name` to `target.resource.name`.  
\- Mapped `src_ip` to `principal.ip`.  
\- Mapped `tar_ip` to `target.ip`.  
\- Mapped `tar_host` to `target.hostname`.  
\- Mapped `subscriptionFilters` to `security_result.about.resource.attribute.labels`.   
2024-10-30 |  Enhancement:  
\- Added support for new log format.  
\- Mapped `type` to `additional.fields`.   
2024-10-03 |  Enhancement:  
\- Added support for new log format.   
2023-04-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
