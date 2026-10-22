---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mandiant-custom-ioc-changelog/
title: Change log for MANDIANT_CUSTOM_IOC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:40.427485+00:00
---

# Change log for MANDIANT_CUSTOM_IOC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mandiant-custom-ioc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MANDIANT_CUSTOM_IOC

Date | Changes  
---|---  
2023-12-19 |  \- Mapped `threat.threat_feed_name` to `Mandiant`.   
2023-12-07 |  \- Mapped `first_seen` to `metadata.interval.start_time`.  
\- When `type` is `fqdn/ipv4/url`, then mapped `custom_ioc_expire_date` to `metadata.interval.end_time`.  
\- Mapped `threat_rating.threat_score` to `entity.entity.labels`.  
\- Mapped `threat_rating.severity_level` to `threat.severity`.  
\- Mapped `threat_rating.confidence_level` to `threat.confidence`.  
\- Mapped `verdict_simple.timestamp` to `verdict_info.verdict_time`.  
\- When `verdict_simple.verdict` is `malicious`, then set `verdict_info.verdict_response` to `MALICIOUS`.  
\- Mapped `verdict_info.verdict_type` based on `verdict_simple.verdict_source`.  
\- Mapped `category` to `threat.category_details`.  
\- Mapped `threat_rating.confidence_score` to `threat.confidence_details`.  
\- Mapped `threat_rating.threat_score` to `threat.risk_score`.   
2023-11-17 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
