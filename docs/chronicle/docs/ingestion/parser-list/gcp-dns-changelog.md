---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-changelog/
title: Change log for GCP_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:00.476262+00:00
---

# Change log for GCP_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_DNS

Date | Changes  
---|---  
2026-09-29 |  metadata.event_type: Updated the conditional logic to set the `metadata.event_type` UDM field to `NETWORK_DNS` instead of `GENERIC_EVENT` when `jsonPayload.vmInstanceName` is present and `jsonPayload.sourceIP` is absent.   
2026-06-02 |  principal.hostname: Newly mapped `jsonPayload.vmInstanceName` raw log field with `principal.hostname` UDM field.   
2026-03-17 |  Improved the grok pattern to extract the correct values from the `jsonPayload.queryName` raw log fields and mapped them to the `network.dns.questions.name` UDM field.   
2025-07-01 |  principal.namespace: Removed mapping of `jsonPayload.sourceNetwork` from `principal.namespace` UDM field and mapped `additional.fields` in order to prevent the feed namespace from being overwritten by the prebuilt parser.   
2024-12-16 |  Promoted GCP_DNS parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
