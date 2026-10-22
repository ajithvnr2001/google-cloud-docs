---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-alert-changelog/
title: Change log for SENTINELONE_ALERT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:00.257478+00:00
---

# Change log for SENTINELONE_ALERT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-alert-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENTINELONE_ALERT

Date | Changes  
---|---  
2026-09-30 |  \- security_result.category_details: Mapped `threatInfo.classification` raw log field with `security_result.category_details` UDM field at the first index (`security_result[0]`) by merging `threatInfo` before `indicators` and `mitigationStatus`.   
2026-07-21 |  \- Enhanced logic to extract and map MITRE ATT&CK technique and subtechnique IDs from URL links when the technique name is a text description rather than a standard ID (e.g., TXXXX).   
2024-12-09 |  Promoted SENTINELONE_ALERT parser to default.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
