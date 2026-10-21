---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-json-changelog/
title: Change log for BRO_JSON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:02:31.062381+00:00
---

# Change log for BRO_JSON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bro-json-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BRO_JSON

Date | Changes  
---|---  
2026-10-06 |  \- additional.fields[original_host]: Newly mapped `host` log field with `additional.fields[original_host]` UDM field when its length exceeds 255 characters.  
\- target.hostname: Truncated the `host` log field to 255 characters before mapping to `target.hostname` UDM field when it exceeds the supported limit.  
\- additional.fields[original_username]: Newly mapped `username` log field with `additional.fields[original_username]` UDM field when its length exceeds 255 characters.  
\- principal.user.userid: Truncated the `username` log field to 255 characters before mapping to `principal.user.userid` UDM field when it exceeds the supported limit.   
2026-10-01 |  \- Updated `zeek_log_type` handling to cover edge cases for `notice/notice_alarm`.  
\- additional.fields[original_query]: Newly mapped `query` log field with `additional.fields[original_query]` UDM field when its length exceeds 255 characters.  
\- network.dns.query.name: Truncated the `query` log field to 255 characters before mapping to `network.dns.query.name` UDM field when it exceeds the supported limit.   
2026-09-23 |  \- Updated the gsub regex in the BRO_JSON parser to only convert top-level JSON boolean values (true/false), preventing malformed JSON errors when boolean strings appear inside fields like uri.  
\- `network.dhcp.seconds`: Updated handling of negative duration raw log values to reset to 0 before converting to uinteger and mapping to `network.dhcp.seconds` to prevent uint64 underflow and uint32 type conversion errors on DHCP logs.   
2026-06-02 |  \- `principal.ip`: Updated the logic to map `id.orig_h` raw log field with `principal.ip` UDM field regardless of the value of `local_orig` raw log field value.  
\- `target.ip`: Updated the logic to map `id.resp_h` raw log field with `target.ip` UDM field regardless of the value of `local_orig` raw log field value.  
\- `principal.port`: Updated the logic to map `id.orig_p` raw log field with `principal.port` UDM field regardless of the value of `local_orig` raw log field value.  
\- `target.port`: Updated the logic to map `id.resp_p` raw log field with `target.port` UDM field regardless of the value of `local_orig` raw log field value.   
2026-03-26 |  \- `target.url`: Updated the logic to check whether the `host` and 'uri` raw log fields have same value, before concatenating them to set the `target.url` UDM field for http log type.   
2024-05-01 |  Updated the deprecated UDM fields.   
2024-01-31 |  Handled the extra spaces in the `regex` condition while setting the log types.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-10-04 |  Added mapping to `network.tls.certificate.md5`, `network.tls.certificate.sha1` and `network.tls.certificate.sha256`.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2022-09-28 |  Promoted BRO_JSON parser to default.  
For the field mapping differences, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/zeek-map-changes>field mapping changes](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
