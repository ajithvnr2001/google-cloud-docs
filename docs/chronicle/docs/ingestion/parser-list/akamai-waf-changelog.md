---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-waf-changelog/
title: Change log for AKAMAI_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:28:27.045757+00:00
---

# Change log for AKAMAI_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_WAF

Date | Changes  
---|---  
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Conditionally mapped `attackData.appliedAction` to `event.idm.read_only_udm.security_result.action`: If `attackData.appliedAction` is `deny`, updated to `BLOCK`. If `attackData.appliedAction` is `allow`, updated to `ALLOW`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `format`, `identity.tlsFingerprintV2`, `identity.tlsFingerprintV3` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.url`: Changed mapping for `event.idm.read_only_udm.target.url` from `httpMessage.path` to a conditional combination of `httpMessage.host` and `httpMessage.path`.  
\- Added the gsub to remove the \r\n and \n characters from the message field.  
\- Added the gsub for the message field. This fixed parsing issue for logs having the \r\n and \n, allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.threat_name`  
\- `event.idm.read_only_udm.security_result.rule_id`  
\- `event.idm.read_only_udm.security_result.detection_fields`  
\- `event.idm.read_only_udm.metadata.event_timestamp`  
\- `event.idm.read_only_udm.security_result.action_details`  
2025-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.labels`: Newly mapped `attackData.clientReputation` raw log field to `event.idm.read_only_udm.principal.labels`.  
\- Added json filter for `message_copy` field.  
\- Modified grok patterns to support an additional format for `httpMessage.requestHeaders`.  
\- Modified grok patterns to support an additional format for `httpMessage.responseHeaders`.  
\- `event.idm.read_only_udm.security_result.about.labels`: Newly mapped `location` raw log field to `event.idm.read_only_udm.security_result.about.labels`.   
2025-07-04 |  Enhancement:  
\- Added a Grok pattern for `fecthdata` and `message` fields.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `STREAMID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cp`, `Custom_Field`, `uncompressedSize`, `overheadBytes`, `totalBytes`, `queryStr`, `breadcrumbs`, `accLang`, `cookie`, `range`, `referer`, `xForwardedFor`, `maxAgeSec`, `reqEndTimeMSec`, `errorCode`, `turnAroundTimeMSec`, `transferTimeMSec`, `dnsLookupTimeMSec`, `lastByte`,`req_processing_time`, `TTFB`, `edgeIP`, `country`, `state`, `city`, `serverCountry`, `billingRegion`, `cacheStatus`, `securityRules`, `ewUsageInfo`, `ewExecutionInfo` and `customField` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `BYTES` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `CLIIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `STATUSCODE` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `PROTO` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `REQHOST` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `REQMETHOD` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `REQPATH` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `REPORT` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `RSPCONTENLEN` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `UA` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `tlsOverheadTimeMSec` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `objSize` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.hostname` and used common field `target_hostname` and mapped it to `event.idm.read_only_udm.target.hostname` UDM field.  
\- Removed redundant mapping of `event.idm.read_only_udm.target.url` and used common field `target_url` and mapped it to `event.idm.read_only_udm.target.url` UDM field.  
\- Consolidate the mapping of `event_type` to eliminate redundant code.   
2025-04-29 |  Enhancement:  
\- Added a for loop for field `ftechWithSub`.  
\- Added a Grok pattern for field `fecthdata`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `princip_ip` raw log field with event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `princip_host` raw log field with event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_Version` raw log field with event.idm.read_only_udm.network.tls.version UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `req_Path` raw log field with event.idm.read_only_udm.target.url UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `res_method` raw log field with event.idm.read_only_udm.network.http.method UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `rescode` raw log field with event.idm.read_only_udm.network.http.response_code UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `rsp_contenttype` raw log field with event.idm.read_only_udm.target.application UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `reqid` raw log field with event.idm.read_only_udm.network.session_id UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` raw log field with event.idm.read_only_udm.network.application_protocol UDM field for HTTPS.   
2025-01-06 |  Enhancement:  
-Mapped `httpMessage.status` to `network.http.response_code`.  
-Mapped `httpMessage.requestId to `network.session_id".  
-Mapped `attackData.ruleTags` to `security_result.rule_set`.  
-Mapped `httpMessage.method` to `network.http.method`.  
-Mapped `httpMessage.bytes` to `network.received_bytes`.  
-Mapped `httpMessage.port` to `target.port`.  
-Added a Grok pattern to parse `httpMessage.requestHeaders`.  
-Mapped `httpMessage.requestHeaders` to `security_result.detection_fields`.  
-Mapped `httpMessage.query` to `security_result.detection_fields`  
-Mapped `httpMessage.tls` to `network.tls.version`.  
-Mapped `version` to `metadata.product_version`.  
-Mapped `format` to `additional.fields`.  
-Mapped `httpMessage.protocol` to `network.application_protocol`.  
-Mapped `attackData.ruleMessages` to `security_result.description`.  
-Mapped `attackData.clientIP` to `principal.ip` and `principal.asset.ip`.  
-Mapped `httpMessage.path` to `target.url`.  
-Mapped `httpMessage.host` to `principal.hostname` and `principal.asset.hostname`.  
-Mapped `attackData.rules` to `security_result.rule_name`.  
-Mapped `attackData.ruleActions` to `security_result.action_details`.  
-Mapped `attackData.policyId` to `security_result.rule_id`.  
-Mapped `attackData.configId` to `additional.fields`.  
-Mapped `geo.country` to `principal.location.country_or_region`.  
-Mapped `geo.city` to `principal.location.city`.  
-Mapped `httpMessage.start` to `metadata.event_timestamp`.   
2024-12-27 |  Enhancement:  
\- Mapped `httpMessage.requestHeaders` and `httpMessage.responseHeaders` to `security_result.detection_fields`.  
\- Mapped `geo.regionCode` and `geo.continent` to `principal.resource.attribute.labels`.   
2024-09-10 |  Enhancement  
\- Mapped `attackData.ruleActions` to `security_result.action_details`.   
2024-05-21 |  Enhancement  
\- Mapped `rules.data` to `security_result.detection_fields`.  
\- Mapped `rules.action`, `rules.selector`, and `rules.version` to `security_result.action_details`.  
\- Mapped `rules.id` to `security_result.rule_id`,  
\- Mapped `rules.tag` to `security_result.category_details`.  
\- Mapped `rules.message` to `security_result.threat_name`.   
2024-03-01 |  Enhancement  
\- Mapped `attackData.configId` to `metadata.product_log_id` and `security_result.detection_fields`.   
2023-10-27 |  Enhancement  
\- Mapped `rule.id` to `security_result.rule_id`.  
\- When `httpMessage.host` is not present, changed value set in `metadata.event_type` from `NETWORK_HTTP` to `GENERIC_EVENT`.  
\- Added support to parse `attackData` when `attackData.rules` is an array.   
2023-04-24 |  Enhancement  
\- Parsed logs ingested in CEF format.   
2023-04-04 |  Enhancement  
\- Mapped `reqHost` to `target.hostname`.  
\- Mapped `reqPort` to `target.port`.  
\- Mapped `reqPath` to `target.url`.  
\- Mapped `reqId` to `network.session_id`.  
\- Mapped `statusCode` to `network.http.response_code`.  
\- Mapped `reqMethod` to `network.http.method`.  
\- Mapped `UA` to `network.http.user_agent`.  
\- Mapped `bytes` to `network.sent_bytes`.  
\- Mapped `reqMethod` to `network.http.method`.  
\- Parsed failing logs in syslog format.  
\- Added condition checks for `attackData.rules` for proper parsing.  
\- Modified `metadata.event_type` to `NETWORK_HTTP` from `STATUS_UPDATE` wherever possible.   
2022-11-07 |  Enhancement  
\- update SecurityRules to check [`-`] also in data.   
2022-08-12 |  Enhancement  
\- Mapped `security_policy_id` to security_result.rule_name.  
\- Mapped `non_deny_rules` to security_result.about.resource.attribute.labels.  
\- Mapped `deny_rule_format` to security_result.about.resource.attribute.labels.   
2022-06-14 |  Enhancement-  
Mapped proto to security_result.summary.  
Mapped securityRules to security_result.rule_name.  
Mapped city to principal.location.city.  
Mapped country to principal.location.country_or_region.  
Mapped cliIP to principal.ip.  
Mapped cp to event.idm.read_only_udm.additional.fields.  
Mapped reqId to metadata.product_log_id.  
Mapped rspContentType to target.file.mime_type.  
Mapped state to target.user.personal_address.state.  
Mapped version to principal.asset.software.version.   
2022-03-23 |  Bugfix-Fix for failed to parse data with all match patterns.  
Added mappings for new fields.  
eventId mapped to metadata.product_log_id.  
eventDefinitionId mapped to target.resource.product_object_id.  
eventDescription mapped to metadata.description.  
eventName mapped to metadata.product_event_type.  
eventTypeName mapped to additional.fields.  
eventTypeId mapped to additional.fields.  
eventData mapped to additional.fields.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
