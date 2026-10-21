---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortinac-changelog/
title: Change log for FORTINET_FORTINAC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:12:53.646943+00:00
---

# Change log for FORTINET_FORTINAC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fortinet-fortinac-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FORTINET_FORTINAC

Date | Changes  
---|---  
2025-05-15 |  Enhancement:  
\- Added new grok patterns in order to parse the logs with CEF format.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `src_hst1` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `src_hst1` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field  
\- event.idm.read_only_udm.principal.mac: Newly mapped `src_macadd` raw log field with `event.idm.read_only_udm.principal.mac` UDM field  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped `src_macadd` raw log field with `event.idm.read_only_udm.principal.mac` UDM field  
\- `USER_UNCATEGORIZED`: Added support for the event `USER_UNCATEGORIZED` and relevant corresponding raw log fields.  
\- `SYSLOG+CSV`: Added support for `SYSLOG+CSV` format.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `column2` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `column3` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column6` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.principal.mac: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.mac` UDM field  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.mac` UDM field  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field  
\- event.idm.read_only_udm.metadata.description: Newly mapped `column10` raw log field with `event.idm.read_only_udm.metadata.description` UDM field  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `rule_name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column8` raw log field with `event.idm.read_only_udm.principal.ip` UDM field  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column8` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field  
\- event.idm.read_only_udm.target.mac: Newly mapped `column9` raw log field with `event.idm.read_only_udm.target.mac` UDM field  
\- event.idm.read_only_udm.target.asset.mac: Newly mapped `column9` raw log field with `event.idm.read_only_udm.target.mac` UDM field   
2022-07-08 |  Enhancement:  
\- Modified mapping for `oldrole` from `principal.user.role_name` to `principal.user.attribute.roles`.  
\- Modified mapping for `newrole` from `target.user.role_name` to `target.user.attribute.roles`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
