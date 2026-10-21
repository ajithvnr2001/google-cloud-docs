---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pulse-secure-vpn-changelog/
title: Change log for PULSE_SECURE_VPN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:49:48.887934+00:00
---

# Change log for PULSE_SECURE_VPN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pulse-secure-vpn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PULSE_SECURE_VPN

Date | Changes  
---|---  
2025-12-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `req_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `req_host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `referrer_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `sr_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `server_name` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped `server_name` raw log field with `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- Updated a grok pattern to use DATA instead of GREEDYDATA for the username field to ensure correct field extraction.  
\- Added conditional check for message_info, rate_limiting_grok_failed, client_ip, req_host, and referrer_url.   
2024-09-24 |  Enhancement:  
\- Mapped `BLOCK` to `security_result.action` when `log_action` is equal to `rejected`.  
\- Mapped `prin_ip` to `principal.ip` and `principal.asset.ip`.  
\- Added a Grok pattern to parse unparsed syslog logs.   
2024-08-01 |  Enhancement:  
\- Mapped `Pulse Secure VPN` to `metadatda.product_name`.  
\- Added a Grok pattern to parse unparsed syslog logs.   
2024-05-27 |  Enhancement:  
\- Mapped `observer_hostname` to `observer.hostname`.  
\- When `dvc_hostname` is a valid IP address, then mapped it to `principal.ip`, else mapped it to `principal.hostname`.  
\- Mapped `priority_code`, `Syslog_version`, and `info_desc` to `about.labels`.  
\- Mapped `prod_name` to `metadata.product_event_type`.   
2024-04-16 |  Enhancement:  
\- Added a new GROK pattern to parse new pattern of SYSLOG logs.  
\- Mapped `connection_status` to `security_result.detection_fields`.   
2024-02-26 |  Enhancement:  
\- Added a `kv` block to parse key-value data.  
\- Mapped `username` to `target.user.userid`.  
\- Added conditional check for `message_info`.  
\- Mapped `u_prin_ip` to `principal.ip`.  
\- Mapped `u_observer_ip` to `observer.ip`.   
2023-11-07 |  Bug-fix:  
\- Modified mapping for `observer_host` from `observer.hostname` to `additional.fields`.   
2023-08-19 |  Enhancement:  
\- Added a Grok pattern to parse failing logs.   
2023-05-26 |  Enhancement:  
\- Added a Grok pattern to support the new syslog logs.   
2023-01-06 |  Enhancement:  
\- Modified grok to parse `product_type` and mapped to `metadata.product_event_type`.   
2022-10-25 |  Enhancement:  
\- Added new grok patterns for `message_info` to extract session_id.  
\- Mapped `session_id` to `network.session_id`.  
\- Changed target.ip to principal.ip when detect_policy_change_failed is false.  
\- Changed target.mac to principal.mac when detect_policy_change_failed is false.   
2022-10-12 |  Enhancement- Added mappings for following fields:  
\- Extracted the value of IP from `msg` field and mapped it to `principal.ip`.  
\- Extracted the value of hostname from `msg` field and mapped it to `principal.hostname`.  
\- Mapped `user` to `target.user.userid`.  
\- Mapped `realm` to `principal.group.attribute.labels`.  
\- Mapped `roles` to `principal.user.group_identifiers`.  
\- Modified value for `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED`.   
2022-10-03 |  Enhancement- Parsed the logs containing `sudo` and parsed them.  
Added Support for new Key-Value Pair type log formats.   
2022-07-01 |  Enhancement- Generated new event for EventID: 4624  
Changed metadata.event_type form `GENERIC_EVENT` to `STATUS_UPDATE` or `NETWORK_CONNECTION` where `principal.ip` or `target.ip` or `principal.hostname` are not null.   
2022-04-13 |  Enhancement-Added mappings for new fields in GENERIC_EVENT event_type:  
\- user_ip to event.idm.read_only_udm.principal.ip.  
\- user_group_identifier to event.idm.read_only_udm.target.user.group_identifiers.  
Modified timestamp in all the event_type to include timezone.  
Modified field user_ip, target_ip for GENERIC and NETWORK_CONNECTION event types.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
