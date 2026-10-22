---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecoat-webproxy-changelog/
title: Change log for BLUECOAT_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:31.904604+00:00
---

# Change log for BLUECOAT_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bluecoat-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BLUECOAT_WEBPROXY

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: Removed mapping of `s_supplier_ip` from `event.idm.read_only_udm.intermediary.ip` UDM field as it contains target IP data.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `s_supplier_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.   
2026-08-17 |  Enhancement:  
\- Added a new grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timeT` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `x-bluecoat-appliance-name` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `cs-categories` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cs-username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `cs-User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `cs-User-Agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `cs-threat-risk` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `cs-uri-scheme` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `cs-Referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `x-bluecoat-reference-id`, `x-rs-certificate-observed-errors`, `x-rs-connection-negotiated-cipher-strength`, `x-data-leak-detected` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `x-exception-id`, `x-bluecoat-transaction-uuid`, `rs-Content-Type`, `x-bluecoat-application-name`, `x-bluecoat-application-operation`, `x-rs-certificate-hostname`, `x-icap-reqmod-header(X-ICAP-Metadata)`, `x-icap-respmod-header(X-ICAP-Metadata)` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field   
2026-07-06 |  Enhancement:  
\- `event.idm.read_only_udm.target.url`: Removed mapping of `target_hostname` from `event.idm.read_only_udm.target.url` UDM field as it represents a hostname value not URL.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_hostname` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields if it is a valid IP address.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields if it is a valid hostname.   
2026-06-19 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `log_event.action` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent.original` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.received_bytes`: Newly mapped `http.response.bytes` raw log field with `event.idm.read_only_udm.network.http.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url.original` and `url.query` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `rs_Content-Type` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `url.scheme` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp_ms` and `timestamp_data` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `url.path` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `http.response.status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `url.port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `url.domain` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.session_duration`: Newly mapped `log_event.duration` raw log field with `event.idm.read_only_udm.network.session_duration` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `source.user.name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.sent_bytes`: Newly mapped `http.request.bytes` raw log field with `event.idm.read_only_udm.network.http.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `server.ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `collector_host` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http.request.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `http.request.referrer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `misc_bluecoat`, `version`, `type`, `format_type`, `group.name`, `s_hierarchy` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-12 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `cs_referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `rs_content_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `sc_filter_result` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `s_source_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.   
2026-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: When `sc_filter_result` is `PROXIED` or `OBSERVED`, set the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.network.application_protocol`: When `app_protocol_src` is `SSL`, set the value of `event.idm.read_only_udm.network.application_protocol` to `HTTPS`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http_method_src` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-21 |  Enhancement:  
\- Added a new grok pattern to parse raw log fields correctly to appropriate UDM fields for `TCP_DENIED` events.   
2026-05-14 |  Enhancement:  
\- Added `gsub` to remove leading newline characters from logs.   
2026-05-07 |  Enhancement:  
\- Modified a grok pattern to parse new format of SYSLOG logs.  
\- `event.idm.read_only_udm.security_result.action`: If `filter_result` is `PROXIED` or `_policy_action` is `PROXIED` then set `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- Refined the conditional check for mapping `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields to exclude values of `http` or `https`.   
2026-04-20 |  Enhancement:  
\- Added the grok patterns to parse new format of syslog logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `xbluecoat_application_operation` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-02 |  Enhancement:  
\- Added a grok pattern on `message` to extract `syslog_priority` and `message` log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `cs_host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as `cs-host` field corresponds to target details.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `cs_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.   
2026-02-13 |  Enhancement:  
\- `event.idm.read_only_udm.about.url`: Removed mapping of `cs_uri` from `event.idm.read_only_udm.about.url` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `cs_uri` raw log field to `event.idm.read_only_udm.target.url` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Removed mapping of `r_dns` from `event.idm.read_only_udm.target.resource.attribute.labels` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.hostname`: Removed mappings of `s_supplier_name` from `event.idm.read_only_udm.target.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `s_supplier_name` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `r_dns` raw log field to `event.idm.read_only_udm.target.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `r_dns` raw log field to `event.idm.read_only_udm.target.asset.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.   
2025-12-06 |  Enhancement:  
event.idm.read_only_udm.target.file.full_path: Newly mapped cs_uri_extension raw log field with event.idm.read_only_udm.target.file.full_path UDM field.  
event.idm.read_only_udm.security_result.about.url: Newly mapped x_cs_Referer_uri_threat_risk raw log field with event.idm.read_only_security_result.about.url UDM field.  
event.idm.read_only_udm.security_result.category_details: Newly mapped x_cs_Referer_uri_categories raw log field with event.idm.read_only_udm.security_result.category_details UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Newly mapped x_rs_certificate_hostname_threat_risk raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped x_icap_reqmod_header_X_ICAP_Metadata, x_icap_respmod_header_X_ICAP_Metadata raw log fields with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
event.idm.read_only_udm.intermediary.ip: Removed mapping of cs_X_Forwarded_For from event.idm.read_only_udm.intermediary.ip UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.principal.ip: Mapped cs_X_Forwarded_For raw log field to event.idm.read_only_udm.principal.ip UDM field.  
event.idm.read_only_udm.security_result.summary: Removed mapping of x_exception_id from event.idm.read_only_udm.security_result.summary UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.security_result.description: Mapped x_exception_id raw log field to event.idm.read_only_udm.security_result.description UDM field.  
event.idm.read_only_udm.security_result.risk_score: Removed mapping of cs_threat_risk from event.idm.read_only_udm.security_result.risk_score UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.security_result.severity_details: Mapped cs_threat_risk raw log field to event.idm.read_only_udm.security_result.severity_details UDM field.  
event.idm.read_only_udm.metadata.product_log_id: Removed mapping of x_bluecoat_transaction_uuid from event.idm.read_only_udm.metadata.product_log_id UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.metadata.id: Mapped x_bluecoat_transaction_uuid raw log field to event.idm.read_only_udm.metadata.id UDM field.  
event.idm.read_only_udm.about.ip: Removed mapping of s_source_ip from event.idm.read_only_udm.about.ip UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.src.ip: Mapped s_source_ip raw log field to event.idm.read_only_udm.src.ip UDM field.  
event.idm.read_only_udm.about.asset.ip: Removed mapping of s_source_ip from event.idm.read_only_udm.about.asset.ip UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.src.asset.ip: Mapped s_source_ip raw log field to event.idm.read_only_udm.src.asset.ip UDM field.  
event.idm.read_only_udm.about.port: Removed mapping of s_source_port from event.idm.read_only_udm.about.port UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.src.port: Mapped s_source_port raw log field to event.idm.read_only_udm.src.port UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of cs_uri_scheme from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.network.application_protocol: Mapped cs_uri_scheme raw log field to event.idm.read_only_udm.network.application_protocol UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of x_rs_connection_negotiated_ssl_version from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.network.tls.version: Mapped x_rs_connection_negotiated_ssl_version raw log field to event.idm.read_only_udm.network.tls.version UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of x_rs_connection_negotiated_cipher from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.network.tls.cipher: Mapped x_rs_connection_negotiated_cipher raw log field to event.idm.read_only_udm.network.tls.cipher UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of cs_uri from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.about.url: Mapped cs_uri raw log field to event.idm.read_only_udm.about.url UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of s_sitename from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.intermediary.application: Mapped s_sitename raw log field to event.idm.read_only_udm.intermediary.application UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of s_supplier_failures from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.intermediary.resource.attribute.labels: Mapped s_supplier_failures raw log field to event.idm.read_only_udm.intermediary.resource.attribute.labels UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of x_bluecoat_application_name from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.target.application: Mapped x_bluecoat_application_name raw log field to event.idm.read_only_udm.target.application UDM field.  
event.idm.read_only_udm.security_result.detection_fields: Removed mapping of rs_Content_Type from event.idm.read_only_udm.security_result.detection_fields UDM field.As it is not an appropriate mapping.  
event.idm.read_only_udm.intermediary.resource.type: Mapped rs_Content_Type raw log field to event.idm.read_only_udm.intermediary.resource.type UDM field.   
2025-11-10 |  Enhancement:  
\- Added support for space-separated log format starting with `broadcomedgeswg`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `c_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `c_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `cs_auth_group` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `date_time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `c_port` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `r_ip` raw log field to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `r_port` and `cs_uri_port` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `s_ip`, `x_bluecoat_appliance_primary_address`, `s_supplier_ip` and `cs_X_Forwarded_For` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `s_port` raw log field to `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `x_bluecoat_placeholder` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.location.country_or_region`: Newly mapped `s_supplier_country` raw log field to `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `s_supplier_name` raw log field to `event.idm.read_only_udm.target.ip` when `s_supplier_name` contains a valid IP address else mapped to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `cs_username` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `cs_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `sc_status` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `cs_User_Agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `cs_Referer` raw log field to `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `cs_bytes` raw log field to `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `sc_bytes` raw log field to `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `x_exception_id` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `sc_filter_result` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `cs_categories`, `cs_category`, `x_rs_certificate_hostname_category` and `x_exception_category` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `cs_threat_risk` raw log field to `event.idm.read_only_udm.security_result.risk_score` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `x_bluecoat_transaction_uuid` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.tls.client.server_name`: Newly mapped `x_rs_certificate_hostname` raw log field to `event.idm.read_only_udm.network.tls.client.server_name` UDM field.  
\- `event.idm.read_only_udm.about.ip`: Newly mapped `s_source_ip` raw log field to `event.idm.read_only_udm.about.ip` UDM field.  
\- `event.idm.read_only_udm.about.port`: Newly mapped `s_source_port` raw log field to `event.idm.read_only_udm.about.port` UDM field.  
\- `event.idm.read_only_udm.about.hostname`: Newly mapped `x_http_connect_host` raw log field to `event.idm.read_only_udm.about.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `cs_uri_scheme`, `rs_Content_Type`, `x_virus_id`, `x_bluecoat_application_name`, `cs_uri`, `s_sitename`, `x_rs_certificate_observed_errors`, `x_rs_connection_negotiated_cipher`, `x_rs_connection_negotiated_cipher_strength`, `x_rs_connection_negotiated_cipher_size`, `x_rs_connection_negotiated_ssl_version` and `s_supplier_failures` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `s_hierarchy` and `r_dns` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `c_cpu` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `x_bluecoat_application_operation`, `x_icap_reqmod_header_X_ICAP_Metadata`, `x_icap_respmod_header_X_ICAP_Metadata`, `x_rs_certificate_hostname_threat_risk`, `x_cs_Referer_uri_threat_risk`, `x_cs_Referer_uri_categories` and `cs_uri_extension` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-16 |  Enhancement:  
\- Added Grok patterns for new format of SYSLOG logs.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `c_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `c_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `cs_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `cs_host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `i_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `i_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `descrip` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `sum1` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `sum2` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `sum3` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `details` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ip_principal` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip_principal` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `t_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `t_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `t_hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `rc` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.   
2025-06-24 |  Enhancement:  
\- Added new grok patterns to support the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `transaction_id`, and `proxy_host` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified the condition for mapping `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when `principal_present` and `target_present` are true.   
2025-06-18 |  Enhancement:  
\- Added Grok patterns for new format of SYSLOG logs.  
\- Added gsub to remove `\\\\\\"` from `cs_categories` and `x_bluecoat_application_name` raw log fields.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `cs_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `cs_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `cs_refer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `rs_service_latency`, `x_icap_reqmod_header`, `x_icap_respmod_header`, `x_bluecoat_app_operation`, `x_bluecoat_total_time_added`, `policy_evaluation_time`, `x_bluecoat_appliance_name`, `cs_connection_ssl_server_name`, `rs_connection_ssl_server_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `x_data_leak_detected` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.ip , event.idm.read_only_udm.target.asset.ip: Newly mapped `r_Ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Added conditional check for `cs_uri_path` raw log field before mapping it to `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- Added conditional check for `sc_status` raw log field before mapping it to `event.idm.read_only_udm.network.http.response_code` UDM field.   
2025-06-09 |  Enhancement:  
\- Added gsub for `message` to replace unwanted data.  
\- Added grok pattern's to support new pattern of SYSLOG logs.  
\- Modified mutate block from `rename` to `replace` for fields `csv.column4`, `csv.column6`, `csv.column9`, `csv.column11`, `csv.column12`, `csv.column14`, `csv.column15`, `csv.column19`, `csv.column20`, `csv.column22`, `csv.column27`, `csv.column30`, `csv.column31`, `csv.column32`, `csv.column34`, `csv.column36`, `csv.column37`, and `csv.column39`.  
\- Added for loop for field `additional` and mapped it to `event.idm.read_only_udm.additional.fields`.  
\- Removed redundant code for `vendor_action`, `s_action`, `s-action`, `cs_username`, `cs_auth_groups`, `cs_auth_group`, `cs-auth-group`, `cs_host`, `cs-host`, `cs_uri_path`, `r_ip`, `r-ip`, `dst`, `dst_ip`, `x_ip`, `dest_ip`, `rs_status`, `sc_status`, `sc-status`, `cs-bytes`, `cs_bytes` `sc-bytes`, `sc_bytes`, `useragent`, `http_user_agent`, `cs_user_agent`, `cs-user-agent`, `cs-method`, `cs_method`, `cs_uri_scheme`, `cs_categories`, and `principal_hostname`.  
\- Added json_block to parse the json_data.   
2025-05-20 |  Enhancement:  
\- Added a `Grok` filter to extract `date` and `time` from the `msg_attrs` field.  
\- Implemented a `mutate` filter to create the `d_time` field by combining the extracted `date` and `time` values  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped `d_time` field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip: Removed mapping of `s-ip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Mapped `s-ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields: Removed mapping of `cs-uri-port` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.port: Mapped `cs-uri-port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `cs-host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname: Mapped `cs-host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `r-ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field  
\- event.idm.read_only_udm.target.ip: Removed mapping of `c-ip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Mapped `c-ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-05-14 |  Enhancement:  
\- Added a GROK pattern to retrieve data `cs_username` and `cs_hostname`.   
2025-04-03 |  Enhancement:  
\- Added a few gsubs to parse new format of logs.   
2025-03-20 |  Enhancement:  
\- Added a GROK pattern to parse SYSLOG log.  
\- Added Gsub for `ip` to remove brackets `\\]|\\[`.  
\- Added Gsub for `json_categories` to remove `\`\"".   
2025-03-13 |  Enhancement:  
\- Mapped `cs-uri-path to `target.file.names".   
2025-02-19 |  Enhancement:  
\- Added conditional check for `url`.   
2025-01-10 |  Enhancement:  
\- Mapped `dest_host` and `target_hostname` to `target.url`.   
2025-01-09 |  Enhancement:  
\- Added support for processing JSON logs in the new format.   
2024-12-23 |  Enhancement:  
\- Added a new Grok pattern to validate the hostname.   
2024-12-10 |  Enhancement:  
\- Removed mapping of `s-ip` from `target.ip` and `target.asset.ip`.  
\- Changed mapping of `x-sr-vpop-ip` from `principal.ip` and `principal.asset.ip` to `intermediary.ip`.   
2024-12-05 |  Enhancement:  
\- Mapped `target_url` to `target.url` only when its value is not `none`.   
2024-11-14 |  Enhancement:  
\- Mapped `proxy_name` and `column3` to `principal.asset.hostname`.   
2024-10-25 |  Enhancement:  
\- Added a new grok pattern to parse `cs_threat_risk` and `cs_categories`.   
2024-10-18 |  Enhancement:  
\- Added support to handle KV, CSV, and SYSLOG logs.   
2024-10-15 |  Enhancement:  
\- Mapped `upload-source` to `additional.fields`.   
2024-09-25 |  Enhancement:  
\- Added support for new format logs.   
2024-09-11 |  Enhancement:  
\- Set `metadata.event_type` to `NETWORK_HTTP` if `message` contains `SG - HTTP`.   
2024-08-29 |  Enhancement:  
\- Added support for a new log pattern.   
2024-08-22 |  Enhancement:  
\- Added support for a new log pattern.  
\- Added a Grok pattern to parse the new format of field `file_name`.   
2024-08-07 |  Enhancement:  
\- Mapped `time-taken` to `session_duration.session_duration`.   
2024-06-20 |  Enhancement:  
\- Added the new Grok patterns to parse new format of field `file_name`.   
2024-06-18 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.   
2024-06-14 |  Enhancement:  
\- Added support to parse dropped logs.   
2024-05-21 |  Enhancement:  
\- Added a Grok pattern over `x_icap_respmod_header` to extract the fields `file_reputation` and `expect_sandbox`.  
\- Mapped `x_icap_respmod_header` to `security_result.detection_fields`.  
\- Mapped `file_reputation` to `security_result.detection_fields`.  
\- Mapped `expect_sandbox` to `security_result.detection_fields`.   
2024-05-14 |  Bug-Fix:  
\- Separated `principal_user_group_identifiers` CSV values and mapped them into `principal.user.group_identifiers`.   
2024-05-09 |  Enhancement:  
\- Parsed `search_query` from `target_url` and mapped it to `target.resource.attribute.labels`.   
2024-05-06 |  Bug-Fix:  
\- Mapped `cs_auth_groups` to `principal.user.group_identifiers`.   
2024-04-25 |  Bug-Fix:  
\- Removed `column16` mapping to `target.ip` as it is being mapped to `intermediary.ip`.   
2024-02-21 |  Enhancement:  
\- Added a Grok pattern to parse new format logs.   
2024-02-16 |  Enhancement:  
\- Parsed `file_name` from `target.file.file_path` and mapped to `target.file.names`.   
2024-02-06 |  Enhancement:  
\- If `time_taken` is less than 1000, then mapped `time_taken` to `network.session_duration.nanos`, else mapped to `network.session_duration.seconds`.   
2024-01-25 |  Enhancement:  
\- Mapped `x-tenant-id` to `security_result.detection_fields`.   
2023-12-19 |  Enhancement:  
\- Added mapping of `originating_ip` to `principal.ip`.   
2023-12-13 |  Bug-Fix:  
\- Changed mapping of `cs-host` from `principal.hostname` to `target.hostname`.  
\- Added null check to `c_ip_host` prior mapping to `principal.hostname`.  
\- Mapped `s-supplier-ip` to `intermediary.ip`.  
\- Mapped `s-source-ip` to `intermediary.ip`.  
\- Mapped `cs-uri-port` to `target.port`.  
\- Mapped `x-bluecoat-application-name` to `target.application`.  
\- Mapped `x-rs-certificate-validate-status` to `network.tls.server.certificate.subject`.  
\- Mapped `x-sr-vpop-country-code` to `principal.location.country_or_region`.  
\- Mapped `cs-icap-status` to `security_result.description`.  
\- Mapped `x-rs-ocsp-error`, `x-cs-ocsp-error`, `cs-icap-error-details`, `rs-icap-error-details`, `risk-groups`, `x-rs-certificate-hostname-threat-risk`, `cs-X-Requested-With`, `x-rs-connection-negotiated-ssl-version`, `x-cs-connection-negotiated-cipher-size`, `x-rs-connection-negotiated-cipher-size`, `x-rs-connection-negotiated-cipher`, `x-bluecoat-reference-id`, `x-bluecoat-placeholder`, `wf_id`, `verdict`, `x-cloud-rs`, `x-symc-dei-via`, `x-sc-connection-issuer-keyring`, `x-client-security-posture-risk-score`, `s-supplier-failures`, `x-data-leak-detected`, `x-virus-id`, `x-rs-certificate-observed-errors`, `x-rs-connection-negotiated-cipher-strength`, to `security_result.detection_fields`.  
\- When principal and target details are present, then set `metadata.event_type` to `NETWORK_CONNECTION`.   
2023-11-27 |  Enhancement:  
\- Added support for JSON logs.  
\- Added on_error for mapping of `_network.http.response_code` to `network.http.response_code`.  
\- Initialized `date_time`, `rs_status`, `c_ip_host`, `r_port`, `json_message`, and `r_dns` to null.  
\- Added null check before mapping `rs_status` to `network.http.response_code`.  
\- Added null check to `date_time` before matching the date pattern.  
\- Mapped `x-sr-vpop-ip` to `principal.ip`.  
\- Mapped `cs-userdn` to `principal.user.userid`.  
\- Mapped `x-client-agent-type` to `principal.application`.  
\- Mapped `x-client-agent-sw` to `principal.asset.software`.  
\- Mapped `x-sr-vpop-country` to `principal.location.country_or_region`.  
\- Mapped `x-client-device-id` to `principal.resource.product_object_id`.  
\- Mapped `application-name` to `target.applcation`.  
\- Mapped `rs_content_type` to `target.file.mime_type`.  
\- Mapped `sc_status` to `network.http.response_code`.  
\- Mapped `x-bluecoat-appliance-name` to `intermediary.application`.  
\- Mapped `s-supplier-country` to `intermediary.location.country_or_region`.   
2023-11-13 |  Enhancement-  
\- Mapped `rs_server` to `security_result.about.labels`.  
\- Mapped `c_uri_path_query` to `target.file.full_path`.  
\- Mapped `time_taken` to `network.session_duration.nanos`.  
\- Added `target_hostname` to complete `target_url`,  
\- Mapped `cs_threat_risk` to `security_result.risk_score`.   
2023-10-01 |  Enhancement-  
\- Removed dropping of logs that contain `Log uploading failed`.  
\- Added check to `ip_target` prior mapping `metadata.event_type` to `NETWORK_CONNECTION`. If `ip_target` is `-` mapped `metadata.event_type` to `STATUS_UPDATE`.  
\- Logs parsed using CSV extraction instead of a Grok pattern.   
2023-08-18 |  Enhancement-  
\- Added additional Grok pattern to parse the new format syslog logs.  
\- Mapped `x_cs_connection_negotiated_cipher` to `network.tls.cipher`.  
\- Mapped `x_rs_certificate_hostname` to `network.tls.client.server_name`.  
\- Mapped `x_rs_certificate_validate_status` to `network.tls.server.certificate.subject`.  
\- Mapped `s_icap_status` to `security_result.description`.  
\- Mapped `x_cs_connection_negotiated_ssl_version` to `network.tls.version`.   
2023-06-25 |  Enhancement- Added a Grok pattern to parse unparsed logs.  
\- Changed `metadata.event_type` from `GENERIC_EVENT` to a more specific value wherever possible.   
2023-04-27 |  \- Mapped `cs(User-Agent)` to `network.http.user_agent`.  
\- Mapped `cs-uri-scheme` to `network.ip_protocol`.  
\- Added null checks to `on_error` statements for some fields.  
\- Mapped `dst_user` to `target.user.userid`.  
\- Mapped `session_id` to `network.session_id`.  
\- Added new Grok pattern for authentication log types.   
2022-09-28 |  Enhancement - Migrated customer-specific parser to default.  
\- Added `on_error` statements while replacing the values of fields as they might not be present in the log.  
\- Updated `metadata.event_type` to `NETWORK_CONNECTION` from `GENERIC_EVENT` wherever possible.  
\- Added condition check before mapping `metadata.event_type` as `STATUS_UPDATE` or `STATUS_UNCATEGORIZED` to ensure value of `target.ip` or `target.hostname` is not present as otherwise it may throw an error.   
2022-08-23 |  Enhancement -  
\- Mapped `sc_status` to `network.http.response_code`.  
\- Mapped `rule_name` to `security_result.rule_name`.  
\- Mapped `cs_method` to `network.http.method`.  
\- Mapped `application_protocol` to `network.application_protocol`.  
\- Mapped `communication_type` to `security_result.rule_name`.  
\- Mapped `rule_name` to `security_result.about.labels`.  
\- Added null check for `cs_host`, `hostname`, `cs_method`, `cs_uri_scheme`, `cs_username`, `sc_bytes`, `username`.  
\- Removed Drop statement.   
2022-05-25 |  Enhancement - Added GROK extraction for PingSSOWAF syslog.   
2022-04-20 |  Enhancement - Dropped logs with improper JSON Format.  
-on_error conditional checks are added to handle such logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
