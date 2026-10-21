---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/steelhead-changelog/
title: Change log for STEELHEAD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:00:56.480790+00:00
---

# Change log for STEELHEAD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/steelhead-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for STEELHEAD

Date | Changes  
---|---  
2025-06-16 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `desc` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_type:  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` if `has_target_user` is `true` and `desc` has `access accepted` or `Login successful`.  
\- Setting `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` if `has_target_user` is `true` and `desc` has `failure` or `terminated`.   
2024-06-11 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.  
\- Mapped `cmd_line` to `principal.process.command_line`.  
\- Mapped `userid` to `principal.user.userid`.   
2024-04-12 |  Enhancement:  
\- Added Grok patterns to support new pattern of SYSLOG logs.   
2024-01-12 |  Enhancement:  
\- Added Grok patterns to support new pattern of SYSLOG logs.   
2022-08-08 |  Enhancement:  
\- The field `agent.ephemeral_id` is mapped to `additional.fields[n]`.  
\- The field `tags` is mapped to `additional.fields[n].list_value[n]`.  
\- The field `logstash.irm_environment` is mapped to `additional.fields[n]`.  
\- The field `logstash.irm_site` is mapped to `additional.fields[n]`.  
\- The field `logstash.irm_region` is mapped to `additional.fields[n]`.  
\- The field `host.hostname` is mapped to `target.hostname`.  
\- The field `host.id` is mapped to `target.asset_id`.  
\- The field `host.architecture` is mapped to `target.asset.hardware[n].cpu_platform`.  
\- The field `host.ip[n]` is mapped to `target.ip`.  
\- The field `host.mac[n]` is mapped to `target.mac`.  
\- The field `host.os.platform` is mapped to `target.platform`.  
\- The field `host.os.version` is mapped to `target.platform_version`.  
\- The field `host.os.kernel` is mapped to `target.platform_patch_level`.  
\- The field `agent.type` and `agent.id` are mapped to `intermediary.asset_id`.  
\- The field `event.category[n]` is mapped to `security_result.category_details[n]`.  
\- The field `syslog_severity` is mapped to `security_result.severity` and `security_result.severity_details`.  
\- The field `network.community_id` is mapped to `network.community_id`.  
\- The field `logstash.ingest.timestamp` is mapped to `metadata.ingested_timestamp`.  
\- The field `logstash.collect.host` is mapped to `observer.hostname` or `observer.ip` accordingly.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
