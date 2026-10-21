---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-edgeconnect-sdwan-changelog/
title: Change log for ARUBA_EDGECONNECT_SDWAN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:23:59.173112+00:00
---

# Change log for ARUBA_EDGECONNECT_SDWAN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-edgeconnect-sdwan-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARUBA_EDGECONNECT_SDWAN

Date | Changes  
---|---  
2026-05-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.vendor_name`: Modified `event.idm.read_only_udm.metadata.vendor_name` value from `ARUBA_EDGECONNECT_SDWAN` to `HPE Aruba Networking`.  
\- `event.idm.read_only_udm.metadata.product_name`: Modified `event.idm.read_only_udm.metadata.product_name` value from `ARUBA_EDGECONNECT_SDWAN` to `EdgeConnect SD-WAN`.   
2026-04-17 |  Enhancement:  
\- Added support to parse JSON format logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `IPTos`, `tcpFlags`, `OutputInt`, `logType`, `InputInt`, `ingressVrfId`, `egressVrfId`, `vrfName`, `Overlay`, `proc`, `rxOctets`, `txOctets`, `flowId`, `cpu_id`, `thread_id`, `startTime`, `endTime` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `rxPkts` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `txPkts` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `tid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `userDevice` raw log field with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dstRole` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `srcRole` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- Added gsubs to parse the raw log fields of JSON format logs.  
\- Added a new grok pattern to parse the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.dns.questions`: Newly mapped `dns_questions` raw log field with `event.idm.read_only_udm.network.dns.questions` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `product_event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type` and `event.idm.read_only_udm.network.application_protocol`: Mapped to `NETWORK_DNS` if `principal_present`, `target_present`, and `dns_present` are `true` and set `event.idm.read_only_udm.network.application_protocol` to `DNS`.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `object_type` log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `status` is `succeeded`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- Added a grok pattern on `parameter` log field to extract `Protocol`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Protocol` log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `parameter` (key: `Parameter`) log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added a conditional check before already existing mapping of `principal_ip` to `event.idm.read_only_udm.principal.ip`.  
\- Added a conditional check before already existing mapping of `principal_ip` to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `principal_ip` is not a valid IP address.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field when `principal_ip` is not a valid IP address.  
\- `event.idm.read_only_udm.metadata.event_type`: If `operation` is `modify` and `principal_present` is `true` and `user_present` is `true`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `SETTING_MODIFICATION`.  
\- `event.idm.read_only_udm.target.resource.resource_type`: If `operation` is `modify` and `principal_present` is `true` and `user_present` is `true`, updated the value of `event.idm.read_only_udm.target.resource.resource_type` to `SETTING`.  
\- Added a Grok pattern for `message` log field to parse the raw log fields.  
\- Added new grok pattern for the `message` log field which resulted in removal of the following UDM fields and parsing those raw log fields correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
2026-02-05 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column1_tunnel_name`, `column2_tunnel_name`, `column3_tunnel_name`, `column4_tunnel_name`, `column5_tunnel_name`, `column6_tunnel_name`, `column7_tunnel_name`, `column8_tunnel_name`, `column9_tunnel_name`, `column10_tunnel_name`, `column11_tunnel_name`, `column12_tunnel_name`, `column13_tunnel_name`, `column14_tunnel_name`, `column15_tunnel_name`, `column16_tunnel_name`, `column17_tunnel_name`, `column18_tunnel_name`, `column19_tunnel_name`, `column20_tunnel_name`, `column21_tunnel_name`, `column22_tunnel_name`, `column23_tunnel_name`, `column24_tunnel_name`, `column25_tunnel_name`, `column26_tunnel_name`, `column27_tunnel_name`, `column28_tunnel_name`, `column29_tunnel_name`, `column30_tunnel_name`, `column31_tunnel_name`, `column32_tunnel_name`, `column33_tunnel_name`, `column34_tunnel_name`, `column35_tunnel_name`, `column36_tunnel_name`, `column37_tunnel_name`, `column38_tunnel_name`, `column39_tunnel_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `column1_variable1`, `column2_variable1`, `column2_variable2`, `column3_variable1`, `column3_variable2`, `column4_variable1`, `column4_variable2`, `column5_variable1`, `column5_variable2`, `column6_variable1`, `column6_variable2`, `column7_variable1`, `column7_variable2`, `column8_variable1`, `column8_variable2`, `column9_variable1`, `column9_variable2`, `column10_variable1`, `column10_variable2`, `column11_variable1`, `column11_variable2`, `column12_variable1`, `column12_variable2`, `column13_variable1`, `column13_variable2`, `column14_variable1`, `column14_variable2`, `column15_variable1`, `column15_variable2`, `column16_variable1`, `column16_variable2`, `column17_variable1`, `column17_variable2`, `column18_variable1`, `column18_variable2`, `column19_variable1`, `column19_variable2`, `column20_variable1`, `column20_variable2`, `column21_variable1`, `column21_variable2`, `column22_variable1`, `column22_variable2`, `column23_variable1`, `column23_variable2`, `column24_variable1`, `column24_variable2`, `column25_variable1`, `column25_variable2`, `column26_variable1`, `column26_variable2`, `column27_variable1`, `column27_variable2`, `column28_variable1`, `column28_variable2`, `column29_variable1`, `column29_variable2`, `column30_variable1`, `column30_variable2`, `column31_variable1`, `column31_variable2`, `column32_variable1`, `column32_variable2`, `column33_variable1`, `column33_variable2`, `column34_variable1`, `column34_variable2`, `column35_variable1`, `column35_variable2`, `column36_variable1`, `column36_variable2`, `column37_variable1`, `column37_variable2`, `column38_variable1`, `column38_variable2`, `column39_variable1`, `column39_variable2` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column1_src_ip`, `column2_src_ip`, `column3_src_ip`, `column3_dst_ip`, `column4_src_ip`, `column5_src_ip`, `column6_src_ip`, `column7_src_ip`, `column8_src_ip`, `column9_src_ip`, `column10_src_ip`, `column11_src_ip`, `column12_src_ip`, `column13_src_ip`, `column14_src_ip`, `column15_src_ip`, `column16_src_ip`, `column17_src_ip`, `column18_src_ip`, `column19_src_ip`, `column20_src_ip`, `column21_src_ip`, `column22_src_ip`, `column23_src_ip`, `column24_src_ip`, `column25_src_ip`, `column26_src_ip`, `column27_src_ip`, `column28_src_ip`, `column29_src_ip`, `column30_src_ip`, `column31_src_ip`, `column32_src_ip`, `column33_src_ip`, `column34_src_ip`, `column35_src_ip`, `column36_src_ip`, `column37_src_ip`, `column38_src_ip`, `column39_src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column1_dst_ip`, `column2_dst_ip`, `column4_dst_ip`, `column5_dst_ip`, `column6_dst_ip`, `column7_dst_ip`, `column8_dst_ip`, `column9_dst_ip`, `column10_dst_ip`, `column11_dst_ip`, `column12_dst_ip`, `column13_dst_ip`, `column14_dst_ip`, `column15_dst_ip`, `column16_dst_ip`, `column17_dst_ip`, `column18_dst_ip`, `column19_dst_ip`, `column20_dst_ip`, `column21_dst_ip`, `column22_dst_ip`, `column23_dst_ip`, `column24_dst_ip`, `column25_dst_ip`, `column26_dst_ip`, `column27_dst_ip`, `column28_dst_ip`, `column29_dst_ip`, `column30_dst_ip`, `column31_dst_ip`, `column32_dst_ip`, `column33_dst_ip`, `column34_dst_ip`, `column35_dst_ip`, `column36_dst_ip`, `column37_dst_ip`, `column38_dst_ip`, `column39_dst_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `column1_tunnel_interface`, `column2_tunnel_interface`, `column3_tunnel_interface`, `column4_tunnel_interface`, `column5_tunnel_interface`, `column6_tunnel_interface`, `column7_tunnel_interface`, `column8_tunnel_interface`, `column9_tunnel_interface`, `column10_tunnel_interface`, `column11_tunnel_interface`, `column12_tunnel_interface`, `column13_tunnel_interface`, `column14_tunnel_interface`, `column15_tunnel_interface`, `column16_tunnel_interface`, `column17_tunnel_interface`, `column18_tunnel_interface`, `column19_tunnel_interface`, `column20_tunnel_interface`, `column21_tunnel_interface`, `column22_tunnel_interface`, `column23_tunnel_interface`, `column24_tunnel_interface`, `column25_tunnel_interface`, `column26_tunnel_interface`, `column27_tunnel_interface`, `column28_tunnel_interface`, `column29_tunnel_interface`, `column30_tunnel_interface`, `column31_tunnel_interface`, `column32_tunnel_interface`, `column33_tunnel_interface`, `column34_tunnel_interface`, `column35_tunnel_interface`, `column36_tunnel_interface`, `column37_tunnel_interface`, `column38_tunnel_interface`, `column39_tunnel_interface` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-01-05 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `log_type`, `syslog_ver`, `meta_sequenceId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `sp_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `component` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-12-05 |  Enhancement:  
\- Added a grok patterns to parse the new log formats.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `id`, `isInSync_`, `p_meta_sequenceId`, `startTime`, `endTime`, `result`, `p_sp_id`, `p_service`, `Registered_events`, `UniqueConfigEventsToSync`, `canRecoverConfigEvents`, `firstConfig_changeSet`, `firstConfig_config`, `firstConfig_state`, `lastConfig_changeSet`, `lastConfig_config`, `lastConfig_state`, `isInSync`, `UniqueStateEventsToSync`, `canRecoverStateEvents`, `firstState_baseUrl`, `firstState_config`, `firstState_state`, `firstState_name`, `lastState_config`, `lastState_state`, `duration`, `config_data` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `log_level_num`, `nepk`, `firstState_url`, `lastState_changeSet`, `lastState_baseUrl`, `lastState_url`, `lastState_op`, `lastState_serial`, `lastState_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `taskStatus` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `logLevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.about.resource.name`: Newly mapped `firstConfig_baseUrl` raw log field with `event.idm.read_only_udm.about.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `firstConfig_url` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Newly mapped `firstConfig_op`, `firstConfig_serial`, `lastConfig_baseUrl`, `lastConfig_url`, `lastConfig_op`, `lastConfig_serial`, `firstState_changeSet`, `firstState_op`, `firstState_serial`, `OnGms_1`, `OnApp_1`, `Diff_1` raw log fields with `event.idm.read_only_udm.about.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_user` is true, updated to `USER_UNCATEGORIZED`.   
2024-06-10 |  Enhancement:  
\- Added a Grok pattern to parse the new pattern of SYSLOG format logs.  
\- Mapped `summary` to `security_result.summary`.  
\- Mapped `userid` to `principal.user.userid`.  
\- Mapped `hostname` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `command` to `principal.process.command_line`.  
\- Mapped `principal_ip` to `principal.asset.ip` and `principal.asset.ip`.  
\- When `userid`, `hostname` are present, and `description` is nearly equal to `login`, then set `metadata.event_type` to `USER_LOGIN`.  
\- When `principal_present` is true, then set `metadata.event_type` to `STATUS_UPDATE`.   
2023-05-03 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
