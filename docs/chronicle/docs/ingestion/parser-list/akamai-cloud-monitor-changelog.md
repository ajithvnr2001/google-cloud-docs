---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-cloud-monitor-changelog/
title: Change log for AKAMAI_CLOUD_MONITOR \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:17:29.763304+00:00
---

# Change log for AKAMAI_CLOUD_MONITOR  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/akamai-cloud-monitor-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AKAMAI_CLOUD_MONITOR

Date | Changes  
---|---  
2026-01-16 |  Enhancement:  
\- `event.idm.read_only_udm.principal.network.asn`: Newly mapped `asn` raw log field(s) with `event.idm.read_only_udm.principal.network.asn` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytes` raw log field(s) with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `rspContentType` raw log field(s) with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `cipher` raw log field(s) with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `state` raw log field(s) with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `turnAroundTimeMSec` raw log field(s) with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `securityRules` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- Added a `has_principal` flag wherever `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.hostname` is being mapped.  
\- Added a `has_target` flag wherever `event.idm.read_only_udm.target.hostname` is being mapped.  
\- Added conditional check before mapping `NETWORK_HTTP` event type to prevent future errors and removed hardcoded event.idm.read_only_udm.metadata.event_type to `NETWORK_HTTP`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true` and `has_target` is `true`, updated to `NETWORK_HTTP`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_principal` is `true`, updated to `STATUS_UPDATE`.  
\- `event.idm.read_only_udm.metadata.event_type`: Otherwise, updated to `GENERIC_EVENT`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `accLang`, `cacheStatus`, `cookie`, `bparentIp`, `contactid`, `akNetwork`, `appv`, `akref`, `rcpid`, `akrefError`, `dnsLookupTimeMSec`, `edgeAttempts`, `maxAgeSec`, `overheadBytes`, `range`, `reqEndTimeMSec`, `rspContentLen`, `streamId`, `tlsOverheadTimeMSec`, `transferTimeMSec`, `uncompressedSize` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `objSize` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `edgeIP` raw log field(s) with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.location.country_or_region`: Newly mapped `serverCountry` raw log field(s) with `event.idm.read_only_udm.intermediary.location.country_or_region` UDM field.  
\- Added grok filter wherever IP address is being mapped to check valid IP address format in order to prevent errors.  
\- Added on_error wherever it is required.  
\- Used gsub on `securityRules` raw log field(s) to remove `||`.  
\- Used gsub on `customField` raw log field(s) to remove `%7`.   
2023-09-16 |  Bug-Fix:  
\- Added a condition check to avoid mapping negative value to `network.received_bytes`, `network.sent_bytes` and `network.http.response_code`.   
2022-09-30 |  Enhancement  
\- Added conditional null check for the fields `reqTimeSec`,`reqId`,`totalBytes`,`proto`,`protocol`,`referer`,`UA`,`xForwardedFor`,`cliIP`,`reqMethod`,`reqPort`,`reqPath`,`queryStr`,`errorCode`,`statusCode`.  
\- Mapped the field `type` to `metadata.product_event_type`.  
\- Mapped the field `version` to `metadata.product_version`.  
\- Mapped the field `id` to `metadata.product_log_id`.  
\- Mapped the field `cp` to `additional.fields`.  
\- Mapped the field `message.proto` to `network.application_protocol`.  
\- Mapped the field `message.status` to `network.http.response_code`.  
\- Mapped the field `message.cliIP` to `principal.ip`.  
\- Mapped the field `message.reqPort` to `target.port`.  
\- Mapped the field `message.reqHost` to `target.hostname`.  
\- Mapped the field `message.reqMethod` to `network.http.method`.  
\- Mapped the field `message.reqPath` to `target.url`.  
\- Mapped the field `message.reqLen` to `network.sent_bytes`.  
\- Mapped the field `message.respLen` to `network.received_bytes`.  
\- Mapped the field `message.sslVer` to `network.tls.version`.  
\- Mapped the field `message.UA` to `network.http.user_agent`.  
\- Mapped the field `message.fwdHost` to `principal.hostname`.  
\- Mapped the field `geo.country` to `principal.location.country_or_region`.  
\- Mapped the field `geo.region` to `principal.location.state`.  
\- Mapped the field `geo.city` to `principal.location.city`.  
\- Mapped the field `geo.lat` to `principal.location.region_latitude`.  
\- Mapped the field `geo.long` to `principal.location.region_longitude`.  
\- Mapped the field `network.edgeIP` to `intermediary.ip`.  
\- Mapped the field `network.network` to `additional.fields`.  
\- Mapped the field `network.networkType` to `additional.fields`.  
\- Mapped the field `network.asnum` to `additional.fields`.   
2022-07-25 |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
