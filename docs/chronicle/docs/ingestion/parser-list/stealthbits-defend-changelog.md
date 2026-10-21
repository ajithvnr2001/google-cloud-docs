---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stealthbits-defend-changelog/
title: Change log for STEALTHBITS_DEFEND \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:22:11.666389+00:00
---

# Change log for STEALTHBITS_DEFEND  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/stealthbits-defend-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for STEALTHBITS_DEFEND

Date | Changes  
---|---  
2022-11-17 |  Enhancement:  
\- Added a new Grok pattern for newly supported CEF logs.  
\- Mapped the following fields:  
\- `suser` mapped to `principal.user.userid`.  
\- `duser` mapped to `target.user.userid`.  
\- `shost` mapped to `principal.hostname`.  
\- `sntdom` mapped to `principal.domain.name`.  
\- `Attribute_Name` mapped to `security_result.summary`.  
\- `Operation` mapped to `security_result.description`.  
\- `Policy_Name` mapped to `security_result.rule_name`.  
\- `Attribute_Name` mapped to `security_result.summary`.  
\- `success` mapped to `security_result_action`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
