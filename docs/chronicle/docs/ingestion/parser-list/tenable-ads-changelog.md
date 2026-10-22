---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-ads-changelog/
title: Change log for TENABLE_ADS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:02.752694+00:00
---

# Change log for TENABLE_ADS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-ads-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TENABLE_ADS

Date | Changes  
---|---  
2026-03-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `PwdSprayingAccountNumberThreshold` , `TimeIntervalInMins` , and `GuidAttack` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `impacted_users` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `process_name` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Modified the filter for the `source_ip` raw log field to exclude localhost.  
\- Added a new json filter to parse `impacted_users` raw log field.  
\- Modified a grok pattern to parse the new log format, due to which the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.intermediary.asset.hostname`  
\- `event.idm.read_only_udm.intermediary.hostname`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.url_back_to_product`  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.principal.user.group_identifiers`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.target.user.group_identifiers`  
2026-03-09 |  Enhancement:  
\- Modified the logic to map multiple IPs from `dc_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `honey_account` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tool` (key: `tool`), `ntds_destination_path` (key: `ntds_destination_path`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified grok patterns to support new log patterns. Due to these changes, the following UDM fields are parsing correctly:  
\- `event.idm.read_only_udm.intermediary.asset.hostname`  
\- `event.idm.read_only_udm.intermediary.hostname`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.url_back_to_product`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.process.file.full_path`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.principal.user.group_identifiers`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.file.full_path`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.user.group_identifiers`  
\- `event.idm.read_only_udm.target.user.userid`  
2025-12-23 |  Enhancement:  
\- Added new grok pattern for `msg_1` to extract `alert_name`, `severity`, `src_ip`, and `kv_msg` raw log fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_image_name` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `shadow_copy_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `IOA_url` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.   
2025-12-12 |  Enhancement:  
A new grok pattern was added to parse `Account locked` events, which enables the extraction of the event description for log messages that include whenchanged.   
2025-11-20 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `AccountList`, `AccountSidList`, `PasswordHashPrefix`, `TenableReasonId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-18 |  Enhancement:  
\- event.idm.read_only_udm.about.user.userid: Newly mapped `CN` raw log field to event.idm.read_only_udm.about.user.userid.  
\- Changed mapping for `event.idm.read_only_udm.security_result.action`:  
\- Mapped to `FAIL` when the `meta_description` field is `Failed authentication` or `Failed auth reset`.  
\- Mapped to `BLOCK` when the `meta_description` field is `Account locked`.  
\- Added grok pattern to parse logs containing the `member` field, extracting user information.   
2025-10-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.hostname` UDM field. As this hostname value is from syslog header, it is appropriate to map it to `intermediary.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.asset.hostname` UDM field. As this hostname value is from syslog header, it is appropriate to map it to `intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `dn.CN` from `event.idm.read_only_udm.target.user.userid` UDM field. It is Common Name (CN) which is requested to be mapped to `principal.user.userid`,  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `dn.CN` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.metadata.event_type`: The logic for setting `event_type` has been entirely revised:  
\- If `has_principal` is `true` AND (`has_principal_user` is `true` OR `has_target_user` is `true`), `event_type` is set to `USER_LOGIN`. Additionally, `event.idm.read_only_udm.extensions.auth.type` is set to `AUTHTYPE_UNSPECIFIED` and `event.idm.read_only_udm.security_result.action` is set to `FAIL`.  
\- Else if `has_principal` is `true`, `event_type` is set to `STATUS_UPDATE`.  
\- Else if `has_principal_user` is `true` OR `has_target_user` is `true`, `event_type` is set to `USER_UNCATEGORIZED`.  
\- Otherwise, `event_type` defaults to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `domain` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-09 |  Enhancement:  
\- Added grok patterns to extract badpasswordtime and badpwdcount to identify failed authentication events.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped adObject raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `badpasswordtime`, `badpwdcount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `AUTHTYPE_UNSPECIFIED` constant value with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped FAIL constant value with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped adObject (from dn.CN) raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.department`: Newly mapped adObject (from dn.OU) raw log field with `event.idm.read_only_udm.target.user.department` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If badpwdcount or badpasswordtime is present, updated to USER_LOGIN.  
\- `event.idm.read_only_udm.metadata.event_type`: The condition to set event type to STATUS_UPDATE now requires badpasswordtime and badpwdcount to be empty.   
2025-09-04 |  Enhancement:  
\- event.idm.read_only_udm.principal.asset.hostname, event.idm.read_only_udm.principal.hostname**: Newly mapped `source_hostname` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip, event.idm.read_only_udm.principal.ip**: Newly mapped `source_ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname, event.idm.read_only_udm.target.hostname**: Newly mapped `dc_name` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` and `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.ip, event.idm.read_only_udm.target.ip**: Newly mapped `dc_ip` raw log field(s) with `event.idm.read_only_udm.target.asset.ip` and `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.user.userid**: Newly mapped `Cn` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname, event.idm.read_only_udm.intermediary.hostname**: Newly mapped `hostname` raw log field(s) with `event.idm.read_only_udm.intermediary.asset.hostname` and `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields**: Newly mapped `BadPwdCountThreshold` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary**: Newly mapped `alert_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.severity**: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- Renamed from `target` to `event.idm.read_only_udm.target`.  
\- Renamed from `intermediary` to `event.idm.read_only_udm.intermediary`.  
\- Added `grok` and `kv` filters to parse new log message formats.   
2025-07-25 |  Enhancement:  
\- Added Grok patterns to retrieve AccountCn, LimitMemberCount, PrivilegesPath, ParentContainer, GroupCn, GroupMemberCount.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped PID raw log field to event.idm.read_only_udm.principal.process.pid.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped eventId raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.metadata.description: Newly mapped meta_description raw log field to event.idm.read_only_udm.metadata.description.  
\- Renamed `messagetype` to `addition.messagetype`, `alertid` to `addition.alertid`, `tenable_codename` to `addition.tenable_codename`, `AD_Reason_Codename` to `addition.AD_Reason_Codename`, `expiry_date` to `addition.expiry_date`, `usnchanged` to `addition.usnchanged`, `AccountCn` to `addition.AccountCn`, `GroupCn` to `addition.GroupCn`, `LimitMemberCount` to `addition.LimitMemberCount`, `PrivilegesPath` to `addition.PrivilegesPath`, `ParentContainer` to `addition.ParentContainer`, `GroupMemberCount` to `addition.GroupMemberCount`, and `ComputerCn` to `addition.ComputerCn`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped messagetype, alertid, AccountCn, GroupCn, LimitMemberCount, PrivilegesPath, ParentContainer, GroupMemberCount and ComputerCn raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped tenable_codename, AD_Reason_Codename and expiry_date raw log fields to event.idm.read_only_udm.security_result.detection_fields.   
2025-07-02 |  Enhancement:  
\- Added a Grok pattern to parse dropping logs.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-01-23 |  Enhancement:  
\- Added support for new format of syslog logs.  
\- Mapped `adObject_1` and `adObject_2` to `principal.user.group_identifiers`.  
\- Added condition check and on_error when mapping `adObject` to `principal.user.group_identifiers`.  
\- Mapped `expiry_date` to `sec_results.detection_fields`.  
\- Mapped `last_login_time` to `principal.user.last_login_time`.  
\- Mapped `operating_system` to `principal.asset.platform_software.platform`.  
\- Mapped `operating_system_version` to `principal.asset.platform_software.platform_version`.   
2023-11-06 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
