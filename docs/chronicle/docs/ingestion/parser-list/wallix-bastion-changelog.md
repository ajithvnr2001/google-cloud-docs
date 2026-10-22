---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wallix-bastion-changelog/
title: Change log for WALLIX_BASTION \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:28.417896+00:00
---

# Change log for WALLIX_BASTION  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wallix-bastion-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WALLIX_BASTION

Date | Changes  
---|---  
2026-09-24 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `user` from `event.idm.read_only_udm.target.user.userid` UDM field as it represents principal user data.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Removed mapping of `infos` from `event.idm.read_only_udm.metadata.description` UDM field as it represents security_result data.  
\- `event.idm.read_only_udm.security_result.description`: Mapped `infos` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `object` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.last_name`: Newly mapped `sn_profile` raw log field with `event.idm.read_only_udm.target.user.last_name` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `email_address` and `emailAddress` raw log fields with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles.name`: Newly mapped `profile_name` raw log field with `event.idm.read_only_udm.target.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `UID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `method`, `O`, `groups_name`, `preferredLanguage`, `forceChangePwd`, `userauths`, `isDisabled`, `gpgFingerprint`, `new_profile`, `old_profile`, `syslog_priority`, `cn_profile`, `CN`, `auth_with`, `identified_with` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped `method` value with `event.idm.read_only_udm.extensions.auth.mechanism` when `method` is `OTP`.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `metadata_product_name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `auth_status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `USER_LOGIN` value with `event.idm.read_only_udm.metadata.event_type` UDM field when type is `UserAuth`, `AUTHENTICATION_TRY`.  
\- Added a Grok pattern to parse the raw log fields.   
2026-04-13 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `partial_data`, `StartTime`, `EndTime`, `ReplicationSuccessCount`, `ReplicationSize_octets` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added and modified grok patterns to parse new format SYSLOG+KV and SYSLOG raw logs.  
\- Added a KV filter to extract fields from `partial_data` and `data`.  
\- Added a conditional check to validate if the value present in `partial_data` is a valid URL; otherwise, mapped `partial_data` to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `psid`,`vault`, `session`, `TTY`, `service`, `format`, `data`, `channel_name`, `RSA_SHA256` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `account`, `target_data` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `partial_data` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal_user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `USER`,`login` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `PWD` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `command_line`,`COMMAND` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `command_line_details` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `principal_process_file_name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.hostname`,`event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `device` raw log field with `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `service` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `size`,`length` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file_name` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.sha256`: Newly mapped `sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc`, `result` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `target_file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `principal_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip`: Newly mapped `host`,`target_ip_details` raw log field with `event.idm.read_only_udm.target.ip`,`event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `psid`, `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `event.idm.read_only_udm.extensions.auth.type` to `MACHINE`.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `summary_details` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional checks to set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when user login activity is detected and target user details are present. If `type` is `TARGET_CONNECTION` and target user details are present, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional checks to set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when user logout activity is detected and target user details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PASSWORD` when user password change activity is detected and target user details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `FILE_MODIFICATION` when `type` is `DRIVE_REDIRECTION_WRITE_EX`, principal machine data,target machine data and target file details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH` when `type` is `NEW_PROCESS`, principal machine data, target machine data and target process details are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_FTP` when `type` is `SFTP_EVENT`, principal machine data, target machine data are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when principal user details are present.  
\- Modified and added grok patterns to parse new format of SYSLOG+KV and SYSLOG the raw log fields.   
2025-04-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `hostname` from `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field   
2024-11-28 |  Enhancement:  
\- Added support to parse `metadata.event_timestamp` for all time zones.   
2024-11-20 |  Enhancement:  
\- Added a Grok pattern to extract the date and to properly map its value to `metadata.event_timestamp`.   
2024-10-29 |  Enhancement:  
\- Added support for new log patterns.   
2024-06-28 |  New:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
