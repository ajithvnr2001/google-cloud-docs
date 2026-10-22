---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-scep-changelog/
title: Change log for MICROSOFT_SCEP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:43.472541+00:00
---

# Change log for MICROSOFT_SCEP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/microsoft-scep-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MICROSOFT_SCEP

Date | Changes  
---|---  
2025-02-24 |  Enhancement:  
\- Added `gsub` to remove `_` from the front of the `file_path` field.   
2025-02-18 |  Enhancement:  
\- Added parser to support the new format of json logs.  
\- Mapped to `has_user` to `target.user.userid`.  
\- Mapped to `resourceid` to `target.resource.name`.  
\- Mapped to `detectionid` to `detectionid_field.key`.  
\- Mapped to `dectectiontime` to `dectectiontime`.  
\- Mapped to `dest_nt_domain` to `target.administrative_domain`.   
2025-02-05 |  Enhancement:  
\- Added support to handle logs when path has multiple entries.   
2025-01-17 |  Enhancement:  
\- Added a new Grok pattern.  
\- Mapped `time` to `syslogtimestamp`.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `DetectionID`, `detection_source`, and `pending_action` to `security_result.detection_fields`.  
\- Mapped `ResourceID` to `target.resource.name`.  
\- Mapped `action` to `temp_action`.  
\- Mapped `action_type` to `principal.group.attribute.labels`.  
\- Mapped `dest_name` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `signature` to `additional.fields`.  
\- Mapped `category` to `security_result.category_details`.   
2025-01-16 |  Bug-Fix:  
\- Added new Grok patterns to parse `file_path` and `source_url` correctly.  
\- Mapped `Name` to `metadata.product_event_type`.   
2024-11-25 |  Enhancement:  
\- Added support to extract `source_url` from `Path` field when it contains `http`.   
2024-10-17 |  Enhancement:  
\- Mapped `UserName` to `principal.user.userid`.  
\- Mapped `Process` to `principal.process.file.full_path`.  
\- Mapped `NTdomain` to `principal.administrative_domain`.  
\- Mapped `file_path` to `target.file.full_path`.  
\- Mapped `source_url` to `src.url`.   
2024-08-13 |  Enhancement:  
\- Mapped `UserName` to `target.user.userid`.   
2024-03-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
