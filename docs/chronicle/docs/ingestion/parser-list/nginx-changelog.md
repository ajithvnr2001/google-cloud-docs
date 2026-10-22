---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nginx-changelog/
title: Change log for NGINX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:37.603604+00:00
---

# Change log for NGINX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/nginx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NGINX

Date | Changes  
---|---  
2026-09-10 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `dest_ip` to extract `dest_ip`  
\- Added a grok pattern on `dest_port` to extract `dest_port`  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytes_in` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes_out` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dest_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dest_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `server`, `site` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `http_x_header`, `https` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `uri_path` and `uri_query` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `response_time`, `cookie` and `category` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-10 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `jsonPayload.timestamp` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- Added support to remove `''` value from `jsonPayload.userAgent` raw log field.   
2026-01-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` : Removed mapping of `log_hostname` from `event.idm.read_only_udm.principal.hostname` UDM field to introduce more accurate mapping.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `log_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field to introduce more accurate mapping.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `ip_part` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.administrative_domain`: Newly mapped `domain_part` raw log fields with `event.idm.read_only_udm.intermediary.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.intermediary.location.name`: Newly mapped `location_part` raw log field with `event.idm.read_only_udm.intermediary.location.name` UDM field.   
2026-01-29 |  Enhancement:  
\- event.idm.read_only_udm.network.http.referral_url: Removed mapping of `jsonPayload.requestUrl` from `event.idm.read_only_udm.network.http.referral_url` UDM field as it is better suited for `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.url: Mapped `jsonPayload.requestUrl` raw log field to `event.idm.read_only_udm.target.url` UDM field.   
2025-12-19 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Removed mapping of `remote_ip` from `event.idm.read_only_udm.target.ip` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.target.asset.ip: Removed mapping of `remote_ip` from `event.idm.read_only_udm.target.asset.ip` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.principal.ip: Mapped `remote_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Removed mapping of `jsonPayload.requestSize` from `event.idm.read_only_udm.network.sent_bytes` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.network.received_bytes: Mapped `jsonPayload.requestSize` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Removed mapping of `jsonPayload.responseSize` from `event.idm.read_only_udm.network.received_bytes` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.network.sent_bytes: Mapped `jsonPayload.responseSize` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `labels.compute_googleapis_com/resource_name` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `labels.compute_googleapis_com/resource_name` raw log field from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `resource.labels.instance_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `resource.labels.instance_id` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.target.resource_ancestors.name: Newly mapped `resource.labels.project_id` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `resource.labels.project_id` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone: Newly mapped `resource.labels.zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `resource.labels.zone` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce more accurate mapping.  
\- event.idm.read_only_udm.target.resource.resource_type: Newly mapped `resource.type` (when equal to `gce_instance`) raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Removed mapping of `resource.type` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field to introduce more accurate mapping.   
2025-12-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped year, month, day, log_time, date raw log field(s) with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped product_log_id raw log field(s) with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped src_ip raw log field(s) with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped source_port raw log field(s) with event.idm.read_only_udm.principal.port UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped log_hostname raw log field(s) with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped pid raw log field(s) with event.idm.read_only_udm.principal.process.pid UDM field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped translated_src raw log field(s) with event.idm.read_only_udm.principal.nat_ip UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped user_name raw log field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped nginx_version, vers raw log field(s) with event.idm.read_only_udm.metadata.product_version UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped dst_ip raw log field(s) with event.idm.read_only_udm.target.ip UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped dst_port raw log field(s) with event.idm.read_only_udm.target.port UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped uri raw log field(s) with event.idm.read_only_udm.target.url UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped application_protocol raw log field(s) with event.idm.read_only_udm.network.application_protocol UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped version raw log field(s) with event.idm.read_only_udm.network.application_protocol_version UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped status_code raw log field(s) with event.idm.read_only_udm.network.http.response_code UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped http_referer raw log field(s) with event.idm.read_only_udm.network.http.referral_url UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped http_user_agent raw log field(s) with event.idm.read_only_udm.network.http.user_agent UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped http_user_agent raw log field(s) with event.idm.read_only_udm.network.http.parsed_user_agent UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped bytes raw log field(s) with event.idm.read_only_udm.network.received_bytes UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped http_method raw log field(s) with event.idm.read_only_udm.network.http.method UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped (learning, total_processed, total_blocked, block, cscore0, score0, cscore1, score1, zone0, id0, http_x_forwarded_for) field(s) with event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped http_content_type raw log field(s) with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped log_level raw log field(s) with event.idm.read_only_udm.security_result.severity_details UDM field.  
\- event.idm.read_only_udm.security_result.about.url: Newly mapped url raw log field(s) with event.idm.read_only_udm.security_result.about.url UDM field.  
\- Other Updates:  
\- Two new grok patterns were added to support additional NGINX log formats, including key-value pair logs.  
\- A kv filter was introduced to parse fields from logs containing key-value data.  
\- A grok filter was added to parse the protocol field to extract the application_protocol and version.   
2025-12-04 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `insertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jsonPayload.latency` raw log field as a custom label with key `latency` with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped from the extracted `application_protocol` from jsonPayload.protocol with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped from the extracted `version` from jsonPayload.protocol with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `remoteIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `jsonPayload.requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `jsonPayload.requestSize` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `jsonPayload.requestUrl` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `jsonPayload.responseSize` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `jsonPayload.serverIp` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `jsonPayload.status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `jsonPayload.userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `jsonPayload.userAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels`, `terminal`, `logName` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.labels` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resource.type` raw log field with key `resource_type` with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `resource.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true` and `has_target` is `true` and `is_http` is `true`, then mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `NETWORK_HTTP`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true` and `has_target` is `true`, then mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `NETWORK_CONNECTION`.  
\- event.idm.read_only_udm.metadata.event_type: If `has_principal` is `true`, then mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `STATUS_UPDATE`.   
2025-07-23 |  Enhancement:  
\- Updated grok pattern to retrieve target_ip.   
2025-06-23 |  Enhancement:  
\- Added a Grok pattern to fetch only the required `user_agent` data and map it to `network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field   
2022-09-10 |  -Newly created parser.  
-Created default parser and deleted customer specific parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
