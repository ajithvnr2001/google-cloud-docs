---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-avinetworks-iwaf-changelog/
title: Change log for VMWARE_AVINETWORKS_IWAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:22.976551+00:00
---

# Change log for VMWARE_AVINETWORKS_IWAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-avinetworks-iwaf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_AVINETWORKS_IWAF

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- Added grok patterns to parse syslog-JSON logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `headers_sent_to_server.X-Forwarded-For` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `vs_name` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields when `vs_name_syslog` is not present.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `gslbservice`, `gslbservice_name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `rx_bytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `tx_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `rx_pkts` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `tx_pkts` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Mapped `DNS` to `event.idm.read_only_udm.network.application_protocol` UDM field when DNS fields (`dns_fqdn`, `dns_qtype`, `dns_request.identifier`) are present.  
\- `event.idm.read_only_udm.network.dns.questions`: Newly mapped `dns_fqdn` raw log fields with `event.idm.read_only_udm.network.dns.questions.name` and `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions`: Newly mapped `dns_qtype` raw log fields with `event.idm.read_only_udm.network.dns.questions.name` and `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.id`: Newly mapped `dns_request.identifier` raw log field with `event.idm.read_only_udm.network.dns.id` UDM field.  
\- `event.idm.read_only_udm.network.dns.authoritative`: Newly mapped `dns_response.authoritative_answer` raw log field with `event.idm.read_only_udm.network.dns.authoritative` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `dns_request.client_location.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `dns_request.client_location.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `dns_request.client_location.name` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `headers_sent_to_server.User-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field when `user_agent` raw log field is empty.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `max_ingress_latency_be`, `avg_ingress_latency_be`, `conn_est_time_be` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator_id`, `ingestiontag`, `servicetag`, `xff`, `etag`, `http_request_policy_rule_name`, `ssl_signature_algorithm`, `jwt_log.is_jwt_verified`, `start_timestamp`, `total_time`, `connection_ended`, `mss`, `out_of_orders`, `retransmits`, `timeouts`, `zero_window_size_events`, `server_total_bytes`, `server_rx_bytes`, `server_tx_bytes`, `server_total_pkts`, `server_rx_pkts`, `server_tx_pkts`, `server_out_of_orders`, `server_retransmits`, `server_timeouts`, `server_zero_window_size_events`, `dns_etype`, `dns_qtype`, `dns_response.response_code`, `dns_response.authoritative_answer`, `dns_response.truncation`, `dns_response.recursion_available`, `dns_response.answer_records_count`, `dns_response.nameserver_records_count`, `dns_response.additional_records_count`, `dns_response.query_or_response`, `dns_response.opcode`, `dns_response.recursion_desired`, `dns_response.question_count`, `dns_response.is_wildcard`, `dns_response.fallback_algorithm_used`, `dns_request.query_or_response`, `dns_request.opcode`, `dns_request.recursion_desired`, `dns_request.checking_disabled`, `dns_request.authentic_data`, `dns_request.question_count`, `dns_request.answer_records_count`, `dns_request.nameserver_records_count`, `dns_request.additional_records_count`, `dns_request.opt_record.version`, `dns_request.opt_record.udp_payload_size`, `dns_request.opt_record.dnssec_ok`, `dns_request.opt_record.options.code`, `dns_request.opt_record.options.addr_family`, `dns_request.opt_record.options.source_prefix_len`, `dns_request.opt_record.options.scope_prefix_len`, `dns_request.opt_record.options.subnet_ip`, `all_request_headers.Accept-Encoding`, `all_response_headers.X-AREQUESTID`, `all_response_headers.X-ANODEID`, `all_response_headers.Referrer-Policy`, `all_response_headers_X_XSS_Protection`, `all_response_headers.X-Content-Type-Options`, `all_response_headers.Content-Security-Policy`, `all_response_headers.Server-Timing`, `all_response_headers.X-Seraph-LoginReason`, `all_response_headers.X-RateLimit-Limit`, `all_response_headers.X-RateLimit-Remaining`, `all_response_headers.X-RateLimit-FillRate`, `all_response_headers.X-RateLimit-Interval-Seconds`, `all_response_headers.Retry-After`, `all_response_headers.Content-Encoding`, `all_response_headers.Vary`, `headers_sent_to_server.Accept`, `headers_sent_to_server.User-Agent`, `headers_sent_to_server.Authorization`, `headers_sent_to_server.Accept-Encoding`, `headers_received_from_server.Date`, `headers_received_from_server.X-Frame-Options`, `headers_received_from_server.X-AREQUESTID`, `headers_received_from_server.X-ANODEID`, `headers_received_from_server.Referrer-Policy`, `headers_received_from_server_X_XSS_Protection`, `headers_received_from_server.X-Content-Type-Options`, `headers_received_from_server.Content-Security-Policy`, `headers_received_from_server.Strict-Transport-Security`, `headers_received_from_server.Server-Timing`, `headers_received_from_server.X-Seraph-LoginReason`, `headers_received_from_server.X-RateLimit-Limit`, `headers_received_from_server.X-RateLimit-Remaining`, `headers_received_from_server.X-RateLimit-FillRate`, `headers_received_from_server.X-RateLimit-Interval-Seconds`, `headers_received_from_server.Retry-After`, `headers_received_from_server.Content-Encoding`, `headers_received_from_server.Vary`, `Set-Cookie`, `Strict-Transport-Security`, `Server-Timing`, `Content-Type`, `X-XSS-Protection`, `client_rtt`, `server_src_port`, `server_dest_port`, `all_response_headers.Set-Cookie` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-10 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.ip`: Removed mapping of `service_engine` from `event.idm.read_only_udm.intermediary.ip` UDM field when `service_engine` is not an IP address.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `service_engine` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.log_type`: Newly mapped `VMWARE_AVINETWORKS_IWAF` to `event.idm.read_only_udm.metadata.log_type` UDM field.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `significant`, `udf`, `vcpu_id`, `rewritten_uri_path`, `compression_percentage`, `client_insights`, `max_ingress_latency_fe`, `avg_ingress_latency_fe`, `conn_est_time_fe`, `tenant_name` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Modified the mapping logic for the `service_engine` raw log field: if `service_engine` is an IP address then maps to `event.idm.read_only_udm.intermediary.ip` else maps to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Modified the mapping logic for the `log_id_syslog` raw log field: if `log_id_syslog` is not similar to `NIL` then maps to `event.idm.read_only_udm.metadata.product_log_id`.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Added a new grok pattern to parse new format of logs this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.about.hostname`  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.intermediary.port`  
\- `event.idm.read_only_udm.network.http.method`  
\- `event.idm.read_only_udm.network.http.referral_url`  
\- `event.idm.read_only_udm.network.http.response_code`  
\- `event.idm.read_only_udm.network.http.user_agent`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.network.session_duration.seconds`  
\- `event.idm.read_only_udm.observer.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.target.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.target.url`  
2025-11-10 |  \- `event.idm.read_only_udm.observer.ip`: Removed mapping of `service_engine` from `event.idm.read_only_udm.observer.ip` UDM field to better reflect the service engine role as an active component in the event path rather than a passive observer.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `service_engine` raw log field to the `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Updated value from `Vmware` to `AVI Load Balancer`.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Updated value from `Vmware Avinetworks iWAF` to `Vmware`.   
2025-10-16 |  \- Modified the grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `redirected_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `server_side_redirect_uri`, `all_request_headers_accept_language`, `all_request_headers_cookie`, `all_response_headers_location`, `all_response_headers_x_frame_options`, `all_response_headers_content_length`, `headers_sent_to_server_x_forwarded_proto` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-25 |  \- Added a grok pattern to parse the logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `report_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `vs_name_syslog` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id_syslog` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `client_src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `vs_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `virtualservice`, `pool_name`, `pool` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `all_response_headers_date`, `all_response_headers_expires`, `rule_log.phase`, `rule_log.rule_id`, `rule_log.rule_group`, `rule_log.msg`, `rule_log_rule_name`, `tag`, `cacheable`, `persistent_session_id`, `uri_path`, `adf`, `server_rtt`, `server_response_length`, `server_response_code`, `compression`, `servers_tried`, `waf_log.latency_request_header_phase`, `response_content_type`, `response_time_first_byte`, `response_time_last_byte`, `http_version`, `request_headers`, `response_headers`, `request_id`, `value`, `ssl_session_id`, `ssl_version`, `ssl_cipher`, `host`, `server_response_time_first_byte`, `server_response_time_last_byte`, `server_ssl_session_id`, `server_connection_reused`, `waf_log.rules_configured`, `waf_log.rules_executed`, `waf_log.latency_request_body_phase`, `waf_log.latency_response_header_phase`, `waf_log.latency_response_body_phase`, `all_request_headers.pragma`, `all_request_headers.accept`, `all_request_headers.connection`, `all_request_headers.host`, `all_request_headers.iv-user`, `all_request_headers.referer`, `all_request_headers.via`, `all_request_headers.x-requestmanager-memo`, `all_request_headers.x-request-memo`, `all_request_headers.iv_server_name`, `all_request_headers.x-scan-memo`, `all_request_headers.x-wipp`, `all_response_headers_content_type`, `all_response_headers_transfer_encoding`, `all_response_headers_connection`, `all_response_headers_pscache_handler`, `all_response_headers_ignoreportalregisteredurl`, `all_response_headers_pscache_excludeparams`, `all_response_headers_portalcachecontent`, `all_response_headers_set_cookie`, `all_response_headers_pscache_control`, `all_response_headers_portalregisteredurl`, `all_response_headers_strict_transport_security`, `headers_sent_to_server_host`, `headers_sent_to_server_accept`, `headers_sent_to_server_iv_user`, `headers_sent_to_server_referer`, `headers_sent_to_server_user_agent`,`headers_sent_to_server_via`, `headers_sent_to_server_x_requestmanager_memo`, `headers_sent_to_server_x_request_memo`, `headers_sent_to_server_iv_server_name`, `headers_sent_to_server_x_scan_memo`, `headers_sent_to_server_x_wipp`, `headers_sent_to_server_pragma`, `headers_received_from_server_transfer_encoding`, `headers_received_from_server_content_type`, `headers_received_from_server_pscache_handler`, `headers_received_from_server_ignoreportalregisteredurl`, `headers_received_from_server_pscache_excludeparams`, `headers_received_from_server_portalcachecontent`, `headers_received_from_server_set_cookie`, `headers_received_from_server_pscache_control`, `headers_received_from_server_portalregisteredurl`, `headers_received_from_server_usesportalrelativeurl`, `matches.is_internal`, `matches.match_element`, `matches.match_value` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `client_rtt` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `request_length` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `response_length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `request_state` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `uri_query` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.about.hostname`: Newly mapped `server_name` raw log field with `event.idm.read_only_udm.about.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.port`: Newly mapped `server_src_port` raw log field with `event.idm.read_only_udm.intermediary.port` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `service_engine`, `server_conn_src_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.detection_fields`: Newly mapped `waf_log.status` raw log field with `event.idm.read_only_udm.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `server_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.   
2025-01-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
