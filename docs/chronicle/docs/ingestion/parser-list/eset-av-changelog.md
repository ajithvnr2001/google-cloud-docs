---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-av-changelog/
title: Change log for ESET_AV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:24:27.842726+00:00
---

# Change log for ESET_AV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/eset-av-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ESET_AV

Date | Changes  
---|---  
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Removed mapping of `host` from `event.idm.read_only_udm.intermediary.hostname` UDM field as it represents the hostname of the device.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `deviceOSName` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `eventDesc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `intermediary_app` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `aggregate_count` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `sourceAddressType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `targetAddressType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `deviceOSName` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.   
2026-03-30 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `desc` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `Login attempt`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.   
2025-06-03 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `occurred` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field. If `occurred` value is not empty then map it to `metadata.event_timestamp` else map `time` to `metadata.event_timestamp`.   
2025-04-10 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `threatHandled` and `needRestart` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `actionTaken` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `threatName` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `threatType` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- If `threatHandled` value is `1` then map `event.idm.read_only_udm.security_result.action` to `BLOCK` else if `threatHandled` value is `0` then map `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- If `severity` is in `7` or `8` then map `event.idm.read_only_udm.security_result.severity` to `HIGH` else if `severity` is `6` then map `event.idm.read_only_udm.security_result.severity` to `MEDIUM` else if `severity` is in `3` or `1` then map `event.idm.read_only_udm.security_result.severity` to `LOW` else if `severity` is `10` then map `event.idm.read_only_udm.security_result.severity` to `CRITICAL`.   
2025-03-04 |  Enhancement:  
\- Added a new Grok pattern to parse new type of logs.  
\- Mapped `time` to `metadata.event_timestamp`.  
\- Mapped `target` to `target.resource.attribute.labels`.   
2024-06-25 |  Enhancement:  
\- Mapped `object_uri` to `target.url`.  
\- Mapped `severity` to `security_result.severity_details`  
\- Mapped `threat_flags` to `security_result.detection_fields`.  
\- Mapped `category` to `security_result.category_details`.  
\- Mapped `object_type` and `engine_version` to `principal.resource.attribute.labels`  
\- If value of the field `detail` is null, then mapped `circumstances` to `security_result.description`.  
\- If value of the field `action_taken` is similar to `Block`, then mapped `security_result_action` to `BLOCK`.  
\- If value of the field `action_taken` is similar to `Start` or `Allow`, then mapped `security_result_action` to `ALLOW`.  
\- If the value of `not_json` is true, then added a Grok pattern over `json_data` to extract `category`, `hostname`, and `group_name`.   
2024-05-31 |  Enhancement:  
\- Mapped `action_taken` to `security_result.action_details`.  
\- Mapped `threat_type` to `security_result.threat_id`.  
\- Mapped `scan_id`, `scanner_id`, and `threat_handled` to `security_result.detection_fields`.  
\- Mapped `need_restart` to `additional.fields`.   
2024-05-21 |  Enhancement:  
\- Changed the case of the value of the field `hash` to lowercase, and then mapped `hash` to `principal.file.sha1`.   
2024-03-14 |  Enhancement:  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `group_name` to `principal.group_display_name`.  
\- Mapped `hash` to `principal.resource.attribute.labels`.  
\- Mapped `eiconsolelink` to `principal.url`.  
\- Mapped `os_name` to `principal.platform_version`.  
\- Mapped `processname` to `principal.process.file.full_path`.  
\- Mapped `rulename` to `security_result.rule_name`.  
\- Mapped `result` to `security_result.summary`.  
\- Mapped `eialarmid` to `security_result.detection_fields`.  
\- Mapped `severity_score` to `security_result.detection_fields`.  
\- Mapped `computer_severity_score` to `security_result.detection_fields`.   
2023-01-10 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
