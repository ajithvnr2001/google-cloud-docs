---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cequence-bot-defense-changelog/
title: Change log for CEQUENCE_BOT_DEFENSE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:58:11.309513+00:00
---

# Change log for CEQUENCE_BOT_DEFENSE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cequence-bot-defense-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CEQUENCE_BOT_DEFENSE

Date | Changes  
---|---  
2025-08-26 |  Enhancement:  
\- Declared field `sec_action` as "".  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped username raw log field to event.idm.read_only_udm.principal.user.userid UDM field.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields, event.idm.read_only_udm.security_result.detection_fields.   
2025-01-31 |  \- Mapped `status_code` to `network.http.response_code`.  
\- Mapped `country` to `principal.location.country_or_region`.  
\- Mapped `city` to `principal.location.city`.  
\- Mapped `experimental_confidence`, `extracted_data.respbody`, `successful_login`, `transaction_id`, and `tag` to `additional.fields`.  
\- Mapped `ruleinfo.weight`, `ruleinfo.hash_component`, `ruleinfo.experimental`, `x-cloud-trace-context`, `access-control-allow-headers, `access-control-allow-methods`, and `access-control-allow-origin` to `security_result.detection_fields".  
\- Mapped `server_ip` to `target.ip`.  
\- Mapped `confidence` to `security_result.confidence_details`.  
\- Mapped `mitigation_action` to `security_result.action`.  
\- Mapped `x_ip` to `principal.ip`.  
\- Mapped `x_externalip` to `target.ip`.   
2024-07-05 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
