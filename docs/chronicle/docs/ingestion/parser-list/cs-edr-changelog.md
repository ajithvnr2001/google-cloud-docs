---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-edr-changelog/
title: Change log for CS_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:38.663354+00:00
---

# Change log for CS_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CS_EDR

Date | Changes  
---|---  
2026-08-25 |  \- `principal.ip` and `principal.asset.ip`: Removed the mapping of `RemoteAddressIP4` for event `UserLogonFailed2` to prevent redundancy, as it is already accurately mapped to `target.ip` and `target.asset.ip`.   
2026-07-09 |  \- `target.user.attribute.labels[user_logon_flags]`: Newly mapped `UserLogonFlags` raw log field with `target.user.attribute.labels[user_logon_flags]` UDM field for event type `UserLogon`.   
2026-06-22 |  \- `network.dns.answers.name`: Removed mapping of `IP4Records`, `IP6Records` and `FirstIP4Record` raw log field from `network.dns.answers.name`. `IP4Records` and `IP6Records` are now mapped to `network.dns.answers.data`. `FirstIP4Record` is part of `IP4Records` which is already mapped to `network.dns.answers.data`, apart from that `FirstIP4Record` is also mapped to `additional.fields[first_ip4_record]`.  
\- `network.dns.answers.data`: Mapped `IP4Records` and `IP6Records` raw log fields with `network.dns.answers.data` UDM field.  
\- Removed the merging of `CNAMERecords` into `IP4Records` and adjusted the JSON parsing logic for `IP4Records`.   
2026-06-08 |  \- `target.file.names`: Removed mapping of `ZoneIdentifier` from `target.file.names` UDM field as it is not a file name but a file attribute and it must be preserved as custom telemetry.  
\- `additional.fields[ZoneIdentifier]`: Mapped `ZoneIdentifier` raw log field with `additional.fields[ZoneIdentifier]` UDM field.   
2026-05-19 |  \- `security_result.action`: Removed mapping of `QUARANTINE` from `security_result.action` UDM field when the raw log field `DCPolicyAction` has value `2` and mapped `ALLOW_WITH_MODIFICATION` instead.  
\- `security_result.details`: Removed mapping of `DcPolicyAction` from `security_result.details` UDM field and mapped `MASSSTORAGE` value when the raw log field `DCPolicyAction` has value `2`.   
2026-05-05 |  \- `principal.hostname`: Newly mapped `ComputerName` raw log field with `principal.hostname` UDM field for event `ProcessRollup2Stats`.  
\- `principal.asset.hostname`: Newly mapped `ComputerName` raw log field with `principal.asset.hostname` UDM field for event `ProcessRollup2Stats`.   
2026-04-30 |  \- General bug-fix: Resolved event validation issue for event `HeapSprayAttempt`.   
2026-04-09 |  \- `principal.hostname`: Newly mapped `ComputerName` raw log field with `principal.hostname` UDM field for event `ProcessRollup2`.  
\- `principal.asset.hostname`: Newly mapped `ComputerName` raw log field with `principal.asset.hostname` UDM field for event `ProcessRollup2`.   
2026-03-23 |  \- `target.file.md5`: Removed mapping of `MD5HashData` from `target.file.md5` UDM field for event `ClassifiedModuleLoad`.  
\- `target.process.file.md5`: Mapped `MD5HashData` raw log field with `target.process.file.md5` UDM field for event `ClassifiedModuleLoad`.   
2026-03-17 |  \- `security_result.risk_score`: Newly mapped raw log field `RiskScore` with `security_result.risk_score` UDM field.   
2026-01-30 |  \- `AutomatedLeadSummaryEvent`: Added support for the event `AutomatedLeadSummaryEvent` and relevant corresponding raw log fields.  
\- `security_result.action`: Mapping `security_result.action` for `QuarantinedFile`, `OdsMaliciousFileFound`, `LfoUploadDataComplete`, and `LfoUploadDataFailed`.   
2026-01-20 |  \- `principal.hostname`: Newly mapped `ComputerName` raw log field with `principal.hostname` UDM field for event `SyntheticProcessRollup2` and `DnsRequest`.  
\- `principal.asset.hostname`: Newly mapped `ComputerName` raw log field with `principal.asset.hostname` UDM field for event `SyntheticProcessRollup2` and `DnsRequest`.   
2026-01-16 |  \- `DotnetModuleLoadDetectInfo`: Added support for the event `DotnetModuleLoadDetectInfo` and relevant corresponding raw log fields.   
2025-12-24 |  \- `security_result.attack_details`: Added support for `MitreAttack` array.  
\- `security_result.action`: Included all the possible values of `PatternDispositionValue` raw log field to populate `security_result.action` UDM field.   
2025-12-12 |  \- `security_result.attack_details`: Added support for the `Attacks` array which contains `Tactic` and `Technique` values.   
2025-11-19 |  \- principal.process.file.full_path : Newly mapped `TargetImageFileName` raw log field with `principal.process.file.full_path` UDM field for event `ClassifiedModuleLoad`.   
2025-10-29 |  \- principal.user.userid : Newly mapped `UserName` raw log field enum value with `principal.user.userid` UDM field for event `CommandHistory`.   
2025-09-15 |  \- principal.process.file.full_path: Removed mapping of `ContextBaseFileName` from `principal.process.file.full_path` UDM field.  
\- principal.process.file.names: Mapped `ContextBaseFileName` raw log field with `principal.process.file.names` UDM field, which enables the enrichment process to later fill in principal.process.file.full_path using the cache.   
2025-09-11 |  metadata.event_type: Updated `metadata.event_type` to `REGISTRY_DELETION` for registry-related events where the raw field `RegOperationType` is `2` or `102`.   
2025-09-05 |  Added support for `MitreAttack` array for event `IdpDetectionSummaryEvent`.   
2025-09-04 |  \- `MacroDetectInfo`: Added support for the event `MacroDetectInfo` and relevant corresponding raw log fields.   
2025-08-26 |  \- additional.fields[offset]: Newly mapped `offset` raw log field with `additional.fields[offset]` UDM field for event `UserActivityAuditEvent`.  
\- additional.fields[OperationName]: Newly mapped `OperationName` raw log field with `additional.fields[OperationName]` UDM field for event `UserActivityAuditEvent`.  
\- Removed duplicate field mappings for raw log fields that were previously present in both `about.labels` and `additional.fields`. All such mappings have been consolidated under `additional.fields`.  
\- For `IdentityProtectionEvent`, the raw log field `Username` is now parsed in the `DOMAIN\userid` format (if present) and mapped to `principal.administrative_domain` and `principal.user.userid`.  
\- metadata.event_type: Updated `metadata.event_type` to `REGISTRY_*` based on the value of the raw log field `RegOperationType` for all registry-related events.   
2025-08-22 |  \- target.resource.attribute.labels: Newly mapped `VolumeLabel` raw log field with `target.resource.attribute.labels` UDM field for event `RemovableMediaVolumeMounted`.   
2025-08-20 |  Enhanced consistency for raw log fields, now maps directly to `target` entity support for Process events:  
\- target.process.file.authentihash Updated Mapping `AuthenticodeHashData` raw log field with `target.process.file.authentihash` UDM field from `principal.process.file.authentihash`.  
\- target.process.command_line Updated Mapping `CommandLine` raw log field with `target.process.command_line` UDM field from `principal.process.command_line`.  
\- target.process.parent_process.file.names Updated Mapping `GrandParentBaseFileName` raw log field with `target.process.parent_process.file.names` UDM field from `principal.process.parent_process.file.names`.  
\- target.process.file.full_path Updated Mapping `ImageFileName` raw log field with `target.process.file.full_path` UDM field from `principal.process.file.full_path`.  
\- target.process.file.md5 Updated Mapping `MD5HashData` raw log field with `target.process.file.md5` UDM field from `principal.process.file.md5`.  
\- target.process.file.exif_info.original_file Updated Mapping `OriginalFilename` raw log field with `target.process.file.exif_info.original_file` UDM field from `principal.process.file.exif_info.original_file`.  
\- target.process.file.names Updated Mapping `ParentBaseFileName` raw log field with `target.process.file.names` UDM field from `principal.process.file.names`.  
\- target.process.parent_process.product_specific_process_id Updated Mapping `ParentProcessId` raw log field with `target.process.parent_process.product_specific_process_id` UDM field from `principal.process.parent_process.product_specific_process_id`.  
\- target.process.file.sha256 Updated Mapping `SHA256HashData` raw log field with `target.process.file.sha256` UDM field from `principal.process.file.sha256`.  
\- target.process.command_line Updated Mapping `ParentCommandLine` raw log field with `target.process.command_line` UDM field from `principal.process.command_line`.  
\- target.process.parent_process.file.full_path Updated Mapping `ParentImageFileName` raw log field with `target.process.parent_process.file.full_path` UDM field from `principal.process.parent_process.file.full_path`.  
\- target.application Updated Mapping `AppIdentifier` raw log field with `target.application` UDM field from `principal.application`.  
\- target.group.product_object_id Updated Mapping `GID` raw log field with `target.group.product_object_id` UDM field from `principal.group.product_object_id`.  
\- principal.process.product_specific_process_id Added Mapping `ParentProcessId` raw log field with `principal.process.product_specific_process_id` UDM field Where `ContextProcessId` raw log field is empty.  
\- The following mappings are changed in order to introduce more accurate mappings.   
2025-08-11 |  \- `IdentityProtectionEvent`: Added support for the event `IdentityProtectionEvent` and relevant corresponding raw log fields.  
\- security_result.description: Newly mapped `Description` raw log field with `security_result.description` UDM field for event `IdpDetectionSummaryEvent`.  
\- security_result.detection_fields[most_recent_activity_time_stamp]: Newly mapped `MostRecentActivityTimeStamp` raw log field with `security_result.detection_fields[most_recent_activity_time_stamp]` UDM field for event `IdpDetectionSummaryEvent`.  
\- additional.fields[activity_browser]: Newly mapped `ActivityBrowser` raw log field with `additional.fields[activity_browser]` UDM field for event `IdpDetectionSummaryEvent`.  
\- metadata.url_back_to_product: Newly mapped `FalconHostLink` raw log field with `metadata.url_back_to_product` UDM field for event `IncidentSummaryEvent`.  
\- principal.user.userid: Newly mapped `UserId` raw log field with `principal.user.userid` UDM field for event `AuthActivityAuditEvent`.   
2025-07-31 |  `ScriptFileWrittenInfo`: Added support for the event `ScriptFileWrittenInfo` and relevant corresponding raw log fields.  
\- `TargetFileName`: Newly mapped `TargetFileName` raw log field with `target.file.full_path` UDM field  
\- `ScriptContent` : Newly mapped `ScriptContent` raw log field with `additional.fields[script_content]` UDM field  
\- `FileFormatString`: Newly mapped `FileFormatString` raw log field with `additional.fields[file_format_string]` UDM field  
\- `OriginalContentLength`: Newly mapped `OriginalContentLength` raw log field with `target.file.size` UDM field  
\- `SHA256HashData`: Newly mapped `SHA256HashData` raw log field with `target.file.sha256` UDM field  
\- `WritingProcessId`: Newly mapped `WritingProcessId` raw log field with `target.process.pid` UDM field  
\- `CscStatus`: Newly mapped `CscStatus` raw log field with `additional.fields[csc_status]` UDM field   
2025-07-30 |  \- additional.fields: Newly mapped `IdpEntityPreviousRiskScoreSeverity` raw log field with `additional.fields` UDM field.  
\- additional.fields: Newly mapped `IdpEntityRiskScoreSeverity` raw log field with `additional.fields` UDM field.  
\- additional.fields: Newly mapped `IdpEntityRiskScoreChangeType` raw log field with `additional.fields` UDM field.  
\- additional.fields: Newly mapped `IdpEntityType` raw log field with `additional.fields` UDM field.   
2025-07-08 |  \- Corrected typo: changed `FalconGrouppingTags` to `FalconGroupingTags`.   
2025-07-01 |  \- additional.fields: Removed mapping of `FalconHostLink` from `additional.fields` UDM field  
\- metadata.url_back_to_product: Mapped `FalconHostLink` raw log field with `metadata.url_back_to_product` UDM field   
2025-06-26 |  \- about.resource.product_object_id: Newly mapped `cid` raw log field with `about.resource.product_object_id` UDM field  
\- about.resource.resource_type: Mapped `CLOUD_ORGANIZATION` with `about.resource.resource_type` UDM field.   
2025-06-16 |  \- target.namespace: Removed mapping of `WmiNamespaceName` from `target.namespace` UDM field.  
\- additional.fields: Mapped `WmiNamespaceName` raw log field with `additional.fields` UDM field.   
2025-05-15 |  \- Enhanced the backward compatibility support for the `IncidentSummaryEvent` event   
2025-04-09 |  \- additional.fields.con_host_id: Newly mapped `ConHostId` raw log field with `additional.fields` UDM field.  
\- additional.fields.cycle_time: Newly mapped `CycleTime` raw log field with `additional.fields` UDM field.  
\- additional.fields.max_thread_count: Newly mapped `MaxThreadCount` raw log field with `additional.fields` UDM field.  
\- additional.fields.kernel_time: Newly mapped `KernelTime` raw log field with `additional.fields` UDM field.  
\- additional.fields.user_time: Newly mapped `UserTime` raw log field with `additional.fields` UDM field.  
\- additional.fields.context_timestamp: Newly mapped `ContextTimeStamp` raw log field with `additional.fields` UDM field.   
2025-04-01 |  \- Promoted CS_EDR gold parser to default.  
\- This version includes many changes to improve the parser mappings (parser overhaul) - contact your Google representative to get a detailed list with all changes  
\- This version will have an extended RC period - we encourage you to opt-in and make the required adjustments before it'll be automatically promoted to Default   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
