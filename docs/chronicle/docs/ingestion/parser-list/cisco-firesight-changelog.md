---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firesight-changelog/
title: Change log for CISCO_FIRESIGHT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:51.179460+00:00
---

# Change log for CISCO_FIRESIGHT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-firesight-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_FIRESIGHT

Date | Changes  
---|---  
2026-08-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `IntrusionPolicy`, `SnortRuleGroups`, `GID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Revision` and `Classification` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `SID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `InlineResult` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `Message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: If `ApplicationProtocol` is `dns`, updated the value of `event.idm.read_only_udm.network.application_protocol` to `DNS`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Priority` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics` and `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `MitreAttackGroups` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` and `event.idm.read_only_udm.security_result.attack_details.techniques` UDM fields.   
2026-07-31 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rec_type_category` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_sec` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `rec_type_desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `rec_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.observer.asset.asset_id`: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.observer.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `sensor` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `client_app` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `class` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `sid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_set`: Newly mapped `ids_policy` raw log field with `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `rev` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `impact` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `impact_desc` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `class_desc` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `web_app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `http_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `http_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `http_response` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `blockType`, `connection_sec`, `gid`, `iface_egress`, `iface_ingress`, `impact_bits`, `instance_id`, `net_analysis_policy`, `snort_version`, `ssl_flow_status`, `ssl_actual_action`, `mpls_label`, `num_ioc`, `event_usec`, `blocked`, `blocked_reason_id`, `vlan_id` and `fw_policy` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `rec_type_category` is `IPS EVENT` updated `event.idm.read_only_udm.metadata.event_type` to `NETWORK_UNCATEGORIZED`.   
2026-04-14 |  Enhancement:  
\- Added a Grok pattern to parse SYSLOG+KV format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority`, `IngressZone`, `EgressZone`, `IngressVRF`, `EgressVRF`, `ClientAppDetector` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Prefilter Policy`, `Tunnel or Prefilter Rule` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-02-21 |  Enhancement:  
\- Added support to handle new format of logs.   
2024-11-28 |  Enhancement:  
\- Mapped `app` field to `metadata.product_event_type`.  
\- Mapped `ApplicationProtocol` to `network.application_protocol`.   
2024-06-25 |  Enhancement:  
\- Added a Grok pattern to parse the new format logs.  
\- If value of the field `sec_severity` is similar to `error`, then set the value of the field `security_result.severity` to `ERROR`.  
\- Mapped `sec_desc` to `sec_result.description`.  
\- Mapped `app` to `principal.application`.  
\- Mapped `summary` to `sec_result.summary`.   
2024-06-05 |  Enhancement:  
\- Parsed unparsed syslogs by adding a new Grok pattern.   
2024-05-22 |  Enhancement:  
\- Added a Grok pattern to parse dropped logs.  
\- Mapped `product` to `vulnerabilities.vendor`.  
\- Mapped `descript` to `vulnerabilities.description`.  
\- Mapped `severity_detail` to `vulnerabilities.severity_details`.  
\- Mapped `inter` to `intermediary.hostname`.  
\- Mapped `eventId` to `metadata.product_event_type`.  
\- Mapped `DeviceUUID` to `metadata.product_log_id`.  
\- Mapped `InstanceID` to `target.asset_id`.  
\- Mapped `ApplicationProtocol` to `network.application_protocol`.  
\- Mapped `SrcIP` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `DstIP` to `target.ip` and `target.asset.ip`.  
\- Mapped `SrcPort` to `principal.port`.  
\- Mapped `DstPort` to `target.port`.  
\- Mapped `Protocol` to `network.ip_protocol`.  
\- Mapped `InitiatorPackets` to `network.sent_packets`.  
\- Mapped `ResponderPackets` to `network.received_packets`.  
\- Mapped `InitiatorBytes` to `network.sent_bytes`.  
\- Mapped `ResponderBytes` to `network.received_bytes`.  
\- Mapped `URL` to `target.url`.  
\- Mapped `AccessControlRuleName` to `security_result.rule_name`.  
\- Mapped `ConnectionID` to `security_result.about.resource.attribute.labels`.  
\- Mapped `FirstPacketSecond` to `security_result.about.resource.attribute.labels`.  
\- Mapped `EventPriority` to `security_result.severity`.  
\- Mapped `WebApplication`, `URLReputation`, `EgressInterface`, `IngressInterface`, `ACPolicy`, and `NAPPolicy` to `additional.fields`.  
\- Mapped `AccessControlRuleAction` to `security_result.action`.   
2024-04-29 |  Enhancement:  
\- Added support to handle new format of ingested logs.   
2023-09-21 |  Enhancement:  
\- Mapped `proto_type` to `network.ip_protocol`.  
\- Added validation checks before mapping `entry.agent.type`.  
\- Removed repetitive code for `recordTypeCategory` and mapped `recordTypeCategory to `metadata.product_event_type".  
\- Mapped `severity_code to `security_result.severity".  
\- Mapped `service_type`, `syslog_facility_code`, `syslog_priority` to `additional.fields`.  
\- Mapped `entry_msg` to `metadata.description`.   
2022-10-01 |  Enhancement:  
\- Migrated customer specific to default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
