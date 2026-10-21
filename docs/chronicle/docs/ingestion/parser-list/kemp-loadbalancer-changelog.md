---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kemp-loadbalancer-changelog/
title: Change log for KEMP_LOADBALANCER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:56.880606+00:00
---

# Change log for KEMP_LOADBALANCER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kemp-loadbalancer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KEMP_LOADBALANCER

Date | Changes  
---|---  
2026-05-21 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `service_info` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `tool_name` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `event_timestamp_data` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.target.process.pid: Newly mapped `process_id` raw log field to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `syslog_ver` , `version1` , `Total` , `Up` , `Down` and `Disabled` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- Added support for SYSLOG format.  
\- Refactored parser logic for event type classification: changed mapping conditions for USER_UNCATEGORIZED , NETWORK_CONNECTION and STATUS_UPDATE event types.   
2025-08-25 |  Enhancement:  
\- Added support Grok pattern for syslog logs.  
\- event.idm.read_only_udm.principal.application: Newly mapped `process_name` raw log field to event.idm.read_only_udm.principal.application.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `sequenceId` raw log field to event.idm.read_only_udm.metadata.product_log_id.  
\- event.idm.read_only_udm.target.url: Newly mapped `http_path` raw log field to event.idm.read_only_udm.target.url.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `hlen` and `nhdrs` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `log_level` raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `http_version` raw log field to event.idm.read_only_udm.security_result.detection_fields.   
2025-04-02 |  Enhancement:  
\- Added Grok patterns to parse the unparsed logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `meta_sequenceId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- Added a gsub to replace `\\r\\n` with ` ` on `message` to parse the logs.  
\- Added a condition check to map event_type to `USER_UNCATEGORIZED` if des_ip is not equal to null, else mapped `event_type` to `GENERIC_EVENT`  
\- Added a condition check before mapping `sshd` to `target.application`.  
\- Added a condition check before mapping `pid` to `target.process.pid`.   
2025-01-13 |  Enhancement:  
\- Added support for a new pattern of syslog logs.  
\- Mapped `event_type` to `USER_UNCATEGORIZED` and `STATUS_UPDATE`.   
2023-05-31 |  Enhancement: Parsed logs with events as `Connected`, `Slave accept`, `Block access to host`.  
\- Mapped `srcip` to `principal.ip`.  
\- Mapped `dstip` to `target.ip`.  
\- Mapped `vs` to `target.ip`.  
\- Mapped `srcport` to `principal.port`.  
\- Mapped `dstport` to `target.port`.  
\- Mapped `resource` to `target.url`.  
\- Mapped `event` to `metadata.product_event_type`.  
\- Parsed failing syslog logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
