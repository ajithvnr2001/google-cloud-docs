---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-deep-security-changelog/
title: Change log for TRENDMICRO_DEEP_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:32.846570+00:00
---

# Change log for TRENDMICRO_DEEP_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-deep-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_DEEP_SECURITY

Date | Changes  
---|---  
2026-04-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` from `NETWORK_HTTP` to `NETWORK_CONNECTION` when both principal machine data and target machine data are present.   
2025-04-16 |  Enhancement:  
\- Modified Grok patterns to parse the new format of `LEEF` logs.   
2025-03-06 |  Enhancement:  
\- Added support to parse the new format of `timestamp`.   
2025-01-08 |  Enhancement:  
\- Modified the mapping of `cn1` to "additional.fields.  
\- Reduced `GENERIC_EVENT` percentage.   
2024-11-27 |  Enhancement:  
\- Added Grok pattern to parse the new log format.  
\- Mapped `cs4` , `TrendMicroDsPacketData` and `cn3` to `security_result.detection_fields`.   
2024-11-14 |  Enhancement:  
\- If `cef_host` is not an IP address, map it to `intermediary.hostname`.   
2024-11-06 |  Enhancement:  
\- Removed mapping for `dvchost` from `target.hostname` and `target.asset.hostname`.  
\- Mapped `cn1` to `principal.asset_id`.   
2024-10-09 |  Enhancement:  
\- When `act` is equal to `Delete` then mapped `security_result.action` to `BLOCK`  
\- Mapped `result` to `security_result.action_details`.  
\- Mapped `cn2` to `target.file.size`.  
\- Mapped `TrendMicroDsTenant` to `metadata.product_deployment_id`.  
\- Mapped `TrendMicroDsProcessPid` to `principal.process.pid`.   
2024-08-22 |  Enhancement:  
\- Mapped `event_name` to `security_result.threat_name`.  
\- Mapped `event_id` to `metadata.product_event_type`.  
\- Mapped `fileInCompressedFile` to `additional.fields`.  
\- Mapped `dvchost` to `principal.asset.hostname` and `principal.hostname`.  
\- Mapped `cef_host` and `hostname` to `intermediary.ip`.   
2024-04-17 |  Enhancement:  
\- Mapped `event_name` to `metadata.product_event_type`.  
\- Mapped `act` additionally to `security_result.action_details`.   
2024-03-29 |  Enhancement:  
\- Added Grok patterns to parse new formats of `cef_event_attributes`.  
\- Mapped `log_type` to `metadata.product_name`.  
\- Mapped `organization` to `metadata.vendor_name`.  
\- Mapped new fields like suer, suid, fileHash, fsize, spt, dpt, etc.  
\- Mapping sheet link for new fields  
https://docs.google.com/spreadsheets/d/1nsI4GmOo0TiTbEKe8rzBe35x2GKT94lQvqWAqjUTYJQ/edit?resourcekey=0-9yuK26FZnswpAeBrF9_x_A#gid=0   
2024-03-23 |  Enhancement:  
\- Added Grok patterns to parse new formats of `event_attributes` and `cef_event_attributes`.  
\- Mapped `name` to `security_result.summary`.   
2024-03-04 |  Enhancement:  
\- Added a Grok pattern to parse CEF format logs.  
\- Mapped `TrendMicroDsFileSHA1` to `target.file.sha1`.  
\- Mapped `msg` to `security_result.description`.  
\- Mapped `result` to `security_result.summary`.  
\- Mapped `filePath` to `target.file.full_path`.  
\- Mapped `TrendMicroDsMalwareTarget`,`TrendMicroDsProcess`, `TrendMicroDsMalwareTargetCount`,`TrendMicroDsMalwareTargetType` and `TrendMicroDsBehaviorType` to `security_result.detection_fields`.  
\- If `dvchost` is not null, then mapped `dvchost` to `target.hostname` else if `cef_host` is not null, then mapped `cef_host` to `target.hostname`.   
2024-02-13 |  Enhancement:  
\- Mapped `target` to `target.hostname`  
\- Mapped `usrName` to `principal.user.userid`  
2022-09-01 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
