---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/druva-backup-changelog/
title: Change log for DRUVA_BACKUP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:21:15.626307+00:00
---

# Change log for DRUVA_BACKUP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/druva-backup-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DRUVA_BACKUP

Date | Changes  
---|---  
2024-12-05 |  \- Changed `inSyncUserName` mapping from `target.user.user_display_name` to `target.user.userid`.  
\- Changed `inSyncUserID` mapping from `target.user.userid` to `additional.fields`.   
2024-11-04 |  \- Changed `inSyncUserID` mapping from `principal.user.userid` to `target.user.userid`.  
\- Changed `inSyncUserEmail` mapping from `principal.user.email_addresses` to `target.user.email_addresses`.  
\- Changed `inSyncUserName` mapping from `principal.user.user_display_name` to `target.user.user_display_name`.   
2024-10-15 |  \- When `initiator` is present then mapped `event_type` as `USER_LOGIN`.   
2024-09-09 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
