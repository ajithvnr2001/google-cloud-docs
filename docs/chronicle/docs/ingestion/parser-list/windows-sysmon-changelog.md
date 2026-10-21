---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-sysmon-changelog/
title: Change log for WINDOWS_SYSMON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:00:33.509778+00:00
---

# Change log for WINDOWS_SYSMON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-sysmon-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_SYSMON

Date | Changes  
---|---  
2026-09-01 |  \- `target.process.integrity_level_rid`: Newly set by the value of `IntegrityLevel` raw log field to `target.process.integrity_level_rid` UDM field for EventID 1, 4, 5, 16, 17, 18 based on the below value mapping:  
\- set to `0` when value matches `(?i)(Untrusted)`  
\- set to `4096` when value matches `(?i)(Low)`  
\- set to `8192` when value matches `(?i)(Medium)`  
\- set to `12288` when value matches `(?i)(High)`  
\- set to `16384` when value matches `(?i)(System)`  
\- set to `20480` when value matches `(?i)(Protected)`  
\- `principal.process.integrity_level_rid`: Newly set by the value of `IntegrityLevel` raw log field to `principal.process.integrity_level_rid` UDM field for other EventIDs based on the below value mapping:  
\- set to `0` when value matches `(?i)(Untrusted)`  
\- set to `4096` when value matches `(?i)(Low)`  
\- set to `8192` when value matches `(?i)(Medium)`  
\- set to `12288` when value matches `(?i)(High)`  
\- set to `16384` when value matches `(?i)(System)`  
\- set to `20480` when value matches `(?i)(Protected)`  
2026-05-28 |  \- `principal.user.windows_sid`: Removed mapping of `UserID` from `principal.user.windows_sid` UDM field if user details are present in Event data.  
\- `additional.fields[UserID]`: Mapped `UserID` raw log field with `additional.fields[UserID]` UDM field if user details are present in Event data.  
\- `principal.user.userid`: Removed mapping of `AccountName` from `principal.user.userid` UDM field if user details are present in Event data.  
\- `additional.fields[AccountName]`: Mapped `AccountName` raw log field with `additional.fields[AccountName]` UDM field if user details are present in Event data.   
2025-11-04 |  \- `target.process.file.pe_file.imphash`: Newly mapped `imphash` raw log field with `target.process.file.pe_file.imphash` UDM field.   
2025-09-04 |  \- Added validation for the `/Event/System/Security/@UserID` raw field to handle the case when the value is not a SID.   
2025-02-25 |  \- Added support for the following fields in the XML format:  
Mapped `/Event/EventData/Data/Product` Raw Field to `target.asset.software.name` UDM Field.  
Mapped `/Event/EventData/Data/Company` Raw Field to `target.asset.software.vendor_name` UDM Field.  
Mapped `/Event/EventData/Data/FileVersion` Raw Field to `target.asset.software.version` UDM Field.   
2025-02-03 |  \- Mapped `hostUrl` to `additional.fields`.   
2024-12-03 |  \- Added `gsub` for message, `protocol` , `sourceIp` and `destinationIp`.   
2024-11-28 |  \- Added support for the `OriginalFileName` field and mapped it to `src.process.file.full_path` for `EventID` = 7 and `EventID` = 8.  
\- Added support for `udm_event_type` for `EventID` = 27.   
2024-11-04 |  Enhancement:  
\- Mapped `contents.valu` to `target.resource.name`.  
\- Mapped `ZoneId` to `target.resource.id`.  
\- Mapped `ReferrerUrl` to `additional.fields`.   
2024-10-04 |  \- Added support for the OriginalFileName field and map it to src.process.file.full_path for EventID = 1.   
2024-09-03 |  Enhancement:  
Added a Grok pattern to map the `SourceUser` field value to `principal.user.userid` and `principal.administrative_domain`, and the `TargetUser` field value to `target.user.userid` and `target.administrative_domain`.   
2024-08-02 |  Enhancement:  
\- Mapped `SourceUser` to `principal.user.userid` and `TargetUser` to `target.user.userid`.   
2024-05-01 |  Updated logic for ConfigurationFileHash.   
2024-04-24 |  Updated mapping of `Company`, `Description`, `Product` and `FileVersion` fields to `target.asset.software`.   
2024-03-15 |  Added new attributes and supported for new log formats.   
2024-01-17 |  Added mapping of `SourceProcessGUID`, `TargetProcessGUID` XML log field for `EventID 10`.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-10-27 |  Added mapping for `ProviderGuid`, `IntegrityLevel`, `LogonId`, `ThreadID` and `Channel` raw log fields.  
Enhancements:  
\- Mapped `ProcessID` to `observer.process.pid`  
\- Mapped `ProcessId` to `principal/target.process.pid`  
\- Mapped `CurrentDirectory` to `additional.field.key/value`  
2023-09-06 |  Added support for Microsoft Windows Sysmon `Event ID 29: FileExecutableDetected`.   
2023-01-26 |  Enhancement:  
\- Mapped `FileVersion` to `principal.asset.software.version`.  
\- Mapped `Description` to `principal.asset.software.description`.  
\- Mapped `Product` to `principal.asset.software.name`.  
\- Mapped `Company` to `principal.asset.software.vendor_name`.   
2022-08-12 |  Added mapping of `CurrentDirectory` field for `PROCESS_LAUNCH` events.   
2022-04-09 |  Added support for logs coming with ExecutionProcessID field.   
2022-04-08 |  Added support to XML format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
