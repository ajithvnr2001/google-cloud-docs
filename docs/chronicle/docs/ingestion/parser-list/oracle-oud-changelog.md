---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-oud-changelog/
title: Change log for ORACLE_OUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:47:07.870833+00:00
---

# Change log for ORACLE_OUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oracle-oud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ORACLE_OUD

Date | Changes  
---|---  
2023-09-11 |  Enhancement:  
\- Mapped `authFailureID`, `filter`, `attrs`, `changetype`, `replace` and `authFailureReason` to `additional.fields`.  
\- Mapped `msg_data` to `security_result.summary`.  
\- Mapped `uid` to `principal.user.userid`.  
\- Mapped `from` to `principal.ip` and `principal.port`.  
\- Mapped `to` to `target.ip` and `target.port`.  
\- Mapped `operation` to `metadata.product_event_type`.   
2023-08-03 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
