---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opengear-changelog/
title: Change log for OPENGEAR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:27.766033+00:00
---

# Change log for OPENGEAR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/opengear-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPENGEAR

Date | Changes  
---|---  
2024-09-13 |  Enhancement:  
\- Added support for new format of SYSLOG logs.   
2024-06-24 |  Enhancement:  
\- Added the Grok patterns to handle the new pattern of authentication logs.  
\- Mapped `principal_port` to `principal.port`.   
2024-05-09 |  Enhancement:  
\- Added Grok patterns to parse a new pattern of SYSLOGS.  
\- Mapped `url` to `target.url`.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `x-pid` to `principal.process.pid`.  
\- Mapped `level` to `security_result.severity`.  
\- Mapped `http_method` to `network.http.method`.  
\- Mapped `swVersion` to `principal.platform_version`.  
\- Mapped `origin_software` to `principal.application`.  
\- Mapped `target_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `module`, `graphdrivers`, `commit`, and `version` to `additional.fields`.   
2024-04-05 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
