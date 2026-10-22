---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiedr-changelog/
title: Change log for FORTINET_FORTIEDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:06.776631+00:00
---

# Change log for FORTINET_FORTIEDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiedr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FORTIEDR

Date | Changes  
---|---  
2026-04-01 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Stack Certificates` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Destination` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Updated a grok pattern to parse the new format of SYSLOG logs.   
2025-11-12 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `Command line` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `Process Hash` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `Threat Name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `Threat Type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Organization ID`, `Raw Data ID`, `Collector Group`, `Device State`, `Count`, `Deployment`, `Certificate`, `Script`, `Script Path`, `Autonomous System`, `Remediation Processes`, `Remediation Files`, `Remote Connection` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `Stack Hashes`, `Threat Family` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `Process Type` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Target` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.techniques: Newly mapped `MITRE techniques` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- event.idm.read_only_udm.security_result.attack_details.tactics: Newly mapped `MITRE techniques` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.   
2025-04-17 |  Enhancement:  
\- Added a Grok pattern to parse new type of logs.  
\- Added condition to check if mac raw log field is valid mac or not  
\- Added condition to check if `asset_os` raw log field has `WINDOWS` or `LINUX` or `MAC`.   
2024-12-13 |  Bug-fix:  
\- Mapped `sec_result.severity` to High when `sec_result.severity` is `High`.  
\- Mapped `Action` to `sec_result.action_details` when Action is Logged.  
\- Mapped timestamp to `metadata.event_timestamp`.   
2024-09-16 |  Enhancement:  
\- Added a Grok pattern to map `Operating System: Linux` to `principal.platform`.   
2024-09-02 |  Enhancement:  
\- Mapped `Users` to `additional.fields`.   
2023-08-07 |  Enhancement:  
\- Added Grok pattern to handle new log format.   
2023-07-06 |  Enhancement:  
\- Mapped `device_name` to `principal.hostname`.  
\- Mapped `Component Name` to `additional.fields`.  
\- Mapped `process_name` to `principal.application`.  
\- Mapped `Operating System` to `principal.platform`.  
\- Mapped `os_version` to `principal.platform_version`.  
\- Mapped `userId` to `principal.user.userId`.  
\- Mapped `userDisplayName` to `principal.user.userId`.  
\- Mapped `event_id` to `metadata.product_log_id`.  
\- Mapped `mac_address` to `principal.mac`.  
\- Mapped `Organization` to `additional.fields`.  
\- Mapped `dst` to `target.ip`.  
\- Mapped `intermediary_ip` to `intermediary.ip`.  
\- Mapped `server_host` to `security_result.detection_fields`.  
\- Mapped `description_details` to `metadata.description`.   
2023-05-09 |  \- Added Grok pattern to handle unparsed logs.  
\- Mapped the field `Destination` to `target.ip`.  
\- Mapped the `metadata.event_type` to `USER_LOGIN` where the field `description` contains `System login`.  
\- Mapped the `metadata.event_type` to `USER_LOGOUT` where the field `description` contains `System logout`.  
\- Changed the `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` where `target.user.userid` is not null.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
