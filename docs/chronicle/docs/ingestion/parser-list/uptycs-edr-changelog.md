---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/uptycs-edr-changelog/
title: Change log for UPTYCS_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:25.392791+00:00
---

# Change log for UPTYCS_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/uptycs-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UPTYCS_EDR

Date | Changes  
---|---  
2026-08-28 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `alertTime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `upt_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `assetGroupName` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `metadata.Command Line` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `localIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `metadata.Process Path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `metadata.Process ID` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `metadata.Login Name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `assetId` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `metadata.SHA256` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.target.process.product_specific_process_id`: Newly mapped `metadata.Uptycs RID` raw log field with `event.idm.read_only_udm.target.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `metadata.User` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.signature_info.codesign.id`: Newly mapped `metadata.Version Information.Signature` raw log field with `event.idm.read_only_udm.target.process.file.signature_info.codesign.id` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `gateway` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `alertId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `metadata.Process Name` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `metadata.Start Time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.file.names`: Newly mapped `metadata.Parents.exe_name` raw log field with `event1.idm.read_only_udm.target.process.parent_process.file.names` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `metadata.Parents.pid` raw log field with `event1.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.parent_process.pid`: Newly mapped `metadata.Parents.ppid` raw log field with `event1.idm.read_only_udm.target.process.parent_process.parent_process.pid` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.command_line`: Newly mapped `metadata.Parents.cmdline` raw log field with `event1.idm.read_only_udm.target.process.parent_process.command_line` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.product_specific_process_id`: Newly mapped `metadata.Parents.upt_rid` raw log field with `event1.idm.read_only_udm.target.process.parent_process.product_specific_process_id` UDM field.  
\- `event1.idm.read_only_udm.target.process.parent_process.file.sha256`: Newly mapped `metadata.Parents.sha256` raw log field with `event1.idm.read_only_udm.target.process.parent_process.file.sha256` UDM field.  
\- `event1.idm.read_only_udm.target.user.windows_sid`: Newly mapped `metadata.Parents.sid` raw log field with `event1.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event1.idm.read_only_udm.target.user.userid`: Newly mapped `metadata.Parents.uname` raw log field with `event1.idm.read_only_udm.target.user.userid` UDM field.  
\- `event1.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `metadata.Parents.proc_time` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event1.idm.read_only_udm.target.user.user_display_name`: Newly mapped `metadata.Parents.login_name` raw log field with `event1.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `type`, `key`, `value`, `assetGroupId`, `metadata.Key`, `metadata.Value`, `metadata.Version Information.StrucVersion`, `metadata.Version Information.FileVersion`, `metadata.Version Information.ProductVersion`, `metadata.Version Information.FileFlagsMask`, `metadata.Version Information.FileFlags`, `metadata.Version Information.FileOS`, `metadata.Version Information.FileType`, `metadata.Version Information.FileDate`, `metadata.Version Information.StringFileInfo.LangID`, `metadata.Version Information.StringFileInfo.CompanyName`, `metadata.Version Information.StringFileInfo.FileDescription`, `metadata.Version Information.StringFileInfo.InternalName`, `metadata.Version Information.StringFileInfo.LegalCopyright`, `metadata.Version Information.StringFileInfo.OriginalFilename`, `metadata.Version Information.StringFileInfo.ProductName`, `metadata.Version Information.VarFileInfo.Translation`, `metadata.eventTags` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event1.idm.read_only_udm.additional.fields`: Newly mapped `metadata.Parents.proc_time_hr`, `metadata.Parents.uid`, `metadata.Parents.session_id`, `metadata.Parents.signature_status`, `metadata.Parents.signed`, `metadata.Parents.integrity_level`, `metadata.Parents.partial` raw log fields with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `code`, `metadata.Action`, `metadata.Signed`, `metadata.Integrity Level`, `metadata.Signature Status`, `metadata.Version Information.type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `NETWORK_DNS` to `event.idm.read_only_udm.metadata.event_type` UDM field when `message` contains principal machine data and DNS data and target machine data, else if mapped to `PROCESS_LAUNCH` when `message` contains principal machine data and target process data, else if mapped to `USER_UNCATEGORIZED` when `message` contains principal machine data and principal user data, else if mapped to `STATUS_UPDATE` when `message` contains only principal machine data, else mapped to `GENERIC_EVENT`.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `upt_asset_group_id` from `principal.user.groupid` to `principal.user.group_identifiers`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
