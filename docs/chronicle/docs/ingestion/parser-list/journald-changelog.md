---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/journald-changelog/
title: Change log for JOURNALD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T02:41:42.347501+00:00
---

# Change log for JOURNALD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/journald-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JOURNALD

Date | Changes  
---|---  
2026-09-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `resource.type` raw log field from `event.idm.read_only_udm.target.resource.type` UDM field since the UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_type`, `event.idm.read_only_udm.target.resource.resource_subtype`: Mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when `resource.type` has a valid enum `resource_type` value, otherwise mapped with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `jsonPayload.JOB_RESULT`, `jsonPayload.JOB_TYPE`, `jsonPayload.USER_INVOCATION_ID`, `jsonPayload.USER_UNIT` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.user.userid`: Newly mapped `jsonPayload._AUDIT_LOGINUID` raw log field with `event.idm.read_only_udm.about.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `jsonPayload._AUDIT_SESSION` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `jsonPayload._STREAM_ID`, `jsonPayload._SYSTEMD_INVOCATION_ID`, `jsonPayload._SYSTEMD_USER_SLICE` raw log fields with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `jsonPayload._SYSTEMD_OWNER_UID`, `jsonPayload._SYSTEMD_USER_UNIT`, `sourceLocation.file`, `sourceLocation.function`, `sourceLocation.line` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `labels.compute.googleapis.com/resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.labels.instance_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone`: Newly mapped `resource.labels.zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2025-10-03 |  Enhancement:  
\- event.idm.read_only_udm.metadata.description: Newly mapped `MESSAGE` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `message_id` field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- event.idm.read_only_udm.src.user.user_display_name: Newly mapped `from` raw log field with `event.idm.read_only_udm.src.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.src.user.userid: Newly mapped `uid` raw log field with `event.idm.read_only_udm.src.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `_HOSTNAME` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `_UID` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `_GID`, `_SYSTEMD_UNIT` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `_PID` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `SYSLOG_PID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `_EXE` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped `_COMM` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `_CMDLINE` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `PRIORITY` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `SYSLOG_FACILITY`, `SYSLOG_IDENTIFIER`, `_SYSTEMD_CGROUP`, `_CAP_EFFECTIVE`, `_TRANSPORT` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `_BOOT_ID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_MACHINE_ID`, `_SYSTEMD_SLICE`, `__CURSOR`, `__MONOTONIC_TIMESTAMP`, `CODE_FUNCTION`, `CODE_LINE`, `RESULT` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.src.file.full_path: Newly mapped `CODE_FILE` raw log field with `event.idm.read_only_udm.src.file.full_path` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `MESSAGE_ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `UNIT` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2024-11-27 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
