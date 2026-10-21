---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-cef-changelog/
title: Change log for IMPERVA_CEF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:10:03.733478+00:00
---

# Change log for IMPERVA_CEF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-cef-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_CEF

Date | Changes  
---|---  
2026-08-05 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `kv.qstr` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `kv.in` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `kv.cn1` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `kv.sip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `kv.xff` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields when `kv.src` and `kv.xff` do not contain same value.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `kv.xff` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field when `kv.src` and `kv.xff` contain same value.   
2026-06-17 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `target_host` log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields for all events.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2026-05-21 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `kv.act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- Added a grok pattern on `kv.request` to extract `target_host`.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `target_host` log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field if log event is `Illegal Resource Access`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `kv.sourceServiceName` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.   
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `organization` log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `log_type` log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `cicode` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `ccode` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.organization_name`: Newly mapped `Customer` raw log field with `event.idm.read_only_udm.network.organization_name` UDM field.  
\- `event.idm.read_only_udm.network.tls.version`: Newly mapped `tls_version` log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- `event.idm.read_only_udm.network.tls.cipher`: Newly mapped `tls_cipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `cpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `fileId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `dproc` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.threat_id`: Newly mapped `severity` log field with `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `deviceFacility`, `deviceExternalId` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `end` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- Added a grok pattern on `ver` to extract `tls_version`, `tls_cipher`.   
2024-09-12 |  Enhancement:  
\- Added support for new log patterns.   
2023-03-07 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
