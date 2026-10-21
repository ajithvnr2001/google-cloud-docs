---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oort-changelog/
title: Change log for OORT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:51:14.825571+00:00
---

# Change log for OORT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oort-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OORT

Date | Changes  
---|---  
2026-03-09 |  Enhancement:  
\- Updated `event.idm.read_only_udm.metadata.vendor_name` to `Cisco`.  
\- Updated `event.idm.read_only_udm.metadata.product_name` to `Identity Intelligence`.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `detail.published` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `detail.login` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `detail.userTrustLevel` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `detail.login` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `detail.checkTopics` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `region` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `detail.checkId`, `detail.checkScope`, `detail.frameworks`, `detail.explainabilityEventIds`, and `data.value` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a grok pattern on `data.value` to extract `ip_addr`.  
\- `event.idm.read_only_udm.principal.ip`: If `data.key` is `ips`, updated the value of `event.idm.read_only_udm.principal.ip` to IP extracted from `data.value`.   
2025-01-23 |  \- Mapped the `security_result.severity` to `MEDIUM` when the log's severity is `Moderate`.   
2024-12-11 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
