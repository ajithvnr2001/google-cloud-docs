---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-edirectory-changelog/
title: Change log for NETIQ_EDIRECTORY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:55:50.635971+00:00
---

# Change log for NETIQ_EDIRECTORY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-edirectory-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETIQ_EDIRECTORY

Date | Changes  
---|---  
2026-06-04 |  Enhancement:  
\- The condition for setting event.idm.read_only_udm.metadata.event_type to STATUS_UPDATE was modified to check if src_host (derived from shost) or src is present, instead of checking shost or src directly to resolve parsing error.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dtz` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-02-17 |  Enhancement:  
\- Mapped `dvchost` to `intermediary.hostname`.  
\- Mapped `dvc` to `intermediary.ip`.   
2023-04-08 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
