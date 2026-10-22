---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-tacacs-changelog/
title: Change log for CISCO_TACACS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:48.368715+00:00
---

# Change log for CISCO_TACACS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-tacacs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_TACACS

Date | Changes  
---|---  
2026-06-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `r_ip_or_host` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field as it contains the intermediary related ip.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `r_ip_or_host` with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `r_cat_name` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `r_msg_id` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when a cmd is present and both machine and user data are present for either the principal or the target.   
2026-01-29 |  Enhancement:  
\- Added new grok pattern to parse new log format.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `common_username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `common_service` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `tacacs_remote_address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `tacacs_acct_session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `common_nas_ip_address` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tacacs_privilege_level`, `tacacs_acct_flags`, `tacacs_auth_source`, `tacacs_authen_method`, `tacacs_authen_service`, `tacacs_authen_type`, `tacacs_enforcement_profiles`, `tacacs_request_type`, `tacacs_session_log_timestamp`, `common_request_timestamp`, `tacacs_acct_timestamp`, `tacacs_authen_action` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is true, updated to `STATUS_UPDATE`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal_user` is true, updated to `USER_UNCATEGORIZED`.   
2024-11-07 |  Enhancement:  
\- Added support to handle SYSLOG+KV logs.   
2024-09-19 |  Enhancement:  
\- Added support for new log format.   
2022-08-09 |  Bug fix -  
-Modified mapping for the field `Networkdevicename` from `prinicipal.asset.hostname` to `intermediary.hostname`.   
2022-03-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
