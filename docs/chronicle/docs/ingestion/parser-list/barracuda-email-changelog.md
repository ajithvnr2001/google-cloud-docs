---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-email-changelog/
title: Change log for BARRACUDA_EMAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:33.431603+00:00
---

# Change log for BARRACUDA_EMAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/barracuda-email-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BARRACUDA_EMAIL

Date | Changes  
---|---  
2026-02-09 |  Enhancement:  
\- Added a gsub filter to replace `\\x` with `\\\\x` in the json field to handle escaped hexadecimal characters.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `auth_serv` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `spf_sender_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dkim_result`, `dmarc_result`, `dkim_domain`, `header_from`, `spf_result`, `smtp_mailfrom` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `gateway` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attachment.name` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `attachment.name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.about`: Newly mapped `attachment.md5` raw log field with `event.idm.read_only_udm.about` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `account_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `domain_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tls`, `env_from`, `hdr_auth_results`, `recipient_count` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `ptr_record` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-07-10 |  Enhancement:  
\- Added Grok pattern to support for new pattern of SYSLOG+JSON logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `log_header_end`, `payload.affected_mailboxes`, `payload.attachment` and `payload.body_text` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `accountId`, `accessTokenId`, `payload.type`, `payload.incident_id`, `payload.messages_received` and `payload.matched_email_count` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Mapped `product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Mapped `payload.sender` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Mapped `payload.recipient` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Mapped `payload.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Mapped `payload.date` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Mapped `payload.category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Mapped `payload.created_by` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Mapped `payload.sender_display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Mapped `payload.sender_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Mapped `payload.login_country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.principal.ip: Mapped `payload.login_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Mapped `payload.login_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Mapped `payload.user_display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Mapped `payload.user_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.security_result.about.url: Mapped `payload.body_links` raw log field with `event.idm.read_only_udm.security_result.about.url` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Mapped `payload.sender_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.   
2024-05-28 |  Enhancement-  
\- Mapped `attachments` to `additional.fields`.   
2024-01-08 |  Enhancement-  
\- Mapped `recipients.action` to `security_result.action_details`.  
\- Mapped `recipients.email` to `network.email.to`.  
\- Mapped `recipients.delivery_detail`, `recipients.reason`, `recipients.taxonomy`, `recipients.reason_extra` and `recipient.delivered` to `security_result.detection_fields`.  
\- Mapped `dst_domain` to `target.hostname`.  
\- Mapped `geoip` to `target.location.country_or_region`.   
2023-01-19 |  Bug-Fix-  
\- Modified grok pattern to extract `subject` and mapped to `network.subject`.   
2022-12-16 |  Enhancement-  
\- Added grok pattern for new logs.  
\- Mapped `host` to `principal.hostname`.  
\- Mapped `product_log_id` to `metadata.product_log_id`.  
\- Mapped `network.application_protocol` to `SMTP` where process includes `smtp`.  
\- Mapped `sender_email` to `network.email.from`.  
\- Mapped `recipient_email` to `network.email.to`.  
\- Mapped `network.direction` to `INBOUND` where process includes `inbound`.  
\- Mapped `network.direction` to `OUTBOUND` where process includes `outbound`.  
\- Mapped `target_ip` to `target.ip`.  
\- Mapped `queue_id` to `security_result.detection_fields`.  
\- Mapped `security_result.action` to `ALLOW` where `action_code` are `0` or `7` and `service` are `RECV` or `SCAN`.  
\- Mapped `security_result.action` to `BLOCK` where `action_code` is `2` and `service` are `RECV` or `SCAN`.  
\- Mapped `security_result.action` to `QUARANTINE` where `action_code` is `3` and `service` are `RECV` or `SCAN`.   
2022-05-19 |  Enhancement-modified data extraction for email and hdr_from to improve parsing   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
