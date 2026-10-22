---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-changelog/
title: Change log for SYMANTEC_VIP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:06.008498+00:00
---

# Change log for SYMANTEC_VIP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-vip-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_VIP

Date | Changes  
---|---  
2023-03-03 |  Enhancement- Mapped `userid` to `target.user.userid` for the logs that were not parsed already.  
\- Mapped `event_type` to `USER_LOGIN` for the logs where `userid` is present  
else if `principal.hostname` is present then mapped `event_type` to `STATUS_UPDATE`,  
else mapped it to `GENERIC_EVENT`.  
\- Parsed the logs that were dropped initially.   
2022-08-03 |  BugFix - Added the grok pattern to handle the unparsed logs having log_type `remove_credentials`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
