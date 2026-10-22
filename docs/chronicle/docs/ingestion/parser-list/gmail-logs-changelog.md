---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmail-logs-changelog/
title: Change log for GMAIL_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:47.266880+00:00
---

# Change log for GMAIL_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gmail-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GMAIL_LOGS

Date | Changes  
---|---  
2024-05-10 |  Bug-Fix:  
\- Added a condition check before merging `category_details` to `security_result.category_details`.   
2024-03-19 |  \- Mapped `gmail.message_info.link_domain` to `about.labels`.  
\- Mapped `gmail.message_info.subject` to `network.email.subject`.  
\- Mapped `gmail.message_info.description` to `metadata.description`.  
\- Mapped `gmail.message_info.attachment.sha256` to `about.file.sha256`.  
\- Mapped `gmail.message_info.destination.address` to `network.email.to`.  
\- Mapped `gmail.message_info.rfc2822_message_id` to `network.email.mail_id`.  
\- Mapped `gmail.message_info.attachment.file_name` to `about.file.full_path`.  
\- Mapped `gmail.message_info.source.from_header_address` to `network.email.from`.  
\- Mapped `gmail.message_info.attachment.file_extension_type` to `about.file.mime_type`.  
\- Mapped `gmail.message_info.triggered_rule_info.rule_type` to `security_result.rule_id`.  
\- Mapped `gmail.message_info.triggered_rule_info.rule_name` to `security_result.rule_name`.  
\- When `gmail.event_info.success` is `true`, then set `security_result.action` to `ALLOW`.  
\- When `gmail.event_info.success` is not `true`, then set `security_result.action` to `BLOCK`.  
\- Mapped `gmail.message_info.source.from_header_displayname` to `principal.user.user_display_name`.  
\- Mapped `gmail.message_info.connection_info.smtp_response_reason` to `security_result.description`.  
\- Mapped `gmail.message_info.connection_info.ip_geo_country` to `principal.location.country_or_region`.  
\- When `gmail.message_info.source.address` is not a valid email, then mapped it to `principal.user.userid`.  
\- Mapped `gmail.message_info.source.service`, `gmail.message_info.source.selector` to `principal.application`.  
\- When `_no_outcoming_message` is false, then mapped `gmail.message_info.payload_size` to `network.sent_bytes`.  
\- When `gmail.message_info.source.address` is a valid email, then mapped it to `principal.user.email_addresses`.  
\- When `_no_incoming_message` is false, then mapped `gmail.message_info.payload_size` to `network.received_bytes`.  
\- Mapped `il.message_info.connection_info.client_host_zone` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `gmail.message_info.destination.0.service`, `gmail.message_info.destination.0.selector` to `target.application`.  
\- Mapped `gmail.message_info.post_delivery_info.action_type`, `gmail.message_info.num_message_attachments`, and `gmail.event_info.mail_event_type` to `additional.fields`.   
2023-12-22 |  Bug-Fix:  
\- Mapped `message_info.source.address` to `network.email.from`.   
2023-12-07 |  Bug-Fix:  
\- Added convert block to convert the respective data to string.  
\- Mapped `message_info.source.from_header_address` to `network.email.from`.   
2023-08-21 |  Enhancement:  
\- Added null check for JSON plugin and dropped malformed logs.  
\- Mapped `email` to `princpal.email_addresses`.  
\- Mapped `token.client_id` to `principal.user.group_identifiers`.  
\- Mapped `token.app_name` to `principal.application`.  
\- Mapped `token.scope_data.0.product_bucket.0` to `additional.fields`.  
\- Mapped `record_type` to `additional.fields`.  
\- Mapped `token.client_type` to `additional.fields`.  
\- Mapped `event_name` to `metadata.product_event_type`.   
2023-06-06 |  Enhancement:  
\- Mapped `event_info.success` to `security_result.action`.  
\- when `event_info.success` is `true` , `security_result.action` is set `ALLOW`.  
\- when `event_info.success` is `false` , `security_result.action` is set `BLOCK`.   
2023-05-19 |  Enhancement:  
\- Mapped `attachment.file_name` to `about.file.full_path`.  
\- Mapped `message_info.post_delivery_info.action_type`, `message_info.post_delivery_info.interaction.link_url`, `event_info.mail_event_type` to `additional.fields`.   
2023-03-31 |  Enhancement:  
\- The field `message_info.source.service` and `message_info.source.selector` is mapped to `principal.application`.  
\- The field `message_info.destination.0.service` and `message_info.destination.0.selector` is mapped to `target.application`.  
\- The field `message_info.triggered_rule_info[n].string_match[n].predefined_detector_name` is mapped to `security_result.detection_fields`.  
\- The field `message_info.triggered_rule_info[n].string_match[n].matched_string` is mapped to `security_result.detection_fields`.  
\- The field `message_info.triggered_rule_info[n].string_match[n].match_expression` is mapped to `security_result.detection_fields`.  
\- The field `message_info.triggered_rule_info[n].string_match[n].source` is mapped to `security_result.detection_fields`.  
\- The field `message_info.triggered_rule_info[n].string_match[n].type` is mapped to `security_result.detection_fields`.  
\- The field `message_info.num_message_attachments` is mapped to `additional.fields`.  
\- Added a `for` loop to map the extracted fields from `message_info.destination`.  
\- Added a `for` loop to map the extracted fields from `message_info.attachment`.  
\- Added null conditional checks for several fields.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
