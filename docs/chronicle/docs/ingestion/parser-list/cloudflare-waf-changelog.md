---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-waf-changelog/
title: Change log for CLOUDFLARE_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:55.895027+00:00
---

# Change log for CLOUDFLARE_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDFLARE_WAF

Date | Changes  
---|---  
2026-01-27 |  Enhancement:  
\- Added support to parse only valid values of `ClientRequestProtocol` raw log field to `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `EdgeResponseBytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `ClientRequestBytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ClientRegionCode`, `WorkerSubrequest` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-03 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `OriginResponseDurationMs`, `SecuritySources`, `WAFFlags`, `WAFMatchedVar`, `BotScoreSrc`, `WAFRCEAttackScore`, `ClientDeviceType`, `ClientRequestScheme`, `WAFSQLiAttackScore`, `WAFXSSAttackScore`, `FraudAttack`, `LeakedCredentialCheckResult`, `ClientIPClass`, `CacheCacheStatus` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `BotDetectionIDs` raw log field to `event.idm.read_only_udm.security_result.rule_id`.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `BotDetectionTags`, `BotTags` raw log fields to `event.idm.read_only_udm.security_result.category_details`.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `ClientSSLCipher` raw log field to `event.idm.read_only_udm.network.tls.cipher`.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `ClientSSLProtocol` raw log field to `event.idm.read_only_udm.network.tls.version`.  
\- event.idm.read_only_udm.principal.port: Newly mapped `ClientSrcPort` raw log field to `event.idm.read_only_udm.principal.port`.  
\- event.idm.read_only_udm.security_result.confidence_score: Newly mapped `WAFAttackScore` raw log field to `event.idm.read_only_udm.security_result.confidence_score`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `OriginIP` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `ZoneName` raw log field to `event.idm.read_only_udm.target.administrative_domain`.   
2025-08-21 |  Enhancement:  
\- event.idm.read_only_udm.network.http.response_code: Removed mapping of `EdgeResponseStatus` with `event.idm.read_only_udm.network.http.response_code` UDM field in order to introduce a more accurate mapping for the raw log field..  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `OriginResponseStatus` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.principal.location.city: Newly mapped `ClientCity` raw log field to event.idm.read_only_udm.principal.location.city UDM field.  
\- event.idm.read_only_udm.network.tls.client.ja3: Newly mapped `JA3Hash` raw log field to event.idm.read_only_udm.network.tls.client.ja3 UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EdgeResponseStatus`, `BotScore`, `JA4`, `ClientRequestReferer`, `RequestHeaders.x-client-id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action: Setting `event.idm.read_only_udm.security_result.action` to `BLOCK` when `SecurityAction` raw log field is `BLOCK` else if `SecurityAction` raw log field is `ALLOW` then `event.idm.read_only_udm.security_result.action` is set to `ALLOW`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `EdgeStartTimestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-01-31 |  Enhancement:  
\- Mapped `SecurityRuleID` to `security_result.threat_id`.  
\- Mapped `SecurityRuleDescription` to `security_result.threat_name`.  
\- Mapped `SecurityRuleDescription` to `security_result.action_details`.   
2024-08-08 |  Enhancement:  
\- Extracted data from `ClientRequestHost` and `ClientRequestURI`, merged it and mapped the result to `target.url`.   
2023-08-30 |  \- Initialized field `ClientRequestPath`.   
2023-02-02 |  \- Validated the `security_result` value before its getting merged to event.   
2022-09-16 |  \- Mapped the field `Action` to `security_result.action_details`.  
\- Mapped `security_result.action` to `ALLOW_WITH_MODIFICATION` when action contains `challengeSolved`, `jschallengeSolved`, `managedchallengenoninteractivesolved`, `managedchallengeinteractivesolved`.  
\- Mapped `security_result.action` to `BLOCK` when action contains `drop`, `block`, `connectionclose`.  
\- Mapped `security_result.action` to `FAIL` when action contains `challengefailed`, `jschallengefailed`.   
2022-07-25 |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
