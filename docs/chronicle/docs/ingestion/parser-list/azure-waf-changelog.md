---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-waf-changelog/
title: Change log for AZURE_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:57:38.953886+00:00
---

# Change log for AZURE_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_WAF

Date | Changes  
---|---  
2024-08-22 |  Enhancement:  
\- Mapped `properties.ruleSetType` to `security_result.detection_fields`.  
\- When `ruleName` and `ruleSetType` are null, mapped `properties.ruleSetType` to `security_result.rule_name`.  
\- Mapped `properties.details.data` to `security_result.detection_fields`.  
\- Mapped `properties.message` to `security_result.description`.   
2024-06-10 |  Enhancement:  
\- Modified the mapping of `properties.originalHost` (and fall back `properties.host` when originalHost is empty) to `target.hostname` and `target.asset.hostname` fields.  
\- Added conditional check for `dest_ip`.  
\- Combined `properties.requestUri` and `target_hostname` to get `target_url`.   
2024-04-07 |  Enhancement:  
\- Mapped `rec.properties.clientIp` to `principal.ip`.  
\- Defined `rec_properties_trackingReference`, `rec_properties_host`, `rec_properties_policyMode`, `rec_properties_ruleName`, `rec_properties_policy`, `rec_properties_details_msg`, `rec_properties_clientIP`, and `rec_time` in state data.   
2023-07-14 |  Enhancement:  
\- Added a `for` loop to handle JSON logs.   
2023-02-28 |  Enhancement:  
\- Mapped `properties.ruleName` to `security_result.rule_name`.  
\- Mapped `properties.action` to `security_result.action`.  
\- Added on_error check for `properties.clientPort`, `properties.httpStatus`, `properties.receivedBytes`, `properties.sentBytes`, `properties.clientResponseTime`, `properties.timeTaken`.   
2022-10-22 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
