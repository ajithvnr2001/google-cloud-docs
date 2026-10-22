---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sangfor-ngaf-changelog/
title: Change log for SANGFOR_NGAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:31.146350+00:00
---

# Change log for SANGFOR_NGAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sangfor-ngaf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SANGFOR_NGAF

Date | Changes  
---|---  
2026-08-18 |  Enhancement:  
\- `event.idm.read_only_udm.observer.process.file.names`: Newly mapped `observer_process` field with `event.idm.read_only_udm.observer.process.file.names` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `json_entry.attributes.net.host.name` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `json_entry.attributes.net.peer.ip` and `json_entry.attributes.net.peer.name` raw log fields with `event.idm.read_only_udm.observer.ip` UDM field when they are valid IP addresses.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `json_entry.attributes.net.peer.name` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field when it is a hostname.  
\- `event.idm.read_only_udm.observer.port`: Newly mapped `json_entry.attributes.net.peer.port` raw log field with `event.idm.read_only_udm.observer.port` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `json_entry.attributes.chronicle_namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `json_entry.attributes.net.transport` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `json_entry.attributes.net.host.port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.platform`: Newly mapped `json_entry.resource_attributes.os.type` raw log field with `event.idm.read_only_udm.intermediary.platform` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `suser` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when it is a valid IP address.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority`, `json_entry.attributes.chronicle_log_type`, `json_entry.attributes.facility_text`, and `Bidirectional` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `json_entry.resource_attributes.host.name` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.   
2026-05-08 |  Enhancement:  
\- Added new grok pattern to support new format of CEF logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `json_entry.appname`, `json_entry.facility`, `json_entry.priority`, `json_entry.proc_id`, `SessionType`, `SourceSystem`, `app`, `group` and `TimeCreated` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `PolicyUUID`, `SessionEndCause` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `SrcZone` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `DstZone` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `principal_machine_id_present` is `true` and `target_machine_id_present` is `true`, set the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.   
2025-10-17 |  Enhancement:  
\- Pre-processing of the `kv_data` field was added using gsub to normalize keys and delimiters.  
\- New grok patterns were added to parse `ResourceAudit` and `UserAudit` messages.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `ra_user`, `ua_user`, `username_from_desc` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ra_ip`, `ua_ip` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `ra_target_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `System` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log fields with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `ra_description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Conditionally mapped from `ua_action` and `ua_status` raw log fields to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Conditionally mapped from `ra_status` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.   
2024-01-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
