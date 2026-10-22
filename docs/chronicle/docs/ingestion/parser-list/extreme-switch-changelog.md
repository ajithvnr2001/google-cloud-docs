---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-switch-changelog/
title: Change log for EXTREME_SWITCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:45.477942+00:00
---

# Change log for EXTREME_SWITCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/extreme-switch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for EXTREME_SWITCH

Date | Changes  
---|---  
2025-09-01 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `host` raw log field(s) with event.idm.read_only_udm.principal.hostname UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host` raw log field(s) with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src_ip` raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `client_mac` raw log field(s) with event.idm.read_only_udm.principal.mac UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `client_mac` raw log field(s) with event.idm.read_only_udm.principal.asset.mac UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst_ip` raw log field(s) with event.idm.read_only_udm.target.ip UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field(s) with event.idm.read_only_udm.target.asset.ip UDM field.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `client_mac` raw log field(s) with event.idm.read_only_udm.network.dhcp.chaddr UDM field.  
\- `event.idm.read_only_udm.network.dhcp.giaddr`: Newly mapped `gateway_ip` raw log field(s) with event.idm.read_only_udm.network.dhcp.giaddr UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `summary` raw log field(s) with event.idm.read_only_udm.security_result.summary UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `vlan_name`, `Port`, `slot`, `packet_type` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, `has_target` is `true`, `has_network_dhcp` is `true`, updated to `NETWORK_DHCP`.  
\- Added new Grok patterns to parse DHCP-related log messages.   
2023-12-19 |  Enhancement:  
\- Added a new Grok pattern to support new type of SYSLOG logs.  
\- Added new Grok patterns to parse `description`.  
\- Mapped `protocol`, `VrId`, `SlppRxVlan`, `SlppIncomingVlanId`, `Type`, `Cause` to `additional.fields`.  
\- Mapped `session_id` to `network.session_id`  
\- Mapped `SlppSrcMacAddress` to `principal.mac`.  
\- Mapped `intermediary_ip` to "intermediary.ip.  
\- Mapped `ver` to `metadata.version`.  
\- Mapped `rcPortVLacpAdminEnable`, `rcSyslogHostMapFatalSeverity`, `rcSyslogHostMapWarningSeverity`, `rcSyslogHostRowStatus`, `rcSyslogHostFacility`, `rcSyslogHostAddressType`, `rcSyslogHostMapErrorSeverity`, `rcSyslogHostMapInfoSeverity`, `rcSyslogHostSeverity`, `rcSyslogHostEnable` to `security_result.detection_fields`.  
\- Mapped `port` to `principal.port`.  
\- Mapped `rcSyslogHostAddress` to `principal.hostname`.   
2023-12-11 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
