---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-sdwan-changelog/
title: Change log for CISCO_SDWAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:55.751686+00:00
---

# Change log for CISCO_SDWAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-sdwan-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_SDWAN

Date | Changes  
---|---  
2026-06-16 |  Enhancement:  
\- Added new grok patterns to parse the new format of SYSLOG logs.   
2025-11-18 |  Enhancement:  
\- Added grok patterns to parse new format of SYSLOG logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rsa_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sha_256` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-25 |  Enhancement:  
\- Modified Grok patterns to parse `metadata.product_event_type` and `intermediary.hostname` UDM fields correctly.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Removed mapping of `peer_ip` raw log field from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `peer_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.process.parent_process.pid: Newly mapped `parent_pid` raw log field to `event.idm.read_only_udm.principal.process.parent_process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `log_id` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `process_name` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `process_path` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.   
2025-08-11 |  Enhancement:  
\- Modified a grok pattern on `message` field to parse the new format of raw logs.  
\- Added a new grok pattern on `msgs` field to parse `session_id`, `ipaddress`,`username` fields for the new format of raw logs.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- Modified a flag used for `username` field mapping from `has_principal` to `has_principal_user`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time_t` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-06-26 |  Enhancement:  
\- Added Grok patterns to parse the raw logs.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `target_name` field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `parent_identifier` field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `specific_identifier` field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `initiator_ip` field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `initiator_port` field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `responder_ip` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `responder_port` field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vlan_id`, `src_vrf`, `dst_vrf`, `qfp`, `Tunnel_id`, `vpn_id`, `tos`, `count`, `tenant_vpn_id`, `sequence`, `result`, `unknown_tenant` and `thread` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `sent_bytes_1`, `sent_bytes_2`, `log_prefix`,`protocol`, `log_reason`, `ingress_interface`, `egress_interface`, `direction`, `policy`, `udp_packets` and `tty` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `src_port` field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst_ip` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dst_port` field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `network_host` field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `application_protocol` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes` field with `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2025-06-23 |  Enhancement:  
\- Added Grok patterns to parse the raw logs.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `logid` field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logmodule` ,`logfeature`,`meta_sequenceId` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `loguser`,`user1` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `logusersrcip`,`principal_ip1` field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `logmsg` field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Newly mapped `logdeviceid` ,`peer_ip` ,`target_ip1` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.intermediary.hostname,event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `host_name` field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `process` field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.pid: Newly mapped `pid` field with `event.idm.read_only_udm.principal.pid` UDM field.  
\- Added Grok patterns on `description_1` field.  
\- event.idm.read_only_udm.network.dhcp.type: Newly mapped `type1` field with `event.idm.read_only_udm.network.dhcp.type` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `principal_port1` field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port1` field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `description_1` field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- Mapped `NETCONF` to `event.idm.read_only_udm.network.application_protocol` UDM field if the message contains `netconf`.  
\- Mapped `TCP` to `event.idm.read_only_udm.network.ip_protocol` UDM field if the message contains `tcp`.  
\- Mapped `DHCP` to `event.idm.read_only_udm.network.application_protocol` UDM field if the message contains `dhcp`.  
\- Added a conditional check if `prod_type` contains `Connection closed` and `has_target` flag is equals to true then map `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` and `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`.  
\- Added a conditional check if `has_principal_user` flag is equals to true then map `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` .  
\- Merged `intermediary` with `event.idm.read_only_udm.intermediary` UDM field.   
2025-03-19 |  Enhancement:  
\- Added Grok patterns to parse the logs.  
\- Mapped `username1` to `target.user.userid`.  
\- Mapped `security_result.action` to `ALLOW` or `BLOCK` based on the message.  
\- Mapped `metadata.event_type` to `USER_LOGIN` when the message contains `success` and `has_principal` and `has_user` are true.  
\- Mapped `metadata.event_type` to `USER_LOGOUT` when the message contains `LOGOUT` and `has_principal` and `has_user` are true.   
2025-03-04 |  Enhancement:  
\- Mapped `timestamp` to `metadata.event_timestamp`.  
\- Mapped `ip_1` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ip_2` to `target.ip` and `target.asset.ip`.  
\- Mapped `port_1` to `principal.port`.  
\- Mapped `port_2` to `target.port`  
\- Mapped `system_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `instance_id` to `target.resource.product_object_id`.  
\- Mapped `message_1` to `metadata.description`.  
\- Mapped `network_protocol` to `network.ip_protocol`.  
\- Mapped `hostname` to `principal.hostname`.  
\- Mapped `classification` to `security_result.category_details`.  
\- Mapped `priority` to `security_result.severity`.  
\- Mapped `policy` to `security_result.detection_fields`.  
\- Mapped `malware` to `security_result.detection_fields`.  
\- Mapped `filename` to `target.file.names`.  
\- Mapped `filetype` to `target.process.file.mime_type`.   
2025-02-24 |  \- Added support to parse the unparsed logs.   
2025-01-16 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
