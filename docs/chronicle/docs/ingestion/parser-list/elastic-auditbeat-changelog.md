---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-auditbeat-changelog/
title: Change log for ELASTIC_AUDITBEAT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:46.523214+00:00
---

# Change log for ELASTIC_AUDITBEAT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/elastic-auditbeat-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ELASTIC_AUDITBEAT

Date | Changes  
---|---  
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `process.parent.process.title` raw log field with `event.idm.read_only_udm.principal.process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `process.parent.process.executable` raw log field with `event.idm.read_only_udm.principal.process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.parent_process.file.full_path`: Newly mapped `process.parent.process.parent.process.executable` raw log field with `event.idm.read_only_udm.principal.process.parent_process.parent_process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.parent_process.command_line`: Newly mapped `process.parent.process.parent.process.title` raw log field with `event.idm.read_only_udm.principal.process.parent_process.parent_process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `process.title` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `auditd.data.socket.addr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `auditd.data.reason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `auditd.data.terminal` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `auditd.summary.object.secondary`, `auditd.data.addr` and `auditd.data.hostname` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auditd.summary.object.secondary`, `auditd.paths`, `auditd.data`, `auditd.summary.actor`, `auditd.summary.object`, `container.labels`, `container`, `user.selinux`, `environment`, `process.args`, `process.parent.process.args`, `process.parent.process.parent.process.args`, `auditd.msg_type`, `auditd.summary.how`, `event1.kind`, `event1.module`, `user.effective.group.id`, `user.effective.group.name`, `user.filesystem.group.id`, `user.filesystem.group.name`, `user.filesystem.id`, `user.filesystem.name`, `user.group.id`, `user.group.name`, `user.saved.group.id`, `user.saved.group.name`, `user.saved.id`, `user.saved.name`, `container.image.name`, `process.parent.process.parent.process.start_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `process.parent.pid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.parent_process.pid`: Newly mapped `process.parent.process.parent.pid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.parent_process.parent_process.parent_process.pid`: Newly mapped `process.parent.process.parent.process.parent.pid` raw log field with `event.idm.read_only_udm.principal.process.parent_process.parent_process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `auditd.result` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `auditd.result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `auditd.sequence` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `file.name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `file`, `auditd.data.socket` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `host_os_platform`, `host.os`, `host.containerized`, `process.parent.process.name`, `process.parent.process.parent.process.name`, `process.parent.process.parent.process.owner.id`, `process.parent.process.parent.process.owner.name`, `process.working_directory` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `agent.name` raw log field with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional logic for `USER_LOGIN`, `USER_LOGOUT`, `SERVICE_START` and `SERVICE_STOP` event types.   
2024-12-10 |  Enhancement:  
\- Added support for new pattern of syslog format.   
2024-07-31 |  Enhancement:  
\- Mapped `file.owner`, `file.uid`, `file.drive_letter`, `file.type`, `file.inode`, `file.ctime`, and `file.mtime` to `target.resource.attribute.labels`.  
\- Mapped `event.dataset` and `event.type` to `additional.fields`.   
2024-06-26 |  Enhancement:  
\- Added `gsub` to replace `\\r\\n` and `\\n` with "" from the message.   
2024-06-13 |  Enhancement:  
\- If the value of `message_not_json` is `true`, added Grok patterns to support SYSLOG + JSON.  
\- If the value of `host_os_platform` is similar to `debian` or `linux`, then set `principal.platform` as `LINUX`.  
\- If the value of `host_os_platform` is similar to `mac` or `ios`, then set `principal.platform` as `MAC`.  
\- If the value of `host_os_platform` is similar to `windows`, then set `principal.platform` as `WINDOWS`.  
\- If the value of `audit_data_sycall` is null, then mapped `type` to `metadata.product_event_type`.  
\- Mapped `tag` to `security_result.category_details`.  
\- Mapped `agent_ephemeral_id` and `ts` to `additional.fields`.  
\- Mapped `os_name`, `os_build`, and `env` to `principal.resource.attribute.labels`.   
2023-09-04 |  Enhancement -  
\- Mapped `auditd.data.syscal` field to `metadata.product_event_type`.   
2023-03-03 |  Enhancement -  
\- Replaced `-` with `:` in `host.mac` prior mapping to UDM with correct MAC address format.  
\- Mapped `cloud.region` to `principal.cloud.availability_zone`.  
\- Mapped `VIRTUAL_MACHINE` to `principal.resource.resource_type` where `cloud.service.name` has `Virtual Machine`.  
\- Mapped `cloud.machine.type` to `principal.resource.resource_subtype`.  
\- Mapped `cloud.instance.id` to `principal.resource.id`.   
2022-07-08 |  Enhancement -  
\- Added on_error for @timestamp field in date filter.  
\- Changed event_type from GENERIC_EVENT to USER_UNCATEGORIZED where target.user is not null.  
\- Changed event_type from GENERIC_EVENT to PROCESS_UNCATEGORIZED where target.process is not null.  
\- Changed event_type from GENERIC_EVENT to STATUS_UPDATE where principal.ip not null or principal.hostname not null.  
\- Added auth.type to AUTHTYPE_UNSPECIFIED where event_type is USER_LOGIN or USER_LOGOUT.  
\- Mapped httpRequest.serverIp to principal.ip.  
\- Mapped httpRequest.remoteIp to target.ip.  
\- Mapped httpRequest.requestSize to network.sent_bytes.  
\- Mapped httpRequest.responseSize to network.received_bytes.  
\- Mapped httpRequest.requestUrl to network.http.referral_url.  
\- Mapped httpRequest.requestMethod to network.http.method.  
\- Mapped httpRequest.status to network.http.response_code.  
\- Mapped resource.labels.backend_service_name to target.resource.name.  
\- Mapped resource.labels.project_id to target.resource.product_object_id.  
\- Mapped resource.labels.target_proxy_name to target.resource.attribute.labels.  
\- Mapped resource.labels.url_map_name to target.resource.attribute.labels.  
\- Mapped trace to target.process.file.full_path.   
2022-05-31 |  Enhancement- Mapped `jsonPayload.process.parent.process.pid` to `principal.process.pid`.  
Mapped `jsonPayload.process.parent.process.exe` to `principal.process.file.full_path`.  
Mapped `jsonPayload.destination.ip` to `target.ip`.  
Mapped `jsonPayload.destination.port` to `target.port`.  
Mapped `jsonPayload.network.direction` to `network.direction`.  
Added on_error statement to avoid failures if the key is not present in the log.  
Applied condition to check for presence of mandatory fields as listed below before mapping the relevant event_type. If these fields are not present, then event_type is set as GENERIC_EVENT.  
\- `jsonPayload.host.hostname` is mandatory for event_type `NETWORK_CONNECTION`  
\- `jsonPayload.host.id` is mandatory for event_type `PROCESS_OPEN`  
2022-05-23 |  Enhancement- Mapped required attribute values to process.command_line.   
2022-05-07 |  Enhancement- Added support for parsing `jsonPayload`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
