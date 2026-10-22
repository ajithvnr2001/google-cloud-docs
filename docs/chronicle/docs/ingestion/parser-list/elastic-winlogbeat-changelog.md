---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-winlogbeat-changelog/
title: Change log for ELASTIC_WINLOGBEAT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:12.286444+00:00
---

# Change log for ELASTIC_WINLOGBEAT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-winlogbeat-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ELASTIC_WINLOGBEAT

Date | Changes  
---|---  
2026-06-30 |  Enhancement:  
\- Added grok pattern on the `winlog.event_data.TargetObject` raw log field to extract `registry_value` field.  
\- `event.idm.read_only_udm.target.registry.registry_value_name`: Newly mapped `registry_value` field to the `event.idm.read_only_udm.target.registry.registry_value_name` UDM field.   
2026-06-09 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `winlog.event_data.EventType` and `winlog.task` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.network_domain`: Newly mapped `host.domain` raw log field with `event.idm.read_only_udm.principal.asset.network_domain` UDM field.   
2026-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `agent.hostname`, `agent.name` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields since these are mapped to `event.idm.read_only_udm.observer.hostname` UDM field when `event.code` is `17`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `winlog.computer_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `event.code` is `17`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `winlog.event_data.User` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `winlog.event_data.PipeName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `winlog.user.type`, `winlog.event_data.UtcTime`, `winlog.version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-26 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `host.os.type` from `event.idm.read_only_udm.security_result.detection_fields` UDM field since it represents principal.resource.attribute.labels value.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `host.os.type` to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Removed mapping of `process.pid` and `winlog.process.pid` from `event.idm.read_only_udm.target.process.pid` UDM field since `process.pid` does not represent the target process pid.  
\- `event.idm.read_only_udm.target.process.pid`: Mapped `winlog.event_data.ProcessId` to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed grok pattern before mapping `winlog.event_data.ParentUser` to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed grok pattern before mapping `winlog.event_data.User` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Removed mapping of `winlog.event_data.ProcessGuid` from `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field for `_event.code` 1, 23, 26, 1116, 1117 and 4702 as there is an enrichment issue.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Mapped concatenated values of `agent.id`, `host.name`, `winlog.event_data.ProcessGuid` and `winlog.event_data.ProcessId` to `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field for `_event.code` 1 with a prefix `sysmon:`.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Removed mapping of `winlog.event_data.ParentProcessGuid` from `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field for `_event.code` 1 as there is an enrichment issue.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Mapped concatenated values of `agent.id`, `host.name`, `winlog.event_data.ParentProcessGuid` and `winlog.event_data.ProcessId` to `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field for `_event.code` 1 with a prefix `sysmon:`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `winlog.event_data.ParentImage` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `winlog.event_data.UtcTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `winlog.user.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `winlog.user.type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `process.pid`, `winlog.process.pid`, `winlog.event_data.Company`, `winlog.event_data.CurrentDirectory`, `winlog.event_data.Description`, `winlog.event_data.FileVersion`, `winlog.event_data.IntegrityLevel`, `winlog.event_data.LogonId`, `winlog.event_data.OriginalFileName`, `winlog.event_data.Product`, `winlog.event_data.TerminalSessionId`, `winlog.event_data.RuleName` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `winlog.version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-15 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `winlog.event_data.powershell.HostApplication` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `winlog.event_data.powershell.ScriptName` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `winlog.event_data.powershell.UserId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `host.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_event.created` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `agent.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `host.domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `winlog.event_data.powershell.CommandName`, `winlog.event_data.powershell.CommandLine`, `winlog.event_data.powershell.HostVersion`, `winlog.event_data.powershell.DetailSequence`, `winlog.event_data.powershell.DetailTotal`, `winlog.event_data.powershell.HostId`, `winlog.event_data.powershell.HostName`, `winlog.event_data.powershell.PipelineId`, `winlog.event_data.powershell.RunspaceId`, `winlog.event_data.powershell.SequenceNumber`, `winlog.keywords`, `winlog.event_data.powershell.EngineVersion` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` as log contains both `principal` and `target` machine data, otherwise mapped `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` as log has only `principal` machine data.   
2026-05-05 |  Enhancement:  
\- Added support for new format of `winlog.event_data.TaskContentNew` logs.  
\- Added a grok pattern on `xml_data` to extract `EventVersion`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `winlog.event_data.TaskName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `host.mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `winlog.event_data.ClientProcessId` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `winlog.event_data.ParentProcessId` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `winlog.event_data.ClientProcessStartKey` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TimeTriggerStartBoundary`,`EventVersion`, `winlog.version` , `RegistrationInfoSecurityDescriptor`, `winlog.event_data.RpcCallClientLocality`, `winlog.provider_guid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-29 |  Enhancement:  
\- Modified the null check for `src_port` to parse the failed logs.  
\- Added a check condition to map `metadata.event_type` for `event_id` 7036 to `SERVICE_STOP` to parse the failed logs.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `winlog.event_data.param1` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- Added a `_is_computer_account_` flag condition before mapping `metadata.event_type` to `USER_LOGIN` for `event_id` `4624`.   
2024-12-23 |  Enhancement:  
\- Mapped `DestinationIp` to `target.ip` and `target.asset.ip`.   
2024-09-24 |  Enhancement:  
\- Mapped `source_network_address` to `src.ip`.  
\- Mapped `source_port` to `src.port`.   
2024-07-01 |  Enhancement:  
\- Mapped `winlog.event_data.TaskContent` to `additional.fields`.  
\- Mapped `principal_user_id` to `principal.user.userid`.  
\- Mapped `principal_command_line` to `principal.process.command_line`.  
\- Mapped `run_level`, `arguments`, `RegistrationInfoURI`, `WnfStateChangeTriggerEnabled`, `WnfStateChangeTriggerStateName`, `WnfStateChangeTriggerData`, `WnfStateChangeTriggerDataOffset`, `IdleSettingsRestartOnIdle`, `IdleSettingsStopOnIdleEnd`, `IdleSettingsWaitTimeout`, `IdleSettingsDuration`, `Priority`, `ExecutionTimeLimit`, `RunOnlyIfIdle`, `DisallowStartOnRemoteAppSession`, `UseUnifiedSchedulingEngine`, `DisallowStartIfOnBatteries`, `MultipleInstancesPolicy`, `StopIfGoingOnBatteries`, `AllowHardTerminate`, `StartWhenAvailable`, `RunOnlyIfNetworkAvailable`, `AllowStartOnDemand`, `Enabled`, `Hidden`, and `WakeToRun` to `additional.fields`.   
2024-06-20 |  Enhancement:  
\- Mapped `winlog.event_data.ObjectServer` to `target.resource.attribute.labels`.   
2024-06-19 |  Enhancement:  
\- Removed the Grok pattern to parse `message_data` completely.   
2024-06-12 |  Enhancement:  
\- Mapped `process.executable` to `principal.process.file.full_path`.  
\- Mapped `process.parent.executable` to `principal.process.parent_process.file.full_path`.  
\- Mapped `process.name` to `principal.process.file.names`.  
\- Mapped `process.parent.name` to `principal.process.parent_process.file.names`.  
\- Mapped `process.entity_id` to `target.process.product_specific_process_id`.  
\- Mapped `process.pid` to `principal.resource.attribute.labels`.   
2024-01-17 |  Enhancement:  
\- Mapped `winlog.logon.failure.sub_status`, `winlog.logon.failure.reason` and `winlog.logon.failure.status` to `security_result.detection_fields`.  
\- Mapped `winlog.event_data.GroupMembership` to `principal.user.group_identifiers`.  
\- Mapped `client_ip` to `principal.asset.ip`.  
\- Mapped `ip` to `principal.asset.ip`.  
\- Mapped `winlog.event_data.SourceIp` to `principal.asset.ip`.  
\- Mapped `destination.ip` to `target.asset.ip`.  
\- Mapped `winlog.event_data.DestinationIp` to `target.asset.ip`.  
\- Mapped `agent.hostname` to `target.asset.hostname`.  
\- Mapped `winlog.event_data.IpAddress` to `principal.asset.ip`.  
\- Mapped `source.ip` to `principal.asset.ip`.   
2023-12-29 |  Enhancement:  
\- Mapped `winlog.event_data.Binary`, `winlog.event_data.process.thread.id`, `winlog.event_data.param1`, `winlog.event_data.param2`, `winlog.event_data.param3`, `winlog.event_data.param4`, `winlog.event_data.param5`, `winlog.event_data.param6`, `winlog.event_data.param7`, `winlog.event_data.param8`, `winlog.event_data.param9`, `winlog.event_data.param10`, `winlog.event_data.param11`, `winlog.event_data.param12`, `winlog.event_data.param13`, `winlog.channel`, `winlog.opcode` to `security_result.detection_fields`.  
\- Mapped `host.ip` to `principal.ip`.  
\- Added null check before mapping `_event.action` to `metadata.description`.  
\- When `_event.code` is not in `1`, `4`, `5`, `16`, `24` then mapped `winlog.process.pid` to `principal.process.pid`.  
\- When `metadata.description` is not set then mapped `message` to `metadata.description`.  
\- When `metadata.description` is set then mapped `message` to `security_result.detection_fields`.   
2023-12-07 |  Enhancement:  
\- Where `_event.code` is `22`, mapped the following:  
\- `agent.hostname` to `principal.hostname`.  
\- `dns.question.name` to `network.dns.questions`.  
\- `winlog.event_data.QueryName` to `target.hostname`.   
2023-11-28 |  Enhancement:  
\- Where `event.param2` is `stopped`, mapped `metadata.event_type` to `SERVICE_STOP`.  
\- Where `event.param2` is `running`, mapped `metadata.event_type` to `SERVICE_START`.   
2023-11-12 |  Enhancement:  
\- Mapped `winlog.event_data.HandleId` to `resource_ancestors.product_object_id`.  
\- Mapped `winlog.event_data.ObjectType` to `target.resource.resource_subtype`.  
\- Mapped `winlog.event_data.OperationType` to `security_result.summary`.  
\- Mapped `object_server` to `resource_ancestors.name`.  
\- Mapped `Accesses` to `target.resource.attribute.labels`.  
\- Mapped `Properties` to `security_result.detection_fields`.   
2023-10-25 |  Enhancement:  
For event_id `7036`:  
\- Mapped `event_data.param1` to `target.application`.  
\- Mapped `event_data.param2` to `security_result.action`.  
\- Set `metadata.event_type` to `SERVICE_STOP`.  
For event_id `10016`:  
\- Mapped `event_data.param1` to `target.resource.attribute.permissions`.  
\- Mapped `event_data.param5` to `target.resource.product_object_id`.  
\- Mapped `event_data.param6` to `target.user.userid`.  
\- Mapped `event_data.param7` to `target.administrative_domain`.  
\- Mapped `event_data.param8` to `target.user.windows_sid`.  
\- Mapped `event_data.param10` to `target.application`.  
\- Set `metadata.event_type` to `SETTING_MODIFICATION`.  
For event_id `18456` and `18451`:  
\- Mapped `event_data.param1` to `target.user.userid`.  
\- Mapped `client_ip` to `principal.ip`.  
\- Mapped `database_name` to `target.hostname`.  
\- Mapped `summary` to `security_result.summary`.  
\- Set `metadata.event_type` to `USER_UNCATEGORIZED`.  
Mapped the following fields:  
\- Mapped `event_id` to `metadata.product_event_type`.  
\- Mapped `computer_name` to `principal.hostname`.  
\- Mapped `type` to `observer.application`.  
\- Mapped `task` to `target.resource.attribute.labels`.  
\- Mapped `source_name` to `security_result.about.labels`.  
\- Mapped `process_id` to `principal.process.pid`.  
\- Mapped `provider_guid` to `additional.fields`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `thread_id` to `security_result.about.resource.attribute.labels`.  
\- Mapped `beat.version` to `principal.platform_version`.  
\- Mapped `message` to `security_result.description`.   
2023-09-06 |  Enhancement:  
\- Mapped `winlog.event_data.LmPackageName` to `target.resource.attribute.labels`.  
\- Mapped `winlog.event_data.AuthenticationPackageName` to `target.resource.attribute.labels`.  
\- Mapped `winlog.event_data.LogonProcessName` to `target.resource.attribute.labels`.  
\- Mapped `winlog.event_data.WorkstationName` to `target.resource.attribute.labels`.  
\- Mapped `winlog.event_data.TargetOutboundUserName` to `target.resource.attribute.labels`.   
2023-08-18 |  Enhancement:  
\- Mapped `CN` from `winlog.event_data.MemberName` to `target.user.userid` for event_id's `4733`, `4732`, `4729`, `4756`, `4757`, `4728`.  
\- Mapped `metadata.event_type` to `GROUP_MODIFICATION` for event_id's `4733`, `4732`, `4729`, `4756`, `4757`, `4728`.  
\- Mapped `winlog.event_data.Image` to `target.process.file.full_path`.  
\- Mapped `winlog.event_data.ProcessGuid` to `target.process.product_specific_process_id`.  
\- Mapped `winlog.event_data.ProcessId` to `target.process.pid`.  
\- Mapped `winlog.event_data.TargetObject` to `target.registry.registry_value_name` for `event.code` = 13 , 14.  
\- Mapped `winlog.event_data.EventType` to `metadata.product_event_type`.  
\- Mapped `winlog.event_data.Subject` to `security_result.detection_fields` for event_id = 4887.  
\- Mapped `winlog.event_data.Requester` to `principal.user.userid` for event_id = 4887.   
2023-07-13 |  \- Mapped `winlog.event_data.LogonType` to `extensions.auth.auth_details`.  
\- Mapped `winlog.event_data.ParentProcessId` to `principal.process.pid`.  
\- Mapped `winlog.event_data.ParentProcessGuid` to `principal.process.product_specific_process_id`.  
\- Mapped `winlog.event_data.ParentCommandLine` to `principal.process.command_line`.  
\- Mapped `winlog.event_data.ParentUser` to `principal.user.userid`.  
\- Mapped `winlog.event_data.ProcessId` to `target.process.pid`.  
\- Mapped `winlog.event_data.ProcessGuid` to `target.process.product_specific_process_id`.  
\- Mapped `winlog.event_data.CommandLine` to `target.process.command_line`.  
\- Mapped `winlog.event_data.User` to `target.user.userid`.  
\- Mapped `winlog.event_data.LogonGuid` to `target.resource.product_object_id`.  
\- Mapped `winlog.event_data.Hashes.SHA1` to `target.process.file.sha1`.  
\- Mapped `winlog.event_data.Hashes.SHA256` to `target.process.file.sha256`.  
\- Mapped `winlog.event_data.Hashes.MD5` to `target.process.file.md5`.  
\- Mapped `host.ip` to `principal.ip` for `event.code` = 6.  
\- Mapped `host.mac` to `principal.mac` for `event.code` = 6.  
\- Mapped `winlog.event_data.ImageLoaded` to `target.process.file.full_path`.  
\- Mapped `winlog.event_data.EventType` to `metadata.product_event_type` for `event.code` = 12.  
\- Mapped `winlog.opcode` to `security_result.description` for `event.code` = 12.  
\- Mapped `winlog.event_data.TargetObject` to `target.registry.registry_value_name`.   
2023-05-25 |  Enhancement: Mapped the following fields when `event.code` = 10043.  
\- mapped `host.ip` to `principal.ip`.  
\- mapped `host.mac` to `principal.mac`.  
\- mapped the XML field `ArrayOfBrowserExtension/BrowserExtension/BrowserExtensionInfo/UsedUrls` of `message` to `principal.process.file.embedded_urls`.  
\- mapped the XML field `ArrayOfBrowserExtension/BrowserExtension/BrowserExtensionInfo/UsedEmails` of `message` to `principal.user.email_addresses`.   
2023-04-21 |  Enhancement:  
\- Refactored code to map common fields for events at top instead of mapping each in all the `event_id` conditions.  
\- Added null checks to `user.name`, `user.domain`, `user.id` prior mapping to udm to avoid overriding SubjectUserName from mapping to `principal.user.userid`.  
\- Mapped `winlog.event_data.MemberName` to `target.user.userid`.  
\- Mapped `winlog.event_data.MemberSid` to `target.user.windows_sid`.  
\- Mapped the following for event_id: 4769:  
\- Mapped `winlog.event_data.TargetUserName` to `target.user.userid`.  
\- Mapped `winlog.event_data.LogonGuid` to `target.resource.product_object_id`.  
\- Mapped `winlog.event_data.TicketOptions`, `winlog.event_data.TicketEncryptionType`, `winlog.event_data.TicketEncryptionTypeDescription`, `winlog.event_data.TransmittedServices`, `winlog.event_data.TicketOptionsDescription` to `security_result.about.resource.attribute.labels`.  
\- Mapped `winlog.event_data.ServiceSid` to `target.user.windows_sid`.  
\- Mapped `winlog.event_data.TargetDomainName` to `target.administrative_domain`.  
\- Mapped `winlog.event_data.ServiceName` to `target.application`.   
2023-03-27 |  Enhancement:  
\- Parsed logs with `event.code` as 4769 to `security_result.rule_name`.  
\- Mapped `Failure Code` and `TicketOptions` to `security_result.about.labels`.  
\- Mapped `winlog.event_data.Status` to `security_result.action_details`.  
\- Mapped `winlog.event_data.Status` and `winlog.event_data.StatusDescription` to `metadata.description`.   
2023-03-10 |  Enhancement  
Handled the following errors:  
\- `acct_status` is not matching on the Grok pattern.  
\- Added empty condition check for `_user.id`, `_user.name`, `_user.domain` and `agent.hostname`.   
2022-12-22 |  Enhancement  
\- Mapped `winlog.event_data.RelativeTargetName` to `target.process.file.full_path`.   
2022-11-28 |  Enhancement  
\- Mapped `event.original` to `security_result.detection_fields`.  
\- Mapped `ip` to `principal.ip`.  
\- Mapped `mac` to `principal.mac`.   
2022-11-22 |  Enhancement - Mapped the following UDM fields:-  
\- when `event.code` = 4724 mapped the following fields:-  
\- Mapped `Account Domain` to `principal.administrative-domain`.  
\- Mapped `metadata.event_type` to `USER_CHANGE_PASSWORD`.  
\- Mapped `event.outcome` to `security_result.outcomes`.  
\- Mapped `event.action and event.outcome` to `security_result.summary`.  
\- Mapped `log.level` to `security_result.severity_details`.   
2022-11-09 |  Enhancement - Mapped the following UDM fields:-  
\- Mapped `User Account control` to `security_result.description` when `event.code` = 4738.  
\- when `event.code` = 4657 mapped the following fields:-  
\- Mapped `Account Domain` to `principal.administrative-domain`.  
\- Mapped `winlog.event_data.ObjectValueName` to `target.registry.registry_value_name`.  
\- Mapped `Operation Type` to `security_result.summary`.  
\- Mapped `metadata.event_type` to `REGISTRY_MODIFICATION`.  
\- Mapped `winlog.event_data.ProcessName` to `target.process.file.full_path`.  
\- Mapped `winlog.event_data.ObjectName` to `target.resource.name`.  
\- Mapped `winlog.event_data.OldValue` to `target.resource.attribute.labels`.  
\- Mapped `winlog.event_data.NewValue` to `target.resource.attribute.labels`.  
\- Mapped `winlog.computer_name` to `target.hostname`.  
\- Mapped `event.outcome` to `security_result.outcomes`.   
2022-11-03 |  Enhancement  
\- Mapped `winlog.provider_name` to `metadata.product_name`.  
\- Mapped `winlog.event_data.OpCorrelationID` to `network.session_id`.  
\- Mapped `winlog.api`,`winlog.event_data.AttributeValue`,`winlog.provider_guid`,`winlog.event_data.ObjectDN`,`winlog.event_data.SubjectLogonId`,`event_data.AttributeSyntaxOID` to `additional.fields`.  
\- Mapped `winlog.record_id` to `metadata.product_log_id`.  
\- Mapped `winlog.opcode` to `security_result.description`.  
\- Mapped `winlog.event_data.AttributeLDAPDisplayName` to `target.resource.type`.  
\- Mapped `winlog.event_data.ObjectGUID` to `target.group.product_object_id`.  
\- Mapped `winlog.channel`,`winlog.process.thread.id`,`winlog.event_data.DSType`,`winlog.event_data.ObjectClass` to `security_result.about.resource.attribute.labels`.  
\- Mapped `winlog.process.pid` to `principal.process.pid`.  
\- Mapped `winlog.event_data.DSName` to `target.hostname`.  
\- Mapped `winlog.event_id` to `metadata.product_event_type`.  
\- Added conditional check for `winlog.record_id`,`_event.provider`,`agent.type`,`agent.version`.   
2022-09-06 |  Enhancement  
\- Mapped `source.ip` to `principal.ip`.  
\- Mapped `source.port` to `principal.port`.  
\- Mapped `user.name` to `principal.user.user_display_name`.  
\- Mapped `related.user` to `principal.user.group_identifiers`.  
\- Mapped `winlog.event_data.TargetUserName` to `target.user.userid`.  
\- Changed event_type from `GENERIC_EVENT` to `STATUS_UPDATE`.  
\- Added condition for event_type `STATUS_UPDATE` to reduce generic percentage.   
2022-08-11 |  Enhancement  
Mapped following fields for logs in json format  
-`host.name` to `observer.hostname`.  
Parsed logs with type USER.   
2022-08-09 |  Bug-fix  
\- Added conditions for extracting Target user details.  
\- Reduced the generic percentage by changing the event_type from `GENERIC_EVENT` to `STATUS_UPDATE`.   
2022-05-26 |  Enhancement  
\- kind mapped to additional.fields.  
\- ephemeral_id mapped to additional.fields.  
\- cs.version mapped to metadata.product_version.  
\- agent.name mapped to observer.user.userid.  
\- agent.ephemeral_id mapped to additional.fields.  
\- winlog.provider_guid mapped to additional.fields.  
\- winlog.channel mapped to additional.fields.  
\- winlog.api mapped to additional.fields.  
\- winlog.process.pid mapped to principal.process.pid.  
\- winlog.user.domain mapped to principal.administrative_domain.  
\- winlog.user.identifier mapped to principal.user.windows_sid.  
\- winlog.user.name mapped to target.user.userid.  
\- winlog.user.type mapped to security_result.about.labels.  
\- ip mapped to principal.ip.  
\- mac mapped to principal.mac.  
\- image mapped to target.process.file.full_path.  
\- processGuid mapped to target.process.product_specific_process_id.  
\- eventType mapped to target.registry.registry_key.  
\- TargetObject mapped to target.registry.registry_value_name.  
\- Action ID mapped to security_result.about.labels.  
\- Action Name mapped to security_result.about.labels.   
2022-05-19 |  Bug-Fix:  
Mapped following fields for event_id = 1, 3, 5:  
`agent.name` mapped to `principal.hostname`.  
`winlog.process.pid` mapped to `principal.process.pid`.  
`winlog.event_data.Image` mapped to `target.process.file.full_path`.  
Mapped following fields for event_id = 7, 11, 18, 17:  
`agent.name` mapped to `principal.hostname`.  
`winlog.event_data.Image` mapped to `target.process.file.full_path`.  
Mapped following fields for event_id = 4, 8, 9, 14, 13, 12, 10, 26, 16, 19, 20, 21:  
`agent.name` mapped to `principal.hostname`:  
Mapped following fields for event_id = 6:  
`agent.name` mapped to `principal.hostname`.  
`winlog.event_data.Hashes` mapped to target.process.file.sha1.  
Mapped following fields for event_id = 2, 15:  
`agent.name mapped` to `principal.hostname`.  
`winlog.event_data.TargetFilename` mapped to `target.file.full_path`.  
Added check for file.path in event_id=9.   
2022-05-04 |  Enhancement  
-Mapped timestamp.  
-Mapped winlog.event_data.TargetFilename and winlog.event_data.ProcessId for event_id 11.  
-Mapped winlog.event_data.SourcePort,winlog.event_data.DestinationPort, winlog.event_data.DestinationIp, winlog.event_data.SourceIp,winlog.event_data.Protocol for event_id 3.  
-Added conditional checks for the field process.pid.   
2022-04-27 |  Enhancement-Added new field mapping.  
mapped StartAddress to target.labels   
2022-04-13 |  Enhancement  
-Mapped ReferrerUrl, HostUrl from additional to security_result.rule_labels.  
-Mapped CallTrace field to security_result.detection_fields.  
Handled the below errors:  
`winlog.keywords.0` not found in state data  
`security_result` not found in state data  
`winlog.record_id`: field not set  
`_event.provider`: field not set  
`powershell.file.script_block_id`: field not set  
`winlog.opcode`: field not set  
`_event.action`: field not set  
`auth_mechanism` must not be empty  
`winlog.process.pid`: field not set  
`winlog.event_data.TargetUserName`: field not set  
`agent.type`: field not set  
`host.name`: field not set  
`agent.version`: field not set   
2022-03-25 |  Enhancement  
\- Added check for event_type where event.code is either 11, 12, or 13.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
