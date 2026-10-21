---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-casb-changelog/
title: Change log for SYMANTEC_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:57:12.627925+00:00
---

# Change log for SYMANTEC_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_CASB

Date | Changes  
---|---  
2024-10-25 |  Enhancement:  
\- Added support for JSON logs.   
2024-03-19 |  Enhancement:  
\- Mapped `content_checks.dlp.updated_timestamp` to `additional.fields`.  
\- Mapped `content_checks.vk_encryption` to `security_result.detection_fields`.  
\- Mapped `user`, `user_mail`, and `user_uid` to `principal.user.email_addresses`.  
\- Mapped `user_email`, `mailbox_owner`, `product_data.target`, and `user_uid` to `target.user.email_addresses`.   
2024-02-19 |  Enhancement:  
\- Added support to parse JSON logs coming in single quotations.  
\- Mapped `severity` to `security_result.severity_details`.   
2024-02-16 |  \- Resolved flakiness issue by replacing `instance.0` with `instance` when it is not an array.   
2024-02-11 |  Enhancement:  
\- Added support for logs of format JSON.  
\- Mapped `_id` to `metadata.product_log_id`.  
\- Mapped `__event_timestamp` to `metadata.event_timestamp`.  
\- Mapped `_elastic_timestamp`, `created_timestamp`, `inserted_timestamp`, `updated_timestamp`, `responsible_logs` and `sub_feature` to `additional.fields`.  
\- Mapped `threat_score`, `locations`, `transaction_id`, `content_checks.dlp.raw_response.requestid`, `content_checks.dlp.raw_response.responseaction`, `org_unit`, `policy_type`, `content_checks.vk_pci`, `content_checks.vk_vba_macros`, `content_checks.vk_glba`, `content_checks.vk_source_code`, `content_checks.vk_pii`, `content_checks.vk_virus`, `content_checks.vk_hipaa`, `content_checks.violations`, `object_name`, `multi_user`, `risks`, `name`, `_latency`, `content_checks.dlp.raw_response.warning`, `content_checks.dlp.raw_response.violation`, `content_checks.dlp.raw_response.contentdetails`, `content_checks.vk_dlp_policy_violations`, `content_checks.risktype_list`, `content_checks.vk_content_iq_violations`, `actions_taken`, `__detect_source`, `multi_facility`, `content_checks.vba_macros.expressions` and `policy_violated` to `security_result.detection_fields`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `file_size` to `product_data.file_size`.  
\- Mapped `source` to `principal.resource.attribute.labels`.  
\- Mapped `resource_id` to `target.resource.id`.  
\- Mapped `policy_action` to `security_result.action_details`.  
\- Mapped `object_type` to `target.resource.name`.  
\- Mapped `ioi_code` to `security_result.summary`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `content_checks.filename` to `target.file.full_path`.  
\- Mapped `content_checks.mimetype` to `target.file.mime_type`.  
\- Mapped `activity_type` to `metadata.product_event_type`.  
\- Mapped `service` to `target.application`.  
\- Mapped `_domain` to `target.hostname`.  
\- Mapped `hosts` to `principal.ip`.  
\- If `has_principal` is `true` then set `metadata.event_type` as `STATUS_UPDATE`.  
\- If `has_principal_user` is `true`, `has_target` is `true` and `has_principal` is `false`, then set `metadata.event_type` as `USER_UNCATEGORIZED`.  
\- If `has_principal_user` is `true`, `has_target` is `true` and `has_principal` is `true`, then set `metadata.event_type` as `USER_LOGIN`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
