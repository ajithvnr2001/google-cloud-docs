---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-datastream-2-changelog/
title: Change log for AKAMAI_DATASTREAM_2 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:19.202142+00:00
---

# Change log for AKAMAI_DATASTREAM_2  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-datastream-2-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_DATASTREAM_2

Date | Changes  
---|---  
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `reqTimeSec` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `arlid`, `cacheable`, `deliveryPolicyId`, `deliveryPolicyReqStatus`, `downloadTime` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `edgeAttempts`, `edgeIPBinding`, `lastByte`, `maxAgeSec`, `prefetchMidgressHits`, `reqEndTimeMSec`, `startupError`, `streamId`, `throughput`, `timeToFirstByte`, `tlsOverheadTimeMSec` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `edgeIP` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `serverCountry` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `state` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.target.process.file.size`: Newly mapped `uncompressedSize` raw log field with `event.idm.read_only_udm.target.process.file.size` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.   
2025-04-10 |  `event.idm.read_only_udm.metadata.event_type`: Removed mapping of `NETWORK_CONNECTION` from `event.idm.read_only_udm.metadata.event_type` UDM field and mapped `NETWORK_HTTP` instead when `has_principal` is true, `has_target` is true and `has_network` is `true`.   
2025-02-27 |  \- Mapped `reqhost` and `reqHost` to `target.hostname` and `target.asset.hostname`.  
\- Mapped `securityRules` to `jsonPayload.securityrules`.  
\- Mapped `country` to `principal.location.country_or_region`.  
\- Mapped `fileSizeBucket` to `additional.fields`.  
\- Mapped `errorCode` to `additional.fields`.   
2025-02-17 |  \- Mapped `totalBytes` to `principal.network.received_bytes`.  
\- Mapped `uncompressedsize` to `target.process.file.size`.  
\- Mapped `turnAroundTimeMSec`, `billingRegion`, `overheadBytes`, and `objSize` to `additional.fields`.  
\- Mapped `asn` to `security_result.detection_fields`.  
\- Mapped `cliIP` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `reqPort` to `target.port`.  
\- Mapped `reqId` to `network.session_id`.   
2025-02-07 |  Newly created parser for AKAMAI_DATASTREAM_2.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
