---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-access-manager-changelog/
title: Change log for NETIQ_ACCESS_MANAGER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:39.304195+00:00
---

# Change log for NETIQ_ACCESS_MANAGER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netiq-access-manager-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETIQ_ACCESS_MANAGER

Date | Changes  
---|---  
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `2` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `3` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Added gsub to replace `\\r\\n` with ` ` , `\\n` with "` and `<@>` with `@".   
2025-04-24 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `1` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `USER_LOGIN` if `I` raw log field is in `002E0505,002E001E,002E0046`.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` UDM field with `BLOCK` if `I` raw log field is in `002E0505,002E001E,002E0046`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Mapped `event.idm.read_only_udm.extensions.auth.type` UDM field with `AUTHTYPE_UNSPECIFIED` when `event.idm.read_only_udm.metadata.event_type` UDM field is `USER_LOGIN` or `USER_LOGOUT`.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `NETWORK_UNCATEGORIZED` if `I` raw log field is `002E0525`.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` UDM field with `ALLOW` if `I` raw log field is `002E0525,002E0045`.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `USER_LOGOUT` if `I` raw log field is `002E0007,002E000C`.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `event.idm.read_only_udm.metadata.event_type` UDM field with `USER_LOGIN` if `I` raw log field is `002E0045`.  
\- `event.idm.read_only_udm.principal.application`: Newly Mapped `appName` raw field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `stringValue2` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eventId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `subTarget` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `stringValue1` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `stringValue3` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `originator` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `originator` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- Added a grok pattern to support variation of log.   
2025-03-18 |  Enhancement:  
\- Mapped `A` to `security_result.rule_id`.  
\- Mapped `B` to `target.resource.id`.  
\- Mapped `D` to `metadata.description`.  
\- Mapped `F` to `principal.application`.  
\- Mapped `G`,`H`,`M` and `V` to `security_result.detection_fields`.  
\- Mapped `I` to `metadata.product_log_id`.  
\- Mapped `L` to `event.idm.read_only_udm.network.session_id`.  
\- Mapped `O` to `target.resource.name`.  
\- Mapped `S` to `target.user.group_identifiers`.  
\- Mapped `T` to `event.idm.read_only_udm.network.http.user_agent`.  
\- Mapped `U` to `target.user.userid`.  
\- Mapped `Y` to `target.url`.  
\- Mapped `host_name` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `process_name` to `target.application`.  
\- Added null checks for `product`, `product_version` and `event_id`.   
2024-12-12 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
