---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-procurve-changelog/
title: Change log for HP_PROCURVE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:03.710565+00:00
---

# Change log for HP_PROCURVE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/hp-procurve-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for HP_PROCURVE

Date | Changes  
---|---  
2025-11-12 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `timezone`, `vendor_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field with key `timezone`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `prin_app` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2024-03-04 |  Enhancement:  
\- Added a Grok pattern to parse unparsing logs.  
\- If `severity` is equal to `DHCP`, then mapped `DHCP` to `network.application_protocol`.  
\- Mapped `severity` to `security_result.severity_details`.  
\- Mapped `prin_port` to `principal.port`.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `descript` to `metadata.description`.  
\- Mapped `inter_ip` to `intermediary.ip`.  
\- Mapped `remote_ip_address` to `principal.ip`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `status`, `config_method`, `event_id`, and `notice_type` to `additional.fields`.   
2023-09-24 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Mapped `target_mac` to `target.mac`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `src_mac` to `principal.mac`.  
\- Mapped `severity` to `security_result.severity`.   
2023-07-24 |  Enhancement -  
\- Added Grok pattern to parse and map unparsed logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
