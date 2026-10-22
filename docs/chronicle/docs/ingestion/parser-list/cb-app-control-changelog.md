---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-app-control-changelog/
title: Change log for CB_APP_CONTROL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:27.485373+00:00
---

# Change log for CB_APP_CONTROL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cb-app-control-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CB_APP_CONTROL

Date | Changes  
---|---  
2025-08-28 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `fname` and `FileName` from event.idm.read_only_udm.additional.fields. (Inappropriate mapping)  
\- event.idm.read_only_udm.principal.process.file.names: mapped fname and FileName raw log field with event.idm.read_only_udm.principal.process.file.names UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Removed mapping of filePath from event.idm.read_only_udm.principal.process.file.names UDM field. (Inappropriate mapping)  
\- event.idm.read_only_udm.principal.file.full_path: mapped filePath raw log field with event.idm.read_only_udm.principal.file.full_path UDM field.   
2025-08-14 |  Enhancement:  
\- To enhance the mapping, remove the UDM mapping from `about` and reassign it to `principal.`  
\- event.idm.read_only_udm.about.process.command_line: Removed mapping of deviceProcessName from event.idm.read_only_udm.about.process.command_line UDM field.  
\- event.idm.read_only_udm.principal.process.parent_process.command_line: Mapped deviceProcessName log field to event.idm.read_only_udm.principal.process.parent_process.command_line UDM field.  
\- event.idm.read_only_udm.about.file.full_path: Removed mapping of filePath from event.idm.read_only_udm.about.file.full_path UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Mapped filePath log field to event.idm.read_only_udm.principal.process.file.names UDM field.  
\- event.idm.read_only_udm.about.file.sha256: Removed mapping of fileHash from event.idm.read_only_udm.about.file.sha256 UDM field.  
\- event.idm.read_only_udm.principal.process.file.sha256: Mapped fileHash log field to event.idm.read_only_udm.principal.process.file.sha256 UDM field.  
\- Transfered ap_app_udm_mapping_json.include code to conf file.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields.  
\- If `principal_userid` is not empty, then set event.idm.read_only_udm.metadata.event_type to SYSTEM_AUDIT_LOG_UNCATEGORIZED and set event.idm.read_only_udm.principal.user.userid to the value of `principal_userid`.  
\- Else if `has_target_user` is true and `has_principal` is true, then set event.idm.read_only_udm.metadata.event_type to USER_LOGIN and set event.idm.read_only_udm.extensions.auth.type to AUTHTYPE_UNSPECIFIED.  
\- Else if `has_principal` is true and `has_target` is true, then set event.idm.read_only_udm.metadata.event_type to NETWORK_CONNECTION.  
\- Else if `has_principal` is true, then set event.idm.read_only_udm.metadata.event_type to STATUS_UPDATE.  
\- Else (if none of the above conditions are met), then set event.idm.read_only_udm.metadata.event_type to GENERIC_EVENT.   
2025-06-17 |  Enhancement:  
\- Modified a conditional mapping for the `log_source` field. Added a grok pattern to identify IP addresses. When an IP is found, it is mapped to `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`.Otherwise, Added a grok pattern to identify hostnames. When a hostname is found, it is mapped to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`. Otherwise, the existing mapping to `event.idm.read_only_udm.security_result.about.labels` is used.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `process` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.   
2025-05-21 |  Enhancement  
\- `log_format`: Added `grok` support for `syslog` format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `syslog_priority` log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type_data` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `log_source` log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `text` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `type` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `subtype` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `date` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.process.file.names: Newly mapped `file_name` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- event.idm.read_only_udm.target.file.sha256: Newly mapped `file_hash` raw log field with `event.idm.read_only_udm.target.file.sha256` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `policy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `server_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `file_trust` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- event.idm.read_only_udm.security_result.about.labels: Newly mapped `file_threat` raw log field with `event.idm.read_only_udm.security_result.about.labels` UDM field.  
\- Modified conditional logic for JSON messages if `message` =~ `^{` are processed by `json` filter and then processed by `cb_app_udm_mapping_json.include`.  
\- Modified conditional logic for CEF messages if `message` =~ `CEF` are processed by `cef_extraction.include`, `cef_udm_mapping.include`  
\- Added a conditional logic for `message` !~ `^{` and `message` !~ `CEF` are processed by `drop` with `TAG_MALFORMED_MESSAGE`.  
\- Initialized the `hostId` field with empty strings to ensure proper data mapping. This field was previously uninitialized.  
\- Refactored `msg_data.HostId`, `msg_data.FileTrust`, `msg_data.Message`, `msg_data.PathName`, `msg_data.HostName`, `msg_data.FileHash`, `msg.host.hostname`, `msg_data.ProcessPathName`, `msg_data.ProcessPath`, `msg.log.file.path`, `msg_data.HostIP`, `msg_data.UserName`, `msg.agent.id`, `msg.agent.type`, `msg.agent.name`, `msg.agent.ephemeral_id`, `msg.host.id`, `msg.host.architecture` and `msg.host.os.platform` these fields mapping from the single `rename` block with multiple `replace` blocks with individual `on_error` handlers, improving robustness.  
\- Modified `mac` address Changed the source field from `host_mac` to `msg.host.mac` in the `for` loop.   
2024-07-29 |  Enhancement  
\- Added a Grok pattern to extract the hostname and mapped it to `intermediary.hostname`.   
2022-07-01 |  Enhancement  
\- Mapped the field `agent.type` to `observer.application`.  
\- Mapped the field `agent.name` to `observer.user.userid`.  
\- Mapped the field `host.name` to `observer.hostname`.  
\- Mapped the field `agent.type` and `agent.name` to `observer.asset_id`.  
\- Mapped the field `agent.ephemeral_id` to `observer.labels`.  
\- Mapped the field `host.os.platform` to `target.platform`.  
\- Mapped the field `host.os.version` to `target.platform_version`.  
\- Mapped the field `host.os.kernel` to `target.platform_patch_level`.  
\- Mapped the field `cloud.instance.id` to `principal.resource.product_object_id`.  
\- Mapped the field `cloud.instance.name` to `principal.resource.name`.  
\- Mapped the field `host.mac` to `target.mac`.  
\- Mapped the field `host.ip` to `target.asset.ip`.  
\- Mapped the field `host.id` to `target.asset.asset_id`.  
\- Mapped the field `host.architecture` to `target.asset.hardware`.  
\- Mapped the field `message.UserSID` to `principal.user.userid`.  
\- Mapped the field `message.ProcessPath` to `about.process.command_line`.  
\- Mapped the field `cloud.machine.type` and `cloud.provider` to `principal.resource.attribute.labels`.  
\- Added conditional checks for `message.Bit9Server` and `message.HostId` mapped to `metadata.url_back_to_product`.   
2022-06-22 |  Bug-Fix  
\- Mapped hostId to principal.asset_id  
\- Mapped Bit9Server and HostId combination to metadata.url_back_to_product   
2022-05-19 |  Bug-Fix  
-parsed requested logs in the bug  
-parsed api failed logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
