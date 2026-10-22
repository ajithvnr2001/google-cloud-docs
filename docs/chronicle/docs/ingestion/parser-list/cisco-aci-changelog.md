---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-aci-changelog/
title: Change log for CISCO_ACI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:53.587196+00:00
---

# Change log for CISCO_ACI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-aci-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ACI

Date | Changes  
---|---  
2026-04-15 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `principal_mac` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `context_id` and `node_number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `code1` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `code2` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field  
\- Added `aci_tag`, `message_class`, `message_dn`, `principal_user`, `principal_ip`, `protocol`, `result`, `code1`, `code2`, `product_event_type` in the overwrite block.  
\- Added grok patterns to parse new formats of SYSLOG logs, allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.additional.fields[`Hitcnt`]`  
\- `event.idm.read_only_udm.additional.fields[`message_class`]`  
\- `event.idm.read_only_udm.additional.fields[`message_dn`]`  
\- `event.idm.read_only_udm.additional.fields[`protocol`]`  
\- `event.idm.read_only_udm.additional.fields[`Vlan Type`]`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_log_id`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.session_id`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.process.file.full_path`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels[`SMac`]`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels[`Src Intf`]`  
\- `event.idm.read_only_udm.principal.resource.id`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.action_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields[`code1`]`  
\- `event.idm.read_only_udm.security_result.detection_fields[`code2`]`  
\- `event.idm.read_only_udm.security_result.rule_name`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.resource.attribute.labels[`DMac`]`  
2025-12-05 |  Enhancement:  
\- Added support to the new format of SYSLOG+KV logs.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `src_intf` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `VXLAN` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `VlanType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `flag` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Hitcnt` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_facility` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `SMac` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `DMac` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `CName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.intermediary.ip : Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip : Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity_action` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-12-03 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_user` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `protocol` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip` field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `ip_1` field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `result` field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `security_result_action` field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Newly mapped a static value `AUTHTYPE_UNSPECIFIED` with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `message_code` contains `logout` and `has_target` is `true`, updated to `USER_LOGOUT`.  
\- event.idm.read_only_udm.metadata.event_type: If `message_code` contains `login` and `has_target` is `true`, updated to `USER_LOGIN`.  
\- Added Grok patterns to parse `principal_user`, `principal_ip`, `protocol`, and `result` from `message_content`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `protocol`, `message_code`, `program`, `syslog_prog`, `message_dn`, `message_class`, `syslog_facility_code`, `syslog5424_pri`, `initial_code`, `syslog_facility`, `logstash.ingest.timestamp`, `cisco_timestamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-09 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `source_host` from `event.idm.read_only_udm.principal.ip` UDM field as it is `observer.ip`.  
\- Modified condition to set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2025-01-16 |  Enhancement:  
\- Added support for new JSON log formats.   
2022-09-26 |  Enhancement: Mapped `vendorname` as `CISCO`  
Mapped `vendorname` as `ACI`  
Mapped `sysloghost` as `Observer ip`  
2022-08-05 |  Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
