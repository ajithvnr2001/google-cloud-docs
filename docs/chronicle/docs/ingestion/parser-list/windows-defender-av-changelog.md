---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-av-changelog/
title: Change log for WINDOWS_DEFENDER_AV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:28.092403+00:00
---

# Change log for WINDOWS_DEFENDER_AV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/windows-defender-av-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WINDOWS_DEFENDER_AV

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.description`, `event.idm.read_only_udm.security_result.summary`: Removed mapping of `EventID` from `event.idm.read_only_udm.security_result.description` and `event.idm.read_only_udm.security_result.summary` UDM fields as it represents an additional event identifier rather than security result details.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `EventID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.registry.registry_key`: Removed mapping of `Path` from `event.idm.read_only_udm.target.registry.registry_key` UDM field when `Path` starts with `file`, `webfile`, or `amsi` as it represents the target file path.  
\- `event.idm.read_only_udm.target.file.full_path`, `event.idm.read_only_udm.target.process.file.full_path`: Mapped `Path` raw log field with `event.idm.read_only_udm.target.file.full_path` and `event.idm.read_only_udm.target.process.file.full_path` UDM fields when `Path` starts with `file`, `webfile`, or `amsi`.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` UDM field to `SCAN_FILE` for `EventID` in `1006`-`1008`, `1011`, and `1116`-`1120` when `has_target_file` is `true`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product_name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field when `EventID` is `1011`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `ProductVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `SeverityID`, `CategoryID`, `Security_Intelligence_Version`, `Engine_Version`, `SeverityValue` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `ThreatID` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `SourceModule` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `ProviderGuid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `User` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field when `AccountName` is empty and `UserID` is present.  
\- Added support for `ISO8601` timestamp format in `EventReceivedTime` raw log field.   
2026-08-07 |  Enhancement -  
\- `event.idm.read_only_udm.security_result.severity`: Removed mapping of `Severity` from `event.idm.read_only_udm.security_result.severity` UDM field as it is redundant.  
\- `event.idm.read_only_udm.target.hostname`: Removed mapping of `target.hostname` from `event.idm.read_only_udm.target.hostname` UDM field when hostname is not present.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Removed mapping of `ProviderGuid` from `event.idm.read_only_udm.metadata.product_deployment_id` UDM field as it represents the principal resource data.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `ProviderGuid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Removed mapping of `description` from `event.idm.read_only_udm.metadata.description` UDM field as it represents the security result details.  
\- `event.idm.read_only_udm.security_result.summary`: Mapped `description` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`:  
\- When `EventID` is 1151, updated the value to `EventID: 1151 MALWAREPROTECTION_SERVICE_HEALTH_REPORT`.  
\- When `EventID` is 2001, updated the value to `EventID: 2001 MALWAREPROTECTION_SIGNATURE_UPDATE_FAILED`.  
\- When `EventID` is 5007, updated the value to `EventID: 5007 MALWAREPROTECTION_CONFIG_CHANGED`.  
\- Added a conditional check before already existing mapping of `Keywords` to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.summary`:  
\- If `EventID` is 1151, Set the value to `Endpoint Protection client health report (time in UTC)`.  
\- If `EventID` is 2001, Set the value to `The security intelligence update failed`.  
\- If `EventID` is 5007, Set the value to `The antimalware platform configuration changed`.  
\- `event.idm.read_only_udm.principal.user.account_type`: When `AccountType` is User, Newly mapped the value `DOMAIN_ACCOUNT_TYPE` to `event.idm.read_only_udm.principal.user.account_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `antivirus_security_intelligence_version`, `antispyware_security_intelligence_version`, `latest_engine_version`, `engine_up_to_date`, `latest_platform_version`, `platform_up_to_date`, `previous_security_intelligence_version`, `update_source`, `security_intelligence_type`, `update_type`, `feature_name`, `failure_reason`, `failure_id`, `Recommendation`, `security_intelligence_type_index`, `update_state_index`, `update_source_index`, `EventType`, `Version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `error_code`, `error_description`, `update_state`, `old_value`, `new_value` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product_name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `source_path` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `EventReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `SeverityValue` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2026-04-06 |  Enhancement -  
\- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `Threat Name` from `event.idm.read_only_udm.security_result.summary` UDM field when `EventID` is `1116` or `1117` in order to introduce a more event specific mapping.  
\- `event.idm.read_only_udm.security_result.summary`: Mapped the `EventID` raw log field to the `event.idm.read_only_udm.security_result.summary` UDM field when `EventID` is `1116` or `1117`, since `EventID` more accurately represents the event summary.  
\- `event.idm.read_only_udm.security_result.description`: Removed mapping of `EventID` from `event.idm.read_only_udm.security_result.description` UDM field when `EventID` is `1116` or `1117` in order to introduce a more event specific mapping.  
\- `event.idm.read_only_udm.security_result.description`: Updated the value based on `EventID`:  
\- If `EventID` is `1116`: `Microsoft Defender Antivirus detected malware or other potentially unwanted software.`  
\- If `EventID` is `1117`: `Microsoft Defender Antivirus performed an action to protect your system from malware or other potentially unwanted software.`  
\- If `EventID` is `1118`: `Microsoft Defender Antivirus attempted to perform an action to protect your system from malware or other potentially unwanted software, but the action failed.`  
\- If `EventID` is `1119`: `Microsoft Defender Antivirus encountered a critical error when trying to take action on malware or other potentially unwanted software. There are more details in the event message.`  
\- If `EventID` is `1120`: `Microsoft Defender Antivirus deduced the hashes for a threat resource.`  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `EventRecordID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Product Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `ProviderGuid` raw log field with `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `xmlns` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `Threat Resource Path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `Hashes` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `RenderingInfoLevel` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `Action Name` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `Detection Time` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `Threat ID` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Remediation User`, `Status Description`, `Action ID`, `Additional Actions ID`, `Additional Actions String`, `Category ID`, `Detection ID`, `Engine Version`, `Error Code`, `Error Description`, `Execution ID`, `Execution Name`, `Origin ID`, `Origin Name`, `Post Clean Status`, `Pre Execution Status`, `Security Intelligence Version`, `Severity ID`, `Source ID`, `State`, `Status Code`, `Type ID`, `Type Name` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Level`, `Culture`, `Keywords`, `Opcode`, `Product Name`, `Provider Name`, `RenderingInfoMessage`, `Service`, `Task`, `Version` and `Security UserID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `EventID` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field when `EventID` is `1118`, `1119` or `1120`.  
\- Added `on_error` handling to the type conversion of the `ProcessID` raw log field, which is mapped to the `event.idm.read_only_udm.principal.process.pid` UDM field.   
2025-02-27 |  Enhancement -  
\- Added `gsub` to parse unparsed logs.  
\- Changed mapping of `Path` from `target.process.file.full_path` to `target.registry.registry_key`.  
\- Added a conditional check when mapping `event_type` to `SCAN_HOST`, `SCAN_FILE`, and `GENERIC_EVENT`.   
2025-02-14 |  Enhancement -  
\- Added support for new JSON log format.   
2024-01-30 |  Bug-Fix -  
\- Added `on_error` check for date filter to parse UNIX and UNIX_MS format.   
2023-09-04 |  Bug-Fix -  
\- Parsed date by adding `rebase` as `true`.  
\- Additionally mapped the following fields:  
\- `UserID` is mapped to `principal.user.userid`.  
\- `Category Name` mapped to `security_result.category_details`.  
\- `ProviderGuid` mapped to `metadata.product_deployment_id`.  
\- `RecordNumber` mapped to `metadata.product_log_id`.  
\- `ActivityID` mapped to `security_result.detection_fields`.  
\- `ProcessID` mapped to `principal.process.pid`.  
\- `Domain` mapped to `principal.administrative_domain`.  
\- `FWLink` mapped to `metadata.url_back_to_product`.  
\- `Path` mapped to `target.process.file.full_path`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
