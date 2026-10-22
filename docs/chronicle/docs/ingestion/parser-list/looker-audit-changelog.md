---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/looker-audit-changelog/
title: Change log for LOOKER_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:42.206262+00:00
---

# Change log for LOOKER_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/looker-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LOOKER_AUDIT

Date | Changes  
---|---  
2025-03-13 |  Enhancement:  
\- Removed the mapping for `User_ID` and `user_id` from `principal.user.userid`.  
\- Changed mapping for `User_ID` and `user_id` from `principal.user.userid` to `principal.user.product_object_id`.  
\- Removed the mapping for `User_Name` and `user_name` from `principal.user.user_display_name`.  
\- Changed mapping for `User_Name` and `user_name` from `principal.user.user_display_name` to `principal.user.userid`.  
\- Mapped `sql_text.text` to `additional.fields`.   
2025-02-26 |  Enhancement:  
-Mapped `history.source` to `additional.fields`.  
-Mapped `user.email` to `principal.email`.  
-Mapped `user.name` to `principal.user.user_display_name`.  
-Mapped `history.connection_name` to `additional.fields`.  
-Mapped `query.model` to `additional.fields`.  
-Mapped `query.view` to `additional.fields`.  
-Mapped `dashboard.title` to `additional.fields`.  
-Mapped `dashboard.link` to `additional.fields`.  
-Mapped `user.id` to `additional.fields`.  
-Mapped `history.status` to `additional.fields`.  
-Mapped `history.id` to `principal.user.userid`.   
2025-02-04 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
