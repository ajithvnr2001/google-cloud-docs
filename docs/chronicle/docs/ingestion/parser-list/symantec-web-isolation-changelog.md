---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-web-isolation-changelog/
title: Change log for SYMANTEC_WEB_ISOLATION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:45:27.901172+00:00
---

# Change log for SYMANTEC_WEB_ISOLATION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-web-isolation-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_WEB_ISOLATION

Date | Changes  
---|---  
2022-07-08 |  Enhancement:  
\- Modified mapping for `device.user.organization.id` from `target.user.groupid` to `target.user.group_identifiers`.  
\- Modified mapping for `device.user.organization.name` from `target.user.group_identifiers` to `target.user.department`.   
2022-06-20 |  Enhancement - Changed UDM field name from `metada.product_name` to `metadata.product_name`.  
Added conditional checks for fields `original_source_ip`, `url_host` and `destination_ip`.  
Dropped the logs having invalid JSON format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
