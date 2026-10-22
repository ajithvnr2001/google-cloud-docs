---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sublimesecurity-changelog/
title: Change log for SUBLIMESECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:09.490956+00:00
---

# Change log for SUBLIMESECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sublimesecurity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SUBLIMESECURITY

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `created_at`, `headers_date` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id`, `data.message.id` raw log fields with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `data.sender.email.email`, `data.headers.from.email.email` raw log fields with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `toemail.email.email` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `ccemail.email.email` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `data.mailbox.display_name` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.first_name`: Newly mapped `data.mailbox.first_name` raw log field with `event.idm.read_only_udm.target.user.first_name` UDM field.  
\- `event.idm.read_only_udm.target.user.last_name`: Newly mapped `data.mailbox.last_name` raw log field with `event.idm.read_only_udm.target.user.last_name` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `data.mailbox.email.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `data.subject.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `data.headers.message_id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.network.email.reply_to`: Newly mapped `data.headers.return_path.email` raw log field with `event.idm.read_only_udm.network.email.reply_to` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `data.headers.auth_summary.spf.details.client_ip.ip`, `ipentry.ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hop.received.source.raw`, `hop.received.server.raw` raw log fields with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.about.url`: Newly mapped `link.href_url.url`, `link.href_url.rewrite.original` raw log fields with `event.idm.read_only_udm.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `flagged.id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `flagged.name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `flagged.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_cipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `data.headers.from.email.domain.domain`, `data.headers.from.email.domain.root_domain`, `data.headers.from.email.domain.sld`, `data.headers.from.email.domain.subdomain`, `data.headers.from.email.domain.tld`, `data.headers.from.email.domain.valid`, `data.sender.email.domain.domain`, `data.sender.email.domain.sld`, `data.sender.email.domain.subdomain`, `data.sender.email.domain.tld`, `data.sender.email.domain.valid`, `link.display_text`, `link.href_url.domain.domain`, `link.href_url.domain.root_domain`, `link.href_url.domain.sld`, `link.href_url.domain.subdomain`, `link.href_url.domain.tld`, `link.href_url.domain.valid`, `link.href_url.path`, `link.href_url.scheme`, `link.parser`, `link.visible`, `link.href_url.rewrite.encoders`, `data.message.canonical_id`, `data.message.external_id`, `data.message.mailbox.external_id`, `data.message.mailbox.id`, `data.message.message_source_id`, `action_id`, `org_id`, `data.attack_score_verdict`, `data.message.id`, `api_version`, `type_extended`, `data.body.plain.raw`, `data.body.plain.charset`, `data.body.plain.content_transfer_encoding`, `data.body.html.charset`, `data.body.html.content_transfer_encoding`, `data.body.html.display_text`, `data.body.html.inner_text`, `data.body.current_thread.text`, `banner.text`, `data.classification`, `data.headers.auth_summary.dmarc.details.verdict`, `data.headers.auth_summary.dmarc.error`, `data.headers.auth_summary.dmarc.pass`, `data.headers.auth_summary.dmarc.received_hop`, `data.headers.auth_summary.dmarc.details.from.domain`, `data.headers.auth_summary.spf.details.verdict`, `data.headers.auth_summary.spf.error`, `data.headers.auth_summary.spf.pass`, `data.headers.auth_summary.spf.details.designator`, `data.headers.auth_summary.spf.received_hop`, `data.headers.date_original_offset`, `data.headers.return_path.local_part`, `data.headers.return_path.domain.domain`, `hop.received.protocol.raw`, `hop.received.time`, `hop.received.id.raw`, `hop.signature.algorithm`, `hop.signature.body_hash`, `hop.signature.domain`, `hop.signature.selector`, `hop.signature.signature`, `hop.signature.type`, `field.value`, `tls_raw`, `dom.domain`, `data.message.landed_in_spam`, `rpt`, `data.subject.base`, `data.subject.is_auto_reply`, `data.subject.is_forward`, `data.subject.is_reply`, `stag`, `action.id`, `action.name`, `action.status`, `action.type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `data.headers.auth_summary.dmarc.details.policy`, `flagged.source_md5`, `flagged.label`, `flagged.attack_types`, `flagged.detection_methods`, `flagged.tactics_and_techniques`, `flagged.tags` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to EMAIL_TRANSACTION when network email details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to STATUS_UPDATE when principal machine details are present.   
2025-12-22 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `headers.date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `headers.from.email.email` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `headers.from.email.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `recipients.to.email.email` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `recipients.to.email.email`, `recipients.cc.email.email` raw log fields with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.email.cc`: Newly mapped `recipients.cc.email.email` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `subject.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `headers.message_id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.network.email.reply_to`: Newly mapped `headers.return_path.email` raw log field with `event.idm.read_only_udm.network.email.reply_to` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `headers.auth_summary.spf.details.client_ip.ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `headers.auth_summary.dmarc.details.policy` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `hop.received.source.raw`, `hop.received.server.raw` raw log fields with `event.idm.read_only_udm.intermediary` UDM field.  
\- `event.idm.read_only_udm.about.url`: Newly mapped `link.href_url.url` raw log fields with `event.idm.read_only_udm.about.url` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `_meta.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_meta.canonical_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about`: Newly mapped `about` field with `event.idm.read_only_udm.about` UDM field.  
\- `event.idm.read_only_udm.security_result`: Newly mapped `security_result2` field with `event.idm.read_only_udm.security_result` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set to `EMAIL_TRANSACTION`.  
\- Added Grok pattern to parse `hop_source` raw log field into `host` and `ip` temporary fields.  
\- Set `event.idm.read_only_udm.network.application_protocol` to `SMTP`.  
\- Added mutate { merge => { `@output` => `event` } } at the end of the new conditional block for `headers` and `body`.   
2025-03-27 |  \- Mapped `flagged_id` to `security_result.ruleid`.  
\- Mapped `flagged_name` to `security_result.rule_name`.  
\- Mapped `flagged_severity` to `security_result.severity`.  
\- Mapped `canonical_id`, `external_id`, `mailbox_external_id`, `mailbox_id`, `start`, `end`, `key`,and `message_source_id` to `additional.fields`.  
\- Mapped `message_id` to `metadata.product_log_id`.  
\- Mapped `eventdata.type` to `metadata.product_event_type`.  
\- Mapped `tags` to `security_result.detection_fields`.  
\- Mapped `eventdata.created_at` to `metadata.event_timestamp`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
