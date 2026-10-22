---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-db-changelog/
title: Change log for IMPERVA_DB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:15.445521+00:00
---

# Change log for IMPERVA_DB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/imperva-db-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IMPERVA_DB

Date | Changes  
---|---  
2025-02-19 |  Enhancement:  
\- Added support to parse new logs with SYSLOG+JSON format.   
2024-04-09 |  Enhancement:  
\- Added `gsubs` to handle invalid JSON characters in logs.  
\- Mapped `raw-query` to `security_result.detection_fields`.   
2024-01-21 |  Enhancement:  
\- Added a new Grok pattern to parse unparsed logs of format SYSLOG+JSON.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `dest-ip` to `target.ip`.  
\- Mapped `dest-port` to `target.port`.  
\- Mapped `source-ip` to `principal.ip`.  
\- Mapped `source-port` to `principal.port`.  
\- Mapped `db-user` to `principal.user.userid`.  
\- Mapped `os-user` to `principal.user.userid`.  
\- Mapped `protocol` to `network.ip_protocol`.  
\- Mapped `audit-policy` to `security_result.category_details`.  
\- Mapped `server-group`, `service-name`, `user-group`, `raw-query`, `parsed-query`, `bind-variables`, `sql-error`, `db-schema-pair.db-name`, `db-schema-pair.schema-name`, and `objects-list` to `additional.fields`.  
\- Mapped `application-name` to `target.application`.  
\- Mapped `source-application` to `principal.application`.  
\- Mapped `event-id` to `metadata.product_log_id`.  
\- Mapped `event-type` to `metadata.product_event_type`.  
\- Mapped `application-user` to `principal.user.user_display_name`.  
\- Mapped `host-name` to `principal.hostname`.  
\- Mapped `mx-ip`, `gw-ip` to `intermediary.ip`.  
\- Mapped `policy-id` and `user-authenticated` to `security_result.detection_fields`.  
\- If `has_principal` is `true` and `has_target` is `true`, then set `metadata.event_type` as `NETWORK_CONNECTION`.  
\- If `has_principal` is `true`, then set `metadata.event_type` as `STATUS_UPDATE`.   
2023-07-17 |  Bug-Fix  
\- Parsed unparsed raw logs using Grok patterns and `kv` filters.  
\- Mapped `srcPort` to `principal.port`.  
\- Mapped `srcIP` to `principal.ip`.  
\- Mapped `dstIP` to `target.ip`.  
\- Mapped `dstPort` to `target.port`.  
\- Mapped `alertSev` to `security_result.severity`.  
\- Mapped `ruleName` to `security_result.rule_name`.  
\- Mapped `category` to `security_result.category`.  
\- Mapped `group` to `target.user.group_identifiers`.  
\- Mapped `dbName` to `target.resource.name`.  
\- Mapped `policyName` to `security_result.detection_fields`.  
\- Mapped `username` to `principal.user.user_display_name`.  
\- Mapped `evntDesc` to `security_result.description`.  
\- Mapped `action` to `security_result.action_details`.   
2023-02-03 |  Enhancement  
\- Mapped `event_name` to `metadata.product_event_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
