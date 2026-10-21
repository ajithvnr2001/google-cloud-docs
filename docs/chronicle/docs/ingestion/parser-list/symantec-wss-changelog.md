---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-wss-changelog/
title: Change log for SYMANTEC_WSS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:58:03.493924+00:00
---

# Change log for SYMANTEC_WSS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-wss-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_WSS

Date | Changes  
---|---  
2025-07-11 |  Enhancement :  
\- Removed the gsub from `message` field.  
\- Added a gsub to replace `\\%20` with ` ` on `msg` field.  
\- Added a date filter to correctly populate the field `when`.  
\- Modified a Grok pattern to parse `rule_name1` field.  
\- Added a Grok pattern on `msg` field.  
\- Added a gsub on `rule_name1` field to replace `^\`|\`$` with ""  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name1` field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `time_taken` field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `content_type`,`rs_negotiated_cipher_size`,`architecture_` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `hostname_categories` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a conditional check if `os_name` nearly equals to `macOS` then map `event.idm.read_only_udm.target.asset.platform_software.platform` to `MAC`  
2025-07-09 |  Enhancement:  
\- Added Grok patterns to parse the new format of syslog logs.  
\- `event.idm.read_only_udm.target.ip_geo_artifact.location.name`: Newly mapped `x_bluecoat_location_name` raw log field with `event.idm.read_only_udm.target.ip_geo_artifact.location.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `x_bluecoat_location_id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2025-06-25 |  Enhancement :  
\- Added a conditional check before using gsub to replace `\\%20` with ` `.  
\- Modified a Grok pattern to parse the raw log.  
\- Added a Grok pattern on `uuid` field .  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_ip` field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.intermediary: Moved the merge block for `event.idm.read_only_udm.intermediary` from line number 827 to line number 1981 to populate the mapping of `intermediary.application`.   
2025-02-25 |  Enhancement :  
\- Mapped `application_name` from `cs_uri_path` to `target.application`.   
2025-02-06 |  Enhancement :  
\- Added a Grok pattern to parse the unparsed logs.   
2025-01-02 |  Enhancement :  
\- If `host` is not an IP address, then Mapped `host` field to `target.url`.   
2024-11-24 |  Enhancement :  
\- Added support to handle the unparsed syslog logs.   
2024-09-24 |  Enhancement :  
\- Added support to handle JSON logs which were parsing as `GENERIC_EVENT`.   
2024-08-07 |  Enhancement :  
\- Added support to handle the unparsed JSON logs.   
2024-05-31 |  Enhancement :  
\- When `when` is empty, then mapped `device_time` and `log_time` to `metadata.event_timestamp`.   
2024-01-23 |  Enhancement :  
\- Modified few Grok patterns to parse additional requested fields.  
\- Mapped `device_name` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `target_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `result` to `security_result.action_details`.  
\- Mapped `product_data.x-client-device-id` and `device_id` to `target.resource.product_object_id`.  
\- If `has_principal` is `true` and `has_target` is `true`, then set `metadata.event_type` as `NETWORK_CONNECTION`.   
2023-06-19 |  Bug-fix :  
\- Parsed JSON logs.  
\- Mapped `proxy_connection.src_ip` to `intermediary.ip`.  
\- Mapped `connection.protocol_version` to `tls.version`.  
\- Mapped `user.full_name` to `user.user_display_name`.  
\- Mapped `connection.dst_location.country` to `target.location.country_or_region`.  
\- Mapped `ref_uid` to `metadata.product_log_id`.  
\- Mapped `network.ip_protocol` for `TCP` field.  
\- Mapped events without `target.host` and `target.ip` to `NETWORK_UNCATEGORIZED` event type.  
\- Parsed UNIX timestamp for `device_time` field.   
2023-01-31 |  Enhancement:  
\- `product_data.x-client-device-name` mapped to `src.hostname`.  
\- `connection.src_ip` mapped to `src.ip`.   
2022-08-29 |  Enhancement -  
\- Added grok pattern to parse syslog logs.  
\- Mapped field `supplier_country` to `principal.location.country_or_region`.  
\- Added conditional check for fields `product_data.x-cs-connection-negotiated-cipher`,`product_data.x-bluecoat-transaction-uuid`,`product_data.r-supplier-country`,`product_ver`,`product_data.x-cs-client-ip-country`,`product_name`.  
\- Added error check for field `product_data.sc-filter-result`  
\- Mapped field `src_ip` to `principal.ip`.  
\- Mapped field `uri_scheme` to `network.application_protocol`.  
\- Mapped field `uuid` to metadata.product_log_id".  
\- Mapped field `cs_connection_negotiated_cipher` to `network.tls.cipher`.  
\- Mapped field `certificate_hostname` to `tls.client.server_name`.  
\- Mapped field `cs_ssl_version` to `network.tls.version_protocol`.  
\- Mapped field `certificate_validate` to `network.tls.server.certificate.subject`.  
\- Mapped field `cs_icap_status` to `security_result.description`.  
\- Mapped field `sent_bytes` to `network.sent_bytes`.  
\- Mapped field `received_bytes` to `network.received_bytes`.  
\- Mapped field `device_name` to `target.resource.name`.  
\- Mapped field `device_id` to `target.resource.id`.  
\- Mapped field `agent_type` to `observer.application`.  
\- Mapped field `os_version` to `observer.platform_version`.  
\- Mapped field `s_action` to `metadata.description`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
