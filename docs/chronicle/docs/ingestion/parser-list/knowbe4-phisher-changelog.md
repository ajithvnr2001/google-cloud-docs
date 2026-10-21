---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/knowbe4-phisher-changelog/
title: Change log for KNOWBE4_PHISHER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:12:35.744697+00:00
---

# Change log for KNOWBE4_PHISHER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/knowbe4-phisher-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KNOWBE4_PHISHER

Date | Changes  
---|---  
2025-12-12 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped receivedAt raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped reportedAt raw log field with event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped syslog_hostname raw log field with event.idm.read_only_udm.intermediary.hostname UDM field.  
\- event.idm.read_only_udm.intermediary.asset.hostname: Newly mapped syslog_hostname raw log field with event.idm.read_only_udm.intermediary.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped sender raw log field with event.idm.read_only_udm.principal.user.email_addresses UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped sender raw log field with event.idm.read_only_udm.principal.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped reporter raw log field with event.idm.read_only_udm.target.user.email_addresses UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped reporter raw log field with event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped action raw log field with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped priority raw log field with event.idm.read_only_udm.security_result.priority_details UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped status raw log field with event.idm.read_only_udm.security_result.action_details UDM field.  
\- event.idm.read_only_udm.network.email.subject: Newly mapped subject raw log field with event.idm.read_only_udm.network.email.subject UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped category raw log field with event.idm.read_only_udm.security_result.category_details UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped permalink raw log field with event.idm.read_only_udm.target.url UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped syslog_program raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_user_email is true, updated to USER_UNCATEGORIZED.  
\- The parser now supports syslog-formatted logs, extracting a JSON payload from the message field.  
\- The log drop condition has been updated to trigger only if both syslog grok parsing and the subsequent JSON parsing fail.   
2025-06-05 |  Enhancement:  
\- Added gsub to replace `Message-ID` with `Message-Id` and `In-Reply-To` with `Reply-To` for new logs.  
\- Changed the field name from `indexraw` to `indexhtml`.  
\- Changed the field name from `indexraw` to `indextext`.  
\- Modified condition to check if `indexhtml`,`indexraw` and `indextext` is equal to the string ``0`` OR the integer `0`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly Mapped `Received` raw log field to extract the ip address and mapped with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Date` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly Mapped `Received-SPF`, `Authentication-Results`, `X-SES-RECEIPT`, `X-SES-DKIM-SIGNATURE`, `ARC-Seal`, `ARC-Message-Signature`, `ARC-Authentication-Results`, `X-Google-DKIM-Signature`, `X-Forwarded-Encrypted`, `X-Gm-Message-State`, `X-Received`, `X-Forwarded-To`, `X-Forwarded-For`, `DKIM-Signature`, `X-Gm-Gg`, `X-Google-Smtp-Source`, and `X-Gm-Features` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2024-10-16 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
