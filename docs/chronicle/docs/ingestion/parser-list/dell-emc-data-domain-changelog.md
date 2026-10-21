---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-data-domain-changelog/
title: Change log for DELL_EMC_DATA_DOMAIN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:20:45.589061+00:00
---

# Change log for DELL_EMC_DATA_DOMAIN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/dell-emc-data-domain-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DELL_EMC_DATA_DOMAIN

Date | Changes  
---|---  
2026-08-07 |  Enhancement:  
\- Modified grok patterns to parse the raw log fields.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Modified the value of `event.idm.read_only_udm.metadata.product_name` from `DELL_EMC_DATA_DOMAIN` to `PowerProtect Data Domain`.  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `host` raw log field from `event.idm.read_only_udm.principal.hostname` UDM field if it matches an IP address pattern to map it to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `host` raw log field from `event.idm.read_only_udm.principal.asset.hostname` UDM field if it matches an IP address pattern to map it to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- Introduced new grok patterns that extract `time`, `inter_host`, `app`, `pid`, `msg1`, `kv_data`, `id`, `reason`, `cmd`, `kernel_error`, `kernel_timestamp` raw fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: The `time` raw log field is now parsed and used to update the event's primary timestamp.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `kernel_timestamp`, `kernel_error` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-09-20 |  Enhancement:  
\- Added support to handle unparsed logs.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `role` from `principal.user.role_name` to `principal.user.attribute.roles`.   
2022-04-27 |  New Default parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
