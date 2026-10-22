---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cynet-360-autoxdr-changelog/
title: Change log for CYNET_360_AUTOXDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:32.053879+00:00
---

# Change log for CYNET_360_AUTOXDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cynet-360-autoxdr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYNET_360_AUTOXDR

Date | Changes  
---|---  
2026-06-18 |  \- Added a Grok pattern to validate that the `src`, `dst`, `RequesterIp`, and `StringIP` raw log fields contain valid IP addresses.  
\- Added timestamp support for the `rt` raw log field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields when it is not a valid IP address.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when it is not a valid IP address.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `cef_device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `cef_signature_id` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `cef_severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `requestUrl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `suid` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dtz`, `event_time` and `msg_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `syslog_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.application`: Newly mapped `syslog_app` raw log field with `event.idm.read_only_udm.observer.application` UDM field.  
\- `event.idm.read_only_udm.observer.process.pid`: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.   
2025-10-01 |  \- event.idm.read_only_udm.additional.fields: Newly mapped `externalId`, `fname`, `sev`, `gpParams`, `gpprUser`, `gpSign`, `hostLS`, `epsVer`, `confVer`, `scanGroupId`, `sign`, `pssdeep`, `pSign`, `pct`, `gpssdeep`, `clientId`, `etwAlertId`, `pParams` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `remedStat` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `actRem` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `prUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `osVer` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.file.sha256: Newly mapped `pFileHash` raw log field with `event.idm.read_only_udm.principal.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `pprUser` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `ppParams` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.sha256: Newly mapped `gpFileHash` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `filePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `cef_header` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `scanGroupName` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `dtUtc`, `rt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `rtUtc` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: The condition to set the event type to USER_UNCATEGORIZED was updated to include a check on the `has_target_user` field.  
\- Added conditional check for json_failed to parse CEF formatted logs as a fallback.  
\- Added conditional check for duser to parse domain and user.  
\- Added conditional check for dtUtc and rt for event timestamp mapping.  
\- Added conditional check for sev to map severity values.   
2024-07-09 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
