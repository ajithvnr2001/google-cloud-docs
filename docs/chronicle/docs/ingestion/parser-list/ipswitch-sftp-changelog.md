---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-sftp-changelog/
title: Change log for IPSWITCH_SFTP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:28:13.581459+00:00
---

# Change log for IPSWITCH_SFTP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ipswitch-sftp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IPSWITCH_SFTP

Date | Changes  
---|---  
2025-05-14 |  Enhancement:  
\- Added a Grok pattern to parse the new format of SYSLOG+KV logs.  
\- Added gsub to replace `\\r\\n` and `\\n` with "" in message.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.principal.hostname,event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.hostname,event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `Host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `SessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Newly mapped `listener_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.port: Newly mapped `listener_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `client_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `User` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `command` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `SSH` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field if `channel` is `SSH`.  
\- Added a `has_principal` flag to `true and `has_user` flag to `false` before mapping `event_type` to `STATUS_UPDATE".  
\- Added a `has_user` flag to `true` before mapping `event_type` to `USER_UNCATEGORIZED`.  
\- Added a `has_principal` flag to `true ,`has_user` flag to `false` and conditional check if `channel` contains `SSH` before mapping `event_type` to `NETWORK_CONNECTION".  
\- Added a conditional check if `invalid_grok_format` is `true` before adding drop condition.   
2022-09-05 |  Bug-fix - Updated/Mapped the following fields:-  
\- Unmapped `src_ip` from `observer.hostname`.  
\- Mapped `logstash.collect.host` to `observer.hostname`;  
\- Changed mapping of `syslog_host` from `target.hostname` to `observer.hostname`.  
\- Changed mapping of `logstash.ingest.host` from `observer.hostname` to `intermediary.hostname`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
