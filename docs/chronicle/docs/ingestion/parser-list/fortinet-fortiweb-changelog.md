---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiweb-changelog/
title: Change log for FORTINET_FORTIWEB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:44.232642+00:00
---

# Change log for FORTINET_FORTIWEB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortiweb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FORTIWEB

Date | Changes  
---|---  
2026-08-06 |  Enhancement:  
\- Added grok pattern to parse new format of logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `date_time` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `main_type`, `owasp_top10` and `signature_cve_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `length` and `syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `threat_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2026-06-12 |  Enhancement:  
\- Added support for integer values in `proto` raw log field.   
2026-06-01 |  Enhancement:  
`event.idm.read_only_udm.principal.nat_ip`, `event.idm.read_only_udm.principal.asset.nat_ip`: Newly mapped `trans_src` raw log field with `event.idm.read_only_udm.principal.nat_ip` and `event.idm.read_only_udm.principal.asset.nat_ip` UDM fields.  
`event.idm.read_only_udm.network.received_bytes`: Newly mapped `ibytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
`event.idm.read_only_udm.network.sent_bytes`: Newly mapped `obytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
`event.idm.read_only_udm.principal.nat_port`: Newly mapped `trans_src_port` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
`event.idm.read_only_udm.security_result.about.resource.name`: Newly mapped `real_server` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `http_cookie` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
`event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dstcountry` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
`event.idm.read_only_udm.target.nat_port`: Newly mapped `trans_dst_port` raw log field with `event.idm.read_only_udm.target.nat_port` UDM field.  
`event.idm.read_only_udm.target.nat_ip`, `event.idm.read_only_udm.target.asset.nat_ip`: Newly mapped `trans_dst` raw log field with `event.idm.read_only_udm.target.nat_ip` and `event.idm.read_only_udm.target.asset.nat_ip` UDM fields.  
`event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when principal machine data, target machine data and network application protocol is set to HTTP.   
2026-01-05 |  Enhancement:  
\- event.idm.read_only_udm.target.url: Newly mapped `http_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `timezone` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-07-02 |  Enhancement:  
\- Added gsub function on `eventtime` to truncate it to 13 digits for correct parsing.  
\- event1.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventtime` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `http_request_time`, `http_response_time` and `subtype` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event1.idm.read_only_udm.principal.ip , event1.idm.read_only_udm.principal.asset.ip: Newly mapped `original_src` raw log field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-06-05 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field when `action` in `login` or `edit`.  
\- Set `sec_result` as BLOCK when action is `Deny`.  
\- Modified conditional check for `sub_type` udm field.   
2025-05-28 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `action` in `login` or `edit`.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `attack_type` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field when `type` is `attack`.  
\- Modified null check conditions for `signature_subclass` and `signature_id`.   
2025-05-21 |  Enhancement:  
\- Added `gsub` for to convert `iframe src` to `iframe_src` to fix log parsing errors.  
\- Added IP Validation to parse the IP address from `src` raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `matched_pattern` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-02-06 |  Enhancement:  
-Changed `devname` mapping from `principal.resource.name` to `intermediary.hostname`.   
2024-09-30 |  Enhancement:  
\- Added support to parse the new format of unparsed KV logs.   
2024-01-09 |  \- Added support for CEF format logs.  
\- Added a Grok pattern to match new format of CEF logs.  
\- Mapped `principal_hostnamne` to `principal.hostname`.  
\- Mapped `principal.app` to `principal.application`.   
2023-05-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
