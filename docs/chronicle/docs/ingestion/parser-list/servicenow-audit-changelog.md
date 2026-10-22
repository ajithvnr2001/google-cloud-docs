---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-audit-changelog/
title: Change log for SERVICENOW_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:59.497392+00:00
---

# Change log for SERVICENOW_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SERVICENOW_AUDIT

Date | Changes  
---|---  
2026-07-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for new timestamp format for `sys_created_on` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-12-19 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Changed the priority of `user` raw log field mapping with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `_logged_in_user` and `_user` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-01 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `_logged_in_user`, `_user`, `user` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `_system_id` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `_session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `_logger_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `tablename` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `documentkey` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `newvalue`, `oldvalue`, `_log_table`, `fieldname`, `_is_impersonating`, `_log_table_field_name`, `_log_table_table_name`, `_page_name`, `_source_type`, `internal_checkpoint`, `record_checkpoint`, and `_txid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-14 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `sys_created_on` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `sys_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `parm2` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `parm2` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_id`, `parm1`, and `parm2` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `claimed_by` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `claimed_by` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `claimed_by_data` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `instance` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `system_property`, `name`, `derived_priority`, `sys_mod_count`, `partition`, `processing_duration`, `state`, `descriptive_name`, `process_on`, `processed`, `queue`, `sys_updated_on`, `sys_updated_by`, `sys_created_by`, and `table` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `desc` contains `login`, or `name` is `session.established` or `login` and a user is present, updated to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.event_type` and `event.idm.read_only_udm.extensions.auth.type`: If `name` is `logout` or `session.terminated` and a user is present, updated to `USER_LOGOUT` and `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If a user is present and the event is not a login or logout, updated to `USER_UNCATEGORIZED`.   
2025-05-21 |  Enhancement:  
\- Added Grok pattern to provide support for SYSLOG logs.  
\- Extracted the `User` from the log using the Grok pattern, which is mapped to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `statprin_ipus` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `statprin_ipus` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `exportByteSize` and `exportRecordCount` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `event.idm.read_only_udm.principal.ip` is getting populated.   
2025-05-16 |  Enhancement:  
\- Added Grok pattern to provide support for SYSLOG logs.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- If `status` is equal to `successful` then set `security_result_action` to `ALLOW`.  
\- If `status` is equal to `failure` then set `security_result_action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `security_result_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result`: Newly merged `security_result` to `event.idm.read_only_udm.security_result` UDM field.   
2025-01-15 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
