---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nutanix-prism-changelog/
title: Change log for NUTANIX_PRISM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:36.937075+00:00
---

# Change log for NUTANIX_PRISM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nutanix-prism-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NUTANIX_PRISM

Date | Changes  
---|---  
2025-12-30 |  Enhancement:  
\- Added a grok patterns to parse the new log formats.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `header_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `thread_name`, `line_number`, `vdisk_id`, `pam_module`, `pam_submodule` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `snapshot_chain_id`, `partition_id`, `block_number`, `transaction_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `replica_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `pam_target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `pam_principal_uid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `pam_message` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.   
2025-12-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `princ_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vblocks`, `nutanix_scan_keys`, `curr_range_idx`, `creation_time_usecs`, `total_rpcs_done`, `total_rpc_time_usecs`, `last_rpc_time_usecs`, `total_rows_read`, `total_data_read_bytes`, `num_rpcs_before_stateful_scans_got_enabled`, `total_deserialization_time_usecs`, `prefetch_hits`, `total_scan_time`, `unprocessed_data_size`, `processed_data_size`, `prefetch_in_progress`, `deserialization_in_progress`, `prefetch_stopped`, `prefetch_error`, `done_callback_set`, `is_arena_enabled`, `use_chakrdb_backend`, `source_file` raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- Added conditional check for `agent.type`.  
\- Added conditional check for `agent.version`.  
\- Added new timestamp formats yyyy-MM-ddTHH:mm:ss.SSSSSSZ and RFC3339.   
2024-02-21 |  Enhancement:  
\- When `inner_message` is not empty and `not_json` is `true`, then set `audit_log` to `true` to support dropped JSON logs.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- When `network_set` is `false`, `has_principal` is `true`, `has_target` is `false` and `audit_log` is `false`, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- When `network_set` is `true`, `has_principal` is `true`, `has_target` is `false` and `audit_log` is `false`, then set `metadata.event_type` to `GENERIC_EVENT`.   
2024-01-12 |  Enhancement:  
\- Added support for new format of syslog logs.  
\- Added a null conditional check before mapping `logstash.ingest.host` to `intermediary.hostname`.  
\- Added a null conditional check before mapping `logstash.process.host` to `intermediary.hostname`.  
\- Added a null conditional check before mapping `logstash.collect.host` to `observer.ip`.   
2023-12-23 |  Enhancement:  
\- Added support for new type of AUDIT logs.  
\- Added new Grok patterns to parse SYSLOG+JSON logs.  
\- Mapped `affectedEntityList` and `alertUid` to `security_result.detection_fields`.  
\- Mapped `clientIp` and `params.requested_ip_address` to `principal.ip`.  
\- Mapped `defaultMsg` to `metadata.description`.  
\- Mapped `operationType` to `metadata.product_event_type`.  
\- Mapped `originatingClusterUuid` and `sessionId` to `additional.fields`.  
\- Mapped `params.mac_address` to `principal.mac`.  
\- Mapped `uuid` to `metadata.product_log_id`.  
\- Mapped `userName` to `principal.user.user_display_name`.  
\- Mapped `params.vm_name` to `target.resource.name`.   
2023-01-23 |  Enhancement:  
\- Mapped `logstash.ingest.host` to `intermediary[0].hostname` instead of `observer.hostname`.  
\- Mapped `logstash.collect.host` to `observer.ip`.  
\- Added null check for `logstash.ingest.host`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
