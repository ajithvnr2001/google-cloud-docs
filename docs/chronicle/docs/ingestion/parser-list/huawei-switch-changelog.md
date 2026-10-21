---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/huawei-switch-changelog/
title: Change log for HUAWEI_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:53.515194+00:00
---

# Change log for HUAWEI_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/huawei-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HUAWEI_SWITCH

Date | Changes  
---|---  
2026-07-25 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `log_type` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `USER` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `MAC` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.observer.mac`: Newly mapped `APMAC` raw log field with `event.idm.read_only_udm.observer.mac` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `ACNAME` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `ACMAC` raw log field with `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `RESULT` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `SSID` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `AUTHID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `RADIOID`, `ERRCODE`, `DAYLIGHT`, `ZONE`, `INTERFACE`, `CIB ID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `TIME` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- Added support to parse new date format of `syslog_timestamp` raw log field.   
2026-07-02 |  Enhancement:  
\- Added grok pattern to parse new format of SYSLOG logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `source_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `syslog_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal or target machine data is present and user data is available, updated the `event.idm.read_only_udm.metadata.event_type` to USER_UNCATEGORIZED.   
2026-04-16 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `UserAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `LocalAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `FailedReason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `VPNInstanceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2026-03-18 |  Enhancement:  
\- Modified a grok pattern on desc to extract event_hostname, event_type, cid, and desc_input.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `event_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc_input` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_type_value` and `event_identifier_value` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `UserType`, `event_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: If `UserType` is SSH, updated the value of `event.idm.read_only_udm.network.application_protocol` to SSH.  
\- `event.idm.read_only_udm.metadata.event_type`: If event_type contains LOGIN, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGIN.  
\- `event.idm.read_only_udm.extensions.auth.type`: If event_type contains LOGIN, updated the value of `event.idm.read_only_udm.extensions.auth.type` to AUTHTYPE_UNSPECIFIED.   
2026-03-10 |  Enhancement:  
\- Added support for a new log format by introducing a new Grok statement.  
\- Modified a grok pattern to extract `alarmID` from the raw log.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `ServiceType` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `IPADDRESS` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `InterfaceName` (key: `InterfaceName`), `TrapThreshold` (key: `TrapThreshold`), `BandWidthUsage` (key: `BandWidthUsage`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Due to such changes, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.intermediary.hostname`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.resource.name`  
2026-03-06 |  Enhancement:  
\- Added KV filter to parse new log format.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `VpnName` from `event.idm.read_only_udm.additional.fields` UDM field. Since principal.resource.name is a appropriate UDM mapping for this field.  
\- `event.idm.read_only_udm.principal.resource.name`: Mapped `VpnName` raw log field to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserName` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `SourceAddress` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SourceAddress` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `DestAddress` raw log field(s) with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `DestAddress` raw log field(s) with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `Method` raw log field(s) with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SessionId` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Url` raw log field(s) with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Extracted `cmd` from `Body` raw log field(s) and mapped with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `FragIndex`, `Accept`, `ContentType`, `Body`, `AssistantName` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-09 |  Enhancement:  
\- Added grok pattern to parse new log format.  
`event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `raw_syslog_timestamp` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
`event.idm.read_only_udm.intermediary.hostname`: Newly mapped `raw_hostname` raw log field(s) with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
`event.idm.read_only_udm.principal.mac`: Newly mapped message `mac_address` raw log field(s) with `event.idm.read_only_udm.principal.mac` UDM field.  
`event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped message `temp_oid` raw log field(s) with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
`event.idm.read_only_udm.target.resource.name`: Newly mapped message `temp_security` raw log field(s) with event.idm.read_only_udm.target.resource.name UDM field.  
`event.idm.read_only_udm.additional.fields`: Newly mapped `service_vlan_id`, `service_original_port`, `service_flapping_port1`, `service_flapping_port2` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.   
2026-02-04 |  Enhancement:  
\- Added grok pattern to parse new log format.  
`event.idm.read_only_udm.network.application_protocol`: Newly mapped `SSH` to `event.idm.read_only_udm.network.application_protocol` UDM field.  
`event.idm.read_only_udm.principal.user.userid`: Newly mapped `temp_username` to `event.idm.read_only_udm.principal.user.userid` UDM field.  
`event.idm.read_only_udm.principal.ip`: Newly mapped `temp_ip` to `event.idm.read_only_udm.principal.ip` UDM field.  
`event.idm.read_only_udm.principal.resource.name`: Newly mapped `temp_vpn` to `event.idm.read_only_udm.principal.resource.name` UDM field.  
`event.idm.read_only_udm.principal.resource.type`: Newly mapped `VPN` to `event.idm.read_only_udm.principal.resource.type` UDM field.  
`event.idm.read_only_udm.security_result.description`: Newly mapped `temp_summary` to `event.idm.read_only_udm.security_result.description` UDM field.  
`event.idm.read_only_udm.target.ip`: Newly mapped `temp_local_ip` to `event.idm.read_only_udm.target.ip` UDM field.  
`event.idm.read_only_udm.target.resource.name`: Newly mapped `tty_type` to `event.idm.read_only_udm.target.resource.name` UDM field.   
2026-01-22 |  Enhancement:  
\- Modified grok pattern to parse new format of hostname.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alarmID`, `event_identifier` and `clearType` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `temp_description` to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `temp_cid` to `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2026-01-08 |  Enhancement:  
\- Added grok pattern to parse new log format.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostname` field with event.idm.read_only_udm.intermediary.hostname UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `severity` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `host` field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facilityName` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severityName` to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severityName` to `event.idm.read_only_udm.security_result.severity` when the field value is `warning`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `DeviceType` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `syslog_timestamp` to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `devid` to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.   
2025-01-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
