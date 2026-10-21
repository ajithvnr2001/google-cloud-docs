---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-trap-changelog/
title: Change log for PROOFPOINT_TRAP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:48.526481+00:00
---

# Change log for PROOFPOINT_TRAP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/proofpoint-trap-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PROOFPOINT_TRAP

Date | Changes  
---|---  
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `created_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field to map it with more appropriate log field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `received_at` raw log field with `event.idm.read_only_udm.additional.fields` UDM field to map it with appropriate UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `received_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `sources.name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `created_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `received_time` (key: `received_time`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `titlePII` (key: titlePII), `pps_guid` (key: pps_guid), `email_recipient_id` (key: email_recipient_id), `email_message_size` (key: email_message_size), `remediation_status` (key: remediation_status), `tap_false_positive` (key: tap_false_positive), `abuse_reporter_rank` (key: abuse_reporter_rank), `quarantine_strategy` (key: quarantine_strategy), `mime_content_expired` (key: mime_content_expired), `mime_content_present` (key: mime_content_present), `click_block_exclusive` (key: click_block_exclusive), `remediation_status_context` (key: remediation_status_context), `last_known_type` (key: last_known_type), `clear_confidence` (key: clear_confidence), `message_status.is_read` (key: message_status_is_read), `message_status.permitted_clicks` (key: message_status_permitted_clicks), `message_status.message_delivered` (key: message_status_message_delivered), `sender_id` (key: sender_id), `tenant_id` (key: tenant_id), `created_at` (key: created_at), `message_id` (key: message_id), `updated_at` (key: updated_at), `disposition` (key: disposition), `received_at` (key: received_at), `tap_cleared` (key: tap_cleared), `body_expired` (key: body_expired), `body_present` (key: body_present), `clear_verdict` (key: clear_verdict), `tap_threat_types` (key: tap_threat_types), `source.id` (key: source_id_%{index}), `source.type` (key: sources_type_%{index}), `incident.id` (key: incident_id_%{index}), `incident.title` (key: incident_title_%{index}), `incident.display_id` (key: incident_display_id_%{index}), and `incident.link_attribute` (key: incident_link_attribute_%{index}) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `sender_address` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `email_id` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `email_subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: Newly mapped `recipient_address` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `assignedUserName` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `assignedUserId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `state` (key: state) raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-08-14 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `updatedAt` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tenantId`,`closedAt`, `displayId`, `assignedTeamName`, `assignedTeamId`, `messageCount`, `vap`, `vip` , `commentCount`, `dispositions`, `sourceTypes` and `sourcesData` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.user.email_addresses: Newly mapped `principal_user1` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.user.email_addresses` UDM field,if its a valid email address.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `principal_user1` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.network.email.to` UDM field,if its a valid email address.  
\- event.idm.read_only_udm.user.userid: Newly mapped `principal_user1` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.user.userid` UDM field,if its not a valid email address.  
\- event.idm.read_only_udm.principal.url: Newly mapped `principal_link` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.user.email_addresses: Newly mapped `principal_user2` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.user.email_addresses` UDM field,if its a valid email address.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `principal_user2` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.network.email.from` UDM field,if its a valid email address.  
\- event.idm.read_only_udm.user.userid: Newly mapped `principal_user2` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.user.userid` UDM field,if its not a valid email address.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `attachment` extracted from `title` raw log field with grok and mapped to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `title` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field,if `title_grok_failed`==`true`.  
\- event.idm.read_only_udm.security_result.alert_state: Newly mapped `state` raw log field with `event.idm.read_only_udm.security_result.alert_state` UDM field, if state has `OPEN` or `CLOSED`. Else mapped `state` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.   
2025-06-04 |  Enhancement:  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `event1.description.messageid` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `sender IP` extracted from `event1.description.headers.Authentication-Results` raw log field with grok and mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `event1.description.sender.email` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `event1.description.recipient.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped `event1.description.subject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event1.description.created_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `event1.description.updated_at` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event1.description.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.sec_result.detection_fields: Newly mapped `event1.description.headers.From` raw log field with `event.idm.read_only_udm.sec_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `event1.description.headers.To` raw log field with `event.idm.read_only_udm.network.email.to` UDM field.  
\- event.idm.read_only_udm.network.email.reply_to: Newly mapped `event1.description.headers.Reply-To` raw log field with `event.idm.read_only_udm.network.email.reply_to` UDM field.  
\- event.idm.read_only_udm.sec_result.description: Newly mapped `event1.description.headers.Received-SPF` raw log field with `event.idm.read_only_udm.sec_result.description` UDM field.  
\- event.idm.read_only_udm.sec_result.detection_fields: Newly mapped `event1.description.headers.DKIM-Signature` raw log field with `event.idm.read_only_udm.sec_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `event1.description.sender.vap` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `event1.description.recipient.vap` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.intermediary.labels: Newly mapped `event1.description.hosts.url` raw log field with `event.idm.read_only_udm.intermediary.labels` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `event1.description.urls` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.sec_result.severity: Newly mapped `event1.description.severity` raw log field with `event.idm.read_only_udm.sec_result.severity` UDM field.  
\- event.idm.read_only_udm.sec_result.summary: Newly mapped `event1.description.state` raw log field with `event.idm.read_only_udm.sec_result.summary` UDM field.   
2025-02-20 |  Enhancement:  
\- Added support for parsing additional fields.   
2025-01-29 |  Enhancement:  
\- Mapped `mailfrom`, `spf`, `dkim1`, `header_s1`, `header_d1`, `dkim2`, `header_s2`, `header_d2`, and `dmarc` to `security_result.detection_fields`.  
\- Mapped `send_email` to `network.email.from`.  
\- Mapped `to_email` to `network.email.to`.   
2025-01-14 |  Enhancement:  
\- Defined labels inside the for loop.   
2024-12-12 |  Enhancement:  
\- Added support for the new pattern of JSON logs.   
2024-09-11 |  Enhancement:  
\- When `proofpoint_trap_host` is a valid IP then mapped it to `intermediary.ip`. Otherwise, mapped it to `intermediary.ip`.  
\- Mapped `users` to `principal.user.userid`.  
\- Mapped `received` to `metadata.event_timestamp`.  
\- Added support for JSON logs.   
2024-06-05 |  Enhancement:  
\- Added support for JSON logs.   
2023-05-26 |  Added mapping for the following fields:  
\- `ewsUrl` mapped to `principal.url`.  
\- `username` mapped to `principal.user.user_display_name`.  
\- `exchangeAuthType`,`exchangeAPI`,`tenantId`,`clientId`,`clientSecret`,`graphApiEndpoint`,`alternateGraphApiEndpoint`,  
`azureAdAuthEndpoint`,`privateKey` mapped to `additional.fields`.   
2022-08-23 |  Newly Created Parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
