---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-nsx-changelog/
title: Change log for VMWARE_NSX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:22.759933+00:00
---

# Change log for VMWARE_NSX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-nsx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_NSX

Date | Changes  
---|---  
2026-01-01 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `src_host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `src_host` raw log field to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Resource` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-19 |  Enhancement:  
\- Added a grok pattern to extract `sent_pkt`, `received_pkt`, `sent_byte`, `received_byte`, `src_zone_value`, and `zone_action` values.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `zone_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-12-11 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `component_tag` and `Time` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Modified grok patterns to dynamically capture the component tag (e.g., `Edge`, `SystemEvent`).   
2025-12-04 |  Enhancement:  
\- Added new grok patterns to parse new format of logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added additional support to `datetime` raw log field to correctly extract the timezone before mapping it to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-11-26 |  Enhancement:  
\- Added grok patterns to provide support for new format of syslog logs.  
\- 'event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `sent_pkt` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `received_pkt` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sent_byte` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `received_byte` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg1` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ip_version`,`ip_protocol_type`, `ip_protocol_code`,`interface_id` and `tcp_flags` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `src_zone_value` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `sec_desc` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2025-11-02 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `datetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `Originated_Ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `Originated_Ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `Module` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `event_source` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Resource_Name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Universal_Object` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `Code` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `Event_Message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Above_supported_instances`, `Above_threshold_instances`, `Below_threshold_instances`, `supported_compact`, `supported_quadlarge`, `supported_large` and `supported_xlarge` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If Operation is LOGOUT, updated to USER_LOGOUT.   
2024-09-25 |  Enhancement :  
\- When `action` is `DROP` then set `security_result.action` to `BLOCK`.  
\- When `action` is not null then mapped `action` to `security_result.action_details`.   
2024-07-09 |  Enhancement :  
\- Added `gsub` to replace `\\r\\n` from the message.   
2024-06-17 |  Enhancement :  
\- Added Grok patterns to parse newly ingested logs.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `protocol` to `network.ip_protocol`.  
\- Mapped `rule_id` to `security_result.rule_id`.  
\- When `direction` is `IN`, then mapped `network.direction` to `INBOUND`.  
\- When `action` is `PASS`, then mapped `security_result.action_details` to `ALLOW`.  
\- When `action` is `FAIL`, then mapped `security_result.action_details` to `BLOCK`.  
\- When `src_ip` and `dst_ip` are not null, then mapped `metadata.event_type` to `NETWORK_CONNECTION`.   
2024-06-10 |  Enhancement :  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.   
2023-11-15 |  Enhancement :  
\- From `Old Value` field:  
\- Mapped `unique_id` to `principal.resource.product_object_id`.  
\- Mapped `resource_type` to `principal.resource.sub_type`.  
\- Mapped `_create_user`,`_last_modified_user` to `principal.user.email_addresses`.  
\- Mapped `action` to `security_result.action`.  
\- Mapped `rule_id` to `security_result.rule_id`.  
\- Mapped `display_name` to `principal.resource.name`.  
\- Mapped `_last_modified_time` to `principal.resource.attribute.last_update_time`.  
\- Mapped `_create_time` to `principal.resource.attribute.creation_time`.  
\- Mapped `parent_path` to `principal.resource.parent`.  
\- Mapped `path` to `principal.process.file.full_path`.  
\- Mapped `id` to `principal.resource.id`.  
\- From New Value field:  
\- Mapped `resource_type` to `target.resource.sub_type`.  
\- Mapped `unique_id` to `target.resource.product_object_id`.  
\- Mapped `path` to `target.process.file.full_path`.  
\- Mapped `display_name` to `target.resource.name`.  
\- Mapped `id` to `target.resource.id`.  
\- Mapped `vmw_host` to `target_details.hostname or target_details.ip` based on value in vmw_host.  
\- Mapped `vmw_product` to `target.application`.  
\- Mapped `vmw_vcenter` to `target.cloud.availability_zone`.  
\- Mapped `vmw_cluster` to `target.resource.name`.  
\- Mapped `vmw_object_id` to `target.resource.product_object_id`.  
\- Mapped `vmw_datacenter` to `target.resource.attribute.labels`.  
\- Mapped `vmw_vcenter_id` to `target.resource.attribute.labels`.  
\- Mapped `vmw_vr_ops_logtype` to `intermediary.resource.attribute.labels`.  
\- Mapped `vmw_vr_ops_appname` to `intermediary.application`.  
\- Mapped `vmw_vr_ops_hostname` to `intermediary.hostname`.  
\- Mapped `vmw_vr_ops_nodename` to `intermediary.resource.attribute.labels`.  
\- Mapped `vmw_vr_ops_clustername` to `intermediary.resource.name`.  
\- Mapped `vmw_vr_ops_clusterrole` to `intermediary.resource.attribute.labels.roles.name`.  
\- Mapped `vmw_vr_ops_id` to `intermediary.resource.product_object_id`.   
2023-10-13 |  Enhancement :  
\- Modified a Grok pattern to parse `sourceIp` with ports.  
\- Mapped `vmw_host`,`vmw_product`,`vmw_vcenter`,`vmw_cluster`,`vmw_vr_ops_id`,`vmw_object_id`,`vmw_datacenter`,`vmw_vcenter_id`,`vmw_vr_ops_logtype`,`vmw_vr_ops_appname`,`vmw_vr_ops_hostname`,`vmw_vr_ops_nodename`,`vmw_vr_ops_clustername`,`vmw_vr_ops_clusterrole`,`managedExternally`,`update`,`filepath`,`eventType`,`resourceId` to `principal.resource.attribute.labels`.  
\- Mapped fields in `payload` to `principal.resource.attribute.labels`.  
\- Mapped `client` to `principal.ip`  
\- Mapped fields in `new_value` to `target.resource.attribute.labels`.   
2023-10-03 |  Enhancement :  
\- Added a Grok pattern to check if `sourceIp` is a valid IP address or not prior mapping it to UDM field.   
2023-09-12 |  Enhancement :  
\- Added support for syslog logs that have `New value` and `Old value` fields.   
2023-06-26 |  Enhancement:  
\- Mapped values in `PASS`, `DROP`, `REJECT`, `NAT`, `NONAT`, `RDR`, `NORDR`, `PUNT`, `REDIRECT`, and `COPY` to `additional.fields` key as `Network_Status`.   
2023-03-07 |  Enhancement:  
\- Mapped `errorCode` to `security_result.detection_fields`.  
\- Mapped `app_type` to `principal.application`.  
\- Mapped `tname`, `s2comp`, `node` to `principal.resource.attribute.labels`.  
\- Mapped `exe` to `target.process.file.full_path`.  
\- Mapped `dst_ip` to `target.ip`.  
\- Mapped `ses` to `network.session_id`.  
\- Mapped `hostname` to `principal.ip`.  
\- Mapped `direction` to `network.direction`.  
\- Mapped `reqId` to `metadata.product_log_id`.   
2022-06-10 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
