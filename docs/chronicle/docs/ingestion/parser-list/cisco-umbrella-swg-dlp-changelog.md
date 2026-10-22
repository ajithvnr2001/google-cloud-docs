---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-swg-dlp-changelog/
title: Change log for CISCO_UMBRELLA_SWG_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:43.921019+00:00
---

# Change log for CISCO_UMBRELLA_SWG_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-umbrella-swg-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_UMBRELLA_SWG_DLP

Date | Changes  
---|---  
2025-10-07 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `column4` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column5` raw log field with `event.idm.read_only_udm.additional.fields` UDM field, with the key `policy_group`.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `column10` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `column13` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `column15` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.security_result.rule_set: Newly mapped `column20` raw log field with `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `column22` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `column24` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- Added gsub function on `message` field to parse log :  
\- Removed `>`  
\- Removed `<`  
\- Replaced `` `Confidential`` with ``Confidential'`  
2025-07-08 |  Enhancement:  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `column10` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `column11` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.process.file.sha256`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.target.process.file.sha256` UDM field.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `column19` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- If `column19` is `OUTBOUND`, then `event.idm.read_only_udm.network.direction` is mapped to `OUTBOUND`.  
\- If `column19` is `INBOUND`, then `event.idm.read_only_udm.network.direction` is mapped to `INBOUND`.   
2025-02-27 |  Enhancement:  
\- Added support to parse unparsed logs.  
\- Mapped `column2` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `column3` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `column4` to `target.ip` and `target.asset.ip`.  
\- Mapped `column5` to `intermediary.ip`.  
\- Mapped `column6` to `principal.file.mime_type`.  
\- Mapped `column8` to `target.url`.  
\- Mapped `column9` to `network.http.referral_url`.  
\- Mapped `column10` to `network.http.user_agent`.  
\- Mapped `column11` to `network.http.response_code`.  
\- Mapped `column15` to `security_result.about.file.sha256`.  
\- Mapped `column16` to `metadata.product_event_type`.  
\- Mapped `column22` to `security_result.summary`.  
\- Mapped `column26` to `network.http.method`.  
\- Mapped `column29` to `additional.fields`.  
\- Mapped `column41` to `principal.asset.asset_id`.  
\- Mapped `column44` to `principal.user.userid`.  
\- Mapped `column49` to `metadata.product_log_id`.   
2024-12-06 |  Enhancement:  
\- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
