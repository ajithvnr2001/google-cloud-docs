---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-network-firewall-changelog/
title: Change log for AWS_NETWORK_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:00.508629+00:00
---

# Change log for AWS_NETWORK_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-network-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_NETWORK_FIREWALL

Date | Changes  
---|---  
2026-06-18 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Connection_info.Direction_id`,`Connection_info.Tcp_flags`,`Severity_id`, `Unmapped.Event_type`,`Unmapped.Pkt_src`,`Unmapped.Age`,`Unmapped.Max_ttl`,`Unmapped.Min_ttl`,`Unmapped.Tcp.Ack`,`Unmapped.Tcp.Fin`, `Unmapped.Tcp.Psh`,`Unmapped.Tcp.Syn`,`Unmapped.Reason`,`Start_time`,`End_time` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Connection_info.Protocol_name` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `Unmapped.Alert.Action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Unmapped.Verdict_action`,`Unmapped.Alert.Rev` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `Unmapped.Alert.Signature_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Unmapped.Alert.Category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `Traffic.Bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `Traffic.Packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Unmapped.Availability_zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Unmapped.Alert.Action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Unmapped.Alert.Suricata_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `App_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.   
2026-02-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`\- Newly mapped `event.timestamp` raw log field to event.idm.read_only_udm.additional.fields with key `event_timestamp`.  
\- `event.idm.read_only_udm.additional.fields`\- Newly mapped `event.proto` raw log field to event.idm.read_only_udm.additional.fields with key `network_protocol_info` when `event.proto` is not a valid ip_protocol enum value.  
\- Added conditional logic within the `event.proto` block to handle different `event.proto` values:  
\- If `event.proto` raw log field is `IPV6-ICMP` or `ICMPV6`, set `event.idm.read_only_udm.network.ip_protocol` to `ICMP`.  
\- else if `event.proto` raw log field is a valid ip_protocol enum value, set `event.idm.read_only_udm.network.ip_protocol` to the value of `event.proto`.  
\- In the else block, the `event.proto` raw log field is mapped to `event.idm.read_only_udm.additional.fields` when `event.proto` is not a valid ip_protocol enum value.   
2025-03-12 |  \- Added support for new JSON log format.  
\- Mapped `Connection_info.Protocol_num` to `network.ip_protocol`.  
\- Mapped `Activity_id` to `metadata.product_log_id`.  
\- Mapped `Activity_id`, `Activity_name` to `metadata.product_event_type`.  
\- Mapped `Tls.Version` to `network.tls.version`.  
\- Mapped `Unmapped.Sni` to `network.tls.client.server_name`.  
\- Mapped `Metadata.Version` to `metadata.product_version`.  
\- Mapped `Connection_info.Uid`, `Metadata.Product.Feature.Name`, `Unmapped.App_proto` `Unmapped.Rev`, `Unmapped.Category`, `Unmapped.Tls_inspected`, `Unmapped.Signature_id, `Metadata.Profiles`, `Class_name`, and `Class_uid` to `additional.fields".  
\- Mapped `Unmapped.Suricata_severity` to `security_result.severity_details`.  
\- Mapped `Unmapped.Action` to `security_result.action`.  
\- Mapped `Src_endpoint.Ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `Dst_endpoint.Ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `Src_endpoint.Port` to `principal.port`.  
\- Mapped `Dst_endpoint.Port` to `target.port`.  
\- Mapped `sr_action` to `security_result.action`.  
\- Mapped `Category_name` to `security_result.category_details`.  
\- Mapped `Category_uid` to `security_result.category_details`.  
\- Mapped `Severity` to `security_result.severity_details`.  
\- Mapped `Type_uid` to `security_result.detection_fields`.   
2024-11-28 |  \- Added support for new JSON log format.  
\- Changed mapping of `firewall_name` field from `metadata.product_event_type` to `target.resource.attribute.labels`.   
2023-05-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
