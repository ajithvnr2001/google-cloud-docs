---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-ecs-changelog/
title: Change log for DELL_ECS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:46.518039+00:00
---

# Change log for DELL_ECS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-ecs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DELL_ECS

Date | Changes  
---|---  
2026-01-12 |  \- Added grok pattern to support new format of logs.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_name` raw log field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg_description` raw log field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Category`, `Component`, `TimeZone` raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for `event.idm.read_only_udm.metadata.event_timestamp` from `timestamp` (UNIX format) to `event_time` (yyyy-MM-ddTHH:mm:ssZZ, ISO8601 formats), and added `timestamp` (MMM dd HH:mm:ss format) as an alternative source.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT` and `principal_present` is not `false`, updated to `STATUS_UPDATE`.  
\- Introduced an initial `mutate` block to clear certain fields (`process_name`, `pid`, `serviceType`, `event_type`, `msg`, `msg_description`, `kv_data`, `severity`, `security_result`, `Category`, `Component`, `TimeZone`, `principal_present`) before processing.  
\- Added `overwrite` option to `grok` filters to explicitly manage field overwrites.  
\- Introduced a `principal_present` flag which is set to `true` when `event.idm.read_only_udm.principal.hostname` is populated.   
2024-03-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
