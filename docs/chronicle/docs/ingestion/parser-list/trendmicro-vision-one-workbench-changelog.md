---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-workbench-changelog/
title: Change log for TRENDMICRO_VISION_ONE_WORKBENCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:30.846589+00:00
---

# Change log for TRENDMICRO_VISION_ONE_WORKBENCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-workbench-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE_WORKBENCH

Date | Changes  
---|---  
2026-08-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src`, `endpointip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `processCmd` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processPid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `processUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processFilePath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `logonUser`, `isRetroScan`, `originUUID`, `platformAssetTags.Asset_group`, `userDomain` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `groups`, `filePath`, `protectionManager` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `platformAssetTags`, `customAssetTags` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `endpointGuid`, `shost` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `alertProvider` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_feed_name`: Mapped `alertProvider` raw log field with `event.idm.read_only_udm.security_result.threat_feed_name` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `model` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `model` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.security_result.category`: Newly mapped `model`, `eventName` raw log fields with `event.idm.read_only_udm.security_result.category` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `firstAct` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `engType`, `engVer`, `objectFileRemoteAccess`, `patVer`, `secondAct`, `secondActResult` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `process_file_path` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `process_cmd` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha1`: Newly mapped `process_file_hash_sha1` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha1` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha256`: Newly mapped `process_file_hash_sha256` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field  
\- `event.idm.read_only_udm.principal.process.parent_process.file.md5`: Newly mapped `process_file_hash_md5` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.md5` UDM field  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `ruleIdStr` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `fileHash` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `objectFileSize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field  
\- `event.idm.read_only_udm.target.file.signature_info.sigcheck.signers`: Newly mapped `objectSigner` raw log field with `event.idm.read_only_udm.target.file.signature_info.sigcheck.signers` UDM field  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `indicator.value` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `alertProvider`, `model` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `campaign`, `malName` raw log fields with `event.idm.read_only_udm.security_result.threat_name` UDM field  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `firstActResult` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `malFamily`, `filterRiskLevel`, `majorVirusType`, `malType`, `objectHashId`, `quarantineFileId`, `scanType` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `tag` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `tag` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `tag` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field   
2026-06-25 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `deviceDirection` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `aggregatedCount`, `direction`, `out`, `rtHour`, `rtWeekDay`, `etherType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `app` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `spt` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `dmac` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `smac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `peerHost`, `interestedHost` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `peerIp`, `interestedIp` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the value of `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when the log contains principal machine data and only target mac.   
2026-06-04 |  Enhancement:  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `groupId` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `osName` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `osVer` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `endpointStatus`, `agentStatus` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `searchDL`, `lastConnectedTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: If `osName` is `Windows`, updated the value of `event.idm.read_only_udm.principal.platform` to `WINDOWS`, else if `osName` is `Linux`, updated the value of `event.idm.read_only_udm.principal.platform` to `LINUX`, else if `osName` is `mac`, updated the value of `event.idm.read_only_udm.principal.platform` to `MAC`.   
2026-03-23 |  Enhancement:  
\- `event.idm.read_only_udm.about.file.full_path`: Removed mapping of `indicator.value` from `event.idm.read_only_udm.about.file.full_path` UDM field as this is an object file path suitable for `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Mapped `indicator.value` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field when `indicator.type` is `fullpath` and `indicator.field` is `objectFilePath`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `indicator.value` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field when `indicator.type` is `fullpath` and `indicator.field` is `processFilePath`.  
\- `event.idm.read_only_udm.target.process.file.sha1`: Newly mapped `indicator.value` raw log field with `event.idm.read_only_udm.target.process.file.sha1` UDM field when `indicator.type` is `file_sha1` and `indicator.field` is `objectFileHashSha1`.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `indicator.value` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field when `indicator.type` is `file_sha256` and `indicator.field` is `objectFileHashSha256`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mappings for `indicator.field` and `indicator.value` now only occur as a fallback if the `indicator.type` and `indicator.field` do not match any of the specific `file_sha256`, `fullpath`, `file_sha1`, `email_message_id`, `email_subject`, `url`, `user_account`, `email_sender` or `command_line` conditions.  
\- Added a Grok pattern on `message` to re-extract the raw value of `workbenchLink` field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: When `indicator_value` is a valid SHA256 hash, map it to `event.idm.read_only_udm.principal.process.file.sha256` UDM field.   
2026-01-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Removed mapping of `entity.entityValue` from event.idm.read_only_udm.principal.user.user_display_name UDM field when `entity.entityType` is equal to `account` and `entity.entityValue` is in the format `domain\\user` then domain value is mapped to `event.idm.read_only_udm.principal.user.user_display_name` UDM field and user value is mapped to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Mapped `domain_value` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of entity.entityId from `event.idm.read_only_udm.principal.user.userid UDM field when `entity.entityType` is equal to `account` and `entity.entityValue` is in the format `domain\\\user` then domain value is mapped to `event.idm.read_only_udm.principal.user.user_display_name` UDM field and user value is mapped to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped user_id_value raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped entity.entityValue raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field to cature the account user identifier details if `entity.entityValue` is not the format `domain\\user` and `entity.entityType` is equal to `account`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped impactScope.cloudWorkloadCount raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `indicator.value`,`indicator.value.name`, `indicator.value.guid`,`indicator.value.ips`,`ownerIds` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check to map `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if (`has_user` is `true` and `has_principal_email` is `true`) or `has_principal_user_id` is `true`.   
2025-12-12 |  Enhancement:  
\- Added logic to check if `entity.entityValue.name` is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` if it`s an IP address. If not an IP, the first entity`s name is mapped to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` (format: `%{entity.entityValue.name}`), while subsequent entity names go to `event.idm.read_only_udm.principal.resource.attribute.labels` (key: `hostname: %{index}`).  
\- event.idm.read_only_udm.principal.ip: Newly mapped `entity.entityValue.name` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `entity.entityValue.name` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `entity.entityId`, `entity.managementScopeGroupId`, `entity.managementScopeInstanceId` and `entity.managementScopePartitionKey` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `entity.entityId` raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `entity.relatedEntities`, `entity.relatedIndicatorIds`, `entity.provenance`, `indicator.id`, `indicator.relatedEntities`, `indicator.filterIds`, `indicator.provenance`, `filter.id`, `filter.name`, `filter.matchedDateTime`, `matchedEvent.uuid`, `matchedEvent.matchedDateTime` and `matchedEvent.type` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `impactScope.desktopCount`, `impactScope.serverCount`, `impactScope.accountCount`, `impactScope.emailAddressCount`, `impactScope.containerCount` and `impactScope.cloudIdentityCount` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-14 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Changed mapping for `event.idm.read_only_udm.security_result.detection_fields.key` from `indicator.type` to `indicator.field` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Changed mapping for `event.idm.read_only_udm.security_result.detection_fields.key` from field to `type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Changed mapping for `event.idm.read_only_udm.security_result.detection_fields.value` from `indicator.field` to `indicator.type` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `alertProvider` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `schemaVersion` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field when schemaVersion is not empty.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field when severity is one of `CRITICAL`, `HIGH`, `MEDIUM`, or `LOW`.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.network.email.mail_id` UDM field when `indicator.type` is `email_message_id` and has_email_message_id is `false`.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.network.email.subject` UDM field when `indicator.type` is `email_subject`.  
\- event.idm.read_only_udm.about.url: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.about.url` UDM field when `indicator.type` is `url` and has_url is `false`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field when `indicator.type` is `user_account` and has_user is `false`.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.principal.process.command_line` UDM field when `indicator.type` is `command_line`, `indicator.field` is `processCmd`, and has_principal_process is `false`.  
\- event.idm.read_only_udm.principal.process.parent_process.command_line: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field when `indicator.type` is `command_line`, `indicator.field` is `parentCmd`, and has_parent_process is `false`.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.target.process.command_line` UDM field when `indicator.type` is `command_line`, `indicator.field` is `objectCmd`, and has_target_process is `false`.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.principal.process.file.sha256` UDM field when `indicator.type` is `file_sha256`, `indicator.field` is `processFileHashSha256`, has_principal_sha256 is `false`, and indicator.value matches regex ^[0-9a-f]+$.  
\- event.idm.read_only_udm.about.file.full_path: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.about.file.full_path` UDM field when `indicator.type` is `fullpath`.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `indicator.value` raw log field(s) with `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `indicator.type` is `email_sender`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `modelId` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `modelType` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `incidentId` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_user == `true` and has_principal_email == `true`, updated to USER_UNCATEGORIZED.   
2025-07-31 |  Enhancement:  
\- Added a new grok pattern to parse ip from raw logs field `src_ip`  
2025-05-13 |  Enhancement:  
\- Added a condition to check if `entity.entityValue.name` is not empty before populating `principal.hostname` and `principal.asset.hostname` UDM fields.   
2024-10-27 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
