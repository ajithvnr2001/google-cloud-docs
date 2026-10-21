---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-activity-changelog/
title: Change log for TRENDMICRO_VISION_ONE_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:09:31.324786+00:00
---

# Change log for TRENDMICRO_VISION_ONE_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-activity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_ACTIVITY

Date | Changes  
---|---  
2025-08-08 |  Enhancement:  
\- Enhanced parsing for `src` and `dst` fields to handle comma-separated IP addresses by pre-processing with gsub and using the json filter.  
\- Newly added JSON filter for `src` and `dst` raw log fields to parse those fields correctly.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `requestBase` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.src.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.src.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dstLocation` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `urlCat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `srcLocation` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `responseSize` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `policyUuid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `requestSize` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `fileHashSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent` : Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `sender` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `failedHTTPSInspection`,`serverProtocol`,and `score` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `fileName`,`fileType`,`fileSize`,`isPrivateApp`,`serverTls`,`cloudAppCat`,`contentEncoding`,`e2eLatency`,`searchDL`,`trafficType`,`userDepartment`,`serverRespTime`,`mimeType`, and `fileHash` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-07 |  Enhancement:  
\- Added for loop over `scannerDetails.policyScanResults` raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `groupId`,`attachmentFileSizes`,`value.name`,`value.id`,`value.spamRidHeader`,`value.spamResultHeader` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `scanType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `downstreamTls` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `mailMsgId` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `eventSourceType`,`mailDirection` ,`value.action`,`value.type` fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern to extract `target_ip`, `target_hostname`,`target_port` from `mailRecipientIp` raw log field.  
\- `event.idm.read_only_udm.target_udm.ip`,`event.idm.read_only_udm.target_udm.asset.ip`: Newly mapped `target_ip` field to `event.idm.read_only_udm.target_udm.ip` and `event.idm.read_only_udm.target_udm.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target_udm.hostname`,`event.idm.read_only_udm.target_udm.asset.hostname`: Newly mapped `target_hostname` field to `event.idm.read_only_udm.target_udm.hostname` and `event.idm.read_only_udm.target_udm.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target_udm.port`: Newly mapped `target_port` field to `event.idm.read_only_udm.target_udm.port` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `remarks` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `deliveryStatus` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- Added a grok pattern on message field .  
\- Added a for loop to over `duser` raw log field .  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `mailToAddr` field with `event.idm.read_only_udm.network.email.to` UDM field.   
2025-04-07 |  \- Newly created parser.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels` and `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` and `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `msgUuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `logReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `eventID`, `app`, `appLabel`, `application`, `productCode` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `pver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `filterRiskLevel` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `pname` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `idpName` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip`: Newly mapped `sourceIPAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.source.port`: Newly mapped `spt` raw log field with `event.idm.read_only_udm.source.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.userid`: Newly mapped `objectUser` raw log field with `event.idm.read_only_udm.principal.user.userid` and `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `objectFilePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `objectFileHashMd5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `objectFileHashSha1` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `objectFileHashSha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.file.last_modification_time`: Newly mapped `objectFileModifiedTime` raw log field with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- `event.idm.read_only_udm.target.file.first_seen_time`: Newly mapped `objectFirstSeen` raw log field with `event.idm.read_only_udm.target.file.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.target.file.last_seen_time`: Newly mapped `objectLastSeen` raw log field with `event.idm.read_only_udm.target.file.last_seen_time` UDM field.  
\- `event.idm.read_only_udm.target.process.integrity_level_rid`: Newly mapped `objectIntegrityLevel` raw log field with `event.idm.read_only_udm.target.process.integrity_level_rid` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `objectIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `objectIps` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `objectPid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `objectPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_data`: Newly mapped `objectRegistryData` raw log field with `event.idm.read_only_udm.target.registry.registry_value_data` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Newly mapped `objectRegistryKeyHandle` raw log field with `event.idm.read_only_udm.target.registry.registry_key` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_value_name`: Newly mapped `objectRegistryValue` raw log field with `event.idm.read_only_udm.target.registry.registry_value_name` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `objectFileSize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vpcEndpointId`, `apiVersion`, `awsRegion`, `recipientAccountId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `endpointHostName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `endpointMacAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `endpointGuid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `endpointIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.domain.name`: Newly mapped `hostName` raw log field with `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- `event.idm.read_only_udm.principal.process.integrity_level_rid`: Newly mapped `integrityLevel` raw log field with `event.idm.read_only_udm.principal.process.integrity_level_rid` UDM field.  
\- `event.idm.read_only_udm.source.process.command_line`: Newly mapped `processCmd` raw log field with `event.idm.read_only_udm.source.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `objectCmd` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.source.file.full_path`: Newly mapped `srcFilePath` raw log field with `event.idm.read_only_udm.source.file.full_path` UDM field.  
\- `event.idm.read_only_udm.source.file.md5`: Newly mapped `srcFileHashMd5` raw log field with `event.idm.read_only_udm.source.file.md5` UDM field.  
\- `event.idm.read_only_udm.source.file.md5`: Newly mapped `srcFileHashSha1` raw log field with `event.idm.read_only_udm.source.file.md5` UDM field.  
\- `event.idm.read_only_udm.source.file.md5`: Newly mapped `srcFileHashSha256` raw log field with `event.idm.read_only_udm.source.file.md5` UDM field.  
\- `event.idm.read_only_udm.source.file.size`: Newly mapped `srcFileSize` raw log field with `event.idm.read_only_udm.source.file.size` UDM field.  
\- `event.idm.read_only_udm.source.file.last_modification_time`: Newly mapped `srcFileModifiedTime` raw log field with `event.idm.read_only_udm.source.file.last_modification_time` UDM field.  
\- `event.idm.read_only_udm.source.file.first_seen_time`: Newly mapped `srcFirstSeen` raw log field with `event.idm.read_only_udm.source.file.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.source.file.last_seen_time`: Newly mapped `srcLastSeen` raw log field with `event.idm.read_only_udm.source.file.last_seen_time` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processFilePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processPid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `processName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `processFileHashMd5` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha1`: Newly mapped `processFileHashSha1` raw log field with `event.idm.read_only_udm.principal.process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `processFileHashSha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `parentPid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `parentCmd` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `parentFilePath` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Newly mapped `parentName` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.md5`: Newly mapped `parentFileHashMd5` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha1`: Newly mapped `parentFileHashSha1` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha256`: Newly mapped `parentFileHashSha256` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid`: Newly mapped `parentIntegrityLevel` raw log field with `event.idm.read_only_udm.principal.process.parent_process.integrity_level_rid` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `request` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `requests` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.source.ip`: Newly mapped `publicSrc` raw log field with `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.source.port`: Newly mapped `publicSpt` raw log field with `event.idm.read_only_udm.source.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `clusterId`, `clusterName`, `k8sNamespace` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `msgId` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.email`: Newly mapped `mailbox` raw log field with `event.idm.read_only_udm.security_result.about.email` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `mailFromAddresses` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `duser` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `mailToAddresses` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `mailCcAddresses` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- `event.idm.read_only_udm.network.email.bcc`: Newly mapped `mailBccAddresses` raw log field with `event.idm.read_only_udm.network.email.bcc` UDM field.  
\- `event.idm.read_only_udm.network.email.reply_to`: Newly mapped `mailReplyToAddresses` raw log field with `event.idm.read_only_udm.network.email.reply_to` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `mailMsgSubject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `mailScore` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.source.ip`: Newly mapped `mailSenderIp` raw log field with `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principalName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.about.file.names`: Newly mapped `attachmentFileName` raw log field with `event.idm.read_only_udm.about.file.names` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attachmentSha256`, `attachmentSha1`, `attachmentMd5`, `idpId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip_location.country_or_region`: Newly mapped `locationCountry` raw log field with `event.idm.read_only_udm.principal.ip_location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.ip_location.city`: Newly mapped `locationCity` raw log field with `event.idm.read_only_udm.principal.ip_location.city` UDM field.  
\- `event.idm.read_only_udm.principal.ip_location.state`: Newly mapped `locationState` raw log field with `event.idm.read_only_udm.principal.ip_location.state` UDM field.  
\- `event.idm.read_only_udm.principal.ip_location.region_coordinates.longitude`: Newly mapped `locationLongitude` raw log field with `event.idm.read_only_udm.principal.ip_location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.principal.ip_location.region_coordinates.latitude`: Newly mapped `locationLatitude` raw log field with `event.idm.read_only_udm.principal.ip_location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `clientId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `userId` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `userDisplayName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.id`: Newly mapped `targetResourceId` raw log field with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `targetResourceDisplayName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `clientDisplayName`, `clientOS` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.model`: Newly mapped `endpointModel` raw log field with `event.idm.read_only_udm.principal.asset.hardware.model` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `clientTls` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tlsSelectedCipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.source.hostname`: Newly mapped `clientHost` raw log field with `event.idm.read_only_udm.source.hostname` UDM field.  
\- `event.idm.read_only_udm.source.hostname`: Newly mapped `shost` raw log field with `event.idm.read_only_udm.source.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `serverHost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol` and `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `clientProtocol` raw log field with `event.idm.read_only_udm.network.application_protocol` and `event.idm.read_only_udm.network.application_protocol_version` UDM fields.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `httpReferer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `respCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `resolvedUrlIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `resolvedUrlPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `malName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detectionType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `deviceGUID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `ruleType` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleUuid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `serverIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `serverPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `serverMAC` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `dmac` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.source.ip`: Newly mapped `clientIp` raw log field with `event.idm.read_only_udm.source.ip` UDM field.  
\- `event.idm.read_only_udm.source.port`: Newly mapped `clientPort` raw log field with `event.idm.read_only_udm.source.port` UDM field.  
\- `event.idm.read_only_udm.source.mac`: Newly mapped `clientMAC` raw log field with `event.idm.read_only_udm.source.mac` UDM field.  
\- `event.idm.read_only_udm.source.mac`: Newly mapped `smac` raw log field with `event.idm.read_only_udm.source.mac` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name` and `event.idm.read_only_udm.metadata.vendor_name`: Newly Mapped `TREND VISION ONE ACTIVITY` to `metadata.product_name` and `metadata.vendor_name` UDM fields.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
