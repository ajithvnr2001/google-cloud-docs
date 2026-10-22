---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/h3c-switch-changelog/
title: Change log for H3C_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:46.020868+00:00
---

# Change log for H3C_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/h3c-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for H3C_SWITCH

Date | Changes  
---|---  
2026-01-23 |  Enhancement:  
\- Added a grok pattern to parse the log format.  
\- `event.idm.read_only_udm.observer.asset_id`: Newly mapped `observer_asset_id` raw log field with `event.idm.read_only_udm.observer.asset_id` UDM field.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `observer_hostname` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severityName` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `duplicate_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `facilityName`, `id`, `interface`, `host`, `device_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dev_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `program` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result`: Newly mapped `security_result` raw log field with `event.idm.read_only_udm.security_result` UDM field.   
2025-10-17 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `product_event_type` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dest_ip` raw log field(s) with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dest_ip` raw log field(s) with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `interface`, `ld_rd`, `status`, `diag`, `sess_type`, `link_type` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If desc contains `logged out` or `failed` and has_target_user is not `true`, updated to GENERIC_EVENT.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Changed static value from `H3C Switch` to `HPE`.  
\- `event.idm.read_only_udm.metadata.product_name`: Changed static value from `H3C Switch` to `Switch`.  
\- Updated conditional logic for tar_user to add a regex-based length validation.   
2025-06-05 |  Enhancement:  
\- Added a new Grok patterns to parse new pattern of SYSLOG logs.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.intermediary.ip: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.metadata.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.metadata.intermediary.asset.ip: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.metadata.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Line`, `OperateType`, `OperateTime`, `OperateState`, `OperateEndTime`, `EventIndex`, `CommandSource`, `ConfigSource`, `ConfigDestination` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `IPAddr` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `IPAddr` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `User` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `prin_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `tar_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `tar_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `tar_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `tar_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.event_type:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `has_target_user` is `true` and `logged in` is present in `desc`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` if `has_target_user` is `true` and `logged out` is present in `desc`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` if `has_target` is `true` and `has_principal` is `true`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if `has_target_user` is `true` and `has_principal_user` is `true`.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if `has_principal` is `true`.   
2025-02-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
