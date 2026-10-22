---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-ddi-changelog/
title: Change log for TRENDMICRO_DDI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:32.394627+00:00
---

# Change log for TRENDMICRO_DDI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/trendmicro-ddi-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TRENDMICRO_DDI

Date | Changes  
---|---  
2026-01-21 |  Enhancement:  
\- A grok pattern was added to extract the domain name from the `reason` field when it contains `Domain`. The extracted value is mapped to `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.network.dns.questions.name: Newly mapped `reason` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `deviceMacAddress` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.security_result.confidence_score: Newly mapped `deviceRiskConfidenceLevel` raw log field with `event.idm.read_only_udm.security_result.confidence_score` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `ruleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `hostSeverity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field. The UDM field is set based on the value of the raw log field (0-3:LOW, 4-6:MEDIUM, 7-8:HIGH, 9-10:CRITICAL).  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `malType` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vLANId`, `cnt`, `evtCat`, `deviceGUID`, `ptype`, `cs9`, `cs10`, `pComp`, `cn4`, `cn5`, `cs8`, `fileType`, `appGroup`, `compressedFileHash` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- The value of the app field is updated to DNS when the original value is DNS Response.   
2025-12-01 |  Enhancement:  
\- Implemented preprocessing for the `deviceTranslatedAddress` raw log field to validate it as an IP address. Non-IP values will be cleared to prevent mapping malformed data.   
2025-05-19 |  Enhancement:  
\- Added a GROK pattern for field `rt`.  
\- Updated rename to replace directive to map the value of dtz into timezone.   
2025-04-08 |  Enhancement:  
\- event.idm.readonly_udm.metadata.event_timestamp: Newly mapped `rt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-01-09 |  Enhancement:  
\- Added a null check for `dvcmac` to parse unparsed logs.   
2024-11-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
