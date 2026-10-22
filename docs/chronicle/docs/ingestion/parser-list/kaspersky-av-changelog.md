---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-av-changelog/
title: Change log for KASPERSKY_AV \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:40.282165+00:00
---

# Change log for KASPERSKY_AV  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kaspersky-av-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KASPERSKY_AV

Date | Changes  
---|---  
2025-10-24 |  Enhancement:  
\- Updated the mapping for `event.idm.read_only_udm.target.user.userid` UDM field. It now a conditional mapping to use the value of `User` raw log field if present, and falls back to `Bruker` raw log field only if `User` is not available in `cef_udm_mapping.include` file.  
\- Modified the logic to set the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `target_hostname_present` or `target_machine_id_present` is `true`, else to `STATUS_UPDATE` when `event_type_set` is `false` and `principal_machine_id_present` is `true`, else to `GENERIC_EVENT`.  
\- Newly added gsub for the `ID del proceso` raw log field to `process_id` raw log field.   
2025-10-08 |  Enhancement:  
\- Added a grok pattern to parse the new log format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs9`, `cn1`, `kl_event_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `cs10` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `cs4` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `vendor_name` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product_name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.   
2025-03-12 |  Enhancement:  
\- Mapped `tdn` to `additional.fields`.  
\- Mapped `file_name` to `target.file.names`.  
\- Mapped `Event_Component` to `additional.fields`.  
\- Mapped `EventType` to `additional.fields`.  
\- Mapped `certificate_verification_status` to `security_result.detection_fields`.  
\- Mapped `threat_level` to `vulnerabilities.severity_details`.  
\- Mapped `object_type` to `security_result.detection_fields`.  
\- Mapped `object_name` to `security_result.detection_fields`.  
\- Mapped `object_path` to `security_result.detection_fields`.  
\- Mapped `bid_id` to `security_result.detection_fields`.  
\- Mapped `et2` to `security_result.detection_fields`.  
\- Mapped `exchange` to `security_result.detection_fields`.  
\- Mapped `ifm_ori` to `security_result.detection_fields`.  
\- Mapped `pub` to `security_result.detection_fields`.  
\- Mapped `publisher_id` to `security_result.detection_fields`.  
\- Mapped `sec_id` to `security_result.detection_fields`.  
\- Mapped `site_id` to `security_result.detection_fields`.  
\- Mapped `xrtb_id` to `security_result.detection_fields`.  
\- Mapped `ip` to `principal.ip` and `principal.asset.ip`.   
2025-02-13 |  Enhancement:  
\- Added support to parse the unparsed CEF logs.   
2025-02-05 |  Enhancement:  
\- Added support to parse the unparsed CEF logs.   
2023-10-13 |  Enhancement:  
\- Mapped `Hachage SHA256`, `p1` to `target.process.file.sha256`.  
\- Mapped `Hachage MD5`, `md5` to `target.process.file.md5`.  
\- Mapped `intermediary` to `event.idm.read_only_udm.intermediary`.   
2022-10-14 |  Added gsub to bypass unwanted special characters.   
2022-05-17 |  Added mappings for the following fields:  
\- Nom (name of the process/application) (Name) mapped to target.file.full_path (extension).  
\- Chemin de l'application (Application path) mapped to target.file.full_path.  
\- Type d'événement (Event type) mapped to metadata.product_event_type.  
\- ID du processus (Process id) mapped to target.process.pid.  
\- Description du résultat (Result description) mapped to metadata.description.  
\- Erreur (Error) mapped to security_result.summary.   
2022-03-29 |  Added mappings for the following missing fields:  
`Result description` to `security_result.description`.  
`Type` to `security_result.threat_name`.  
`MD5` to `process.file.md5`.  
`SHA256` to `process.file.sha256`.  
`p2` to `target.process.file.full_path`.  
`p5` to `security_result.rule_name`.  
`p7` to `principal.user.user_display_name`.  
`Reason` to `security_result.summary`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
