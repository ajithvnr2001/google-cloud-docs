---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-changelog/
title: Change log for RUBRIK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:58:22.086967+00:00
---

# Change log for RUBRIK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rubrik-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RUBRIK

Date | Changes  
---|---  
2025-01-22 |  Enhancement:  
\- Added support to parse JSON log formats.   
2025-01-16 |  Enhancement:  
\- Renamed `product_event_type` to `source`.  
\- Mapped `source` to `additional.fields`.  
\- Mapped `src_host` to `intermediary.hostname`.   
2024-12-24 |  Enhancement  
\- Added support for syslog pattern to parse the unparsed logs.  
\- Mapped `eventSeverity` to `security_result.severity`.  
\- Mapped `eventId` to `metadata.product_log_id`.  
\- Mapped `objectType` to `security_result.detection_fields`.  
\- Mapped `nodeId` to `additional.fields`.  
\- Mapped `eventDetail` to `additional.fields`.  
\- Mapped `objectId` to `principal.resource.product_object_id`.  
\- Mapped `nodeIpAddress`, `src_ip1`, `src_ip2` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `status` to `security_result.detection_fields`.  
\- Mapped `eventSeriesId` to `additional.fields`.  
\- Mapped `clusterName` to `target.resource.name`.  
\- Mapped `eventName` to `additional.fields`.  
\- Mapped `desc` to `metadata.description`.  
\- Mapped `app_function` to `additional.fields`.  
\- Mapped `app` to `metadata.product_name`.  
\- Mapped `eventType` to `metadata.product_event_type`.  
\- Mapped `sec_desc` to `security_result.description`.   
2024-12-09 |  Enhancement:  
\- Improved the default RUBRIK parser to handle KV data.   
2022-12-01 |  Enhancement - Modified grok pattern to parse `Rubrik Polaris` logtypes.  
Mapped the field `iD` to `metadata.product_log_id`.  
Mapped the field `severity` to `security_result.severity`.  
Mapped the field `lastActivityStatus` to `security_result.action_details`.  
Mapped the field `clusterName` to `target.resource.name`.  
Mapped the field `clusterID` to `target.resource.product_object_id`.   
2022-07-01 |  Enhancement - Modified grok pattern to parse `ansible-command`, `sshd`, `Rubrik` logtypes.  
Mapped `event.idm.read_only_udm.metadata.event_type` to status_update from Generic_event.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
