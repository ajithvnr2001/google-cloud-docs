---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dns-changelog/
title: Change log for F5_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:09.894361+00:00
---

# Change log for F5_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_DNS

Date | Changes  
---|---  
2026-02-09 |  Enhancement:  
\- Added grok patterns to parse the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.network.dns.response_code`: Newly mapped `query_response_code` raw log field with `event.idm.read_only_udm.network.dns.response_code` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dns_flags` with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-09 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid : Newly Mapped `User` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- Added an IP validation before mapping `host` and `src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added a grok pattern to parse message with `rule_id_val`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `attemptCount` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `rule_id_val` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.   
2025-06-30 |  Enhancement:  
\- Added a grok pattern to parse new format of logs.  
\- event.idm.read_only_udm.principal.user.userid: Set `has_user` to `true` when `userName` raw field is mapped to`event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-06-27 |  Enhancement:  
\- Added grok patterns to retrieve dns data like `dns_name`, `dns_class`, `query_type`, `dnsAnswers`.  
\- `event.idm.read_only_udm.network.dns.question.type`: Newly mapped `query_type`, `record_type` raw log field with `event.idm.read_only_udm.question.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.question.class`: Newly mapped `dns_class` raw log field with `event.idm.read_only_udm.network.dns.question.class` UDM field.  
\- `event.idm.read_only_udm.network.dns.answer.data`: Newly mapped `intermediary_host` or `intermediary_ip` raw log field with `event.idm.read_only_udm.network.dns.answer.data` UDM field.  
\- `event.idm.read_only_udm.network.dns.answer.ttl`: Newly mapped `ttl_data` raw log field with `event.idm.read_only_udm.network.dns.answer.ttl` UDM field.  
\- `event.idm.read_only_udm.network.dns.answer.name`: Newly mapped `dns_answer_domain` raw log field with `event.idm.read_only_udm.network.dns.answer.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.answer.class`: Newly mapped `qclass` raw log field with `event.idm.read_only_udm.network.dns.answer.class` UDM field.  
\- `event.idm.read_only_udm.network.dns.question.name`: Newly mapped `dns_name` raw log field with `event.idm.read_only_udm.question.name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dest_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Updated the mapping of `event.idm.read_only_udm.additional.fields` to utilize a generalized map for fields `partition`, `tty`, `attempts`, `start`, and `end`.  
\- Added on_error for kv filter `kv_data`, `proto_version`, `application`, `userName`, `file_path`, `src_port`, and `desc`.  
\- Added conditional check for field `cmd_data`, `status`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.process.command_line`  
\- If url is not empty, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP`.  
\- If `has_principal` is `true` and has_question is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` and set `event.idm.read_only_udm.network.application_protocol` to `DNS`.  
\- If `has_principal` is `true` and has_target is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `has_user` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- If `has_principal` is `true` and has_target is false, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- If none of the above conditions are met, then set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2025-05-19 |  Enhancement:  
\- Added support for new pattern of SYSLOG + KV logs by adding a Grok pattern followed by a kv filter.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field and set `has_user` to `true`.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.ip` & `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to `true`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `partition`, `level`, `attempts`, `tty`, `start` and `end` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to: `USER_UNCATEGORIZED` if `has_user` is `true`, else `STATUS_UPDATE` if `has_principal` is `true`.  
\- Added null checks for `data12`, `action`, `desc_scriptd` and `file_path` fields before mapping their concatenation with `event.idm.read_only_udm.security_result.description` UDM field.  
\- Added a gsub block to parse logs where `application` is `httpd` and `msg3` is not null.   
2025-04-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `datetime` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-01-30 |  Enhancement:  
\- Added support to parse logs with `httpd` application.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
