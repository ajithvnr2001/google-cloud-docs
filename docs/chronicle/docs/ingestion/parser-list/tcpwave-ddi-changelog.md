---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tcpwave-ddi-changelog/
title: Change log for TCPWAVE_DDI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T09:32:18.569141+00:00
---

# Change log for TCPWAVE_DDI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tcpwave-ddi-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TCPWAVE_DDI

Date | Changes  
---|---  
2026-09-07 |  Enhancement:  
\- Added grok patterns to parse the raw log fields.  
\- `event.idm.read_only_udm.network.ip_subnet_range`: Newly mapped `subnet` raw log field with `event.idm.read_only_udm.network.ip_subnet_range` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cb` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.yiaddr`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.network.dhcp.yiaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.ciaddr`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `d_host` and `d_mac` raw log fields with `event.idm.read_only_udm.network.dhcp.chaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.type`: If `description` contains `DHCPOFFER`, updated the value of `event.idm.read_only_udm.network.dhcp.type` to `OFFER`.  
\- `event.idm.read_only_udm.network.application_protocol`: If `description` contains `DHCPOFFER`, updated the value of `event.idm.read_only_udm.network.application_protocol` to `DHCP`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `description` contains `DHCPOFFER`, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP`.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated `event.idm.read_only_udm.metadata.event_type` to `PROCESS_UNCATEGORIZED` when client_identifier, src_mac, and DHCP-related data are not present.   
2026-08-23 |  Enhancement:  
\- Added a grok pattern to parse new format of logs.  
\- Added grok patterns to parse new format of `description` field.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `question_name` raw log field to `event.idm.read_only_udm.network.dns.questions.name`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `int_ip` raw log field to `event.idm.read_only_udm.intermediary.hostname` if it is not an IP address.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support to parse new format of timestamp for field `ts`.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asser.mac`: Newly mapped `d_host` raw log field to `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asser.mac` when it is a valid MAC address.   
2025-12-02 |  Enhancement:  
SYSLOG raw log format: Added support for the SYSLOG raw log format.  
event.idm.read_only_udm.principal.process.file.full_path: Mapped filepath raw log field to event.idm.read_only_udm.principal.process.file.full_path.  
event.idm.read_only_udm.target.hostname: Mapped d_host raw log field to event.idm.read_only_udm.target.hostname.  
event.idm.read_only_udm.target.ip: Mapped d_ip raw log field to event.idm.read_only_udm.target.ip.  
event.idm.read_only_udm.target.mac: Mapped d_mac raw log field to event.idm.read_only_udm.target.mac.  
event.idm.read_only_udm.target.administrative_domain: Mapped d_domain raw log field to event.idm.read_only_udm.target.administrative_domain.  
event.idm.read_only_udm.network.dhcp.client_identifier: Mapped d_clientID raw log field to event.idm.read_only_udm.network.dhcp.client_identifier.  
security_result.description: Mapped des raw log field to security_result.description.  
event.idm.read_only_udm.src.hostname: Mapped src raw log field to event.idm.read_only_udm.src.hostname.  
event.idm.read_only_udm.src.mac: Mapped src_mac raw log field to event.idm.read_only_udm.src.mac.  
event.idm.read_only_udm.network.dhcp.chaddr: Mapped src_mac raw log field to event.idm.read_only_udm.network.dhcp.chaddr.  
event.idm.read_only_udm.intermediary.ip: Mapped int_ip raw log field to event.idm.read_only_udm.intermediary.ip.  
event.idm.read_only_udm.metadata.event_type: Set to NETWORK_DHCP for DHCP events.  
event.idm.read_only_udm.network.application_protocol: Set to DHCP for DHCP events.  
event.idm.read_only_udm.network.dhcp.type: Mapped DHCP message type from description field to event.idm.read_only_udm.network.dhcp.type.  
security_result.action: Set to BLOCK when the description field contains `rejected`.  
event.idm.read_only_udm.additional.fields: Mapped DHCP pool-related fields to event.idm.read_only_udm.additional.fields.   
2022-09-27 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
