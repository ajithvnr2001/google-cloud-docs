---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatlocker-changelog/
title: Change log for THREATLOCKER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:35.848472+00:00
---

# Change log for THREATLOCKER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatlocker-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THREATLOCKER

Date | Changes  
---|---  
2026-07-14 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.id`: Removed mapping of `organizationId` raw log field from `event.idm.read_only_udm.principal.resource.id` UDM field as it is a deprecated field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `organizationId` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `networkDirection` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `osType` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `threatSeverityLevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `dateTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field as a fallback if `t` is not present.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceIPAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationIPAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `fp` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field when `at` is `powershell`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eActionLogId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `organizationName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `policyId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `hash` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `processName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `parentProcessId` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `parentProcessName` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `edgeStoreUrl`, `chromeStoreUrl`, `firefoxStoreUrl` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policyName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.serial`: Newly mapped `serialNumber` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.serial` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.subject`: Newly mapped `certificates.subject` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.subject` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256Hash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `processId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `fullPath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.outcomes`: Newly mapped `isMonitorMode` raw log field with `event.idm.read_only_udm.security_result.outcomes` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `notes` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `applicationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.category`: Newly mapped `deviceType` raw log field with `event.idm.read_only_udm.principal.asset.category` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `processPath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `encryptionStatus` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dateTimeImported`, `actionTypeId`, `actionId`, `remotePresence`, `createdByProcess`, `remotePresenceThreatLockerDetected`, `remotePresenceText`, `certExists`, `certText`, `applicationOrganizationId`, `applicationIsBuiltIn`, `policyExists`, `policyEnabled`, `storagePolicyExists`, `nacPolicyExists`, `secureNetworkPolicyExists`, `twPolicyExists`, `webControlPolicyExists`, `cmPolicyExists`, `optionToRequest`, `allowPermitVendorButton`, `reportMissing`, `isVirusTotalUnavailable`, `deleteFileRequestSent`, `isAccessDevice`, `allowFileUpload`, `canViewOnSystemLookup`, `hasPolicyData`, `monitorMode`, `learningModeEndDate`, `policyLocation`, `policyOrganizationId`, `applicationId`, `encryption`, `effectiveAction`, `virusTotalCheckName`, `virusTotalCheckArgument`, `isExtension`, `actionLogCreatedByProcesses`, `totalCount`, `lastSortValue`, `groupByCount`, `batchId`, `isProtectedProcess`, `memoryBytes`, `parentProcessApplicationId`, `parentProcessApplicationName`, `parentProcessApplicationOrganizationId`, `hasViewComputerPermission`, `systemLookupUrl`, `threatLockerItem`, `integrationTypeId`, `isCloudLog`, `isCloudActionType`, `engineRatings`, `actionLogId`, `threatLockerItem.d`, `threatLockerItem.at`, `threatLockerItem.aid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `certificates.validCert` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2023-06-18 |  Bug-Fix - Modified Grok pattern to fetch source IP address and destination IP address for `fp` when `at` is `network`.   
2023-05-24 |  Enhancement - Modified mapping of `security_result.outcomes.key` to `Monitor mode status` and value to `monitor mode on` and `monitor mode off`.  
\- Added mapping `s256` to `target.file.sha256` and `target.process.file.sha256`.  
\- When `at` is `network`, mapped `metadata.event_type` to `NETWORK_CONNECTION`  
. Mapped `fp` to `target.hostname`, `target.ip` and `target.port`.  
\- When `at` is `execute`, `install`, mapped `metadata.event_type` to `PROCESS_LAUNCH`.  
. Mapped `fp` to `target.process.file.full_path`.  
\- When `at` is `newprocess`, mapped `metadata.event_type` to `PROCESS_OPEN`.  
. Mapped `fp` to `target.process.file.full_path`.  
\- When `at` is `write`, mapped `metadata.event_type` to `FILE_MODIFICATION`.  
. Mapped `fp` to `target.file.full_path`.  
\- When `at` is `read`, mapped `metadata.event_type` to `FILE_READ`.  
. Mapped `fp` to `target.file.full_path`.  
\- When `at` is `delete`, mapped `metadata.event_type` to `FILE_DELETION`.  
. Mapped `fp` to `target.file.full_path`.  
\- When `at` is `move`, mapped `metadata.event_type` to `FILE_MODIFICATION`.  
. Mapped `fp` to `target.file.full_path`.  
\- When `at` is `registry`, mapped `metadata.event_type` to `REGISTRY_UNCATEGORIZED`.  
. Mapped `fp` to `target.registry.registry_key`.   
2022-12-16 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
