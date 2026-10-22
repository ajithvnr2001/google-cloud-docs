---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-th-changelog/
title: Change log for TANIUM_TH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:03.500937+00:00
---

# Change log for TANIUM_TH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-th-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_TH

Date | Changes  
---|---  
2026-09-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `fields.record_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `fields.event_id` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `fields.event__ProcessId` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `fields.event__SubjectUserName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `fields.event__SubjectDomainName` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `fields.event__SubjectUserSid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `fields.event__ProcessName` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `fields.event__TargetUserName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `fields.event__TargetUserSid` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `fields.event__TargetDomainName` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `fields.event__IpAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `fields.event__IpPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `fields.event__WorkstationName` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `fields.event__LogonProcessName` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `fields.event__LogonGuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.name`: Newly mapped `fields.event__AuthenticationPackageName` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `fields.event__LogonType` raw log field with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `fields.event__SubjectLogonId`, `fields.event__TargetLogonId`, `fields.event__KeyLength`, `fields.event__RestrictedAdminMode`, `fields.event__TransmittedServices`, `fields.event__LmPackageName`, `fields.event__TargetLinkedLogonId`, `fields.event__TargetOutboundUserName`, `fields.event__TargetOutboundDomainName`, `fields.event__ImpersonationLevel`, `fields.event__ElevatedToken`, and `fields.event__VirtualAccount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `additional.event_id` is 4624, 4625, 4648, or 4627, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGIN.  
\- `event.idm.read_only_udm.extensions.auth.type`: If `additional.event_id` is 4624, 4625, 4648, or 4627, updated the value of `event.idm.read_only_udm.extensions.auth.type` to MACHINE.  
\- `event.idm.read_only_udm.security_result.action`: If `additional.event_id` is 4624, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW else if `additional.event_id` is 4625, 4648, or 4627, updated the value of `event.idm.read_only_udm.security_result.action` to BLOCK.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Added a conditional check before already existing mapping of `metadata.logType` to `event.idm.read_only_udm.metadata.product_event_type` when `tanium_event` is `security_event`.   
2026-08-03 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `tanium_computer_id` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM fields.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `fields.tanium_process_id` raw log field with `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `fields.dst_full_path` and `fields.full_path` raw log fields with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.src.file.full_path`: Newly mapped `fields.src_full_path` raw log field with `event.idm.read_only_udm.src.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `fields.process__pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `fields.process__file__full_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `fields.process__user__name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `fields.process__user__group` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.product_event_type`: Newly mapped `tanium_event` log field with `event.idm.read_only_udm.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_CREATION` when `tanium_event` is `file_create` and principal machine and target file are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_DELETION` when `tanium_event` is `file_delete` and principal machine and target file are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_MODIFICATION` when `tanium_event` is `file_write` and principal machine and target file are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `FILE_MOVE` when `tanium_event` is `file_move` and principal machine and target file and source file are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine is present.   
2023-12-18 |  Enhancement-  
\- Mapped `network.direction` JSON field to `network.direction` UDM field.   
2023-09-20 |  Enhancement-  
\- Mapped `metadata.description` JSON field to `metadata.description` UDM field.   
2022-12-12 |  Enhancement-  
\- Mapped `metadata.event_type` to `USER_LOGIN` when `additional.event_id` is `4625`, `4624`, `4648`, or `4627`.  
\- Mapped `metadata.event_type` to `USER_LOGOUT` when `additional.event_id` is `4634` or `4647`.  
\- Mapped `metadata.event_type` to `USER_CHANGE_PERMISSIONS` when `additional.event_id` is `4670`, `4672`, `4673`, `4674`, `4703`, `4704`, `4705`.  
\- Mapped `metadata.event_type` to `PROCESS_LAUNCH` when `additional.event_id` = `4688`.  
\- Mapped `metadata.event_type` to `PROCESS_TERMINATION` when `additional.event_id` = `4689`.  
\- Mapped `metadata.event_type` to `PROCESS_UNCATEGORIZED` when `additional.event_id` = `4799`.  
\- Mapped `metadata.event_type` to `SCHEDULED_TASK_MODIFICATION` when `additional.event_id` = `4702`.  
\- Mapped `metadata.event_type` to `SCHEDULED_TASK_DISABLE` when `additional.event_id` = `4701`.  
\- Mapped `metadata.event_type` to `SCHEDULED_TASK_ENABLE` when `additional.event_id` = `4700`.  
\- Mapped `metadata.event_type` to `SCHEDULED_TASK_DELETION` when `additional.event_id` = `4699`.  
\- Mapped `metadata.event_type` to `SCHEDULED_TASK_CREATION` when `additional.event_id` = `4698`.  
\- Modified `metadata.event_type` from `USER_UNCATEGORIZED` to `STATUS_UPDATE` for all other event types not handled specifically.   
2022-09-16 |  Enhancement-  
\- Added error check for `principal.process.file.fullPath`,`principal.process.file.md5`,`target.file.md5`.  
\- Set `event_type` to `STATUS_UPDATE` when field `logType` is equal to `PROCESS_MODULE_LOAD` and `target.file.md5` is null.   
2022-08-10 |  Enhancement-  
\- Modified mapping for the field `additional.event_id` from `metadata.product_log_id` to `security_result.rule_name`.  
\- Modified mapping for `metadata.event_type` from `GENERIC_EVENT` to `USER_LOGIN` where `additional.event_id` == `4625`.  
\- Modified mapping for `additional.event__AuthenticationPackageName` from `target.resource.name` to `security_result.about.resource.name` where `additional.event_id` == `4625`and `4624`.  
\- Mapped the field `additional.event__LogonType` to `extensions.auth.mechanism`.  
\- Mapped `security_result.category` to `AUTH_VIOLATION` where `additional.event_id` == `4625`.   
2022-06-01 |  Enhancement- For logs with logType `GENERIC_EVENT_LOG`, changed `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED`.  
Enhanced the parser to correct the parsing of the field `additional.query` so as to accordingly map it to target.ip or target.hostname based upon the value present in the log.   
2022-05-12 |  Bug-Fix  
\- Added condition check on field additional.query so as to map it to target.ip or target.hostname based upon the value present in the log.   
2022-03-30 |  Enhancement to map following raw logs elements to UDM elements:  
Mapped field `additional.event__TargetSid` and `additional.event__TargetUserSid` to `target.user.windows_sid`.  
Mapped field `additional.event__SubjectUserName` to `principal.user.user_display_name`.  
Mapped field `additional.event__CallerProcessId` and `additional.event__ClientProcessId` to `principal.process.pid`.  
Mapped field `additional.event__CallerProcessName` to `principal.process.file.full_path`.  
Mapped filed `additional.event__FQDN` to `principal.hostname`.  
Mapped field `additional.event__ParentProcessName` to `principal.process.parent_process.file.full_path`.  
Mapped field `additional.event__CommandLine` to `target.process.command_line`.  
Mapped field `additional.event__NewProcessId` to `target.process.pid`.  
Mapped field `additional.event__NewProcessName` to `target.process.file.full_path`.  
Mapped field `additional.event__ParentProcessId` to `principal.process.parent_process.pid`.  
Mapped field `additional.event__ObjectServer` to `security_result.category_details`.  
Mapped field `additional.event__Service` to `security_result.description`.  
Mapped field `additional.event__PrivilegeList` to `principal.user.attribute.permissions`.  
Mapped field `additional.event__TransmittedServices`, `additional.event__LmPackageName`, `additional.event__TokenElevationType`, `additional.event__MandatoryLabel`, `additional.event__AlgorithmName`, `additional.event__KeyName`, `additional.event__KeyType`, `additional.event__Operation`, `additional.event__ProviderName`, `additional.event__ReturnCode`, `additional.event__RpcCallClientLocality`, `additional.event__ClientProcessStartKey`, `additional.event__TaskContentNew`, `additional.event__TaskName`, `additional.event__Status`, `additional.event__FailureReason`, `additional.event__SubStatus`, `additional.event__KeyLength`, `additional.event__RestrictedAdminMode`, `additional.event__TargetLinkedLogonId`, `additional.event__TargetOutboundUserName`, `additional.event__TargetOutboundDomainName` to `additional.fields`.  
Changed mapping for `additional.event__VirtualAccount`, `additional.event__ElevatedToken`, `additional.event__ImpersonationLevel`, `additional.event__TargetLogonId`, `additional.event__SubjectLogonId` from `about.labels` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
