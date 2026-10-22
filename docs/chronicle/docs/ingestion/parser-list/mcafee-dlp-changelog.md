---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-dlp-changelog/
title: Change log for MCAFEE_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:40.056655+00:00
---

# Change log for MCAFEE_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_DLP

Date | Changes  
---|---  
2025-12-04 |  Enhancement:  
-`event.idm.read_only_udm.principal.labels`: Removed mapping of `status_id` from `event.idm.read_only_udm.principal.labels` UDM field since it is deprecated.  
-`event.idm.read_only_udm.additional.fields`: Mapped `status_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added null conditional checks for the fields to ensure they are not empty before processing.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal_user` flag is true, updated to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` flag is true, updated to `STATUS_UPDATE`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_address` field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-11-24 |  \- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `resolution_id`, `expected_action` from `event.idm.read_only_udm.security_result.about.labels` UDM field since it is deprecated.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `resolution_id`, `expected_action` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional check for user_ou.   
2022-04-13 |  Enhancement-Added mappings for following fields:  
`sev` to `security_result.severity_details`  
`action` to `security_result.action_details`  
`dst` to `target.user.userid`  
`status_id` to `principal.labels`  
`usb_serial_number`, `encrypt`, `volume_serial_number` to `security_result.detection_fields`  
`fail_reason`, `evidence_count`, `total_count`, `total_size`, `class_count`, `class_display`, `count`, to `additional.fields`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
