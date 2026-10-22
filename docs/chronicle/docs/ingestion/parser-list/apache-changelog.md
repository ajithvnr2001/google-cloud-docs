---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/apache-changelog/
title: Change log for APACHE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:42.138708+00:00
---

# Change log for APACHE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/apache-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for APACHE

Date | Changes  
---|---  
2026-07-07 |  Enhancement:  
\- Added a Grok pattern to support new pattern of Syslog logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `timestamp_value` and `module` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-20 |  Enhancement:  
\- Added support for KV format logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `server` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytes_in` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `PHPSESSID`, `AuthToken`, `response_time_microseconds` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added support to parse new date format for the `time` raw log field.   
2026-03-03 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `Filename` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `kv_key` with label `info`, `SourceModuleName` with label `SourceModuleName`, `SourceModuleType` with label `SourceModuleType` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `EventReceivedTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp`.  
\- Grok pattern updated to extract `kv_key` from the `hostname` field.  
\- Added a grok pattern to extract `pid` from `kv_key`.  
\- Added support for new pattern of SYSLOG logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.application_protocol`  
\- `event.idm.read_only_udm.network.http.method`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.family`  
\- `event.idm.read_only_udm.network.http.response_code`  
\- `event.idm.read_only_udm.network.http.user_agent`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.ip`  
2026-01-29 |  Enhancement:  
\- Added a new Grok pattern to parse logs in a new format.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `method` raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.target.url: Newly mapped `request` raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_sent` raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.target.application: Newly mapped `program` raw log field to event.idm.read_only_udm.target.application.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `syslog_timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `ts` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `syslog_hostname` raw log field to event.idm.read_only_udm.intermediary.hostname.   
2026-01-12 |  Enhancement:  
\- Updated supported formats in the configuration file.   
2025-08-25 |  Enhancement:  
\- Added new Grok patterns to support additional log formats.  
\- event.idm.read_only_udm.target.ip: Changed mapping for `event.idm.read_only_udm.target.ip` from `src_ip` to `target_ip` in several Grok patterns in order to introduce a more accurate mapping for the raw log field.   
2025-08-18 |  Enhancement:  
\- Added grok pattern to parse uparsed fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped response_body_bytes, contentlength, contenttype, connection, AcceptEncoding, AcceptLanguage, Accept, proto_version raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- Added conditional check if the value is similar to `-` then don't map the value to additional.fields.   
2025-07-30 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip : Removed mapping of `src_ip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip : Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Updated the grok patterns to replace `IPV4` with `IP` to support both IPv4 and IPv6 addresses.   
2025-07-29 |  Enhancement:  
\- Added a new Grok pattern to parse the new log format.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `error_code` raw log field to event.idm.read_only_udm.security_result.rule_id.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `error_message` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_request_method` raw log field to event.idm.read_only_udm.network.http.method.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `traffic_bytes` raw log field to event.idm.read_only_udm.network.sent_bytes.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `protocol` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field to event.idm.read_only_udm.target.url.   
2025-07-02 |  Enhancement:  
\- Added grok pattern to handle the appropriate mapping.  
\- Updated the mapping of `event.idm.read_only_udm.additional.fields` to utilize a generalized map for fields `tzKnown`, `keep_alive`, `duration_microseconds`, `http_content_type`, `uri_path`, `uri_query`, `msg_test`, `exception`, `sHierarchy`, `scResultCode`, and `cookie`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.detection_fields` to utilize a generalized map for fields `isSynced` and `syncAccuracy`.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.version_protocol`: Newly mapped `version_protocol` raw log field with `event.idm.read_only_udm.network.tls.version_protocol` UDM field.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.hostname`, `"event.idm.read_only_udm.network.application_protocol`, `event.idm.read_only_udm.target.port`.  
\- Removed redundant code for field `security_result_category`.  
\- Added on_error for fields `resource.labels.project_id`.  
\- If `has_principal` is `true` and `has_target` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP`.  
\- If `has_principal` is `true` and `has_target` is `false`, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- Otherwise, set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2025-06-24 |  Enhancement:  
\- Added new Grok pattern to parse the logs with `hostname` field correctly.  
\- Added new KV filter to parse the additional information from `kv_data` log field.  
\- Added new gsub filter to parse the log with `kv_data` raw log field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `syncAccuracy` , and `isSynced` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `tzKnown` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-06-19 |  Enhancement:  
\- Added grok patterns to address the issue like truncation.   
2025-04-30 |  Enhancement:  
\- Added a new Grok pattern in order to parse the logs with Syslog format.  
\- Added a new Grok pattern to parse the `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Handled new pattern of `RFC3339` timestamps for `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-01-09 |  Enhancement:  
\- Added a new Grok pattern to parse the new log format.  
\- Mapped `user_location` to `principal.location.country_or_region`.  
\- Mapped `proto`, `proto_version`, `uri_path`, and `uri_query` to `additional.fields`.   
2024-12-19 |  Enhancement:  
\- Added a Grok pattern to parse the unparsed logs.   
2024-09-10 |  Enhancement:  
\- Added support to parse unparsed logs.   
2024-08-05 |  Enhancement:  
\- Added a Grok pattern to parse the `jsonPayload.message` field into `additional.fields`.  
\- Mapped `ip_msg` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `msg_method` to `network.http.method`.  
\- Mapped `response_code` to `network.http.response_code`.  
\- Mapped `useragentvalue` to `network.http.user_agent`.   
2024-06-11 |  Enhancement:  
\- Added a Grok pattern to parse the new pattern of SYSLOG format logs.   
2024-01-25 |  Enhancement:  
\- Added a new Grok pattern to parse syslog logs that contain symbol `+`.  
\- Added a new Grok pattern to remove date field being parsed alonside targeturl.   
2023-12-21 |  Enhancement:  
\- Handled unparsing JSON logs.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `x_forwarded_for` to `principal.ip`.  
\- Mapped `keep_alive`, `duration_microseconds`, `cookie`, `http_content_type` to `additional.fields`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `http_host` to "principal.hostname.  
\- Mapped `file_full_path` to `target.file.full_path`.  
\- Mapped `ssl_version` to `network.tls.version_protocol`.  
\- Mapped `ssl_cipher` to `network.tls.cipher`.  
\- Mapped `uri_path` to `target.process.file.full_path`.  
\- Mapped `http_referrer` to `network.http.referral_url`.  
\- Mapped `http_user_agent` to `network.http.user_agent`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `protocol` to `network.application_protocol`.  
\- Mapped `dest_port` to `target.port`.  
\- Mapped `dest_name` to `target.hostname`.  
\- Mapped `bytes_out` to `network.sent.bytes`.   
2023-07-31 |  Enhancement:  
\- Modified Grok pattern to handle hyphen(`-`) when bytes are not available.   
2023-06-05 |  Enhancement:  
\- Mapped `Content` to `target.url`, `network.http.method` and `network.tls.version_protocol`.  
\- Mapped `LastStatus` to `network.http.response_code`.  
\- Mapped `SizeBytes` to `network.received_bytes`.  
\- Mapped `Workername` to `principal.hostname`.  
\- Mapped `Port` to `target.port`.  
\- Mapped `ID` to `metadata.id`.  
\- Mapped `XForwardedForIP` and `RemoteHost` to `principal.ip`.  
\- Mapped `Remoteuser` to `principal.user.userid`.  
\- Modified Grok pattern to support incorrect log parsing.   
2023-02-20 |  Enhancement:  
\- Modified Grok pattern to support incorrect log parsing.  
\- Converted `user_agent` to `network.http.parsed_user_agent`.   
2022-09-21 |  Enhancement: - Migrated to default parser.   
2022-09-07 |  Enhancement:  
\- Added grok patterns to parse logs with json + syslog format.  
\- Mapped the field `host.name` and `hostname` to `target.hostname`.  
\- Mapped the field `log.file.path` to `principal.process.file.full_path`.  
\- Mapped the field `mac` to `principal.mac`.  
\- Mapped the field `ip` to `principal.asset.ip`.  
\- Mapped the field `os.version` to `principal.platform_version`.  
\- Mapped the field `os.kernel` to `principal.platform_patch_level`.  
\- Mapped the field `os.platform` to `principal.platform`.  
\- Mapped the field `architecture` to `principal.asset.hardware`.  
\- Mapped the field `id` to `principal.asset.asset_id`.   
2022-05-12 |  Enhancement:  
Added grok patterns for unique unparsed logs.  
\- Added conditional checks for `network.http.user_agent` and `network.http.referral_url`.  
\- Added support for Apache Traffic Server (ATS) proxy logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
