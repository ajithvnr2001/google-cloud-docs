---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-threats-changelog/
title: Change log for PROOFPOINT_TAP_THREATS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:00:58.336839+00:00
---

# Change log for PROOFPOINT_TAP_THREATS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-tap-threats-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_TAP_THREATS

Date | Changes  
---|---  
2025-01-09 |  \- Newly created parser.  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `TAP Threats` to `metadata.product_name`.  
\- Mapped `Proofpoint` to `metadata.vendor_name`.  
\- Mapped `Proofpoint_Threats_Feed` to `metadata.product_event_type`.  
\- Mapped `name` to `security_result.threat_name`.  
\- Mapped `identifiedAt` to `security_result.first_discovered_time`.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `status` to `security_result.threat_status`.  
\- Mapped `severityScore` to `threat_result.severity` and `threat_result.severity_details`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `attackSpread` to `security_result.verdict_info.global_customer_count`.  
\- Mapped `geoTargeted` to `additional.fields`.  
\- Mapped `verticallyTargeted` to `additional.fields`.  
\- Mapped `notable` to `additional.fields` and `security_result.priority`.  
\- Mapped `detectionType` to `additional.fields`.  
\- Mapped `actors` to `security_result.associations.associated_actors`.  
\- Mapped `families` to `security_result.associations.associated_actors`.  
\- Mapped `malware` to `security_result.associations.associated_actors`.  
\- Mapped `techniques` to `security_result.attack_details.techniques`.  
\- Mapped `brands` to `security_result.associations.associated_actors`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
