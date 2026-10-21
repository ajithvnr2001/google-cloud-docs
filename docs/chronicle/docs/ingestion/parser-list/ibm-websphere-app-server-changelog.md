---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-websphere-app-server-changelog/
title: Change log for IBM_WEBSPHERE_APP_SERVER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:36:09.723421+00:00
---

# Change log for IBM_WEBSPHERE_APP_SERVER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-websphere-app-server-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_WEBSPHERE_APP_SERVER

Date | Changes  
---|---  
2026-05-14 |  Enhancement:  
\- Added a grok pattern on `description` to extract `principal_user`, `exception_code`, `exception_class` fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `exception_code`, `exception_class` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when principal userid details are present.   
2026-04-23 |  Enhancement:  
\- Modified grok pattern to parse new format of syslogs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `exception_type`, `ldap_error_code`, `hex_error_code`, `NameErr`, `problem_code` and `data_value` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `problem_description` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-04-01 |  Enhancement:  
\- Modified grok pattern on `msg` to extract `source_line`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `source_line` and `length` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: If `os_name` contains `windows`, Set the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `WINDOWS`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `websphere_java_version` (key: `websphere_java_version`), `websphere_platform_details` (key: `websphere_platform_details`), `java_compiler` (key: `java_compiler`), `java_vm_name` (key: `java_vm_name`), `parent_context` (key: `parent_context`), `event_context` (key: `event_context`) and `method_name` (key: `method_name`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `principal_application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `os_version` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_patch_level`: Newly mapped `os_name` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_patch_level` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `full_orb_version` (key: `full_orb_version`) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `target_application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- Added the grok patterns to ensure incorrect values are no longer being mapped to `event.idm.read_only_udm.metadata.event_timestamp.nanos` UDM field. Additionally, this is allowing the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.process.file.full_path`  
2025-10-03 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `inter_app` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `prin_pid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `level` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `level` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sess_id` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ThreadId`, `logSource`, `app_specific_tag`, `sectok`, `FINSESSION_ID` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional checks to map `product`, `vendor`, and `file_name` to `event.idm.read_only_udm.metadata.product_name`, `event.idm.read_only_udm.metadata.vendor_name`, and `event.idm.read_only_udm.target.file.full_path` only if the raw fields are not empty.  
\- Added grok pattern in order to parse new pattern of syslog logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
