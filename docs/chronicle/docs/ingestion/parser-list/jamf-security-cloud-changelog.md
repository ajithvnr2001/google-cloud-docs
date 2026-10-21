---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-security-cloud-changelog/
title: Change log for JAMF_SECURITY_CLOUD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:37:41.542154+00:00
---

# Change log for JAMF_SECURITY_CLOUD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/jamf-security-cloud-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JAMF_SECURITY_CLOUD

Date | Changes  
---|---  
2025-03-23 |  \- Added support for new pattern of JSON logs.  
\- Modified the mappings of `severity` as per the documentation provided.  
\- Mapped `externalId` to `metadata.product_log_id`.  
\- Mapped `customerId` to `principal.user.userid`.  
\- Mapped `user.userName` to `principal.user.user_display_name`.  
\- Mapped `user.userEmail` to `principal.user.email_addresses`.  
\- Mapped `event_dataType` to `additional.fields`.  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `eventTimeUtcMs` to `additional.fields`.  
\- Mapped `software.softwareId` to `additional.fields`.  
\- Mapped `software.softwareVersion` to `additional.fields`.  
\- Mapped `software.softwareName` to `additional.fields`.  
\- Mapped `cve.id` to `security_result.detection_fields`.  
\- Mapped `cve.description` to `metadata.description`  
\- Mapped `cve.baseScore` to `security_result.detection_fields`.  
\- Mapped `cve.severity` to `security_result.severity`  
\- Mapped `cve.exploitAvailable` to `security_result.detection_fields`.  
\- Mapped `cve.cveDetailUrl` to `security_result.url_back_to_product`  
\- Mapped `cve.attribution` to `security_result.detection_fields`.  
\- Mapped `cve.consoleUrl` to `principal.url`  
\- Mapped `metadata.product` to `metadata.product_event_type`.  
\- Mapped `threat.types` to `additional.fields`.  
\- Mapped `device.os.osVersion` to `target.platform_version`.  
\- Mapped `app.id`, `app.name`, `app.version` to `additional.fields`.  
\- Set `target.platform` to `LINUX` if `device.os.osType` is `Lin`.  
\- Set `target.platform` to `WINDOWS` if `device.os.osType` is `Win`.  
\- Set `target.platform` to `MAC` if `device.os.osType` is `MAC_OS`.  
\- Set `security_result.severity` to `INFORMATIONAL` if `severity` is 2.  
\- Set `security_result.severity` to `LOW` if `severity` is 4.  
\- Set `security_result.severity` to `MEDIUM` if `severity` is 6.  
\- Set `security_result.severity` to `HIGH` if `severity` is 8.  
\- Set `security_result.severity` to `CRITICAL` if `severity` is 10.  
\- Removed mapping of `destination.name` from `target.resource.name`.  
\- Mapped `destination.name` to `target.hostname` and `target.asset.hostname`.  
\- Removed mapping of `security_result.severity` to `INFORMATIONAL` if `severity` ranges from 0 to 19.  
\- Removed mapping of `security_result.severity` to `LOW` if `severity` ranges from 20 to 39.  
\- Removed mapping of `security_result.severity` to `MEDIUM` if `severity` ranges from 40 to 59.  
\- Removed mapping of `security_result.severity` to `HIGH` if `severity` ranges from 60 to 79.  
\- Removed mapping of `security_result.severity` to `CRITICAL` if `severity` ranges from 80 to 100.   
2025-01-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
