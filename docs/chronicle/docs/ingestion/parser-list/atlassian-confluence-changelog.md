---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-confluence-changelog/
title: Change log for ATLASSIAN_CONFLUENCE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:37.199674+00:00
---

# Change log for ATLASSIAN_CONFLUENCE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-confluence-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ATLASSIAN_CONFLUENCE

Date | Changes  
---|---  
2024-07-05 |  Enhancement :  
\- Added support for a new format of syslog logs.   
2023-11-14 |  Enhancement :  
\- Added `Grok` pattern to match `SYSLOG` \+ `JSON`.  
\- Mapped `affectedObjects.id`, `affectedObjects.name`, `affectedObjects.type` to `principal.resource.attribute.labels` when `affectedObjects.type` value is not `user`.  
\- Mapped `affectedObjects.id` to `principal.user.userid` when `affectedObjects.type` is `user`.  
\- Mapped `affectedObjects.name` to `principal.user.user_display_name` when `affectedObjects.type` value is `user`.  
\- Mapped `auditType.category` to `security_result.category_details`.  
\- Mapped `auditType.action` to `security_result.summary` when `auditType.area` value is `SECURITY`.  
\- Mapped `auditType.action`, `auditType.actionI18nKey`, `auditType.area`, `auditType.categoryI18nKey` and `auditType.level`, to `security_result.detection_fields` when `auditType.area` value is not `SECURITY`.  
\- Mapped `author.id` to `principal.user.userid` when `author.type` value is `user`.  
\- Mapped `author.name` to `principal.user.user_display_name` when `author.type` value is `user`.  
\- Mapped `changedValues.from`, `changedValues.i18nKey`, `changedValues.key` and `changedValues.to` to `principal.resource.attribute.labels`.  
\- Mapped `extraAttributes.name`, `extraAttributes.nameI18nKey` and `extraAttributes.value` to `principal.resource.attribute.labels`.  
\- Mapped `source` to `principal.ip`.  
\- Mapped `system` to `principal.hostname`.   
2023-10-24 |  Bug-Fix :  
\- Mapped `session_duration` to `additional fields`.  
\- Mapped `bytes_in` to `network.received_bytes`.  
\- Mapped `app_protocol` to `network.application_protocol`.   
2023-08-28 |  Bug-Fix :  
\- Mapped `principal_host` to `principal.hostname`.  
\- Modified mapping of `user_id` from `prinicipal.hostname` to `principal.user.userid`.   
2023-04-28 |  Enhacement :  
\- Wrote new Grok pattern to parse additional logs as `GENERIC_EVENT` event type.   
2023-04-03 |  Bug-Fix :  
\- Changed the order of date formats while mapping the timestamp.  
\- Mapped `category` to `security_result.category_details`.   
2023-02-16 |  Enhancement:  
\- Handled JSON logtype.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
