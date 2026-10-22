---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pure-storage-changelog/
title: Change log for PURE_STORAGE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:38.672728+00:00
---

# Change log for PURE_STORAGE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pure-storage-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PURE_STORAGE

Date | Changes  
---|---  
2026-08-21 |  \- `event.idm.read_only_udm.additional.fields`: Removed mapping of `array_name` from `event.idm.read_only_udm.additional.fields` UDM field as it represents ingestion label data.  
\- `event.idm.read_only_udm.metadata.ingestion_labels`: Mapped `array_name` raw log field with `event.idm.read_only_udm.metadata.ingestion_labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Link` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `utc_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- Modified a grok pattern to parse the raw log fields.   
2024-10-01 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
