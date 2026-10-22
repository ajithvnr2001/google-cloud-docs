---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rh-isac-ioc-changelog/
title: Change log for RH_ISAC_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:33.866435+00:00
---

# Change log for RH_ISAC_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rh-isac-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RH_ISAC_IOC

Date | Changes  
---|---  
2024-03-07 |  Bug-Fix:  
\- Mapped fields from array `TAG` to `event.idm.entity.metadata.threat.detection_fields`.   
2024-01-11 |  Bug-Fix:  
\- When `indicatorType` is `text/other`, then mapped `value` to `event.idm.entity.entity.file.full_path`.  
\- When `indicatorType` is `text/other`, then set `event.idm.entity.metadata.entity_type`` to `FILE".   
2023-11-21 |  Fix:  
\- When `firstSeen` is `null`, then mapped `event.idm.entity.metadata.interval.start_time` to `1`.  
\- When `indicatorType` is `hostname/domain`, then mapped `value` to `event.idm.entity.entity.hostname`.  
\- When `indicatorType` is `email`, then mapped `uuid` to `event.idm.entity.metadata.product_entity_id`.  
\- When `indicatorType` is `comment|phone` dropped the logs.  
\- Mapped `comment` to `event.idm.entity.metadata.threat.summary`.  
\- Mapped `category` to `event.idm.entity.metadata.threat.category_details`.  
\- Mapped `id` to `event.idm.entity.metadata.threat.detection_fields`.  
\- Mapped `object_id` to `event.idm.entity.metadata.threat.detection_fields`.  
\- Mapped `uuid` to `event.idm.entity.metadata.threat.detection_fields`.   
2022-03-22 |  Enhancement - Added entity fields to all the logs that has firstseen and lastseen fields.  
Avoided dropping of logs of indicatorType: SHA256, EMAIL_ADDRESS, MD5, SHA1, SOFTWARE, CVE and mapped them as entity type fields without ioc.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
