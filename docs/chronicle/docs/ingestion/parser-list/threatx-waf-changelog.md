---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatx-waf-changelog/
title: Change log for THREATX_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:00:58.329356+00:00
---

# Change log for THREATX_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/threatx-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for THREATX_WAF

Date | Changes  
---|---  
2025-01-28 |  \- Mapped `dst_domain` to `target.hostname` and `target.assest.hostname`.  
\- Defined `version`, `severity`, and `priority` fields in statedata.  
\- Mapped `rule.id`, `rule.description`, `rule.classification`, `rule.state`, `rule.contrib_score`, `rule.beta`, and `rule.blocking` to `security_result.detection_fields`.  
\- Mapped `action`, `tenant_name`, `random_id`, `cookie`, `js_fingerprint`, `content_type`, `postblock_event`, `ssl`, `content_length`, `count`, `upstream_response_time`, `upstream_response_time`, and `response_length` to `additional.fields`.  
\- Mapped `risk` to `security_result.risk_score`.  
\- Mapped `rule.description` to `metadata.description`.  
\- Added a new Grok pattern to map `msg1` to `principal.url`.  
\- Mapped `username` to `target.hostname` and `target.assest.hostname`.  
\- Mapped `old_value` and `new_value` to `additional.fields`.   
2024-10-14 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
