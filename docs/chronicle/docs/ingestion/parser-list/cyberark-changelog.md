---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-changelog/
title: Change log for CYBERARK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:02.644352+00:00
---

# Change log for CYBERARK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERARK

Date | Changes  
---|---  
2026-09-21 |  Enhancement:  
\- Added a grok pattern on `fname` to extract `file_name`.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `file_name` log field with `event.idm.read_only_udm.target.file.names` UDM field.   
2026-08-17 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `PolicyID` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `LogonDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `Address` raw log field with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM fields when it's a valid IP.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Address` raw log field with `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `CPMStatus` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.resource_subtype: Newly mapped `DeviceType` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.   
2026-04-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `event_msg.created` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-01-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `datetime` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Issuer` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Message` raw log field(s) with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Station` raw log field(s) with `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `MessageID` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Safe` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: If `Severity` is Info, updated to INFORMATIONAL.  
\- New grok pattern added to parse datetime, host, and kv_pairs from raw logs.  
\- New kv filter added to parse the kv_pairs field using ; as a field splitter and = as a value splitter.   
2025-12-30 |  \- Modified grok pattern to handle log formats with an optional leading syslog priority.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cn1` raw log field to `event.idm.read_only_udm.additional.fields`, using the value of the `cn1Label` raw log field as the key.   
2025-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly Mapped `usrName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly Mapped `Safe` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly Mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly Mapped `GatewayStation` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly Mapped `Reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly Mapped `Location` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly Mapped `File` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `security_result.detection_fields`: Newly Mapped `RequestId` raw log field with `security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result`: Newly Mapped `sev` raw log field with `event.idm.read_only_udm.security_result` UDM field.  
\- Added gsub to replace `\\t` with `#`.  
\- Added a grok pattern to parse unparsed logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `Category`, `ExtraDetails`, `CAPolicy`, `status`, `class_name`, `vault_name`, `timeout`, `data_socket`, `control_socket`, `pasvc_action`, `line_number` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly Mapped `ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly Mapped `file_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly Mapped `tid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly Mapped `pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly Mapped `date` and `time` raw log field `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description` : Newly Mapped `EventMessage` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- Removed redundant code for event.idm.read_only_udm.security_result.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly Mapped `SourceUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly Mapped `TargetUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly Mapped `user_name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.   
2024-06-14 |  Enhancement:  
\- Added a regex pattern to map `msg` to `security_result.description`.   
2024-05-21 |  Enhancement:  
\- Updated Grok pattern to retrieve `host`.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- Removed word `HostName` from field `cs5`.  
\- Removed redundant `_auth_mechanism` mapping and added common mapping for `_auth_mechanism`.  
\- When `user` is present then map `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Added flag `has_principal` and `has_target`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when `has_principal` and `has_target` is true.  
\- Added conditional check for `user` and domain.   
2024-04-30 |  Enhancement:  
\- Added `affected user name`, `reason`, `app` and `device type` fields  
in additional UDM field.   
2024-04-05 |  Enhancement:  
\- Added a Grok pattern to parse the new format of SYSLOG logs.   
2022-10-10 |  \- Declared fields `cs2`,`FileQualifier`,`msg`,`shost`,`dhost`.  
\- Mapped `metadata.event_type` to `STATUS_UPDATE` where `metadata.event_type` is `GENERIC_EVENT` and `shost` is not null and `dhost` is null.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
