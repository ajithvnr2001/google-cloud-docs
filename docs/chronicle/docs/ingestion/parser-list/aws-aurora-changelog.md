---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-aurora-changelog/
title: Change log for AWS_AURORA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:35.568036+00:00
---

# Change log for AWS_AURORA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-aurora-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_AURORA

Date | Changes  
---|---  
2026-04-17 |  Enhancement:  
\- Added support to parse raw log fields correctly for the new pattern of JSON format logs.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `target.@timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp_value` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `target.logGroup`, `target.logStream`, `target.messageType`, `target.owner` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added an IP check before already existing mapping of `prin_ip` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Modified the conditional logic before mapping `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_WRITTEN` and `GENERIC_EVENT`.   
2026-04-02 |  Enhancement:  
\- Added a Grok pattern to parse the SYSLOG format raw logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ms_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `csv_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `csv_userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `csv_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `csv_host` raw log field with `event.idm.read_only_udm.principal.ip` UDM fields.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `csv_connection_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `csv_query_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `csv_operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `csv_object` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `csv_retcode` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `thread_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `error_code` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `component` raw log field with `event.idm.read_only_udm.target.application` UDM field.   
2026-03-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auth_method` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_path` raw log field(s) with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `line` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_version` raw log field(s) with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_cipher` raw log field(s) with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `bits` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `sec_desc` raw log field(s) with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Changed the sequence of grok patterns and added conditional checks, allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.resource.name`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.target.resource.name`  
\- `event.idm.read_only_udm.target.user.userid`  
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `t_userid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `t_dbname` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `auth_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field. If `auth_user` is empty, `princ_userid` is used instead.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auth_method` (key: `method`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `unix_socket_path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `invalid_param` (key: `invalid_setting_name`) raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped from `platform_details` raw log field to `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `pr_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `platform_details` (key: `platform_details`), `compiler` (key: `compiler`), `architecture_bits` (key: `architecture_bits`) raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `network_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- Added new Grok patterns to the main filter to support additional SYSLOG log formats.  
\- Added a secondary Grok filter to parse fields from the `desc` field, extracting details such as file paths, IP addresses, authentication methods, and parameters.  
\- Added specific parsing logic for logs indicating PostgreSQL startup to extract version, platform, compiler, and architecture details.  
\- `event.idm.read_only_udm.network.session_id`: Added conditional check to ensure that the `event.idm.read_only_udm.network.session_id` UDM field is only mapped when the `connection_id_val` raw log field is not empty.  
\- `event.idm.read_only_udm.security_result.summary`: Added conditional check to ensure that the `event.idm.read_only_udm.security_result.summary` UDM field is only mapped when the `operation_val` UDM field is not empty.   
2026-02-03 |  Enhancement:  
\- Added conditional check for msg_prefix.  
\- query: If msg_prefix contains `AUDIT`, all commas (,) are temporarily replaced with `COMMASPLIT`. Otherwise, `, ` and `,` are replaced with ` `.  
\- message: Reconstructed using the modified query.  
\- `event.idm.read_only_udm.principal.process.command_line`: After being populated, any instances of `COMMASPLIT` are converted back to commas (,).   
2026-01-26 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.resource_type: If object_type is SCHEMA updated to DATABASE.  
\- The logic to parse select statements in the message field was updated from a simple gsub to a more robust grok pattern. This allows for correct parsing of complex select statements that contain multiple commas. The previous gsub logic is now used as a fallback.   
2025-12-12 |  Enhancement:  
\- Added data sanitization for the message field to handle a malformed raw log by removing an extra comma from a specific SQL query string.  
\- event.idm.read_only_udm.target.resource.resource_type: If object_type is TABLE CONSTRAINT,INDEX,TABLE COLUMN,VIEW,SEQUENCE updated to DATABASE.   
2025-10-24 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `table_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_type: Newly mapped `object_type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field.  
\- Renamed from column3 to ip_address_1.  
\- Renamed from column3 to ip_address_3.  
\- Renamed from column5 to ip_address_5.  
\- Added new grok patterns to parse additional log formats.  
\- Initialized a new internal field has_target_resource to `false`, which is set to `true` based on successful operations.  
\- event.idm.read_only_udm.metadata.event_type: If `op` is (SELECT|READ|QUERY) and has_target_resource is `true`, updated to RESOURCE_READ.  
\- event.idm.read_only_udm.metadata.event_type: If `cmd` is (SELECT|select) and has_target_resource is `true`, updated to RESOURCE_READ.  
\- event.idm.read_only_udm.metadata.event_type: Default value set to GENERIC_EVENT in the final else block.   
2025-09-26 |   
2024-01-12 |  Enhancement:  
\- Mapped `logEvents.messageType`, `logEvents.owner`, `logEvents.logGroup`, `logEvents.logStream` to `target.resource.attribute.labels`.  
\- Mapped `logEvents.logEvents.message`, `logEvents.logEvents.timestamp`, `logEvents.logEvents.id` to `securit_result.detection_fields`.  
\- Added a Grok pattern to retrieve the IP address from `logEvents.logEvents.message` and mapped `src_data` to `principal.ip`.  
\- Mapped `user` to `principal.user.userid`.   
2023-11-02 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
