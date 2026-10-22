---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/shibboleth-idp-changelog/
title: Change log for SHIBBOLETH_IDP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:40.848387+00:00
---

# Change log for SHIBBOLETH_IDP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/shibboleth-idp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SHIBBOLETH_IDP

Date | Changes  
---|---  
2024-11-14 |  Enhancement:  
\- Changed the Grok pattern field name from `USERNAME` to `DATA` to map `userid` to `principal.user.userid`.   
2024-08-05 |  Enhancement:  
\- Added Grok patterns to parse a new format of logs.   
2024-03-11 |  Enhancement:  
\- Added support for JSON format logs.  
\- Added a Grok pattern to parse `dns` type logs.  
\- Mapped `createdDateTime` to `metadata.event_timestamp`.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `ipAddress` and `ip` to `principal.ip`.  
\- Mapped `location.city` to `principal.location.city`  
\- Mapped `location.state` to `principal.location.state`.  
\- Mapped `location.country` to `principal.location.country`.  
\- Mapped `location.geoCoordinates.latitude` to `principal.location.region_latitude`.  
\- Mapped `location.geoCoordinates.longitude` to `principal.location.region_longitude`.  
\- Mapped `userDisplayName` to `principal.user.user_display_name`.  
\- Mapped `resourceDisplayName` to `target.resource.name`.  
\- Mapped `resourceId` to `target.resource.product_object_id`.  
\- Mapped `deviceDetail.displayName` to `principal.asset.hardware`.  
\- Mapped `deviceDetail.browser` to `network.http.user_agent`.  
\- Mapped `deviceDetail.operatingSystem` to `principal.platform_version`.  
\- Mapped `deviceDetail.operatingSystem` to `principal.platform`.  
\- Mapped `record_name` to `dns.question.name`.  
\- Mapped `record_type` to `dns.question.class`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
