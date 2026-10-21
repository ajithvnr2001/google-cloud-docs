---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/twingate-changelog/
title: Change log for TWINGATE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:26:46.476684+00:00
---

# Change log for TWINGATE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/twingate-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TWINGATE

Date | Changes  
---|---  
2024-12-11 |  Enhancement:  
\- Mapped `event_data.actor.type` to `principal.user.attribute.roles`.  
\- Mapped `event_data.actor.id` to `principal.user.userid`.  
\- Mapped `event_data.actor.info.email` to `principal.user.emailaddresses`.  
\- Mapped `event_data.action` to `security_result.action_details`.  
\- Mapped `event_data.version` to `metadata.product_version`.  
\- Mapped `event_data.targets.id` to `target.resource.attribute.labels`.  
\- Mapped `event_data.targets.name` to `target.resource.attribute.labels`.  
\- Mapped `event_data.targets.type` to `target.resource.resource_type`.  
\- Mapped `event_data.targets.version` to `target.resource.attribute.labels`.  
\- Mapped `event_data.targets.email` to `target.resource.attribute.labels`.  
\- Mapped `event_data.targets.role` to `target.resource.attribute.labels`.  
\- Mapped `event_data.targets.address.value` to `target.ip`.  
\- Mapped `event_data.targets.address.value` to `target.asset.ip`.   
2024-10-11 |  Enhancement:  
\- Added `gsub` to parse unparsed logs.  
\- Mapped `event.reasons.id` to `security_result.detection_fields`.  
\- Mapped `event.reasons.name` to `security_result.detection_fields`.  
\- Mapped `device.name` to `target.resource.attribute.labels`.   
2024-07-30 |  Enhancement:  
\- Mapped connection_protocol to `addition.fields`.  
\- Changed `event_type` to `event_data_type`.  
\- Mapped the unmapped fields.   
2024-05-23 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
