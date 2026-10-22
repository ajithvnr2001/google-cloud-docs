---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-changelog/
title: Change log for JAMF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:42.799383+00:00
---

# Change log for JAMF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JAMF

Date | Changes  
---|---  
2024-05-28 |  Enhancement:  
\- Changed mapping of `entity.asset.asset_id` from `id` to `udid`.  
\- Mapped `id` to `entity.asset.attribute.labels`.   
2024-02-23 |  \- Added support for logs where `message` is nearly equal to `phoneNumber` and `message` is nearly equal to `softwareUpdateDeviceId`.  
\- Initialized `username`, `wifiMacAddress` and `softwareUpdateDeviceId` to `null`.  
\- Added IP check before mapping `general.lastReportedIp` to `event.idm.entity.entity.asset.ip`.   
2023-04-27 |  \- Mapped `extensionAttributes.0.extensionAttribute.0.id` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `extensionAttributes.0.extensionAttribute.0.name` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `extensionAttributes.0.extensionAttribute.0.value` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `general.site.name` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `general.serialNumber` to `event.idm.entity.entity.user.attribute.labels`.  
\- Mapped `general.jamfVersion` to `event.idm.entity.entity.asset.software.version`.  
\- Added a null condition check for `extensionAttribute` mappings.   
2023-03-02 |  Customer Issue - Added additional mappings to parse failing logs  
\- Mapped `udid` to `entity.asset.product_object_id`.  
\- Mapped `id`/`data.deviceId` to `entity.asset.asset_id` depending on availability in logs.  
\- Mapped `general.id`/`data.deviceId` to `entity.metadata.product_entity_id` depending on availability in logs.  
\- Mapped `data.details.location.username` to `entity.user.userid`.  
\- Mapped `general.name` to `entity.asset.hostname`.  
\- Mapped `traceId` to `entity.user.windows_sid`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
