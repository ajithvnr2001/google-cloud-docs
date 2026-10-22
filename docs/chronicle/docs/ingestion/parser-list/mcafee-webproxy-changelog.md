---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-webproxy-changelog/
title: Change log for MCAFEE_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:39.066520+00:00
---

# Change log for MCAFEE_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_WEBPROXY

Date | Changes  
---|---  
2026-04-23 |  Enhancement:  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `categories` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `url` field is present in log, event_type is updated to `NETWORK_HTTP`.   
2026-04-03 |  Enhancement:  
\- Modified a grok pattern to parse the raw logs with timestamp of ISO format.  
\- Added a Grok pattern to parse the raw log fields.   
2026-03-12 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: If `cn_1` is 1, 2, or 3, updated the value of `event.idm.read_only_udm.security_result.action` to UNKNOWN_ACTION.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `rt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-02-25 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field as `BLOCK` or `ALLOW` based on the value of `cn1` raw log field.   
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `reputationString`, `blockID`, `applicationName`, `facility`, `priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `appname` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `proto_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytesFromClient` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `bytesToClient` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Mapped `clientIP` raw log field with `event.idm.read_only_udm.principal.ip` UDM field globally.  
\- `event.idm.read_only_udm.principal.asset.ip`: Mapped `clientIP` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field globally.  
\- `event.idm.read_only_udm.target.hostname`: Added a conditional check before mapping `tar_host` to `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Added a conditional check before mapping `tar_host` to `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.port`: Added a conditional check before mapping `tar_port` to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_UNCATEGORIZED` when user data is present.  
\- Added a grok pattern on `firstLine` raw log field to extract `http_method`, `tar_host`, `tar_port`, `proto`, `proto_version`.  
\- Added support for new pattern of JSON+CEF logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.network.application_protocol`  
\- `event.idm.read_only_udm.network.http.response_code`  
\- `event.idm.read_only_udm.target.url`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.metadata.event_timestamp`  
2026-02-10 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Refactored the parser logic for merging `intermediary` to `event.idm.read_only_udm.intermediary` UDM field across all types of logs due to which hostname from the SYSLOG header is now being mapped to `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2026-01-21 |  Enhancement:  
\- Added new grok pattern to parse unparsed log.  
\- event.idm.read_only_udm.principal.process.file.mime_type: Newly mapped `fileType` raw log field with `event.idm.read_only_udm.principal.process.file.mime_type` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `Type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.   
2025-01-30 |  Enhancement:  
\- Added support for parsing previously unparsed syslog logs.   
2024-12-19 |  Bug-Fix:  
\- Added support to parse unparsed syslog logs.  
\- Changed the mapping of `metadata.event_type` from `STATUS_UPDATE` to `NETWORK_HTTP`.   
2024-10-24 |  Bug-Fix:  
\- Added support to parse unparsed logs.   
2023-06-17 |  Enhancement-  
\- Mapped `sr_bytes` to `network.send_bytes`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `client_ip` to `principal.ip`.   
2023-05-31 |  Bug-fix-  
\- Added Grok pattern to parse logs failing due to extra `-` in CSV format logs.   
2023-01-27 |  Enhancement-  
\- Mapped `requested_host` and `requested_path` to `target.url`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `destination_ip` to `target.ip`.  
\- Mapped `destination_port` to `target.port`.  
\- Mapped `client_ip` to `intermediary.ip`.  
\- Mapped `user_agent` to `network.http.parsed_user_agent`.   
2023-01-16 |  Enhancement-  
\- Added grok pattern for unparsed log.  
\- Mapped `target_ip` to `target.ip`.  
\- Mapped `response_code` to `network.http.response_code`.  
\- Mapped `category_details` to `security_result.category_details`.  
\- Mapped `risk` to `security_result.category_details`.   
2022-09-21 |  Merged customer specific parser to default.  
Added Mapping for unparsed log.  
\- Added on error check for `kv_entry.server_ip`,`kv_entry.method`,kv_entry.src_ip`,`kv_entry.server_ip`,`kv_entry.url_port`,`kv_entry.url`,`kv_entry.status_code"  
`kv_entry.auth_user`,`kv_entry.host`,`kv_entry.user_agent`,`kv_entry.bytes_from_client`,`kv_entry.bytes_to_client,`kv_entry.rep_level,`kv_entry.block_reason`,kv_entry.categories`,`kv_entry.application_name`,`kv_entry.block_res"   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
