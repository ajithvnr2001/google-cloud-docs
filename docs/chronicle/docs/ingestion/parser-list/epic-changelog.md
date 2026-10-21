---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/epic-changelog/
title: Change log for EPIC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:41:55.303109+00:00
---

# Change log for EPIC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/epic-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for EPIC

Date | Changes  
---|---  
2026-04-07 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `REMOTEIP`, `CLIENTTYPE`, `INTERNETAREA`, `LOGINCLIENTID`, `LOGINCONTEXT`, `PERIMAUTHST`, `HYPACCESSID`, and `UNRECDEVICE` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `LOGINLDAPID` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- Modified the grok pattern to extract the raw log fields accurately.   
2025-07-24 |  Enhancement:  
\- Added a new grok pattern to support for CEF format logs.  
\- Included additional date formats for timestamp parsing.  
\- Added gsubs to handle `` and convert `AUDIT SESSION` to `AUDIT_SESSION`.  
\- Refactored key-value splitting logic in `kv_data` to handle space-separated keys using gsub.  
\- Added `on_error` for KV filter.  
\- Rearranged the conditions for determining `event.idm.read_only_udm.metadata.event_type`.  
\- Extracted `severity` from raw log and renamed it to `sev` if `sev` raw log field is empty.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `act` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cnt` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `end` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `product_version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `workstationID` raw log field to `event.idm.read_only_udm.principal.asset.asset_id`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `shost` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `shost` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `suser` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `suser` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `IP` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `IP` raw log field to `event.idm.read_only_udm.target.ip`.   
2024-07-01 |  Enhancement:  
\- Changed mapping of `metadata.event_timestamp` from `devTime` to `timestamp` by extracting year from the field `devTime`.  
\- Mapped `devTime` to `additional.fields`.   
2022-10-31 |  Bugfix- Added support for multiple events.   
2022-06-09 |  Bugfix - added support for multiple events containing center dot `·`.  
Added conditional checks for field `devTime`, `usrName`, `shost`, `sev`, `IP`.   
2022-04-14 |  Bugfix-added support for multiple events   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
