---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-hana-audit-changelog/
title: Change log for SAP_HANA_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:26.840949+00:00
---

# Change log for SAP_HANA_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-hana-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_HANA_AUDIT

Date | Changes  
---|---  
2026-04-17 |  Enhancement:  
\- Added support for new format of `SYSLOG`, `SYSLOG+KV` logs.  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cnt`, `free`, `rem`, `rem3`, `jds_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `thread`, `content_repository`, `source_location` log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `summary` log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_details` log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `doc_id` log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sent_bytes` log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_protocol_src` log field with `event.idm.read_only_udm.network.application_protocol` UDM field.   
2026-03-30 |  Enhancement:  
\- Added a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.target.resource.attribute.roles`: Newly mapped `RoleName` raw log field with `event.idm.read_only_udm.target.resource.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Comment` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.src.resource.name`: Newly mapped `OriginDatabaseName` raw log field with `event.idm.read_only_udm.src.resource.name` UDM field.  
\- `event.idm.read_only_udm.src.user.userid`: Newly mapped `OriginUserName` raw log field with `event.idm.read_only_udm.src.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `XsaUuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `PrivilegeName`, `Grantable` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `GranteeSchemaName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RoleSchemaName`, `CreateTime`, `XsaMessageIp`, `XsaTenant`, `XsaChannel`, `XsaAttachmentId`, `XsaAttachmentName`, `XsaOrganizationId`, `XsaSpaceId`, `XsaInstanceId`, `XsaBindingId`, `XsaObject`, `XsaDataSubject` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `principal_hostname` raw log field(s) with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `prin_user` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `USER` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `principal_application` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `PWD` raw log field(s) with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `COMMAND` raw log field(s) with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `AuditLevel` raw log field(s) with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- Added grok patterns to parse the new format json logs and csv logs.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `component`, `parameter`, `old_value`, `new_value`, `section` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `ActionStatus` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.   
2026-02-18 |  Newly created parser:  
\- Added support to parse CSV, JSON+CSV format of logs.  
\- Added a grok pattern on `_raw` field to extract header information.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` field with `event.idm.read_only_udm.metadata.description` UDM field if `msg` does not contain csv format value.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `syslog_host` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `process_name` raw log field(s) with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `pid` raw log field(s) with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time`, `EventTimestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_time` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.observer.file.full_path`: Newly mapped `source` raw log field(s) with `event.idm.read_only_udm.observer.file.full_path` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`,`event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `host` raw log field(s) with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `ServiceName` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Hostname` raw log field(s) with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `PortNumber` raw log field(s) with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ClientIpAddress` raw log field(s) with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `ClientName` raw log field(s) with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ClientProcessId` raw log field(s) with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `ClientPortNumber` raw log field(s) with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `AuditAction` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `SessionUser` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `TargetUser` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SessionId` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `DatabaseName` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `ApplicationUserName` raw log field(s) with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `ApplicationName` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `clz_dir`, `clz_subdir`, `clzfilename` raw log field(s) with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `system_id`, `InstanceNumber`, `TargetSchema`, `TargetObject` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ExecutedStatement`, `XsApplicationUserName`, `StatementUserName`, `appname`, `facility`, `hostname`, `priority`, `proc_id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `SAP` raw log field(s) with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `SAP_HANA_AUDIT` raw log field(s) with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: The event_type is updated to `USER_RESOURCE_ACCESS`, `NETWORK_CONNECTION`, `USER_UNCATEGORIZED`, or `STATUS_UPDATE` based on the presence of necessary principal and target data, defaulting to GENERIC_EVENT if those details are missing.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
