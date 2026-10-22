---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-epm-changelog/
title: Change log for CYBERARK_EPM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:33.205078+00:00
---

# Change log for CYBERARK_EPM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-epm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERARK_EPM

Date | Changes  
---|---  
2025-09-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `userIsAdmin`, `workingDirectory` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `hash` and `sourceProcessHash` raw log fields had been conveted to lowercase to get the correct UDM field mapping.  
\- Added regex for the `sourceProcessHash` raw log field to get the correct UDM field mapping with `event.idm.read_only_udm.target.process.parent_process.file.sha1` UDM field.  
\- Only mapped `fileSize` raw log field to `event.idm.read_only_udm.target.file.size` UDM field only if it was not `null` and should be greater than `0`.   
2025-06-03 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `exposeduser.username`, `exposeduser.source`, `exposeduser.domain` ,`sourceProcessPublisher`, and `exposeduser.accountName` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `evidencesuser.accessedObject.name`, `evidencesuser.accessedProcess.commandLine`, `evidencesuser.accessedProcess.hash`, `evidencesuser.accessedProcess.publisher`, `evidencesuser.accessedProcess.username`, `evidencesuser.accessedProcess.hashAlgorithm`, `evidencesuser.accessedProcess.fullImageName`, `evidencesuser.evidenceCounter`, `evidencesuser.datetimeUTC`, `evidencesuser.evidenceAction`, `evidencesuser.additionalData`, and `evidencesuser.comment` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `displayName` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `policyName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `processCommandLine` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.command_line: Newly mapped `sourceProcessCommandLine` raw log field with `event.idm.read_only_udm.target.process.parent_process.command_line` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `sourceProcessUsername` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.process.parent_process.file.sha1: Newly mapped `sourceProcessHash` raw log field with `event.idm.read_only_udm.target.process.parent_process.file.sha1` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `threatProtectionActionId`, `skippedCount`, `eventCount`, `sourceProcessSigner`, `deceptionType`, `winEventType`, `winEventRecordId`, `logonAttemptTypeId`, and `logonStatusId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Removed `fileDescription` raw log field mapping from `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `fileDescription` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2025-05-22 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `accessAction`, `accessTargetType`, `agentEventCount`, `modificationTime`, `arrivalTime`, `originalFileName`, `owner`, `packageName`, `publisher`, `setID`, `sourceType`, and `threatProtectionAction` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped `lastEventDate` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `agentId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.user.company_name: Newly mapped `company` raw log field with `event.idm.read_only_udm.principal.user.company_name` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `computerName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `computerName` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `fileDescription` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.process.file.names: Newly mapped `fileName` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `filePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `fileQualifier` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `fileSize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.target.asset.software.version: Newly mapped `fileVersion` raw log field with `event.idm.read_only_udm.target.asset.software.version` UDM field.  
\- event.idm.read_only_udm.target.file.sha1: Newly mapped `hash` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `justification` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `operatingSystemType` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `productName` and `productVersion` raw log fields with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `sourceName` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` with `USER_UNCATEGORIZED` when `has_principal_user` is `true` and `STATUS_UPDATE` when `has_principal` is `true` else `GENERIC_EVENT`.  
\- event.idm.read_only_udm.metadata.vendor_name: Set `event.idm.read_only_udm.metadata.vendor_name` with `CYBERARK`.  
\- event.idm.read_only_udm.metadata.product_name: Set `event.idm.read_only_udm.metadata.product_name` with `EPM`.   
2023-08-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
