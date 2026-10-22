---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-nx-os-changelog/
title: Change log for CISCO_NX_OS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:50.263274+00:00
---

# Change log for CISCO_NX_OS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-nx-os-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_NX_OS

Date | Changes  
---|---  
2025-07-02 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support to include timezone for `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added support to map `status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field globally.   
2025-06-16 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support globally to map `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-06-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support for new format of timestamp for `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-06-05 |  Enhancement:  
\- Added a Grok patterns to parse `event.idm.read_only_udm.intermediary.hostname` UDM field correctly.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `ipaddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.assets.ip: Newly mapped `ipaddress` raw log field with `event.idm.read_only_udm.principal.assets.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `src_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field when it is an HOSTNAME.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `ip_or_host` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field when it is an IP.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `descrip` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- Added conditional check `has_user` == `true` or `has_target_user == `true` before mapping event_type to `USER_UNCATEGORIZED".  
\- Added conditional check `has_principal` == `true` before mapping event_type to `STATUS_UPDATE`.   
2025-05-19 |  Enhancement:  
\- Added a Grok pattern to parse `event.idm.read_only_udm.intermediary.hostname` UDM field correctly.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `tar_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.   
2025-05-14 |  Enhancement:  
\- Added a Grok pattern for `description` to parse important UDM field values.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `roles` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.assets.ip`: Newly mapped `prin_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.assets.ip` UDM field   
2025-04-14 |  Enhancement:  
\- Added a Grok pattern in order to map the `GENERIC_EVENT` logs to proper `event_type`.  
\- Added a Grok pattern to extract the `username` field from a new format of logs with SYSLOG format.   
2025-03-05 |  Enhancement:  
\- Added support for SYSLOG logs.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.   
2025-02-14 |  Enhancement:  
\- Changed mapping of `device_ip` to `intermediary.hostname` and `intermediary.ip`.  
\- Removed mapping of `device_ip` to `target.ip`.   
2025-02-07 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2025-02-05 |  Enhancement:  
\- Added a new Grok pattern to support new log formats.  
\- Mapped `Hostname` to `intermediary.hostname`.  
\- Mapped `ip_1` to `intermediary.ip`.   
2024-12-23 |  Enhancement:  
\- Changed mapping of `device_ip` from `principal.ip`. If `device_ip` is an IP address, it is mapped to `intermediary.ip`. Otherwise, it is mapped to `intermediary.hostname`.   
2023-09-05 |  Enhancement:  
\- Added a new Grok pattern to support new log formats.   
2023-08-11 |  Enhancement:  
\- Added support for logs containing `AAA_ACCOUNTING_MESSAGE`.  
\- Added new Grok pattern to support new log formats.  
\- Reduced number of `GENERIC_EVENTS` by mapping `metadata.event_type` to a more specific enum value.   
2023-06-28 |  \- Added new Grok pattern to parse date.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
