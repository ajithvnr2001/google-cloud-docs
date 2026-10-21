---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dcs-changelog/
title: Change log for F5_DCS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:11:23.952269+00:00
---

# Change log for F5_DCS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-dcs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_DCS

Date | Changes  
---|---  
2026-04-01 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `rsp_size` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.network.received_bytes`: Mapped `rsp_size` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field in order to introduce more accurate mapping.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- Added gsub to remove unwanted characters from the `user_agent` raw log field for correct parsing.   
2025-12-28 |  Enhancement:  
\- event.idm.read_only_udm.target.ip: Removed mapping of `user_ip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` as it is better suited for `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.ip: Mapped `user_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `x_forwarded_for` from `event.idm.read_only_udm.intermediary.ip` UDM field and updated it`s mapping logic to reflect the header`s standard structure (client, proxy1, proxy2...):  
\- The first IP (identifying the client) is mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- Subsequent IPs (identifying proxies) are mapped to `event.idm.read_only_udm.intermediary.ip`.  
\- Updated conditional logic for `waf_action`, it is now only mapped to the `action` field if the `action` field is not already populated. Otherwise, `waf_action` is added to `security_result.detection_fields`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `has_sec_event` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-18 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `node_id`, `sample_rate`, `time_to_first_downstream_tx_byte`, `time_to_first_upstream_rx_byte`, `time_to_first_upstream_tx_byte`, `time_to_last_downstream_tx_byte`, `time_to_last_rx_byte`, `time_to_last_upstream_rx_byte`, `time_to_last_upstream_tx_byte`, `timeseries_enabled`, `sni`, `terminated_time`, `rtt_downstream_seconds`, `rtt_upstream_seconds`, `rsp_code_details`, `authority`, `connected_time`, `req_id`, `proxy_type`, `vh_type`, `dst_instance`, `lb_port`, `mtls`, `ja4_tls_fingerprint`, `duration_with_data_tx_delay` and `dst_site` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol and scheme` raw log fields with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_cipher_suite` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.principal.browser.browser_type`: Newly mapped `browser_type` raw log field with `event.idm.read_only_udm.principal.browser.browser_type` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.mime_type`: Newly mapped `content-type` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- `security_result.detection_fields`: Newly mapped `response_flags`, waf_action, connection_state, device_type, accept, and policy_hits` raw log fields with `security_result.detection_fields` UDM field.  
\- `security_result.detection_fields`: Removed mapping of `as_org` from `security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.organization_name`: Mapped `as_org` raw log field to `event.idm.read_only_udm.network.organization_name` UDM field.  
\- `security_result.detection_fields`: Removed mapping of `asn` from `security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.asn`: Mapped `asn` raw log field to `event.idm.read_only_udm.network.asn` UDM field.  
\- `security_result.detection_fields`: Removed mapping of `vh_name` from `security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `vh_name` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `rsp_code` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Mapped `rsp_code` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `original_path` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Mapped `original_path` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `original_authority` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.   
2025-08-12 |  Enhancement:  
\- Added support for new format of SYSLOG+JSON logs.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `waf_mode` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `tenant` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `bot_info_classification` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `bot_info_name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `bot_info_type` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.namespace: Newly Mapped `src` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly Mapped `kubernetes_labels_app` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly Mapped `kubernetes_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly Mapped `kubernetes_container_name` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.   
2025-04-25 |  Enhancement:  
\- Added a conditional check before mapping `latitude` to `event.idm.read_only_udm.principal.location.region_latitude`.  
\- Added a conditional check before mapping `longitude` to `event.idm.read_only_udm.principal.location.region_longitude`.  
\- Added a conditional check before mapping `user_id` to `event.idm.read_only_udm.principal.user.userid`.  
\- Added a `on_error` check where `namespace` is mapped to `event.idm.read_only_udm.target.namespace`.  
\- Removed `has_target` flag used in conditional check before mapping `NETWORK`CONNECTION" event_type.   
2025-04-03 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `policy_hit.malicious_user_mitigate_action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `policy_hit.policy` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `policy_hit.policy_namespace` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `policy_hit.policy_rule` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `policy_hit.policy_rule_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `policy_hit.policy_set` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `policy_hit.result` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added Grok pattern match on `x_forwarded_for` raw log field to extract `ip` and mapped with `event.idm.read_only_udm.intermediary.ip`. Non ip values are mapped to `event.idm.read_only_udm.security_result.about.resource.attribute.labels`.  
\- Renamed `event1` to `event` to parse `hostname` raw log field with `event.idm.read_only_udm.principal.hostname`.  
\- Added Grok pattern match on `user` raw log field to extract ip and mapped it to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- Added `NULL` and empty condition check before mapping `event.idm.read_only_udm.principal.user.userid` UDM field.   
2025-03-25 |  Enhancement:  
\- Added regex check to `latitude`, `longitude`, `host` and `network` fields.  
\- Mapped `x_forwarded_for` to `intermediary.ip`.   
2025-01-17 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
