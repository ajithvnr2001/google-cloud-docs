---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-openidm-changelog/
title: Change log for FORGEROCK_OPENIDM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:05:08.667239+00:00
---

# Change log for FORGEROCK_OPENIDM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forgerock-openidm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORGEROCK_OPENIDM

Date | Changes  
---|---  
2025-02-13 |  Enhancement:  
\- Added a new Grok pattern to parse new format logs.  
\- Mapped `elapsed_time` and `X-Content-Type-Options` to `additional.fields`.  
\- When `Host` has `ip`, then mapped `Host` to `principal.ip`.   
2025-01-24 |  Enhancement:  
\- Added support for syslog format logs.   
2024-11-28 |  Enhancement:  
\- Added support for a new array format of the logs.   
2024-06-15 |  Enhancement:  
\- Mapped `trackingIds.0` to `metadata.product_log_id`.  
\- Mapped `principalData.0` to `principal.user.userid`.  
\- Mapped `context.userRolesProperty`, `context.authenticationId`, and `context.authenticationIdProperty` to `principal.user.attribute.roles`.  
\- Mapped `context.component`, `context.moduleId`, and `context.queryId` to `principal.resource.attribute.labels`.  
\- Mapped `context.roles`, `_normalized.fieldNames`, and `_eventId` to `additional.fields`.  
\- Removed `gsubs` to handle array values of `principalData` and `trackingIds`.  
\- When `status` is nearly equal to `success`, then set `security_result.action` to `ALLOW`.  
\- When `status` is nearly equal to `fail`, then set `security_result.action` to `BLOCK`.  
\- Initialized `security_result` to null.   
2024-04-03 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
