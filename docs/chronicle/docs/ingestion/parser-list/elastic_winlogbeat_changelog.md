---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic_winlogbeat_changelog/
title: Change log for ELASTIC_WINLOGBEAT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:44:47.504005+00:00
---

# Change log for ELASTIC_WINLOGBEAT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic_winlogbeat_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ELASTIC_WINLOGBEAT 

Date | Changes | 2022-04-27 | Enhancement-Added new field mapping.   
mapped StartAddress to target.labels   
  
---|---  
2022-04-13 | Enhancement   
-Mapped ReferrerUrl, HostUrl from additional to security_result.rule_labels.   
-Mapped CallTrace field to security_result.detection_fields.   
Handled the below errors:   
"winlog.keywords.0" not found in state data   
"security_result" not found in state data   
"winlog.record_id": field not set   
"_event.provider": field not set   
"powershell.file.script_block_id": field not set   
"winlog.opcode": field not set   
"_event.action": field not set   
"auth_mechanism" must not be empty   
"winlog.process.pid": field not set   
"winlog.event_data.TargetUserName": field not set   
"agent.type": field not set   
"host.name": field not set   
"agent.version": field not set   
  
2022-03-25 | Enhancement   
\- Added check for event_type where event.code is either 11, 12, or 13.   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
