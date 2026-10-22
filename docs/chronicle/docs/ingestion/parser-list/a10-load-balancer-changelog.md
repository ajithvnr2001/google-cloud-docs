---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/a10-load-balancer-changelog/
title: Change log for A10_LOAD_BALANCER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:44.510850+00:00
---

# Change log for A10_LOAD_BALANCER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/a10-load-balancer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for A10_LOAD_BALANCER

Date | Changes  
---|---  
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped the default value `A10 Networks` to event.idm.read_only_udm.metadata.vendor_name.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped the default value `A10 Thunder` to event.idm.read_only_udm.metadata.product_name.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `log_type` raw log field to event.idm.read_only_udm.metadata.product_event_type when `event_name` or `device_event_class_id` is empty.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jdeLoginCookie`, `Max-Age`, `SameSite`, `cookie_http`, `cookie_version` raw log field(s) to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.security_result.action: Conditional mapping applied: Mapped `FAIL` to event.idm.read_only_udm.security_result.action if desc contains `failed`, `down`, or `error` and Mapped `ALLOW` to event.idm.read_only_udm.security_result.action if desc contains `successful`, `is up`, or `established` Mapped to `UNKNOWN_ACTION` if no other conditions for desc are met.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `gslb` raw log field to event.idm.read_only_udm.security_result.severity if severity is empty and gslb is not empty.   
2025-11-19 |  Enhancement:  
\- Added a Grok pattern to parse the userid field from `msg_description`.  
\- Modified the Grok pattern to parse the dns_server field from `message`.   
2025-10-23 |  Enhancement:  
\- The key for storing the log type in the `event.idm.read_only_udm.additional.fields` UDM field has been renamed from `Log_category` to `log_category`, `Total_bytes` to `total_bytes`, `Total_packets` to `total_packets`, `Script_name` to `script_name`, and `HTTP Cookie Header Length` to `http cookie header length`.  
\- Newly added grok pattern for the `desc` data field to parse the `event.idm.read_only_udm.metadata.description` UDM field in the correct format.  
\- Modified the grok pattern for the `message` data field to parse all the raw log fields in the correct manner.   
2025-10-22 |  Enhancement:  
\- Modified the grok pattern to parse `user` field correctly.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `has_principal` is `true` and `has_principal_user` is `true` and `msg_description` is similar to `Login`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.   
2025-10-01 |  Enhancement:  
\- Added a new Grok pattern to parse new format of logs.  
\- event.idm.read_only_udm.target.resource.name: Removed mapping of `virtualserver` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.intermediary.hostname: Removed mapping of `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `virtualserver` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Script_name`, `len` and `seq_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` if `has_principal` is `true` and `has_target` is `true` and `app_proto` is `HTTP` or `has_http` is `true`.   
2025-09-29 |  Enhancement:  
\- Modified Grok patterns to parse `log_type`, `vlan_id` field correctly.  
\- event.idm.read_only_udm.security_result.description: Removed mapping of `log_type` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_type`,`vlan_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-10 |  Enhancement:  
\- Added Grok patterns to parse metadata.description.  
\- Modified Grok patterns to parse `principal.hostname`, `intermediary.hostname`, `target.application` correctly.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `httpversion` raw log field to `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `sourceip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_out` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `bytes_in` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_packets: Newly mapped `pkts_out` raw log field to `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- event.idm.read_only_udm.network.received_packets: Newly mapped `pkts_in` raw log field to `event.idm.read_only_udm.network.received_packets` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `bytes_total`u and `pkts_total` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Added condition check for `event.idm.read_only_udm.target.url` UDM field to parse correctly.  
\- Modified the mappings of `event.idm.read_only_udm.metadata.event_timestamp` UDM field to parse correctly.   
2025-09-02 |  Enhancement:  
\- Added Grok patterns to extract fields such as `user`, `prin_ip` and `sessionid` from unparsed logs.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg_description` field to event.idm.read_only_udm.metadata.description.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_priority` field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `service_name` field to event.idm.read_only_udm.target.resource.name.   
2025-08-20 |  Enhancement:  
\- Added Grok patterns to parse unparsed logs.  
\- Corrected a typo in the extracted field name from `partition_id` to `partition_id` in the grok pattern. This also applies to the key name used within the `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped virtualserver raw log field to event.idm.read_only_udm.target.resource.name.  
\- event.idm.read_only_udm.metadata.ingested_timestamp: Newly mapped timestamp raw log field to event.idm.read_only_udm.metadata.ingested_timestamp.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped time_1 raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped attack_details raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.security_result.description: Newly mapped log_type raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped waf_engine raw log field to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.action: Newly mapped attack_status raw log field to event.idm.read_only_udm.security_result.action.  
\- event.idm.read_only_udm.target.hostname: Newly mapped http_host raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped http_host raw log field to event.idm.read_only_udm.target.asset.hostname.  
\- event.idm.read_only_udm.target.url: Newly mapped http_uri raw log field to event.idm.read_only_udm.target.url.   
2025-07-09 |  Enhancement:  
\- Added Grok patterns to parse unparsed logs.  
\- Added XML support to parse new format of logs.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `vendor_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `facility` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip and event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `proxy_machine_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_dt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_type:  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` if `has_principal` is `true` and `has_target_user` is `true` and `desc` is similar to `logout`.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` if `has_target_user` is `true`.   
2024-12-27 |  Enhancement:  
\- Added Grok patterns to parse unparsed logs.  
\- Added a KV block to parse the logs.  
\- Mapped `prin_host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `app` to `target.application`.  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `device_vendor` to `metadata.vendor_name`.  
\- Mapped `device_product` to `metadata.product_name`.  
\- Mapped `event_name` and `device_event_class_id` to `metadata.product_event_type`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `src` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `spt` to `principal.port`.  
\- Mapped `dst` to `target.ip` and `target.asset.ip`.  
\- Mapped `dpt` to `target.port`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `suser` to `principal.user.user_display_name`.  
\- Mapped `act` and `cn1` to `additional.fields`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `app_proto` to `network.application_protocol`.  
\- Mapped `tls_version` to `network.tls.version`.   
2024-01-28 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
