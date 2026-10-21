---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openpath-changelog/
title: Change log for OPENPATH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:38:33.530739+00:00
---

# Change log for OPENPATH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openpath-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPENPATH

Date | Changes  
---|---  
2025-06-10 |  \- event.idm.read_only_udm.metadata.product_name: Removed mapping of `SPYCLOUD` from `event.idm.read_only_udm.metadata.product_name` UDM Field and mapped `AVIGILON` instead (a incorrect value was mapped so we are replacing it with the correct one).  
\- event.idm.read_only_udm.metadata.vendor_name: Removed mapping of `SPYCLOUD` from `event.idm.read_only_udm.metadata.vendor_name` UDM Field and mapped `AVIGILON` instead (a incorrect value was mapped so we are replacing it with the correct one).   
2025-03-05 |  \- Added support to parse the unparsed logs.  
\- Mapped `data.userId to `principal.user.userid"  
\- Mapped `data.acuId` to `target.resource.id`.  
\- Mapped `data.acu.name` to `target.resource.name`.  
\- Mapped `data.acu.opal`, entry.siteId`, and `entry.zoneId` to `target.resource.attribute.labels".  
\- Mapped `data.connectionType`, `data.credentialOpal`, `entry.id`, `entry.name`, and `entry.opal` to `security_result.detection_fields`.  
\- Mapped `entry.entryStatecode` to `security_result.category_details`.  
\- Mapped `entry.statusDetails`, `entry.entryId`, `opal`, and `entryId` to `security_result.detection_fields`.  
\- Mapped `data.hardwareDAta.cardNumber`, `data.hardwareData.cardType`, and `data.hardware.numBits` to `additional.fields`.  
\- Mapped `data.hardwareData.requestId` to `network.session_id`.  
\- Mapped `data.httpUserAgent` to `network.http.user_agent`.  
\- Mapped `data.userOpal`, `data.validProximityOtp`, and `data.validProximityProof` to `additional.fields`.  
\- Mapped `data.org.id`, `data.org.name`, and `data.org.opal` to `target.resource.attribute.labels`.  
\- Mapped `data.readerId`, `data.requestType`, `source_type`, `data.thirdPartyReaderId`, and `data.thirdPartyWiegandId` to `additional.fields`.  
\- Mapped `data.requestId` to `security_result.detection_fields`.  
\- Mapped `data.requestStatusDetail` to `security_result.summary`.  
\- Mapped `data.requestUri` to `target.url`.  
\- Mapped `data.siteIds` and `data.zondeIds` to `target.resource.attribute.labels`.  
\- Mapped `data.status` to `network.http.response_code`.  
\- Mapped `event` to `metadata.product_event.type`.  
\- Mapped `host` to `principal.ip` and `principal.asset.ip`.   
2023-11-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
