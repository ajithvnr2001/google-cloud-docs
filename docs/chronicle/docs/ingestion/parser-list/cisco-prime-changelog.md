---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-prime-changelog/
title: Change log for CISCO_PRIME \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:49.643104+00:00
---

# Change log for CISCO_PRIME  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-prime-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_PRIME

Date | Changes  
---|---  
2025-04-30 |  Enhancement:  
\- Added grok patterns to parse new pattern of logs.  
\- event.idm.read_only_udm.metadata.timestamp: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `target_hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2024-01-26 |  Bug-Fix:  
\- Added Grok patterns to reduce percentage of `GENERIC_EVENT` event types.  
\- Mapped `principal_port` to `principal.port`.  
\- Mapped `ip_address` to `principal.asset.ip`.  
\- Mapped `user_name` to `principal.user.userid`.  
\- Mapped `device_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `client_ip_address` to `principal.ip`, `principal.asset.ip`.  
\- Mapped `principal_ip` to `principal.ip`, `principal.asset.ip`.  
\- Mapped `Type` to `metadata.product_event_type`.  
\- Mapped `dst_user` to `target.user.userid`.  
\- Mapped `target_ip` to `target.asset.ip`.  
\- Mapped `device_type` to `target.resource.attribute.labels`.  
\- Mapped `device_hostname` to `target.resource.attribute.labels`.  
\- Mapped `sec_description` to `security_result.description`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
