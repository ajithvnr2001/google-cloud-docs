---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mysql-changelog/
title: Change log for MYSQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:20:57.636073+00:00
---

# Change log for MYSQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mysql-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MYSQL

Date | Changes  
---|---  
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `wp_ua` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `wp_username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `wp_fa_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `wp_action` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `login_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `time_login`, `time_last_seen`, `hit_id`, `ctime`, `fail`, `history_id`, `key` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `IP` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-05-05 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `properties.event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `properties.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `properties.error_code` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.event_subclass` and `properties.is_aad_auth` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when user data is present.   
2026-04-20 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `properties.host` to extract `user_id`, `p_host`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `category` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `ServerType` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `properties.start_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `properties.server_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `properties.thread_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `properties.db` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `operationName` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `location` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.host`, `properties.last_insert_id`, `properties.insert_id`, `properties.sql_text`, `properties.rows_examined`, `properties.rows_sent`, `properties.lock_time`, `properties.query_time`, `properties.replication_set_role` and `properties.event_class` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-08 |  Enhancement:  
\- Added a Grok pattern to parse new format of SYSLOG logs.  
\- Renamed the field name from `csv_target_hostname` to `csv_principal_hostname` for better naming convention.  
\- Added support for field `timestamp` to parse new format of timestamps.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `csv_target_hostname` log field from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields as it is an IP address not a hostname.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `csv_principal_hostname` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `csv_hostname` log field from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields as this log field value represents hostname value not an IP address.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `csv_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `csv_principal_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ts`, `csv_query_id`, `csv_mysql` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `account_host`, `login_proxy`, `login_os`, `arg` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `startup_data_server_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `startup_data_os_version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `startup_data_mysql_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `arg` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `csv_mysql_sql_query` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-04-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed the mapping of `hostname` from the `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields; since this is a header hostname, it should be in the intermediary.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `id`, `login.proxy`, `connection_data.connection_type` and `connection_data.status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `login.os` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `account.host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `connection_data.db` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` with `USER_UNCATEGORIZED` when log has user data.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added new grok patterns to parse the raw log fields.   
2026-03-31 |  Enhancement:  
\- Added a grok pattern on `inner_message` to parse new format of syslogs.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `mysql_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `mysql_errno` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `mysql_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `mysql_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `error_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `mysql_thread_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `mysql_socket`, `log_level` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-23 |  Enhancement:  
\- Replaced `has_principal` from merge condition to replace condition, to correctly parse the event_type.   
2026-02-19 |  \- Added the Grok patterns to parse the unparsed csv and syslog logs  
`event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `mysql_timestamp`, `event_date`, `event_time`, `csv_timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
`event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `mysql_action`, `log_category`, `csv_mysql_action`, `csv_mysql_connection_type` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
`event.idm.read_only_udm.metadata.description`: Newly mapped `event_message`, `resolution_error` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
`event.idm.read_only_udm.principal.application`: Newly mapped `component` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
`event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `mysql_hostname` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
`event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `csv_hostname_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
`event.idm.read_only_udm.principal.user.userid`: Newly mapped `mysql_username`, `csv_username` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
`event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `csv_target_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
`event.idm.read_only_udm.target.resource.name`: Newly mapped `csv_database_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
`event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `mysql_sql_query`, `csv_mysql_sql_query` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
`event.idm.read_only_udm.network.session_id`: Newly mapped `mysql_thread_id`, `csv_connection_id` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
`event.idm.read_only_udm.security_result.rule_id`: Newly mapped `mysql_message_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
`event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_mysql_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `csv_mysql_connection_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-04 |  \- event.idm.read_only_udm.principal.ip: Newly mapped `login.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `login.ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `login.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `account.user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `connection_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `general_data.command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `general_data.query` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `connection_data.connection_type` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `general_data.sql_command`, `event_data`, `general_data.status`, `class`, `Status` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped a static `MACHINE` value with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- If connection_type contains tcp/ip, event.idm.read_only_udm.network.ip_protocol is set to TCP.   
2025-04-03 |  \- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `sql_query`, `value`, `num`, `ns`, `itemid`, `value_min`, `value_avg`, `value_max` and `query_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `clock` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field  
\- Added a Grok pattern to parse the unparsed logs.   
2024-07-05 |  Enhancement:  
\- Added the Grok patterns to parse the unparsed logs.  
\- Mapped `inner_message` to `security_result.description`  
\- Mapped `summary` to `security_result.summary`  
\- Mapped `path` to `principal.file.full_path`  
\- Mapped `logtype` to `metadata.product_event_type`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
