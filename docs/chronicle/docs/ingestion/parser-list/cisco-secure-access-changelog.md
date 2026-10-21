---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-access-changelog/
title: Change log for CISCO_SECURE_ACCESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:41:45.121210+00:00
---

# Change log for CISCO_SECURE_ACCESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-secure-access-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_SECURE_ACCESS

Date | Changes  
---|---  
2026-06-10 |  Enhancement:  
\- `event.idm.read_only_udm.network.sent_bytes`: Removed mapping of `column12` from `event.idm.read_only_udm.network.sent_bytes` UDM field as it contains `security_rule_id` related data.  
\- `event.idm.read_only_udm.security_result.rule_id`: Mapped `column12` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Removed mapping of `column15` from `event.idm.read_only_udm.network.received_bytes` UDM field as it contains `product_object_id` related data.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Mapped `column15` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Removed mapping of `column56` from `event.idm.read_only_udm.security_result.rule_name` UDM field as it contains `profile_id` related data.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `column56` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column32` from `event.idm.read_only_udm.additional.fields` UDM field as it contains `action` related data.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped `column32` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.   
2026-04-03 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column22` from `event.idm.read_only_udm.additional.fields` UDM field as it represents an User Source Group rather than additional fields.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Mapped `column22` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column11` from `event.idm.read_only_udm.additional.fields` UDM field as it represents the HTTP response code rather than additional fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column16` from `event.idm.read_only_udm.additional.fields` UDM field as it represents the security result category details rather than additional fields.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `column44` from `event.idm.read_only_udm.additional.fields` UDM field as it represents the hostname rather than additional fields.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `column11` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `column44` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `column44` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `column25` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `column8` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Modified a conditional check to parse the `column10` correctly in `event.idm.read_only_udm.network.http.user_agent` UDM field.   
2026-03-17 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.user_agent`: Modified a conditional check to parse the `column10` correctly in `event.idm.read_only_udm.network.http.user_agent`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Modified a conditional check to correctly parse `column10` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.   
2026-03-13 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: If the `column6` raw log field contains `block`, the value of the `event.idm.read_only_udm.security_result.action` UDM field is updated to `BLOCK`.  
\- Due to the above change, `column6` raw log field having values similar to `block` is no longer being mapped to `event.idm.read_only_udm.additional.fields`.  
\- Modified the conditional mapping of `column3` to `event.idm.read_only_udm.principal.hostname` to execute when `is_dns` is `true`.   
2026-02-18 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `column 10` to `event.idm.read_only_udm.network.http.user_agent` after regex check.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column 15` to `event.idm.read_only_udm.additional.fields` after conditional check.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column 30` to `event.idm.read_only_udm.additional.fields` after regex check.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column 43` to `event.idm.read_only_udm.additional.fields` after conditional check.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `column 2` to `event.idm.read_only_udm.principal.user.user_display_name` using grok.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `column 5` to `event.idm.read_only_udm.target.ip` using grok.  
\- `event.idm.read_only_udm.target.ip: Newly mapped `column 4` to `event.idm.read_only_udm.target.ip` using grok.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `column 26` to `event.idm.read_only_udm.network.http.method` after conditional check.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `column 45` to `event.idm.read_only_udm.principal.user.windows_sid` using grok.  
\- Added grok patterns and conditions, allowing the following UDM fields to be mapped correctly:  
event.idm.read_only_udm.additional.fields  
event.idm.read_only_udm.intermediary.hostname  
event.idm.read_only_udm.metadata.event_timestamp.seconds  
event.idm.read_only_udm.metadata.event_type  
event.idm.read_only_udm.metadata.product_log_id  
event.idm.read_only_udm.metadata.product_name  
event.idm.read_only_udm.metadata.vendor_name  
event.idm.read_only_udm.network.application_protocol  
event.idm.read_only_udm.network.http.method  
event.idm.read_only_udm.network.http.user_agent  
event.idm.read_only_udm.network.ip_protocol  
event.idm.read_only_udm.network.received_bytes  
event.idm.read_only_udm.network.sent_bytes  
event.idm.read_only_udm.network.session_id  
event.idm.read_only_udm.principal.application  
event.idm.read_only_udm.principal.asset.hostname  
event.idm.read_only_udm.principal.asset.ip  
event.idm.read_only_udm.principal.asset.product_object_id  
event.idm.read_only_udm.principal.asset.software.name  
event.idm.read_only_udm.principal.hostname  
event.idm.read_only_udm.principal.ip  
event.idm.read_only_udm.principal.platform_version  
event.idm.read_only_udm.principal.process.file.full_path  
event.idm.read_only_udm.principal.process.pid  
event.idm.read_only_udm.principal.user.email_addresses  
event.idm.read_only_udm.principal.user.group_identifiers  
event.idm.read_only_udm.principal.user.user_display_name  
event.idm.read_only_udm.principal.user.userid  
event.idm.read_only_udm.principal.user.windows_sid  
event.idm.read_only_udm.security_result.action  
event.idm.read_only_udm.security_result.rule_name  
event.idm.read_only_udm.target.asset.hostname  
event.idm.read_only_udm.target.asset.ip  
event.idm.read_only_udm.target.hostname  
event.idm.read_only_udm.target.ip   
2026-01-27 |  Enhancement:  
\- Modified the conditions under which `column45` is mapped. The raw log field `column45` is now only mapped to `event.idm.read_only_udm.principal.user.windows_sid` if its value is not empty, `true`, or `false`. If the value of `column45` is `true` or `false`, it is instead mapped to `event.idm.read_only_udm.additional.fields` with `column45` as the key.  
\- Modified the conditions under which `column33` is mapped. The raw log field `column33` is now mapped to `event.idm.read_only_udm.target.port` if its value is an_integer. If the value of `column33` is `not_an_integer`, it is instead mapped to `event.idm.read_only_udm.additional.fields` with `column33` as the key.  
\- Modified the conditions under which `column22` is mapped. The raw log field `column22` is now mapped to `event.idm.read_only_udm.target.ip` if its value is ip. If the value of `column22` is `not_an_ip`, it is instead mapped to `event.idm.read_only_udm.additional.fields` with `column22` as the key.  
\- Modified the conditions under which `column3` is mapped. The raw log field `column3` is now mapped to `event.idm.read_only_udm.principal.user.user_display_name` if its value is `not_an_ip` . If the value of `column3` is `an_ip`, it is instead mapped to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column45`, `column22`, `column55` and `column33` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-21 |  \- Newly Created Parser:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `column2`, `column3`, `column7` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column4`, `column10`, `column15` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column5`, `column16`, `column22` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column7`, `column43` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `column1` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column6`, `column8`, `column9`, `column10`, `column11`, `column13`, `column14`, `column16`, `column17`, `column18`, `column19`, `column23`, `column24`, `column25`, `column27`, `column28`, `column29`, `column32`, `column36`, `column42`, `column44`, `column46`, `column47`, `column48`, `column49`, `column50`, `column51`, `column52`, `column53`, `column54`, raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `column15` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `column20` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `column5`, `column21` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `column33` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `column34` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `column26` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `column3` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.software`: Newly mapped `column30` raw log field with `event.idm.read_only_udm.principal.asset.software` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `column31` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `column35` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `column40` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `column41` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `column57` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `column56` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `column6` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `auth_event` is true, updated to `USER_LOGIN`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is true and `has_target` is true, updated to `NETWORK_CONNECTION`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is true, updated to `STATUS_UPDATE`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_user` is true, updated to `USER_UNCATEGORIZED`.  
\- `event.idm.read_only_udm.metadata.event_type`: If none of the above conditions are met, updated to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `column45` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
