---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-detections-changelog/
title: Change log for TRENDMICRO_VISION_ONE_DETECTIONS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:30.877075+00:00
---

# Change log for TRENDMICRO_VISION_ONE_DETECTIONS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-detections-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_DETECTIONS

Date | Changes  
---|---  
2026-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `entityType`, `entityName`, `detail.interestedIpCountry`, `detail.interestedIpIsp`, `detail.engVer`, `detail.eventId`, `detail.processChain.process_hash_id`, `detail.processChain.process_signer_valid`, `detail.processChain.process_signer`, `detail.processChain.process_sub_true_type`, `detail.processChain.process_true_type`, `detail.processChain.integrity_level`, `detail.processChain.process_name`, `detail.processChain.process_launch_time`, `detail.mpname`, `detail.mpver`, `detail.productCode`, `detail.eventSourceType`, `detail.filePath`, `detail.logKey`, `detail.objectFileRemoteAccess`, `detail.objectFileSize`, `detail.objectHashId`, `detail.objectTrueType`, `detail.objectType`, `detail.processHashId`, `detail.rt_utc`, `detail.eventTimeDT`, `detail.rtDate`, `detail.rtHour`, `detail.rtWeekDay`, `detail.ruleIdStr` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `filter_obj.id`, `filter_obj.name`, `filter_obj.unique_id`, `filter_obj.type`, `h_value`, `detail.detectionAggressivenessLevel`, `detail.engType`, `detail.engineOperation`, `detail.firstAct`, `detail.firstActResult`, `detail.malType`, `detail.patVer`, `detail.scanType`, `detail.secondAct`, `detail.secondActResult`, `detail.majorVirusType`, `filter_obj.description`, `filter_obj.level` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `detail.pname` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `detail.pver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `detail.processPid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.file.first_seen_time`: Newly mapped `detail.fileCreation` raw log field with `event.idm.read_only_udm.target.file.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `detail.endpointHostName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `detail.interestedHost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `detail.objectFilePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.last_modification_time`: Newly mapped `detail.objectLastModifyTime` raw log field with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `detail.mDeviceGUID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `detail.malName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `endpoint.ips` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `detail.interestedIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.src.file.names`: Newly mapped `detail.fileName` raw log field with `event.idm.read_only_udm.src.file.names` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `detail.tags` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.about.process.file.size`: Newly mapped `detail.processChainInfo.process_file_size` raw log field with `event.idm.read_only_udm.about.process.file.size` UDM field.  
\- `event.idm.read_only_udm.about.process.file.full_path`: Newly mapped `detail.processChainInfo.process_file_path` raw log field with `event.idm.read_only_udm.about.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.process.pid`: Newly mapped `detail.processChainInfo.process_pid` raw log field with `event.idm.read_only_udm.about.process.pid` UDM field.  
\- `event.idm.read_only_udm.about.process.file.sha256`: Newly mapped `detail.processChainInfo.process_file_hash_sha256` raw log field with `event.idm.read_only_udm.about.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.about.process.command_line`: Newly mapped `detail.processChainInfo.process_cmd` raw log field with `event.idm.read_only_udm.about.process.command_line` UDM field.  
\- `event.idm.read_only_udm.about.process.file.sha1`: Newly mapped `detail.processChainInfo.process_file_hash_sha1` raw log field with `event.idm.read_only_udm.about.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.about.process.file.md5`: Newly mapped `detail.processChainInfo.process_file_hash_md5` raw log field with `event.idm.read_only_udm.about.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.src.file.sha1`: Newly mapped `detail.fileHash` raw log field with `event.idm.read_only_udm.src.file.sha1` UDM field.  
\- `event.idm.read_only_udm.src.file.full_path`: Newly mapped `detail.filePathName` raw log field with `event.idm.read_only_udm.src.file.full_path` UDM field.  
\- `event.idm.read_only_udm.src.asset.asset_id`: Newly mapped `detail.senderGUID` raw log field with `event.idm.read_only_udm.src.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `filter_obj.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `filter_obj.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `filter_obj.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `f_technique` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `f_tactic` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: If `eventTime` is empty, updated the value of `event.idm.read_only_udm.metadata.event_timestamp` to `detectionTime`.  
\- `event.idm.read_only_udm.principal.domain.name`: Newly mapped `detail.domainName` raw log field with `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.network_domain`: Newly mapped `detail.domainName` raw log field with `event.idm.read_only_udm.principal.asset.network_domain` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `detail.logReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `detail.filterRiskLevel` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `detail.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `detail.uuid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `detail.groupId` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.   
2025-11-04 |  \- event.idm.read_only_udm.security_result.category_details: Newly mapped `urlCat` raw log field(s) with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suid` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `app` raw log field(s) with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `direction` raw log field(s) with `event.idm.read_only_udm.network.direction` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rating`, `aggregatedCount`, `blocking` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `cccaRiskLevel`, `cccaDetectionSource` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Set a flag variable `has_principal` to true if `tmpUser1` is not null and is a valid email thus event_type is set to `USER_UNCATEGORIZED`.   
2025-09-10 |  \- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly mapped `groupId` raw log field(s) with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `samUser` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `malDst` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `malDst` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.file.last_modification_time: Newly mapped `objectLastModifyTime` raw log field(s) with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `tags` raw log field(s) with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `actResult` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.about.file.sha256: Newly mapped `attachmentFileHashs`, `attachmentFileHashes` raw log field(s) with `event.idm.read_only_udm.about.file.sha256` UDM field.  
\- event.idm.read_only_udm.about.file.names: Newly mapped `attachment.attachmentFileName` raw log field(s) with `event.idm.read_only_udm.about.file.names` UDM field.  
\- event.idm.read_only_udm.about.file.sha1: Newly mapped `attachment.attachmentFileHash` raw log field(s) with `event.idm.read_only_udm.about.file.sha1` UDM field.  
\- event.idm.read_only_udm.about.file.size: Newly mapped `attachment.attachmentFileSize` raw log field(s) with `event.idm.read_only_udm.about.file.size` UDM field.  
\- event.idm.read_only_udm.about.user.userid: Newly mapped `process_user from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.user.userid` UDM field.  
\- event.idm.read_only_udm.about.administrative_domain: Newly mapped `process_user_domain from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.administrative_domain` UDM field.  
\- event.idm.read_only_udm.about.process.pid: Newly mapped `process_pid from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.process.pid` UDM field.  
\- event.idm.read_only_udm.about.process.file.size: Newly mapped `process_file_size from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.process.file.size` UDM field.  
\- event.idm.read_only_udm.about.process.file.full_path: Newly mapped `process_file_path from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.about.process.file.sha1: Newly mapped `process_file_hash_sha1 from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.process.file.sha1` UDM field.  
\- event.idm.read_only_udm.about.process.file.sha256: Newly mapped `process_file_hash_sha256 from processChainInfo` raw log field(s) with `event.idm.read_only_udm.about.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `matchedRule.id from correlatedIntelligence` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `matchedRule.name from correlatedIntelligence` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `matchedRule.threatType from correlatedIntelligence` raw log field(s) with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `suser` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `actResult`, `engVer`, `eventId`, `eventSourceType`, `eventSubName`, `filePath`, `logKey`, `mpname`, `mpver`, `objectHashId`, `objectType`, `pComp`, `rt`, `rt_utc`, `severity`, `dataType`, `groupIdCorrKey`, `groupIdCorrValues`, `mailMsgDirection`, `msgUuid`, `orgId`, `requests`, `scanTs`, `cloudAppName`, `mailFolder`, `mailMsgId`, `mailReceivedTime`, `mailUniqueId`, `objectSubType`, `integrity_level level objectFileRemoteAccess`, `objectFileSize`, `objectSubTrueType`, `objectTrueType`, `processHashId`, `process_hash_id`,`process_launch_time`, `process_name`, `process_signer`, `process_signer_valid`, `process_sub_true_type`, `process_true_type` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `channel`, `engType`, `firstAct`, `firstActResult`, `patVer`, `scanType`, `secondAct`, `secondActResult`, `subRuleName`, `matchedFilter_id`, `matchedFilter_name`, `matchedFilter_id`, `matchedFilter_name`, `detectionType`, `filterName`, `policyName`, `threatType`, `actResult`, `detectionAggressivenessLevel`, `engineOperation`, `malSubType`, `malType` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped non-email values from `duser` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped non-email values from `mailbox` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.about.resource.attribute.labels: Newly mapped negative values from `attachment.attachmentFileSize` raw log field(s) with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped non-email values from `suser` raw log field(s) with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2025-04-07 |  \- Newly created parser.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventType` and `eventName` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `pver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msgUuid` and `uuid` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `logReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `filterRiskLevel` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `productCode`, `application`, `aptCampaigns`, `appLabel`, `eventID`, `eventSubId`, `clusterId`, `clusterName`, `k8sNamespace` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `pname` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `endpointHostName` and `dvchost` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `endpointMacAddress` and `deviceMacAddress` raw log fields with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `endpointIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `endpointGUID`, `deviceGUID`, and `mDeviceGUID` raw log fields with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.source.asset.asset_id`: Newly mapped `senderGUID` raw log field with `event.idm.read_only_udm.source.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.source.ip`: Newly mapped `senderIp` and `mDevice` raw log fields with `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.principal.domain.name`: Newly mapped `hostName`, `userDomain`, and `domainName` raw log fields with `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `computerDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.asset.network_domain`: Newly mapped `domainName` raw log field with `event.idm.read_only_udm.principal.asset.network_domain` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `interestedHost`, `dhost` raw log fields with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `interestedIp`, `objectIp`, and `dst` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.userid`: Newly mapped `objectUser` raw log field with `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.userid` UDM fields.  
\- `event.idm.read_only_udm.source.hostname`: Newly mapped `shost` raw log field with `event.idm.read_only_udm.source.hostname` UDM field.  
\- `event.idm.read_only_udm.source.platform_version`: Newly mapped `sOSName` raw log field with `event.idm.read_only_udm.source.platform_version` UDM field.  
\- `event.idm.read_only_udm.source.mac`: Newly mapped `smac` raw log field with `event.idm.read_only_udm.source.mac` UDM field.  
\- `event.idm.read_only_udm.target.platform_version`: Newly mapped `dOSName` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `dmac` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `dstGroup` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `request` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.domain.name`: Newly mapped `requestBase` raw log field with `event.idm.read_only_udm.target.domain.name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `peerIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `peerHost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `peerEndpointGUID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.source.port`: Newly mapped `spt` raw log field with `event.idm.read_only_udm.source.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.source.file.names`: Newly mapped `fileName`, `compressedFileName` raw log fields with `event.idm.read_only_udm.source.file.names` UDM field.  
\- `event.idm.read_only_udm.source.file.full_path`: Newly mapped `fullPath`, `srcFilePath`, `filePathName` raw log fields with `event.idm.read_only_udm.source.file.full_path` UDM field.  
\- `event.idm.read_only_udm.source.file.size`: Newly mapped `fileSize`, `compressedFileSize` raw log fields with `event.idm.read_only_udm.source.file.size` UDM field.  
\- `event.idm.read_only_udm.source.file.sha1`: Newly mapped `compressedFileHash`, `srcFileHashSha1`, `fileHash` raw log fields with `event.idm.read_only_udm.source.file.sha1` UDM field.  
\- `event.idm.read_only_udm.source.file.sha256`: Newly mapped `compressedFileHashSha256`, `srcFileHashSha256`, `fileHashSha256` raw log fields with `event.idm.read_only_udm.source.file.sha256` UDM field.  
\- `event.idm.read_only_udm.source.file.mime_type`: Newly mapped `compressedFileType` raw log field with `event.idm.read_only_udm.source.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.source.file.md5`: Newly mapped `srcFileHashMd5` raw log field with `event.idm.read_only_udm.source.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `objectFileName` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `objectFilePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `objectFileHashSha1` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `objectFileHashSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `objectFileHashMd5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.about.file.names`: Newly mapped `attachmentFileName` raw log field with `event.idm.read_only_udm.about.file.names` UDM field.  
\- `event.idm.read_only_udm.about.file.size`: Newly mapped `attachmentFileSize` raw log field with `event.idm.read_only_udm.about.file.size` UDM field.  
\- `event.idm.read_only_udm.about.file.sha1`: Newly mapped `attachmentFileHash`, `attachmentFileHashSha1` raw log fields with `event.idm.read_only_udm.about.file.sha1` UDM field.  
\- `event.idm.read_only_udm.about.file.sha256`: Newly mapped `attachmentFileHashSha256` raw log field with `event.idm.read_only_udm.about.file.sha256` UDM field.  
\- `event.idm.read_only_udm.about.file.md5`: Newly mapped `attachmentFileHashMd5` raw log field with `event.idm.read_only_udm.about.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.integrity_level_rid`: Newly mapped `integrityLevel` raw log field with `event.idm.read_only_udm.principal.process.integrity_level_rid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `processCmd` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `processFileHashMd5` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha1`: Newly mapped `processFileHashSha1` raw log field with `event.idm.read_only_udm.principal.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `processFileHashSha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `parentCmd` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `parentFilePath` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Newly mapped `parentName` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `parentPid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.md5`: Newly mapped `parentFileHashMd5` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha1`: Newly mapped `parentFileHashSha1` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha256`: Newly mapped `parentFileHashSha256` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid`: Newly mapped `parentIntegrityLevel` raw log field with `event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `objectCmd` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `objectPid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `objectTargetProcess` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processFilePath`, `processImagePath` raw log fields with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `processName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processPid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_data`: Newly mapped `objectRegistryData` raw log field with `event.idm.read_only_udm.target.registry.registry_value_data` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Newly mapped `objectRegistryKeyHandle` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_name`: Newly mapped `objectRegistryValue` raw log field with `event.idm.read_only_udm.target.registry.registry_value_name` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `suser.0` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `duser` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `mailMsgSubject`, `highlightMailMsgSubject` raw log fields with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `msgId` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.email`: Newly mapped `mailbox` raw log field with `event.idm.read_only_udm.security_result.about.email` UDM field.  
\- `event.idm.read_only_udm.network.smtp.mail_from`: Newly mapped `mailSmtpFromAddresses` raw log field with `event.idm.read_only_udm.network.smtp.mail_from` UDM field.  
\- `event.idm.read_only_udm.network.smtp.rcpt_to`: Newly mapped `mailSmtpRecipients` raw log field with `event.idm.read_only_udm.network.smtp.rcpt_to` UDM field.  
\- `event.idm.read_only_udm.network.smtp.is_tls`: Newly mapped `mailSmtpTls` raw log field with `event.idm.read_only_udm.network.smtp.is_tls` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `httpReferer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `respCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques.id`: Newly mapped `techniqueId` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.id` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics.id`: Newly mapped `tacticId` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics.id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.vulnerabilities.cve_id`: Newly mapped `cve` raw log field with `event.idm.read_only_udm.principal.asset.vulnerabilities.cve_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.vulnerabilities.cve_id`: Newly mapped `cves` raw log field with `event.idm.read_only_udm.principal.asset.vulnerabilities.cve_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `ruleType` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `ruleVer` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `threatName`, `malName`, and `threatNames` raw log fields with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `subRuleId`, `subRuleName`, `detectionType`, `detectionName`, `malFamily`, `malType`, `malSubType`, and `riskLevel` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `score` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.department`: Newly mapped `userDepartment` raw log field with `event.idm.read_only_udm.principal.user.department` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principalName`, `logonUsers` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.model`: Newly mapped `endpointModel` and `deviceModel` raw log fields with `event.idm.read_only_udm.principal.asset.hardware.model` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
