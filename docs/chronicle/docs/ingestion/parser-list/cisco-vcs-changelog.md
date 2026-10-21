---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vcs-changelog/
title: Change log for CISCO_VCS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:55:18.185827+00:00
---

# Change log for CISCO_VCS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-vcs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_VCS

Date | Changes  
---|---  
2025-08-22 |  \- A new grok pattern was added to parse logs that use the ISO8601 timestamp format.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped timestamp raw log field with event.idm.read_only_udm.metadata.event_timestamp UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped principal_hostname raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped Src-ip, Local-ip raw log field(s) with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped Dst-ip raw log field with event.idm.read_only_udm.target.asset.ip UDM field.  
\- event.idm.read_only_udm.additional.fields: Dynamically maps key-value pairs from the addition map. The Msg-Hash, From-Tag, Call-ID, CSeq, To-Tag and To raw log fields are mapped as key-value pairs.  
\- Added on_error checks to all mutate, grok, kv, and date filters to prevent parsing failures from stopping the entire pipeline.   
2023-06-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
