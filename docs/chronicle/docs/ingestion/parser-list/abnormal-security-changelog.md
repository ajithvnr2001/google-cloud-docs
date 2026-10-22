---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/abnormal-security-changelog/
title: Change log for ABNORMAL_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:04.620416+00:00
---

# Change log for ABNORMAL_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/abnormal-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ABNORMAL_SECURITY

Date | Changes  
---|---  
2026-03-25 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Mapped `event.abx_body.abnormal_message_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event.abx_body.email_label_or_location` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event.abx_body.not_analyzed` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern on `message` to extract `abnormal_message_id` raw log field.   
2025-09-18 |  Enhancement:  
\- Added support for the event `THREAT_LOG` and relevant corresponding raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event.abx_body.source`,`event.abx_body.message_engagement.replied_count`, `event.abx_body.message_engagement.forwarded_count` ,`event.abx_body.abx_message_id_str`, `event.abx_body.auto_remediated`, `event.abx_body.message_sources`, `event.abx_body.folder_locations`, `event.abx_body.attachment_count`, `event.abx_body.url_count`, `event.abx_body.attack_score`, `event.abx_body.sender_auth_results.spf`, `event.abx_body.sender_auth_results.dkim`, `event.abx_body.sender_auth_results.dmarc`, `event.abx_body.tenant`, `event.abx_body.is_read`, `event.abx_body.post_remediated`, `event.abx_body.remediation_status`, `event.abx_body.return_path`, `event.abx_body.received_time`, `event.abx_body.sent_time`, and `event.abx_body.remediation_timestamp` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result`: Newly mapped `event.abx_body.threat_id`, `event.abx_body.attack_strategy`, `event.abx_body.attack_vector`, `event.abx_body.attacked_party`, `event.abx_body.impersonated_party`, `event.abx_body.summary_insights`, and `event.abx_body.urls` raw log fields to subfields within `event.idm.read_only_udm.security_result`.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `event.abx_body.to_addresses` raw log field to `event.idm.read_only_udm.network.email.to`.  
\- `event.idm.read_only_udm.network.email.reply_to`: Newly mapped `event.abx_body.reply_to_emails` raw log field to `event.idm.read_only_udm.network.email.reply_to`.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `event.abx_body.cc_emails` raw log field to `event.idm.read_only_udm.network.email.cc`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `event.abx_body.sender_ip_address` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `event.abx_body.sender_domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `event.abx_body.from_name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name`.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `event.abx_body.from_address` raw log field to `event.idm.read_only_udm.network.email.from`.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `event.abx_body.abx_portal_url` raw log field to `event.idm.read_only_udm.network.http.referral_url`.  
\- `event.idm.read_only_udm.security_result.threat_name` : Newly mapped `event.abx_body.attack_type` raw log field to `event.idm.read_only_udm.security_result.threat_name`.  
\- Corrected typo in initialization from `event_date.cc_emails` to `event_data.cc_emails`.   
2024-09-18 |  Enhancement:  
\- Mapped `event_data.message_sources`, `event_data.sender_auth_results.spf`, `event_data.sender_auth_results.dkim`, `event_data.sender_auth_results.dmarc`, `event_data.tenant`, and `event_data.attack_score` to `additional.fields`.   
2024-09-12 |  Enhancement:  
\- When `sourcetype` is `case`, then mapped the following:  
\- `event.abx_body.event_timeline.n.ip_address` to `principal.ip` and `principal.asset.ip`.  
\- `event.abx_body.event_timeline.n.insights.0.signal`, `event.abx_body.event_timeline.n.insights.0.description`, `event.abx_body.event_timeline.n.browser`, `event.abx_body.event_timeline.n.operating_system`, `event.abx_body.event_timeline.n.isp`, `event.abx_body.event_timeline.n.application`, `event.abx_body.event_timeline.n.signin_event_status`, and `event.abx_body.event_timeline.n.platform` to `additional.fields`.   
2024-08-21 |  Enhancement:  
\- Mapped `event_data.abx_body.severity` to `security_result.severity`.  
\- Mapped `event_data.abx_body.trigger_event` and `event_data.abx_body.entity.entity_type` to `additional.fields`.  
\- Mapped `event_data.abx_body.entity.identifier` to `principal.user.email_addresses`.  
\- Mapped `event_data.abx_body.case_id` to `metadata.product_log_id`.   
2024-07-24 |  Enhancement:  
\- Mapped `sourcetype`, `event.folder_locations` to `additional.fields`.  
\- Mapped `event.abx_message_id` to `metadata.product_log_id`.   
2024-05-02 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2023-11-06 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
