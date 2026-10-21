---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-sa-changelog/
title: Change log for SYMANTEC_SA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:56:03.978264+00:00
---

# Change log for SYMANTEC_SA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/symantec-sa-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SYMANTEC_SA

Date | Changes  
---|---  
2025-05-23 |  \- Changed the collected_timestamp format in the syslog header from `yyyy-MM-ddTHH:mm:ssZ` to `yyyy-MM-ddTHH:mm:ssZZ`.   
2025-05-14 |  \- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`:Removed mapping of `host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `event_name` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `event_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `end` from `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `end` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `ts` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Mapped `ts` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2025-03-12 |  \- Newly created parser.  
\- Added a Grok pattern to parse the logs.  
\- Added a KV block to parse the logs.  
\- Mapped `mac_address` to `principal.mac`.  
\- Mapped `sn` to `principal.mac`.  
\- Mapped `ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `remote_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `ip_address` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `host` to `principal.hostname` and `principal.asset.hostname`.  
\- Mapped `logmsg` to `metadata description`.  
\- Mapped `query_id` to `target.resource.attribute.labels`.  
\- Mapped `action_name` to `security_result.action_details`.  
\- Mapped `id` to `target.resource.id`.  
\- Mapped `category` to `target.resource.type`.  
\- Mapped `model` to `target.resource.name`.  
\- Mapped `path` to `target.file.full_path`.  
\- Mapped `evt` to `metadata.product_event_type`.  
\- Mapped `m` and `c` to `additional.fields`.  
\- Mapped `sequenceId` to `metadata.product_log_id`.  
\- Mapped `elapsed_time` to `security_result.detection_fields`.  
\- Mapped `version` to `metadata.product_version`.  
\- Mapped `event_id` to `security_result.rule_id`.  
\- Mapped `event_name` to `security_result.detection_fields`.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `msgs` to `metadata.description`.  
\- Mapped `cs5` to `security_result.summary`.  
\- Mapped `cs4` to `security_result.description`.  
\- Mapped `dmac` to `target.mac`.  
\- Mapped `dst` to `target.ip` and `target.asset.ip`.  
\- Mapped `spt` to `principal.port`.  
\- Mapped `end` to `start` `additional.fields`.  
\- Mapped `smac` to `principal.mac`.  
\- Mapped `src` to `principal.ip` and `principal.asset.ip`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
