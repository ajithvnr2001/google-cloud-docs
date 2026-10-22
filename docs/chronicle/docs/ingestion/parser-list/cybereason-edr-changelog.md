---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cybereason-edr-changelog/
title: Change log for CYBEREASON_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:32.865830+00:00
---

# Change log for CYBEREASON_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cybereason-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBEREASON_EDR

Date | Changes  
---|---  
2026-02-24 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `rootCauseElementHashes` from event.idm.read_only_udm.security_result.detection_fields UDM field because the file hash is mapped to principal to emphasize the malware (identified by its hash) as the primary actor initiating the malicious operation.  
\- event.idm.read_only_udm.principal.file.sha1: Mapped `rootCauseElementHashes` raw log field to event.idm.read_only_udm.principal.file.sha1 UDM when index is zero.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Mapped the `rootCauseElementHashes` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels, when index is non-zero.   
2025-10-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Modified transformation to use only the value of `user_displayName` raw log field, removing the appended index.  
\- `event.idm.read_only_udm.principal.hostname`: Modified transformation to use only the value of `machine.displayName` raw log field, removing the appended index.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rootCauseElementHashes`, `class_val` (from @class), `edr`, `malopStatus`, `closed`, `empty` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `primaryRootCauseName`, `rootCauseElementNamesCount`, `malopCloseTime`, `malopDetectionType`, `malopType`, `machine.empty` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-08 |  Enhancement:  
\- Used intermediate variables (`machine_guid`, `machine_lastConnected`, `machine_displayName`, `machine_connected`, `machine_isolated`) to store values from the `machine` raw log field (`machine.guid`, `machine.lastConnected`, `machine.displayName`, `machine.connected`, `machine.isolated`) and added conditional checks.  
\- Used intermediate variables (`user_guid`, `user_displayName`, `user_admin`, `user_domainUser`, `user_localSystem`) to store values from the `user` raw log field (`user.guid`, `user.displayName`, `user.admin`, `user.domainUser`, `user.localSystem`) and added conditional checks.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `iocs` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `mitreSubTechniques`, `decisionStatuses`, `groups`, `labels` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Renamed internal variables `secu_result` and `sec_result` to `security_result` to consolidate a single `event.idm.read_only_udm.security_result` block.   
2025-09-18 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `machines.displayName` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `users.displayName` raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `lastUpdateTime`, `detectionEngines`, `mitreTactics`, `mitreTechniques` and `detectionTypes` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `rootCauseElementHashes` and `machines.lastConnected` raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- Enhanced event type detection: setting event.idm.read_only_udm.metadata.event_type to USER_UNCATEGORIZED when user information is available, and STATUS_UPDATE when host information is available.   
2025-07-02 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `LogType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.guid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `status` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.guid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.fqdn` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.serviceStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.avDbVersion` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.documentProtectionMode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.antiMalwareStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.documentProtectionStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.amStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.outdated` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.collectionStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.collectiveUuid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.privateServerIp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `Sensor.privateServerIp` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.siteId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.isolated` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.exitReason` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.lastUpgradeResult` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.quickScanStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.policyName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.groupId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.groupName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.groupStickinessLabel` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.fullScanStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Sensor.siteName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `machine.pylumId` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `needsAttention` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id.malwareType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `referenceGuid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `referenceElementType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `schedulerScan` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `malwareDataModel` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `iconBase64` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2025-04-24 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `Sensor.serverId` from `event.idm.read_only_udm.target.user.userid` UDM field for Malware logs.  
\- event.idm.read_only_udm.principal.user.user_display_name: Removed mapping of `displayName` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field for Malop logs.  
\- event.idm.read_only_udm.additional.fields: Added mapping of `Sensor.serverId` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Added mapping of `displayName` to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-01-23 |  Enhancement:  
\- Changed `metadata.event_type` from `NETWORK_CONNECTION` to `SCAN_FILE`.  
\- Changed mapping for externalIP from target.ip to principal.ip.  
\- Mapped security_result.category to `SOFTWARE_MALICIOUS` if type is `knownMalware` and elementType is `File`, else if type is `knownMalware` and elementType is not `File` then mapped it to `NETWORK_MALICIOUS`.  
\- Changed mapping for `name` from `principal.process.file.full_path` to `target.file.names`.  
\- Changed mapping for `malwareDataModel` from `principal.process.command_line` to `target.file.full_path`.  
\- Mapped type to security_result.summary.  
\- Mapped status to security_result.action.   
2024-11-29 |  Enhancement:  
\- Added support to parse logs when the LogType is `Malware` and `Malop`.   
2024-01-25 |  Enhancement:  
\- Mapped `cs3Label`, `cs4Label`, `cs5Label`, `deviceCustomDate1Label`, `deviceCustomDate2Label` and `deviceCustomDate3Label` to `security_result.detection_fields`.  
\- Aligned `principal.hostname`, `target.hostname`, `principal.asset.hostname`, and `target.asset.hostname` mappings.  
\- Aligned `principal.ip`, `target.ip`, `principal.asset.ip`, and `target.asset.ip` mappings.   
2023-02-23 |  Enhancement  
\- Mapped `malop_data.elementValues.affectedUsers.elementValues.0.guid` to `principal.user.userid`.  
\- Mapped `malop_data.elementValues.affectedUsers.elementValues.0.name` to `principal.user.user_display_name`.  
\- Mapped `malop_data.elementValues.affectedMachines.elementValues.0.guid` to `principal.asset.asset_id`.  
\- Mapped `malop_data.elementValues.affectedMachines.elementValues.0.name` to `principal.hostname`.  
\- Mapped `malop_data.simpleValues.malopActivityTypes.values.0`, `malop_data.isMalicious` to `security_result.detection_fields`.  
\- Mapped `security_result.alert_state` to `ALERTING` if `is_alert` is `true`.   
2023-02-06 |  Enhancement  
\- Parsed logs ingested in CEF format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
