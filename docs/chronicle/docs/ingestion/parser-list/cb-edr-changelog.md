---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-edr-changelog/
title: Change log for CB_EDR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:22:28.638561+00:00
---

# Change log for CB_EDR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-edr-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CB_EDR

Date | Changes  
---|---  
2025-12-18 |  Enhancement:  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `childproc_name` raw log field to `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `ttps` raw log field to `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.security_result.atatck_details.tactics.id: Newly mapped `attack_tactic` raw log field to `event.idm.read_only_udm.security_result.atatck_details.tactics.id` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.pid: Newly mapped `parent_pid` raw log field to `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.file.sha256: Newly mapped `parent_sha256` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.command_line: Newly mapped `parent_cmdline` raw log field to `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `childproc_effective_reputation` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `childproc_username` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.   
2025-11-21 |  Enhancement:  
\- `event.idm.read_only_udm.target.process.file.full_path`: Removed mapping of `process_name` from `event.idm.read_only_udm.target.process.file.full_path` UDM field since it is principal process.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `parent_name` from `event.idm.read_only_udm.additional.fields` UDM field in order to map it to the appropriate UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `parent_name` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `childproc_sha256` raw log field to `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `report_tags` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `childproc_cmdline` raw log field to `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `childproc_name` raw log field to `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Mapped `process_name` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- Enhanced parsing of the `ioc_hit` field to extract and map `parent_name` and `childproc_name`.  
\- Added logic to map `parent_name` from the `docs` array elements.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH` if `type` is `PROCESS_LAUNCH`.   
2025-11-10 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `process_username`, `parent_username`, and `determination.change_timestamp` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `workflow.change_timestamp`, `detection_timestamp`, `last_event_timestamp`, `process_issuer`, `process_publisher`, `process_effective_reputation`, `parent_effective_reputation`, and `parent_reputation` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `backend_timestamp` and `backend_update_timestamp` raw log fields with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `report_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `parent_pid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.md5`: Newly mapped `parent_md5` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.sha256`: Newly mapped `parent_sha256` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `parent_cmdline` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.sha256`: Newly mapped `process_sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- updated the condition for `sensor_action` to include `ALLOW` to set `sec_action` to `ALLOW`.   
2025-09-10 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `org_key` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `workflow.changed_by`, `primary_event_id`, `workflow.closure_reason`, `workflow.changed_by_type`, `alert_origin`, `device_username`, `vendor_name`, `product_name`, raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `tags`, `run_state`, `workflow.status`, `alert_notes_present`, `threat_notes_present`, `is_updated`, `device_policy_id`, `mdr_alert`, `mdr_alert_notes_present`, `mdr_threat_notes_present`, `determination.changed_by`, `determination.changed_by_type`, `determination.value`, `reason_code` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `device_uem_id`, `device_target_value`, `asset_group` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `device_policy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.location.name`: Newly mapped `device_location` raw log field with `event.idm.read_only_udm.principal.asset.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `device_os_version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `vendor_id`, `product_id`, `serial_number` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `external_device_friendly_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `first_event_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `policy_applied` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `device_internal_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `threat_id` raw log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2025-06-23 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.alert_state: Set `event.idm.read_only_udm.security_result.alert_state` UDM field to `ALERTING` if `workflow.status` raw log field is equal to `OPEN` or `IN_PROGRESS`.  
\- event.idm.read_only_udm.security_result.alert_state: Set `event.idm.read_only_udm.security_result.alert_state` UDM field to `NOT_ALERTING` if `workflow.status` raw log field is equal to `CLOSED`.   
2025-05-02 |  Enhancement:  
\- Added new Grok patterns to parse new format of SYSLOG logs.  
\- Added gsub function to remove ` (\\\w+?)=` and `'` from `message" field.  
\- Added a null conditional check when mapping `group` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- Added a null conditional check when mapping `comms_ip` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `type` is `alert.watchlist.hit.ingress.process`, `feed.query.hit.process` and `feed.storage.hit.process`.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `feed_id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `interface_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip, event.idm.read_only_udm.additional.fields: Added mapping for `comms_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field when is different of interface_ip, otherwise mapped to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `reason` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `segment_id`, `index_type`, `search_query`, `start_time`, and `last_update` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `watchlist_id` raw log fields with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `watchlist_name` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `group` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.target.resource.id: Newly mapped `report_id` and watchlist_id raw log fields with `event.idm.read_only_udm.target.resource.id` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `report_id` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Newly mapped `process_sha256` raw log field with `event.idm.read_only_udm.principal.process.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alliance_data_attackframework` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alliance_updated_attackframework` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.confidence_score: Newly mapped `alliance_score_attackframework` raw log field with `event.idm.read_only_udm.security_result.confidence_score` UDM field.  
\- event.idm.read_only_udm.security_result.url_back_to_product: Newly mapped `alliance_link_attackframework` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `NETWORK_CONNECTION` if both principal and target are present.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `STATUS_UPDATE` if only principal is present.   
2025-04-10 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `comms_ip` from `event.idm.read_only_udm.intermediary.ip` UDM field when `comms_ip` is equal to `interface_ip`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `comms_ip` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when `comms_ip` is equal to `interface_ip`.   
2025-03-25 |  Enhancement:  
\- Mapped fully qualified value of `device_name` to `intermediary.hostname`, `intermediary.asset.hostname`, `principal.hostname` and `principal.asset.hostname`.  
\- Removed mapping for `device_internal_ip from `additional.fields".  
\- Mapped `device_internal_ip` to `intermediary.ip`, `intermediary.asset.ip`, `principal.ip` and `principal.asset.ip`.  
\- Removed mapping for `device_external_ip` from `principal.asset.ip` and `principal.ip`.  
\- Mapped `device_external_ip` to `principal.nat_ip`.   
2025-03-19 |  Bug-Fix:  
\- Added `on_error` to all the fields mapped from docs.*.  
\- Added additional check for `sha256` and `md5` to avoid parsing errors.  
\- Mapped `feed_name` to `principal.resource.name`.  
\- When `feed_name` is not null, then mapped `principal.resource.resource_subtype` to `Feed`.   
2024-07-02 |  Enhancement:  
\- Added `gsub` function to parse the unparsed fields.   
2024-05-13 |  Enhancement:  
\- Mapped `alert_url` field to `metadata.url_back_to_product` UDM field.   
2024-01-19 |  Enhancement:  
\- Added a null check for `filemod_hash.0` and `filemod_hash.1` before mapping.   
2023-12-27 |  Enhancement:  
\- Initialized `filemod_hash.0` and `filemod_hash.1` to null to parse the unparsed logs.   
2023-10-26 |  Enhancement:  
\- Added `gsub` function to parse the unparsed fields.   
2023-10-13 |  Enhancement:  
\- Handled new JSON logs by adding JSON block.  
\- Removed redundant code for fields `computer_name`, `parent_name`, `process_name`, `pid`, `process_path`, `md5`, `sha256`, `process_guid`, `parent_pid`, `docs.0.process_pid`, `cb_version`, `process_hash.0`, `process_hash.1`, `parent_hash.0` and `parent_hash.1`.   
2023-07-21 |  \- Added MITRE ATT&CK tactic and technique details to `security_result.attack_details`.   
2023-03-24 |  \- Mapped the field `protocol` to `network.ip_protocol`.  
\- Added null conditional check for the field `child_username`, `child_pid`, `child_command_line`.  
\- Changed the `metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` when `principal.hostname` or `principal.ip` is not null.   
2023-03-14 |  Bug-fix:  
\- Mapped the following fields when the field `type` is null:  
\- Mapped the field `process_guid` to `principal.process.product_specific_process_id`.  
\- Mapped the field `device_external_ip` to `target.ip`.  
\- Mapped the field `device_os` to `principal.platform`.  
\- Mapped the field `device_group` to `principal.group.group_display_name`.  
\- Mapped the field `process_pid` to `principal.process.pid`.  
\- Mapped the field `process_path` to `principal.process.file.full_path`.  
\- Mapped the field `process_cmdline` to `principal.process.command_line`.  
\- Mapped the field `process_hash.0` to `principal.process.file.md5`.  
\- Mapped the field `principal.1` to `principal.process.file.sha256`.  
\- Mapped the field `process_username` to `principal.user.userid`.  
\- Mapped the field `clientIp` to `principal.ip`.  
\- Mapped the field `description` to `metadata.description`.  
\- Mapped the field `orgName` to `principal.administrative_domain`.  
\- Mapped the following fields when the field `ruleName` contains `CYDERES`:  
\- Mapped the field `deviceInfo.internalIpAddress` to `principal.ip`.  
\- Mapped the field `deviceInfo.externalIpAddress` to `target.ip`.  
\- Mapped the field `ruleName` to `security_result.rule_name`.  
\- Mapped the field `deviceInfo.deviceType` to `principal.asset.platform_software.platform`.  
\- Mapped the field `domain` to `principal.administrative_domain`.  
\- Mapped the field `deviceInfo.groupName` to `principal.group.group_display_name`.  
\- Mapped the field `deviceInfo.deviceVersion` to `principal.asset.platform_software.platform_version`.  
\- Mapped the field `deviceInfo.deviceId` to `principal.asset.asset_id`.  
\- Mapped the field `eventId` to `additional.fields`.  
\- Changed the `metadata.event_type` from `GENERIC_EVENT` to `NETWORK_CONNECTION` when `principal.ip` and `target.ip` is not null.  
\- Changed the `metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` when `principal.ip` is not null.   
2023-02-03 |  Bug-fix:  
\- Map `filemod_hash` to `target.file` instead of `target.process.file`.   
2023-01-20 |  Bug-fix:  
\- Stopped populating and mapping product_specific_process_id for empty process ids.   
2022-11-25 |  \- Mapped `remote_ip` to `principal.ip` and `local_ip` to `target.ip` for `Inbound` TCP/UDP events.  
\- Mapped `remote_port` to `principal.port` and `local_port` to `target.port` for `Inbound` TCP/UDP events.   
2022-10-06 |  \- Migrated all customer specific parsers to default parser.   
2022-07-10 |  \- Updated mapping of `event_type` to `PROCESS_LAUNCH` for logs of type `endpoint.event.`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
