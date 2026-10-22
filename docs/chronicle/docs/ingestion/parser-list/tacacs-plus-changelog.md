---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tacacs-plus-changelog/
title: Change log for TACACS_PLUS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:04.698819+00:00
---

# Change log for TACACS_PLUS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tacacs-plus-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TACACS_PLUS

Date | Changes  
---|---  
2025-03-13 |  \- Mapped `status to `security_result.action_details".  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `service` to `target.application`.  
\- Mapped `terminal` to `target.resource.name`.  
\- Mapped `command` to `target.process.command_line`.  
\- Mapped ` ResponseDescription` to `security_result.summary` when ResponseDescription is `pcre2` else mapped to `metadata.description`.  
\- Mapped `return_code` to `security_result.summary`.  
\- Mapped `process_id` to `target.process.pid`.  
\- Mapped `session_id` to `network.session_id`.  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `principalIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `device_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `Deviceip` to `target.asset.ip` and `target.ip`.  
\- Mapped `TACACS Plus` Value to `metadata.product_name`.  
\- Mapped `TACACS Plus` Value to `metadata.vendor_name`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
