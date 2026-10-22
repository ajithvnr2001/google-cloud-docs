---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mikrotik-router-changelog/
title: Change log for MIKROTIK_ROUTER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:42.496625+00:00
---

# Change log for MIKROTIK_ROUTER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mikrotik-router-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MIKROTIK_ROUTER

Date | Changes  
---|---  
2025-09-09 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `dvchost` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `dvc` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `dvchost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `dvc` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP` if the `vlan` field is not empty and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP` if the `message` field contains `dhcp` and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` if the `proto` field is `UDP`, the `dpt` field is `53`, and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DHCP` if the `message` field contains `dhcp`, the `has_dhcp` field is true, and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` if the `has_target` field is true and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_UNCATEGORIZED` if the `target_addr` field is not empty, and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` if a DNS question is parsed and the `has_principal` field is true.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` in the fallback section if the `has_target_user` field is true; otherwise, it defaults to GENERIC_EVENT.   
2025-08-19 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`:Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.hostname`:Newly mapped `dvchost` raw log field to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`:Newly mapped `dvchost` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.application`:Newly mapped `app` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.application`:Newly mapped `application_name` raw log field (from msg) to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`:Newly mapped `duser` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`:Newly mapped `username` raw log field (from msg) to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`:Newly mapped `src_ip` raw log field (from KV) to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`:Newly mapped `srcip` raw log field (from msg) to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`:Newly mapped dvc `raw log` field to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`:Newly mapped dstip `raw log` field (from msg) to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`:Newly mapped tar_ip `raw log` field (from msg) to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.description`:Newly mapped `msg` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.ciaddr`:Newly mapped `ciaddr` raw log field (from msg) to `event.idm.read_only_udm.network.dhcp.ciaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.chaddr`:Newly mapped `chaddr` raw log field (from msg) to `event.idm.read_only_udm.network.dhcp.chaddr` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.client_hostname`:Newly mapped `dhcp_hostname` raw log field (from msg) to `event.idm.read_only_udm.network.dhcp.client_hostname` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.yiaddr`:Newly mapped `yiaddr` raw log field (from msg) to `event.idm.read_only_udm.network.dhcp.yiaddr` UDM field.  
\- `event.idm.read_only_udm.principal.mac`:Newly mapped `smac` raw log field (from msg) to `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.network.dhcp.siaddr`:Newly mapped `siaddr` raw log field (from msg) to `event.idm.read_only_udm.network.dhcp.siaddr` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`:Newly mapped `srcip` raw log field (from msg) to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`:Newly mapped `dstip` raw log field (from msg) to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.dns.id`:Newly mapped `dns_id` raw log field (from msg) to `event.idm.read_only_udm.network.dns.id` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions[0].name`:Newly mapped `question_name` raw log field (from msg) to `event.idm.read_only_udm.network.dns.questions[0].name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`:Newly mapped `outcome` (key `Outcome`), in (key `in`), out (key `out`), packet_mark (key `packet_mark`), connection_mark (key `connection_mark`), param_list (key `param_list`), max_dhcp_message_size (key `max_dhcp_message_size`), client_id (key `client_id`), action_id (key `action_id`), add_time (key `add_time`) raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.port`:Renamed from `srcport` to `event.idm.read_only_udm.principal.port`.  
\- `event.idm.read_only_udm.target.port`:Renamed from `dstport` to `event.idm.read_only_udm.target.port`.  
\- Added grok patterns to parse msg field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- If msg contains `logged in`, updated to USER_LOGIN.  
\- If msg contains `logged out`, updated to USER_LOGOUT.  
\- If message contains `dns` and has_dns is `true`, updated to NETWORK_DNS.  
\- If message contains `dhcp` and has_dhcp is `true`, updated to NETWORK_DHCP.  
\- If has_target is `true` and not previously set, updated to NETWORK_CONNECTION.  
\- Added support for parsing CEF formatted logs.  
\- Added KV filter to parse key-value pairs from the kv_data field extracted from CEF.  
\- Added gsub to rename src to src_ip in kv_data before KV processing.  
\- Added gsub to rename dst to dst_ip in kv_data before KV processing.   
2025-02-25 |  Enhancement:  
\- Added `gsub` to parse valid `client_mac` to `principal.mac`.   
2025-02-07 |  Enhancement:  
\- Changed `WORD` to `DATA` in the Grok pattern.   
2025-01-21 |  Enhancement:  
\- Mapped `metadata.event_type` to `NETWORK_DHCP` for DHCP logs.  
\- Mapped `client_mac` to `principal.mac`.  
\- When `details` has `assigned`, then mapped `network.dhcp.type` to `ACK`.  
\- When `details` has `deassigned`, then mapped `network.dhcp.type` to `RELEASE`.  
\- When `details` has `request`, then mapped `network.dhcp.type` to `REQUEST`.  
\- When `details` has `offer`, then mapped `network.dhcp.type` to `OFFER`.   
2025-01-20 |  Enhancement:  
\- Modified the Grok pattern to parse `intermediary.hostname` data.   
2024-12-18 |  Enhancement:  
\- Added support for new format of syslog logs.   
2024-11-26 |  Enhancement:  
\- Modified the Grok pattern to remove `period` from the data.  
\- Mapped `server_name` to `target.hostname` and "target.asset.   
2024-11-15 |  Enhancement:  
\- Mapped `action` to `security_result.action`.   
2024-09-30 |  \- Changed mapping for `username` from `principal.user.userid`, `src.user.userid` to `target.user.userid`.  
\- For the login event, mapped `metadata.event_type` to `USER_LOGIN`.  
\- For the logout event, mapped `metadata.event_type` to `USER_LOGOUT`.  
\- Mapped `application` to `target.application`.  
\- Mapped `bytes_in` to `network.received_bytes`.  
\- Mapped `bytes_out` to `network.sent_bytes`.  
\- Mapped `connection_time_in_seconds`, `packets_in` and `packets_out` to `security_result.detection_fields`.   
2024-05-28 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
