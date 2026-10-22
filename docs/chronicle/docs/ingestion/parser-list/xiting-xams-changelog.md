---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/xiting-xams-changelog/
title: Change log for XITING_XAMS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:49.169519+00:00
---

# Change log for XITING_XAMS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/xiting-xams-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for XITING_XAMS

Date | Changes  
---|---  
2024-09-26 |  Enhancement:  
\- Changed mapping for `sapClassName` from `security_result.description` to `security_result.category_details`.  
\- Mapped `sapEventId` to `metadata.product_event_type`.  
\- Mapped `duser` to `principal.user.userid`.  
\- Mapped `cs3` to `target.user.userid`.  
\- Mapped `suser` to `principal.user.userid`.  
\- When `column5` is having `/XITING/SA_S_SAL_PROTOCOL` as value then mapped `Security Audit Log` as `metadata.product_name` and `SAP` as `metadata.vendor_name`.  
\- Mapped `event_name_value` to `metadata.description`.  
\- Changed mapping for `msg` from `metadata.description` to `security_result.description`.  
\- Mapped `client` to `additional.fields`.   
2024-09-05 |  Enhancement:  
\- Mapped `sapTsUtc` to `metadata.event_timestamp`.  
\- Mapped `sapClassName`, `cs2` to `additional.fields`.  
\- When `sapEventId` is `AU7`, then mapped the following:  
\- `sapEventId` to `deviceEventClassID`.  
\- Changed cs_4 label key to `Client`.  
\- `column6` to `eventName`.  
\- `cs3` as `Report` in `additional.fields`.  
\- Changed cs_5 label key to `ParamC`.  
\- Mapped `shost` to `principal.application`.  
\- Mapped `suser` to `principal.user.user_display_name`.   
2024-08-12 |  Enhancement:  
\- Mapped `sourceAddress` to principal.ip.  
\- Mapped CEF header ip and host to intermediate.ip and intermediate.hostname respectively.   
2024-03-13 |  \- Updated mapping for raw fields `sapEventId`, `devicePayloadId`, `sapTsTime`, and `sapTsDate`.  
\- Updated parser with conditional mapping.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
