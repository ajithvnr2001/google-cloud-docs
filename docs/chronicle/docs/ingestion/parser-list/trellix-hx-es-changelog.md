---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-es-changelog/
title: Change log for TRELLIX_HX_ES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:32.354465+00:00
---

# Change log for TRELLIX_HX_ES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trellix-hx-es-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRELLIX_HX_ES

Date | Changes  
---|---  
2026-08-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `SourceImage`, `ClientProcessStartKey`, `database`, `CurrentDirectory`, `User`, `FileVersion`, `ParentProcessGuid`, `ParentUser`, `SourceThreadId`, `SourceUser`, `SourceIsIpv6`, `SourceHostname`, and `Hostname` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `TargetUser`, `DestinationIsIpv6`, and `DestinationPortName` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `security_result.detection_fields`: Newly mapped `NewThreadId` raw log field with `security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RpcCallClientLocality`, `Message`, `QueryStatus`, `rawmsg`, `Description`, `IntegrityLevel`, `LogonId`, `Product`, `TerminalSessionId`, `CallTrace`, `GrantedAccess`, `--type`, `--utility-sub-type`, `--lang`, `--service-sandbox-type`, `--user-data-dir`, `--webview-exe-name`, `--webview-exe-version`, `--embedded-browser-webview`, `--metrics-shmem-handle`, `--field-trial-handle`, `--pseudonymization-salt-handle`, `--trace-process-track-uuid`, `--mojo-platform-channel-handle`, `Initiated`, `--annotation`, `--attachment`, `--attachment_1`, `--initial-client-data`, `--service`, `CreationUtcTime`, `Contents`, `ZoneId`, `StartAddress`, `StartFunction`, `StartModule`, `TaskContentNew`, `encoding`, `xmlns`, and `FQDN` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `ReferrerUrl` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `--url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `OriginalFileName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions`: Newly mapped `QueryName` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers`: Newly mapped `type_value` and `data_value` raw log fields with `event.idm.read_only_udm.network.dns.answers` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `Image` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `MD5` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `SHA256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.pe_file.imphash`: Newly mapped `IMPHASH` raw log field with `event.idm.read_only_udm.principal.process.file.pe_file.imphash` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `CommandLine` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.user.company_name`: Newly mapped `Company` raw log field with `event.idm.read_only_udm.principal.user.company_name` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `ParentCommandLine` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `ParentImage` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `TargetProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `TargetImage` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SourceIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `SourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `DestinationIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `DestinationHostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `DestinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `TargetFilename` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ClientProcessId`, `ProcessId`, and `SourceProcessId` raw log fields with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `SourceProcessGUID` raw log fields with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `LogonGuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `TargetProcessGUID` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when target user details are present and `TargetUserName` raw log field is not empty.   
2026-02-27 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `src_hostname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `EventID` is `4624` or `4625` as this represents the target hostname for particular events.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `WorkstationName` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when `EventID` is `4624` or `4625` as this represents the source hostname.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `WorkstationName` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `EventID` is `4624` or `4625`.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`:  
\- If `EventID` is `4624` or `4625`:  
\- If `Hostname` is not empty, Newly mapped `Hostname` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- If `Hostname` is empty and `src_hostname` is not empty, mapped `src_hostname` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `LmPackageName` (key: `LmPackageName`), `KeyLength` (key: `KeyLength`), `TransmittedServices` (key: `TransmittedServices`) raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `new_process_id` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `new_process_name` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `process_command_line` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `token_elevation_type`, `mandatory_label`, `sourcemodulename`, `sourcemoduletype`, `Opcode`, `logon_id`, `NewProcessId`, `NewProcessName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `eventreceivedtime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message_start` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `Severity` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_target_process` is true, `has_principal` is true, and `Category` contains `Process Creation`, updated to `PROCESS_LAUNCH`.  
\- Added conditional check for [EventType] == `AUDIT_SUCCESS` and ( [Source_Value] == `Microsoft-Windows-Security-Auditing` and [Message] == `A new process has been created.` or [Category] == `Process Creation`) to map `creator_process_id` to `event.idm.read_only_udm.principal.process.pid` and `creator_process_name` to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.   
2026-01-07 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.file.names: Removed mapping of `process` from `event.idm.read_only_udm.principal.process.file.names` UDM field when `eventType` is `ipv4NetworkEvent` and `processPath` is empty.  
\- event.idm.read_only_udm.principal.process.file.full_path: Mapped `process` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `eventType` is `ipv4NetworkEvent` and `processPath` is empty.  
\- event.idm.read_only_udm.principal.process.file.full_path: Changed mapping for `event.idm.read_only_udm.principal.process.file.full_path` from `processPath` to `processPath`\\\`process` or `processPath`/`process` UDM field when `eventType` is `ipv4NetworkEvent` and both `processPath` and `process` are not empty.   
2026-01-06 |  Enhancement:  
\- Modified the conditional logic for handling the ProcessID field. The field will no longer be added to additional.fields if the EventType is `AUDIT_FAILURE`.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `ProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field when `EventType` is `AUDIT_FAILURE`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `RuleAttr` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-16 |  Enhancement:  
\- Added a new Grok pattern to parse new pattern of logs.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.   
2025-12-09 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EventTime`, `UtcTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `ProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field when `EventType` is `SetValue`.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `ProcessID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field when `EventType` is `DeleteKey`.  
\- event.idm.read_only_udm.target.registry.registry_key: Newly mapped `TargetObject` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- event.idm.read_only_udm.target.registry.registry_value_name: Newly mapped `TargetValue` raw log field with `event.idm.read_only_udm.target.registry.registry_value_name` UDM field.  
\- event.idm.read_only_udm.target.registry.registry_value_data: Setting `event.idm.read_only_udm.target.registry.registry_value_data` UDM field to `BINARY` when `Details` raw log field is similar to `Binary` else setting to `Details` raw log field with `event.idm.read_only_udm.target.registry.registry_value_type` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `Image` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `EventType` is `DeleteValue`, `DeleteKey` and `SetValue`.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `REGISTRY_DELETION` when `principal_machine_present` is `true` and `has_target_registry` is `true` and `EventType` is `DeleteValue` or `DeleteKey`.   
2025-11-20 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `addr` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `addr` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added a new grok pattern to extract fields from `kv_msg` raw log field.   
2025-11-13 |  Enhancement:  
\- event.idm.read_only_udm.target.http.user_agent: Removed mapping of `userAgent` from `event.idm.read_only_udm.network.http.user_agent` UDM field when `EventType` is `urlMonitorEvent` in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.target.http.method: Removed mapping of `urlMethod` from `event.idm.read_only_udm.network.http.method` UDM field when `EventType` is `urlMonitorEvent` in order to introduce a more accurate mapping for the raw log fields.  
\- event.idm.read_only_udm.target.network.http.user_agent: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.target.network.http.user_agent` UDM field when `EventType` is `urlMonitorEvent`.  
\- event.idm.read_only_udm.target.network.http.method: Newly mapped `urlMethod` raw log field with `event.idm.read_only_udm.target.network.http.method` UDM field when `EventType` is `urlMonitorEvent`.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `EventType` is `urlMonitorEvent`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Connection`, `Accept`, `Accept-Encoding`, `If-Unmodified-Since`, and `Range` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `ProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field when `EventType` is `DeleteValue`.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `Image` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `EventType` is `DeleteValue`.  
\- event.idm.read_only_udm.target.registry.registry_key: Newly mapped `TargetObject` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field when `EventType` is `DeleteValue`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `SourceName`, `AccountType`, `text`, `ProcessID` and `Keywords` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `RuleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.principal.process.product_specific_process_id: Newly mapped `ProcessGuid` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Setting `event.idm.read_only_udm.security_result.severity` UDM field to `INFORMATIONAL` when `Severity` raw log field is `INFO` else if `Severity` raw log field is `ERROR` then set `ERROR`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `SeverityValue` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.src.registry.registry_key: Newly mapped `originalPath` raw log field with `event.idm.read_only_udm.src.registry.registry_key` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `processPath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.target.registry.registry_value_name: Newly mapped `valueName` raw log field with `event.idm.read_only_udm.target.registry.registry_value_name` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.target.registry.registry_value_type: Set `event.idm.read_only_udm.target.registry.registry_value_type` UDM field to `DWORD` when `valueType` is similar to `DWORD`.  
\- event.idm.read_only_udm.target.registry.registry_key: Newly mapped `path` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.target.registry.registry_value_data: Newly mapped `value` raw log field with `event.idm.read_only_udm.target.registry.registry_value_data` UDM field when `eventType` is `RegValueChange`.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `REGISTRY_DELETION` when `principal_machine_present` is `true` and `has_target_registry` is `true` and `EventType` is `DeleteValue`.  
\- Modified the date filter to parse `event.idm.read_only_udm.metadata.event_timestamp` correctly.   
2025-11-07 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.file.names`: Removed mapping of `process` from `event.idm.read_only_udm.target.process.file.names` UDM field so it belongs in principal, while the registry key itself is the object.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `process` raw log field to the `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Removed mapping of `processPath` from `event.idm.read_only_udm.target.process.file.full_path` UDM field because it identifies the actor process causing the event, not the target of the action.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processPath` raw log field to the `event.idm.read_only_udm.principal.process.file.full_path UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Removed mapping of `pid` from `event.idm.read_only_udm.target.process.pid` UDM field because the PID identifies the process initiating the event, making it the actor principal, not the object being acted upon target.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field to the `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Newly mapped `path` raw log field to the `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Removed mapping of `originalPath` from `event.idm.read_only_udm.target.registry.registry_key` UDM field because it is the actual underlying registry key being affected, distinguishing it from the potentially symbolic path.  
\- `event.idm.read_only_udm.src.registry.registry_key`: Newly mapped `originalPath` raw log field with `event.idm.read_only_udm.src.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `eventType` is `RegKeyChange`, updated to `REGISTRY_MODIFICATION`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `eventType` is `imageLoadEvent`, updated to `USER_UNCATEGORIZED`.   
2025-11-06 |  Enhancement:  
\- Added grok for `kv_msg` field to map more number of fields.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `threat_name` raw log field to `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `threat_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly Mapped `startTime` raw log field to `event.idm.read_only_udm.security_result.first_discovered_time` UDM Field.  
\- Added a replace condition to `pid` raw log field to set `has_target_process` to `true` and event_type will become `PROCESS_TERMINATION`.   
2025-08-06 |  Enhancement:  
\- Added on_error check condition for `parentProcess` raw log field before setting `has_principal_process` as `true`.   
2025-08-03 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped the `timestamp` field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.network.dns.questions: Mapped the `hostname` field to `event.idm.read_only_udm.network.dns.questions.name` when it`s available.  
\- event.idm.read_only_udm.target.process.file.names: Mapped the `process` field to `event.idm.read_only_udm.target.process.file.names`.  
\- event.idm.read_only_udm.target.process.file.full_path: Mapped the `processPath` field to `event.idm.read_only_udm.target.process.file.full_path`.  
\- event.idm.read_only_udm.target.process.file.md5: Mapped the `md5` field to `event.idm.read_only_udm.target.process.file.md5`.  
\- event.idm.read_only_udm.target.process.command_line: Mapped the `processCmdLine` field to `event.idm.read_only_udm.target.process.command_line`.  
\- event.idm.read_only_udm.target.process.pid: Mapped the `pid` field to `event.idm.read_only_udm.target.process.pid`.  
\- event.idm.read_only_udm.target.file.names: Mapped the `fileName` field to `event.idm.read_only_udm.target.file.names`.  
\- event.idm.read_only_udm.target.file.mime_type: Mapped the `fileExtension` field to `event.idm.read_only_udm.target.file.mime_type`.  
\- event.idm.read_only_udm.target.file.full_path: Mapped `processPath` and `fileName` to `event.idm.read_only_udm.target.file.full_path` when both are available.  
\- event.idm.read_only_udm.principal.process.file.full_path: Mapped the `fullPath` field to `event.idm.read_only_udm.principal.process.file.full_path`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped fields `sequence_num`, `drive`, `filePath`, `devicePath`,`args`,`ipv6`,`writes`,`numBytesSeenWritten`,`lowestFileOffsetSeen`,`dataAtLowestOffset`,`textAtLowestOffset`,`closed`,`openTimeRaw`,`openDuration`, `eventReason`,`AgentId`,`data`,`hive`,`keyPath`,`path` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.process.pid: Mapped the `parentPid` field to `event.idm.read_only_udm.principal.process.pid`.  
\- event.idm.read_only_udm.principal.process.file.full_path: Mapped the `parentProcessPath` field to `event.idm.read_only_udm.principal.process.file.full_path`.  
\- event.idm.read_only_udm.principal.process.parent_process.file.names: Mapped the `parentProcess` field to `event.idm.read_only_udm.principal.process.parent_process.file.names`.  
\- event.idm.read_only_udm.principal.process.parent_process.file.full_path: Mapped the `parentPath` field to `event.idm.read_only_udm.principal.process.parent_process.file.full_path`.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Mapped the `remoteIP` and `remoteIpAddress` field to `event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Mapped the `localIP` field to `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.port: Mapped the `localPort` field to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.target.port: Mapped the `remotePort` field to `event.idm.read_only_udm.target.port`.  
\- event.idm.read_only_udm.target.url: Mapped the `requestUrl` field to `event.idm.read_only_udm.target.url`.  
\- event.idm.read_only_udm.network.http.method: Mapped the `urlMethod` field to `event.idm.read_only_udm.network.http.method`.  
\- event.idm.read_only_udm.network.http.user_agent: Mapped the `userAgent` field to `event.idm.read_only_udm.network.http.user_agent`.  
\- event.idm.read_only_udm.metadata.product_event_type: Mapped the `EventType` or `eventType` field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.network.application_protocol: Mapped the `proto` field to `event.idm.read_only_udm.network.application_protocol`.  
\- event.idm.read_only_udm.network.application_protocol_version: Mapped the `proto_version` field to `event.idm.read_only_udm.network.application_protocol_version`.  
\- event.idm.read_only_udm.target.registry.registry_key: Mapped the `originalPath` field to `event.idm.read_only_udm.target.registry.registry_key`.  
\- event.idm.read_only_udm.metadata.event_type:  
\- If EventID is `7036`, and has principal and target, updated to SERVICE_STOP or SERVICE_START based on the `param2` field.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true and `has_dns` is true, updated to `NETWORK_DNS`.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true and `network_application_protocol` is `HTTP`, updated to `NETWORK_HTTP`.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true, `has_target_process` and `eventType` is `start`, updated to `PROCESS_LAUNCH`.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true, `has_target_process` and `eventType` is `end`, updated to `PROCESS_TERMINATION`.  
\- If event_type is GENERIC_EVENT, `has_file`, `principal_machine_present` is true and `eventType` is `fileWriteEvent`, updated to `FILE_MODIFICATION`.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true, `has_target_process` and `has_principal` process, updated to `PROCESS_MODULE_LOAD`.  
\- If event_type is GENERIC_EVENT, `principal_machine_present` is true and `has_target_registry`, updated to `REGISTRY_MODIFICATION`.  
\- If event_type is GENERIC_EVENT, `has_target` and `has_principal`, updated to NETWORK_CONNECTION.   
2025-02-28 |  Enhancement:  
\- Refreshed parser to map all fields correctly.   
2024-11-28 |  Enhancement:  
\- Mapped `security_result.action` based on login status.  
\- When login is failed, then mapped `security_result.category` to `AUTH_VIOLATION`.  
\- Mapped `Status`, `FailureReason`, `SubStatus`, and `LogonType` to `additional.fields`.   
2024-11-14 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-03-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
