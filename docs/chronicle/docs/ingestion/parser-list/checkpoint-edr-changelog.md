---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-edr-changelog/
title: Change log for CHECKPOINT_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:11:00.443265+00:00
---

# Change log for CHECKPOINT_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/checkpoint-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CHECKPOINT_EDR

Date | Changes  
---|---  
2026-08-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `administrator` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `endpointname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.observer.asset.product_object_id`: Newly mapped `orig_log_server` raw log field with `event.idm.read_only_udm.observer.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `orig_log_server_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `product_family`, `type`, `domain_name`, `sequencenum`, `trimTime`, `trimHour`, `trimDate`, `hourOfDay`, `dedup_time`, `__id`, `syslog_program`, `syslog_pid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `orig` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `appi_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `matched_category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `policy_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `policy_number` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process_exe_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `resource` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2026-04-14 |  Enhancement  
\- Added a Grok pattern on `fieldschanges` to extract the `Icon`, `Name`, `ExclusionName`, `id`, `program_file` and `auth` raw log fields.  
\- Added a Grok pattern on `logic_changes` to extract the `guid1`, `guid2`, `guid3`, `guid4`, `exclusionName1`, `exclusionName2`, `exclusionName3`, `exclusionName4`, `Icon`, `Name` raw log fields.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal and target data is present and `operation` is `Create Object` then setting `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_CREATION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal and target data is present and `operation` is `Log Out` then setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT`.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal and target data is present and `operation` is `Log In` then setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `administrator` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `objectname` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `objecttype`, `Name`, `guid1`, `guid2`, `guid3`, `guid4`, `exclusionName1`, `exclusionName4` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.security_result_action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result_action` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_uid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `loguid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `origin` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `ifdir` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Icon`, `flags`, `originsicname`, `sequencenum`, `advanced_changes`, `sendtotrackerasadvancedauditlog`, `additional_info` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `ExclusionName` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.resource.product_object_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.about.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `program_file` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.security_result.about.url`: Newly mapped `exclusionName2` raw log field with `event.idm.read_only_udm.security_result.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.full_path`: Newly mapped `exclusionName3` raw log field with `event.idm.read_only_udm.security_result.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.url`: Newly mapped `auth` raw log field with `event.idm.read_only_udm.about.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2025-09-12 |  \- Enhancement  
\- event.idm.read_only_udm.additional.fields: Newly mapped am_update_source, client_name, connectivity_state, engine_ver, failed_updates, flags, installed_products, local_time, originsicname, policy_date, policy_type, policy_version, product_family, sequencenum, sig_ver, tenant_id, uid, version, virtual_groups, am_update_proxy raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped subject raw log field(s) with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped event_type, operation raw log field(s) with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped loguid raw log field(s) with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped product raw log field(s) with event.idm.read_only_udm.metadata.product_name UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped client_version raw log field(s) with event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped ifdir raw log field(s) with event.idm.read_only_udm.network.direction UDM field.  
\- event.idm.read_only_udm.observer.ip: Newly mapped origin raw log field(s) with event.idm.read_only_udm.observer.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped endpointname, src_machine_name raw log field(s) with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped src raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped os_version raw log field(s) with event.idm.read_only_udm.principal.asset.platform_software.platform_version UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped endpointname, src_machine_name raw log field(s) with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped src raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped policy_name raw log field(s) with event.idm.read_only_udm.principal.resource.name UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped policy_guid raw log field(s) with event.idm.read_only_udm.principal.resource.product_object_id UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped user_name raw log field(s) with event.idm.read_only_udm.principal.user.email_addresses UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped src_user_name raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped user_sid raw log field(s) with event.idm.read_only_udm.principal.user.windows_sid UDM field.  
\- event.idm.read_only_udm.security_result: Newly mapped security_result raw log field(s) with event.idm.read_only_udm.security_result UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped action_details raw log field(s) with event.idm.read_only_udm.security_result.action_details UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped policy_number raw log field(s) with event.idm.read_only_udm.security_result.rule_id UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped audit_status raw log field(s) with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped machine_guid raw log field(s) with event.idm.read_only_udm.principal.asset.product_object_id UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped description raw log field(s) with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.security_result.action_comment: Newly mapped action_comment raw log field(s) with event.idm.read_only_udm.security_result.action_comment UDM field.  
\- Added conditional check for event_type to process Policy Update and Update events.  
\- Added conditional check for operation to process Access Key For Encryptor events.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: If os_name contains WINDOWS, updated to WINDOWS.  
\- event.idm.read_only_udm.principal.asset.type: If host_type is Desktop, updated to WORKSTATION.  
\- event.idm.read_only_udm.principal.asset.type: If host_type is Laptop, updated to LAPTOP.  
\- event.idm.read_only_udm.security_result.action: If action is Drop, updated to BLOCK.  
\- event.idm.read_only_udm.security_result.action: If result is Finished, updated to ALLOW.  
\- event.idm.read_only_udm.security_result.severity: If severity is 1 or 0, updated to LOW.  
\- event.idm.read_only_udm.metadata.event_type: If event_type is Policy Update or Update, updated to STATUS_UPDATE.  
\- event.idm.read_only_udm.metadata.event_type: If operation is Access Key For Encryptor and the has_principal flag is true, updated to STATUS_UPDATE.   
2025-07-15 |  Enhancement  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `src_machine_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `src_user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `user_sid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `src`, and `origin` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `process_exe_path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `resource` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `appi_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `matched_category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `policy_name` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped `policy_number` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `action` raw log field with `event.idm.read_  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `protection_name`, and `protection_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `loguid`, `sequencenum`, `policy_date`, `usercheck_incident_uid`, `tenant_id`, `exclusion_engine_type`, `exclusion_type` and `virtual_groups` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `client_name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `client_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `os_name` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped `os_version` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.principal.asset.software: Newly mapped `installed_products` raw log field with `event.idm.read_only_udm.principal.asset.software` UDM field.  
\- event.idm.read_only_udm.network.direction: Set `event.idm.read_only_udm.network.direction` to `INBOUND` if `ifdir` raw log field is `Inbound` else if `ifdir` raw log field is `Outbound` set to `OUTBOUND`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.   
2024-05-09 |  Enhancement- Parsed logs with `event_type` as `empty`.  
\- Added support for the MEPP, Compliance, Anti-Malware, and Threat Emulation  
logs.   
2022-09-07 |  Enhancement- Parsed logs with event_type as `empty`.  
\- mapped `client_ip` to `event.edr.network.target_ip`.  
\- mapped `origin` to `event.edr.network.target_ip` if client_ip empty.  
\- mapped `subject` to `event.edr.task.task_name`.  
\- mapped `host_name` to `event.edr.client.hostname`.  
\- mapped `ifdir` to `event.edr.network.direction`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
