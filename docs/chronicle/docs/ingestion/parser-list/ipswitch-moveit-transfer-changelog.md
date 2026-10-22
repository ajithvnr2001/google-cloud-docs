---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-moveit-transfer-changelog/
title: Change log for IPSWITCH_MOVEIT_TRANSFER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:43.500641+00:00
---

# Change log for IPSWITCH_MOVEIT_TRANSFER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-moveit-transfer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IPSWITCH_MOVEIT_TRANSFER

Date | Changes  
---|---  
2025-11-04 |  Enhancement:  
\- Added support for KV log format.  
\- Added support for event type mapping for non-empty FolderPath: added `USER_LOGIN` (auth type MACHINE) for empty action_performed, and specified action_performed must be non-empty for `FILE_UNCATEGORIZED`.  
\- Added support for event mapping for has_target_details == `true`: now sets event_type to `USER_RESOURCE_ACCESS` if Action is `sec_viewlog`, otherwise continues to set `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `LogStamp` and `LogTime` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `TaskID` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Action` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `SourceHost` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `SourceHost` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `SourceFilename` raw log field to `event.idm.read_only_udm.principal.file.full_path`.  
\- `event.idm.read_only_udm.principal.file.names`: Newly mapped `SourceFilenameOnly` raw log field to `event.idm.read_only_udm.principal.file.names`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `DestHost` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `DestHost` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `DestFilename` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `DestFilenameOnly` raw log field to `event.idm.read_only_udm.target.file.names`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `TaskName` raw log field to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `Node` and `SourceNBytes` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `SourceDuration` and `DestDuration` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `NBytes` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ErrCode` raw log field to `event.idm.read_only_udm.additional.fields`.   
2025-09-12 |  Enhancement:  
\- Added new grok patterns to parse the logs.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `product_event` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dstip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `AdminTrust` and `Permission` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action.details`: Newly mapped `log_status` raw log field with `event.idm.read_only_udm.security_result.action.details` UDM field.  
\- Modified the grok pattern to capture the IP address as srcip instead of tgtip.  
\- `event.idm.read_only_udm.target.ip`:Removed mapping of `tgtip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field as it was a source IP.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field-  
\- `NETWORK_CONNECTION`: Added support for the event `NETWORK_CONNECTION` when `has_principal` and `has_target` are true.  
\- `USER_UNCATEGORIZED`: Added support for the event `USER_UNCATEGORIZED` when `Username` and `username` are present.  
\- `STATUS_UPDATE` : Added support for the event `STATUS_UPDATE` when `has_principal` is `true`.  
\- `USER_RESOURCE_ACCESS` : Added support for the event `USER_RESOURCE_ACCESS` when `target_application` is having `SQL`.   
2024-04-22 |  Bug-Fix:  
\- Mapped `column1` to `metadata.event_timestamp`.   
2023-08-18 |  Enhancement:  
\- Added Grok pattern for verifying `principal.ip` and `target.ip`.  
\- Mapped `fileName` to `target.file.full_path`.  
\- Added conditional check for `event_type` `FILE_CREATION`, `FILE_DELETION`, `STATUS_UPDATE`.   
2023-07-19 |  \- Added support for CSV logs.   
2023-02-03 |  Enhancement:  
\- Added Grok pattern for JSON logs.  
\- Mapped `EventReceivedTime` to `event.timestamp`.  
\- Mapped `SourceModuleName` to `observer.resource.attribute.labels`.  
\- Mapped `SourceModuleType` to `observer.application`.  
\- Mapped `SourceName` to `metadata.product_event_type`.  
\- Mapped `Severity` to `security_result.`.  
\- Mapped `Hostname` to `principal.hostname`.  
\- Mapped `Channel` to `security_result.about.resource.attribute.labels`.  
\- Mapped `AgentVersion` to `metadata.version`.  
\- Mapped `IPAddress` to `principal.ip`.   
2022-10-07 |  Bugfix - Added new Grok pattern for unparsed logs.  
\- Added new event type - FILE_DELETION when FolderPath is not null and action_performed is Delete File.  
\- Added new event type - FILE_UNCATEGORIZED when FolderPath is not null and action_performed is not Delete File.  
\- Mapped FolderPath/FileName to `target.file.full_path`.  
\- Mapped XFerSize,Error,AgentBrand to `additional.fields`.  
\- Mapped FolderID,FileID,FileName to `target.resource.attribute.labels`.  
\- Mapped company_name to `principal.user.company_name`.  
\- Mapped action_performed to `metadata.description`.  
\- Mapped ID to `target.process.pid`.  
\- Mapped InstID to `metadata.product_log_id`.   
2022-06-22 |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
