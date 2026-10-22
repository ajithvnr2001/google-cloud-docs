---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snare-solutions-changelog/
title: Change log for SNARE_SOLUTIONS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:57.155977+00:00
---

# Change log for SNARE_SOLUTIONS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/snare-solutions-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SNARE_SOLUTIONS

Date | Changes  
---|---  
2025-11-21 |  Enhancement:  
\- Added new grok pattern to parse logs with tab-separated values and new fields.  
\- Extracted `agent` field from the log.  
\- Added new timestamp formats `yyyy-MM-ddTHH:mm:ss.SSSSSSZZ` and `yyyy-MM-ddTHH:mm:ssZZ` to the date filter.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_hostname` field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_log_id` field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EventChecksum`, `additional_field_1`, `date1`, `windows_event_record_id` field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-22 |  Enhancement:  
\- Added gsub to replace `\\r\\n` with "` , `\\\n` with ` ` and `Filter Information: Filter Run-Time ID` with `filter_runtime_id"  
\- Added a Grok pattern to parse unparsed raw log.  
\- Replaced `event1`, `event2` with `product_event_type_1`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `product_event_type_1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `agent` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `source_source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `severity_number` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record_number` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `event_source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time_syslog` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2025-04-04 |  Enhancement:  
\- Mapped `GROUP_MODIFICATION` with `event.idm.read_only_udm.metadata.event_type` UDM field for `4732` and `4733` eventIDs.   
2025-03-11 |  Enhancement:  
\- Updated mapping of `metadata.event_type` to `GROUP_MODIFICATION` for `4728`, `4729`, `4752`, `4756`, `4757`, `4762` and `4751` eventIDs.   
2025-02-25 |  Enhancement:  
\- Added `gsub` to parse the fields.  
\- Mapped `service_account` to `target.resource.name`.  
\- Mapped `service_start_type` to `additional.fields`.  
\- Mapped `service_type` to `additional.fields`.  
\- Mapped `service_file_name` to `target.file.full_path`.  
\- Mapped `SubjectLogonId` to `additional.fields`.   
2025-02-05 |  Enhancement:  
\- Changed the key name of field `EventType` from `EventType` to `System_Keywords`.  
\- Changed the key name of field `EventCategory` from `EventCategory` to `Task`.  
\- Mapped `TicketEncryptionType` and `TicketOptions` to `additional.fields`.  
\- Mapped `application` to `target.application`.  
\- Mapped `src_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Account Name` to `target.user.userid`.   
2025-02-04 |  Enhancement:  
\- Changed mapping for `network_information_source_network_address` from `target.ip` and `target.asset.ip` to `src.ip`.  
\- Mapped `Process_ProviderPath` to `principal.process.file.full_path`.  
\- Mapped `subject_user` to `principal.user.userid`.  
\- Mapped `subject_account_domain1` to `principal.administrative_domain`.   
2024-12-26 |  Enhancement:  
\- Added a Grok pattern to support new pattern of syslog logs.  
\- Mapped `source_workstation` to `additional.fields`.  
\- Mapped `error_code` to `security_result.description`.   
2024-11-14 |  Enhancement:  
\- Added support for a new format of SYSLOG+JSON logs.  
\- Mapped `event_id` to `additional.fields`.  
\- Mapped `log_name` to `principal.application`.  
\- Mapped `workstation_name` to `target.hostname`.  
\- Mapped `keyword` to `security_result.summary`.  
\- Mapped `event_action` to `security_result.description`.   
2024-07-31 |  Enhancement:  
\- Added support for a new format of SYSLOG logs.   
2024-06-06 |  Enhancement:  
\- Mapped `network_information_workstation_name` to `target.hostname`.  
\- Mapped `intermediary.ip`.  
\- Mapped `target.user.userid`.   
2024-06-04 |  Enhancement:  
\- Added a new Grok pattern to parse the `SYSLOG + KV` format logs.  
\- Mapped `EventCategory` and `EventlogType` to `additional.fields`.  
\- Mapped `filter_runtime_id`, `layer_name`, and `layer_runtime_id` to `security_result.detection_fields`.   
2024-05-31 |  Enhancement:  
\- Mapped `target.user.userid` to have the second part of value.  
\- Mapped event IDs to `metadata.product_event_type`.   
2024-05-20 |  Enhancement:  
\- Mapped `logon type` to `extensions.auth.auth_details`.   
2024-04-17 |  Enhancement:  
\- Supported new Microsoft Windows event logs.   
2024-01-24 |  Enhancement:  
\- Added Grok patterns to parse dropped `SYSLOG + KV` format logs.  
\- Mapped `ts` to `metadata.event_timestamp`.  
\- Mapped `hostname` and `src_host` to `principal.asset.hostname`.  
\- Mapped `src_ip` to `principal.asset.ip`.  
\- Mapped `Namespace` to `principal.user.userid`.  
\- Mapped `ClientProcessID` to `principal.process.pid`.  
\- Mapped `HostApplication` to `principal.application`.  
\- Mapped `Id` to `principal.resource.product_object_id`.  
\- Mapped `ip_protocol` to `network.ip_protocol`.  
\- Mapped `event_id` and `Component` to `additional.fields`.  
\- Mapped `NotificationQuery`, `PossibleCause`, `Operation` and `ResultCode` to `security_result.detection_fields`.  
\- Mapped `ProviderName`, `NewProviderState`, `SequenceNumber`, `HostName`, `HostVersion`, `HostId`, "`EngineVersion`, `RunspaceId`, `PipelineId`, `CommandName`, `ScriptName`, `CommandPath`, `Volume_GUID`, and `Volume_name` to `principal.resource.attribute.labels`.   
2022-07-29 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
