---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonic-firewall-changelog/
title: Change log for SONIC_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:21:46.689412+00:00
---

# Change log for SONIC_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sonic-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SONIC_FIREWALL

Date | Changes  
---|---  
2026-07-21 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support globally to map `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-04-15 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `op` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `appName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `srcZone` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `dstZone` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `code` and `change` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `app` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.   
2025-11-07 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Network_data`, `dpi` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `src_interface` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `dst_interface` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `syslog_priority` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `net_application` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field when it matches a list of standard protocols.   
2025-04-16 |  Enhancement:  
\- Added support to remove UTF-8 characters from `appid` field.  
\- `event.idm.read_only_udm.security_result.rule_id` \- Newly Mapped `appid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM Field.  
\- `event.idm.read_only_udm.security_result.summary` \- Newly Mapped `appcat` raw log field with `event.idm.read_only_udm.security_result.summary` UDM Field.   
2025-02-06 |  Enhancement:  
\- Changed `fw` mapping from `principal.ip` to `intermediary.ip`.   
2025-01-07 |  Enhancement:  
\- Added support for unparsed logs.   
2024-11-05 |  Enhancement:  
\- Mapped `firewall_serial_number` to `intermediary.asset_id` and `firewall_hostname` to `intermediary.hostname`.   
2024-09-05 |  Enhancement:  
\- If `fw_action` is equal to `NA`, then changed the mapping of `security_result.action` from `UNKNOWN_ACTION` to `BLOCK`.   
2024-06-06 |  Enhancement:  
\- Mapped the `C` field to `additional.fields`.  
\- Mapped the `gcat` field to `additional.fields`.  
\- Mapped `note` to `additional.fields`.  
\- Mapped `n` to `additional.fields`.  
\- Mapped `vpnpolicyDst` to `additional.fields`.  
\- Mapped `FileId` to `additional.fields`.  
\- Mapped `dur` to `additional.fields`.  
\- Mapped `m` to `additional.fields`.   
2024-06-04 |  Enhancement:  
\- Removed alignment of `principal.asset.ip` and `target.asset.ip`.  
\- If the IP value is in range-format, then `src` and `dst` are mapped to `additional.fields`.  
\- Mapped `gw` to `intermediary.ip`.   
2024-05-29 |  Enhancement:  
\- Mapped `firewall_hostname` to `intermediary.hostname`.  
\- Modified the Grok pattern to parse the field `sn`.  
\- Mapped `sn` to `intermediary.asset_id`.   
2024-04-18 |  Enhancement:  
\- Changed the mapping of `fw` from `observer.ip` to `principal.ip`.  
\- Changed the mapping of `id` from `resource.id` to `principal.hostname`.   
2023-05-26 |  Enhancement -  
\- Mapped `fw_action` to `security_result.action_details`.  
\- Mapped `spkt` to `network.sent_packets`.   
2023-03-08 |  Enhancement -  
\- Added a condition check to `User` field to parse the appropriate field (i.e. principal.user.email_addresses or principal.user.user_display_name or principal.user.userid).  
\- Removed `pri` from `security_result.detection_fields` and mapped it to `security_result.severity`.  
\- Mapped `usr` to `principal.user.email_addresses`.  
\- Mapped `vpnpolicy` field to `security_result.detection_fields`.  
\- Mapped `cdur` field to `security_result.detection_fields`.  
\- Mapped `sess` field to `security_result.detection_fields`.   
2023-03-06 |  Enhancement -  
\- Mapped `fw` to `observer.ip` instead of target.ip.   
2023-02-22 |  Enhancement -  
\- Events are parsing traffic as `NETWORK_HTTP` are mapped to `NETWORK_CONNECTION` instead, when the protocol is not HTTP.  
\- Mapped `msg` to `security_result.summary` where `fw_action` is equal to `drop` Mapped `BLOCK` to `security_result.action`.  
\- Mapped `fw` to `observer.ip` and `src` to `principal.ip`.   
2022-06-24 |  Enhancement -  
\- Mapped `msg` to `security_result.summary`.  
\- Where `fw_action` is equal to `drop` Mapped `BLOCK` to `security_result.action`.  
\- Mapped `sent` to `network.sent_bytes`.  
\- Mapped `rcvd` to `network.received_bytes`.  
\- Mapped `usr` to `principal.user.userid`.  
\- Mapped `pri` to `additional.fields`.  
\- Mapped `sn` to `additional.fields`.  
\- Mapped `id` to `target.resource.id`.   
2022-05-26 |  Bug fix-  
Mapped duration to network.session_duration.seconds.  
Mapped user to principal.user.userid.  
Mapped agent to network.http.user_agent.  
Mapped avgThroughput to target.resource.attribute.labels.  
Mapped bytesIn to network.sent_bytes.  
Mapped bytesOut to network.received_bytes.  
Mapped bytesTotal to target.resource.attribute.labels.  
Mapped maxThroughput to target.resource.attribute.labels.  
Mapped dst to target.ip.  
Mapped fw to principal.ip.  
Mapped pri to event.idm.read_only_udm.additional.fields.   
2022-05-19 |  Enhancement - Converted parser from SDM to UDM (changed mapping from webproxy fields to event fields).   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
