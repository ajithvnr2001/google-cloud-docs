---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-edr-changelog/
title: Change log for SYMANTEC_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:07.138406+00:00
---

# Change log for SYMANTEC_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_EDR

Date | Changes  
---|---  
2026-06-11 |  \- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `symcSEDRUUID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `symcSEDRLogName` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `device_domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `user_domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `event_actor.file.md5` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `event_actor.file.sha2` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `event_actor.file.path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `event_actor.user.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `event_actor.user.sid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.id`: Newly mapped `event_actor.uid` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `event_actor.cmd_line` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `event_actor.pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `enriched_data.rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `enriched_data.category_name` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `connection.url.path`, `connection.url.query`, `connection.uid`, `ref_uid`, `event_actor.file.signature_level_id`, `edr_files` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_actor.xattributes.symc_injected`, `event_actor.xattributes.is_trusted`, `enriched_data.suspicion_score`, `enriched_data.rule_description`, `enriched_data.category_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `rt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When `has_target` is `true` and `has_principal` is `true` or `principal_machine_id_present` is `true` and `target_machine_id_present` is `true` and `app_protocol_src` is `HTTP`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` and When `has_target` is `true` and `has_principal` is `true` or `principal_machine_id_present` is `true` and `target_machine_id_present` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`and when `has_principal` is `true` or `principal_machine_id_present` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2026-02-26 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `device_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field, now supporting `UNIX_MS` and `ISO8601` formats.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `log_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field, supporting `UNIX_MS` and `ISO8601` formats.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: If `type_id` does not match any known type, Set the value of `event.idm.read_only_udm.target.user.userid` to the value of `user_name`.  
\- `event.idm.read_only_udm.target.resource.name`:  
\- If `type_id` does not match any known type, set the value of `event.idm.read_only_udm.target.resource.name` to the value of `resource`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity_id` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `risk_ref_value` raw log field with `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `attacks.technique_uid` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `attacks.technique_uid` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `event_actor.file.normalized_path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `event_actor.file.name` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `user_sid` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `event_actor.file.signature_company_name` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `event_actor.app_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_actor.integrity_id` (key: `event_actor_integrity_id`), `event_actor.signature_level_id` (key: `event_actor_signature_level_id`), `event_actor.start_time` (key: `event_actor_start_time`), `event_actor.file.modified` (key: `event_actor_file_modified`), `operation` (key: `operation`), `event_actor.file.signature_value_ids` (key: `signature_value_id_0`), `event_actor.file.signature_value_ids` (key: `signature_value_id_1`), `analysis` (key: `analysis`), `amsi_data` (key: `amsi_data`), `log_name` (key: `log_name`), `scan_uid` (key: `scan_uid`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `enriched_data.category_id` (key: `category_id`) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_user` is `true` and `metadata_event_type` is "" or `GENERIC_EVENT`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- Added a conditional check before already existing mapping of `target_file_full_path` to `event.idm.read_only_udm.target.file.full_path`.  
\- `event.idm.read_only_udm.metadata.description`: Modified the condition for ensuring only the inner `message` raw log field is being mapped to `event.idm.read_only_udm.metadata.description` UDM field.  
\- Removed an unnecessary drop statement due to which the following UDM fields are now being mapped:  
\- event.idm.read_only_udm.metadata.collected_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.collected_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.administrative_domain`  
\- `event.idm.read_only_udm.principal.asset.asset_id`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.asset_id`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.platform_version`  
\- `event.idm.read_only_udm.principal.process.command_line`  
\- `event.idm.read_only_udm.principal.process.file.md5`  
\- `event.idm.read_only_udm.principal.process.file.sha256`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.principal.resource.id`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.threat_name`  
\- `event.idm.read_only_udm.target.administrative_domain`  
\- `event.idm.read_only_udm.target.file.size`  
\- `event.idm.read_only_udm.target.registry.registry_key`  
\- `event.idm.read_only_udm.target.registry.registry_value_name`  
2025-04-18 |  \- Added a Grok pattern to parse the json format of logs.  
\- event.idm.read_only_udm.metadata.event_timestamp:Newly mapped `device_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `ref_incident_uid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `type_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `incident_uid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `remediation` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `priority_id` raw log field with `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `logging_device_name` raw log field with `event.idm.read_only_udm.principal.hostname` and "event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `logging_device_ip` raw log field into `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `detection_type` raw log field into `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- Added `has_principal` flag for `internalIP`,`device_ip`,`internalHost` raw log fields.  
\- Added `has_target` flag for `external_ip`,`user_agent_ip`,`device_uid` raw log field.  
\- Added `has_target` and `has_principal` flags as a conditional check before mapping `NETWORK`CONNECTION" event_type.  
\- Added `has_principal` flag as a conditional check before mapping `STATUS_UPDATE` event_type.  
\- Added ([logging_device_name] == "`) and ([logging_device_ip] == ``) as a conditional check before mapping `GENERIC_EVENT" event_type.  
\- Added `on_error` check for `event_actor.pid`,`log_time`,`asset_id` raw log fields.  
\- Added a separate mutate block for `internalHost`,`event_actor.pid`,`event_actor.file.path`,`type_id`,`product_name`,`product_ver`,`uuid`,`message` raw log fields.  
\- Added a conditional check before mapping `message` raw log field to `event.idm.read_only_udm.metadata.description` UDM fields.  
\- Added a separate mutate block for `device_name`,`device_ip` raw log field ,replacing `rename` with `replace`.  
\- Replacing `rename` with `replace` for `device_name` raw log field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `device_uid` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `incident` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `event_actor_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `event_actor_uid` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `event_actor_cmd_line` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.process.file.md5: Newly mapped `event_actor_file.md5` raw log field with `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `event_actor_file.sha2` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `event_actor_file.path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `enriched_data_rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only.udm.security_result.detection_fields: Newly mapped `enriched_data_suspicion_score` raw log field with `event.idm.read_only.udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only.udm.security_result.category_details: Newly mapped `enriched_data_category_name` raw log field with `event.idm.read_only.udm.security_result.category_details` UDM field.  
\- event.idm.read_only.udm.security_result.detection_fields: Newly mapped `enriched_data_rule_description` raw log field with `event.idm.read_only.udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only.udm.additional.fields: Newly mapped `ref_uid` raw log field with `event.idm.read_only.udm.additional.fields` UDM field.  
\- event.idm.read_only.udm.additional.fields: Newly mapped `correlation_uid` raw log field with `event.idm.read_only.udm.additional.fields` UDM field.  
\- event.idm.read_only.udm.additional.fields: Newly mapped `ref_orig_uid` raw log field with `event.idm.read_only.udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `user_domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- Added `has_target` flag for `asset_id` raw log field.  
\- Added a separate mutate block for `principal_hostname`,`target_hostname` raw log field, replacing `rename` with `replace`.  
\- Added a separate mutate block for `principal_ip`,`target_ip` raw log field.   
2022-03-31 |  \- Added Device Id prefix to asset details.  
\- Added CEF parsing support.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
