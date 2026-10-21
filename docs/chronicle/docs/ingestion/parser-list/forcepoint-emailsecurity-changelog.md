---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-emailsecurity-changelog/
title: Change log for FORCEPOINT_EMAILSECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:38:00.810602+00:00
---

# Change log for FORCEPOINT_EMAILSECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/forcepoint-emailsecurity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORCEPOINT_EMAILSECURITY

Date | Changes  
---|---  
2025-12-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped trueSrc raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped trueSrc raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.network.email.to: Newly mapped to raw log field with event.idm.read_only_udm.network.email.to UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped timestamp_value raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped in raw log field with event.idm.read_only_udm.network.sent_bytes UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped dvc, intermediary_ip raw log field(s) with event.idm.read_only_udm.intermediary.ip UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped dvc, intermediary_ip raw log field(s) with event.idm.read_only_udm.intermediary.asset.ip UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped rt raw log field with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped intermediary raw log field with event.idm.read_only_udm.intermediary UDM field.  
\- event.idm.read_only_udm.network.email.to: The to field, previously a simple string, is now parsed to handle multiple email addresses, including those with display names.  
\- The conditional check for from was updated to include a length validation.  
\- A new log format is now parsed using a new grok pattern. Key-value pairs are extracted from the kv_data field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped duser raw log field with event.idm.read_only_udm.target.user.email_addresses UDM field.  
\- Renamed from x-mailer to x_mailer.   
2025-04-04 |  Enhancement:  
-`SYSLOG`: Added support for `SYSLOG` format.  
\- `event.idm.ready_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.ready_only_udm.metadata.product_version` UDM field.  
\- `event.idm.ready_only_udm.principal.hostname`: Newly mapped `dvchost` raw log field with `event.idm.ready_only_udm.principal.hostname` and `event.idm.ready_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.ready_only_udm.metadata.product_log_id`: Newly mapped `externalId` raw log field with `event.idm.ready_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.ready_only_udm.principal.resource.attribute.labels`: Newly mapped `messageId` raw log field with `event.idm.ready_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.ready_only_udm.target.user.email_addresses`: Newly mapped `duser` raw log field with `event.idm.ready_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.ready_only_udm.principal.user.userid`: Newly mapped `suser` raw log field with `event.idm.ready_only_udm.principal.user.userid` UDM field.  
\- `event.idm.ready_only_udm.principal.ip`: Newly mapped `src` raw log field with `event.idm.ready_only_udm.principal.ip` and `event.idm.ready_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.ready_only_udm.target.ip`: Newly mapped `dst` raw log field with `event.idm.ready_only_udm.target.ip` and `event.idm.ready_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.ready_only_udm.network.tls.cipher`: Newly mapped `encryptedDelivery` raw log field with `event.idm.ready_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.ready_only_udm.network.http.response_code`: Newly mapped `deliveryCode` raw log field with `event.idm.ready_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `deliveryCodeInfo` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.ready_only_udm.network.email.mail_id`: Newly mapped `message_id` raw log field with `event.idm.ready_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.ready_only_udm.principal.resource.attribute.labels`: Newly mapped `internal_id` raw log field with `event.idm.ready_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.ready_only_udm.target.hostname`: Newly mapped `hostname` raw log field with `event.idm.ready_only_udm.target.hostname` and `event.idm.ready_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.ready_only_udm.network.sent_bytes`: Newly mapped `message_size` raw log field with `event.idm.ready_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.ready_only_udm.network.application_protocol`: Newly mapped `app` raw log field with `event.idm.ready_only_udm.network.application_protocol` UDM field.  
\- `event.idm.ready_only_udm.security_result.description`: Newly mapped `act` raw log field with `event.idm.ready_only_udm.security_result.description` UDM field.  
\- `event.idm.ready_only_udm.network.email.from`: Newly mapped `from` raw log field with `event.idm.ready_only_udm.network.email.from` UDM field.  
\- `event.idm.ready_only_udm.network.email.to`: Newly mapped `to` raw log field with `event.idm.ready_only_udm.network.email.to` UDM field.  
\- `event.idm.ready_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.ready_only_udm.metadata.description` UDM field.  
\- `event.idm.ready_only_udm.network.email.cc`: Newly mapped `cc` raw log field with `event.idm.ready_only_udm.network.email.cc` UDM field.  
\- `event.idm.ready_only_udm.network.email.subject`: Newly mapped `x_mailer` raw log field with `event.idm.ready_only_udm.network.email.subject` UDM field.  
\- `event.idm.ready_only_udm.principal.resource.attribute.labels`: Newly mapped `spfResult` raw log field with `event.idm.ready_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.ready_only_udm.principal.resource.attribute.labels`: Newly mapped `event` raw log field with `event.idm.ready_only_udm.principal.resource.attribute.labels` UDM field.   
2024-08-22 |  Enhancement:  
\- Added support for a new log format of JSON logs.   
2024-05-30 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
