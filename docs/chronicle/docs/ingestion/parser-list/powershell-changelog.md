---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/powershell-changelog/
title: Change log for POWERSHELL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:44:14.178379+00:00
---

# Change log for POWERSHELL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/powershell-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for POWERSHELL

Date | Changes  
---|---  
2026-09-07 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `winlog.version`, `winlog.user.type`, `winlog.event_data.MessageNumber`, `winlog.event_data.MessageTotal`, and `winlog.event_data.ScriptBlockId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event.original` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `winlog.event_data.ScriptBlockText` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `winlog.event_data.Path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.   
2026-08-04 |  Enhancement:  
\- Added a grok pattern on `binding.ipAddress` to extract valid `ip_address`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `event.provider` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `agent.type` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `agent.id` raw log field with `event.idm.read_only_udm.observer.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `agent.name` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `@metadata.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `event.created` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `agent.ephemeral_id` , `agent.version` , `ecs.version` , `@metadata.beat` , `@metadata.type` , `event.kind` , `tags` , `winlog.keywords` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `log.level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `binding.protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `binding.sniFlag` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-03 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `princ_host` raw log field to event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `princ_host` raw log field to event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ingestiontag`, `originator_id` and `servicetag` raw log field to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `providername` raw log field to event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userid` raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `eventrecordid` raw log field to event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `eventid` raw log field to event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `command_details` raw log field to event.idm.read_only_udm.target.process.command_line UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `application` raw log field to event.idm.read_only_udm.target.application UDM field.   
2025-11-19 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `syslog_host`, `Computer` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Task`, `OpcodeValue`, `ThreadID` and `AccountType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- If `syslog_host` contains an IP address, it is mapped to `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`. Otherwise, it is mapped to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- If `syslog_host` is present, `Hostname` is mapped to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`.  
\- If `syslog_host` is not present, `Hostname` is mapped to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`.   
2025-09-05 |  Enhancement:  
\- event.idm.read_only_udm.principal.application: Newly mapped `Nombre_de_host` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `Version_de_host` raw log field to `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `Id_de_host` raw log field to `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `Application_host` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `Nombre_de_comando` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `Usuario` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `admin_domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Version_del_motor`, `Id_de_espace_de_ejecucion`, `Id_de_canalizacion` ,`Tipo_de_comando` `Numero_de_secuencia` and `Id_de_shell` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Refactored parser logic to handle Spanish field names in ContextInfo by adding gsub mutations before KV extraction.  
\- Added regex validation (=~ `^S-\\\\d-(\\\\d+-){1,14}\\\\d+$`) to ensure only valid windows SIDs are mapped to `event.idm.read_only_udm.principal.user.windows_sid`.  
\- Added a non-empty check for HostID before mapping to `event.idm.read_only_udm.target.asset.asset_id` UDM field.   
2025-05-13 |  Enhancement:  
\- Added Gsub to remove `\\n`.   
2025-04-22 |  Enhancement:  
\- Added a `gsub` function to handle the new format of JSON logs.  
\- Added a null condition check for `opcode` raw log field before mapping `event1.idm.read_only_udm.metadata.description` UDM field.  
\- Added a condition check for `System.ProcessID` raw log field before mapping `event1.idm.read_only_udm.principal.process.pid` UDM field.  
\- Added a condition check for `System.ThreadID` raw log field before mapping `event1.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-04-15 |  Enhancement:  
\- event1.idm.read_only_udm.additional.fields : Newly Mapped `Offset` raw log field with `event1.idm.read_only_udm.additional.fields` UDM Field.  
\- event1.idm.read_only_udm.additional.fields : Newly Mapped `SeverityValue` raw log field with `event1.idm.read_only_udm.additional.fields` UDM Field.  
\- Added convert for `host_application_not_found` to handle for unparsed of JSON logs.   
2025-03-20 |  Enhancement:  
\- Mapped `Hostname` to `intermediary.hostname` and `intermediary.asset.hostname`.  
\- Added support to parse the unparsed logs.  
\- Mapped `Keywords`, `EventType`, `Channel`, `Opcode` and `Sequence Number` to security_result.detection_fields.  
\- Mapped `NewEngineState`, `PreviousEngineState`, `HostVersion`, `RunspaceId`, `SequenceNumber`, `EngineVersion` and `PipelineId` to `additional.fields`.  
\- Mapped `HostApplication` to `principal.application`.  
\- Mapped `HostName` to `target.hostname` and `target.asset.hostname`  
\- Mapped `HostId` to `target.asset.asset_id`.  
\- Mapped `HostApplication` to `principal.process.command_line`.   
2025-03-05 |  Enhancement:  
\- Added support for new format of XML logs.   
2025-01-29 |  Enhancement:  
\- Changed mapping for `ScriptBlockText` from `security_result.detection_fields` to `target.process.command_line`.   
2025-01-28 |  Enhancement:  
\- Added `gsub` to support new format of JSON logs.   
2025-01-09 |  Enhancement:  
\- Mapped `Payload` to `security_result.detection_fields`.  
\- Mapped `Script Name` to `target.file.full_path`.   
2024-11-28 |  Enhancement:  
\- Added support for new pattern of SYSLOG logs.   
2024-08-20 |  Enhancement:  
\- Added `gsub` to remove extra characters to parse JSON logs.   
2024-08-14 |  Enhancement:  
\- Mapped `Version` to `metadata.product_version`.  
\- Mapped `SystemTime` to `metadata.event_timestamp`.  
\- Mapped `channel`, `keywords`, `MessageNumber`, `MessageTotal`, and `ScriptBlockId` to `security_result.detection_fields`.  
\- Mapped `Path` to `target.process.file.full_path`.   
2024-07-24 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-07-20 |  Enhancement:  
\- Mapped `HostApplication` to `principal.application`.  
\- Mapped `HostId` to `principal.resource.product_object_id`.  
\- Mapped `System.Computer` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `System.Version` to `metadata.product_version`.  
\- Mapped `System.ProcessID` to `principal.process.pid`.  
\- Mapped `System.ProviderName` to `principal.resource.attribute.labels`.  
\- Mapped `HostVersion`, `RunspaceId`, `PipelineId`, `EngineVersion`, `DetailSequence`, `DetailTotal`, `SequenceNumber`, and `ScriptName` to `additional.fields`.  
\- Mapped `System.EventRecordID`, `System.Task`, `System.Keywords`, `System.Opcode`, and `System.ThreadID` to `security.detection_fields`.   
2023-12-05 |  Enhancement:  
\- Added mapping for unparsed JSON logs.  
\- Mapped `Computer` to `principal.hostname`.  
\- Mapped `EventLevelName` to `security_result.severity`.  
\- Mapped `ManagementGroupName`, `Source`, `TenantId` to `additional_fields`.  
\- Mapped `RenderedDescription` to `security_result.description`.  
\- Mapped `UserName` to `principal.user.userid`.   
2023-09-14 |  Enhancement:  
\- Added mappings for unparsed JSON logs.  
\- Mapped `winlog.activity_id` to `security_result.detection_fields`.  
\- Mapped `winlog.api` to `additional.fields`.  
\- Mapped `winlog.channel`, `winlog.process.thread.id` to `security_result.about.resource.attribute.labels`.  
\- Mapped `winlog.computer_name` to `principal.hostname`.  
\- Mapped `winlog.event_id` to `metadata.product_event_type` and `security_result.rule_name`.  
\- Mapped `winlog.opcode` to `metadata.description`.  
\- Mapped `winlog.process.pid` to `principal.process.pid`.  
\- Mapped `winlog.provider_guid` to `metadata.product_deployment_id`.  
\- Mapped `winlog.provider_name` to `metadata.product_name`.  
\- Mapped `winlog.record_id` to `metadata.product_log_id`.  
\- Mapped `winlog.user.domain` to `principal.administrative_domain`.  
\- Mapped `winlog.user.identifier` to `principal.user.windows_sid`.  
\- Mapped `winlog.user.name` to `principal.user.userid`.   
2023-07-05 |  Enhancement:  
\- For `EventID = 403`, mapped `metadata.event_type` to `STATUS_UPDATE` when the value for `HostApplication` is not present.  
\- Extracted the value for `target.file.full_path` from the log using a Grok pattern when `Path` is empty.  
\- Added gsub function to rename `@timestamp` to `EventTime`.   
2022-11-09 |  Enhancement:  
\- The field `ProviderGuid` is mapped to `metadata.product_deployment_id`.  
\- The field `ExecutionProcessID` is mapped to `principal.process.pid`.  
\- The field `ProcessID` or `Process ID` is mapped to `principal.process.pid`.  
\- The field `SourceModuleType` is mapped to `principal.resource.resource_subtype`.  
\- The field `SourceModuleName` is mapped to `principal.resource.name`.  
\- The field `Machine` is mapped to `principal.asset.asset_id`.  
\- The field `MessageSourceAddress` is mapped to `principal.ip`.  
\- The field `File` is mapped to `target.process.file.full_path`.  
\- The field `Host Application` or `Command` is mapped to `target.process.command_line`.  
\- The field `Output` is mapped to `security_result.detection_fields`.  
\- The field `Message` is mapped to `security_result.description`.  
\- The field `ActivityID` is mapped to `security_result.detection_fields`.  
\- Added following mapping when EventID is `4103`  
\- The field `Host ID` or `ContextInfo_Host ID` is mapped to `target.asset.asset_id`.  
\- The field `Host Name` or `ContextInfo_Host Name` is mapped to `target.hostname`.  
\- The field `ContextInfo_Script Name` is mapped to `target.process.file.full_path`.  
\- The field `ContextInfo_Host Application` is mapped to `target.process.command_line`.  
\- The field `ContextInfo_Command Name` is mapped to `security_result.detection_fields`.  
\- The field `ContextInfo_Command Type` is mapped to `security_result.detection_fields`.  
\- The field `ContextInfo_Sequence Number` or `Sequence Number` is mapped to `security_result.detection_fields`.  
\- Added following mapping when EventID is `800`, `600` or `400`  
\- The field `UserId` is mapped to `principal.user.userid`.  
\- The field `HostApplication` is mapped to `target.process.command_line`.  
\- The field `HostId` is mapped to `target.asset.asset_id`.  
\- The field `HostName` is mapped to `target.hostname`.  
\- The field `ScriptName` is mapped to `target.process.file.full_path`.  
\- The field `SequenceNumber` is mapped to `security_result.detection_fields`.   
2022-10-13 |  Bug-Fix:  
\- Parsed failed logs by making the following changes.  
\- Added `on_error` checks on fields that failed parsing in case of no values. Fields like `opcode`, `Host Application`.  
\- Added new source,`ContextInfo` for KV parsing when `Message` is not present in the logs.  
Enhancement:  
\- Modified event_type from `GENERIC_EVENT` to `STATUS_UPDATE`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
