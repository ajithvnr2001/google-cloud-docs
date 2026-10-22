---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-central-changelog/
title: Change log for TRENDMICRO_APEX_CENTRAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:32.172642+00:00
---

# Change log for TRENDMICRO_APEX_CENTRAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-apex-central-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_APEX_CENTRAL

Date | Changes  
---|---  
2026-09-02 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Added support for new date format when parsing the rt raw log field to map to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-03-25 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs3` (key: `Product_Version`) raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Initialized `deviceNtDomain` to null to avoid parsing errors. This change is resulting mapping of following fields correctly:  
-`event.idm.read_only_udm.metadata.event_timestamp.seconds`.  
-`event.idm.read_only_udm.metadata.event_type`.  
-`event.idm.read_only_udm.metadata.log_type`.  
-`event.idm.read_only_udm.metadata.product_event_type`.  
-`event.idm.read_only_udm.metadata.product_log_id`.  
-`event.idm.read_only_udm.metadata.product_name`.  
-`event.idm.read_only_udm.metadata.product_version`.  
-`event.idm.read_only_udm.metadata.vendor_name`.  
-`event.idm.read_only_udm.principal.asset.hostname`.  
-`event.idm.read_only_udm.principal.asset.ip`.  
-`event.idm.read_only_udm.principal.asset.platform_software.platform_version`.  
-`event.idm.read_only_udm.principal.hostname`.  
-`event.idm.read_only_udm.principal.ip`.  
-`event.idm.read_only_udm.principal.user.userid`.  
-`event.idm.read_only_udm.security_result.action_details`.  
-`event.idm.read_only_udm.security_result.description`.  
-`event.idm.read_only_udm.security_result.detection_fields.key`.  
-`event.idm.read_only_udm.security_result.detection_fields.value`.  
-`event.idm.read_only_udm.security_result.severity`.  
-`event.idm.read_only_udm.security_result.threat_name`.  
-`event.idm.read_only_udm.security_result.verdict_info.malicious_count`.  
-`event.idm.read_only_udm.src.asset.hostname`.  
-`event.idm.read_only_udm.src.hostname`.  
-`event.idm.read_only_udm.target.file.full_path`.  
-`event.idm.read_only_udm.target.file.names`.  
-`event.idm.read_only_udm.target.user.userid`.   
2025-01-23 |  Enhancement:  
\- If the message contains `spyware`, then mapped `cs5` to `security_result.action_details` and `severity` to `security_result.severity`.  
\- When `cn2Label` is `Scan_Type`, then mapped `security_result.description` based on `cn2`.   
2024-12-04 |  Enhancement:  
\- When `cn2Label` is `Second_Action` and `cn2` is `1` then mapped `var_cn2_label.value` to `N/A`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `0` then mapped `var_cn2_label.value` to `Unknown`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `2` then mapped `var_cn2_label.value` to `Clean`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `3` then mapped `var_cn2_label.value` to `Delete`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `4` then mapped `var_cn2_label.value` to `Move`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `5` then mapped `var_cn2_label.value` to `Rename`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `6` then mapped `var_cn2_label.value` to `Pass/Log`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `7` then mapped `var_cn2_label.value` to `Strip`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `8` then mapped `var_cn2_label.value` to `Drop`.  
\- When `cn2Label` is `Second_Action` and `cn2` is `9` then mapped `var_cn2_label.value` to `Quarantine`.   
2024-09-23 |  \- Changed the `fileHash` field to lowercase.  
\- Mapped `dntdom` to `target.administrative_domain`.  
\- Mapped `event_name` to `security_result.threat_name`.  
\- Mapped `dhost` to `principal.hostname`.  
\- Mapped `filePath` to `target.file.full_path`.  
\- Mapped `duser` to `target.user.userid`.  
\- Mapped `cs3` to `metadata.product_version`.  
\- Mapped `cs6` to `additional.fields`.  
\- Mapped `product_version` to `additional.fields`.  
\- Mapped `cat` to `additional.fields`.  
\- Mapped `msg` to `additional.fields`.  
\- Mapped `TMCMLogDetectedIP` to `additional.fields`.  
\- Mapped `dvchost` to `additional.fields`.  
\- Mapped `cnt` to `security_result.verdict_info.malicious_count`.  
\- Mapped `cs4` to `security_result.category_details`.   
2024-08-12 |  \- When `dvchost` is available, then mapped `metadata.event_type` to `STATUS_UPDATE`.   
2024-04-24 |  \- Added support for new event type `Endpoint Application Control`  
2024-04-03 |  \- Added new attributes and support for customer specific new log format (CEF).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
