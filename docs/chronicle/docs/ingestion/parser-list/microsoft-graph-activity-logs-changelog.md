---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-graph-activity-logs-changelog/
title: Change log for MICROSOFT_GRAPH_ACTIVITY_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:12:49.384178+00:00
---

# Change log for MICROSOFT_GRAPH_ACTIVITY_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-graph-activity-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_GRAPH_ACTIVITY_LOGS

Date | Changes  
---|---  
2024-10-08 |  Enhancement:  
\- Changed the mapping of `properties.requestUri` from `network.http.referral_url` to `target.url`.   
2024-09-05 |  Enhancement:  
\- Removed mapping of `callerIpAddress` from `principal.ip` and `principal.asset.ip`.  
\- Mapped `properties.C_Idtyp` to `principal.user.account_type`.  
\- Changed mapping of `properties.appId` from `target.resource.product_object_id` to `principal.resource.product_object_id`.  
\- Changed mapping of `properties.requestUri` from `target.url` to `network.http.referral_url`.  
\- Changed mapping of `properties.servicePrincipalId` and `properties.userId` from `principal.user.userid` to `principal.user.product_object_id`.   
2024-07-09 |  Enhancement:  
\- Added support for a new type of JSON logs.   
2024-05-27 |  \- Set `metadata.vendor_name` as `Microsoft` and `metadata.product_name` as `Microsoft Graph`.   
2024-03-01 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
