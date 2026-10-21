---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-casb-changelog/
title: Change log for MICROSOFT_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:05:43.035828+00:00
---

# Change log for MICROSOFT_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_CASB

Date | Changes  
---|---  
2025-03-26 |  Enhancement:  
\- Modified and added Grok pattern to parse different time formats.  
\- Added a conditional check when mapping `suser` to `principal.user.userid`.  
\- Mapped `uniqueServiceAppIds` to `target.resource.id`.  
\- Added a conditional check before setting `metadata.event_type` to `USER_LOGIN` and renaming `event.idm.read_only_udm.principal.user` to `event.idm.read_only_udm.target.user`.  
\- Added a conditional check before setting `metadata.event_type` to `USER_RESOURCE_CREATION` , `USER_RESOURCE_UPDATE_CONTENT` and `RESOURCE_READ`.  
\- Added a `user_display_name` null check before mapping `user_display_name` to `principal.user.userid`.  
\- Added on error when mapping `suser` to `principal.user.userid` and `principal.user.user_display_name`.   
2023-11-27 |  Enhancement:  
\- Handled unparsed JSON logs.   
2023-06-28 |  Enhancement:  
\- Enhanced parser to set the `metadata.event_type` to a more specific value and reduce the number of logs with `GENERIC_EVENT` for `metadata.event_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
