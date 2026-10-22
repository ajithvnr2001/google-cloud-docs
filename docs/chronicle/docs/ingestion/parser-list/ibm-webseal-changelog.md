---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-webseal-changelog/
title: Change log for IBM_WEBSEAL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:01.956234+00:00
---

# Change log for IBM_WEBSEAL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-webseal-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_WEBSEAL

Date | Changes  
---|---  
2025-10-08 |  Enhancement:  
\- Removed the default assignment of `0.0.0.0` to `event.idm.read_only_udm.target.ip` when the `target_ip` raw field is empty. This change is made so that GCP can correctly enrich the destination instance.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http_version`, `http_uri`, `caca`, `@version` and `logtype` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Modified grok patterns to extract `http_method`, `http_uri`, and `http_version` from the `URI` raw log field.  
\- Refined parsing for `code_resp`, `response_code`, and `res_code` to only process values that match a standard HTTP response code format (`^[1-5][0-9]{2}$`).  
\- Updated `metadata.event_type` from `NETWORK_CONNECTION` to `STATUS_UPDATE` for certain log entries.  
\- Modified the condition for mapping `network.tls.version` to not allow empty spaces in `temp_data`.   
2025-03-03 |  Enhancement:  
\- Mapped `src_host` to `principal.hostname`  
\- Mapped `src_app` to `principal.application`  
\- Mapped `network_method` to `network.http.method`  
\- Mapped `dst_url` to `target.url`  
\- Mapped `app_protocol` to `additional.fields`  
\- Mapped `res_code` to `network.http.response_code`  
\- Mapped `sent_bytes` to `network.sent_bytes`  
\- Mapped `rec_bytes` to `network.received_bytes`  
\- Mapped `app_proto` to `network.application_protocol`  
\- Mapped `src_port` to `principal.port`  
\- Mapped `dst_host` to `target.hostname`  
\- Mapped `level` to `security_result.severity`  
\- Mapped `error` to `target.resource.attribute.labels`  
\- Mapped `description` to `security_result.description`  
\- Mapped `operation` to `target.user.attribute.labels`  
\- Mapped `username` to `target.user.userid`  
\- Mapped `authSourceCode` to `additional.fields`  
\- Mapped `accountValid` to `additional.fields`  
\- Mapped `passwordValid` to `additional.fields`  
\- Mapped `hashedPassword` to `additional.fields`  
\- Mapped `registryDn` to `target.user.attribute.labels`  
\- Mapped `secUserDn` to `target.resource.attribute.labels`  
\- Mapped `passwordResetAllowed` to `additional.fields`  
\- Mapped `nonExpiringPassword` to `additional.fields`  
\- Mapped `customPasswordPolicy` to `additional.fields`  
\- Mapped `authSource` to `additional.fields`.   
2024-01-22 |  Enhancement: Added Grok patterns to support new format of logs.   
2023-11-17 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
