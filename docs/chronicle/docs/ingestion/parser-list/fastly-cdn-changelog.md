---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-cdn-changelog/
title: Change log for FASTLY_CDN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:14:16.889998+00:00
---

# Change log for FASTLY_CDN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-cdn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FASTLY_CDN

Date | Changes  
---|---  
2026-07-16 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed the mapping of `host` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as it represents the target hostname to which the client is connecting.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped the `host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when log has principal and target machine data along with HTTP details.   
2026-07-14 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.response_code`: Added support for `status` to ensure proper mapping to `event.idm.read_only_udm.network.http.response_code`.  
\- `event.idm.read_only_udm.network.tls.established`: Added support for `is_tls` to ensure proper mapping to `event.idm.read_only_udm.network.tls.established`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cookies`, `platform_origin`, `post_body`, `request_accept_charset` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-02 |  Enhancement:  
\- Added logic to handle `\r\n` characters in the raw JSON message.  
\- Updated `metadata.event_type` to `NETWORK_CONNECTION` when target and principal/target details are available.  
\- Enhanced `protocol` field parsing using grok to extract the base protocol name.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `service_id` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `time_elapsed` raw log field to `event.idm.read_only_udm.network.session_duration.seconds`.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `client_as_name` raw log field to `event.idm.read_only_udm.principal.group.group_display_name`.  
\- `event.idm.read_only_udm.network.asn`: Newly mapped `client_as_number` raw log field to `event.idm.read_only_udm.network.asn`.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `request` raw log field to `event.idm.read_only_udm.network.http.method`.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field to `event.idm.read_only_udm.network.application_protocol`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `origin_host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `origin_host` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.network.tls.version_protocol`: Newly mapped `tls_client_protocol` raw log field to `event.idm.read_only_udm.network.tls.version_protocol`.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `tls_client_servername` raw log field to `event.idm.read_only_udm.network.tls.client.server_name`.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_client_cipher` raw log field to `event.idm.read_only_udm.network.tls.cipher`.  
\- `event.idm.read_only_udm.network.tls.established`: Newly mapped `is_tls` raw log field to `event.idm.read_only_udm.network.tls.established`.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `req_body_size` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `resp_body_size` raw log field to `event.idm.read_only_udm.network.sent_bytes`.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field to `event.idm.read_only_udm.network.http.response_code`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `server` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `server` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `server_ip` raw log field to `event.idm.read_only_udm.intermediary.ip`.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `server_ip` raw log field to `event.idm.read_only_udm.intermediary.asset.ip`.  
\- `event.idm.read_only_udm.intermediary.location.name`: Newly mapped `server_datacenter` raw log field to `event.idm.read_only_udm.intermediary.location.name`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `geo_country_code` raw log field to `event.idm.read_only_udm.principal.location.country_or_region`.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `geo_region` raw log field to `event.idm.read_only_udm.principal.location.state`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `client_connection_speed` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cache_status` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `request_accept_content`, `request_accept_language`, `request_accept_encoding`, `content_type`, `response_cache_control`, `response_expires`, `response_last_modified`, `geo_continent_code`, `req_header_size`, `resp_header_size`, `time_start`, `time_end`, `socket_cwnd`, `socket_tcpi_rtt`, `is_ipv6`, `platform_cluster`, `platform_router` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-01-10 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
