---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-shape-changelog/
title: Change log for F5_SHAPE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:53:20.837448+00:00
---

# Change log for F5_SHAPE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/f5-shape-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for F5_SHAPE

Date | Changes  
---|---  
2024-08-20 |  Bug-Fix:  
\- If `target` is null, and `has_principal_machine` is `true`, then mapped `metadata.event_type` to `STATUS_UPDATE`, else it is mapped to `GENERIC_EVENT`.  
\- Mapped `requestHeaders_id_array.User-Agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped `requestHeaders_id_array.Referer` to `network.http.referral_url`.  
\- Mapped `requestHeaders_id_array.Proxy-Client-IP`, `requestHeaders_id_array.WF-Forwarded-For`, `requestHeaders_id_array.X-Forwarded-For`, and `requestHeaders_id_array.wl-proxy-client-ip` to `additional.fields`.   
2024-06-18 |  \- Added support to handle unparsed JSON logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
