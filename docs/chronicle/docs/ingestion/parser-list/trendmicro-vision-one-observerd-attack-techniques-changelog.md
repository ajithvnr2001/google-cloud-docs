---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-observerd-attack-techniques-changelog/
title: Change log for TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:37:33.165494+00:00
---

# Change log for TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-observerd-attack-techniques-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_OBSERVERD_ATTACK_TECHNIQUES

Date | Changes  
---|---  
2026-10-05 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `detectedDateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `ingestedDateTime` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `endpoint.endpointName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `fl.riskLevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `fl.mitreTacticIds` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `fl.mitreTechniqueIds` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source`, `customer_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Changed mapping from `endpoint.guid` (prefixed with `GUID: `) with `endpoint.guid`, `endpoint.agentGuid`, `detail.endpointGuid`, and `detail.endpointGUID` (all now prefixed with `agentGuid:`) raw log fields with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.   
2026-09-08 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.file.full_path`: Removed mapping of `objectFilePath` from `event.idm.read_only_udm.target.process.file.full_path` UDM field when `detail.eventId` values are not present in `TELEMETRY_PROCESS`, `TELEMETRY_BM` and `TELEMETRY_AMSI` in order to introduce a more accurate mapping.  
\- `event.idm.read_only_udm.target.file.full_path`: Mapped `objectFilePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `objectCmd` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Newly mapped `detail.objectRegistryKeyHandle` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_name`: Newly mapped `detail.objectRegistryValue` raw log field with `event.idm.read_only_udm.target.registry.registry_value_name` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_data`: Newly mapped `detail.objectRegistryData` raw log field with `event.idm.read_only_udm.target.registry.registry_value_data` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `detail.endpointHostName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH` when `detail.eventId` is `TELEMETRY_PROCESS` and target process file details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_UNCATEGORIZED` when `detail.eventId` is `TELEMETRY_BM` or `TELEMETRY_AMSI` and target process file details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_CREATION` when `detail.eventId` is `TELEMETRY_FILE` and `detail.eventSubId` is `TELEMETRY_FILE_CREATE` and target file details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_DELETION` when `detail.eventId` is `TELEMETRY_FILE` and `detail.eventSubId` is `TELEMETRY_FILE_DELETE` and target file details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_MODIFICATION` when `detail.eventId` is `TELEMETRY_FILE` and target file details are present.   
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `highlight.src` from `event.idm.read_only_udm.security_result.detection_fields` UDM field to map to a more accurate UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `highlight.src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped highlight.dst raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `highlight.dpt` from `event.idm.read_only_udm.security_result.detection_fields` UDM field to map to a more accurate UDM field.  
\- `event.idm.read_only_udm.target.port`: Mapped `highlight.dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `detail.processCmd` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detail.objectHostname` from `event.idm.read_only_udm.additional.fields` UDM field to map to a more accurate UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `detail.objectHostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detail.srcCountry` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `detail.parentCmd` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when target machine data and principal machine data is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when user data,target machine data and principal machine data are not present.   
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detail.spt` from `event.idm.read_only_udm.additional.fields` UDM field since `detail.spt` represents the port number of the principal.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `detail.spt` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `detail.objectFilePath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field when `highlightedObjects` does not contain `objectFilePath` values.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `detail.processFilePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `highlightedObjects` does not contain `processFilePath` values.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail.logonUser` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `detail.processFileHashId` from `event.idm.read_only_udm.additional.fields` UDM field to map to a more accurate UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detail.processFileHashId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added gsub transformations for `objectFileHashId`, `objectHashId`, `eventHashId`, and `processFileHashId` to ensure they are treated as strings before JSON parsing, this ensures large numerical values are not truncated.   
2025-10-10 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Removed mappings of `eventId`, `logReceivedTime`, `pver`, `uuid`, `firstSeen`, `lastSeen`, `groupId`, `parentFileModifiedTime`, `parentSessionId`, `processFileModifiedTime`, `parentLaunchTime` , `processLaunchTime`, `objectLaunchTime`, `osDescription` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `fl.type`, `highlight.riskLevel` and `highlight.master` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field (Key: `Type`).  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `detail.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `detail.logReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `detail.pver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `detail.processUserDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.asset.type: Newly mapped `detail.entityType` raw log field with `event.idm.read_only_udm.principal.asset.type` UDM field.  
\- event.idm.read_only_udm.principal.user.managers: Newly mapped `detail.parentUser` raw log field with `event.idm.read_only_udm.principal.user.managers.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.managers.attribute.roles: Newly mapped `detail.parentUser` raw log field with `event.idm.read_only_udm.principal.user.managers.attribute.roles` UDM field (fixed role name `Parent`).  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `detail.firstSeen` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `detail.lastSeen` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.target.file.signature_info.sigcheck.signers: Newly mapped `detail.objectSigner` raw log field with `event.idm.read_only_udm.target.file.signature_info.sigcheck.signers.name` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.signature_info.sigcheck.signers: Newly mapped `detail.parentSigner` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.signature_info.sigcheck.signers.name` UDM field.  
\- event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers: Newly mapped `detail.processSigner` raw log field with `event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers.name` UDM field.  
\- event.idm.read_only_udm.target.file.signature_info.sigcheck.signers: Newly mapped `detail.objectSignerValid` raw log field with `event.idm.read_only_udm.target.file.signature_info.sigcheck.signers.status` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.signature_info.sigcheck.signers: Newly mapped `detail.parentSignerValid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.signature_info.sigcheck.signers.status` UDM field.  
\- event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers: Newly mapped `detail.processSignerValid` raw log field with `event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers.status` UDM field.  
\- event.idm.read_only_udm.principal.process.integrity_level_rid: Newly mapped `detail.integrityLevel` raw log field with `event.idm.read_only_udm.principal.process.integrity_level_rid` UDM field.  
\- event.idm.read_only_udm.target.process.integrity_level_rid: Newly mapped `detail.objectIntegrityLevel` raw log field with `event.idm.read_only_udm.target.process.integrity_level_rid` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid: Newly mapped `detail.parentIntegrityLevel` raw log field with `event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid` UDM field.  
\- event.idm.read_only_udm.target.file.last_modification_time: Newly mapped `detail.objectFileModifiedTime` raw log field with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- event.idm.read_only_udm.principal.process.file.last_modification_time: Newly mapped `detail.processFileModifiedTime` raw log field with `event.idm.read_only_udm.principal.process.file.last_modification_time` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.last_modification_time: Newly mapped `detail.parentFileModifiedTime` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.last_modification_time` UDM field.  
\- event.idm.read_only_udm.target.file.create_time: Newly mapped `detail.objectLaunchTime` raw log field with `event.idm.read_only_udm.target.file.create_time` UDM field.  
\- event.idm.read_only_udm.principal.process.file.create_time: Newly mapped `detail.processLaunchTime` raw log field with `event.idm.read_only_udm.principal.process.file.create_time` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.create_time: Newly mapped `detail.parentLaunchTime` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.create_time` UDM field.  
\- event.idm.read_only_udm.network.parent_session_id: Newly mapped `detail.parentSessionId` raw log field with `event.idm.read_only_udm.network.parent_session_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `detail.eventId` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.platform_patch_level: Newly mapped `detail.osDescription` raw log field with `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped `detail.groupId` raw log field with `event.idm.read_only_udm.target.user.group_identifiers` UDM field.   
2025-07-25 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped endpoint.guid raw log field to event.idm.read_only_udm.principal.asset.asset_id.  
\- event.idm.read_only_udm.security_result.rule_version: Newly mapped fl.unique_id raw log field to event.idm.read_only_udm.security_result.rule_version.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped logonUser raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped processUser raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped userDomain raw log field to event.idm.read_only_udm.principal.user.group_identifiers.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped processUserGroupSids raw log field to event.idm.read_only_udm.principal.user.group_identifiers.  
\- event.idm.read_only_udm.principal.mac: Newly mapped endpointMacAddress raw log field to event.idm.read_only_udm.principal.mac.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped endpointMacAddress raw log field to event.idm.read_only_udm.principal.asset.mac.  
\- event.idm.read_only_udm.principal.ip: Newly mapped endpointIp raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped endpointIp raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped objectUserGroupSids raw log field to event.idm.read_only_udm.target.user.group_identifiers.  
\- event.idm.read_only_udm.target.user.group_identifiers: Newly mapped objectUserDomain raw log field to event.idm.read_only_udm.target.user.group_identifiers.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped processPid raw log field to event.idm.read_only_udm.principal.process.pid.  
\- event.idm.read_only_udm.principal.process.file.md5: Newly mapped processFileHashMd5 raw log field to event.idm.read_only_udm.principal.process.file.md5.  
\- event.idm.read_only_udm.principal.process.file.sha1: Newly mapped processFileHashSha1 raw log field to event.idm.read_only_udm.principal.process.file.sha1.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped processFileHashSha256 raw log field to event.idm.read_only_udm.principal.process.file.sha256.  
\- event.idm.read_only_udm.principal.process.file.size: Newly mapped processFileSize raw log field to event.idm.read_only_udm.principal.process.file.size.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped processName raw log field to event.idm.read_only_udm.principal.process.file.names.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped processFileOriginalName raw log field to event.idm.read_only_udm.principal.process.file.names.  
\- event.idm.read_only_udm.principal.process.file.first_seen_time: Newly mapped processFileCreation raw log field to event.idm.read_only_udm.principal.process.file.first_seen_time.  
\- event.idm.read_only_udm.principal.process.integrity_level_rid: Newly mapped integrityLevel raw log field to event.idm.read_only_udm.principal.process.integrity_level_rid.  
\- event.idm.read_only_udm.principal.process.parent_process.pid: Newly mapped parentPid raw log field to event.idm.read_only_udm.principal.process.parent_process.pid.  
\- event.idm.read_only_udm.principal.process.parent_process.file.md5: Newly mapped parentFileHashMd5 raw log field to event.idm.read_only_udm.principal.process.parent_process.file.md5.  
\- event.idm.read_only_udm.principal.process.parent_process.file.sha1: Newly mapped parentFileHashSha1 raw log field to event.idm.read_only_udm.principal.process.parent_process.file.sha1.  
\- event.idm.read_only_udm.principal.process.parent_process.file.sha256: Newly mapped parentFileHashSha256 raw log field to event.idm.read_only_udm.principal.process.parent_process.file.sha256.  
\- event.idm.read_only_udm.principal.process.parent_process.file.full_path: Newly mapped parentFilePath raw log field to event.idm.read_only_udm.principal.process.parent_process.file.full_path.  
\- event.idm.read_only_udm.principal.process.parent_process.file.size: Newly mapped parentFileSize raw log field to event.idm.read_only_udm.principal.process.parent_process.file.size.  
\- event.idm.read_only_udm.principal.process.parent_process.file.names: Newly mapped parentName raw log field to event.idm.read_only_udm.principal.process.parent_process.file.names.  
\- event.idm.read_only_udm.principal.process.parent_process.file.names: Newly mapped parentFileOriginalName raw log field to event.idm.read_only_udm.principal.process.parent_process.file.names.  
\- event.idm.read_only_udm.principal.process.parent_process.file.first_seen_time: Newly mapped parentFileCreation raw log field to event.idm.read_only_udm.principal.process.parent_process.file.first_seen_time.  
\- event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid: Newly mapped parentIntegrityLevel raw log field to event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped objectPid raw log field to event.idm.read_only_udm.target.process.pid.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped objectUser raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.process.file.md5: Newly mapped objectFileHashMd5 raw log field to event.idm.read_only_udm.target.process.file.md5.  
\- event.idm.read_only_udm.target.process.file.sha1: Newly mapped objectFileHashSha1 raw log field to event.idm.read_only_udm.target.process.file.sha1.  
\- event.idm.read_only_udm.target.process.file.sha256: Newly mapped objectFileHashSha256 raw log field to event.idm.read_only_udm.target.process.file.sha256.  
\- event.idm.read_only_udm.target.process.file.names: Newly mapped objectName raw log field to event.idm.read_only_udm.target.process.file.names.  
\- event.idm.read_only_udm.target.process.file.names: Newly mapped objectFileOriginalName raw log field to event.idm.read_only_udm.target.process.file.names.  
\- event.idm.read_only_udm.target.process.file.first_seen_time: Newly mapped objectFileCreation raw log field to event.idm.read_only_udm.target.process.file.first_seen_time.  
\- event.idm.read_only_udm.target.file.size: Newly mapped objectFileSize raw log field to event.idm.read_only_udm.target.file.size.  
\- event.idm.read_only_udm.target.process.integrity_level_rid: Newly mapped objectIntegrityLevel raw log field to event.idm.read_only_udm.target.process.integrity_level_rid.  
\- event.idm.read_only_udm.target.registry.registry_key: Newly mapped objectRegistryKeyHandle raw log field to event.idm.read_only_udm.target.registry.registry_key.  
\- event.idm.read_only_udm.target.registry.registry_value_name: Newly mapped objectRegistryValue raw log field to event.idm.read_only_udm.target.registry.registry_value_name.  
\- event.idm.read_only_udm.target.registry.registry_value_data: Newly mapped objectRegistryData raw log field to event.idm.read_only_udm.target.registry.registry_value_data.  
\- event.idm.read_only_udm.principal.platform: Newly mapped osName raw log field to event.idm.read_only_udm.principal.platform.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped osVer raw log field to event.idm.read_only_udm.principal.platform_version.  
\- event.idm.read_only_udm.network.session_id: Newly mapped objectSessionId raw log field to event.idm.read_only_udm.network.session_id.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of highlight.value from event.idm.read_only_udm.security_result.detection_fields where highlight.field is processCmd.  
\- event.idm.read_only_udm.principal.process.command_line: Mapped highlight.value raw log field to event.idm.read_only_udm.principal.process.command_line where highlight.field is processCmd.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of highlight.value from event.idm.read_only_udm.security_result.detection_fields where highlight.field is objectCmd.  
\- event.idm.read_only_udm.target.process.command_line: Mapped highlight.value raw log field to event.idm.read_only_udm.target.process.command_line where highlight.field is objectCmd.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of highlight.value from event.idm.read_only_udm.security_result.detection_fields where highlight.field is parentCmd.  
\- event.idm.read_only_udm.principal.process.parent_process.command_line: Mapped highlight.value raw log field to event.idm.read_only_udm.principal.process.parent_process.command_line where highlight.field is parentCmd.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of highlight.value from event.idm.read_only_udm.security_result.detection_fields where highlight.field is objectFilePath.  
\- event.idm.read_only_udm.target.process.file.full_path: Mapped highlight.value raw log field to event.idm.read_only_udm.target.process.file.full_path where highlight.field is objectFilePath.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of highlight.value from event.idm.read_only_udm.security_result.detection_fields where highlight.field is processFilePath.  
\- event.idm.read_only_udm.principal.process.file.full_path: Mapped highlight.value raw log field to event.idm.read_only_udm.principal.process.file.full_path where highlight.field is processFilePath.   
2025-04-07 |  \- Newly created parser.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `endpoint.name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `endpoint.ips` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `entityName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `entityType` is `identity`.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `filters.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `filters.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `filters.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `filters.level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `filters.tactics` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `filters.techniques` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `filters.highlightedObjects.field` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `filters.highlightedObjects.type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `filters.highlightedObjects.value` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
