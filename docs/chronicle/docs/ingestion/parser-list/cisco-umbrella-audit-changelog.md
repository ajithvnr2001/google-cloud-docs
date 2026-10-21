---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-audit-changelog/
title: Change log for CISCO_UMBRELLA_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:28:53.972182+00:00
---

# Change log for CISCO_UMBRELLA_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_UMBRELLA_AUDIT

Date | Changes  
---|---  
2026-08-20 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.vendor_name`: Updated the value of `event.idm.read_only_udm.metadata.vendor_name` from `CISCO UMBERLLA` to `CISCO UMBRELLA`.  
\- `event.idm.read_only_udm.metadata.product_name`: Updated the value of `event.idm.read_only_udm.metadata.product_name` from `CISCO UMBERLLA` to `CISCO UMBRELLA`.   
2025-09-30 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `column2` raw log field to event.idm.read_only_udm.metadata.event_timestamp.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user_mail` raw log field to event.idm.read_only_udm.principal.user.email_addresses.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `mail_to` raw log field to event.idm.read_only_udm.network.email.to.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `column5` raw log field to event.idm.read_only_udm.principal.resource.name.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `column6` raw log field to event.idm.read_only_udm.security_result.action_details.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `column6` raw log field to event.idm.read_only_udm.security_result.action.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column7` raw log field to event.idm.read_only_udm.principal.ip.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column7` raw log field to event.idm.read_only_udm.principal.asset.ip.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column1`, `column8`, `column9` and `column4` raw log field to event.idm.read_only_udm.additional.fields.   
2025-09-03 |  Enhancement:  
\- Added GROK patterns to parse unparsed logs.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly mapped id raw log field with event.idm.read_only_udm.principal.resource.product_object_id UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped createdAt raw log field with event.idm.read_only_udm.metadata.collected_timestamp UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped email raw log field with event.idm.read_only_udm.principal.user.email_addresses UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped user raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- Removed mapping of principal_user from event.idm.read_only_udm.principal.user.userid UDM field and mapped `event.idm.read_only_udm.principal.user.user_display_name` instead. (inappropriate mapping)  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped displayname raw log field with event.idm.read_only_udm.principal.user.user_display_name UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped action_type raw log field with event.idm.read_only_udm.network.http.method UDM field.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields.   
2025-08-21 |  Enhancement:  
\- Added a grok pattern to support new format of logs.  
\- Added a condition to map event_type to `NETWORK_DNS` if `network_dns_details_present` is equal to `true`.  
\- Added a condition to map event_type to `STATUS_UPDATE` if `has_principal` is equal to `true`.   
2024-01-10 |  Enhancement:  
\- Added support for DNS type logs.  
\- Mapped `date_time` to `metadata.event_timestamp`.  
\- Mapped `most_granular_identity`, `most_granular_identity_type`, `identity_types` and `blocked_categories` to `additional.fields`.  
\- Mapped `internal_ip` and `external_ip` to `principal.ip`.  
\- Mapped `action_type` to `security_result.action_details`.  
\- Mapped `dns_query_type` to `network.dns.questions.type`.  
\- Mapped `dns_response_code` to `network.dns.response_code`.  
\- Mapped `domain` to `network.dns.questions.name`.  
\- Mapped `categories` to `security_result.category_details`.   
2023-02-28 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
