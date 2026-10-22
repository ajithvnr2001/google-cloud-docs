---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-openmanage-changelog/
title: Change log for DELL_OPENMANAGE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:45:31.118678+00:00
---

# Change log for DELL_OPENMANAGE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-openmanage-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DELL_OPENMANAGE

Date | Changes  
---|---  
2025-05-14 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Changed raw log field name from `src_host` to `host_name`.   
2022-07-27 |  Enhancement -  
\- Modified naming of host field from user_name to src_host in the grok.  
\- Mapped user to target.user.userid.  
\- Added null check for ip prior mapping to udm.  
\- Changed event_type from GENERIC_EVENT to STATUS_UPDATE where scr_host is not null.  
\- Added null check for date_time field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
