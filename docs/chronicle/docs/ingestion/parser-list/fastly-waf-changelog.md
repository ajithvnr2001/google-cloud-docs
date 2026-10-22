---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-waf-changelog/
title: Change log for FASTLY_WAF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:44.184562+00:00
---

# Change log for FASTLY_WAF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fastly-waf-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FASTLY_WAF

Date | Changes  
---|---  
2025-05-08 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Content-Length`, `Accept-Language`, `CDN-Loop`, `Cloud-WAF-Key`, `Fastly-Client`, `Keep-Alive`, `Content-Type`, `Fastly-Orig-Accept-Encoding`, `Fastly-SSL`, `Via`, `X-Cloud-Trace-Context`, `X-Forwarded-Server`, `fastly_csi_request_id`, `x-sigsci-traceid`, `payload.exampleRequest.responseMillis`, `X_Varnish`, `X_Timer`, `type`, `payload.id`, `payload.exampleRequest.id`, `payload.type`, `Connection` and `created` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `Host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `Host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `User_Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `link` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `x-sigsci-tlscipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `x-sigsci-tlsprotocol` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `payload.exampleRequest.serverHostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `payload.exampleRequest.serverHostname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `payload.exampleRequest.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Newly mapped `payload.exampleRequest.path` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `payload.exampleRequest.responseCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `proto_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `x-request-id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `payload.exampleRequest.responseSize` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `X_Forwarded_For` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `X_Forwarded_For` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `payload.source` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `payload.source` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `payload.exampleRequest.remoteIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `payload.exampleRequest.remoteIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `payload.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly mapped `payload.remoteCountryCode` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `payload.exampleRequest.tags.detector`, `payload.exampleRequest.tags.link`, `payload.exampleRequest.tags.location`, `payload.exampleRequest.tags.readaction`, `payload.exampleRequest.tags.type`, and `payload.exampleRequest.tags.value` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `payload.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `RL-orig-url` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2022-06-06 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
