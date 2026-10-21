---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mx-changelog/
title: Change log for JUNIPER_MX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:20:38.704636+00:00
---

# Change log for JUNIPER_MX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-mx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUNIPER_MX

Date | Changes  
---|---  
2025-11-18 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Newly mapped `destination_address` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `destination_address` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_address` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_address` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `source_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `destination_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `ip_protocol_out (derived from ip_protocol)` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.outcomes: Newly mapped `outcome` raw log field with `event.idm.read_only_udm.security_result.outcomes` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `exe`,`key`,`node`, `permitted`, `router`, `ingress_interface`, `collector_id`, `arch`, `syscall`, `exit`, `a0`, `a1`, `a2`, `a3`, `items`, `auid`, `uid`, `gid`, `euid`, `suid`, `fsuid`, `egid`, `sgid`, `fsgid`, `tty`, `ses`, `old_time`, `new_time` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `subtype`, `type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added `UNIX` to the date match patterns for `date_time` field.  
\- Added a new grok pattern to parse logs and extract fields like `intermediary_hostname` and `kv_data_1`.  
\- Added null conditional check for `host`.  
\- event.idm.read_only_udm.principal.process.parent_pid: Newly mapped `ppid` raw log field(s) with `event.idm.read_only_udm.principal.process.parent_pid` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `comm` raw log field(s) with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-01-15 |  Enhancement:  
\- Mapped hostname to `principal.hostname`.  
\- Added new Grok patterns to parse a new pattern of syslogs.   
2024-10-24 |  Enhancement:  
\- Added new Grok patterns to parse a new pattern of SYSLOGS.   
2024-07-02 |  Enhancement:  
\- Added new Grok patterns to parse a new pattern of SYSLOGS.   
2024-04-15 |  Enhancement:  
\- Added new Grok patterns to handle a new pattern of SYSLOG logs.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- When `metadata.event_type` is `GENERIC_EVENT`, and `src_ip` and `dest_ip` is not empty, then set `metadata.event_type` to `NETWORK_CONNECTION`.  
\- When `metadata.event_type` is `GENERIC_EVENT`, and `src_ip` is not empty, then set `metadata.event_type` to `STATUS_UPDATE`.   
2023-11-26 |  Enhancement:  
\- Mapped host sending logs to `intermediary.hostname` instead of `principal.hostname`.  
\- Parsed event_type `SSHD_LOGIN_FAILED` and mapped `metadata.event_type` to `USER_LOGIN`.  
\- Changed and mapped more appropriate "metadata.event_type' wherever possible.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
