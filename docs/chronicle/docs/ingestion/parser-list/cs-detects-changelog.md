---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-detects-changelog/
title: Change log for CS_DETECTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:49:39.043054+00:00
---

# Change log for CS_DETECTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-detects-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CS_DETECTS

Date | Changes  
---|---  
2026-02-18 |  \- principal.user.userid: Removed mapping of `user_id` from `principal.user.userid` UDM field if `user_id` value is in valid SID format.  
\- principal.user.windows_sid: Newly mapped `user_id` raw log field with `principal.user.windows_sid` UDM field if `user_id` value is in valid SID format.   
2026-01-06 |  Updated existing mappings and added new mappings in order to introduce more accurate mappings.  
\- target.file.full_path: Removed mapping of `filepath` from `target.file.full_path` UDM field.  
\- target.process.file.full_path: Mapped `filepath` raw log field with `target.process.file.full_path` UDM field.  
\- target.file.sha256: Removed mapping of `sha256` from `target.file.sha256` UDM field.  
\- target.process.file.sha256: Mapped `sha256` raw log field with `target.process.file.sha256` UDM field.  
\- target.process.pid: Newly mapped `local_process_id` raw log field with `target.process.pid` UDM field.  
\- metadata.description: Removed mapping of `description` from `metadata.description` UDM field.  
\- security_result.description: Mapped `description` raw log field with `security_result.description` UDM field.  
\- target.process.pid: Removed mapping of `process_id` from `target.process.pid` UDM field.  
\- target.process.product_specific_process_id: Mapped `process_id` raw log field with `target.process.product_specific_process_id` UDM field.  
\- principal.process.command_line: Newly mapped `parent_details[cmdline]` raw log field with `principal.process.command_line` UDM field.  
\- principal.process.file.names: Newly mapped `parent_details[filename]` raw log field with `principal.process.file.names` UDM field.  
\- principal.process.file.full_path: Newly mapped `parent_details[filepath]` raw log field with `principal.process.file.full_path` UDM field.  
\- principal.process.pid: Newly mapped `parent_details[local_process_id]` raw log field with `principal.process.pid` UDM field.  
\- target.process.parent_process.pid: Newly mapped `parent_details[local_process_id]` raw log field with `target.process.parent_process.pid` UDM field.  
\- principal.process.product_specific_process_id: Newly mapped `parent_details[local_process_id]` raw log field with `principal.process.product_specific_process_id` UDM field.  
\- target.process.parent_process.product_specific_process_id: Newly mapped `parent_details[local_process_id]` raw log field with `target.process.parent_process.product_specific_process_id` UDM field.  
\- principal.process.file.md5: Newly mapped `parent_details[md5]` raw log field with `principal.process.file.md5` UDM field.  
\- target.process.parent_process.file.sha256: Newly mapped `parent_details[sha256]` raw log field with `target.process.parent_process.file.sha256` UDM field.  
\- principal.process.parent_process.command_line: Newly mapped `grandparent_details[cmdline]` raw log field with `principal.process.parent_process.command_line` UDM field.  
\- target.process.parent_process.parent_process.command_line: Newly mapped `grandparent_details[cmdline]` raw log field with `target.process.parent_process.parent_process.command_line` UDM field.  
\- principal.process.parent_process.file.names: Newly mapped `grandparent_details[filename]` raw log field with `principal.process.parent_process.file.names` UDM field.  
\- target.process.parent_process.parent_process.file.names: Newly mapped `grandparent_details[filename]` raw log field with `target.process.parent_process.parent_process.file.names` UDM field.  
\- principal.process.parent_process.file.full_path: Newly mapped `grandparent_details[filepath]` raw log field with `principal.process.parent_process.file.full_path` UDM field.  
\- target.process.parent_process.parent_process.file.full_path: Newly mapped `grandparent_details[filepath]` raw log field with `target.process.parent_process.parent_process.file.full_path` UDM field.  
\- principal.process.parent_process.pid: Newly mapped `grandparent_details[local_process_id]` raw log field with `principal.process.parent_process.pid` UDM field.  
\- target.process.parent_process.parent_process.pid: Newly mapped `grandparent_details[local_process_id]` raw log field with `target.process.parent_process.parent_process.pid` UDM field.  
\- principal.process.parent_process.product_specific_process_id: Newly mapped `grandparent_details[process_id]` raw log field with `principal.process.parent_process.product_specific_process_id` UDM field.  
\- target.process.parent_process.parent_process.product_specific_process_id: Newly mapped `grandparent_details[process_id]` raw log field with `target.process.parent_process.parent_process.product_specific_process_id` UDM field.  
\- principal.process.parent_process.file.md5: Newly mapped `grandparent_details[md5]` raw log field with `principal.process.parent_process.file.md5` UDM field.  
\- target.process.parent_process.parent_process.file.md5: Newly mapped `grandparent_details[md5]` raw log field with `target.process.parent_process.parent_process.file.md5` UDM field.  
\- principal.process.parent_process.file.sha256: Newly mapped `grandparent_details[sha256]` raw log field with `principal.process.parent_process.file.sha256` UDM field.  
\- target.process.parent_process.parent_process.file.sha256: Newly mapped `grandparent_details[sha256]` raw log field with `target.process.parent_process.parent_process.file.sha256` UDM field.   
2025-08-26 |  Changing existing mappings in order to introduce more accurate mappings for `target.process.command_line`, `target.file.full_path` and `target.file.sha256` for the epp product and ofp type.  
\- target.process.command_line: Removed mapping of `cmdline` from `target.process.command_line` UDM field when `macros.cmdline` raw log field is not empty.  
\- security_result.detection_fields[cmdline]: Mapped `cmdline` raw log field with `security_result.detection_fields[cmdline]` UDM field when `macros.cmdline` raw log field is not empty.  
\- target.process.command_line: Newly mapped `macros.cmdline` raw log field with `target.process.command_line` UDM field.  
\- target.file.full_path: Removed mapping of `filepath` from `target.file.full_path` UDM field when `macros.ioc_description` raw log field is not empty.  
\- security_result.detection_fields[filepath]: Mapped `filepath` raw log field with `security_result.detection_fields[filepath]` UDM field when `macros.ioc_description` raw log field is not empty.  
\- target.file.full_path: Newly mapped `macros.ioc_description` raw log field with `target.file.full_path` UDM field.  
\- target.file.sha256: Removed mapping of `sha256` from `target.file.sha256` UDM field when `macros.ioc_value` raw log field is not empty and `macros.ioc_type` is equal to `hash_sha256`.  
\- security_result.detection_fields[sha256]: Mapped `sha256` raw log field with `security_result.detection_fields[sha256]` UDM field when `macros.ioc_value` raw log field is not empty and `macros.ioc_type` is equal to `hash_sha256`.  
\- target.file.sha256: Newly mapped `macros.ioc_value` raw log field with `target.file.sha256` UDM field when `macros.ioc_type` is equal to `hash_sha256`.  
\- security_result.detection_fields[macros_display_name]: Newly mapped `macros.display_name` raw log field with `security_result.detection_fields[macros_display_name]` UDM field.  
\- security_result.detection_fields[macros_ioc_source]: Newly mapped `macros.ioc_source` raw log field with `security_result.detection_fields[macros_ioc_source]` UDM field.  
\- security_result.detection_fields[macros_md5]: Newly mapped `macros.md5` raw log field with `security_result.detection_fields[macros_md5]` UDM field when `macros.md5` raw log field is not equal to `N/A`.  
\- security_result.detection_fields[macros_sha256]: Newly mapped `macros.sha256` raw log field with `security_result.detection_fields[macros_sha256]` UDM field.  
\- security_result.detection_fields[macros_type]: Newly mapped `macros.type` raw log field with `security_result.detection_fields[macros_type]` UDM field.  
\- security_result.detection_fields: Newly mapped `macros.ioc_type` raw log field with `security_result.detection_fields.key` UDM field and `macros.ioc_value` raw log field with `security_result.detection_fields.value` UDM field.   
2025-06-27 |  \- security_result.detection_fields: Newly mapped `ioc_value` raw log field with `security_result.detection_fields` UDM field   
2025-06-06 |  \- metadata.product_event_type: Newly mapped `product` raw log field with `metadata.product_event_type` UDM field   
2025-04-01 |  \- Newly created parser.  
\- Parser mappings improved. Contact your Google representative to get a detailed list of all changes.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
