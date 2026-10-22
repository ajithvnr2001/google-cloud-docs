---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netwrix-changelog/
title: Change log for NETWRIX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:37.669916+00:00
---

# Change log for NETWRIX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netwrix-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETWRIX

Date | Changes  
---|---  
2026-09-22 |  Enhancement:  
\- Added Support for XML format of logs.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `Opcode` from `event.idm.read_only_udm.about.labels` UDM field since this UDM field is deprecated.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `Opcode` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.domain.name`: Mapped `Data2` raw log field with `event.idm.read_only_udm.target.domain.name` UDM field if it passes the domain regex validation.  
\- `event.idm.read_only_udm.target.application`: Mapped `Data2` raw log field with `event.idm.read_only_udm.target.application` UDM field if `EventID` is 1001 or 1002 and `Data1` equals `Unknown`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RenderingInfoLevel`, `RenderingInfoOpcode`, `Qualifiers`, `Culture`, `RenderingInfoTask` , `RenderingInfoKeyword` , `free_space` , `Data1`, `Data2`(if it fails domain regex validation and `EventID` is not 1001 or 1002), `Data4`, `Data5`, `Data6`, `timestamp` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Data3` raw log field with `event.idm.read_only_udm.additional.fields` UDM field in the fallback `else` block when parsing `Data3` as JSON fails.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `RenderingInfoMessage` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `disk_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `error` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Data1`, `error_description` raw log fields with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `error_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `trace_id`, `correlation_id`, `error_codes` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.   
2024-05-23 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
