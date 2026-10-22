---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sendmail-changelog/
title: Change log for SENDMAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:01.143017+00:00
---

# Change log for SENDMAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sendmail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENDMAIL

Date | Changes  
---|---  
2026-07-24 |  Enhancement:  
\- Added grok pattern to parse new format of SYSLOG + KV logs.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `auth_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `sender_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: Newly mapped `sender_email` raw log field with `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `bodytype` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-20 |  Enhancement:  
\- `SYSLOG`: Added support for SYSLOG format.  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `program` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `mail_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field when `proto` value is `ESMTP`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_prio`, `syslog_pri`, `syslog_version`, `id`, `mail_type`, `mail_info`, `class`, `nrcpts`, `proto`, and `daemon` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-12 |  Enhancement:  
\- Added grok pattern to support new format of SYSLOG logs.  
\- `event.idm.read_only_udm.target.email`: Newly mapped `email` raw log field with `event.idm.read_only_udm.target.email UDM field`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_hostname` raw log field with `event.idm.read_only_udm.target.hostname UDM field`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority` raw log field with `event.idm.read_only_udm.additional.fields UDM field`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `pri` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `product_log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dsn` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `mailer` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `delay`, `STARTTLS`, `bits` and `xdelay` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_details` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `verify` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.   
2023-09-20 |  Enhancement:  
\- Added condition to `from` parameter if the value is not in email format, then append `@local`.   
2022-05-06 |  Enhancement-Mapped following fields:  
tls_verify to security_result.description.  
tls_version to network.tls.version.  
cipher to network.tls.cipher.  
size to network.sent_bytes.  
eventid to metadata.product_log_id.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
