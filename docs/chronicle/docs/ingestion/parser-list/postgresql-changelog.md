---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postgresql-changelog/
title: Change log for POSTGRESQL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:41.645040+00:00
---

# Change log for POSTGRESQL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postgresql-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for POSTGRESQL

Date | Changes  
---|---  
2026-02-18 |  Enhancement:  
\- Three new grok patterns were added to support additional SYSLOG log formats, enabling the extraction of `remote_port` and `error_severity` as new raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added `yyyy-MM-dd HH:mm:ss` to the supported timestamp formats for the `ts` raw log field.  
\- 'event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_path` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `error_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field. If `error_severity` is `LOG`, `event.idm.read_only_udm.security_result.severity` is mapped to `INFORMATIONAL`, and if `error_severity` is `FATAL`, `event.idm.read_only_udm.security_result.severity` is mapped to `ERROR`.   
2025-12-02 |  Enhancement:  
\- Added grok patterns to parse SYSLOG+KV log formats.  
\- event.idm.read_only_udm.extensions.auth.type: Set auth type to `MACHINE` when `db_user` is present in log.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `db_user` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `db_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_address`, `ip_host` raw log fields to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip_address`, `ip_host` raw log fields to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `client_host`, `host` raw log fields to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `client_host`, `host` raw log fields to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `connection_type` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `process_pid` raw log field to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `session_time`, `database`, and `duration` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-09-19 |  Enhancement:  
\- Added a grok pattern to parse the `resourceId` field to extract cloud project and resource information.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `properties.DatabaseName` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `properties.Schemaname`, `resourcegroups` (extracted from resourceId), `providers` (extracted from resourceId), `flexibleservers` (extracted from resourceId), `subscriptions` (extracted from resourceId) raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.Tables_counter`, `properties.Tables_vacuumed`, `properties.N_live_tup`, `properties.Tables_autovacuumed`, `properties.Tables_analyzed`, `properties.Tables_autoanalyzed`, `properties.N_dead_tup`, `properties.Seq_scan`, `properties.Seq_tup_read`, `properties.Idx_scan`, `properties.Idx_tup_fetch`, `properties.N_tup_ins`, `properties.N_tup_upd`, `properties.N_tup_del`, `properties.N_tup_hot_upd`, `properties.N_mod_since_analyze`, `properties.Vacuum_count`, `properties.Autovacuum_count`, `properties.Analyze_count`, `properties.Autoanalyze_count`, `loggingSourceName` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field when the `Timestamp` field is not available.   
2025-06-05 |  Enhancement:  
\- Added gsub to to modify `message` in the raw log to `msg`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `backend_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `remote_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `remote_host` raw log field with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM fields when `remote_host` is a valid IP.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `remote_host` raw log field with `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `remote_host` is not a valid IP.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `application_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `error_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.target.resource.parent: Newly mapped `dbname` raw log field with `event.idm.read_only_udm.target.resource.parent` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `detail_ip` raw log field with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `query_id`, `txid`, `vxid`, `state_code`, `detail` and `line_num` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timeStamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `ps` is `authentication` or `message` contains `LOGON`.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_CREATION` when `msg` contains `CREATE USER`, `CREATE TABLE`, `CREATE DATABASE` or `CREATE OBJECT`, `has_target_resource`, `has_principal` and `has_user` are true.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_DELETION` when `msg` contains `Delete` or `Drop`, `has_target_resource`, `has_principal` and `has_user` are true.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_PERMISSIONS` when `msg` contains `Grant`, `has_target_resource`, `has_principal` and `has_user` are true.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_UPDATE_CONTENT` when `msg` contains `Alter`, `has_target_resource`, `has_principal` and `has_user` are true.   
2024-08-07 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
