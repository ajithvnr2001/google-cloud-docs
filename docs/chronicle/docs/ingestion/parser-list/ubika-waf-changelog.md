---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubika-waf-changelog/
title: Change log for UBIKA_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:41:17.697001+00:00
---

# Change log for UBIKA_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ubika-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UBIKA_WAF

Date | Changes  
---|---  
2026-03-09 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `headers.value` with `key` as `X-Forwarded-Host` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `request.portDst` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `httpVersion` (extracted from `request.protocol`), `tokens.date` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `context.tags`, `events.tokens.ipReputationThreats`, `events.tokens.ipReputationScore` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `context.geoipName` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `context.geoipCode` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Added processing for `X-Forwarded-For-Ori` and `X-Forwarded-For` `header.key` raw log fields to populate `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `events.tokens.severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped the concatenation of `X-Forwarded-Proto`, `request.hostname`, `request.path` and `request.query` raw log fields to `event.idm.read_only_udm.target.url` UDM field.   
2026-02-05 |  Enhancement:  
\- Added a grok pattern to parse new format of raw logs.  
\- Modified the grok pattern to parse the raw log.  
\- Added grok patterns on `tokens.reasons` to extract `response_code`,`tar_hostname`,`location` and `prin_ip` fields.  
\- `event.idm.read_only_udm.intermediary.process.pid`: Newly mapped `inter_pid` field(s) with `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `status_description` field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `tokens.ipReputationIp` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `tokens.ipReputationIp` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `response_code` field(s) with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `tar_hostname` field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `location` field(s) with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `prin_ip` field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `prin_ip` field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `tokens.matchingParts`,`request.body`,`unique_id1`, `thread_id`, `tokens.ipReputationScore`, `tokens.eaTotalScore`, `tokens.eaPolicyUid`, `tokens.eaPolicyName`, `tokens.eaStaticPolicyUid`, `tokens.eaRuleId`, `tokens.eaNewRulesWarningMode`, `internal_timestamp`, `tokens.securityExceptionConfigurationUid` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `tokens.icxPolicyName`, `tokens.icxPolicyUid`, `tokens.icxRuleName`, `tokens.icxRuleUid`, `tokens.ipReputationThreats` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `message_component` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- All the IP address fields tar_ip, src_ip, request.ipDst, request.ipSrc, tokens.ipReputationIp, prin_ip, tempData.request.ipSrc, tempData.request.ipDst are now validated using grok %{IP:*} pattern before mapping.  
\- The logic for handling JSON parsing from json_data has been updated. If the first attempt fails, it now attempts to replace \\\\\` with \` before retrying the JSON parsing.   
2025-11-02 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http_host_header` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `eventData.eventUid`, `eventData.tokens.severity`, `eventData.tokens.date`, `eventData.tokens.eventType`, `eventData.tokens.attackFamily`, `eventData.tokens.reason`, `eventData.tokens.customMessage` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Changed mapping for `event.idm.read_only_udm.metadata.product_event_type` from `tokens.eventType` to `eventData.tokens.eventType`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` to `event.idm.read_only_udm.intermediary.hostname`.  
\- Added grok pattern to parse new pattern of SYSLOG logs.   
2025-10-03 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `src_host` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `src_app` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `tar_ip`, `target_ip` from `tokens.reason` raw log field(s) to `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `tar_ip`, `target_ip` from `tokens.reason` raw log field(s) to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `request.query` ,`header.value`, `eventData.tokens.icxPolicyName`, `eventData.tokens.icxPolicyUid`, `eventData.tokens.icxRuleName`, `eventData.tokens.icxRuleUid`, `eventData.tokens.securityExceptionConfigurationUids`, `matchingPart.part`, `matchingPart.partKey`, `matchingPart.partKeyOperator`, `matchingPart.partKeyPattern`, `matchingPart.partKeyMatch`, `matchingPart.partValue`, `matchingPart.partValueOperator`, `matchingPart.partValuePatternUid`, `matchingPart.partValuePatternName`, `matchingPart.partValuePatternVersion`, `matchingPart.partValueMatch`, `matchingPart.attackFamily`, `matchingPart.riskLevel`, `matchingPart.riskLevelOWASP`, `matchingPart.cwe` to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added groks to parse new pattern of SYSLOG logs.  
\- Set the event_type to `NETWORK_CONNECTION` when both `has_principal` and `has_target` are `true`.  
\- Corrected typos in internal field names (e.g., `eventt.tokens.riskLevel` to `tokens.riskLevel`).   
2024-08-23 |  Enhancement:  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.   
2024-07-23 |  Enhancement:  
\- Added `eventIndex` to resolve the flakiness in the parser.  
\- Added a new Grok pattern to parse a new format of SYSLOG logs.   
2024-06-13 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
