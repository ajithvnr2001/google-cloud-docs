---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/halcyon-changelog/
title: Change log for HALCYON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:04.794941+00:00
---

# Change log for HALCYON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/halcyon-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HALCYON

Date | Changes  
---|---  
2026-02-18 |  Enhancement:  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `timeElapsed`, `threshold` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
-`event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
-`event.idm.read_only_udm.target.file.mime_type`: Newly mapped `summary.artifact.kind` raw log field to `event.idm.read_only_udm.target.file.mime_type` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `process.artifact.sha256`, `process.artifact.filePath`, `process.artifact.kind` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `process.modules.sha256`, `process.modules.filePath`, `process.modules.kind` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.about.file.mime_type`: Newly mapped `module.kind` raw log field to `event.idm.read_only_udm.about.file.mime_type` UDM field.  
\- The following UDM fields are now being mapped correctly:  
-`event.idm.read_only_udm.principal.process.command_line`  
-`event.idm.read_only_udm.principal.process.parent_pid`  
-`event.idm.read_only_udm.principal.process.pid`  
2025-09-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `firstOccurredAt` from `event.idm.read_only_udm.metadata.event_timestamp` when `dataType` is `Alert` to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.process.file.first_seen_time: Mapped `firstOccurredAt` raw log field to `event.idm.read_only_udm.principal.process.file.first_seen_time` when `dataType` is `Alert` to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.process.file.last_seen_time: Removed mapping of `lastOccurredAt` from `event.idm.read_only_udm.principal.process.file.last_seen_time` when `dataType` is `Alert` to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped `lastOccurredAt` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` when `dataType` is `Alert` to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.about.file.sha256: Newly mapped `primaryProcess.modules.sha256` raw log field to `event.idm.read_only_udm.about.file.sha256` UDM field.  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `primaryProcess.modules.filePath` raw log field to `event.idm.read_only_udm.about.file.full_path` UDM field.   
2025-09-11 |  Enhancement:  
\- Added support for array of `JSON` format.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `process.artifact.filePath`, `process.artifact.kind`, `process.artifact.sha256`, `record.count`, `record.dataType`, `record.policyMode`, `record.totalOccurrences` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.occurredAt` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record.kind` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.gupid` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `record.asset.id` raw log field to `event.idm.read_only_udm.principal.asset.asset_id`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `record.asset.name` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `record.asset.name` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `record.artifact.filePath` raw log field to `event.idm.read_only_udm.principal.process.file.full_path`.  
\- event.idm.read_only_udm.principal.process.file.last_seen_time: Newly mapped `record.lastOccurredAt` raw log field to `event.idm.read_only_udm.principal.process.file.last_seen_time`.  
\- event.idm.read_only_udm.principal.process.file.mime_type: Newly mapped `record.artifact.kind` raw log field to `event.idm.read_only_udm.principal.process.file.mime_type`.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `record.artifact.sha256` raw log field to `event.idm.read_only_udm.principal.process.file.sha256`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `process.commandLine`, `process.parentPid`, `process.pid`, `record.tenantId` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.target.asset_id: Newly mapped `record.id` raw log field to `event.idm.read_only_udm.target.asset_id`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `record.summary.artifact.filePath` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `record.summary.artifact.sha256` raw log field to `event.idm.read_only_udm.target.file.sha256`.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `record.primaryProcess.commandLine` raw log field to `event.idm.read_only_udm.target.process.command_line`.  
\- event.idm.read_only_udm.target.process.file.mime_type: Newly mapped `record.primaryProcess.artifact.kind` raw log field to `event.idm.read_only_udm.target.process.file.mime_type`.  
\- event.idm.read_only_udm.target.process.parent_process.pid: Newly mapped `record.primaryProcess.parentPid` raw log field to `event.idm.read_only_udm.target.process.parent_process.pid`.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `record.primaryProcess.pid` raw log field to `event.idm.read_only_udm.target.process.pid`.   
2025-07-31 |  Enhancement:  
\- event.idm.read_only_udm.target.process.file.mime_type: Newly mapped `primaryProcess.kind` raw log field with `event.idm.read_only_udm.target.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.process.file.mime_type: Newly mapped `primaryProcess.artifact.kind` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `processes.artifact.filePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `processes.artifact.sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `action` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `filterName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `policyMode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `euid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `occurrences.AuthFailure` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `occurrences.FailedPassword` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `occurredAt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `occurrences.IncorrectPasswords` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `guid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `gupid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `count` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `artifact.filePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `artifact.sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.process.file.mime_type: Newly mapped `artifact.kind` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `monitoringReason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `dxpRule` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `modifiedFilePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.rule_version: Newly mapped `ipArtifact.version` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ipArtifact.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ipArtifact.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_pid: Newly mapped `process.parentPid` raw log field with `event.idm.read_only_udm.principal.process.parent_pid` UDM field.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `dxpRuleType` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `summary.applicationName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process.pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `reason.exitCode` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `reason.cause` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.network.dns.questions: Newly mapped `dnsArtifact_uri` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `uid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tty` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sshd` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `phost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user_displayname` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-04-09 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `dataType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `totalOccurrences` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.file.mime_type: Newly mapped `process.artifact.kind` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `process.artifact.sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `process.artifact.filePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `process.commandLine` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `firstOccurredAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.process.file.last_seen_time: Newly mapped `lastOccurredAt` raw log field with `event.idm.read_only_udm.principal.process.file.last_seen_time` UDM field.  
\- event.idm.read_only_udm.target.asset_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.target.asset_id` UDM field.   
2024-10-17 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
