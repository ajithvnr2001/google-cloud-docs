---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iiq-changelog/
title: Change log for SAILPOINT_IIQ \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:02:49.703847+00:00
---

# Change log for SAILPOINT_IIQ  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sailpoint-iiq-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAILPOINT_IIQ

Date | Changes  
---|---  
2026-02-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `created` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `lauer`, `launcher`, `source`, `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host`, `client_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `server_host`, `server` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_host` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Modified mapping logic for `event.idm.read_only_udm.metadata.product_log_id` to map `id` raw log field globally.  
\- `event.idm.read_only_udm.principal.application`: Modified mapping logic for `event.idm.read_only_udm.principal.application` to map `application` raw log field globally.  
\- `event.idm.read_only_udm.security_result.severity`:  
\- Setting `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL` when `event_level` raw log field is `INFORMATIONAL`.  
\- Setting `event.idm.read_only_udm.security_result.severity` to `LOW` when `event_level` raw log field is `LOW`.  
\- Setting `event.idm.read_only_udm.security_result.severity` to `HIGH` when `event_level` raw log field is `HIGH`.  
\- Setting `event.idm.read_only_udm.security_result.severity` to `CRITICAL` when `event_level` raw log field is `CRITICAL`.  
\- Setting `event.idm.read_only_udm.security_result.severity` to `ERROR` when `event_level` raw log field is `ERROR`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `type`, `completion_status`, `name`, `owner`, `assigned_scope`, `assigned_scope_path`, `stack`, `launched`, `progress`, `percent_complete`, `expiration`, `verified`, `definition`, `schedule`, `pending_signoffs`, `signoff`, `report`, `target_class`, `target_id`, `target_name`, `task_terminated`, `partitioned`, `live`, `run_length`, `run_length_average`, `run_length_deviation`, `interface`, `account_name`, `instance`, `attribute_name`, `attribute_value`, `tracking_id`, `string1`, `string2`, `string3`, `string4`, `quick_key`, `classname`, `line_number`, `thread`, `stacktrace`, `message_data`, `target_data`, `modified`, `completed` and `data_value` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field if those values are not null.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped key-value pairs from XML within `attributes` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `has_principal` is `true` and `has_target` is `true` and `action` is `login`.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when `has_principal` is `true` and `has_target` is `true` and `action` is `logout`.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PASSWORD` when `has_principal` is `true` and `has_target` is `true` and XML attribute `operation` is `PasswordChange`.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_user` is true and prior conditions not met.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED` when `event.idm.read_only_udm.metadata.event_type` is `USER_LOGIN` or `USER_LOGOUT`.  
\- Added KV filter to parse new type of logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
2024-10-01 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
