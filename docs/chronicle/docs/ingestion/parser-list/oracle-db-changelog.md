---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-db-changelog/
title: Change log for ORACLE_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:19:18.032473+00:00
---

# Change log for ORACLE_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ORACLE_DB

Date | Changes  
---|---  
2026-09-25 |  \- Added Grok patterns to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for new timestamp format for `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `os_release` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `process_image` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `build_label`, `oracle_home`, `machine`, `redo_thread`, and `oracle_process_number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: If `system_name` is `linux`, updated the value of `event.idm.read_only_udm.principal.platform` to `LINUX`.   
2026-09-08 |  \- `event.idm.read_only_udm.additional.fields`: Removed mapping of `CURUSER` raw log field from `event.idm.read_only_udm.additional.fields` UDM field as it contains `target user` information.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `CURUSER` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `RETCODE` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field when `RETURNCODE` raw log field is empty.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `PDB_GUID` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `RETURNCODE` is `zero` updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`, else updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- Modified a Grok pattern to parse the raw log fields.  
\- Added a Grok pattern to parse the raw log fields.   
2026-06-08 |  \- `event.idm.read_only_udm.principal.process.command_line`: Removed mapping of `TERMINAL` from `event.idm.read_only_udm.principal.process.command_line` UDM field as it represents the application value.  
\- `event.idm.read_only_udm.principal.application`: Mapped `TERMINAL` raw log field with `event.idm.read_only_udm.principal.application` UDM field when `TERMINAL` is not "` and not `unknown".  
\- `event.idm.read_only_udm.target.application`: Removed mapping of `SRC_DATABASE` from `event.idm.read_only_udm.target.application` UDM field as it represents the resource name.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `SRC_DATABASE` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2026-05-22 |  Enhancement:  
\- Added grok pattern to parse `ip_address`, `ip_address_port`, `protocol`, `authenticated_identity`, and `auth_method` from `COMMENTTEXT` field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ip_address` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_address` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `ip_address_port` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `authenticated_identity` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auth_method` parsed from `COMMENTTEXT` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-08 |  \- Added a Grok pattern and a kv filter to parse the raw log fields.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `grantee` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field since `grantee` represents the user id of the target.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped if `has_target_user` is true and `GRANTEE` raw log field is not empty with `event.idm.read_only_udm.target.user.userid` UDM field else if `has_target_user` is true and `grantee` raw log field is mapped to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `EXTENDED_TIMESTAMP` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `USERNAME` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `SRC_DATABASE` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `DBID`, `OBJ_NAME` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `OS_USERNAME`, `OWNER`, `NEW_OWNER`, `NEW_NAME`, `OBJ_PRIVILEGE`, `ADMIN_OPTION`, `SES_ACTIONS`, `LOGOFF_TIME`, `LOGOFF_LREAD`, `LOGOFF_PREAD`, `LOGOFF_LWRITE`, `LOGOFF_DLOCK`, `ECONTEXT_ID`, `SESSION_CPU`, `PROXY_SESSIONID`, `GLOBAL_UID`, `SQL_BIND`, `SQL_TEXT`, `OBJ_EDITION_NAME` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `COMMENT_TEXT` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added a grok pattern on `COMMENT_TEXT` to extract `extracted_auth_type`, `comment_principal_ip`, `comment_principal_port`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `AUTHTYPE_UNSPECIFIED` with `event.idm.read_only_udm.extensions.auth.type` UDM field if `extracted_auth_type` raw log field value is `DATABASE`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `comment_principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `comment_principal_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `temp_ts` log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority` and `facility` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified gsub blocks to parse the JSON logs correctly.  
\- Added support for new pattern of JSON logs due to which the following fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.session_id`  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.user.attribute.permissions.name`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.target.user.user_display_name`  
2025-12-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Removed `action_name` field mapping from `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_det` field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- An intermediate field `action_det` is now conditionally populated with the value of the `ACTION` field.   
2025-12-08 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped os_process raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped sessionid raw log field with event.idm.read_only_udm.network.session_id UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped username raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped db_host raw log field with event.idm.read_only_udm.target.hostname UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped db_host raw log field with event.idm.read_only_udm.target.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped os_username raw log field with event.idm.read_only_udm.principal.user.user_display_name UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped rls_info, current_user, logoff_lread, obj_edition_name, logoff_lwrite, obj_privilege, logoff_pread, global_uid, session_cpu, ses_actions, logoff_time, logoff_dlock, extended_timestamp, audit_option, admin_option, owner, new_owner, new_name, sql_text, comment_text, timestamp raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped econtext_id, sql_bind, grantee, scn, instance_number, statementid raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped instance_name raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped action, proxy_sessionid, sys_privilege raw log field(s) with security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped terminal raw log field with event.idm.read_only_udm.principal.process.command_line UDM field.  
\- A new grok pattern was added to parse a new key-value log format.  
\- Added logic to set has_target_user to true based on the presence of t_hostname or client_id.  
\- Added logic to dynamically process and add a set of fields to event.idm.read_only_udm.additional.fields using a for-each loop construct.  
\- Added on_error for sys_privilege, priv_used, transactionid, scn, instance_number, statementid, userhost, obj_name, terminal, sessionid, client_id, rls_info, current_user, entryid, db_host, os_username, action, econtext_id, os_process, sql_bind, username, instance_name, proxy_sessionid, grantee, obj_edition_name, logoff_lread, logoff_lwrite, logoff_pread, global_uid, session_cpu, ses_actions, logoff_time, logoff_dlock, extended_timestamp, audit_option, admin_option, owner, new_owner, new_name, sql_text, comment_text, timestamp.  
\- Added conditional check for sys_privilege, priv_used, transactionid, scn, instance_number, statementid, userhost, obj_name, terminal, sessionid, client_id, rls_info, current_user, entryid, db_host, os_username, action, econtext_id, os_process, sql_bind, username, instance_name, proxy_sessionid, grantee.  
\- Updated conditional logic for the RETURNCODE field to include 0.0 in the success condition.   
2025-11-11 |  Enhancement:  
\- Added support for a new key-value format for logs starting with `SESSIONID:`, including pre-processing the raw log with gsub transformations before parsing with the kv filter.  
\- `event.idm.read_only_udm.principal.process.command_line`: Mapped `TERMINAL` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.   
2025-10-15 |  Enhancement:  
\- Added a new grok pattern to support a new syslog format from Oracle Unified Audit.  
\- Enhanced the date filter to support the additional timestamp format.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.   
2025-08-20 |  Enhancement:  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped ingestionTime raw log field with event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped Extended_Timestamp raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped log_type raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped Audit_Type, DB_User, EntryId, eventId, Ext_Name, logStreamName, OSPrivilege, Sql_Text, StatementId raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped Current_User raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped Userhost raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped Userhost raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped Userhost raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped Userhost raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped OS_Process raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped Terminal raw log field with event.idm.read_only_udm.principal.process.command_line UDM field.  
\- event.idm.read_only_udm.src.user.userid: Newly mapped OS_User raw log field with event.idm.read_only_udm.src.user.userid UDM field.  
\- event.idm.read_only_udm.target.cloud.project.id: Newly mapped aws_account_id raw log field with event.idm.read_only_udm.target.cloud.project.id UDM field.  
\- event.idm.read_only_udm.target.cloud.availability_zone: Newly mapped aws_region raw log field with event.idm.read_only_udm.target.cloud.availability_zone UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped log_group_name raw log field with event.idm.read_only_udm.target.resource.name UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped arn_log_group, Instance_Number raw log field(s) with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped Returncode raw log field with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped Session_Id raw log field with event.idm.read_only_udm.network.session_id UDM field.   
2025-08-12 |  Enhancement:  
\- Added a grok pattern to parse `inter_ip` and `inter_port`.  
\- Added a conditional check for `kv_data2`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `inter_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `HOST_ID` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `SYS_PRIVILEGE` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `PRIV_USED` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `OS_PROCESS` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `TRANSACTIONID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SCN` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `INSTANCE_NUMBER` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `ENTRY_ID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `STATEMENTID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2025-05-20 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary_hostname` : Newly mapped `intermediary_hostname` raw log field with `event.idm.read_only_udm.intermediary_hostname` UDM field.  
\- Added a new grok pattern in order to parse the logs with `intermediary_hostname` raw log field.   
2025-03-18 |  Enhancement:  
\- Added Grok pattern to parse SYSLOG logs.  
\- Mapped `org_id` and `comp_id` to `additional.fields`.  
\- Mapped `host_addr` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `host_id` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `level` to `security_result.severity_details`.   
2025-02-12 |  Enhancement:  
\- Added date filter to support new pattern of syslog logs.   
2025-01-15 |  Enhancement:  
\- Mapped `ID` to `metadata.event_timestamp`.   
2024-12-19 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2024-12-12 |  Enhancement:  
\- Added `gsub` pattern to handle new format of KV logs.  
\- Added a new Grok pattern to handle new format of KV logs.  
\- Mapped `ORACLE_DB` to `metadata.log_type`.   
2024-10-25 |  Enhancement:  
\- If `ACTION` is `GRANT`, then set `metadata.event_type` to `USER_RESOURCE_UPDATE_PERMISSIONS`.  
\- If `ACTION` is `DROP` or `DELETE`, then set `metadata.event_type` to `USER_RESOURCE_DELETION`.  
\- If `ACTION` is `CREATE`, then set `metadata.event_type` to `USER_RESOURCE_CREATION`.  
\- If `ACTION` is `ALTER` or `INSERT`, then set `metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT`.   
2024-09-25 |  Enhancement:  
\- Added support for new pattern of KV logs.   
2024-07-24 |  Enhancement:  
\- Mapped `AUDIT_POLICY` as a single string to `additional.fields` instead of splitting it into multiple values.   
2024-06-06 |  \- Minor change in `principal.user.user_display_name`.   
2024-05-30 |  \- Added support for exadata fields.   
2024-04-03 |  \- Added support for some attributes which were not covered.   
2023-10-25 |  Enhancement:  
\- Mapped `LENGTH`, `LOGOFFDEAD`, `LOGOFFLREAD`, `LOGOFFLWRITE`, `LOGOFFPREAD`, `SESSIONCPU`, `CLIENT_TERMINAL` to `target.resource.attribute.labels`.  
\- Mapped `ACTION` to `security_result.summary`.  
\- Set `security_result.description` to `Success` when `RETURNCODE` is 0 or `STATUS` is 0.  
\- Set `security_result.description` to `Failure` when `RETURNCODE` is either 1 or -1, or `STATUS` is either 1 or -1.  
\- Mapped `principal.ip` and `principal.port` from `CLIENT_ADDRESS`.   
2022-10-13 |  Enhancement:  
\- Added grok pattern to handle SYSLOG and KV logs.   
2022-08-01 |  Enhancement: Added mapping for following fields:  
\- `hostname` mapped to `principal.hostname`.  
\- if `returncode` is `0` then security_result.action mapped to `ALLOW` else if it is `-1` then mapped to `BLOCK`  
\- `ACTION` mapped to `metadata.product_event_type`.  
\- `DATABASE USER` mapped to `principal.user.user_display_name`.  
\- `PRIVILEGE` mapped to `principal.user.attribute.permissions`.  
\- `CLIENT USER` mapped to `target.user.user_display_name`.  
\- `file_name` mapped to `target.file.full_path`.  
\- `event_name` mapped to `metadata.product_event_type`.  
\- `ACTION_NUMBER` mapped to `event.idm.read_only_udm.additional.fields`.  
\- `length` mapped to `event.idm.read_only_udm.additional.fields`.  
\- `DBID` mapped to `metadata.product_log_id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
