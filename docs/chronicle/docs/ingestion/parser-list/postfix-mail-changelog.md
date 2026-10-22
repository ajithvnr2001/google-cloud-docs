---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postfix-mail-changelog/
title: Change log for POSTFIX_MAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:48.402294+00:00
---

# Change log for POSTFIX_MAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/postfix-mail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for POSTFIX_MAIL

Date | Changes  
---|---  
2026-01-29 |  Enhancement:  
\- `event.idm.read_only_udm.network.email.mail_id`: Newly mapped `transaction_id` field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `s`, `d`, `nrcpt` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped for `status_description` field to `event.idm.read_only_udm.metadata.description` UDM field if `daemon` is `opendkim` and `qmgr`.  
\- Modified a grok pattern to parse `inter_host` field.  
\- Added a new grok pattern to parse `transaction_id` if log has `qmgr`.  
\- Added new grok patterns to parse new format of logs containing `opendkim`.  
\- Overwritten and initialised `data_size` field.  
\- Corrected the mapping of `data_zize` field by using null check and replace instead of rename before mapping with `event.idm.read_only_udm.network.received_bytes`  
2026-01-23 |  Enhancement:  
\- Added grok pattern to parse new log format.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `email_from` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `smtp_code`, `smtp_status`, `time_sec`, `speed_kbps` and `InternalId` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `ssmtp_message_id` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes_sent` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `security_result.summary`: Newly mapped `delivery_status` raw log field with `security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.   
2025-09-03 |  Enhancement:  
\- Removed drop tag when log contains `bounce` value to parse the logs.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `bounceid` and `originalmsgid` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-06-25 |  Enhancement:  
\- Added support to parse new format of syslog logs.   
2024-05-22 |  Enhancement  
\- Added a Grok pattern to extract `from` and `to` email addresses, `subject`, and `filename` from the raw log and set `metadata.event_type` to `EMAIL_TRANSACTION`.   
2022-10-06 |  Enhancement  
\- Modified grok pattern to parse the logs.   
2022-07-18 |  Enhancement  
\- Mapped host.hostname to principal.hostname.  
\- Mapped host.ip to principal.ip.  
\- Mapped host.mac to principal.mac.  
\- Mapped host.id to principal.asset.asset_id.  
\- Mapped host.os.name to principal.platform.  
\- Mapped network.ip_protocol to TCP if input.type is tcp.  
\- Mapped log.source.address data src_ip to principal.ip, src_port to principal.port.  
\- Mapped agent.id to metadata.product_log_id.  
\- Mapped agent.type to metadata.product_event_type.  
\- Mapped agent.version to metadata.product_version.  
\- Mapped source_ip to principal.ip.  
\- Mapped source_hostname to principal.hostname.  
\- Mapped target_email to network.email.to if it is an email else mapped to target.user.userid.  
\- Mapped from_user to network.email.from.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
