---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-siem-connector-changelog/
title: Change log for AKAMAI_SIEM_CONNECTOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:55.171428+00:00
---

# Change log for AKAMAI_SIEM_CONNECTOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-siem-connector-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_SIEM_CONNECTOR

Date | Changes  
---|---  
2026-07-17 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attackData.ruleTags` from `event.idm.read_only_udm.additional.fields` UDM field since this field contains security-related information.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `attackData.ruleTags` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field with key `AttackData_RuleTags`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attackData.rules` from `event.idm.read_only_udm.additional.fields` since this field contains security-related information.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Mapped `attackData.rules` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field with key `AttackData`.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attackData.ruleMessages` from `event.idm.read_only_udm.additional.fields` as the data is more suitable for the UDM rule name field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Mapped `attackData.ruleMessages` raw log field to `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `attackData.ruleActions` from `event.idm.read_only_udm.additional.fields` to map it to more specific security result fields.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `attackData.ruleActions` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `attackData.ruleActions` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `last_successful_run` and `Offset` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `last_to_ts` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2025-10-24 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `attackData.apiId` raw log field to `event.idm.read_only_udm.security_result.detection_fields` with key `API_ID`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `attackData.ruleVersions`, `attackData.ruleTags`, `attackData.ruleSelectors`, `attackData.rules`, `attackData.ruleMessages`, `attackData.ruleActions`, `attackData.ruleData`, `botData.botScore`, `botData.responseSegment`, `identity.tlsFingerprintV2`, `identity.tlsFingerprintV3`, `clientData.telemetryType`, `httpMessage.requestHeaders`, `httpMessage.responseHeaders`, and `httpMessage.query` raw log fields to `event.idm.read_only_udm.additional.fields` raw log field.   
2025-02-27 |  Enhancement:  
\- Added base64 decoding for `attackData.ruleTags`, `attackData.ruleSelectors`, `attackData.rules`, `attackData.ruleMessages`, `attackData.ruleActions`, and `attackData.ruleData`.   
2024-06-07 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
