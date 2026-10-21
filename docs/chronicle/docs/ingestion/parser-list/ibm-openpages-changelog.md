---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-openpages-changelog/
title: Change log for IBM_OPENPAGES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:39:37.038559+00:00
---

# Change log for IBM_OPENPAGES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-openpages-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_OPENPAGES

Date | Changes  
---|---  
2024-10-10 |  Enhancement:  
\- Dropped the header which is getting parsed as a log.  
\- Mapped `target_user` to `target.user.userid` and `target_role` to `target.user.attribute.roles.name`.   
2024-10-07 |  Enhancement:  
\- When `logon successful?=No` then mapped `security_result.action` as `BLOCK`.  
\- When `logon successful?=No` then mapped `security_result.action_details` as `Logon Failed`.  
\- Mapped `IBM_OPENPAGES` to `metadata.vendor_name`.  
\- Mapped `IBM_OPENPAGES` to `metadata.product_name`.   
2024-09-10 |  \- Changed `column6` mapping from `target.user.userid` to `principal.user.userid`.  
\- Mapped `OpenPages` to `metadata.product_name` and `IBM` to `metadata.vendor_name`.   
2024-08-02 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
