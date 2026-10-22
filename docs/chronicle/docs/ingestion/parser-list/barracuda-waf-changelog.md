---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-waf-changelog/
title: Change log for BARRACUDA_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:33.220826+00:00
---

# Change log for BARRACUDA_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BARRACUDA_WAF

Date | Changes  
---|---  
2026-06-29 |  Enhancement:  
\- Added a Grok pattern to parse new format of SYSLOG logs.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `protocolAndVersion` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `target_port_2` and `ReqClientId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `rule`, `sessionNavTourCookie` and `auth_type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip_2` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.   
2026-06-26 |  Enhancement:  
\- Added and Updated a Grok pattern to parse new format of SYSLOG + CSV raw logs.  
-`event.idm.read_only_udm.security_result.severity`: Updated mapping of `severity` raw log field from `INFORMATIONAL` to `MEDIUM` when the value is `WARN`. because in `BARRACUDA_WAF` `WARN` indicates severity `MEDIUM`.  
-`event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `pattern`, `token` and `type` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
-`event.idm.read_only_udm.additional.fields`: Newly mapped `FromValue`, `FromValue1`, `remember_me`, `timeTakenMS`, `Cookie` ,`followAction` and `avsession` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-09 |  Enhancement:  
\- Added a Grok pattern to parse new format of SYSLOG + CSV raw logs.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `appProtocol` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field   
2026-05-15 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Updated the value of `event.idm.read_only_udm.metadata.product_name` from `LEEF` to `BARRACUDA_WAF`.  
\- `event.idm.read_only_udm.intermediary.hostname`, `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`, `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `intermediary_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `intermediary_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_name`: Newly mapped `attackType` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `policy_scope` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `network_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- Added a grok pattern to parse the new pattern of syslog logs.   
2025-11-26 |  Enhancement:  
\- Added support for LEEF format.  
\- Added support for an additional Syslog format.  
\- Added logic to set event.idm.read_only_udm.security_result.severity based on the raw logLevel field.  
\- Refactored parser logic to support the additional log formats.  
\- Modified drop logic to only tag as TAG_MALFORMED_MESSAGE if all parsing attempts (JSON, LEEF, and other Grok patterns) fail.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `rt` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `evId` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg` raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to event.idm.read_only_udm.metadata.product_version.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logType`, `modName`, `log_Type`, `vendor`, `product`, `event_type`, `device_version`, `timeTaken`, `serverTime` and `subcomponent` raw log fields to event.idm.read_only_udm.additional.fields.   
2025-07-22 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host` raw log field to event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `_time` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `recid` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `host_ip` raw log field to event.idm.read_only_udm.intermediary.ip and event.idm.read_only_udm.intermediary.asset.ip.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `cribl_processing_time` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cribl_wp_id`, `logType`, `timeTaken` and `query` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `_raw` raw log field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `time` raw log field to event.idm.read_only_udm.security_result.first_discovered_time.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src` raw log field to event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.principal.port: Newly mapped `srcPort` raw log field to event.idm.read_only_udm.principal.port.  
\- event.idm.read_only_udm.target.ip: Newly mapped `dst` raw log field to event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.target.port: Newly mapped `dstPort` raw log field to event.idm.read_only_udm.target.port.  
\- event.idm.read_only_udm.target.url: Newly mapped `url` raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `srcBytes` raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `dstBytes` raw log field to event.idm.read_only_udm.network.received_bytes.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `proto` raw log field to event.idm.read_only_udm.network.tls.version.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `httpStatus` raw log field to event.idm.read_only_udm.network.http.response_code.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referer` raw log field to event.idm.read_only_udm.network.http.referral_url.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `hostname_1` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `hostname_1` raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `httpVersion` raw log field to event.idm.read_only_udm.network.application_protocol_version.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `usrName` raw log field to event.idm.read_only_udm.network.http.user_agent.  
\- Set event.idm.read_only_udm.metadata.product_name to LEEF and event.idm.read_only_udm.metadata.product_event_type to WAF for JSON-based logs.  
\- Added logic to merge security_result into event.idm.read_only_udm.security_result.   
2025-02-10 |  Enhancement:  
\- Mapped `inter_host` to `null` if it is not present in the log.   
2025-01-16 |  Enhancement:  
\- Added a Grok pattern to support new format of syslog logs.  
\- Mapped `inter_host` to `intermediary.hostname`.   
2024-11-19 |  Enhancement:  
\- Added support for CEF format logs.   
2024-11-18 |  Enhancement:  
\- Removed unnecessary drop condition to fix the parsing issue.   
2024-09-25 |  Enhancement:  
\- Added support for a new pattern of SYSLOG logs.   
2024-09-05 |  Enhancement:  
\- Added support for a new pattern of SYSLOG logs.   
2023-07-19 |  Bug-Fix:  
-Parsed uparsed raw logs using a Grok pattern.  
-Mapped `server` to `target.ip`.   
2022-09-09 |  Enhancement: Created a default parser and Migrated the custom parsers into default parser.  
The following fields are mapped:  
\- `duser` mapped to `target.user.user_display_name`.  
\- `suser` mapped to `.principal.user.user_display_name`.  
\- `suid` mapped to `principal.user.userid`.  
\- `src` mapped to `principal.ip`.  
\- `dst` mapped to `target.ip`.  
\- `shost` mapped to `principal.hostname`.  
\- `severity` mapped to `security_result.severity`.  
\- `action` mapped to `security_result.action`.  
\- `user_name` mapped to `target.user.userid`.  
\- `domain_name` mapped to `target.domain.name`.  
\- `mac_address` mapped to `principal.mac`.  
\- `direction` mapped to `network.direction`.  
\- `ip_protocol` mapped to `network.ip_protocol`.  
\- `summary` mapped to `security_result.summary`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
