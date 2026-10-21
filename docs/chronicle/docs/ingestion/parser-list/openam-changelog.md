---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openam-changelog/
title: Change log for OPENAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:59:42.508559+00:00
---

# Change log for OPENAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openam-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPENAM

Date | Changes  
---|---  
2024-11-28 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- Added support for new pattern of SYSLOG logs.   
2024-02-09 |  Enhancement:  
\- When `eventName` is `AM-SESSION-MAX_TIMED_OUT`, then set `metadata.event_type` to `USER_LOGOUT`.   
2024-02-06 |  \- Added support for new pattern of JSON logs.  
\- When `principal` is present and `metadata.event_type` is `GENERIC_EVENT`, then set `metadata.event_type` to `STATUS_UPDATE`.  
\- When `eventName` is `AM-ACCESS-OUTCOME`, then mapped `http.request.headers.host.0` to `tatget.hostname`.  
\- When `eventName` is `AM-ACCESS-OUTCOME`, then mapped `http.request.headers.user-agent.0` to `network.http.user_agent`.  
\- When `eventName` is `AM-ACCESS-OUTCOME`, then mapped `http.request.path` to `target.url`.  
\- When `eventName` is `AM-ACCESS-OUTCOME`, then mapped `http.request.method` to `network.http.method`.  
\- When `http.request.secure` is `true`, then set `network.application_protocol` to `HTTPS`.  
\- When `http.request.secure` is not `true`, then set `network.application_protocol` to `HTTP`.  
\- Aligned `principal.ip`, `target.ip`, `target.hostname` to `principal.asset.ip`, `target.asset.ip`, `target.asset.hostname`.   
2023-05-19 |  \- Mapped `extensions.auth.type` to `SSO` where `eventName` indicates login and logout events.  
\- Added check to `server.ip` prior mapping to UDM.   
2023-05-15 |  \- Added support for JSON format logs.   
2022-12-26 |  Bug - The field `info.ipAddress` is mapped to `principal.ip`.   
2022-04-29 |  Bug - Mapped target.userid for unparsed logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
