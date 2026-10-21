---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/semperis-dsp-changelog/
title: Change log for SEMPERIS_DSP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:05:29.772735+00:00
---

# Change log for SEMPERIS_DSP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/semperis-dsp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SEMPERIS_DSP

Date | Changes  
---|---  
2025-09-12 |  Enhancement:  
\- Added support for events from the `DSP` application, parsing Key-Value pairs from the main log message.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `RESOURCE_WRITTEN` when `MESSAGE` is `Overwrite`.  
\- Refactored conditional logic for setting default `event.idm.read_only_udm.metadata.event_type` to a later stage in the parser.  
\- Implemented conditional parsing logic to handle the key-value pairs enclosed in square brackets for `Semperis.DSP.OperationLog` messages.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `TIME_GENERATED` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `MESSAGE` raw log field to `event.idm.read_only_udm.metadata.description` (when `MESSAGE` is `Overwrite`).  
\- event.idm.read_only_udm.principal.ip: Newly mapped `CLIENT_IP` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `CLIENT_IP` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `CLIENT_HOST` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `USERNAME` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `USER_SID` raw log field to `event.idm.read_only_udm.principal.user.windows_sid`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `SERVERNAME` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `SERVERNAME` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `NEW_FILE_NAME` raw log field to `event.idm.read_only_udm.target.file.full_path`.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `FILE_SIZE` raw log field to `event.idm.read_only_udm.target.file.size`.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `IS_SUCCESS_EVENT` raw log field to `event.idm.read_only_udm.security_result.action` (sets to `ALLOW` if `IS_SUCCESS_EVENT` is `true`).  
\- event.idm.read_only_udm.additional.fields: Newly mapped `LOCATION`, `OLD_SHARE_PATH`, `NEW_SHARE_PATH`, `FILE_ATTRIBUTES`, `IS_TRANSACTION`, `IS_USB_EVENT`, `FILETYPE_EXTENSION`, `CREATION_TIME`, `LAST_WRITE_TIME`, `LAST_ACCESS_TIME`, `COMPLETION_TIME`, `ACCESS_MASK`, and `IMAGE_FILE_NAME` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-09-05 |  Enhancement:  
\- Added grok pattern to accommodate the additional syslog format.  
\- Implemented conditional parsing logic to handle the key-value pairs enclosed in square brackets for `Semperis.DSP.AdChanges` messages.  
\- Added new timestamp format for `OriginatingTime` field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `ChangeId` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `PartitionNamingContext` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `AttributeModificationType` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `linkedValueDN`, `ValidUntil`, `OriginatingUserWorkstations`, 'StringValueFrom`, `StringValueTo` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2024-05-03 |  Enhancement:  
\- Added a new Grok pattern to parse unparsed logs.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- When `principal_present` is `true`, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- When `principal_user_present` is `true`, then set `metadata.event_type` to `USER_UNCATEGORIZED`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
