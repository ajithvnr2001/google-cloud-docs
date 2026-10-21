---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-abp-changelog/
title: Change log for IMPERVA_ABP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:56:50.400277+00:00
---

# Change log for IMPERVA_ABP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-abp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_ABP

Date | Changes  
---|---  
2026-02-26 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Removed mapping of `imperva.ids.account_name` from `event.idm.read_only_udm.metadata.product_event_type` UDM field to introduce more appropriate mapping UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `imperva.ids.account_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Removed mapping of `req.imperva.ids.account_name` from `event.idm.read_only_udm.metadata.product_event_type` UDM field to introduce more appropriate mapping UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped `req.imperva.ids.account_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Updated the key for the `req.imperva.abp.bot_behaviors` raw log field from `botbehaviors_%{index}` to `bot_behaviors_%{index}`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `req.url.query` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `req.event.id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `req.client.geo.name` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `req.imperva.abp.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `req.event.provider` (key: provider), `req.imperva.abp.fpid` (key: fpid), `req.event.category` (key: event category), `req.imperva.abp.random_id` (key: random_id), `req.imperva.abp.captcha_solved_timestamp` (key: captcha_solved_timestamp), `req.imperva.abp.requests_since_captcha_succeeded` (key: requests_since_captcha_succeeded), `req.imperva.abp.tcp_rtt_ms` (key: tcp_rtt_ms), `req.imperva.abp.tls_rtt_ms` (key: tls_rtt_ms), `req.imperva.abp.headers_cookie_length` (key: headers_cookie_length), `req.imperva.abp.header_lengths` (key: header_lengths), and `req.imperva.abp.cookie_lengths` (key: cookie_lengths) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `req.imperva.abp.headers_accept_language` (key: req_headers_accept_language), `req.imperva.abp.headers_accept` (key: req_imperva_headers_accept), `req.imperva.abp.zid` (key: req_imperva_zid), `req.imperva.abp.header_id` (key: req_imperva_header_id), `req.imperva.abp.cookie_names` (key: cookie_names_%{index}), `req.imperva.abp.deciding_tags` (key: deciding_tags_%{index}), `req.imperva.abp.bot_deciding_condition_ids` (key: bot_deciding_condition_ids_%{index}), `req.imperva.abp.bot_triggered_condition_names` (key: bot_triggered_condition_names_%{index}), and `req.imperva.abp.bot_deciding_condition_names` (key: bot_deciding_condition_names_%{index}) raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-12-05 |  Enhancement:  
\- Added support to parse requested fields.  
\- Changed mapping of `url.path` from `target.url` to `network.http.referral_url`.   
2024-11-07 |  Enhancement:  
\- If the value of the `monitor_action` field is neither `block` nor `allow`, then mapped it to `security_result.action_details`.   
2024-10-10 |  Enhancement:  
\- Mapped `metadata.vendor_name` to `Imperva ABP`.   
2024-03-23 |  Enhancement:  
\- Added a JSON block to parse additional logs.  
\- Mapped `event.provider` to `principal.user.userid`.  
\- Mapped `client.ip` to `principal.ip`.  
\- Mapped `client.domain` to `principal.hostname`.  
\- Mapped `imperva.abp.request_type` to `principal.labels`.  
\- Mapped `imperva.abp.pid` to `principal.process.pid`.  
\- Mapped `client.geo.country_iso_code` to `principal.location.country_or_region`.  
\- Mapped `server.domain` to `target.hostname`.  
\- Mapped `server.geo.name` to `target.location.name`.  
\- Mapped `url.path` to `target.process.file.full_path`.  
\- Mapped `imperva.abp.customer_request_id` to `network.session_id`.  
\- Mapped `imperva.abp.token_id` to `target.resource.product_object_id`.  
\- Mapped `imperva.abp.random_id` to `additional.fields`.  
\- Mapped `http.request.method` to `network.http.method`.  
\- Mapped `user_agent.original` to `network.http.parsed_user_agent`.  
\- Mapped `imperva.abp.headers_referer` to `network.http.referral_url`.  
\- Mapped `imperva.abp.zuid` to `additional.fields`.  
\- Mapped `imperva.ids.site_name` to `additional.fields`.  
\- Mapped `imperva.ids.site_id` to `additional.fields`.  
\- Mapped `imperva.ids.account_name` to `metadata.product_event_type`.  
\- Mapped `imperva.ids.account_id` to `metadata.product_log_id`.  
\- Mapped `imperva.abp.headers_accept_encoding` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.headers_accept_language` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.headers_connection` to `security_result.detection_fields`  
\- Mapped `imperva.abp.policy_id` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.policy_name` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.selector_derived_id` to `security_result.detection_fields`.  
\- Mapped `imperva.abp.monitor_action` to `security_result.action`.  
\- Mapped `http.request.body.bytes` to `network.sent_bytes`.  
\- Mapped `imperva.abp.tls_fingerprint` to `security_result.description`.  
\- Mapped `imperva.abp.session_length_seconds`, `imperva.abp.requests_per_session`, `imperva.abp.requests_per_minute`, `imperva.abp.token_expire`, `imperva.abp.seconds_with_expired_token`, `imperva.abp.requests_with_expired_token`, `imperva.abp.requests_with_no_token`, `imperva.abp.seconds_with_no_token`, `imperva.ids.site_name`, and `imperva.ids.site_id` to `additional.fields`.   
2023-07-21 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
