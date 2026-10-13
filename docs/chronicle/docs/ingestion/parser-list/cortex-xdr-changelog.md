---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cortex-xdr-changelog/
title: Change log for CORTEX_XDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:28:57.177622+00:00
---

# Change log for CORTEX_XDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cortex-xdr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CORTEX_XDR

Date | Changes  
---|---  
2026-08-12 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Modified `user_name` raw log field to remove numeric and domain prefixes before mapping to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `domain_part` raw log field to `event.idm.read_only_udm.target.administrative_domain` UDM field.   
2026-08-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dst_action_country` raw log field to `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `original_alert_json.raw_abioc.event.action_network_protocol` raw log field to `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `original_alert_json.raw_abioc.event.agent_external_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `original_alert_json.raw_abioc.event.action_session_duration` raw log field to `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- Added additional checks for raw log fields (`original_alert`, `endPointHeader`, and `messageData`) and port fields (`action_local_port`, `action_remote_port`, `sourceTranslatedPort`, `destinationTranslatedPort`, `spt`) before mapping to their corresponding UDM fields.   
2026-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_deployment_id`: Newly mapped `external_id` raw log field to `event.idm.read_only_udm.metadata.product_deployment_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped combination of `alert_source` and `alert_name` raw log fields to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `case_id` and `internal_id` raw log fields to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `eventtime` and `creation_time` raw log fields to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `last_issue_ts` and `source_insert_ts` raw log fields to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.ingested_timestamp`: Newly mapped ingestion insert timestamp raw log field to `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Added conditional logic to set `metadata_event_type` to `SCAN_PROCESS` when `principal_device` is present, `has_target_process` is true, and `alert_source` is non-empty.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `agent_id` raw log field with `Cortex XDR:` prefix to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.principal.hostname`: Newly mapped `agent_hostname` raw log field to `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.principal.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip`: Newly mapped `agent_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` and `event.idm.read_only_udm.principal.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `ast.asset_id` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.domain.name`: Newly mapped `agent_fqdn` raw log field to `event.idm.read_only_udm.principal.domain.name` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `ast.asset_region` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Mapped raw log platform values to `LINUX` or `MAC` in `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor_eff_username` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `actor_process_command_line` raw log field to `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `actor_process_image_path` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `actor_process_image_name` raw log field to `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `actor_process_image_sha256` raw log field to `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `actor_process_image_md5` raw log field to `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `actor_process_os_pid` raw log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.product_specific_process_id`: Newly mapped `actor_process_causality_id` raw log field with `cor:` prefix to `event.idm.read_only_udm.principal.process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `causality_actor_process_command_line` raw log field to `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `causality_actor_process_image_path` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Newly mapped `causality_actor_process_image_name` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha256`: Newly mapped `causality_actor_process_image_sha256` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.md5`: Newly mapped `causality_actor_process_image_md5` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `causality_actor_process_os_pid` raw log field to `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.product_specific_process_id`: Newly mapped `causality_actor_process_instance_id` raw log field with `cor:` prefix to `event.idm.read_only_udm.principal.process.parent_process.product_specific_process_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `cntid` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Set `event.idm.read_only_udm.principal.resource.resource_subtype` to `CONTAINER` when `cntid` is present.  
\- `event.idm.read_only_udm.principal.resource_ancestors`: Newly mapped `resource_ancestors` raw log field to `event.idm.read_only_udm.principal.resource_ancestors` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `action_process_image_path` raw log field to `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.md5`: Newly mapped `action_process_image_md5` raw log field to `event.idm.read_only_udm.target.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `action_process_os_pid` raw log field to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped action raw log field (`ALLOW`, `BLOCK`, `QUARANTINE`) to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.alert_state`: Set `event.idm.read_only_udm.security_result.alert_state` UDM field to `ALERTING`.  
\- `event.idm.read_only_udm.security_result.category` and `event.idm.read_only_udm.security_result.category_details`: Newly mapped `alert_category` raw log field to `category_details` and set `category` to `SOFTWARE_MALICIOUS`.  
\- `event.idm.read_only_udm.security_result.confidence_details`: Newly mapped `associationstrengthvalue` raw log field to `event.idm.read_only_udm.security_result.confidence_details` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_name` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped raw log severity values (`LOW`, `MEDIUM`, `HIGH`, `CRITICAL`, `INFORMATIONAL`) to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `alert_description` and `leading_issue_description` raw log fields to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped raw log `endPointHeader` fields (`accountId`, `addresses`, `agentIp`, `agentIpList`, `agentLocation`, `agentTime`, `agentVersion`, `cloudLabels`, `cloudProvider`, `cloudRegion`, `cloudResourceId`, `contentVersion`, `dataCollectionStatus`, `deviceDomain`, `deviceName`, `endpointTags`, `essentialSecurityModeEnabled`, `fileRetrievalEnabled`, `fileSearchEnabled`, `is64`, `isolationStatus`, `isVdi`, `linuxKernelVersion`, `linuxOperationMode`, `liveTerminalEnabled`, `mac`, `manualProtectionPause`, `osType`, `osVersion`, `policyTag`, `policyYamlVersion`, `protectionStatus`, `productType`, `scriptExecutionEnabled`, `securityStatus`, `tzOffset`, `vaContainerScanEnabled`), `contains_featured_host`, `contains_featured_user`, `contains_featured_ip`, `original_alert_json.messageData.trapsSeverity`, `original_alert_json.messageData.yaraDetails` to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped raw log alert, process, container, and case metadata fields (`actor_process_execution_time`, `actor_thread_thread_id`, `assignee`, `assignee_pretty`, `asset_account`, `asset_name`, `container_id`, `cloud_security_agent_capable`, `cloud_security_agent_mode`, `dispatch_state`, `exported`, `feedBased`, `alert_is_fp`, `hasRole`, `issue_count`, `manual_score`, `messageData` (`cystatusDescription`, `eventCategory`, `moduleId`, `moduleStatusId`, `policyId`, `preventionKey`, `preventionMode`, `profile`), `Users`, `module_id`, `module_name`, `original_alert` (`agentId`, `customerId`, `generatedTime`, `isEndpoint`, `originalAgentTime`, `recordType`, `serverTime`), `retained`, `rule_based_score`, `is_rule_triggering`, `scortex`, `status_progress`, `is_xsoar_alert`) to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped raw log fields (`case_genesis_time`, `cloud_labels`, `container_name`, `deduplicate_tokens`, `family_tag_name`, `container_image_id`, `container_image`, `last_update_time`, `source_uuid`, `original_severity`, `resolve_comment`, `resolve_reason`, `resolved_ts`, `tag_id`, `tag_name`) to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `variation_rule_id` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics`: Newly mapped `mitre_tactic_id_and_name` raw log field to `event.idm.read_only_udm.security_result.attack_details.tactics` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `mitre_technique_id_and_name` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques` UDM field.  
\- `event.idm.read_only_udm.intermediary.process.file.names`: Newly mapped `actor_process_image_name` raw log field elements to `event.idm.read_only_udm.intermediary.process.file.names` UDM field when `actor_process_image_name` is an array.  
\- `event.idm.read_only_udm.src.process.file.names`: Newly mapped `os_actor_process_image_name` raw log field elements to `event.idm.read_only_udm.src.process.file.names` UDM field when `os_actor_process_image_name` is an array.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `causality_actor_process_image_name` raw log field elements to `event.idm.read_only_udm.principal.process.file.names` UDM field when `causality_actor_process_image_name` is an array.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `association_strength` raw log field elements to `event.idm.read_only_udm.additional.fields` UDM field when `association_strength` is an array.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cloud_provider`, `event_timestamp`, `action_process_signature_status`, `action_process_signature_vendor`, `action_process_causality_id`, `action_process_image_command_line`, `action_process_image_name`, `action_process_image_sha256`, `action_process_instance_id`, `actor_process_signature_status`, `actor_process_image_sha256`, `actor_process_signature_vendor`, `actor_thread_thread_id`, `actor_process_causality_id`, `actor_process_image_md5`, `actor_process_os_pid`, `actor_process_image_path`, `actor_process_command_line`, `agent_host_boot_time`, `actor_causality_id`, `event_id`, `event_sub_type`, `os_actor_process_instance_id`, `os_actor_process_causality_id`, `os_actor_process_image_path`, `os_actor_process_os_pid`, `os_actor_process_command_line`, `os_actor_process_image_sha256`, `os_actor_process_signature_status`, `os_actor_thread_thread_id`, `os_actor_process_signature_vendor`, `causality_actor_causality_id`, `causality_actor_process_command_line`, `causality_actor_process_execution_time`, `causality_actor_process_image_path`, `causality_actor_process_image_md5`, `causality_actor_process_image_sha256`, `causality_actor_process_signature_status`, `causality_actor_process_signature_vendor`, `event_type`, `user_name`, `action_country` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-08 |  Enhancement:  
\- Shifted mapping for `host_name` to global level.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped host_name raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `action_process_signature_vendor` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `actor_process_instance_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `actor_process_signature_status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `os_actor_process_instance_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert_domain` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_sub_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dst_association_strength` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `bioc_indicator` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-07-28 |  Enhancement:  
\- Added a grok pattern to parse `principal.ip`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: newly mapped `ip1` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: newly mapped `ip2` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Removed mapping of `domain` from `event.idm.read_only_udm.target.hostname` UDM field because, it is more appropriate to map `principal`.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `domain` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- STATUS_UPDATE: Support for this event has been added when ip1, ip2 and domain are all not null.   
2025-06-02 |  Enhancement:  
\- Added a gsub to replace `\\r\\n`, `\\n` with ` ` and `\\*\\*` with "" on message.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `deviceFacility` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `end` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `external_id` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `fs1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `fs2` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.process.file.names: Newly mapped `targetprocessname` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- event.idm.read_only_udm.target.process.command_line: Newly mapped `targetprocesscmd` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `targetprocesssignature` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.process.file.sha256: Newly mapped `targetprocesssha256` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.   
2025-04-17 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.file.names`:Removed mapping of `action_file_name` from `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Mapped `action_file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.   
2025-04-16 |  Bug-Fix:  
\- Modified the comparator from `==` to `=~` for mapping the `action_external_hostname` raw log field to the `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields."   
2025-04-10 |  Enhancement:  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Removed mapping of `action_remote_ip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field when `action_remote_ip` is equal to `dst_agent_id`.   
2025-03-18 |  Enhancement:  
\- Removed the mapping for `action_file_path` from `target.resource.attribute.labels`.  
\- Changed mapping of `action_file_path` from `target.resource.attribute.labels` to `target.file.full_path`.  
\- Removed the mapping for `action_file_name` from `target.file.full_path`.  
\- Changed mapping of `action_file_name` from `target.file.full_path` to `target.process.file.names`.   
2025-02-24 |  Enhancement:  
\- Changed `agent_os_sub_type` mapping from `target.platform_version` to `principal.platform_version`.  
\- Changed `agent_os_type` mapping from `target.platform` to `principal.platform`.   
2025-02-13 |  Enhancement:  
\- Removed `host_ip` mapping from `principal.ip`.   
2025-02-11 |  Enhancement:  
\- Mapped `AUDIT_SEVERITY` to `security_result.severity_details`.  
\- When `AUDIT_SEVERITY` is nearly equal to `LOW`, then set `security_result.severity` to `LOW`.   
2025-02-04 |  Enhancement:  
\- Added support for audit events logs.   
2024-12-30 |  Enhancement:  
\- Changed mapping of `action_local_ip` from `target.ip` to `principal.ip`.   
2024-12-19 |  Bug-fix:  
\- Changed mapping of `tags` from `security_result.rule_name` to `security_result.rule_labels`.  
\- Changed mapping of `source` from `principal.asset.attribute.labels` to `security_result.rule_type`.   
2024-11-18 |  Enhancement:  
\- Mapped `event_name` to `security_result.description`.  
\- Mapped `shost` to `principal.ip` and `principal.asset.ip`.   
2024-08-20 |  Enhancement:  
\- Mapped `user_name` to `target.user.userid`.   
2024-08-19 |  Enhancement:  
\- Mapped `actor_process_os_pid` to `target.process.pid`.  
\- Changed mapping of `alert_id` from `security_result.rule_id` to `security_result.detection_fields`.  
\- Changed mapping of `endpoint_id` from `target.process.product_specific_process_id` to `principal.asset.asset_id`.  
\- Added support to parse new format of unparsed JSON logs.   
2024-07-02 |  Enhancement:  
\- Mapped `external_id` to `metadata.product_log_id`.  
\- Mapped `action_pretty` to `security_result.action_details`.   
2024-06-17 |  Enhancement:  
\- When `severity` is less than or equal to 6, then set `security_result.severity` to `LOW`.  
\- when `severity` is greater than 6 and less than or equal to 8, then set `security_result.severity` to `MEDIUM`.  
\- When `severity` is greater than 8, then set `security_result.severity` to `HIGH`.  
\- Mapped `action` to `security_result.action_details`.  
\- Mapped `original_tags` to `additional.fields`.   
2024-04-17 |  Enhancement:  
\- Mapped `action_local_port` to `principal.port`.  
\- Mapped `dst_agent_id` to `principal.ip`.  
\- Mapped `action_remote_ip` to `target.ip`.  
\- Mapped `action_remote_port` to `target.ip`.  
\- Added check if `target_device` is preset prior setting `metadata.event_type` to `NETWORK_CONNECTION`.   
2024-03-15 |  Enhancement:  
\- Added a Grok to retrieve `source` and `sr_summary` from the message header.  
\- Mapped `sr_summary` to `security_result.summary`  
2024-03-11 |  Enhancement:  
\- Added support for CEF format logs.  
\- Mapped `rt` to `metadata.event_timestamp`.  
\- Mapped `category` and `cat` to `security_result.category_details`.  
\- Mapped `cs2Label`, `cs2`, `tenantname`, `tenantCDLid` and `CSPaccountname` to `additional.fields`.  
\- Mapped `shost` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `spt` to `principal.port`.  
\- Mapped `src` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `suser` to `principal.user.user_display_name`.  
\- Mapped `dpt` to `target.port`.  
\- Mapped `dst` to `target.ip` and `target.asset.ip`.  
\- Mapped `fileHash` to `target.file.sha256`.  
\- Mapped `filePath` to `target.file.full_path`.  
\- Mapped `request` to `network.http.referral_url`.  
\- Mapped `msg` to `security_result.description`.   
2024-01-18 |  Enhancement:  
\- Changed `action_file_path` mapping from `target.file.full_path` to `target.resource.attribute.labels`.  
\- Mapped `domain` to `target.asset.hostname`.  
\- Mapped `destinationTranslatedAddress` to `target.asset.ip`.  
\- Mapped `host_name` to `principal.asset.hostname`.  
\- Mapped `dvchost` to `principal.asset.hostname`.  
\- Mapped `ip` to `principal.asset.ip`.  
\- Mapped `sourceTranslatedAddress` to `principal.asset.ip`.   
2023-11-10 |  Enhancement:  
\- When `event_type` is `RPC Call`, then mapped `metadata.event_type` to `STATUS_UPDATE`.  
\- Mapped `events.action_country` to `security_result.about.location.country_or_region`.  
\- Mapped `events.actor_process_command_line` to `target.process.command_line`.  
\- Mapped `events.actor_process_image_md5` to `target.file.md5`.  
\- Mapped `events.actor_process_image_path` to `target.file.full_path`.  
\- Mapped `events.actor_process_image_sha256` to `target.file.sha256`.  
\- Mapped `events.actor_process_instance_id` to `target.process.pid`.  
\- Mapped `events.os_actor_process_command_line` to `principal.process.command_line`.  
\- Mapped `events.os_actor_process_image_path` to `principal.file.full_path`.  
\- Mapped `events.os_actor_process_image_sha256` to `principal.file.sha256`.  
\- Mapped `events.os_actor_process_instance_id` to `principal.process.pid`.  
\- Mapped `events.causality_actor_process_command_line` to `intermediary.process.command_line`.  
\- Mapped `events.causality_actor_process_image_path` to `intermediary.file.full_path`.  
\- Mapped `events.causality_actor_process_image_sha256` to `intermediary.file.sha256`.  
\- Mapped `events.causality_actor_process_instance_id` to `intermediary.process.pid`.  
\- Mapped `events.causality_actor_process_image_md5` to `intermediary.file.md5`.  
\- Mapped `events.event_type` to `metadata.product_event_type`.  
\- Mapped `events.user_name` to `principal.user.user_display_name`.   
2023-10-16 |  Enhancement:  
\- Mapped `source` to `principal.asset.attribute.labels`.  
\- Set `metadata.event_type` to `NETWORK_CONNECTION` if `event_type` in `Network Connections` or `Network Event`.   
2022-11-03 |  Enhancement:  
\- Mapped `PanOSConfigVersion` to `security_result.detection_fields`.  
\- Mapped `PanOSContentVersion` to `security_result.detection_fields`.  
\- Mapped `PanOSDGHierarchyLevel1` to `security_result.detection_fields`.  
\- Mapped `PanOSDestinationLocation` to `target.location.country_or_region`.  
\- Mapped `PanOSDynamicUserGroupName` to `principal.group.group_display_name`.  
\- Mapped `PanOSSourceLocation` to `principal.location.country_or_region`.  
\- Mapped `PanOSThreatCategory` to `security_result.category_details`.  
\- Mapped `PanOSThreatID` to `security_result.threat_id`.  
\- Mapped `app` to `target.application`.  
\- Mapped `cs1` to `additional.fields`.  
\- Mapped `cs3` to `additional.fields`.  
\- Mapped `cs4` to `additional.fields`.  
\- Mapped `cs5` to `additional.fields`.  
\- Mapped `cs6` to `additional.fields`.  
\- Mapped `cn1` to `additional.fields`.  
\- Mapped `sourceTranslatedPort` to `principal.port`.  
\- Mapped `sourceTranslatedAddress` to `principal.ip`.  
\- Mapped `destinationTranslatedAddress` to `target.ip`.  
\- Mapped `destinationTranslatedPort` to `target.port`.  
\- Mapped `act` to `security_result.action_details`.  
\- Mapped `deviceExternalId` to `security_result.about.asset_id`.  
\- Mapped `dvchost` to `principal.hostname`.  
\- Mapped `proto` to `network.ip_protocol`.  
\- Mapped `fileId` to `target.resource.attribute.labels`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
