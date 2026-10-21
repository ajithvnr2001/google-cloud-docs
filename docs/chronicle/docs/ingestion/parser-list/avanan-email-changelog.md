---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avanan-email-changelog/
title: Change log for AVANAN_EMAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:28:50.280682+00:00
---

# Change log for AVANAN_EMAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/avanan-email-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AVANAN_EMAIL

Date | Changes  
---|---  
2025-11-17 |  Enhancement:  
\- Added support for JSON log format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventValue.metadata.event_timestamp` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `eventValue.metadata.product_name` raw log field to event.idm.read_only_udm.metadata.product_name.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `eventValue.metadata.vendor_name` raw log field to event.idm.read_only_udm.metadata.vendor_name.  
\- event.idm.read_only_udm.principal.user.product_object_id: Newly mapped `eventValue.principal.user.product_object_id` raw log field to event.idm.read_only_udm.principal.user.product_object_id.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `eventValue.principal.user.user_display_name` raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `eventValue.principal.user.userid` raw log field to event.idm.read_only_udm.principal.user.userid.  
\- event.idm.read_only_udm.principal.user.title: Newly mapped `eventValue.principal.user.title` raw log field to event.idm.read_only_udm.principal.user.title.  
\- event.idm.read_only_udm.principal.user.department: Newly mapped `eventValue.principal.user.department` raw log field to event.idm.read_only_udm.principal.user.department.  
\- event.idm.read_only_udm.target.application: Newly mapped `eventValue.target.application` raw log field to event.idm.read_only_udm.target.application.  
\- event.idm.read_only_udm.target.user.product_object_id: Newly mapped `eventValue.target.user.product_object_id` raw log field to event.idm.read_only_udm.target.user.product_object_id.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `eventValue.target.user.user_display_name` raw log field to event.idm.read_only_udm.target.user.user_display_name.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `eventValue.target.user.userid` raw log field to event.idm.read_only_udm.target.user.userid.  
\- event.idm.read_only_udm.target.user.title: Newly mapped `eventValue.target.user.title` raw log field to event.idm.read_only_udm.target.user.title.  
\- event.idm.read_only_udm.target.user.department: Newly mapped `eventValue.target.user.department` raw log field to event.idm.read_only_udm.target.user.department.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `eventValue.target.user.email_addresses` raw log field to event.idm.read_only_udm.target.user.email_addresses.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `eventValue.additional.entityValue.entity_payload.recipients` raw log field to event.idm.read_only_udm.target.user.email_addresses.  
\- event.idm.read_only_udm.observer.application: Newly mapped `eventValue.observer.application` raw log field to event.idm.read_only_udm.observer.application.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `eventValue.network.email.from` raw log field to event.idm.read_only_udm.network.email.from.  
\- event.idm.read_only_udm.network.email.reply_to: Newly mapped `eventValue.network.email.reply_to` raw log field to event.idm.read_only_udm.network.email.reply_to.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `eventValue.network.email.to` raw log field to event.idm.read_only_udm.network.email.to.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `eventValue.network.email.mail_id` raw log field to event.idm.read_only_udm.network.email.mail_id.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `eventValue.network.email.subject` raw log field to event.idm.read_only_udm.network.email.subject.  
\- event.idm.read_only_udm.security_result.category: Newly mapped `sec_res.category raw log field to event.idm.read_only_udm.security_result.category.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `sec_res.rule_id` raw log field to event.idm.read_only_udm.security_result.rule_id.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `sec_res.description` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `sec_res.severity` raw log field to event.idm.read_only_udm.security_result.severity.  
\- event.idm.read_only_udm.security_result.confidence: Newly mapped `sec_res.confidence` raw log field to event.idm.read_only_udm.security_result.confidence.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `sec_res.action` raw log field to event.idm.read_only_udm.security_result.action.  
\- event.idm.read_only_udm.about.ip: Newly mapped `about_1.ip` raw log field to event.idm.read_only_udm.about.ip.  
\- event.idm.read_only_udm.additional.fields: Newly mapped fields from `eventValue.metadata.event_type` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped fields from `eventValue.additional.entityValue.entity_info` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped fields from `eventValue.additional.entityValue.entity_payload` and `eventValue.additional.entityValue.time` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped fields from `eventValue.additional.entityValue.entity_security_result` and its nested fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped fields from `eventValue.additional.security_event` and its nested fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped fields from `eventValue.additional.security_event.security_event_action` and its nested fields to event.idm.read_only_udm.security_result.detection_fields.   
2022-07-12 |  Enhancement:  
\- Mapped `id` to `metadata.product_log_id`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `entity_link` to `principal.process.file.full_path`.  
\- Mapped `user_id` to `principal.user.userid`.  
\- Mapped `Size` to `target.file.size`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `matched_security_tool` to `additional.fields`.  
\- Mapped `customer_domain` to `additional.fields`.  
\- Mapped `current_state` to `additional.fields`.  
\- Mapped `policy_rule_id` to `security_result.rule_id`.  
\- Mapped `Body_ContentType` to `security_result.detection_fields`.  
\- Mapped `aggregation_id` to `security_result.detection_fields`.  
\- Mapped `entity_source` to `security_result.detection_fields`.  
\- Mapped `av_mail_hash` to `security_result.detection_fields`.  
\- Mapped `entity_type` to `security_result.detection_fields`.  
\- Mapped `InternetMessageIdHash` to `security_result.detection_fields`.  
\- Mapped `recipients_hash` to `target.process.file.sha256`.  
\- Mapped `From` to `target.process.product_specific_process_id`.  
\- Added for loop for `recipients`.  
\- Added for loop for `recipient_emails`.  
\- Mapped `av_file_hash_md5` to `principal.process.file.md5`.  
\- Mapped `av_file_hash_sha256` to `principal.process.file.sha256`.  
\- Mapped `av_file_hash_sha1` to `principal.process.file.sha1`.  
\- Mapped `av_file_mime` to `principal.process.file.mime_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
