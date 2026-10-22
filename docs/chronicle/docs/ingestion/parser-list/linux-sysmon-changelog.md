---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-sysmon-changelog/
title: Change log for LINUX_SYSMON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:42.964644+00:00
---

# Change log for LINUX_SYSMON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/linux-sysmon-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LINUX_SYSMON

Date | Changes  
---|---  
2026-02-18 |  Enhancement:  
\- Added a conditional check before already existing mapping of `SourceProcessGUID` to `event.idm.read_only_udm.principal.process.product_specific_process_id`.  
\- Added a conditional check before already existing mapping of `TargetProcessGUID` to `event.idm.read_only_udm.target.process.product_specific_process_id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `SourceThreadId` (key: `source_thread_id`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `SourceUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `TargetUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `SecurityUserId` (key: `security_user_id`), `Opcode` (key: `opcode`) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Due to the changes mentioned above, some failing logs are fixed and the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.intermediary[].hostname`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.direction`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip[]`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip[]`  
\- `event.idm.read_only_udm.principal.network.session_id`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.process.command_line`  
\- `event.idm.read_only_udm.principal.process.file.full_path`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.security_result[].action[]`  
\- `event.idm.read_only_udm.security_result[].rule_name`  
\- `event.idm.read_only_udm.security_result[].severity`  
\- `event.idm.read_only_udm.target.asset.ip[]`  
\- `event.idm.read_only_udm.target.file.full_path`  
\- `event.idm.read_only_udm.target.ip[]`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.process.command_line`  
\- `event.idm.read_only_udm.target.process.file.full_path`  
\- `event.idm.read_only_udm.target.process.file.sha256`  
\- `event.idm.read_only_udm.target.process.pid`  
\- `event.idm.read_only_udm.target.resource.attribute.labels[].key`  
\- `event.idm.read_only_udm.target.resource.attribute.labels[].value`  
\- `event.idm.read_only_udm.target.resource.name`  
\- `event.idm.read_only_udm.target.resource.resource_subtype`  
2025-09-25 |  Enhancement:  
\- Added a grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `component`, `source_file` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description: Newly mapped `desc` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2025-07-29 |  Enhancement:  
\- Modified the grok pattern to fetch timestamp and Added date filter to support new format of timestamps.  
\- Added a Grok pattern to support new pattern of logs.  
\- Modified else condition to filter null values in `Category` raw log field.  
\- Added KV filter to support new format of logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logname`,`tty`,`uid`,`euid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `user` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `summary` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.   
2025-07-02 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `Computer` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Channel`, `ThreadID`, `SystemTime`, `Keywords`, `Task`, `Version`, `ProviderGuid`, `SourceName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-10-22 |  Enhancement:  
\- Added support for the new pattern of syslog logs.   
2024-06-17 |  Enhancement:  
\- Added support for the new pattern of JSON logs.   
2024-01-25 |  Enhancement :  
\- Removed extra escape characters from the `message` to avoid `xml` filter failure.  
\- Changed mapping for `UserID` from `principal.user.windows_sid` to `principal.user.userid`.   
2023-11-09 |  Enhancement :  
\- Mapped `User` to `target.user.userid`.  
\- Mapped `ParentUser` to `principal.user.userid`.  
\- Mapped `ProcessId` to `target.process.pid`.  
\- Mapped `FileVersion` to `principal.software.version`.  
\- Mapped `Product` to `principal.software.name`.  
\- Mapped `Company` to `principal.software.vendor_name`.  
\- Mapped `LogonId` to `principal.network.session_id`.  
\- Mapped `OriginalFileName`, `CurrentDirectory`, `LogonGuid`, `TerminalSessionId`, `IntegrityLevel` to `additional.fields`.   
2022-07-12 |  Enhancement :  
\- Added null check to EventID field prior mapping.  
\- Mapped insertId to metadata.product_log_id.  
\- Mapped logName to target_process_file.  
\- Mapped resource.type to target.resource.type.  
\- Mapped resource.labels.project_id to target.resource.product_object_id.  
\- Mapped resource.labels.instance_id to target.resource.id.  
\- Mapped refer_url to network.http.referral_url.   
2022-05-10 |  Initial creation of the LINUX_SYSMON Chronicle parser, based upon WINDOWS_SYSMON  
\- Supports events IDs 1, 3, 5, 9, 11, 16, 23.  
\- Uses the Chronicle Forwarder Regex Filter capabilities with an allow filter of `sysmon` to exclude syslog logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
