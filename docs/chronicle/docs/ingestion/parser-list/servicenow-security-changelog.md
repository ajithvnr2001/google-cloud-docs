---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-security-changelog/
title: Change log for SERVICENOW_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:59.445038+00:00
---

# Change log for SERVICENOW_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/servicenow-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SERVICENOW_SECURITY

Date | Changes  
---|---  
2026-07-17 |  Enhancement:  
\- `event1.idm.read_only_udm.metadata.event_type`: If `event` is `Failed Login`, `SNC Login`, `Admin Login`, or `Impersonation` and `has_target_user` is `true`, updated the value of `event1.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`, else if `event` is `Security Elevation` and `has_target_user` is `true`, updated the value of `event1.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PERMISSIONS`, else if `has_principal_user` is `true` and `has_target_user` is `true`, updated the value of `event1.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`, else if `has_principal_ip` is `true`, updated the value of `event1.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- `event1.idm.read_only_udm.extensions.auth.type`: If `event` is `Failed Login`, `SNC Login`, `Admin Login`, or `Impersonation` and `has_target_user` is `true`, updated the value of `event1.idm.read_only_udm.extensions.auth.type` to `MACHINE`.  
\- `event1.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_address` raw log field with `event1.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added a conditional check before already existing mapping of `ip_address` to `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added a conditional check before already existing mapping of `snc_user`, `created_by`, `data_granted_by` to `event1.idm.read_only_udm.target.user.userid` UDM field.   
2026-04-30 |  Enhancement:  
\- `event1.idm.read_only_udm.metadata.event_timestamp`: Mapped `timestamp` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event1.idm.read_only_udm.metadata.product_log_id`: Mapped `data.sys_id` raw log field with `event1.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event1.idm.read_only_udm.metadata.description`: Mapped `data.message_data` raw log field with `event1.idm.read_only_udm.metadata.description` UDM field.  
\- `event1.idm.read_only_udm.principal.resource.name`: Mapped `data.source` raw log field with `event1.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event1.idm.read_only_udm.additional.fields`: Mapped `source` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- `event1.idm.read_only_udm.metadata.collected_timestamp`: Mapped `data.sys_created_on` raw log field with `event1.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event1.idm.read_only_udm.principal.user.userid`: Mapped `data.sys_created_by`, `data.user` raw log field with `event1.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event1.idm.read_only_udm.principal.namespace`: Mapped `source_instance` raw log field with `event1.idm.read_only_udm.principal.namespace` UDM field.  
\- `event1.idm.read_only_udm.target.resource.attribute.roles`: Mapped `data.role` raw log field with `event1.idm.read_only_udm.target.resource.attribute.roles` UDM field.  
\- `event1.idm.read_only_udm.target.user.userid`: Mapped `data.granted_by` raw log field with `event1.idm.read_only_udm.target.user.userid` UDM field.  
\- `event1.idm.read_only_udm.security_result.severity`: Mapped `data.level` raw log field with `event1.idm.read_only_udm.security_result.severity` UDM field.  
\- `event1.idm.read_only_udm.security_result.action_details`: Mapped `data.state` raw log field with `event1.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event1.idm.read_only_udm.metadata.event_type`: Updated the condition to set `event1.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `principal user` data is present else mapped to `GENERIC_EVENT`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
