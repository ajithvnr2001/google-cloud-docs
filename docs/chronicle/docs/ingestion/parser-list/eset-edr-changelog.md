---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-edr-changelog/
title: Change log for ESET_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:06:20.743408+00:00
---

# Change log for ESET_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ESET_EDR

Date | Changes  
---|---  
2024-04-08 |  Enhancement:  
\- Mapped `Detectiontype` to `security_result.category_details`.  
\- Mapped `Time_of_occurrence` to `additional.fields`.   
2024-03-12 |  Enhancement:  
\- Added Grok patterns to parse new log.  
\- Mapped `Detectiontype` to `security_result.category_details`.  
\- Mapped `Detection_name` to `security_result.threat_name`.  
\- Mapped `Scanner` to `security_result.description`.  
\- Mapped `Action_performed` to `security_result.action_details`.  
\- Mapped `Computer_name` to `principal.hostname`.  
\- Mapped `Computer_name` to `principal.asset.hostname`.  
\- Mapped `Logged_user` to `principal.user.userid`.  
\- Mapped `app` to `principal.application`.  
\- Mapped `process_id` to `principal.process.pid`.   
2022-05-10 |  Added and modified multiple fields to increase log parsing percentage:  
userid, file.full_path, processName, threat_name, action_details, port, process.pid, event_type, hostname, ip, accountName.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
