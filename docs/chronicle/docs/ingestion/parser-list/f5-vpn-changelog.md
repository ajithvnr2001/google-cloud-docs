---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-vpn-changelog/
title: Change log for F5_VPN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:08.569143+00:00
---

# Change log for F5_VPN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-vpn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_VPN

Date | Changes  
---|---  
2026-09-25 |  Enhancement:  
\- Modified a grok pattern to parse the SYSLOG log fields.  
\- Added a grok pattern on `description` to extract `target_ip`, `id`, `type`, `tunnel_resource`, and `client_ip`.  
\- Added a grok pattern to parse `errdefs_msgno` and `assignment_type` from the raw log.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `errdefs_msgno` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `assignment_type` and `syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.type`: Removed the mapping of `file_path` raw log field from `event.idm.read_only_udm.principal.resource.type` since the UDM field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `file_path` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `client_ip` and `target_ip` are present, updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.   
2024-10-23 |  Enhancement:  
\- Added support for KV format.   
2024-05-20 |  Enhancement:  
\- Modified a Grok pattern to parse `principal.resource.name` correctly.  
\- Added a Grok pattern to parse `uid` and `sAmAccountName` and mapped to `target.hostname`.  
\- Mapped `Hostname` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `sess_id` to `network.session_id` for `SAML Agent` messages.   
2024-03-05 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.  
\- Mapped `internal_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `sess_id` to `network.session_id`.  
\- Mapped `file_path` to `principal.resource.name`.  
\- Mapped `useragent` to `network.http.user_agent`.  
\- Mapped `User-Agent` and `useragent` to `network.http.parsed_user_agent`.  
\- Mapped `username` to `target.user.userid`.  
\- Mapped `sid` to `target.user.windows_sid`.  
\- Mapped `bytes_out` to `network.sent_bytes`.  
\- Mapped `bytes_in` to `network.received_bytes`.  
\- Mapped `Platform` to `principal.platform`.  
\- Mapped `Platform_Version` to `principal.platform_version`.  
\- Mapped `Javascript_Support`, `ActiveX_Support`, `Plugin_Support`, `Version`, `Model`, `CPU`, `UI_Mode`, `SP`, `IDP`, `to_rule_item`, `from_rule_item`, `policy_result`, `rule`, `resource`, `ppp_id`, `tunnel_resource`, `server_vip_ip`, `server_vip_name`, and `Canonical_Info` to `additional.fields`.   
2022-07-22 |  Enhancement:  
\- Modified grok pattern to parse the date present in `RFC 3339` format.  
\- Added `gsub` to remove `/` from `resource_id`.   
2022-07-08 |  Enhancement:  
\- Mapped `uri_path` to `target.url`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `User-Agent` to `network.http.user_agent`.  
\- Mapped `s_ip` to `src.ip`.  
\- Mapped `t_ip` to `target.ip`.  
\- Mapped `t_port` to `target.port`.  
\- Mapped `s_nat_ip` to `target.nat_ip`.  
\- Mapped `ip_protocol` to `network.ip_protocol`.  
\- Mapped `descrip` to `security_result.description`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `command` to `target.process.command_line`.  
When `application` is equal to `logger`  
\- Mapped `cipher_name` to `network.tls.cipher`.  
\- Mapped `tls_version` to `network.tls.version`.  
\- Mapped `resource_id` to `target.resource.id`  
\- Mapped `src_ip` to `principal.ip`.  
\- Mapped `url` to `network.http.referral_url`.  
\- Mapped `status` to `network.http.response_code`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
