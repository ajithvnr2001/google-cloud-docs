---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-waf-changelog/
title: Change log for AWS_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:18:04.130306+00:00
---

# Change log for AWS_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aws-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AWS_WAF

Date | Changes  
---|---  
2026-08-12 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `http_request.url.hostname`, `Http_request.Url.Hostname` raw log fields from `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields as the fields correspond to target machine details.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Mapped `http_request.url.hostname`, `Http_request.Url.Hostname` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `http_request.url.hostname`, `Http_request.Url.Hostname` raw log fields from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields as the fields correspond to target machine details and already mapped to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Metadata.Profiles.Array` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If log has valid principal and target machine details and `class_name` is HTTP Activity, updated the value of `event.idm.read_only_udm.metadata.event_type` to NETWORK_HTTP.   
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.resource.name`: Removed mapping of `webaclId` from `event.idm.read_only_udm.intermediary.resource.name` UDM field to map it with more appropriate UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Mapped `webaclId` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `requestBodySize` from `event.idm.read_only_udm.additional.fields` UDM field to map it with more appropriate UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Mapped `requestBodySize` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly Mapped `http_request.scheme`, `http_request.url.host`, `http_request.uri`, `http_request.args` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- Added a grok pattern on `header.value` to extract `hostname`, `port`.  
\- Modified mapping for `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped from `hostname` extracted via grok from `header.value` if port is present, otherwise mapped from `header.value`.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `port` raw log field with `event.idm.read_only_udm.target.port` UDM field.   
2026-03-30 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: Removed mapping of `ruleGroupList.nonTerminatingMatchingRules.ruleId` from `event.idm.read_only_udm.security_result.rule_id` UDM field in order to more accurately represent the `ruleId` in the security result.  
\- `event.idm.read_only_udm.security_result.action_details`: Removed mapping of `ruleGroupList.nonTerminatingMatchingRules.action` from `event.idm.read_only_udm.security_result.action_details` UDM field in order to more accurately represent the `action` in the security result.  
\- `event.idm.read_only_udm.security_result.action`: Removed mapping of `ruleGroupList.nonTerminatingMatchingRules.overriddenAction` from `event.idm.read_only_udm.security_result.action` UDM field in order to more accurately represent the `overriddenAction` in the security result.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ruleGroupList.nonTerminatingMatchingRules.action`, `ruleGroupList.nonTerminatingMatchingRules.overriddenAction`, and `ruleGroupList.nonTerminatingMatchingRules.ruleId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `httpRequest.uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2026-01-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `labels.name` from list_value/array format because arrays under a single key prevent direct UDM search of individual values.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `labels.name` raw log field with single string value, with the key containing the index to make each label name independently searchable via its unique indexed key.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ruleGroup.terminatingRule.ruleId`,`ruleGroup.terminatingRule.action`,`nonTerminatingMatchingRule.ruleMatchDetails.conditionType`,`nonTerminatingMatchingRule.ruleMatchDetails.location` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-01-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `formatVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `httpRequest.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `httpRequest.httpVersion` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `httpRequest.scheme` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rateBasedRuleList`, `requestBodySize`, and `requestBodySizeInspectedByWAF` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result`: Refactored mapping for `ruleGroupList.nonTerminatingMatchingRules` to create a distinct `security_result` entry for each rule. `ruleId` is mapped to `security_result.rule_id`, `action` to `security_result.action_details`, and `overriddenAction` to `security_result.action`. This prevents values from being overwritten when multiple rules are present.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ruleGroupList.customerConfig` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-08-12 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Newly mapped `matchingrules.overriddenAction` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `matchingrules.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field when `action` is `ALLOW` or `BLOCK`.  
\- event.idm.read_only_udm.network.tls.client.ja3: Newly mapped `ja3Fingerprint` raw log field with `event.idm.read_only_udm.network.tls.client.ja3` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ja4Fingerprint` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `labels` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-04-25 |  Enhancement:  
\- event.idm.read_only_udm.target.hostname: Newly mapped `http_request.url.hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `http_request.url.hostname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `Http_request.Url.Hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `Http_request.Url.Hostname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.   
2025-02-17 |  Enhancement:  
\- Added support for OCSF JSON format logs.   
2024-03-14 |  Enhancement:  
\- Added gsub function to handle invalid escape characters `\` in the source logs to valid JSON format.   
2023-12-29 |  Enhancement:  
\- Mapped `user-agent` and `User-Agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.  
\- Mapped the base64 decoded value of `authorization` header from `httpRequest.header` to `target.user.userid`.   
2023-12-08 |  Bug-Fix:  
\- Modified the condition before mapping `header.value` to `target.hostname`.  
\- Modified the mapping of `target.url` from `http://%{header.value}%{httpRequest.uri}` to `httpRequest.uri`.  
\- If `terminatingRuleType` is `MANAGED_RULE_GROUP`, then added a condition for mapping `ruleGroupList.terminatingRule`.  
\- Added `on_error` for mutate blocks wherever required".   
2023-09-11 |  Enhancement:  
\- Added a Grok pattern to support a new log format.   
2023-08-16 |  Enhancement:  
\- Mapped `ruleGroup.terminatingRule.action` to `security_result.detection_fields` when `terminatingRuleType` is `REGULAR`.   
2022-12-16 |  Enhancement:  
\- Combined two date filters into one and updated condition for date filter to if `timestamp` is not null.  
\- Dropped logs when `json_failure` is true.  
\- Mapped `httpRequest.headers.value` to `event.idm.read_only_udm.network.http.parsed_user_agent` when `httpRequest.headers.name` is `user-agent`.   
2022-08-11 |  Enhancement:- Removed the logic to handle CSV and SYSLOG message logs.   
2022-07-22 |  Newly Created Parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
