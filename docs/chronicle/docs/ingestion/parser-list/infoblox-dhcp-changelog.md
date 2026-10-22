---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dhcp-changelog/
title: Change log for INFOBLOX_DHCP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:42.892545+00:00
---

# Change log for INFOBLOX_DHCP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dhcp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for INFOBLOX_DHCP

Date | Changes  
---|---  
2026-07-30 |  Enhancement:  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Removed mapping of the log field originally named `target_mac` (which has been renamed now to `principal_mac` in the grok pattern) from the `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM fields as the mac represents the client mac.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `principal_mac` log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of the log field originally named `target_ip` (which has been renamed now to `prin_ip` in the grok pattern) from the `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields as it represents the Infoblox device IP.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `prin_ip` log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`: Newly mapped `principal_mac` raw log field with `event.idm.read_only_udm.network.dhcp.chaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.client_hostname`: Mapped `client_Hostname` raw log field with `event.idm.read_only_udm.network.dhcp.client_hostname` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.type`: Mapped `prod_type` to `event.idm.read_only_udm.network.dhcp.type` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.ciaddr`: When `dhcp_type` is RELEASE, REQUEST or INFORM, set the value of `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field with `prin_ip` log field.  
\- `event.idm.read_only_udm.network.dhcp.yiaddr`: When `dhcp_type` is ACK or OFFER, set the value of `event.idm.read_only_udm.network.dhcp.yiaddr` UDM field with `prin_ip` log field.   
2026-07-24 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `syslogHost` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields for `DHCPACK` events since the value in it represents the Infoblox device IP and not the target IP.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `syslogHost` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `clientIp` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields for `DHCPACK` events since this does not represent the device ip for `DHCPACK` events.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `clientIp` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields for `DHCPACK` events.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Mapped `clientIp` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields for `DHCPNAK` events when the process is `dhcpd`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `uid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-09 |  Enhancement:  
\- Added a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `client_Hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.dhcp.lease_time_seconds`: Newly mapped `lease_lifetime` raw log field with `event.idm.read_only_udm.network.dhcp.lease_time_seconds` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `prod_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `internal_ts`, `syslog_priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `process` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field when `process` is `dhcp`.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP` when `process` is `dhcp` and principal machine data is present and target machine data is present and DHCP details are present else if setting to `NETWORK_CONNECTION` when `process` is `dhcp` and principal machine data and target IP are present else if setting to `STATUS_UPDATE` when `process` is `dhcp` and principal machine data is present else setting to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.principal.asset.software.name`: Newly mapped `software_name` raw log field with `event.idm.read_only_udm.principal.asset.software.name` UDM field.   
2026-06-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of the log field originally named `host_name` (which has been renamed to `dns_zone` in the grok pattern) from the `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, as this field represents the DNS server name.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `dns_zone` log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Removed mapping of `clientHostname` log field from `event.idm.read_only_udm.observer.hostname` UDM field. As this represents client details which should primarily be in the `principal` noun, where it is already being mapped, making the `observer` mapping redundant.  
\- `event.idm.read_only_udm.observer.ip`: Removed mapping of `clientIp` log field from `event.idm.read_only_udm.observer.ip` UDM field. As this field represents client details which should primarily be in the `principal` noun, where it is already being mapped, making the `observer` mapping redundant.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping for `syslogHost` log field from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields when message contains `bind update`. As these events, `syslogHost` identifies the Infoblox device reporting the log, which is acting as an intermediary, not the target of the reported action.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `syslogHost` log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Set the value of `event.idm.read_only_udm.security_result.action` UDM field based on the value of `description` field in the log.  
\- `event.idm.read_only_udm.target.asset.ip`: Mapped `syslogHost` log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `dnsDomain` log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_details` log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set the `event_type` to `NETWORK_CONNECTION` when the log has both principal and target machine data.   
2025-09-01 |  Enhancement:  
\- Modified the grok pattern to parse `clientHostname` properly.  
\- event.idm.read_only_udm.network_dhcp.client_identifier: Newly mapped `uid` raw log field with `event.idm.read_only_udm.network_dhcp.client_identifier` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `process` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `status_msg` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added gsub to replace `\r\n` with an empty string.   
2025-08-19 |  Enhancement:  
\- Added a Grok pattern to parse new format of log.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname and event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.mac: Newly mapped `target_mac` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- event.idm.read_only_udm.observer.ip and event.idm.read_only_udm.observer.hostname: If `observerdata` raw log field has IP value then mapped with `event.idm.read_only_udm.observer.ip` UDM field else mapped `observerdata` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- Declared `principal_port` to null in statedata.  
\- Added condition check for `network_dhcp.type` to `ACK` when `clientMac` is not empty.  
\- Added a Grok pattern to parse `clientMac` properly.  
\- Added condition check for `event_type` to `NETWORK_DHCP` when `clientMac` is not empty or `clientIp` is not empty or `dhcpServerIp` is not empty.  
\- Added condition check for `event_type` to `STATUS_UPDATE` when `clientHostname` is not empty or `clientIp` is not empty.   
2025-07-18 |  Enhancement:  
\- Added grok patterns to parse new format of logs.  
\- event.idm.read_only_udm.network_dhcp.client_hostname : Newly mapped `clientHostname` raw log field with `event.idm.read_only_udm.network_dhcp.client_hostname` UDM field when `eventType` is `DHCPREQUEST`, `REQUEST`, `r-l-e` or `BOOTREQUEST`.  
\- event.idm.read_only_udm.network_dhcp.ciaddr : Newly mapped `clientIp` raw log field with `event.idm.read_only_udm.network_dhcp.ciaddr` UDM field when `eventType` is `DHCPACK` or `DHCPOFFER`.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname, event.idm.read_only_udm.network_dhcp.client_hostname : Newly mapped `clientHostname` raw log field with `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname` and `event.idm.read_only_udm.network_dhcp.client_hostname` UDM field when `eventType` is `DHCPDISCOVER`, `DHCPDECLINE` or `DISCOVER`.  
\- event.idm.read_only_udm.observer.ip : Newly mapped `observer_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field when `eventType` is `reverse map`, `forward map`, `Forward map` or `Reverse map`.   
2025-06-04 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `syslogHost` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field when eventType is `DHCPREQUEST`, `DHCPDISCOVER`, `DHCPEXPIRE`, `DHCPDECLINE`, `DHCPINFORM`, `DHCPNAK`, `DHCPRELEASE`.  
\- event.idm.read_only_udm.network_dhcp.giaddr: Newly mapped `dhcpServerIp` raw log field with `event.idm.read_only_udm.network_dhcp.giaddr` UDM field when eventType is `DHCPDISCOVER`, `DHCPDECLINE`, `DHCPINFORM`, `DHCPNAK`, `DHCPRELEASE`.  
\- event.idm.read_only_udm.network_dhcp.ciaddr: Newly mapped `clientIp` raw log field with `event.idm.read_only_udm.network_dhcp.ciaddr` UDM field when eventType is `DHCPEXPIRE`, `DHCPDECLINE`, `DHCPNAK`.  
\- event.idm.read_only_udm.network_dhcp.chaddr: Newly mapped `clientMac` raw log field with `event.idm.read_only_udm.network_dhcp.chaddr` UDM field when eventType is `DHCPDECLINE`, `DHCPNAK`.  
\- event.idm.read_only_udm.target.port: Newly mapped `targetport` raw log field with `event.idm.read_only_udm.target.port` UDM field when eventType is `reverse map`.   
2025-03-03 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `syslogIp` from `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Removed mapping of `syslogHost` from `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Removed mapping of `syslogHost` from `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `syslogHost` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.network.dhcp.ciaddr: Removed mapping of `clientIp` from `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed mapping of `clientHostname` from `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped of `dhcpServerIp` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Removed mapping of `clientIp` from `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.observer.ip: Removed mapping of `clientIp` from `event.idm.read_only_udm.observer.ip` UDM field.   
2024-10-17 |  Enhancement:  
\- Mapped `clientIp` to `network_dhcp.ciaddr` for DHCPOFFER and DHCPINFORM logs.   
2024-04-19 |  Enhancement:  
\- Added conditional check for `dhcpServerIp`.  
\- Mapped `syslogIp` to `network_dhcp.ciaddr`.   
2024-01-10 |  \- Mapped `status` to `additional.fields`.   
2023-04-26 |  \- Reverted a previous check-in as it was breaking DHCP aliasing   
2022-08-05 |  \- Modified `event_type` from `GENERIC_EVENT` to `USER_RESOURCE_ACCESS` to reduce generic percentage.   
2022-07-06 |  Enhancement:  
\- Handled the dropped logs and mapped them to valid event_types.  
\- Dropped logs had following eventType, which are now handled:  
`forward map`, `Reverse`, `Forward`, `Removed`, `Processed`, `Dynamic`, `Lease`, `Unable`, `reverse map`, `bind`, `map update`, `parse_option_buffer`, `Added`,`DDNS`, `ICMP`,`update-security` ,`update`,`notify`,`general`,`LPF`, `Sending`.  
\- Also, following `process` were dropped earlier are now handled:  
`netauto_discovery`, `ntpd`.  
\- Other condition checks like `msg1` containing `DNS update latency|pool|syslog|declaration|write|Consortium|reserved|duplicate|leases|visit|disconnected` are handled.  
\- Added new code block to handle `forward map` and `reverse map` and made them parse.  
\- Changed event type from `GENERIC_EVENT` to `STATUS_UPDATE` wherever possible.   
2022-04-13 |  Newly created default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
