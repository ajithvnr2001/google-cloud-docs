---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-eve-changelog/
title: Change log for SURICATA_EVE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:07.995987+00:00
---

# Change log for SURICATA_EVE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/suricata-eve-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SURICATA_EVE

Date | Changes  
---|---  
2026-05-11 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `src_ip` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, as `src_ip` contains an IP address, not a hostname and is already being mapped to the appropriate UDM field.   
2026-04-21 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`: If `alert.severity` is `2`, updated the value of `event.idm.read_only_udm.security_result.severity` to MEDIUM.  
\- `event.idm.read_only_udm.security_result.severity`: If `alert.severity` is `3`, updated the value of `event.idm.read_only_udm.security_result.severity` to LOW.  
\- `event.idm.read_only_udm.security_result.severity`: If `alert.severity` is `4`, updated the value of `event.idm.read_only_udm.security_result.severity` to LOW.  
\- `event.idm.read_only_udm.principal.ip` / `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `flow.src_ip`, `alert.source.ip` raw log fields with `event.idm.read_only_udm.principal.ip` / `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` / `event.idm.read_only_udm.target.asset.ip`: Newly mapped `flow.dest_ip`, `alert.target.ip` raw log fields with `event.idm.read_only_udm.target.ip` / `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `flow.pkts_toserver`, `flow.pkts_toclient`, `alert.source.port`, `alert.target.port`, `alert.rule` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `alert.metadata.attack_target`, `alert.metadata.confidence`, `alert.metadata.deployment`, `alert.metadata.tag` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Added conditional check to update the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` and `NETWORK_DHCP`.  
\- `event.idm.read_only_udm.network.dhcp.ciaddr`: Newly mapped `dhcp.client_ip` raw log field with `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.client_identifier`: Newly mapped `dhcp.client_id` raw log field with `event.idm.read_only_udm.network.dhcp.client_identifier` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dhcp.params` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.client_hostname`: Newly mapped `dhcp.hostname` raw log field with `event.idm.read_only_udm.network.dhcp.client_hostname` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.options`: Newly mapped `dhcp.vendor_class_identifier` raw log field with `event.idm.read_only_udm.network.dhcp.options` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.opcode`: Newly mapped `dhcp.type` raw log field with `event.idm.read_only_udm.network.dhcp.opcode` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.type`: Newly mapped `dhcp.dhcp_type` raw log field with `event.idm.read_only_udm.network.dhcp.type` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.yiaddr`: Newly mapped `dhcp.assigned_ip` raw log field with `event.idm.read_only_udm.network.dhcp.yiaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `dhcp.client_mac` raw log field with `event.idm.read_only_udm.network.dhcp.chaddr` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: If event is DHCP, updated the value of `event.idm.read_only_udm.network.application_protocol` to `DHCP`.   
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check for `SCAN_NETWORK` when `event_type` is `alert` and principal machine data such as src_ip is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event_type` to `NETWORK_CONNECTION` when principal machine data such as `src_ip` or `src_FQDN` is present, and target machine data such as `dest_ip` or `dest_FQDN` is present.   
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dns.qr` (key: `dns_qr`), `tls.ja3.string` (key:`tls_ja3_string`), `tls.ja3s.string` (key: `tls_ja3s_string`), `tls.ja4` (key: `tls_ja4`), `dns.version` (key: `dns_version`), `dns.type` (key: `dns_type`), `dns.opcode` (key: `dns_opcode`), `dns.tx_id` (key: `dns_tx_id`), `dns.flags` (key: `dns_flags`), `audata.soa.mname` (key: `soa_mname_%{index}`), `audata.soa.rname` (key: `soa_rname_%{index}`), `audata.soa.serial` (key: `soa_serial_%{index}`), `audata.soa.refresh` (key: `soa_refresh_%{index}`), `audata.soa.retry` (key: `soa_retry_%{index}`), `audata.soa.expire` (key: `soa_expire_%{index}`), `audata.soa.minimum` (key: `soa_minimum_%{index}`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.dns.recursion_desired`: Newly mapped `dns.rd` raw log field with `event.idm.read_only_udm.network.dns.recursion_desired` UDM field.  
\- `event.idm.read_only_udm.network.dns.recursion_available`: Newly mapped `dns.ra` raw log field with `event.idm.read_only_udm.network.dns.recursion_available` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers`: Newly mapped fields from `dns.answers` and `dns.authorities` raw log fields with `event.idm.read_only_udm.network.dns.answers` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `event_type` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field when `event_type` is `dns`.  
\- `event.idm.read_only_udm.network.dns.answers.ttl`: Newly mapped `dns.answers.ttl` and `dns.authorities.ttl` raw log fields with `event.idm.read_only_udm.network.dns.answers.ttl` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.type`: Newly mapped `dns.authorities.rrtype` and `dns.answers.rrtype` raw log fields with `event.idm.read_only_udm.network.dns.answers.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.name`: Newly mapped `dns.authorities.rrname` and `dns.answers.rrname` raw log fields with `event.idm.read_only_udm.network.dns.answers.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.data`: Newly mapped `dns.answers.rdata` raw log field with `event.idm.read_only_udm.network.dns.answers.data` UDM field.  
\- `event.idm.read_only_udm.network.dns.response_code`: Newly mapped `dns.rcode` raw log field with `event.idm.read_only_udm.network.dns.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `event_type` is `dns`, updated to `NETWORK_DNS`.  
\- Modified a grok pattern to parse the `protocol` raw log field correctly.   
2025-12-03 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `direction`, `file.filename`, `file.gaps`, `file.size`, `file.stored`, `file.tx_id`, `http.length`, `in_iface`, and `pkt_src` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.target.url: Newly mapped a combination of `http.protocol`, `http.hostname`, and `http.url` raw log fields to `event.idm.read_only_udm.target.url`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `alert.category` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `alert.gid` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `sensor` raw log field to `event.idm.read_only_udm.observer.hostname`.  
\- Added type conversion for the `flow_id` field to ensure it is a string before mapping.   
2025-01-09 |  Enhancement:  
\- Mapped `ssh.server.hassh.software_version`, `ssh.server.hassh.proto_version`, `ssh.server.hassh.string`, `ssh.client.hassh.software_version`, `ssh.client.hassh.proto_version`, `ssh.client.hassh.string` to `additional.fields`.   
2024-12-03 |  Enhancement:  
\- Added support to parse requested fields.   
2024-11-07 |  Enhancement:  
\- Mapped `alert.metadata.stamus_classification` to `additional.fields`.  
\- Mapped `alert.metadata.sightings_key` to `additional.fields`.  
\- Mapped `alert.metadata.sightings_asset` to `additional.fields`.   
2024-09-11 |  Enhancement:  
\- Mapped `discovery` to `additional.fields`.   
2024-08-22 |  Enhancement:  
\- When `app_proto` is a valid enum value, then mapped to `network.application_protocol` else mapped it to `additional.fields`.  
\- Mapped `dns.rrtype` to `network.dns.questions.type`.  
\- Mapped `dns.rrname` to `network.dns.questions.name`.  
\- Mapped `dns.id` to `network.dns.id`.  
\- Mapped `see_id` to `network.session_id`.  
\- Mapped `flow_id` to `additional.fields`.   
2024-05-16 |  Enhancement:  
\- Declared fields `direction`, `dstnetwork`, and `application_port`.   
2024-04-17 |  Enhancement:  
\- Mapped `payload_printable` to `additional.fields`.   
2022-08-17 |  Enhancement -  
\- Mapped dest_ip to target.ip.  
\- Modified mapping of security_result.severity from critical to high where severity is 1.  
\- Added a grok to parse logs with syslog header.   
2022-07-25 |  Enhancement -  
\- Mapped `process.executable` to `principal.process.file.full_path`.  
\- Mapped `process.pid` to `principal.process.pid`.  
\- Mapped `process.command_line` to `principal.process.command_line`.  
\- Mapped `service.type` to `additional.fields`.  
\- Mapped `event.dataset` to `about.labels`.  
\- Mapped `event.module` to `about.labels`.  
\- Mapped `event.duration` to `about.labels`.  
\- Mapped `agent.id` to `metadata.product_log_id`.  
\- Mapped `agent.type` to `metadata.product_event_type`.  
\- Mapped `agent.version` to `metadata.product_version`.  
\- Mapped `agent.hostname` to `principal.hostname`.  
\- Mapped `agent.name` to `principal.hostname`.  
\- Mapped `agent.ephemeral_id` to `additional.fields`.  
\- Mapped `ecs.version` to `principal.asset.attribute.labels`.  
\- Mapped `process.args` to `about.file.capabilities_tags`.   
2022-07-08 |  Enhancement - Added mappings for following fields :  
\- `tls.sni` mapped to `target.hostname`.  
\- `tls.issuerdn` mapped to `network.tls.client.certificate.issuer`.  
\- `tls.subject` mapped to `network.tls.client.certificate.subject`.  
\- `tls.serial` mapped to `network.tls.client.certificate.serial`.  
\- `tls.fingerprint` mapped to `network.tls.client.certificate.sha256`.  
\- `tls.version` mapped to `network.tls.version`.  
\- `tls.ja3.hash` mapped to `network.tls.client.ja3`.  
\- `tls.ja3s.hash` mapped to `network.tls.server.ja3s`.  
\- `tls.notbefore` mapped to `network.tls.client.certificate.not_before`.  
\- `tls.notafter` mapped to `network.tls.client.certificate.not_after`.  
\- `tls.sni` mapped to `network.tls.client.server_name`.  
\- Modified the mappings for following fields :  
\- if `alert.severity` has values 0,1,2 then `security_result.severity` mapped to CRITICAL.  
\- if `alert.severity` has values 3,4 then `security_result.severity` mapped to HIGH.  
\- if `alert.severity` has values 5,6,7 then `security_result.severity` mapped to LOW.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
