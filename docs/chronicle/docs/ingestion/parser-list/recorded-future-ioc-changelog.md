---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/recorded-future-ioc-changelog/
title: Change log for RECORDED_FUTURE_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:29.226266+00:00
---

# Change log for RECORDED_FUTURE_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/recorded-future-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RECORDED_FUTURE_IOC

Date | Changes  
---|---  
2026-01-19 |  Enhancement:  
\- `event.idm.read_only_udm.entity.entity.file.sha256`: Newly mapped `Value` raw log field with `event.idm.read_only_udm.entity.entity.file.sha256` UDM field.  
\- `event.idm.read_only_udm.entity.entity.url`: Newly mapped `Value` raw log field with `event.idm.read_only_udm.entity.entity.url` UDM field.  
\- `event.idm.read_only_udm.entity.metadata.entity_type`: Updated to `FILE` when `Value` matches a SHA256 hash.  
\- `event.idm.read_only_udm.entity.metadata.entity_type`: Updated to `URL` when `Value` is identified as a URI.   
2025-04-11 |  Enhancement:  
\- Updated parser to parse each log entry into single event instead of multiple events.  
\- event.ioc.categorization: Removed mapping of `detail.Rule` from `event.ioc.categorization` UDM field.  
\- event.ioc.description: Removed mapping of `detail.EvidenceString` from `event.ioc.description` UDM field.  
\- event.ioc.raw_severity: Removed mapping of `detail.CriticalityLabel` from `event.ioc.raw_severity` UDM field.  
\- event.idm.entity.metadata.threat.first_discovered_time: Newly mapped `detail.FirstSeen` raw log field with `event.idm.entity.metadata.threat.first_discovered_time` UDM field.   
2025-04-07 |  Enhancement:  
\- `event.idm.ready_only_udm.metadata.threat.risk_score`: Newly mapped `risk_score` raw log field with `event.idm.ready_only_udm.metadata.threat.risk_score` UDM field.  
\- Added conversion of `event.idm.ready_only_udm.metadata.threat.risk_score` to float.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
