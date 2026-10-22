---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cis-albert-alert-changelog/
title: Change log for CIS_ALBERT_ALERT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:58.410779+00:00
---

# Change log for CIS_ALBERT_ALERT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cis-albert-alert-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CIS_ALBERT_ALERT

Date | Changes  
---|---  
2025-05-19 |  Enhancement -  
\- Added grok pattern for `analysis` field.  
\- Added `gsub` to remove backslash and single quote immediately followed by alphanumeric or underscore characters.  
\- Added a `gsub` which looks for a sequence of alphabetic characters followed by a backslash and a single quote.Removes the backslash and single quote, keeping only the alphabetic characters.  
\- Added a `gsub` that searches for patterns that start with any character, followed by an opening curly brace, then any content, followed by a closing curly brace, and finally a comma. It replaces that entire pattern with just a comma.  
\- Added a `grok` pattern which block tries to extract two pieces of information (json1 and json2) from the extension field.  
\- Added a `gsub` that looks for `[.]` within the analysis field and replaces it with a single dot `.` .   
2025-04-16 |  Enhancement -  
\- Added `overwrite` and `on_error` to `grok`.  
\- Added `drop` for malformed logs.  
\- `json_log`: Added support for `json_log` format.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `sourceip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Updated `has_principal` to `true` when `event.idm.read_only_udm.principal.ip` or `event.idm.read_only_udm.principal.asset.ip` is not null.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `queue`, `activity_summary`, `siem_event_id`, `previous_escalations` and `status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `logical_sensor_id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `event.idm.read_only_udm.security_result.severity` raw log field with `LOW` if `severity` is `Informational`, `MEDIUM` if `severity` is `Warning` and `HIGH` if `severity` is `Critical`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `analysis` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` raw log field with `STATUS_UPDATE` if `has_principal` is `true`.   
2022-10-10 |  Enhancement - Some logs contain malformed data (such as extra \") which cause JSON parsing to fail.  
Added regex`s and gsub`s to transform logs into valid JSON format.  
\- Added conditional check for fields `src_ip`, `target_ip`, `target_port`, `protocol`.   
2022-05-20 |  Enhancement - Some logs contain malformed data (such as extra \") which cause JSON parsing to fail.  
Added regex`s and gsub`s to transform logs into valid JSON format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
