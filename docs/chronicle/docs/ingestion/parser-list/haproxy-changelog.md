---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/haproxy-changelog/
title: Change log for HAPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:31:32.881597+00:00
---

# Change log for HAPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/haproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HAPROXY

Date | Changes  
---|---  
2026-06-01 |  Enhancement:  
\- Added a grok pattern to parse the raw logs.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `sni` raw log field with `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `sys_time` field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `prin_app` field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `prin_pid` field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `date_time` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly mapped `frontendName`, `backendName` fields with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Added a grok pattern on `request` raw log field to extract `method`, `proto` and `tar_host` fields.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `host_ip` field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `tar_host` field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field when `host` raw log field is null.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `proto` field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `proto_value` field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP`, `NETWORK_CONNECTION` and `STATUS_UPDATE` when necessary raw log fields are present else set it to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `timers` field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-30 |  Enhancement:  
\- Added a Grok pattern to parse new pattern of logs.  
\- Added KV filter block to parse the kv_data field, splitting keys and values.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field .  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field .  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `source_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field .  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field .  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field .  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` (from header_host) raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field .  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `inter_port` (from header_host) raw log field with `event.idm.read_only_udm.intermediary.port` UDM field .  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `destination_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field .  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destination_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field .  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destination_port` raw log field with `event.idm.read_only_udm.target.port` UDM field .  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field .  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field .  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `time_stamp` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field .  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `x_forwarded_for` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field .  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `content_length` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field .  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `datetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field .   
2024-08-23 |  Enhancement:  
\- Added support for a new pattern of syslog logs.   
2023-09-25 |  Enhancement:  
\- Added new Grok patterns to parse new type of logs.  
\- Mapped `http_version` to `metadata.product_version`.  
\- Mapped `user_name` to `target.user.userid`.  
\- Mapped `process_name` to `target.application`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `msg` to `security_result.summary`.  
\- Added new conditions for new log types and their severity.   
2023-05-08 |  \- Added new Grok pattern to parse new type of logs.   
2022-10-20 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
