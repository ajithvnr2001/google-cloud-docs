---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudgenix-sdwan-changelog/
title: Change log for CLOUDGENIX_SDWAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:55.405537+00:00
---

# Change log for CLOUDGENIX_SDWAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudgenix-sdwan-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDGENIX_SDWAN

Date | Changes  
---|---  
2022-09-08 |  Enhancement-  
\- Added conditional check for `PROTOCOL_NAME`.  
\- Added conditional check for `MSG` if it is similar `failure,fail,invalid user,closed,closing` set event_type to `STATUS_SHUTDOWN`.  
\- Set event_type to `NETWORK_FLOW` when `principal.ip` and `target.ip` not null.  
\- Set event_type to `STATUS_STARTUP` when `MSG` similar to `initiating,establishing,establishing,check pass`.  
\- Set event_type to `STATUS_UNCATEGORIZED` when `MSG` similar to `no such user`.  
\- Added grok pattern for `MSG` to retrieve `dest_ip` and Mapped it to `target.ip`.  
\- Added grok pattern for the new logs to retrieve `ION_HOST`.  
\- Mapped `ION_HOST` to `principal.hostname`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
