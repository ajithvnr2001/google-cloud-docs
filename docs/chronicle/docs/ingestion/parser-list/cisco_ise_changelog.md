---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco_ise_changelog/
title: Change log for CISCO_ISE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:43.307154+00:00
---

# Change log for CISCO_ISE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco_ise_changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ISE 

Date | Changes | 2022-04-21 | Enhancement-Parsed the logs with log_type='CISE_Profiler'   
-For log_type='CISE_TACACS_Accounting changed event_type from 'GENERIC_EVENT' to 'USER_UNCATEGORIZED'   
-Added proper condition for 'NASPort' field and 'Port' field.   
  
---|---  
2022-04-18 | -Mapped 'foreign_ip' to 'intermediary.ip'   
-Parsed the logs with log_type='CISE_TACACS_Accounting' and 'CISE_RADIUS_Accounting'   
-For log_type='CISE_TACACS_Accounting changed event_type from 'GENERIC_EVENT' to 'USER_UNCATEGORIZED'   
-Added proper condition for 'NASPort' field.   
  
2022-04-13 | \- Mapped NAS-Port-Id in event: 5200.   
\- Mapped hostname in events: 60188, 60125, 60116, 60115, 60081, 60080, 51021, 51020, 51003, 51002, 51001, 51000, 52000, 52001, 52002.   
\- Mapped Operation Message text in about.labels in event: 52000.   
\- Mapped Serial Number in additional_fields in event: 5200.   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
