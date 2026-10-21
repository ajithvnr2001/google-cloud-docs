---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thycotic-changelog/
title: Change log for THYCOTIC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:18:45.966628+00:00
---

# Change log for THYCOTIC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/thycotic-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THYCOTIC

Date | Changes  
---|---  
2024-10-08 |  Enhancement:  
\- Defined the `msg` field in a mutate replace filter.   
2024-06-04 |  Enhancement:  
\- Added a Grok block to parse unparsed logs.  
\- Mapped `Host` and `server` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `Container_Id` to `principal.asset.asset_id`.  
\- Mapped `Container_name` to `principal.resource.name`.   
2023-09-22 |  Enhancement:  
\- Modified the Grok pattern to parse unparsed logs.  
\- Added `on_error` check for fields `rt` and `ts`.   
2023-06-12 |  Enhancement -  
\- Modified the Grok pattern to parse new log format.  
\- Mapped `fname` to `additional.fields`.  
\- Mapped `cs2` to `additional.fields`.  
\- Mapped `details` to `additional.fields` and `security_result.summary`.   
2022-08-01 |  Enhancement -  
Mapped the following fields for logs in JSON format :  
\- `device_version` to `metadata.product_version`.  
\- `agent.id` to `observer.asset_id`.  
\- `agent.version` to `observer.platform_version`.  
\- `agent.hostname` to `observer.hostname`.  
\- `agent.type` to `observer.application`.  
\- `agent.name` to `observer.user.userid`.  
\- `agent.ephemeral_id` to `observer.labels`.  
\- `log.source.address` to `principal.ip`.  
\- `host.hostname` to `principal.hostname`.  
\- `host.id` to `principal.asset.asset_id`.  
\- `host.os.kernel` to `principal.platform_patch_level`.  
\- `host.os.version` to `principal.platform_version`.  
\- `host.os.platform` to `principal.platform`.  
\- `host.architecture` to `principal.asset.hardware.cpu_platform`.  
\- `syslog_severity` to `security_result.severity`.  
\- Parsed logs with type `SECRET - SECRETPASSWORDCHANGEFAILURE`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
