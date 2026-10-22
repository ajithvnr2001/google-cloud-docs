---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-changelog/
title: Change log for FIREEYE_HX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:07.548026+00:00
---

# Change log for FIREEYE_HX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-hx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIREEYE_HX

Date | Changes  
---|---  
2026-08-20 |  Enhancement:  
\- Added a new grok pattern on `temp_data` field to extract `collected_time` from the raw log.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `collected_time` field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cs8`, `start` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `categoryTechnique` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-07-07 |  Enhancement:  
\- Added grok pattern to Support SYSLOG format of logs.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_hostname` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_id` field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `k_value`, `v_value`, `source_line`, `source_file`, `syslog_pri` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `id1` field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `desc1` field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `process` field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity1` field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-05-14 |  Enhancement:  
\- Declared `cs6Label` initially.   
2024-12-12 |  Enhancement:  
\- Added support for new format of JSON logs.   
2024-10-23 |  Enhancement:  
\- Mapped `cs12` to `additional.fields`.  
\- Mapped `cs9` to `target.process.file.md5`.   
2024-10-15 |  Enhancement:  
\- Mapped `account_name`, `UUID`, `Mitre`, `host_details.data.sysinfo.url`, `host_details.route`, `host_details.data.reported_clone`, and `host_details.data.timezone` to `security_result.detection_fields`.  
\- Mapped `Desc` to `metadata.description`.  
\- Mapped `Confidence` to `security_result.confidence`.  
\- Mapped `alert.appliance._id` to `additional.fields`.  
\- Mapped `host_details.data.stats.acqs`, `host_details.data.stats.alerting_conditions`, `host_details.data.stats.alerts`, `host_details.data.stats.exploit_alerts`, `host_details.data.stats.exploit_blocks`, and `host_details.data.stats.false_positive_alerts` to `security_result.detection_fields`.   
2024-09-12 |  Enhancement:  
\- Mapped `categoryOutcome`, `cs13` to `additional.fields`.  
\- Mapped `cs6` to `target.process.file.sha1`.  
\- Mapped `cs9` to `target.process.file.md5`.   
2024-08-28 |  Enhancement:  
\- Mapped `host_details.message` to `security_result.action_details`.  
\- Mapped `alert.md5values`, `alert.resolution`, `alert.is_false_positive`, and `alert.alert_type` to `additional.fields`.  
\- Mapped `type.threat_type` to `security_result.threat_name`.  
\- Mapped `ent.lms_event_id` to `metadata.product_log_id`.  
\- Mapped `email.smtp.mail_from` to `network.email.from`.  
\- Mapped `email.headers.subject` to `network.email.subject`.  
\- Mapped `email.headers.to` to `network.email.to`.  
\- Mapped `ent.type`, `ent.id`, `ent.name`, `ent.object_source`, `ent.binary`, and `ent.attributes.scan_id` to `security_result.detection_fields`.   
2024-08-13 |  Enhancement:  
\- Mapped `cs11Label` to `additional_cs11Label.key`.  
\- Mapped `cs11` to `additional_cs11.value`.   
2024-04-04 |  Enhancement:  
\- Added a Grok pattern retrieve JSON data to parse unparsed logs.  
\- Mapped `alert.sysinfo.mac_address` to `principal.mac`.  
\- Mapped `host_details.data.agent_version` to `metadata.product_version`.  
\- Mapped `alert.url` to `metadata.url_back_to_product`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `alert.event_type` to `metadata.product_event_type`.  
\- Mapped `alert.agent._id` to `principal.asset.asset_id`.  
\- Mapped `alert.event_id` to `metadata.product_log_id`.   
2024-04-03 |  Enhancement:  
\- Mapped `deviceCustomDate1Label` to `additional_deviceCustomDate1.key`.  
\- Mapped `deviceCustomDate1` to `additional_deviceCustomDate1.value`.  
\- Mapped `deviceCustomDate2` to `additional_deviceCustomDate2.value`.   
2024-04-02 |  Enhancement:  
\- Added a regex check to `fileHash` to map md5 and sha256 respectively.   
2024-01-04 |  Enhancement:  
\- Added support for dropped logs.  
\- Mapped `client` to `principal.ip`.  
\- Mapped `principal_ip` to `principal.ip`.  
\- Mapped `remoteaddress` to `principal.ip`.  
\- Mapped `host_` to `principal.hostname`.  
\- Mapped `line` to `principal.application`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `client_app_type` to `principal.resource.attribute.labels`.  
\- Mapped `upstream` to `target.url`.  
\- Mapped `role` to `target.user.role_name`.  
\- Mapped `server` to `target.resource.attribute.labels`.  
\- Mapped `localusername` to `target.user.user_display_name`.  
\- Mapped `request` to `additional.fields`.  
\- Mapped `mlocked` to `additional.fields`.  
\- Mapped `kernel_stack` to `additional.fields`.  
\- Mapped `sessionID` to `network.session_id`.  
\- Mapped `auth_mechanism` to `extensions.auth.mechanism`.  
\- Mapped `authsubmethod` to `extensions.auth.auth_details`.   
2023-05-08 |  Enhancement -  
\- Supported new type of JSON logs.  
\- `client_ip` mapped to `principal.ip`.  
\- `client_src_port` mapped to `principal.port`.  
\- `ssl_version` mapped` to `network.tls.version_protocol".  
\- `ssl_cipher` mapped to `network.tls.cipher`.  
\- `method` mapped to `network.http.method`.  
\- `uri_path` mapped to `network.http.referral_url`.  
\- `persistent_session_id` mapped to `network.session_id`.  
\- `uri_query` mapped to `additional.fields`.  
\- `rewritten_uri_query` mapped to `additional.fields`.  
\- `virtualservice` mapped to `additional.fields`.  
\- `service_engine` mapped to `additional.fields`.  
\- `etag` mapped to `additional.fields`.  
\- `pool` mapped to `additional.fields`.  
\- `pool_name` mapped to `additional.fields`.  
\- `request_state` mapped to `additional.fields`.  
\- `compression` mapped to `additional.fields`.  
\- `vs_name` mapped to `additional.fields`.  
\- `request_id` mapped to `additional.fields`.  
\- `headers_received_from_server.Server` mapped to `additional.fields`.  
\- `headers_received_from_server.X-Request-Id` mapped to `additional.fields`.  
\- `headers_received_from_server.X-Server-Id` mapped to `additional.fields`.   
2023-04-24 |  Enhancement -  
\- Added support for CEF format logs.   
2022-08-19 |  Fix -  
\- Mapped event_values.ipv4NetworkEvent/localIP to `principal.ip`.  
\- Renamed event to event1 from log to avoid no descriptor error.  
\- Added null check to host_details.data.primary_ip_address prior mapping it to `principal.ip`.  
\- Added null check to host_details.data.primary_mac prior mappig to `principal.mac`.  
\- Added null check to alert.reported_at prior mapping to `event.timestamp`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
