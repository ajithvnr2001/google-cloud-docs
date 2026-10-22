---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-dns-changelog/
title: Change log for AKAMAI_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:35:04.436133+00:00
---

# Change log for AKAMAI_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_DNS

Date | Changes  
---|---  
2024-11-25 |  Enhancement:  
\- If the `answers` field contains an integer value, it is mapped to the `network.dns.answers.ttl` field.   
2024-10-23 |  Enhancement:  
\- Removed the static number from the `network.dns.answers.name` field.   
2024-08-29 |  Enhancement:  
\- Mapped `answers` to `network.dns.answers.name`.   
2024-08-07 |  Enhancement:  
\- Mapped `rules.data` to `security_result.detection_fields`.  
\- Mapped `rules.action`, `rules.selector`, and `rules.version` to `security_result.action_details`.  
\- Mapped `rules.id` to `security_result.rule_id`.  
\- Mapped `rules.tag` to `security_result.category_details`.  
\- Mapped `rules.message` to `security_result.threat_name`.   
2024-05-28 |  Bug-Fix  
\- Added a gsub function to remove double quotes from the log message.  
\- Added Grok patterns to check IP address and port values before mapping.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
