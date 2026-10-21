---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/velo-firewall-changelog/
title: Change log for VELO_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:49.478932+00:00
---

# Change log for VELO_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/velo-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VELO_FIREWALL

Date | Changes  
---|---  
2026-02-12 |  Enhancement:  
\- Added new Grok pattern to parse the `sdwan` type logs.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `product_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cloud_software` raw log field with `event.idm.read_only_udm.additional.fields` UDM field, using the key `CLOUD_SOFTWARE`.   
2024-10-10 |  Enhancement:  
\- Mapped `action` field from log to `security_result.action_details`.  
\- If `action` is `Allow`, then set `security_result.action as `ALLOW".   
2024-09-12 |  Enhancement:  
\- Modified the Grok pattern to parse unparsed logs.   
2024-06-30 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
