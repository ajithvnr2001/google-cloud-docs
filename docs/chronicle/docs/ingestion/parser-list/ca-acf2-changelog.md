---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-acf2-changelog/
title: Change log for CA_ACF2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:28.294666+00:00
---

# Change log for CA_ACF2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ca-acf2-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CA_ACF2

Date | Changes  
---|---  
2022-05-24 |  Enhancement - Changed mappings for the following fields:  
\- Changed mapping from `target.resource.id` to `target.resource.product_object_id`.  
\- Changed mapping from `target.resource.type` to `target.resource.resource_type`.  
\- Changed mapping for field `usrPriv`, `auth`, `intent`, `cat` from `target.labels` to `additional.fields`.  
\- Changed `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` for events `ACF2-A`, ACF2-R` and `ACF2-J".  
\- Changed mapping for field `box` from `target.file.full_path` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
