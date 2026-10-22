---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pfsense-changelog/
title: Change log for PFSENSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:43.327852+00:00
---

# Change log for PFSENSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pfsense-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PFSENSE

Date | Changes  
---|---  
2025-07-18 |  Enhancement:  
\- Added grok patterns to parse retrieve relevant fields.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `user_agent` raw log field to event.idm.read_only_udm.network.http.user_agent.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped from the `user_agent` field after parsing.  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed `host` raw log field from event.idm.read_only_udm.principal.asset.hostname because host here is name of network device. So, mapping it to event.idm.read_only_udm.principal.asset.hostname is not suitable.  
\- event.idm.read_only_udm.principal.hostname: Removed `host` raw log field from event.idm.read_only_udm.principal.hostname because host here is name of network device. So, mapping it to event.idm.read_only_udm.principal.hostname is not suitable.  
\- If event.idm.read_only_udm.metadata.event_type is equal to PROCESS_LAUNCH then mapped `host` to event.idm.read_only_udm.principal.asset.hostname and event.idm.read_only_udm.principal.hostname.   
2025-03-20 |  Enhancement:  
\- Mapped `host` to `intermediary.hostname`.  
\- Mapped `pid` to `intermediary.process.pid` and `principal.process.pid`.  
\- Mapped `application` to `intermediary.application`.  
\- Removed mapping for `command` to `principal.process.command_line` and mapped it to `target.process.command_line`.  
\- Set `metadata.event_type` as `PROCESS_LAUNCH` when `target.process.command_line` is available.  
\- Removed mapping of `principal.user.userid` and mapped it to `target.user.userid` for User Login events.  
\- Mapped `ipv4` and `ipv6` to `principal.ip` and `principal.asset.ip` if they are valid IPs.  
\- Mapped `security_result.category` to `AUTH_VIOLATION` if `description` has `could not authenticate`.  
\- Added support for http events.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `referer` to `network.http.referral_url`.  
\- Mapped `response_code` to `network.http.response_code`.  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `sent_bytes` to `network.sent_bytes`.  
\- Mapped `url` to `target.url`.  
\- Mapped `http_version` to `additional.fields`.  
\- Mapped `host` to `target.host` for http events.   
2024-10-11 |  Enhancement:  
\- Added support for a new pattern of syslog logs.   
2024-05-08 |  Enhancement:  
\- Added Grok patterns to parse field `description`.  
\- Mapped `principal_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `compression_algo` to `additional.fields`.  
\- Mapped `status` to `security_result.detection_fields`.  
\- Mapped `principal_username` to `principal.user.userid`.  
\- Mapped `target_host` to `target.hostname` and `target.asset.hostname`.   
2023-05-05 |  Enhancement:  
\- Added convert to uppercase before mapping `network.ip_protocol`.  
\- Mapped `column18` to `principal.port` when protocol is present in `column13`.  
\- Mapped `column19` to `target.port` when protocol is present in `column13`.  
\- Mapped `column20` to `additional.fields` as `data-length` when protocol is present in `column13`.   
2023-02-20 |  Enhancement:  
\- Added Grok pattern to support new filter-log format and syslog-ng format.   
2022-10-04 |  Enhancement:  
\- Remapped firewall device name to intermediary.hostname instead of principal.hostname for logs where event_types is `NETWORK_CONNECTION`.   
2022-09-05 |  Enhancement-  
\- for csv format logs mapped following fields.  
\- Added grok pattern to retrieve `IP` and `MAC`.  
\- Mapped `column19` which is `source-address` to `network.dhcp.yiaddr`.  
\- Mapped `security_result.action` to `ALLOW` when `column7` is equal to `pass`.  
\- When `column9` is equal to `6` which indicates `IPV6`, then following fields are mapped:  
\- Mapped `column17` which is `destination-address` to `target.ip`.  
\- Mapped `column16` which is `source-address` to `principal.ip`.  
\- Mapped `event_type` to `NETWORK_CONNECTION` when `column16` and `column17` is not null.  
\- Mapped `column12` which is `hop_limit` to `additional.fields`.  
\- Mapped `column13` which is `ip_protocol` to `network.ip_protocol`.  
\- Migrated the custom parsers into default parser.  
\- Added conditional check to set `event_type` to `STATUS_UPDATE`  
2022-06-30 |  Enhancement:  
\- Mapped `ttl` to `additional.fields`.  
\- Mapped `Id` to `additional.fields`.  
\- Mapped `Offset` to `additional.fields`.  
\- Mapped `Data length` to `additional.fields`.  
\- Mapped `Length` to `additional.fields`.  
\- Mapped `Sequence-number` to `additional.fields`.   
2022-04-11 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
