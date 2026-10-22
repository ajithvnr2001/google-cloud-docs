---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-loadbalancing-changelog/
title: Change log for GCP_LOADBALANCING \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:52.925027+00:00
---

# Change log for GCP_LOADBALANCING  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-loadbalancing-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_LOADBALANCING

Date | Changes  
---|---  
2026-06-30 |  Added grok patterns support to improve the extraction of the IP address and ports from the raw log fields.   
2025-08-13 |  additional.fields[tlsJa4Fingerprint]: Newly mapped `jsonPayload.securityPolicyRequestData.tlsJa4Fingerprint` raw log field with `additional.fields[tlsJa4Fingerprint]` UDM field.   
2025-07-07 |  metadata.product_name: Newly mapped `metadata.product_name` UDM field.   
2024-07-19 |  Added additional mappings for deprecated `noun.labels`.   
2024-02-14 |  Added mapping for the raw log fields `jsonPayload.securityPolicyRequestData.tlsJa3Fingerprint` and `jsonPayload.securityPolicyRequestData.remoteIpInfo.regionCode`.   
2023-11-29 |  Enhancement  
Added mapping for additional raw log fields.   
2023-11-01 |  Added mapping for the raw log field `jsonPayload.enforcedSecurityPolicy.threatIntelligence.categories`.   
2023-09-01 |  Promoted parser to default.  
For the field mapping reference, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/gcp-loadbalancing>Collect Google Cloud Load Balancing logs](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
