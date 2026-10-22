---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-cf-changelog/
title: Change log for SENTINELONE_CF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:00.286017+00:00
---

# Change log for SENTINELONE_CF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-cf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENTINELONE_CF

Date | Changes  
---|---  
2026-06-30 |  \- Removing the drop condition for the log doesn't have `event.type` field and parsing it as `GENERIC_EVENT`.   
2026-05-14 |  Updated SENTINELONE_CF parser to correctly identify macOS platforms.  
\- Supported additional variations (`osx`, `macos`) in addition to `os x` from `endpoint.os` and `os.name` raw log fields to map to the `MAC` platform type in the `principal.asset.platform_software.platform` , `target.asset.platform_software.platform` , `target.platform` and `principal.platform` fields.   
2026-04-16 |  Updated the mapping of `endpoint.*`, `src.process.*`, `osSrc.process.*` and `os.name` raw log fields based on the condition `event.network.direction = INCOMING` raw log field as follows:  
\- `principal.labels`: Removed the mapping of `principal.labels` UDM field since it is deprecated.  
\- `principal.*`: Updated the mapping of `principal.*` UDM fields to `target.*` UDM fields for the raw log fields `endpoint.*`, `src.process.*`, `osSrc.process.*` and `os.name` to accurately reflect targeted system attributes for incoming network direction.   
2025-03-20 |  Updated the mapping for `Registry Value Create` and `Registry Value Modified` event types as follows:  
\- `target.registry.registry_key` (Changed UDM field mapping) -> Earlier, the entire `registry.keyPath` raw log field was mapped. -> New UDM mapping extracts `registry_key` from the `registry.keyPath` raw log field using a grok pattern.  
\- `target.registry.registry_value_name` (Changed UDM field mapping) -> Earlier, the `registry.valueType` raw log field was mapped. -> New UDM mapping extracts `value_name` from the `registry.keyPath` raw log field using a grok pattern.  
\- `additional.fields` (New UDM field mapping) -> No UDM mapping to mapping of `registry.valueType` fields from the raw log.   
2025-03-04 |  `target.hostname` (New UDM field mapping) -> No UDM Mapping To Mapping of `event.dns.request` raw log field for the event type `NETWORK_DNS`.   
2024-08-02 |  Added support for metadata.product_name.   
2024-06-11 |  Enhancement:  
\- When `os.name` is `os x`, then mapped `MAC` to `principal.platform`.   
2024-05-01 |  Updated the mapping for the deprecated UDM field.   
2024-04-24 |  Updated event validation to `STATUS_UPDATE` event for `group.id` field not present.   
2024-03-15 |  Updated the mapping for `process.product_specific_process_id` UDM field.   
2024-01-17 |  Updated metadata.event_type mapping of `Registry Key Create` event.   
2024-01-03 |  Updated mapping of `Agent`-related fields from `observer` to `principal`.   
2023-10-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
