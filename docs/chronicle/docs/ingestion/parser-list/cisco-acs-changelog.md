---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-acs-changelog/
title: Change log for CISCO_ACS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:56.895950+00:00
---

# Change log for CISCO_ACS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-acs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ACS

Date | Changes  
---|---  
2026-08-28 |   
2026-08-21 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `kv.UserName` from `event.idm.read_only_udm.target.user.userid` UDM field when `log_type` is `CSCOacs_Passed_Authentications` as the field represents principal user information.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `kv.UserName` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field when `log_type` is `CSCOacs_Passed_Authentications`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `kv.E-Mail` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `kv.Real Name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `kv.Port` raw log field to `event.idm.read_only_udm.target.resource.name` when `kv.Port` is not an integer.   
2026-06-18 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `NAS-Identifier`, `cribl_pipe`, `event_data.created`, `_time`, `@timestamp`, `organization.name`, `organization.id` and `kafkaTopic` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `AcsSessionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field when `audit_session_id` field is not present.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `@version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field when `product_version` field is not present.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `NAS-IP-Address` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field for all events.   
2026-05-07 |  Enhancement:  
\- Modified a grok pattern to parse the new raw logs.  
\- Added support for the event `CisACS_02_FailedAuth` and relevant corresponding raw log fields.  
\- Added support for the event `CisACS_05_TACACSAdmin` and relevant corresponding raw log fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as this is a syslog header it should be mapped to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields if the `hostname` is an IP address.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `kv.NAS-IP-Address` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `kv.source_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.target.asset.hostname`: Mapped `kv.NetworkDeviceName` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field  
\- `event.idm.read_only_udm.target.asset.ip`: Mapped `kv.Remote-Address` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `kv.DeviceIPAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `kv.AD-IP-Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `kv.Framed-IP-Address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `kv.Caller-Id` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `kv.Group-Name` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `kv.Session ID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `kv.FailureReason`, `kv.IdentityPolicyMatchedRule` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `kv.ServiceSelectionMatchedRule` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `kv.cmd` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `kv.Network Device Group`, `kv.Access Device`, `kv.Priv-lvl`, `kv.Network Access Profile Name`, `kv.Authen-Failure-Code`, `kv.Message-Type`, `kv.Privilege-Level`, `kv.Authen-Type`, `kv.Service`, `kv.Port`, `kv.NAS-Portname`, `kv.service`, `kv.priv-lvl`, `kv.task_id`, `kv.Acct-Flags`, `kv.Acct-Method`, `kv.Acct-Type`, `kv.Acct-Service`, `kv.timezone`, `kv.AAA Server`, `kv.start_time`, `steps`, `kv.NetworkDeviceGroups` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- If target machine data is present AND network dns data is present, set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS`.  
\- If `log_type` is `CSCOacs_Passed_Authentications` OR `CSCOacs_Failed_Attempts` AND target machine AND target user data is present, set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- If principal machine AND target machine data is present, set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `log_type` is CSCOacs_System_Statistics and principal machine data is present, set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UNCATEGORIZED`.  
\- If principal machine data is present, set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- If user data is present, set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Else, set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2024-11-14 |  Enhancement:  
\- Added support to parse unparsed logs.   
2023-09-26 |  Enhancement -  
\- Initialized `hostname` to null and added a hostname not null check prior setting `metadata.event_type` to `STATUS_UPDATE`.  
\- Added a valid IP address check to `kv.DeviceIPAddress`, `kv.Remote-Address` prior to mapping to UDM fields.   
2022-08-19 |  Enhancement -  
-Mapped `User-Name` to `principal.user.userid`.  
-Renamed ip:source-ip` to `source_ip` and Mapped it to `principal.ip".  
-Renamed `kv.audit-session-id` to `kv.audit_session_id` and Mapped it to `network.session_id`.  
-Mapped `kv.AuthenticationMethod` to `additional.fields`.  
-Mapped `kv.SelectedAccessService` to `additional.fields`.  
-Mapped `kv.SelectedAuthorizationProfiles` to `security_result.detection_fields`.  
-Mapped `kv.SelectedAuthenticationIdentityStores` to `security_result.detection_fields`.  
-Mapped `kv.device-uid-global` to `principal.asset.product_object_id`.  
-Mapped `kv.device-uid` to `principal.asset.asset_id`.  
-Mapped `metadata.event_type` to `USER_UNCATEGORIZED` where kv.DestinationIPAddress and kv.NAS-IP-Address and kv.NAS-IP-Address and kv.UserName and kv.NetworkDeviceName is null.  
-Added support for logs with LEEF format.   
2022-06-14 |  Enhancement - Modified grok to parse logs of log_type = `CSCOacs_Passed_Authentications` which were failing due to multiple spaces.  
\- Replaced the value of `device-mac` with the dummy value of `00:00:00:00:00:00` for logtype `CSCOacs_RADIUS_Accounting` in case of invalid value (00).   
2022-06-06 |  Enhancement - Parsed logs of type `CSCOacs_Passed_Authentications` that doesn't have either of `DestinationIPAddress` or `NAS-IP-Address` present in the logs.  
\- Modified metadata.event_type from `USER_UNCATEGORIZED` to `USER_LOGIN` for logs of type `CSCOacs_Passed_Authentications`  
2022-05-05 |  Enhancement - The newly ingested logs which do not have message code are parsed and dropped.   
2022-04-27 |  Enhancement - Parsed the logs with log_type=CISE_TACACS_Accounting.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
