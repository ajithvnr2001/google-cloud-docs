---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-webproxy-changelog/
title: Change log for FORCEPOINT_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:08.569211+00:00
---

# Change log for FORCEPOINT_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORCEPOINT_WEBPROXY

Date | Changes  
---|---  
2026-08-07 |  Enhancement:  
\- `event.idm.read_only_udm.network.sent_bytes`: Removed mapping of `column28` from `event.idm.read_only_udm.network.sent_bytes` UDM field since the field represents bytes received.  
\- `event.idm.read_only_udm.network.received_bytes`: Mapped `column28` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Removed mapping of `column29` from `event.idm.read_only_udm.network.received_bytes` UDM field since the field represents bytes sent.  
\- `event.idm.read_only_udm.network.sent_bytes`: Mapped `column29` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `column8` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `column10` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `column19` raw log field to `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `column21` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field.   
2026-07-23 |  Enhancement:  
\- Added support for new format of csv logs.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_log_id` fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `groups` field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product_event_type` field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_sent` field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `bytes_received` field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip`, `principal_ip` fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_userid` fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_hostname` field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `user_agent` field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `data_center` field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date`, `time` fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `region_value` field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `policy_value`, `classification` fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `request_id`, `auth`, `file_size`, `signature_version` and `method_2` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.file.names: Newly mapped `filename` field with `event.idm.read_only_udm.principal.file.names` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `tls` field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `tls_2` field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `protocol_version` field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `protocol_version` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `vendor_name` field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: When valid principal and target are present, and protocol version is HTTP or HTTPS, updated to `NETWORK_HTTP`.   
2026-06-03 |  Enhancement:  
\- Added gsub to parse `request` raw log field correctly.   
2026-05-21 |  Enhancement:  
\- Removed the grok pattern used to specially parse `requestClientApplication`.  
\- Added a conditional check to only apply `gsub` on `kv_msg` (replacing `|` with `@` and `@` with `#`) if the raw `message` starts with `Bluecoat`.   
2026-05-04 |  Enhancement:  
\- Modified a grok pattern to parse the logs accurately.  
\- Added a grok pattern on `kv_msg` to extract `requestClientApplication` field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-02-20 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Enhanced `rt` timestamp field parsing to also handle 10-digit UNIX epoch format and map it to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `product_version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cn2` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `destinationTranslatedPort` and `logRecordSource` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Modified grok patterns to extract fields `product_version` and `severity`.   
2025-10-14 |  Enhancement:  
\- The gsub mutations were removed because they stripped percentage signs, corrupting URL-encoded data in logs, which caused grok patterns to extract invalid IP addresses (e.g., 24.0.0.07) and trigger field type check failures.   
2025-09-12 |  Enhancement:-  
\- Added support to parse the timestamp properly.  
\- event.idm.read_only_udm.target.process.file.mime_type: Newly Mapped `extension` raw log field with `event.idm.read_only_udm.target.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly Mapped `filetype` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly Mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly Mapped `received_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly Mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly Mapped `response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly Mapped `region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly Mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `sec_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly Mapped `version` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly Mapped `version` raw log with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly Mapped `city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.target.url: Newly Mapped `turl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly Mapped `email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly Mapped `_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly Mapped `descrip` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly Mapped `appname` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `tip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `tip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `pip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `pip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly Mapped `log_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.port: Newly Mapped `port` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2025-09-05 |  Enhancement:-  
\- Added support for new csv format logs.  
\- event.idm.read_only_udm.network.http.user_agent: Newly Mapped `version` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly Mapped `version` raw log with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly Mapped `city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- event.idm.read_only_udm.target.url: Newly Mapped `turl` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly Mapped `email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly Mapped `descrip` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly Mapped `status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly Mapped `appname` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `tip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `tip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `pip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `pip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `p_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-04-11 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname : Removed Mapping of `dhost` from `event.idm.read_only_udm.intermediary.hostname` UDM field and Mapped `dvchost` instead.  
\- event.idm.read_only_udm.target.hostname: Newly Mapped `dhost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.   
2025-03-06 |  Enhancement:  
\- Mapped `rt` to `event.timestamp`.   
2025-01-16 |  Enhancement:  
\- Mapped `security_result.action` to `BLOCK` when `s-action` is `TCP_DENIED`.   
2024-10-18 |  Enhancement:  
\- Added support to parse the unparsed CSV logs.  
\- Added support to drop invalid CSV logs.  
\- Mapped `host-url` to `principal.url`.   
2024-07-10 |  Enhancement:  
\- Added the Grok patterns for new KV format logs.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `cs-uri` to `target.url`.  
\- Mapped `cs-uri-query` , `time-taken` , `filter-category` , `cs-uri-path` , `cs-uri-extension` and `rs_content_type` to `additional.fields`.  
\- If `sc-filter-result` is `OBSERVED` then set `security_result.action` to `ALLOW` , else if `sc-filter-result` is `DENIED` then set `security_result.action` to `BLOCK` , else set `security_result.action` to `ALLOW`.  
\- Mapped `cs-auth-group` to `principal.user_group_identifiers`.  
\- Mapped `cs-method` to `network.http.method`.  
\- Mapped `sc-status` to `response_code`.  
\- Mapped `s-action` to `security_result.detection_fields`.  
\- Mapped `srcport` to `principal.port`.  
\- Mapped `dstport` to `target.port`.  
\- Mapped `sc-bytes` to `network.received_bytes`.  
\- Mapped `cs-bytes` to `network.sent_bytes`.  
\- Mapped `cs` to `security_result.summary`.  
\- Mapped `cs_referer` to `network.http.referral_url`.  
\- Mapped `cs-host` to `target.hostname`.   
2024-06-10 |  Enhancement:  
\- Added support for CSV format logs.   
2023-06-12 |  Enhancement:  
\- Modified Grok pattern to parse failing logs in which some of the values are present as `-`.  
\- Added condition check for field `http_response` before mapping.   
2022-08-11 |  Enhancement:  
\- Modified grok to parse CEF type logs with no syslog header.   
2022-05-16 |  Enhancement: mapped category number to security_result.detection_fields.   
2022-05-05 |  Enhancement:  
dded mapping for fields:  
requestClientApplication to http.user_agent.  
proxyStatus-code to http.response_code.  
disposition and cn1 to security_result.detection_fields.  
Mapped `cs2` field to `security_result.category_details` if the value of `cs2Label` is `DynCat`.  
Mapped `cs2` field to `security_result.detection_fields` if the value of `cs2Label` is `NatRuleId`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
