---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-ips-changelog/
title: Change log for JUNIPER_IPS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:37:22.394918+00:00
---

# Change log for JUNIPER_IPS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-ips-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUNIPER_IPS

Date | Changes  
---|---  
2022-05-26 |  Added and modified multiple fields to increase log parsing percentage.  
\- source-address and internal-ip mapped to principal.ip.  
\- destination-address and reflexive-ip mapped to target.ip.  
\- destination-port and reflexive-port target.port.  
\- source-port and internal-port mapped to principal.port.  
\- bytes-from-client mapped to received_bytes.  
\- bytes-from-server mapped to sent_bytes.  
\- service-name,policy-name mapped to additional.fields.  
\- devicename mapped to principal.hostname.  
\- src-nat-rule-name mapped to security_result.rule_name.  
\- src-nat-rule-type mapped to security_result.rule_type.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
