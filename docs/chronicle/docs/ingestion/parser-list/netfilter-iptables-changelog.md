---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netfilter-iptables-changelog/
title: Change log for NETFILTER_IPTABLES \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:25:01.236704+00:00
---

# Change log for NETFILTER_IPTABLES  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/netfilter-iptables-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for NETFILTER_IPTABLES

Date | Changes  
---|---  
2025-11-17 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rulename` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `application` raw log field with `event.idm.read_only_udm.additional_fields` UDM field.  
\- Updated the date filter to handle the new pattern of timestamp with `yyyy-MM-ddTHH:mm:ssZZ` format.   
2023-10-12 |  Enhancement:  
\- Added a Grok pattern to parse SYSLOG type logs.  
\- Mapped `OUT` to `target.resource.attribute.labels`.  
\- Mapped `IN` to `principal.resource.attribute.labels`.   
2022-10-12 |  Enhancement:  
\- Added new grok to parse unparsed logs(logs with header format <133> Sep 29 01:38:26).  
\- Mapped security_result.action to Block where action is reject.   
2022-10-04 |  Enhancement:  
\- Remapped `src_host` to `intermediary.hostname` instead of `principal.hostname`.   
2022-06-21 |  Enhancement:  
\- Mapped `TOS` with `tos_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `LEN` with `len_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `URGP` with `urgp_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `PREC` with `prec_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `SPI` with `spi_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `CODE` with `code_label` to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `DF` with `df_label` to `event.idm.read_only_udm.additional.fields`.  
\- If `action` is `DROP` then `security_result.action` is assigned with `BLOCK`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
