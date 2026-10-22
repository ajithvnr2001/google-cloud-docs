---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-edr-changelog/
title: Change log for SENTINEL_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:41.409042+00:00
---

# Change log for SENTINEL_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENTINEL_EDR

Date | Changes  
---|---  
2025-07-23 |  Enhancement:  
-`event.idm.read_only_udm.principal.mac`: Newly mapped `sourceMacAddresses` raw log field to event.idm.read_only_udm.principal.mac and event.idm.read_only_udm.principal.asset.mac.  
-`event.idm.read_only_udm.principal.port`: Newly mapped `firewallNotificationTrafficLocalPort` raw log field to event.idm.read_only_udm.principal.port.  
-`event.idm.read_only_udm.target.port`: Newly mapped `firewallNotificationTrafficRemotePort` raw log field to event.idm.read_only_udm.target.port.  
-`event.idm.read_only_udm.network.application_protocol`: Newly mapped `firewallNotificationTrafficProtocol` raw log field to event.idm.read_only_udm.network.application_protocol.  
-`event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `firewallNotificationTrafficProcessName` raw log field to event.idm.read_only_udm.principal.process.file.full_path.  
-`event.idm.read_only_udm.principal.process.pid`: Newly mapped `firewallNotificationTrafficPID` raw log field to event.idm.read_only_udm.principal.process.pid.  
-`event.idm.read_only_udm.target.ip`: Newly mapped `firewallNotificationTrafficRemoteHost` raw log field to event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped to `sourceIpAddresses` raw log field to event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip UDM fields.  
-`event.idm.read_only_udm.security_result.action`: Newly mapped `firewallNotificationRuleAction` raw log field to event.idm.read_only_udm.security_result.action.  
-`event.idm.read_only_udm.security_result.rule_id`: Newly mapped `firewallNotificationRuleId` raw log field to event.idm.read_only_udm.security_result.rule_id.  
-`event.idm.read_only_udm.security_result.rule_name`: Newly mapped `firewallNotificationRuleName` raw log field to event.idm.read_only_udm.security_result.rule_name.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `firewallNotificationTrafficNumberOfEvents`, `firewallNotificationTrafficDurationOfMeasurement` and `sourceThreatCount` raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- Added logic to set event.idm.read_only_udm.metadata.event_type to NETWORK_CONNECTION when both principal and target ip are present.  
\- Updated the condition to validate fileHash values, excluding `N/A`, `None` and empty values.   
2024-07-29 |  Enhancement:  
\- If `registry.keyPath` or `registry.value` is not null, then only mapped `metadata.event_type` to `REGISTRY_CREATION`.   
2024-07-23 |  Enhancement:  
\- Mapped `agentDetectionInfo.agentOsName` to `target.platform_version`.  
\- Mapped `agentDetectionInfo.agentLastLoggedInUserName` to `target.user.userid`.   
2024-07-09 |  Bug-Fix:  
\- Changed mapping for `suser` from `principal.user.userid` to `target.user.userid`.  
\- Changed mapping for `suser` from `principal.user.user_display_name` to `target.user.user_display_name`.  
\- Removed mapping for `accountId` from `target.user.userid`.  
\- Mapped `prin_user` to `principal.user.userid`.   
2024-06-03 |  Enhancement:  
\- Mapped `suser` to `principal.user.userid`.  
\- Mapped `accountId` to `target.user.userid`.  
\- Mapped `MessageSourceAddress` to `principal.ip`.  
\- Mapped `machine_host` to `principal.hostname`.   
2024-05-20 |  Enhancement:  
\- Mapped `event.dns.response` to `network.dns.answers.data`.   
2024-05-06 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-03-22 |  Enhancement:  
\- Added new Grok pattern to parse new format of tab-separated KV logs.  
\- Mapped `osName` to `src.platform`.   
2024-03-15 |  Enhancement:  
\- Mapped `site.id:account.id:agent.uuid:tgt.process.uid` to `target.process.product_specific_process_id`.  
\- Mapped `site.id:account.id:agent.uuid:src.process.uid` to `principal.process.product_specific_process_id`.  
\- Mapped `site.id:account.id:agent.uuid:src.process.parent.uid` to `principal.process.parent_process.product_specific_process_id`.  
\- Removed `src.process.cmdline` from being mapped to `target.process.command_line`.   
2023-11-09 |  Fix:  
\- Mapped `tgt.process.user` to `target.user.userid`.   
2023-10-30 |  Fix:  
\- Added not null check to `principal_port` prior mapping to UDM.  
\- When `event.category` is `url` and `meta.event.name` is `HTTP`, mapped `metadata.event_type` to `NETWORK_HTTP`.   
2023-09-06 |  \- Added mapping of `tgt.process.storyline.id` to `security_result.about.resource.attribute.labels`.  
\- Modified mapping of `src.process.storyline.id` from `principal.process.product_specific_process_id` to `security_result.about.resource.attribute.labels`.  
\- Modified mapping of `src.process.parent.storyline.id` from `principal.parent.process.product_specific_process_id` to `security_result.about.resource.attribute.labels`.   
2023-08-31 |  \- Mapped `indicator.category` to `security_result.category_details`.   
2023-08-03 |  \- Initialized `event_data.login.loginIsSuccessful` to null.  
\- Mapped `module.path` to `target.process.file.full_path` and `target.file.full_path` where `event.type` is `Module Load`.  
\- Mapped `module.sha1` to `target.process.file.sha1` and `target.file.sha1` where `event.type` is `Module Load`.  
\- Mapped `metadata.event_type` to `PROCESS_MODULE_LOAD` where `event.type` is `Module Load`.  
\- Mapped `registry.keyPath` to `target.registry.registry_key` for `REGISTRY_*` events.  
\- Mapped `registry.value` to `target.registry.registry_value_data` for `REGISTRY_*` events.  
\- Mapped `event.network.protocolName` to `network.application_protocol`.  
\- Mapped `principal.platform`, `principal.asset.platform_software.platform` to `LINUX` if `endpoint.os` is `linux`.  
\- Mapped `event.login.userName` to `target.user.userid` when `event.type` is `Login` or `Logout.`  
\- Mapped `target.hostname` by obtaining the hostname from `url.address` when `event.type` is `GET`, `OPTIONS`, `POST`, `PUT`, `DELETE`, `CONNECT`, `HEAD`.   
2023-06-09 |  \- Mapped `osSrc.process.parent.publisher` to `principal.resource.attribute.labels`.  
\- Mapped `src.process.rUserName/src.process.eUserName/src.process.lUserName` to `principal.user.user_display_name`.  
\- Added check to fields: `src.process.eUserId`, `src.process.lUserId`, `tgt.process.rUserUid` prior mapping to UDM.  
\- Mapped `tgt.file.location`, `registry.valueFullSize`, `registry.valueType` to `target.resource.attribute.labels`.  
\- Mapped `indicator.description` to `security_result.summary`.  
\- Mapped `metadata.event_type` to `SCAN_NETWORK` where `event.type` is `Behavioral Indicators`.  
\- Mapped `metadata.event_type` to `SCAN_UNCATEGORIZED` where `event.type` is `Command Script`.  
\- Initialized fields `meta.osFamily`, `meta.osRevision`, `event.type`.  
\- Added ISO8601 to date filter to parser ISO8601 timestamp.  
\- Added on_error to `@timestamp` string conversion.  
\- Added on_error to `meta.uuid` prior mapping.   
2023-05-25 |  \- Mapped `event.source.commandLine` to `principal.process.command_line`.  
\- Mapped `event.source.executable.path` to `principal.process.file.full_path`.  
\- Set `metadata.event_type` to `PROCESS_OPEN` where `event.type` is `openProcess`.  
\- Mapped `site.name:site.id` to `principal.namespace` if both `site.name` and `site.id` are not null.  
\- Mapped `event.network.direction` to `network.direction`.  
\- Mapped `meta.event.name` to `metadata.description`.  
\- Mapped `task.name` to `target.resource.name`.  
\- Mapped `agent.uuid` to `principal.asset.product_object_id`.  
\- Mapped `src.process.publisher` to `principal.resource.attribute.labels`.  
\- Mapped `src.process.cmdline` to `target.process.command_line`.  
\- Mapped `mgmt.osRevision` to `principal.asset.platform_software.platform_version`.  
\- Mapped `security_result.category` according to `indicator.category` value.  
\- Mapped `event.dns.response` to `network.dns.answers`.  
\- Mapped `registry.keyPath` to `target.registry.registry_key`.  
\- Mapped `event.id` to `target.registry.registry_value_name`.   
2023-04-27 |  \- Mapped `event.type` to `metadata.product_event_type` for Cloud Funnel v2 logs.   
2023-04-20 |  Enhancement:  
\- Added null and `-` conditinal check for the field `data.ipAddress`.  
\- Added grok conditional check for the field `sourceMacAddresses`.   
2023-03-02 |  Enhancement:  
\- When (`event.type` == `tcpv4` and `event.direction` == `INCOMING`) or `event.type` contains `(processExit|processTermination|processModification|duplicate)` , then mapped `event.source.executable.signature.signed.identity` to `target.resource.attribute.labels` else mapped it to `principal.resource.attribute.labels`.  
\- Mapped `event.parent.executable.signature.signed.identity`, `event.process.executable.signature.signed.identity to `principal.resource.attribute.labels`, `".  
\- Mapped `event.targetFile.signature.signed.identity`, `event.target.executable.signature.signed.identity`, `event.target.parent.executable.signature.signed.identity` to `target.resource.attribute.labels`.   
2023-02-24 |  BugFix:  
\- Refactored the code to clearly differentiate between the log versions.  
\- For USER_LOGIN cloud funnel v2 logs, mapped `event.login.lognIsSuccessful` details to `security_result.action` and `security_result.summary`  
2023-02-13 |  BugFix:  
\- Parsed cloud funnel v1 logs as required.  
\- Mapping all http logs to `NETWORK_HTTP`.  
\- `NETWORK_HTTP` should have url field mapped to `target.url` instead of `metadata.url_back_to_product`.   
2023-01-20 |  Enhancement:  
\- Mapped the field `event.url` to `target.hostname` and `target.url`.  
\- Mapped `metadata.event_type` to `NETWORK_HTTP` where `event.type` == `http`.   
2023-01-16 |  Fix  
\- Mapped `mgmt.url` to `metadata.url_back_to_product` instead of `target.url`.  
\- Mapped `site.name` to `principal.location.name`.  
\- Mapped `src.process.rUserUid` to `principal.user.userid`.  
\- Mapped `src.process.eUserId` to `principal.user.userid`.  
\- Mapped `src.process.lUserId` to `principal.user.userid`.  
\- Mapped `src.process.parent.rUserUid` to `metadata.ingestion_labels`.  
\- Mapped `src.process.parent.eUserId` to `metadata.ingestion_labels`.  
\- Mapped `src.process.parent.lUserId` to `metadata.ingestion_labels`.  
\- Mapped `tgt.process.rUserUid` to `target.user.userid`.  
\- Mapped `tgt.process.eUserId` to `target.user.userid`.  
\- Mapped `tgt.process.lUserId` to `target.user.userid`.  
\- If `event.type` is `Process Creation` mapped `metadata.event_type` to `PROCESS_LAUNCH`.  
\- If `event.type` is `Duplicate Process Handle` mapped `metadata.event_type` to `PROCESS_OPEN`.  
\- If `event.type` is `Duplicate Thread Handle` mapped `metadata.event_type` to `PROCESS_OPEN`.  
\- If `event.type` is `Open Remote Process Handle` mapped `metadata.event_type` to `PROCESS_OPEN`.  
\- If `event.type` is `Remote Thread Creation` mapped `metadata.event_type` to `PROCESS_LAUNCH`.  
\- If `event.type` is `Command Script` mapped `metadata.event_type` to `FILE_UNCATEGORIZED`.  
\- If `event.type` is `IP Connect` mapped `metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `event.type` is `IP Listen` mapped `metadata.event_type` to `NETWORK_UNCATEGORIZED`.  
\- If `event.type` is `File ModIfication` mapped `metadata.event_type` to `FILE_MODIfICATION`.  
\- If `event.type` is `File Creation` mapped `metadata.event_type` to `FILE_CREATION`.  
\- If `event.type` is `File Scan` mapped `metadata.event_type` to `FILE_UNCATEGORIZED`.  
\- If `event.type` is `File Deletion` mapped `metadata.event_type` to `FILE_DELETION`.  
\- If `event.type` is `File Rename` mapped `metadata.event_type` to `FILE_MODIfICATION`.  
\- If `event.type` is `Pre Execution Detection` mapped `metadata.event_type` to `FILE_UNCATEGORIZED`.  
\- If `event.type` is `Login` mapped `metadata.event_type` to `USER_LOGIN`.  
\- If `event.type` is `Logout` mapped `metadata.event_type` to `USER_LOGOUT`.  
\- If `event.type` is `GET` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `OPTIONS` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `POST` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `PUT` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `DELETE` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `CONNECT` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `HEAD` mapped `metadata.event_type` to `NETWORK_HTTP`.  
\- If `event.type` is `Not Reported` mapped `metadata.event_type` to `STATUS_UNCATEGORIZED`.  
\- If `event.type` is `DNS Resolved` mapped `metadata.event_type` to `NETWORK_DNS`.  
\- If `event.type` is `DNS Unresolved` mapped `metadata.event_type` to `NETWORK_DNS`.  
\- If `event.type` is `Task Register` mapped `metadata.event_type` to `SCHEDULED_TASK_CREATION`.  
\- If `event.type` is `Task Update` mapped `metadata.event_type` to `SCHEDULED_TASK_MODIfICATION`.  
\- If `event.type` is `Task Start` mapped `metadata.event_type` to `SCHEDULED_TASK_UNCATEGORIZED`.  
\- If `event.type` is `Task Trigger` mapped `metadata.event_type` to `SCHEDULED_TASK_UNCATEGORIZED`.  
\- If `event.type` is `Task Delete` mapped `metadata.event_type` to `SCHEDULED_TASK_DELETION`.  
\- If `event.type` is `Registry Key Create` mapped `metadata.event_type` to `REGISTRY_CREATION`.  
\- If `event.type` is `Registry Key Rename` mapped `metadata.event_type` to `REGISTRY_MODIfICATION`.  
\- If `event.type` is `Registry Key Delete` mapped `metadata.event_type` to `REGISTRY_DELETION`.  
\- If `event.type` is `Registry Key Export` mapped `metadata.event_type` to `REGISTRY_UNCATEGORIZED`.  
\- If `event.type` is `Registry Key Security Changed` mapped `metadata.event_type` to `REGISTRY_MODIfICATION`.  
\- If `event.type` is `Registry Key Import` mapped `metadata.event_type` to `REGISTRY_CREATION`.  
\- If `event.type` is `Registry Value ModIfied` mapped `metadata.event_type` to `REGISTRY_MODIfICATION`.  
\- If `event.type` is `Registry Value Create` mapped `metadata.event_type` to `REGISTRY_CREATION`.  
\- If `event.type` is `Registry Value Delete` mapped `metadata.event_type` to `REGISTRY_DELETION`.  
\- If `event.type` is `Behavioral Indicators` mapped `metadata.event_type` to `SCAN_UNCATEGORIZED`.  
\- If `event.type` is `Module Load` mapped `metadata.event_type` to `PROCESS_MODULE_LOAD`.  
\- If `event.type` is `Threat Intelligence Indicators` mapped `metadata.event_type` to `SCAN_UNCATEGORIZED`.  
\- If `event.type` is `Named Pipe Creation` mapped `metadata.event_type` to `PROCESS_UNCATEGORIZED`.  
\- If `event.type` is `Named Pipe Connection` mapped `metadata.event_type` to `PROCESS_UNCATEGORIZED`.  
\- If `event.type` is `Driver Load` mapped `metadata.event_type` to `PROCESS_MODULE_LOAD`.   
2022-11-30 |  Enhancement  
\- Enhanced the parser to support the logs ingested in version V2 by mapping following fields.  
\- Mapped `account.id` to `metadata.product_deployment_id`.  
\- Mapped `agent.uuid` to `principal.asset.asset_id`.  
\- Mapped `dst.ip.address` to `target.ip`.  
\- Mapped `src.ip.address` to `principal.ip`.  
\- Mapped `src.process.parent.image.sha1` to `principal.process.parent_process.file.sha1`.  
\- Mapped `src.process.parent.image.sha256` to `principal.process.parent_process.file.sha256`.  
\- Mapped `src.process.parent.image.path` to `principal.process.parent_process.file.full_path`.  
\- Mapped `src.process.parent.cmdline` to `principal.process.parent_process.command_line`.  
\- Mapped `src.process.parent.image.md5` to `principal.process.parent_process.file.md5`.  
\- Mapped `src.process.parent.pid` to `principal.process.parent_process.pid`.  
\- Mapped `src.process.image.sha1` to `principal.process.file.sha1`.  
\- Mapped `src.process.image.md5` to `principal.process.file.md5`.  
\- Mapped `src.process.pid` to `principal.process.pid`.  
\- Mapped `src.process.cmdline` to `principal.process.command_line`.  
\- Mapped `src.process.image.path` to `principal.process.file.full_path`.  
\- Mapped `src.process.image.sha256` to `principal.process.file.sha256`.  
\- Mapped `src.process.user` to `principal.user.user_display_name`.  
\- Mapped `src.process.uid` to `principal.user.userid`.  
\- Mapped `src.process.storyline.id` to `principal.process.product_specific_process_id`.  
\- Mapped `src.process.parent.storyline.id` to `principal.process.parent_process.product_specific_process_id`.  
\- Mapped `mgmt.url` to `target.url`.  
\- Mapped `site.id` to `principal.namespace`.  
\- Mapped `src.port.number` to `principal.port`.  
\- Mapped `dst.port.number` to `target.port`.  
\- Mapped `event_data.id` to `metadata.product_log_id`.   
2022-10-11 |  Enhancement  
\- Mapped `threatClassification` to `security_result.category_details`.  
\- Mapped `threatConfidenceLevel` and `threatMitigationStatus` to `security_result.detection_fields`.  
\- Mapped `Location` to `principal.location.name`.  
\- Mapped `data.filePath` to `principal.process.parent_process.file.full_path`.  
\- Updated the mapping (CAT Value)security_result.category_details to metadata.product_event_type   
2022-09-01 |  Enhancement  
\- Changed metadata.product_name from SentinelOne to Singularity.  
\- Mapped `event.regValue.key.value` to `target.registry.registry_value_name`.  
\- Mapped `principal_userid` to `principal.user.userid`.  
\- Mapped `principal_domain` to `principal.administrative_domain`.  
\- Mapped `threatInfo.threatId` to `security_result.threat_id`  
\- Mapped `threatInfo.identifiedAt` to `metadata.event_timestamp`.  
\- Mapped `threatInfo.threatId` to `metadata.product_log_id`.  
\- Mapped `security_result.alert_state` to `ALERTING`.  
\- Mapped `threatInfo.maliciousProcessArguments` to `security_result.description`.  
\- Mapped `threatInfo.threatName` to `security_result.threat_name`.  
\- Mapped `threatInfo.classification` to `security_result.category_details`.  
\- Mapped `security_result.category` to `SOFTWARE_MALICIOUS` where threatInfo.classification is malicious else to `NETWORK_SUSPICIOUS`.  
\- Mapped `security_result.action` to `ALLOW` where threatInfo.mitigationStatus is mitigated else to `BLOCK`.  
\- Mapped `threatInfo.mitigationStatus` to `security_result.action_details`.  
\- Mapped `threatInfo.classification threatInfo.classificationSource threatInfo.analystVerdictDescription threatInfo.threatName` to `security_result.summary`.  
\- Mapped `threatInfo.createdAt` to `metadata.collected_timestamp`.  
\- Mapped `agentRealtimeInfo.accountId` to `metadata.product_deployment_id`.  
\- Mapped `agentRealtimeInfo.agentVersion` to `metadata.product_version`.  
\- Mapped `indicator.category` to `detection_fields.key` and `indicator.description` to `detection_fields.value`.  
\- Mapped `detectionEngines.key` to `detection_fields.key` and `detectionEngines.title` to `detection_fields.value`.  
\- Mapped `metadata.event_type` to `SCAN_UNCATEGORIZED` where `meta.computerName` is not null.   
2022-07-21 |  Enhancement  
\- Mapped event.source.executable.hashes.md5 to principal.process.file.md5.  
\- Mapped event.source.executable.hashes.sha256 to principal.process.file.sha256.  
\- Mapped event.source.executable.hashes.sha1 to principal.process.file.sha1.  
\- Mapped event.source.fullPid.pid to principal.process.pid.  
\- Mapped event.source.user.name to principal.user.userid.  
\- Mapped meta.agentVersion to metadata.product_version.  
\- Mapped event.appName to target.application.  
\- Mapped event.contentHash.sha256 to target.process.file.sha256.  
\- Mapped event.source.commandLine to target.process.command_line.  
\- Mapped event.decodedContent to target.labels.  
\- Changed metadata.description from scripts to Command Scripts where event.type is scripts.  
\- Mapped vendor to metadata.vendor_name.  
\- Mapped data.fileContentHash to target.process.file.md5.  
\- Mapped data.ipAddress to principal.ip.  
\- Mapped activityUuid to target.asset.product_object_id.  
\- Mapped agentId to metadata.product_deployment_id.  
\- Added email verification for user_email prior to mapping it to principal.user.email_addresses, if failed mapped it to principal.user.userid.  
\- Mapped sourceIpAddresses to principal.ip.  
\- Mapped accountName to principal.administrative_domain.  
\- Mapped activityId to additional.fields.   
2022-07-15 |  Enhancement - Parsed the new logs with JSON format and mapped the following new fields:-  
\- `metadata.product_name` to `SENTINEL_ONE`.  
\- `sourceParentProcessMd5` to `principal.process.parent_process.file.md5`.  
\- `sourceParentProcessPath` to `principal.process.parent_process.file.full_path`.  
\- `sourceParentProcessPid` to `principal.process.parent_process.pid`.  
\- `sourceParentProcessSha1` to `principal.process.parent_process.file.sha1`.  
\- `sourceParentProcessSha256` to `principal.process.parent_process.file.sha256`.  
\- `sourceParentProcessCmdArgs` to `principal.process.parent_process.command_line`.  
\- `sourceProcessCmdArgs` to `principal.process.command_line`.  
\- `sourceProcessMd5` to `principal.process.file.md5`.  
\- `sourceProcessPid` to `principal.process.pid`.  
\- `sourceProcessSha1` to `principal.process.file.sha1`.  
\- `sourceProcessSha256` to `principal.process.file.sha256`.  
\- `sourceProcessPath` to `principal.process.file.full_path`.  
\- `tgtFilePath` to `target.file.full_path`.  
\- `tgtFileHashSha256` to `target.file.sha256`.  
\- `tgtFileHashSha1` to `target.file.sha1`.  
\- `tgtProcUid` to `target.process.product_specific_process_id`.  
\- `tgtProcCmdLine` to `target.process.command_line`.  
\- `tgtProcPid` to `target.process.pid`.  
\- `tgtProcName` to `target.application`.  
\- `dstIp` to `target.ip`.  
\- `srcIp` to `principal.ip`.  
\- `dstPort` to `target.port`.  
\- `srcPort` to `principal.port`.  
\- `origAgentName` to `principal.hostname`.  
\- `agentIpV4` to `principal.ip`.  
\- `groupId` to `principal.user.group_identifiers`.  
\- `groupName` to `principal.user.group_display_name`.  
\- `origAgentVersion` to `principal.asset.software.version`.  
\- `origAgentOsFamily` to `principal.platform`.  
\- `origAgentOsName` to principal.asset.software.name".  
\- `event_type` to `FILE_MODIFICATION` when sourceEventType = FILEMODIFICATION.  
\- `event_type` to `FILE_DELETION` when sourceEventType = FILEDELETION.  
\- `event_type` to `PROCESS_LAUNCH` when sourceEventType = PROCESSCREATION.  
\- `event_type` to `NETWORK_CONNECTION` when sourceEventType = TCPV4.   
2022-06-13 |  Enhancement  
\- for [event][type] == `fileCreation` and [event][type] == `fileDeletion`  
\- Mapped `event.targetFile.path` to `target.file.full_path`.  
\- Mapped `event.targetFile.hashes.md5` to `target.process.file.md5`.  
\- Mapped `event.targetFile.hashes.sha1` to `target.process.file.sha1`.  
\- Mapped `event.targetFile.hashes.sha256` to `target.process.file.sha256`.  
\- for [event][type] == `fileModification`  
\- Mapped `event.file.path` to `target.file.full_path`.  
\- Mapped `event.file.hashes.md5` to `target.process.file.md5`.  
\- Mapped `event.file.hashes.sha1` to `target.process.file.sha1`.  
\- Mapped `event.file.hashes.sha256` to `target.process.file.sha256`.   
2022-04-18 |  \- Enhanced the parser to handle all the unparsed raw logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
