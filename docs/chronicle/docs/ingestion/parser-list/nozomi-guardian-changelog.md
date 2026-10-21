---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nozomi-guardian-changelog/
title: Change log for NOZOMI_GUARDIAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:48:56.951822+00:00
---

# Change log for NOZOMI_GUARDIAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nozomi-guardian-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NOZOMI_GUARDIAN

Date | Changes  
---|---  
2026-01-29 |  \- Updated the mappings of `event.idm.read_only_udm.metadata.event_timestamp` to map `date_time` first if present else map `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-01-16 |  \- event.idm.read_only_udm.security_result.attack_details.techniques.id: Newly mapped `flexString1` raw log field with `event.idm.read_only_udm.security_result.attack_details.techniques.id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `flexString2Label`, `flexString2` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `flexString3Label`, `flexString3` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-10-14 |  \- event.idm.read_only_udm.security_result.description: Newly mapped `properties.cause` raw log field(s) with event.idm.read_only_udm.security_result.description UDM field.  
\- event.idm.read_only_udm.security_result.priority: Newly mapped `properties.priority` raw log field(s) with event.idm.read_only_udm.security_result.priority UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `trigger_type` raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `properties.bad_actor`,`properties.from_id`,`properties.to_id`,`properties.victims`,`created_time`,`destination_types`,`source_level`,`types_src`,`ack`,`properties.mitre_attack_for_ics.destination.types`, `properties.mitre_attack_for_ics.source.levels`,`types_dst`,`levels_src`,`counter`, `closed_time`, `properties.message`, `properties.is_src_reputation_bad`, `properties.is_src_public`,`properties.is_src_node_learned`,`properties.is_dst_node_learned`,`properties.is_dst_public` and `properties.is_dst_reputation_bad` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `properties.rule_name` if present else mapped `trigger_id` raw log field(s) with event.idm.read_only_udm.security_result.rule_name UDM field when `type_id` is equal to `SIGN:PACKET-RULE`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `properties.sid` raw log field(s) with event.idm.read_only_udm.security_result.rule_id UDM field when `type_id` is equal to `SIGN:PACKET-RULE`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `label_dst` raw log field(s) with event.idm.read_only_udm.target.hostname UDM field.   
2025-06-19 |  \- Added a Grok pattern to check whether `from` and `to` are `ip` or `mac` and if `from` is `ip` then mapped `from_ip` to `principal.ip` and `principal.asset.ip` and if `to` is `ip` then mapped `to_ip` to `target.ip` and `target.asset.ip` and if `from` is `mac` then mapped `from_mac` to `principal.mac` and `principal.asset.mac` and if `to` is `mac` then mapped `to_mac` to `target.mac` and `target.asset.mac`.  
\- Removed `security_result_attach` label instead using `security_result` label as it is already being initialized.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `type_id` and `name` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Mapped `type_id` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- event.idm.read_only_udm.security_result.summary: Mapped `name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `properties_rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field , if `properties_rule_name` is empty then use `type_name` field value.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `threat_name` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `trigger_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field  
\- event.idm.read_only_udm.intermediary.hostname: Removed mapping of `appliance_host` from `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.observer.hostname: Mapped `appliance_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `appliance_ip` from `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.observer.ip: Mapped `appliance_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field   
2025-06-18 |  Enhancement:  
\- Added Grok pattern for new pattern of logs.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `metadata.event_type` UDM field as `USER_UNCATEGORIZED` when `suser` is present and `event.idm.read_only_udm.metadata.event_type` is `GENERIC_EVENT`.   
2025-03-10 |  Enhancement:  
\- Added support for JSON format logs.  
\- Mapped `id` and "` to `metadata.product_log_id".  
\- Mapped `type_id` to `additional.fields`.  
\- Mapped `name` to `additional.fields`.  
\- Mapped `mac_src` to `principal.mac`.  
\- Mapped `mac_dst` to `target.mac`.  
\- Mapped `ip_src` to `principal.ip`.  
\- Mapped `ip_dst` to `target.ip`.  
\- Mapped `risk` to `security_result.risk_score`.  
\- Mapped `protocol` to `network.ip_protocol` and `network.application_protocol`.  
\- Mapped `src_roles` to `additional.fields`.  
\- Mapped `dst_roles` to `additional.fields`.  
\- Mapped `port_src` to `principal.port`.  
\- Mapped `port_dst` to `target.port`.  
\- Mapped `appliance_host` to `intermediary.hostname`.  
\- Mapped `appliance_ip` to `intermediary.ip`.  
\- Mapped `is_security` to `security_result.detection_fields`.  
\- Mapped `is_incident` to `security_result.detection_fields`.  
\- Mapped `properties.raised_by` to `additional.fields`.  
\- Mapped `properties.base_risk` to `additional.fields`.  
\- Mapped `properties.learn_rules` to `security_result.detection_fields`.  
\- Mapped `properties.delete_rules` to `security_result.detection_fields`.  
\- Mapped `bpf_filter` to `additional.fields`.  
\- Mapped `status` to `additional.fields`.  
\- Mapped `capture_device` to `additional.fields`.  
\- Mapped sec_profile_visible to `additional.fields`.  
\- Mapped `zone_src` to `principal.location.country_or_region`.  
\- Mapped `zone_dst` to `target.location.country_or_region`.  
\- Mapped `from` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `to` to `target.ip` and `target.asset.ip`.  
\- Mapped `from_zone` to `principal.location.country_or_region`.  
\- Mapped `to_zone` to `target.location.country_or_region`.  
\- Mapped `from_port` to `principal.port`.  
\- Mapped `to_port` to `target.port`.  
\- Mapped `transferred.packets` to `network.sent_packets`.  
\- Mapped `transferred.bytes` to `network.sent_bytes`.  
\- Mapped `throughput_speed` to `additional.fields`.   
2025-01-30 |  \- Changed mapping for `dvchost` from `principal.hostname` to `intermediary.hostname`.  
\- Changed mapping for `device_event_class_id` from `additional.fields` to `metadata.product_event_type`.  
\- Mapped `start` to `metadata.event_timestamp`.  
\- If `start` field is not present mapped `timestamp` from syslog header to `metadata.event_timestamp`.  
\- Mapped `spt` to `principal.port`.  
\- Mapped `smac` to `prinicipal.mac`.  
\- Mapped `proto` to `network.ip_protocol`.  
\- Mapped `app`, `proto`, `cs4`, `cs4Label`, `cs3`, `cs3Label`, `cs2`, `cs2Label`, `cs1`, `cs1Label`, `cs5`, and `cs5Label` to `additional.fields`.  
\- Mapped `dst` to `target.ip`.  
\- Mapped `dpt` to `target.port`.  
\- Mapped `dmac` to `target.mac`.   
2024-11-06 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
