---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/unifi-ap-changelog/
title: Change log for UNIFI_AP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:06.766701+00:00
---

# Change log for UNIFI_AP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/unifi-ap-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UNIFI_AP

Date | Changes  
---|---  
2025-11-24 |  Enhancement:  
\- Added new Grok pattern to parse new format logs.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `principal_mac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `details`, `event_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `assoc_status`, `dns_resp_seen`, `avg_rssi` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.   
2024-03-22 |  Enhancement:  
\- Added new Grok pattern to parse new format logs.   
2022-05-24 |  Enhancement - Mapped `event_type` to security_result.action_details   
2022-04-13 |  Bug fix-Added null check for PROTO field prior to mapping it to ip_protocol. Increased parsing percentage by making all the unparsed logs get parsed.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
