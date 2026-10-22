---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zerofox-platform-changelog/
title: Change log for ZEROFOX_PLATFORM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:48.104237+00:00
---

# Change log for ZEROFOX_PLATFORM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zerofox-platform-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZEROFOX_PLATFORM

Date | Changes  
---|---  
2025-03-21 |  \- Mapped `metadata.ai_confidence_display.color` to `additional.fields`.  
\- Mapped `metadata.ai_confidence_display.icon` to `additional.fields`.  
\- Mapped `metadata.ai_confidence_display.name` to `additional.fields`.  
\- Mapped `metadata.ai_confidence_display.detections.label` to `security_result.detection_fields`.  
\- if `index` is `0` then mapped `metadata.ai_confidence_display.detections.confidence` to `security_result.confidence_score` else mapped to `security_result.detection_fields`.   
2025-01-09 |  \- Added support for additional fields parsing.   
2024-08-30 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
