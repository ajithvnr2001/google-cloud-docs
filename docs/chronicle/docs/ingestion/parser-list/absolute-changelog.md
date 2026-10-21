---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/absolute-changelog/
title: Change log for ABSOLUTE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:38:29.487828+00:00
---

# Change log for ABSOLUTE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/absolute-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ABSOLUTE

Date | Changes  
---|---  
2024-12-03 |  Enhancement:  
\- Added a KV block to map `objectProperties`.  
\- Mapped `objectProperties` to `target.resource.attribute.labels`.   
2023-07-07 |  Enhancement:  
\- Modified Grok pattern to support new log formats.  
\- Mapped `actorType` to `principal.user.attribute.roles.name`.  
\- Mapped `actorID` to `principal.user.product_object_id`.  
\- Mapped `objectType` to `principal.resource.resource_type` when `objectType` is `Device`.  
\- Mapped `objectName` to `principal.hostname`.  
\- Mapped `objectID` to `principal.resource.product_object_id`.  
\- Mapped `dvc_ip` to `intermediary.ip`.  
\- Mapped `hostname` to `intermediary.hostname`.  
\- Mapped `pid` to `about.process.pid`.  
\- Mapped `event_class` to `metadata.product_event_type`.  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `eventType` to `metadata.product_event_type`.  
\- Mapped `verb` to `security_result.summary`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
