---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-mail-changelog/
title: Change log for SYMANTEC_MAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:11.499410+00:00
---

# Change log for SYMANTEC_MAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-mail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_MAIL

Date | Changes  
---|---  
2025-12-22 |  Enhancement:  
\- Added a grok pattern to parse the new log formats.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `process` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `tag` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `loglevel` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `internal_id`, `ruleset`, `ttl`, `source`, `allow_redirect`, `transaction_id`, `component`, `msg_code` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.ingestion_labels`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.metadata.ingestion_labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-14 |  \- Newly created parser.  
\- Mapped `emailInfo.xMsgRef` to `metadata.product_log_id`.  
\- Mapped `emailInfo.longMsgRef`, `emailInfo.messageId`, `emailInfo.isOutbound`, `emailInfo.HELOString`, `emailInfo.authResults.raw_header`, `emailInfo.authResults.dkim`, `emailInfo.authResults.dkim_signing_domain`, `emailInfo.authResults.spf`, `emailInfo.authResults.dmarc`, `emailInfo.authResults.dmarc_policy`, `emailInfo.authResults.dmarc_override_action`, `emailInfo.tlsInfo.tlsAdvertised`, `emailInfo.tlsInfo.tlsUsed`, `emailInfo.tlsInfo.tlsKeyLength`, `emailInfo.tlsInfo.tlsFallbackReason`, `emailInfo.tlsInfo.tlsForwardSecrecy`, `emailInfo.tlsInfo.tlsNegotiationFailed`, `emailInfo.messageSize`, `emailInfo.avQuarantinePenId`, `emailInfo.rawHeaderFrom`, `emailInfo.headerReplyTo`, `emailInfo.newDomainAge`, `emailInfo.timeInCynicSandboxMs`, and `incidents` to `additional.fields`.  
\- Mapped `emailInfo.subject` to `network.email.subject`.  
\- Mapped `emailInfo.envFrom` to `principal.user.email_addresses`.  
\- Mapped `emailInfo.headerFrom` to `network.email.from`.  
\- Mapped `emailInfo.envTo` to `network.email.to`.  
\- Mapped `emailInfo.headerTo` to `network.email.to`.  
\- Mapped `emailInfo.senderMailserver` to `principal.hostname`.  
\- Mapped `emailInfo.filesAndLinks` to about field.  
\- Mapped file.urlCategories to about.labels.  
\- Mapped file.urlRiskScore to about.labels.  
\- Mapped `emailInfo.tlsInfo.tlsPolicy` to `network.tls.version`.  
\- Mapped `emailInfo.tlsInfo.tlsProtocol` to `network.tls.version_protocol`.  
\- Mapped `emailInfo.tlsInfo.tlsCipher` to `network.tls.cipher`.  
\- Mapped `emailInfo.senderIp` to `principal.ip`.  
\- Mapped `emailInfo.senderMailserver` to `network.tls.client.server_name`.  
\- Mapped `emailInfo.country` to `principal.location.country_or_region`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
