---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snort-ids-changelog/
title: Change log for SNORT_IDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:38.897399+00:00
---

# Change log for SNORT_IDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snort-ids-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SNORT_IDS

Date | Changes  
---|---  
2024-12-04 |  Enhancement-  
\- Added Grok patterns to handle SYSLOG format logs.  
\- If the value of `net_proto` is `Tcp`, then set the value of `network.ip_protocol` to `TCP`.   
2024-11-21 |  Enhancement-  
\- Added a Grok pattern to handle SYSLOG format logs.   
2022-09-22 |  Enhancement-  
\- Added on_error condition for the field `agent.hostname` to parse the unparsed logs.   
2022-07-05 |  Enhancement-  
\- Added a Grok pattern to handle syslog format logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
