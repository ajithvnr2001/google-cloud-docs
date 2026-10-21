---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-ids-changelog/
title: Change log for SURICATA_IDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:37:11.963675+00:00
---

# Change log for SURICATA_IDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-ids-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SURICATA_IDS

Date | Changes  
---|---  
2024-12-03 |  Enhancement:  
\- Mapped `pkt_src`, `direction`, `http.length`, `flow.pkts_toserver`, `flow.pkts_toclient`, and `http.http_content_type` to `additional.fields`.  
\- Mapped `http.http_user_agent` to `network.http.user_agent`.  
\- Mapped `http.http_method` to `network.http.method`.  
\- Mapped `http.status` to `network.http.response_code`.  
\- Mapped `http://%{http.hostname}%{http.url}` to `target.url`.  
\- Mapped `http.protocol` to `network.tls.version`.   
2024-04-08 |  Enhancement:  
\- Mapped `dns.query.id` to `network.dns.id`.  
\- Mapped `dns.query.rrtype` to `network.dns.questions.type`.  
\- Mapped `dns.query.rrname` to `network.dns.questions.name`.  
\- Mapped `dns.query.opcode` to `network.dns.opcode`.   
2024-03-21 |  Enhancement -  
\- Added support for logs with `event_type` as `stats` and `proto` as `IPv6-ICMP`.   
2023-11-23 |  Enhancement:  
\- Added a Grok pattern to parse newly ingested unparsed logs.  
\- Added a null check before mapping `dns.rrname` to `dns_question.name`.  
\- Set `metadata.event_type` to `NETWORK_CONNECTION` for logs where `dns_rrname` is not present.   
2023-08-24 |  Bug-Fix - Removed `TODO` comments from the parser.   
2022-07-07 |  Enhancement -  
When `event_type` is equal to `snmp`.  
\- Mapped `in_iface` to `security_result.rule_labels`.  
\- Mapped `community_id` to `security_result.rule_labels`.  
\- Mapped `snmp.pdu_type` to `additional.fields`.  
\- Mapped `snmp.community` to `additional.fields`.  
\- Added for loop for `snmp.vars` and mapped it to `additional.fields`.  
When `event_type` is equal to `rdp`.  
\- Mapped `sr_action` to `security_result.action`.  
\- Mapped `in_iface` to `security_result.rule_labels`.  
\- Mapped `community_id` to `security_result.rule_labels`.   
2022-06-13 |  Bug - Following changes are made to this parser-  
1) Fixed unparsed logs of event_type `alert`.  
2) Mapped missing alert event_type fields.  
3) Modified the parser to eliminate old format related to sdm.proto and changed the parser entirely as per udm.proto   
2022-05-23 |  Enhancement - Added mapping for following alert fields:  
Mapped `in_iface` to `target.resource.attribute.labels`.  
Mapped `vlan` to `target.resource.attribute.labels`.  
Mapped `src_ip` to `principal.ip`.  
Mapped `src_port` to `principal.port`.  
Mapped `dest_ip` to `target.ip`.  
Mapped `dest_port` to `target.port`.  
Mapped `proto` to `network.ip_protocol`.  
Mapped `alert.action` to `security_result.action`.  
Mapped `alert.gid` to `target.resource.attribute.labels`.  
Mapped `alert.signature_id` to `target.resource.attribute.labels`.  
Mapped `alert.rev` to `target.resource.attribute.labels`.  
Mapped `alert.signature` to `target.resource.attribute.labels`.  
Mapped `alert.category` to `security_result.threat_name`.  
Mapped `alert.severity` to `security_result.severity`.  
Mapped `alert.metadata.affected_product` to `target.resource.attribute.labels`.  
Mapped `alert.metadata.attack_target` to `target.resource.attribute.labels`.  
Mapped `alert.metadata.deployment` to `target.resource.attribute.labels`.  
Mapped `alert.metadata.former_category` to `target.resource.attribute.labels`.  
Mapped `alert.metadata.signature_severity` to `target.resource.attribute.labels`.  
Mapped `flow.pkts_toserver` to `target.resource.attribute.labels`.  
Mapped `flow.pkts_toclient` to `target.resource.attribute.labels`.  
Mapped `flow.bytes_toserver` to `network.sent_bytes`.  
Mapped `flow.bytes_toclient` to `network.received_bytes`.  
Mapped `payload` to `additional.fields`.  
Mapped `alert.metadata.updated_at` with the format `yyyy-MM-dd` to `date`(metadata.event_timestamp).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
