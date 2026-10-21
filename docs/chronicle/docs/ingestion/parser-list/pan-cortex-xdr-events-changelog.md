---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-cortex-xdr-events-changelog/
title: Change log for PAN_CORTEX_XDR_EVENTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:39:42.028426+00:00
---

# Change log for PAN_CORTEX_XDR_EVENTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-cortex-xdr-events-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_CORTEX_XDR_EVENTS

Date | Changes  
---|---  
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `action_user_session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `action_username` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Removed mapping of `agent_ip_addresses` from `event.idm.read_only_udm.observer.ip` UDM field because `agent_ip_addresses` is the IP address field associated with the agent and is a fundamental machine identifiers.  
\- `event.idm.read_only_udm.principal.ip`,`event.idm.read_only_udm.principal.asset.ip`: Mapped `agent_ip_addresses` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.platform_version`: Removed mapping of `agent_os_sub_type` from `event.idm.read_only_udm.target.platform_version` UDM field because `agent_os_sub_type` field provides specific details about the Operating System of the agent.  
\- `event.idm.read_only_udm.principal.platform_version`: Mapped `agent_os_sub_type` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `agent_id` from `event.idm.read_only_udm.additional.fields` UDM field because `agent_id` appears to be a unique identifier for the agent, similar to an asset ID.  
\- `event.idm.read_only_udm.principal.asset.asset_id`,`event.idm.read_only_udm.principal.asset_id`: Mapped `agent_id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` and `event.idm.read_only_udm.principal.asset_id` UDM fields.  
\- `event.idm.read_only_udm.principal.platform` : Newly mapped `agent_os_type` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `action_process_token` and `action_process_fds` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field as key value instead of parsing whole string.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `action_process_termination_date`,`action_process_termination_code`,`action_network_stats_is_last`,`action_user_is_local_session`,`action_user_status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.platform`: Removed mapping of `agent_os_sub_type` when it contains `WINDOWS` from `event.idm.read_only_udm.target.platform` UDM field as `agent_os_sub_type` field provides details about the Operating System of the agent,which should be principal.  
\- `event.idm.read_only_udm.principal.platform`: Mapped `agent_os_sub_type` when it contains `WINDOWS` with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: The event_type is updated to `PROCESS_LAUNCH`, `USER_LOGIN` or `USER_UNCATEGORIZED` based on the presence of necessary principal and target data, defaulting to GENERIC_EVENT if those details are missing.   
2025-09-24 |  Enhancement:  
\- Shifted mapping for action_process_image_path to global level.  
\- event.idm.read_only_udm.additional.fields newly mapped action_process_image_extension, action_process_signature_product, action_process_signature_is_embedded, action_process_integrity_level, action_process_pe_load_info.image_base, action_process_pe_load_info.image_size, action_process_pe_load_info.entry_point_rva, action_process_peb32, action_process_token, action_process_privileges, action_process_fds, uuid raw log field to event.idm.read_only_udm.additional.fields UDM field.   
2025-07-18 |  Enhancement:  
\- event.idm.read_only_udm.metadata.description: Newly mapped description raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped agent_version raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.principal.mac: Newly mapped mac raw log field to event.idm.read_only_udm.principal.mac.  
\- event.idm.read_only_udm.principal.platform: Newly mapped agent_os_type raw log field to event.idm.read_only_udm.principal.platform.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped agent_hostname raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped host_name raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped action_local_ip raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped host_ip raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped mac raw log field to event.idm.read_only_udm.principal.asset.mac.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped endpoint_id raw log field to event.idm.read_only_udm.principal.asset.asset_id.  
\- event.idm.read_only_udm.principal.asset.hardware: Newly mapped hardware raw log field to event.idm.read_only_udm.principal.asset.hardware.  
\- event.idm.read_only_udm.target.hostname: Newly mapped action_external_hostname raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped action_external_hostname raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped action_remote_ip raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped user_name raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped agent_device_domain raw log field to event.idm.read_only_udm.target.administrative_domain.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped dst_agent_id raw log field to event.idm.read_only_udm.target.user.product_object_id.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly mapped dst_action_country raw log field to event.idm.read_only_udm.target.location.country_or_region.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped cluster_name raw log field to event.idm.read_only_udm.target.resource.name.  
\- event.idm.read_only_udm.intermediary.process.file.sha256: Newly mapped actor_process_image_sha256 raw log field to event.idm.read_only_udm.intermediary.process.file.sha256.  
\- event.idm.read_only_udm.intermediary.process.product_specific_process_id: Newly mapped actor_process_causality_id raw log field to event.idm.read_only_udm.intermediary.process.product_specific_process_id.  
\- event.idm.read_only_udm.intermediary.process.file.names: Newly mapped actor_process_image_name raw log field to event.idm.read_only_udm.intermediary.process.file.names.  
\- event.idm.read_only_udm.intermediary.process.file.md5: Newly mapped actor_process_image_md5 raw log field to event.idm.read_only_udm.intermediary.process.file.md5.  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped actor_process_os_pid raw log field to event.idm.read_only_udm.intermediary.process.pid.  
\- event.idm.read_only_udm.intermediary.process.file.full_path: Newly mapped actor_process_image_path raw log field to event.idm.read_only_udm.intermediary.process.file.full_path.  
\- event.idm.read_only_udm.intermediary.process.command_line: Newly mapped actor_process_command_line raw log field to event.idm.read_only_udm.intermediary.process.command_line.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped user_agent raw log field to event.idm.read_only_udm.network.http.user_agent.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped user_agent raw log field to event.idm.read_only_udm.network.http.parsed_user_agent.  
\- event.idm.read_only_udm.network.session_id: Newly mapped action_network_connection_id raw log field to event.idm.read_only_udm.network.session_id.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped action_total_upload raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped action_total_download raw log field to event.idm.read_only_udm.network.received_bytes.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped ip_protocol_out raw log field to event.idm.read_only_udm.network.ip_protocol.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped fw_email_subject raw log field to event.idm.read_only_udm.network.email.subject.  
\- event.idm.read_only_udm.network.email.to: Newly mapped fw_email_recipient raw log field to event.idm.read_only_udm.network.email.to.  
\- event.idm.read_only_udm.network.email.from: Newly mapped fw_email_sender raw log field to event.idm.read_only_udm.network.email.from.  
\- event.idm.read_only_udm.security_result.about.location.country_or_region: Newly mapped action_country raw log field to event.idm.read_only_udm.security_result.about.location.country_or_region.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped name raw log field to event.idm.read_only_udm.security_result.threat_name.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped source raw log field to event.idm.read_only_udm.security_result.rule_type.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped fw_rule_id raw log field to event.idm.read_only_udm.security_result.rule_id.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped category raw log field to event.idm.read_only_udm.security_result.category_details.  
\- event.idm.read_only_udm.additional.fields: Newly mapped action_file_last_writer_actor, action_network_creation_time, action_file_access_time, action_file_create_time, action_file_mod_time, action_file_attributes, event_rpc_func_opnum, event_rpc_interface_uuid, action_socket_type. action_network_is_server, action_file_device_type, action_file_previous_file_name, action_file_name, agent_id, agent_version, agent_os_type, actor_thread_thread_id, action_file_type, action_file_prev_type, os_actor_process_logon_id, agent_content_version, detection_timestamp, events_length, local_insert_ts, matching_status, module_id raw log fields to event.idm.read_only_udm.additional.fields. These are added as key-value pairs.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped dst_action_external_hostname, dst_action_external_port, dns_query_name, dst_causality_actor_process_execution_time, dst_association_strength raw log fields to event.idm.read_only_udm.target.resource.attribute.labels. These are added as key-value pairs.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped action_process_signature_status, actor_process_signature_status, actor_process_signature_vendor, actor_process_image_name, actor_process_instance_id, agent_data_collection_status, agent_fqdn, agent_install_type, starred, causality_actor_process_signature_status, causality_actor_process_image_name, causality_actor_process_command_line, causality_actor_process_image_path, causality_actor_process_signature_vendor, causality_actor_causality_id, causality_actor_process_execution_time, causality_actor_process_image_md5, causality_actor_process_image_sha256, is_whitelisted, alert_id, agent_is_vdi, is_pcap, contains_featured_host, contains_featured_user, contains_featured_ip, action_process_instance_id, actor_causality_id, os_actor_effective_username, os_actor_process_image_name, os_actor_process_signature_vendor, os_actor_process_causality_id, os_actor_causality_id, os_actor_process_os_pid, tags, matching_service_rule_id, attempt_counter, bioc_category_enum_key, case_id, mitre_tactic_id_and_name, mitre_technique_id_and_name, action_local_ip_v6, action_remote_ip_v6, action_process_signature_vendor, action_file_macro_sha256, action_registry_full_key, external_id, fw_app_id, fw_interface_from, fw_interface_to, fw_rule, fw_url_domain, fw_app_subcategory, fw_app_category, fw_app_technology, fw_vsys, fw_xff, fw_misc, fw_is_phishing, end_match_attempt_ts, last_modified_ts, bioc_indicator, deduplicate_tokens, filter_rule_id, agent_host_boot_time, event_sub_type, association_strength, story_id, image_name, image_id, container_id, container_name, namespace, referenced_resource, operation_name, identity_sub_type, identity_type, project, cloud_provider, resource_type, resource_sub_type, alert_type, resolution_status, resolution_comment, dynamic_fields, malicious_urls, action_pretty, original_tags, event_version, agent_ip_addresses_v6 raw log fields to event.idm.read_only_udm.security_result.detection_fields. These are added as key-value pairs.  
\- Updated unloac to unload.  
\- Updated conditional check for `event_sub_type` to 9, 10 and 11 when `event_type` is `4`.   
2025-06-12 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `event_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `action_file_previous_file_path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `agent_interface_map.ipv4` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- event.idm.read_only_udm.observer.mac: Newly mapped `agent_interface_map.mac` raw log field with `event.idm.read_only_udm.observer.mac` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `action_file_last_writer_actor`, `action_file_device_type`, `action_file_previous_file_name`, `action_file_name`, `agent_id`, `agent_version`, `agent_os_type`, `os_actor_thread_thread_id`, `action_file_type`, `action_file_prev_type`, `os_actor_process_signature_status`, `os_actor_process_logon_id`, `agent_content_version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `action_module_image_size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field if `event_type` raw log field is equal to `6`.   
2025-05-15 |  Enhancement:  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `action_file_md5` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `action_file_sha256` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field   
2025-03-19 |  Enhancement:  
\- Mapped `action_module_md5` to `target.process.file.md5`.  
\- Mapped `action_module_sha256` to `target.process.file.sha256`.   
2023-12-15 |  Enhancement:  
\- Mapped `event_timestamp` to `metadata.event_timestamp`.  
\- When `event_type` is `5/6` and `action_remote_ip`, `action_local_ip`, `agent_hostname` are null, then mapped `metadata.event_type` to `GENERIC_EVENT.`  
2023-02-01 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
