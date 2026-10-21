---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opnsense-changelog/
title: Change log for OPNSENSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:27:49.079190+00:00
---

# Change log for OPNSENSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opnsense-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPNSENSE

Date | Changes  
---|---  
2025-09-17 |  Enhancement:  
\- Added Grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column27`, `column2`, `column3`, `column11`, `column26`, `column28`, `column25`, `column16`, `column9` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-29 |  Enhancement:  
\- Added a new Grok pattern to support for new pattern of logs.  
\- Separated date filters to handle timestamps without year data.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` log field to event.idm.read_only_udm.principal.process.pid.   
2025-05-29 |  Enhancement:  
\- event.idm.read_only_udm.principal.administrative_domain: Removed mapping of `domain` from `principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field to `intermediary.hostname` UDM field.   
2025-02-18 |  Enhancement:  
\- Added support to parse the unparsed logs.   
2025-01-21 |  Enhancement:  
\- Added support to parse the unparsed logs.   
2024-12-05 |  Enhancement:  
\- Added support to handle CSV logs.   
2024-11-07 |  Enhancement:  
\- Added support to handle CSV logs.   
2023-11-22 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
