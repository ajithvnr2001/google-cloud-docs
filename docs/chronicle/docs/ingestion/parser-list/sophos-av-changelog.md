---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-av-changelog/
title: Change log for SOPHOS_AV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:26:26.182285+00:00
---

# Change log for SOPHOS_AV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sophos-av-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOPHOS_AV

Date | Changes  
---|---  
2024-08-22 |  Enhancement -  
\- Added a Grok pattern to parse new logs.  
\- Mapped `appSha256` to `principal.file.sha256`.   
2022-07-27 |  Enhancement -  
\- Added conditional check for fields `rule` and `rules`.  
\- Mapped `src_ip` to `principal.ip`.  
\- Mapped `f_path` to `target.file.full_path`.  
\- Mapped `rules` to `security_result.rule_name`.  
\- Mapped `url` to `target.url`.  
\- Mapped `application` to `target.application`.  
\- Mapped `duid` to `target.user.userid`.  
\- Mapped `endpoint_type` to `security_result.about.labels`.  
\- Mapped `endpoint_id` to `security_result.about.labels`.  
\- Mapped `id` to `principal.resource.id`.  
\- Mapped `customer_id` to `target.resource.id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
