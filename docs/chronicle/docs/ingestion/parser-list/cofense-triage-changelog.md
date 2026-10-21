---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cofense-triage-changelog/
title: Change log for COFENSE_TRIAGE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:32:57.512800+00:00
---

# Change log for COFENSE_TRIAGE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cofense-triage-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for COFENSE_TRIAGE

Date | Changes  
---|---  
2024-06-18 |  Enhancement:  
\- Retrieved `productlogid` from field `cs3` and mapped it to `metadata.product_log_id`.   
2024-06-11 |  Enhancement:  
\- Modified `gsub` to parse KV logs.  
\- Added conditional check for `cs4`.   
2024-03-04 |  Enhancement:  
\- Mapped `event_data` to `metadata.description`.  
\- Mapped `cat` to `security_result.description`.  
\- Mapped `severity` to `security_result.rule_id`.  
\- Mapped `msg`, `rule_id`, `start`, and `rt` to `additional.fields`.  
\- If `severity` is equal to `8, `10`, `11`, `12`, `13`, or `14`, then `security_result.alert_state` is set to `ALERTING` else set it to `NOT_ALERTING".   
2023-04-19 |  Enhancement:  
\- Added Grok pattern to handle new logs.  
\- Mapped `ProcessID` to `principal.process.pid`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `descrip` to `metadata.description`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Added conditional check for `rule_id`, `sec_result`, `ipaddress`, `security_action`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
