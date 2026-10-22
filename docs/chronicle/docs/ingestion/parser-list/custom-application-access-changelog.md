---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-application-access-changelog/
title: Change log for CUSTOM_APPLICATION_ACCESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:51.398344+00:00
---

# Change log for CUSTOM_APPLICATION_ACCESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/custom-application-access-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CUSTOM_APPLICATION_ACCESS

Date | Changes  
---|---  
2025-02-07 |  \- Added support to parse the unparsed logs.  
\- Mapped `request_time` to `metadata.collected_timestamp`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `level` to `additional.fields`.  
\- Mapped `msg_1` to `metadata.description`.  
\- Mapped `service` to `additional.fields`.  
\- Mapped `env` to `additional.fields`.  
\- Mapped `request_id` to `principal.resource.product_object_id`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `response.status` to `network.http.response_code`.   
2024-03-11 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
