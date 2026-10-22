---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/isc-dhcp-changelog/
title: Change log for ISC_DHCP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:43.342438+00:00
---

# Change log for ISC_DHCP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/isc-dhcp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ISC_DHCP

Date | Changes  
---|---  
2024-11-27 |  Bug-Fix:  
\- Changed mapping for `host` from `principal.hostname` to `target.asset.hostname`.  
\- Mapped `pid` go `target.process.pid`.  
\- Mapped `process` to `target.application`.  
\- Mapped `via` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `ipaddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `macaddress` to `principal.mac` and `principal.asset.mac`.   
2024-01-29 |  Enhancement:  
\- Added Grok patterns to parse dropped logs.   
2023-12-29 |  Enhancement:  
\- Added Grok patterns to match new log format.  
\- If `network.dhcp.ciaddr` is not set, set `metadata.event_type` to `STATUS_UPDATE`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
