---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-changelog/
title: Change log for TRENDMICRO_VISION_ONE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:31.426269+00:00
---

# Change log for TRENDMICRO_VISION_ONE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-vision-one-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_VISION_ONE

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `endpointdesktop.Guid`, `endpointservers.Guid`, `endpointGuid`, `endpoint.guid`, `endpointGUID`, `detail.endpointGUID`, `entity.entityId`, `entity.entityValue.guid` raw log fields to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.platform_patch_level`: Newly mapped `detail.osDescription` raw log field to `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `productName`, `detail.filterRiskLevel`, `detail.protectionManager` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `mDeviceGUID` raw log field to `event.idm.read_only_udm.observer.asset.asset_id` UDM field when `mDeviceGUID` is present.  
\- Updated the prefix naming convention for `endpoint.agentGuid` and `detail.endpointGuid` mapped to `event.idm.read_only_udm.principal.asset.asset_id` from `Device Id:` to `agentGuid:`, and for `endpointdesktop.Guid` and `endpointservers.Guid` from `GUID:` to `agentGuid:`.  
\- Added support to parse JSON array format logs by wrapping `message` into `records` and extracting fields from `records`.  
\- Updated mapping of `mDeviceGUID` to `event.idm.read_only_udm.principal.asset.asset_id` UDM field to only populate when `mDeviceGUID` is present.   
2026-01-08 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `indicator.value` from `event.idm.read_only_udm.security_result.detection_fields` UDM field because the `indicator.value` contains a file's SHA1 hash when the `indicator.type` is file_sha1.  
\- event.idm.read_only_udm.principal.file.sha1: Mapped `indicator.value` raw log field to `event.idm.read_only_udm.principal.file.sha1` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `engVer` raw log field with `event.idm.read_only_udm.additional.fields UDM field`.  
\- event.idm.read_only_udm.security_result.attack_details.tactics: Newly mapped `tacticId` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics UDM field`.  
\- When `indicator.type` is `file_sha1`, the `indicator.value` field is now converted to lowercase before being mapped to `event.idm.read_only_udm.principal.file.sha1`.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `process_file_size`, `level`, `detail.instanceId`, `detail.channel`, `detail.objectLaunchTime`, `detail.engineOperation`, `detail.processHashId`, `process_pid`, `process_file_path`, `process_cmd`, `process_file_hash_sha1`, `process_file_hash_sha256`, `process_user` and `process_launch_time` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `detail.objectFileSize` raw log field to event.idm.read_only_udm.target.file.size.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `detail.policyId` raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `detail.behaviorCat` raw log field to event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_pid` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.process.pid.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `process_file_path` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.process.file.full_path.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `process_cmd` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.process.command_line.  
\- event.idm.read_only_udm.principal.process.file.sha1: Newly mapped `process_file_hash_sha1` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.process.file.sha1.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `process_file_hash_sha256` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.process.file.sha256.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `process_user` raw log field from `detail.processChainInfo` to event.idm.read_only_udm.principal.user.userid.  
\- Conditionally mapped `entity_entityValue`: maps to `event.idm.read_only_udm.principal.user.user_display_name` for the first entity, and to `event.idm.read_only_udm.additional.fields` for subsequent entities.   
2025-11-27 |  Enhancement:  
\- Implemented a grok pattern to parse the username from the `entity.entityValue` field when the `entityType` is `account`.  
\- Iterating through `impactScope.entities` with index for more granular field mapping in `additional.fields`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `matchedRules.matchedFilters.id`, `matchedRules.matchedFilters.matchedDateTime`, `schemaVersion`, `status`, `modelId`, `modelType`, `incidentId`, `impactScope.desktopCount`, `impactScope.serverCount`, `impactScope.accountCount`, `impactScope.emailAddressCount`, `impactScope.containerCount`, `impactScope.cloudIdentityCount`, `entity.managementScopePartitionKey`, `entity.managementScopeInstanceId`, `entity.managementScopeGroupId`, `entity.entityValue.guid`, and `entity.provenance` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Changed mapping for `event.idm.read_only_udm.principal.user.user_display_name` from `entity.entityValue` to the part of `entity.entityValue` after a backslash, extracted via grok.  
\- `event.idm.read.only_udm.security_result.detection_fields`: Newly mapped `matchedRules.matchedFilters.matchedEvents.uuid` and `matchedRules.matchedFilters.matchedEvents.type` to `event.idm.read_only_udm.security_result.detection_fields`.   
2025-11-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `detail.eventTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `detectedDateTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `detail.mpver` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `detail.senderIp` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `detail.dvchost` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `detail.mDeviceGUID` raw log field with `event.idm.read_only_udm.observer.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `detail.logReceivedTime`, `detail.logKey`, `detail.eventSourceType`, `detail.senderGUID`, `detail.eventSubName`, `detail.pname` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `detail.processName` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `detail.groupId` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `detail.dacDeviceType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `detail.deviceGUID` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `detail.accessPermission` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `filter.riskLevel` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_type`: Newly mapped `filter.type` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `tag`, `object.field`, `object.type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `value` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `endpoint.agentGuid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `entityName` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped `ingestedDateTime` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `detail.eventName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `detail.endpointMacAddress` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.   
2025-08-05 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `entityType`,`deviceFacility`, `ApexCentralHost` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- Added a grok pattern on `TMCMdevicePlatform` raw log field to extract `plat_form` and `platform_version` fields.  
\- event.idm.read_only_udm.principal.platform_version: Newly Mapped `platform_version` field to event.idm.read_only_udm.principal.platform_version UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly Mapped `plat_form` raw log field to event.idm.read_only_udm.principal.platform UDM field.  
\- Initialised `msg` field in statedata to parse the unparsed raw log.  
\- Removed the variable `process_present` that was set to `true` for `processFilePath` field .  
\- Removed the conditional check for `process_present` where the event.idm.read_only_udm.metadata.event_type is set to `PROCESS_UNCATEGORIZED`.  
\- event.idm.read_only_udm.target.process.file.full_path: Updated logic to set `target_process_present` to `true` when mapping `object.value` to event.idm.read_only_udm.target.process.file.full_path if object.field is equal to `processFilePath`.  
\- event.idm.read_only_udm.target.process.file.sha1: Updated logic to set `target_process_present` to `true` when mapping `object.value` to event.idm.read_only_udm.target.process.file.sha1 if object.field is equal to `processFileHashSha1`.  
\- event.idm.read_only_udm.target.process.command_line: Updated logic to set `target_process_present` to true when mapping `object.value` to event.idm.read_only_udm.target.process.command_line if object.field is equal to `processCmd`.   
2025-06-05 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `filters.highlightedObjects.value` raw log field when `filters.highlightedObjects.field` is `dst` with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `filters.highlightedObjects.value` raw log field when `filters.highlightedObjects.field` is `src` with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-05-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Impactscopedetails.EndpointServers.Guid` and `Impactscopedetails.EndpointDesktops.Guid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added `index` for `Impactscopedetails.EndpointDesktops` and `Impactscopedetails.EndpointServers`.   
2025-04-30 |  Enhancement:  
\- Added a Gsub to convert `Endpoint - Servers` to `EndpointServers`.  
\- Added a flag `has_asset_id` and `has_process`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Impactscopedetails.EndpointServers.Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id`: Newly mapped `Impactscopedetails.EndpointServers.Guid` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `Impactscopedetails.EndpointServers.Ips` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.file.sha1`: Newly mapped `objectfield` if equal to `objectFileHashSha1` or `fileHash` raw log field with `event.idm.read_only_udm.target.process.parent_process.file.sha1` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.command_line`: Newly mapped `objectfield` if equal to `processCmd` raw log field with `event.idm.read_only_udm.target.process.parent_process.command_line` UDM field.  
\- `PROCESS_LAUNCH`: Added support for the event `PROCESS_LAUNCH` when `principal_present` is `true`, `has_asset_id` is `true` AND `has_process` is `true` `has_target_hostname` is `true` and set `event.idm.read_only_udm.principal.asset_id` to "".  
\- `event.idm.read_only_udm.metadata.event_type`: Removed mapping of `EMAIL_TRANSACTION` from `event.idm.read_only_udm.metadata.event_type` UDM field.  
\- Set `has_asset_id` to `true` when `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` is populated.  
\- Set `has_process` to `true` when `event.idm.read_only_udm.target.process.file.full_path` is populated.   
2025-04-22 |  Enhancement:  
\- `event.idm.read_only.udm.additional.fields`: Removed mapping of `endpoint.name` from `event.idm.read_only.udm.additional.fields` UDM field.  
\- `event.idm.read_only.udm.principal.hostname`: Mapped `endpoint.name` raw log field with `event.idm.read_only.udm.principal.hostname` UDM field.  
\- `event.idm.read_only.udm.principal.asset.hostname`: Mapped `endpoint.name` raw log field with `event.idm.read_only.udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only.udm.principal.ip`: Mapped `endpoint.ips` raw log field with `event.idm.read_only.udm.principal.ip` UDM field if valid IP, esle mapped it to `event.idm.read_only.udm.additional.fields`.  
\- `event.idm.read_only.udm.principal.asset.ip`: Mapped `endpoint.ips` raw log field with `event.idm.read_only.udm.principal.asset.ip` UDM field if valid IP, esle mapped it to `event.idm.read_only.udm.additional.fields`.  
\- `event.idm.read_only.udm.additional.fields`: Newly mapped `actResult` raw log list field with `event.idm.read_only.udm.additional.fields` UDM field.  
\- `event.idm.read_only.udm.security_result.action`: Newly mapped `event.idm.read_only.udm.security_result.action` UDM field as `ALLOW` if `actResult` raw log field value is `Passed` else mapped it to `BLOCK`.   
2025-03-21 |  Enhancement:  
\- If `objecttype` is `command_line` and `objectfield` is `objectCmd` and `target_commandline_process_set` is false then mapped `object.CustomValue` to `target.process.command_line`.  
\- If `objecttype` is `command_line` and `objectfield` is `parentCmd` and `target_commandline_parent_process_set` is false then mapped `object.CustomValue` to `target.process.parent_process.command_line`.  
\- If `objecttype` is `command_line` and `objectfield` is not `processCmd` and `objectCmd` then mapped `object.CustomValue` to `target.resource.attribute.labels`.  
\- If `objecttype` is `file_sha1` and `objectfield` is `processFileHashSha1` and `target_filesha1_set` is false then mapped `object.CustomValue` to `target.file.sha1` and `target.process.file.sha1`.  
\- If `objecttype` is `file_sha1` and `objectfield` is `parentFileHashSha1` and `target_parent_filesha1_set` is false then mapped `object.CustomValue` to `target.process.parent_process.file.sha1`.  
\- If `objecttype` is `file_sha1` and `objectfield` is not `parentFileHashSha1` and `processFileHashSha1` then mapped `object.CustomValue` to `target.resource.attribute.labels`.  
\- If `objecttype` is `fullpath` and `objectfield` is `processFilePath` and `target_filepath_set` is false then mapped `object.CustomValue` to `target.file.full_path` and `target.process.file.full_path`.  
\- If `objecttype` is `fullpath` and `objectfield` is `parentFilePath` and `target_parent_filepath_set` is false then mapped `object.CustomValue` to `target.process.parent_process.file.full_path`.  
\- If `objecttype` is `fullpath` and `objectfield` is not `processFilePath` and `processFilePath` then mapped `object.CustomValue` to `target.resource.attribute.labels`.   
2025-03-17 |  Enhancement:  
\- Removed the mapping of `uuid` from `principal.user.userid`.  
\- Added the mapping of `uuid` to `principal.resource.product_object_id`.   
2025-03-06 |  Enhancement:  
\- Added a for loop to handle multiple `Impactscopedetails` and `Accounts`.  
\- Added a for loop to handle multiple `Impactscopedetails` and `EndpointDesktops`.  
\- Mapped `endpointdesktop.Hostname` to `principal.hostname`.  
\- Mapped `guid` to `principal.asset.asset_id`.  
\- Mapped `Ips` to `principal.ip`.  
\- If `objecttype` is `text` then mapped `object.CustomValue` to `security_result.detection_fields`.  
\- If `objecttype` is `command_line` then mapped `object.CustomValue` to `target.process.command_line`.  
\- If `objecttype` is `file_sha1` then mapped `object.CustomValue` to `target.process.file.sha1`.  
\- If `objecttype` is `fullpath` then mapped `object.CustomValue` to `target.file.full_path`.  
\- Mapped `IP_address` to `principal.ip`.  
\- Mapped `pliance_IP_address` to `Appliance_IP_address`.   
2025-02-11 |  Enhancement:  
\- When `object_field` is `parentCmd`, it is mapped to `principal.process.command_line`.  
\- When `object_field` is `parentFilePath`, it is mapped to `principal.process.file.full_path`.  
\- Removed `principal.process.command_line` and `principal.process.file.full_path` when `object_field` is `processCmd`.   
2025-01-31 |  Enhancement:  
\- When `object_field` is `processCmd` mapped to `principal.process.command_line` and `principal.process.file.full_path`.  
\- When `object_field` is `malName` mapped to `security_result.threat_name`.  
\- When `object_field` is `actResult` mapped to `security_result.action_details` and `security_result.action`.   
2025-01-24 |  Enhancement:  
\- Removed mappings for `target`.  
\- Mapped `detail.eventSubId` should be mapped from `metadata.product_event_type`  
\- Mapped `endpoint.guid` and `detail.endpointGuid` to `principal.asset_id` and `principal.asset.asset_id`  
\- Mapped `detail.uuid` to `metadata.product_log_id`  
\- Mapped `filters.0.unique_id` to `security_result.rule_id`  
\- Mapped `filters.0.name` to `security_result.summary`  
\- Mapped `filters.0.id` to `security_result.rule_name`  
2025-01-17 |  Enhancement:  
\- Removed mapping of `highlightedObjects` to `additional.fields` and mapped them to respective `process` and `file` fields.   
2024-12-06 |  Enhancement:  
\- Added date match pattern for firstSeen, createdDateTime, and lastSeen.   
2024-11-15 |  Enhancement:  
\- Added support for dropped logs.   
2024-11-04 |  Enhancement:  
\- When `severity` value is `info`, then mapped `security_result.severity` to `INFORMATIONAL`.  
\- Added support for IPv6 logs.   
2024-10-10 |  Enhancement:  
\- Mapped `detectionTime` to `metadata.event_timestamp`.   
2024-10-03 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Changed mapping of `details.ipAddr` from `principal.ip` and `principal.asset.ip` to `target.ip` and `target.asset.ip`.   
2024-08-15 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2024-08-01 |  Enhancement:  
\- Initialized `about` to null and added a check before merging.   
2024-05-24 |  Enhancement:  
\- Added support for the new pattern of JSON logs.   
2024-05-13 |  Enhancement:  
\- Added support for JSON logs.   
2023-03-24 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
