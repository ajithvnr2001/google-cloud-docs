---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cambium-networks-changelog/
title: Change log for CAMBIUM_NETWORKS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:56:15.171726+00:00
---

# Change log for CAMBIUM_NETWORKS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cambium-networks-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CAMBIUM_NETWORKS

Date | Changes  
---|---  
2025-10-28 |  Enhancement:  
\- Added a new grok pattern to support an additional log format.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `wlan` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `client_mac`, `sta` raw log fields with `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `connection_status` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Replaced hyphens with colons in the `client_mac` and `sta` fields.   
2023-07-27 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
