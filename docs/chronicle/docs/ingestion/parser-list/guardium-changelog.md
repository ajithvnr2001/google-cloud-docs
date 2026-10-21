---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardium-changelog/
title: Change log for GUARDIUM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:02:01.388367+00:00
---

# Change log for GUARDIUM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardium-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GUARDIUM

Date | Changes  
---|---  
2025-01-28 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.   
2024-12-26 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.   
2024-08-05 |  Enhancement:  
\- Added support to handle unparsed LEEF format logs.   
2024-06-07 |  Enhancement:  
\- Mapped `query` to `additional.fields`.   
2024-04-01 |  Enhancement:  
\- Added mapping for `severity` with value `Very-High` to `security_result.severity`  
\- Added gsub function to manage `space` in the `spt` parameter before mapping to `principal.port`.   
2023-12-15 |  Enhancement:  
\- Added support for LEEF format logs.   
2022-10-06 |  Added Grok pattern to parse syslog logs.  
\- Changed `observer.hostname` mapping to `intermediary.hostname`.  
\- Changed `observer.ip` mapping to `intermediary.hostname`.   
2022-09-06 |  Enhancement:  
\- Migrated customer-specific parser to default and also removed customer-specific parser.   
2022-07-08 |  Enhancement:  
\- Modified mapping for `user_role` from `target.user.role_name` to `target.user.attribute.roles`.   
2022-06-30 |  Enhancement: Added mappings for the following fields:  
\- Mapped `timestamp` to `metadata.collected_timestamp`  
\- Mapped SQL to `security_result.summary`  
2022-05-17 |  Enhancement: Modified the parser to support logs that are in `CEF` format.   
2022-03-24 |  Enhancement: Added mappings for the following new fields:  
`Full SQL ID` field mapped to `event.idm.read_only_udm.target.process.pid`.  
`Session ID` field mapped to `event.idm.read_only_udm.network.session_id`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
