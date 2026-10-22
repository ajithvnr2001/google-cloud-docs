---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sharepoint-changelog/
title: Change log for SHAREPOINT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:58.899129+00:00
---

# Change log for SHAREPOINT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sharepoint-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SHAREPOINT

Date | Changes  
---|---  
2025-03-15 |  Newly created parser.  
Mapped the following fields:  
\- `database` to `principal.process.file.names`  
\- `SamAccountName` to `principal.hostname` and `principal.asset.hostname`  
\- `UserName` to `principal.user.user_display_name`  
\- `UserEmail` to `principal.user.email_addresses`  
\- `ItemType` to `target.resource.type`  
\- `EventType` to `security_result.description`  
\- `Directory` to `target.file.full_path`  
\- `Leaf` to `target.file.names`  
\- `EventData` to `metadata.product_version`  
\- `Created` to `principal.asset.attribute.labels`  
\- `LastModified` to `principal.asset.attribute.labels`  
\- `SecGroupName` to `target.user.group_identifiers`  
\- `SecSamAccountName` to `target.user.userid`  
\- `SecUserName` to `target.user.user_display_name`  
\- `SecUserEmail` to `target.user.email_addresses`  
\- `SecUserRole` to `target.user.attribute.roles`  
\- `SecUserURL` to `target.url`  
\- `SourceModuleName` to `metadata.product_version`  
\- `SourceModuleType` to `metadata.product_event_type`  
\- `SHAREPOINT` to `metadata.vendor_name` and `metadata.product_name`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
