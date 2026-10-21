---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-asm-changelog/
title: Change log for F5_ASM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:33:26.328210+00:00
---

# Change log for F5_ASM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-asm-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_ASM

Date | Changes  
---|---  
2026-07-30 |  Enhancement:  
\- Added a conditional check before already existing mapping of `suid`, `suser`, `net.peer.name`, `net_host_name` raw log fields to avoid mapping of `0` value.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `X-WorkspaceOne-Boxer-RequestId`, `MS-ASProtocolVersion`, `X-VMware-Boxer-RequestId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-07-20 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/f5-asm`.   
2026-07-17 |  Enhancement:  
\- Added Grok patterns to parse the fields correctly.  
\- Removed regex check for `message` to parse new pattern of logs.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.   
2026-06-19 |  Enhancement:  
\- Added support to parse the `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields correctly.   
2026-05-27 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed static mapping of `0.0.0.0` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `device_product` log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-05-08 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: When `c6a1Label` is `device_address`, Set the value of `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` with `c6a1`.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: When `c6a3Label` is `destination_address`, Set the value of `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` with `c6a3`.  
\- `event.idm.read_only_udm.security_result.about.ip` and `event.idm.read_only_udm.security_result.about.asset.ip`: When `c6a4Label` is `ip_address_intelligence`, Set the value of `event.idm.read_only_udm.security_result.about.ip` and `event.idm.read_only_udm.security_result.about.asset.ip` with `c6a4`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `c6a1Label`, `c6a2Label`, `c6a3Label`, `c6a4Label` raw log fields as keys to the `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `headers_kv_data.host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2026-04-28 |  Enhancement:  
\- Added a KV filter to parse the raw log fields.  
\- Modified a grok pattern on `X-Forwarded-For` to extract `XForwardedFor` and `principal_mail`.  
\- Modified a grok pattern on `column6` to extract `ip_column6` and `scope_details`.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column18` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `column19` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `column15` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `column14` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `principal_mail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `Referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Content-Length`, `Origin`, `Sec-Fetch-Site`, `Sec-Fetch-Mode`, `Sec-Fetch-Dest`, `X-XSRF-TOKEN`, `Priority`, `request_body_size`, `scope_details` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `violation_index_value`, `context_value`, `object_value`, `object_pattern_value`, `staging_value`, `content_profile_type_value`, `content_id_value`, `content_profile_id_value`, `content_profile_name_value`, `buffer_value`, `content_profile_index_value`, `content_profile_location_value`, `content_profile_error_code_value`, `content_profile_specific_desc_value`, `content_profile_fault_detail_value` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-14 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority_value`, `headers_kv_data.bundle-version`, `microservice`, `threatCampaignNames`, `stagedThreatCampaignNames`, `Ipv4AddressIntelligence`, `IpIntelligenceCategory`, `c6a1`, `c6a2`, `c6a3`, `c6a4` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `headers_kv_data.host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `headers_kv_data.device-id` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `headers_kv_data.app-version` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `json_parsed_data.device.model`, `json_parsed_data.device.manufacturer`, `json_parsed_data.device.build_number`, `json_parsed_data.device.os`, `json_parsed_data.device.sdk_int`, `json_parsed_data.device.app_signature`, `json_parsed_data.device.app_version` raw log fields with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform_version`: Newly mapped `json_parsed_data.device.os_version` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `json_parsed_data.username`,`json_parsed_data.request_id`, `headers_kv_data.content-type`, `headers_kv_data.accept-encoding`,`headers_kv_data.signature`, `headers_kv_data.sequence_id`, raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.creation_time`: Newly mapped `json_parsed_data.timestamp` raw log field with `event.idm.read_only_udm.principal.asset.attribute.creation_time UDM` field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Newly mapped `headers_kv_data.platform` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `cs3` to extract `request_line`, `headers_string`, `json_body`.  
\- Modified the conditional check before mapping `sec_result_category_details` field with `event.idm.read_only_udm.security_result.category_details` UDM field to exclude `N/A` values.  
\- Modified the conditional check before mapping `suser` field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field to exclude `N/A` values.  
\- Added a JSON filter to parse `json_body` into `json_parsed_data`.  
\- Added a KV filter to parse `headers_string` into `headers_kv_data`.   
2026-03-27 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `column24` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `column29` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `column8` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column10`, `accept`, `accept_encoding`, `header_one`, `check_id` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `requestMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.network.tls.version`: Newly mapped `http_version` raw log field with `event.idm.read_only_udm.network.network.tls.version` UDM field.  
\- Added a conditional check for `column23`.  
\- Added a grok pattern in order to handle new pattern of syslog logs.  
\- Added a grok pattern on column13 to extract accept, accept_encoding, header_one, useragent, check_id, host.   
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `X-AnchorMailbox` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `X-OWA-ExplicitLogonUser` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `X-OWA-CorrelationId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority`, `facility`, `deviceExternalId`, `X-OWA-ActionName`, `X-OWA-Attempt`, `X-OWA-CANARY`, `client-request-id`, `sec-ch-ua-mobile`, `Action`, `X-Requested-With`, `cs2`, `X-OWA-ActionId`, `cn3` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `X-OWA-UrlPostData`, `X-OWA-ClientBuildVersion`, `sec-ch-ua` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: If `sec-ch-ua-platform` is `iOS`, updated the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `IOS` else if `sec-ch-ua-platform` is `Android`, updated the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `ANDROID` else if `sec-ch-ua-platform` is `Windows`, updated the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `WINDOWS` else if `sec-ch-ua-platform` is `MAC`, updated the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `MAC` else if `sec-ch-ua-platform` is `Other`, updated the value of `event.idm.read_only_udm.principal.asset.platform_software.platform` to `UNKNOWN_PLATFORM`.  
\- Added a Grok pattern to parse the `cs3` field and extract the `cs3data` field.  
\- Added kv filter for `cs3data` field to extract key value pairs.  
\- Added support for new pattern of JSON logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device`.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device_version`.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.principal.url`: Removed mapping of `client_request_uri` from `event.idm.read_only_udm.principal.url`. As the client is target here, this field should be populated for the target.  
\- `event.idm.read_only_udm.target.url`: Mapped `client_request_uri` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `bigip_mgmt_ip` from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`. As this mapping is relevant for the intermediary.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `bigip_mgmt_ip` raw log field to `event.idm.read_only_udm.intermediary.ip`.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Removed mapping of `f5_host` from `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`. This field is incorrectly populating in target and should only be present in the intermediary  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `f5_host` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `device_product`,`configuration_date_time`, `actual_mitigation_action`, `configured_mitigation_action` and `actual_mitigation_action_reason` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.   
2025-12-23 |  Enhancement:  
\- Modified the grok pattern to handle the new pattern of logs.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `summary` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `rule_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `requestClientApplication` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `product_name` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `cs3` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `pathContext` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `f5_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-04 |  Enhancement:  
\- Added support to remove back slash `\` from raw log.  
\- event.idm.read_only_udm.principal.user.userid: Removed `N/A` value from `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.description: Removed `N/A` value from `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed `N/A` value from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Removed `N/A` value from `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Removed `N/A` value from `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.target.asset_id and event.idm.read_only_udm.target.asset.asset_id: Removed `N/A` value from `event.idm.read_only_udm.target.asset_id` and `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.network.http.method: Removed `N/A` value from `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Removed `N/A` value from `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.url: Removed `N/A` value from `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Removed `N/A` value from `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Removed `N/A` value from `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `refer_url` (from `cs3`) raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `staged_sig_names` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new timestamp pattern for `date_time` raw log field.  
\- Added gsubs for `target_hostname`, `f5_host`, `response` to extract data correctly.   
2025-11-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `net.transport, net.host.port, net.peer.port, net.peer.name` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Added a grok pattern in order to handle new pattern of syslog logs.   
2025-09-02 |  Enhancement:  
\- Added a conditional check using the `has_severity` field. This ensures that the generic fallback logic for `event.idm.read_only_udm.security_result.severity` is executed only when a more specific severity has not already been assigned, preventing more precise severity levels from being overwritten.   
2025-08-20 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `net.host.ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `net.host.ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `net.peer.ip` raw log field(s) with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `net.peer.ip` raw log field(s) with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `net.peer.name` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `net.peer.name` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `net.host.name` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `net.host.name` raw log field(s) with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `net.host.port` raw log field(s) with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `net.peer.port` raw log field(s) with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `vs_name` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `captcha_result`, `policy_apply_date` and `request` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Converted type to boolean with error handling for `message_json_parse_failure_conversion_error`.  
\- Modified the drop logic to only drop if the message is not JSON and doesn't match other patterns.   
2025-08-11 |  Enhancement:  
\- Added JSON filter to parse unparsed JSON logs.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields.   
2025-07-10 |  Enhancement:  
\- Added grok patterns to extract `action` raw log field from the logs.  
\- event.idm.read_only_udm.security_detection_fields: Newly mapped `action`, `dos_attack_detection_mode`, `dos_attack_event`, `dos_attack_id`, `dos_attack_latency`, `dos_attack_name`, `dos_attack_tps`, `dos_mitigation_action`, and `dos_mitigation_reason` raw logs field with `event.idm.read_only_udm.security_detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `context_type`, `dos_baseline_latency`, `dos_baseline_tps`, `dos_incoming_requests_count`, `dos_dropped_requests_count`, `errdefs_msg_name`, `reported_entity_type` and `event_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field and set `has_principal` to `true`.  
\- event.idm.read_only_udm.intermediary.asset.attribute.labels: Newly mapped `device_blade` and `partition_name` raw log fields with `event.idm.read_only_udm.intermediary.asset.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-06-27 |  Enhancement:  
\- Added grok patterns to handle the dropped logs.  
\- Renamed `SOAPAction` to `addition.SOAPAction`, `externalId` to `addition.externalId`, `attempts` to `addition.attempts`, `tty` to `addition.tty`, `audit_component` to `addition.audit_component`, `errdefs_msgno` to `addition.errdefs_msgno`, `route_domain` to `addition.route_domain`, `profile_name` to `addition.profile_name`, `action` to `addition.action`, `previous_action` to `addition.previous_action`, `bot_signature` to `addition.bot_signature`, `bot_signature_category` to `addition.bot_signature_category`, `bot_name` to `addition.bot_name`, `class` to `addition.class`, `anomaly_categories` to `addition.anomaly_categories`, `anomalies` to `addition.anomalies`, `micro_service_name` to `addition.micro_service_name`, `micro_service_type` to `addition.micro_service_type`, `micro_service_matched_wildcard_url` to `addition.micro_service_matched_wildcard_url`, `micro_service_hostname` to `addition.micro_service_hostname`, `browser_configured_verification_action` to `addition.browser_configured_verification_action`, `browser_actual_verification_action` to `addition.browser_actual_verification_action`, `new_request_status` to `addition.new_request_status`, `enforced_by` to `addition.enforced_by`, `mobile_is_app` to `addition.mobile_is_app`, `challenge_failure_reason` to `addition.challenge_failure_reason`, `client_type` to `addition.client_type`, `application_display_name` to `addition.application_display_name`, `Accept-Language` to `addition.Accept-Language`, `Content-Type` to `addition.Content-Type`, `support_id` to `addition.support_id`, `form_data` to `addition.form_data`, `query_string` to `addition.query_string`, `req_status` to `addition.req_status`, `resp` to `addition.resp`, `violate_rate` to `addition.violate_rate`, `ip_addr_intelli` to `addition.ip_addr_intelli`, `geo_info` to `addition.geo_info`, `websocket_message_type` to `addition.websocket_message_type`, `Cookie` to `addition.Cookie`, `Accept-Encoding` to `addition.Accept-Encoding`, `Accept-Charset` to `addition.Accept-Charset`, `Keep-Alive` to `addition.Keep-Alive`, `Connection` to `addition.Connection`, `Pragma` to `addition.Pragma`, `Cache-Control` to `addition.Cache-Control`, `Accept` to `addition.Accept`, `sub_violations` to `addition.sub_violations`, `and violation_rating` to `addition.violation_rating`.  
\- Updated the mapping of `event.idm.read_only_udm.additional.fields` to utilize a generalized map for fields `SOAPAction`, `support_id`, `externalId`, `attempts`, `tty`, `audit_component`, `errdefs_msgno`, `route_domain`, `profile_name`, `action`, `previous_action`, `bot_signature`, `bot_signature_category`, `bot_name`, `class`, `anomaly_categories`, `anomalies`, `micro_service_name`, `micro_service_type`, `micro_service_matched_wildcard_url`, `micro_service_hostname`, `browser_configured_verification_action`, `browser_actual_verification_action`, `new_request_status`, `enforced_by`, `mobile_is_app`, `challenge_failure_reason`, `client_type`, `application_display_name`, `Accept-Language`, `Content-Type`, `form_data`, `query_string`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.detection_fields` to utilize a generalized map for fields `req_status`, `resp`, `violate_rate`, `ip_addr_intelli`, `geo_info`, `websocket_message_type`, `Cookie`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.about.resource.attribute.labels` to utilize a generalized map for fields `Accept-Encoding`, `Accept-Charset`, `Keep-Alive`, `Connection`, `Pragma`, `Cache-Control`, `Accept`, `sub_violations`, `violation_rating`.  
\- Consolidate the mapping of `severity` and `level` to eliminate redundant code.  
\- Removed redundant mapping of `event.idm.read_only_udm.security_result`.  
\- Removed redundant mapping of `event.idm.read_only_udm.network.http.response_code` and used common field `network_http_response_code` and mapped it to `event.idm.read_only_udm.network.http.response_code`.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.port` and used common field `target_port` and mapped it to `event.idm.read_only_udm.target.port`.  
\- Removed redundant mapping of `event.idm.read_only_udm.principal.port` and used common field `principal_port` and mapped it to `event.idm.read_only_udm.principal.port`.  
\- Removed redundant code for field `attack_type`.  
\- Renamed `security_result` to `sec_result`.  
\- If `has_principal` is `true` and `has_target` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` and `event.idm.read_only_udm.network.application_protocol` to `HTTP`.  
\- If `has_target` is `false` and `has_principal` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2025-06-02 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action_details, event.idm.read_only_udm.security_result.action: Newly mapped `req_status` raw log field with `event.idm.read_only_udm.security_result.action` and `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- if `act` is `alerted` and `cn1` is not `0` then set `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `deviceCustomDate1` and `deviceCustomDate1Label` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Added grok pattern to extract IP address from `c6a2` raw log field then mapped `source_ip` with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field if `c6a2Label` is `source_address`.  
\- event.idm.read_only_udm.metadata.event_type: If principal data and target data is present then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- Added grok pattern for `cs3` raw log field to extract `incap_client_ip` and `refer_url` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip, event.idm.read_only_udm.principal.ip: Newly mapped `incap_client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `refer_url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.   
2025-05-21 |  Enhancement:  
\- Added a new grok pattern in order to parse log with `kv_data_1` and `kv_data_2` raw log fields.  
\- Added a new kv filter for `kvdata1` and `kvdata2` raw log fields.   
2025-04-16 |  Enhancement:  
\- Added a Grok pattern to parse `event.idm.read_only_udm.network.http.user_agent` UDM field from `cs5` raw log field.   
2025-04-02 |  Enhancement:  
\- Modified and added few gsubs to ensure proper parsing of KV format logs.  
\- Added IP check for field `src` using grok before mapping it to `principal.nat_ip`.   
2025-03-10 |  Enhancement:  
\- Mapped `cn1` to `additional.fields`.  
\- Mapped `security_result.action` to `BLOCK` when `cn1` is `0`.   
2025-02-11 |  Enhancement:  
\- Mapped `column3` to `principal.ip` and `principal.asset.ip`  
2025-02-04 |  Enhancement:  
\- Added a `gsub` to remove non-utf8 characters from `uri` field when it contains non-utf8 characters to parse logs.   
2025-01-30 |  Enhancement:  
\- Removed the `cs5` field from `_intermediary.ip` and `_intermediary.asset.ip`.  
\- Mapped `src` to `principal.nat_ip`.  
\- Mapped `cs5` to `principal.ip` and `principal.asset.ip`.   
2025-01-17 |  Enhancement:  
\- Removed the drop condition to parse logs with non-utf8 characters.   
2024-12-11 |  Enhancement:  
\- Modified a Grok Pattern to support a new format of syslog logs.   
2024-11-28 |  Enhancement:  
\- Changed the mapping of `Referer` from `network.http.referral_url` to `target.url`.   
2024-11-07 |  Enhancement:  
\- Mapped `exec_data` to `target.process.command_line`.  
\- Mapped `src` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `cs3` to `additional.fields`.   
2024-10-30 |  Enhancement:  
\- Added support to handle CSV logs.   
2024-10-28 |  Enhancement:  
\- Modified existing Grok pattern to handle ISP block and ISP GEO block.   
2024-10-25 |  Enhancement:  
\- Mapped `form_data` to `additional.fields`.   
2024-10-23 |  Enhancement:  
\- Mapped `SOAPAction` to `additional.fields`.   
2024-09-30 |  Enhancement:  
\- Mapped `link` to `target.url`  
\- When the message contains `DROP` then set `security_result.action` to `BLOCK`.  
\- When the message contains `allowed` then set `security_result.action` to `ALLOW`.   
2024-08-07 |  Enhancement:  
\- Modified existing Grok pattern to handle CEF logs.  
\- Mapped `suid` to `principal.user.userid`.  
\- Mapped `suser` to `principal.user.user_display_name`.  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `severity` to `security_result.severity`.   
2024-07-15 |  Enhancement:  
\- Added support to handle the SYSLOG + KV logs.   
2024-06-17 |  Enhancement:  
\- Added support for a new pattern of CSV logs.   
2024-06-11 |  Enhancement:  
\- Added KV block to handle unparsed KV logs.  
\- Formatted CSV logs using `gsub` to parse CSV logs.   
2024-05-13 |  Enhancement:  
\- Added KV block to parse KV logs.  
\- Added `gsub` to remove unwanted characters.   
2024-04-19 |  Enhancement:  
\- Handled CSV unparsed logs.  
\- Added a Grok pattern to map `resp_code`.  
\- Mapped `errdefs_msgno`, `support_id_array`, `audit_component` to `additional.fields`.  
\- Mapped `descrip` to `metadata.description`.   
2024-04-08 |  Enhancement:  
\- Added support to parse newly ingested unparsed logs.   
2024-04-05 |  Bug-Fix:  
\- Added condition to parse dropped ASF CEM logs.   
2024-02-27 |  Bug-Fix:  
\- When `cs5` field has a valid IP address, then mapped to `principal.ip`.  
\- Aligned `principal.ip` and `principal.asset.ip` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- Aligned `target.ip` and `target.asset.ip` mappings.  
\- Aligned `target.hostname` and `target.asset.hostname` mappings.   
2024-01-12 |  Enhancement:  
\- Mapped `severity` to `security_result.severity_details`.  
\- Mapped `resp_code` to `http.response_code`.  
\- Mapped `virus_name` to `security_result.threat_name`.  
\- Mapped `ip_route_domain` to `principal.ip`.  
\- Mapped `geo_info`, `resp`, `req_status`, `violate_rate`, and `ip_addr_intelli` to `security_result.detection_fields`.   
2023-12-15 |  Enhancement:  
\- Handled newly ingested set of logs where `metadata.event_type` is `GENERIC_EVENT` and `network.application_protocol` is `HTTP`.  
\- Set `network.ip_protocol` to `UDP` if message contains `UDP`.  
\- Removed hardcoding value of `network.application_protocol`.  
\- Set `network.application_protocol` to `HTTP` and `HTTPS` if `message` has `HTTP` and "HTTPS, respectively.  
\- Set `network.application_protocol` to `HTTP` if `metadata.event_type` is `NETWORK_HTTP`.  
\- Added two Grok patterns to parse `principal_ip` and `src_port` from newly ingested logs.  
\- Mapped `message_body` to `metadata.description`.  
\- Mapped `tmm_msg` to `metadata.description`  
2023-12-07 |  Enhancement:  
\- Added a new Grok pattern to parse new KV+XML logs.  
\- Added KV filters to parse unparsed KV logs.  
\- Added XML filters to parse unparsed XML logs.  
\- Mapped `policy_name` to `security_result.about.resource.name`.  
\- Mapped `viol_name` to `security_result.detection_fields`.  
\- Mapped `response_code` to `network.http.response_code`.  
\- Modified Grok pattern to map complete `Referer` field to `network.http.referral_url`.  
\- Mapped `parseduseragent` to "network.http.parsed_user_agent.   
2023-11-08 |  Enhancement:  
\- Added a new Grok pattern to parse new KV logs.  
\- Added a KV filter to parse uparsed KV logs.  
\- Mapped `bigip_mgmt_ip`, `client_ip_geo_location`, `client_port`, `client_request_uri`, `device_version`, `http_method`, `route_domain` and `virtual_server_name` to `principal.ip`, `principal.location.country_or_region`, `principal.port`, `principal.url`, `metadata.product_version`, `network.http.method`, `additional.fields`, `network.tls.client.server_name`, respectively.  
\- Added `legal` to `request_status` condition to map `security_result.action_details` as `ALLOW`.  
\- Mapped `profile_name`, `action`, `previous_action`, `bot_signature`, `bot_signature_category`, `bot_name`, `class`, `anomaly_categories`, `anomalies`, `micro_services_name`, `micro_services_type`, `micro_services_matched_wildcard_url`, `micro_services_hostname`, `browser_configured_verification_action`, `browser_actual_verification_action`, `new_request_status`, `mobile_is_app`, `enforced_by`, `application_display_name`, `client_type`, and `challenge_failure_reason` to `additional.fields`.   
2023-10-19 |  Enhancement:  
\- Added a Grok pattern to extract the value of `Referer` field as `referer` from CEF logs.  
\- Mapped `referer` to `network.http.referral_url`.   
2023-09-27 |  Bug-Fix:  
\- Set `security_result.action` to `BLOCK` and `security_result.action_details` to `blocked` for logs having `request_status = blocked`.  
\- Set `security_result.action` to `ALLOW` and `security_result.action_details` to `passed` for logs having `request_status = passed`.  
\- Set `security_result.action` to `QUARANTINE` and `security_result.action_details` to `alerted` for logs having `request_status = alerted`.   
2023-08-07 |  Enhancement:  
\- Mapped `management_ip_address` to `metadata.intermediary.ip`.  
\- Mapped `request_status` to `security_result.action`.  
\- Mapped `query_string` to `additional.fields`.  
\- Mapped `sig_ids` to `security_result.rule_id`.  
\- Mapped `sig_names` to `security_result.rule_name`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `policy_name` to `security_result.about.resource.name`.  
\- Mapped `sub_violations` to `security_result.about.resource.attribute.labels`.  
\- Mapped `violation_rating` to `security_result.about.resource.attribute.labels`.  
\- Mapped `websocket_direction` to `network.direction`.  
\- Mapped `websocket_message_type` to `security_result.detection_fields`.   
2023-07-27 |  Bug-Fix:  
\- Added a new field `target_app` to contain value corresponding to `target.application`.  
\- Mapped the field `process` to `target.application` only when value of the field `target_app` is null.  
\- Converted the field `process` to `string` if it's already not a string.   
2023-07-03 |  Enhancement:  
\- Mapped `externalId` to "`additional.fields`.  
\- Mapped the event time to "`metadata.event_timestamp`.   
2023-05-12 |  Enhancement - For CEF format logs, mapped the information about the attack to `security_result.description`.   
2023-04-06 |  Enhancement:  
\- Login event parsed as `USER_LOGIN` instead of `STATUS UPDATE`.  
\- Parsed the username value in `firstname.lastname` and mapped to `principal.user.userid`.   
2023-02-09 |  Enhancement- Parsed the logs containing `type=irule` by adding new grok pattern and mapped the following fields:  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `data.sessionid` to `network.session_id`.  
\- Mapped `data.bits` to `network.sent_bytes`.  
\- Mapped `data.version` to `network.tls.version`.  
\- Mapped `client_ip` to `principal.ip`.  
\- Mapped `client_port` to `principal.port`.  
\- Mapped `snat_ip` to `principal.nat_ip`.  
\- Mapped `snat_port` to `principal.nat_port`.  
\- Mapped `server_ip` to `target.ip`.  
\- Mapped `server_port` to `target.port`.  
\- Mapped `irule` to `security_result.rule_name`.  
\- Mapped `irule-version` to `security_result.rule_version`.  
\- Mapped `proxy_id` to `security_result.rule_id`.  
\- Mapped `virtualserver` to `network.tls.client.server_name`.   
2022-11-03 |  Enhancement:  
\- Added a condition for unparsed CEF format logs.  
\- Added a condition to check for sshd and httpd user_login logs.  
\- Added grok patterns to parse httpd and sshd user_login success/failure logs.  
\- Mapped `event_id` to `metadata.product_log_id`.  
\- Mapped `application` to `target.application`.  
\- Mapped `prin_ip` to `principal.ip`.  
\- Mapped `SSH` to `app_protocol` when `tty` is `ssh` or `applicaition` is `sshd`.  
\- Mapped `user_id` `principal.user.user_id`.  
\- Mapped `USER_LOGIN` to `metadata.event_type` for httpd/sshd user_login logs.  
\- Mapped `auth_level` to `principal.user.attribute.roles`.  
\- Mapped `addr` from log to `target.ip`  
\- Mapped `port` from log to `target.port`  
2022-09-21 |  Enhancement:  
\- Migrated customer specific to default parser.   
2022-05-17 |  Enhancement: Enhanced the parser to parse the header of the HTTP request.   
2022-04-27 |  Bug - Fix:  
\- Enhanced the parser to parse logs with the `ASM:` format.   
2022-04-26 |  Enhanced the parser to handle unparsed raw logs   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
