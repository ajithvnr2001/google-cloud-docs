---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-edge-defense-changelog/
title: Change log for ARBOR_EDGE_DEFENSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:05:02.560698+00:00
---

# Change log for ARBOR_EDGE_DEFENSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arbor-edge-defense-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARBOR_EDGE_DEFENSE

Date | Changes  
---|---  
2025-10-16 |  Enhancement -  
\- Added grok pattern and KV filter to parse new pattern of logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cn1Label`, `cn1` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2023-02-21 |  Enhancement -  
\- Mapped `protection_Group_Name`,`traffic_level` to `principal.group.attribute.labels`.   
2022-11-03 |  Enhancement - Extracted the value of hostname from syslog header and mapped it to `intermediary.hostname`.  
\- Mapped `msg` to `metadata.description`.  
\- Extracted value of `group_name`, `traffic_level` from `msg` field and mapped it to `principal.group.attribute.labels`.  
\- Mapped `cs3Label`, `cs3` to `security_result.detection_fields`.  
\- Mapped `cs7` to `security_result.category_details`.   
2022-09-30 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
