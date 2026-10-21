---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-dv-changelog/
title: Change log for SENTINEL_DV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:36:17.890980+00:00
---

# Change log for SENTINEL_DV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinel-dv-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENTINEL_DV

Date | Changes  
---|---  
2026-04-23 |  Enhancement:  
\- Removed `has_target_process` from rename block and added to replace block. Because of flakiness issue.   
2026-04-13 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dv_event.id`, `process.unique.key`, `src.process.dnsCount`, `src.process.image.binaryIsExecutable`, `src.process.image.description`, `src.process.image.extension`, `src.process.image.internalName`, `src.process.image.productName`, `src.process.image.productVersion`, `src.process.name`, `src.process.netConnCount`, `src.process.netConnInCount`, `src.process.netConnOutCount`, `src.process.parent.displayName`, `src.process.parent.image.extension`, `src.process.parent.image.signature.isValid`, `src.process.parent.image.type`, `src.process.parent.image.uid`, `src.process.parent.integrityLevel`, `src.process.parent.isNative64Bit`, `src.process.parent.isStorylineRoot`, `src.process.parent.name`, `src.process.parent.sessionId`, `src.process.parent.signedStatus`, `src.process.parent.startTime`, `src.process.parent.subsystem`, `src.process.parent.user`, `src.process.publisher`, `src.process.sessionId`, `src.process.startTime`, and `src.process.verifiedStatus` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `meta.event.name` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `endpoint.os` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `os.name` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `src.port.number` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `src.process.image.originalFileName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.size`: Newly mapped `src.process.parent.image.size` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.size` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `group.id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `src.process.userSid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `dv_event.network.connectionStatus` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `src.process.indicatorRansomwareCount`, `src.process.crossProcessDupRemoteProcessHandleCount`, `src.process.crossProcessOpenProcessCount`, `src.process.indicatorInjectionCount`, `src.process.crossProcessThreadCreateCount`, `src.process.crossProcessCount`, `src.process.tgtFileModificationCount`, `src.process.crossProcessDupThreadHandleCount`, `src.process.tgtFileDeletionCount`, `src.process.indicatorPostExploitationCount`, `src.process.indicatorPersistenceCount`, `src.process.registryChangeCount`, `src.process.crossProcessOutOfStorylineCount`, and `src.process.indicatorReconnaissanceCount` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst.port.number` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the event_type to GENERIC_EVENT for logs that do not contain the required data.   
2025-10-14 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `metaEventName`, `objectType`, `publisher`, `srcProcVerifiedStatus`, `srcProcParentStorylineId`, `id`, `verifiedStatus` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `accountId` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `traceId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `agentVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `agentDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `processName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `agentIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `agentUuid` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.asset.type: Newly mapped `agentMachineType` raw log field with `event.idm.read_only_udm.principal.asset.type` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `agentId` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `agentName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `agentIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `siteName` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.namespace: Newly mapped `siteId` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `agentOs` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `srcProcCmdLine` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.process.file.create_time: Newly mapped `processStartTime` raw log field with `event.idm.read_only_udm.principal.process.file.create_time` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `srcProcImagePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha1: Newly mapped `srcProcImageSha1` raw log field with `event.idm.read_only_udm.principal.process.file.sha1` UDM field.  
\- event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers: Newly mapped `srcProcSigned`, `signer`, `srcProcSignedStatus` raw log fields with `event.idm.read_only_udm.principal.process.file.signature_info.sigcheck.signers` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.create_time: Newly mapped `parentProcessStartTime` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.create_time` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.full_path: Newly mapped `srcProcParentImagePath` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.sha1: Newly mapped `srcProcParentImageSha1` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha1` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.product_specific_process_id: Newly mapped `srcProcParentUid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.product_specific_process_id` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `srcProcPid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.process.product_specific_process_id: Newly mapped `srcProcUid` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `agentGroupId`, `agentInfected`, `agentIsActive`, `agentIsDecommissioned`, `processIntegrityLevel`, `agentNetworkStatus`, `isAgentVersionFullySupportedForPg`, `isAgentVersionFullySupportedForPgMessage`, `srcProcIntegrityLevel`, `parentProcessName`,`srcProcPublisher`, and `srcProcParentName` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `srcProcUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `relatedToThreat`, `retentionPeriod`, `storyline`, `trueContext`, `parentProcessUniqueKey`, `processGroupId`, `processUniqueKey`, `user`, `srcProcStorylineId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `tgtProcName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.platform: Newly mapped `endpointOs` raw log field with `event.idm.read_only_udm.target.platform` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `tgtProcCmdLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.target.process.file.create_time: Newly mapped `tgtProcStartTime` raw log field with `event.idm.read_only_udm.target.process.file.create_time` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `tgtProcImagePath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.process.file.sha1: Newly mapped `tgtProcImageSha1` raw log field with `event.idm.read_only_udm.target.process.file.sha1` UDM field.  
\- event.idm.read_only_udm.target.process.file.sha256: Newly mapped `tgtProcImageSha256` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.target.process.file.signature_info.sigcheck.signers: Newly mapped `tgtProcSigned`, `tgtProcSignedStatus` raw log fields with `event.idm.read_only_udm.target.process.file.signature_info.sigcheck.signers` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `tgtProcPid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.product_specific_process_id: Newly mapped `tgtProcUid` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `tgtProcStorylineId`, `tgtProcIntegrityLevel` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2023-09-06 |  Enhancement -  
\- Modified mapping of `tgt.process.storyline.id` from `target.process.product_specific_process_id` to `security_result.about.resource.attribute.labels`.  
\- Modified mapping of `src.process.storyline.id` from `principal.process.product_specific_process_id` to `security_result.about.resource.attribute.labels`.  
\- Modified mapping of `src.process.parent.storyline.id` from `principal.parent.process.product_specific_process_id` to `security_result.about.resource.attribute.labels`.   
2023-07-31 |  Enhancement -  
\- Handled logs containing `XML` data.   
2023-04-09 |  Enhancement -  
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
2023-02-13 |  Enhancement -  
\- Mapped `endpoint.os` to `principal.platform`.  
\- Mapped `endpoint.name` to `target.hostname`.  
\- Mapped `src.process.pid` to `principal.process.pid`.  
\- Mapped `src.process.cmdline` to `principal.process.command_line`.  
\- Mapped `src.process.image.path` to `principal.process.file.full_path`.  
\- Mapped `src.process.image.sha1` to `principal.process.file.sha1`.  
\- Mapped `src.process.eUserUid` to `metadata.ingestion_labels`.  
\- Mapped `src.process.lUserUid` to `metadata.ingestion_labels`.  
\- Mapped `src.process.uid` to `principal.user.userid`.  
\- Mapped `src.process.displayName` to `principal.user.user_display_name`.  
\- Mapped `src.process.isRedirectCmdProcessor`, `src.process.isNative64Bit`, `src.process.isStorylineRoot`, `src.process.signedStatus`, `src.file.isSigned`, `src.process.subsystem`, `src.process.integrityLevel`, `src.process.tgtFileCreationCount`, `src.process.childProcCount`, `src.process.indicatorBootConfigurationUpdateCount`, `src.process.indicatorEvasionCount`, `src.process.indicatorExploitationCount`, `src.process.indicatorGeneralCount`, `src.process.indicatorInfostealerCount`, `src.process.moduleCount` to `principal.resource.attribute.labels`.  
\- Mapped `src.process.image.md5` to `principal.process.file.md5`.  
\- Mapped `agent.uuid` to `principal.asset.asset_id`.  
\- Mapped `agent.version` to `metadata.product_version`.  
\- Mapped `site.id` to `principal.namespace`.  
\- Mapped `site.name` to `principal.location.name`.  
\- Mapped `trace.id` to `metadata.product_log_id`.  
\- Mapped `dataSource.category` to `security_result.category_details`.  
\- Mapped `packet.id` to `about.resource.attribute.labels`.  
\- Mapped `mgmt.url`, `endpoint.type` to `metadata.url_back_to_product`.  
\- Mapped `tgt.process.image.sha1` to `target.process.file.sha1`.  
\- Mapped `tgt.process.image.path` to `target.process.file.full_path`.  
\- Mapped `tgt.process.pid` to `target.process.pid`.  
\- Mapped `tgt.process.uid` to `target.user.userid`.  
\- Mapped `tgt.process.cmdline` to `target.process.command_line`.  
\- Mapped `tgt.process.displayName` to `target.user.user_display_name`.  
\- Mapped `tgt.process.image.md5` to `target.process.file.md5`.  
\- Mapped `src.process.parent.image.sha256` to `principal.process.file.sha256`.  
\- Mapped `tgt.process.image.sha256` to `target.process.file.sha256`.  
\- Mapped `tgt.process.sessionId` to `network.session_id`.  
\- Mapped `tgt.process.storyline.id` to `target.process.product_specific_process_id`.  
\- Mapped `tgt.process.isRedirectCmdProcessor`, `tgt.process.isNative64Bit`, `tgt.process.isStorylineRoot`, `tgt.process.signedStatus`, `tgt.file.isSigned`, `tgt.process.subsystem`, `tgt.process.integrityLevel`, `tgt.process.publisher` to `target.resource.attribute.labels`.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.   
2022-09-09 |  Enhancement - Undropped the logs with `event_type` = null.  
\- Provided null checks for `meta.os_version`, `meta.os_name`, `meta.uuid`, `meta.computer_name`, `meta.os_revision`.  
\- Reduced the size of `*.targetFile.hashes.sha1` and `*.source.executable.hashes.sha1` to 64 bytes when exceeding the limit of 64 bytes.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
