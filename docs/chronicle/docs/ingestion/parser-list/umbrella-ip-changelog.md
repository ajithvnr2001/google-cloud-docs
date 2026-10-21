---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-ip-changelog/
title: Change log for UMBRELLA_IP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:34:58.548069+00:00
---

# Change log for UMBRELLA_IP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/umbrella-ip-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UMBRELLA_IP

Date | Changes  
---|---  
2025-10-07 |  Enhancement:  
\- Modified the conditional check for mapping `column15` to parse correctly for `event.idm.read_only_udm.security_result.about.file.sha256` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `column3` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column4`, `column5` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `column11` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column15` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `column22` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column13` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added conditional checks involving `pattern_unmatched` and `pattern_not_matched` data fields before the final merge of the `security_result` variable into `event.idm.read_only_udm.security_result` UDM field.  
\- Refactored parser logic to handle cases where `column3`, `column4`, and `column5` do not contain IP addresses by mapping them to alternative UDM fields.  
\- Refactored parser logic to extract and map an IP address from `column13` to principal IP fields.  
\- Refactored parser logic to extract and map an IP address from `column15` to target IP fields when it does not represent a SHA256 hash.   
2025-08-07 |  Enhancement:  
\- Remove uneccesssary initialization of variables to correctly populate the fields.   
2025-02-27 |  Enhancement:  
\- Added support to parse unparsed csv logs.   
2022-08-22 |  Enhancement:  
\- Mapped the field `action` to `security_result.action` and `security_result.action_details`.  
\- Added grok for the field `query_type` and mapped it to `network.dns.questions.type`.  
\- Mapped the field `domain` to `network.dns.questions.name`.  
\- Mapped `DNS` to `network.application_protocol`.  
\- Mapped the field `response_code` to `network.dns.response_code`.  
\- Mapped `security_result.category` to `NETWORK_MALICIOUS` where the field `categories` contains `Malware` and `NETWORK_SUSPICIOUS` where `categories` contains `Potentially Harmful`.  
\- Mapped the field `categories` to `security_result.category_details`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
