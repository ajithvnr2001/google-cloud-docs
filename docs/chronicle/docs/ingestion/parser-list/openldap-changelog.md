---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openldap-changelog/
title: Change log for OPENLDAP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:27.536235+00:00
---

# Change log for OPENLDAP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openldap-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPENLDAP

Date | Changes  
---|---  
2025-11-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped eventType raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cn`,`sequenceId`, `dc_2`, `dc_3`, `dc`, and `dc_1` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `path` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- Added new Grok patterns to parse new format logs.   
2025-02-14 |  Enhancement:  
\- Mapped `filter` to `additional.fields`.  
\- Added a new Grok pattern to parse new format logs.   
2025-02-11 |  Enhancement:  
\- Added Grok patterns to parse new format logs.  
\- Added the correct mappings for `additional.fields`. For example, `ou`, `ou_1`, and `ou_2`.   
2025-01-29 |  Enhancement:  
\- Added Grok patterns to parse new format logs.  
\- Added the correct mappings for `additional.fields`. For example, `cn`, `dc`, `method`, `Request and Response`.  
\- Mapped `ip1` to `principal.ip`.   
2024-12-17 |  Enhancement:  
\- Mapped `base`, `err`, `attr`, `tag`, `scope`, and `valueData` to `additional.fields`.   
2024-06-06 |  Enhancement:  
\- Added Grok patterns to parse new format logs.  
\- Mapped `principal_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `syslog_process` to `principal.process.file.full_path`.  
\- Mapped `syslog_pid` to `principal.process.pid`.  
\- Mapped `ldap_conn` to `metadata.product_log_id`.  
\- Mapped `op` to `additional.fields`.  
\- Mapped `fd` to `additional.fields`.  
\- Mapped `msg1` to `metadata.description`.  
\- When `err` = `0`, then mapped `security_result.action` to `ALLOW`.  
\- When `err` = `50`, then mapped `security_result.action` to `BLOCK`.  
\- When `err` = `2`, then mapped `security_result.action` to `BLOCK`.  
\- Mapped `ldap_action` to `metadata.product_event_type`.  
\- Mapped `prin_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `tuser` to `target.user.userid`.   
2023-07-18 |  Enhancement:  
\- Added a Grok pattern to parse failing logs.   
2022-08-17 |  Enhancement:  
\- Handled the dropped logs due to grak failure and mapped them to valid event_types.  
\- Mapped `metadata.event_type` to `STATUS_UPDATE` where `principal.hostname` is not null else mapped it as `GENERIC_EVENT`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
