---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/solaris-system-changelog/
title: Change log for SOLARIS_SYSTEM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:38.611562+00:00
---

# Change log for SOLARIS_SYSTEM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/solaris-system-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOLARIS_SYSTEM

Date | Changes  
---|---  
2025-12-10 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `sev_det` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- `event.idm.read_only_udm.target.process.command_line`: Removed mapping of `command` from `event.idm.read_only_udm.target.process.command_line`. These changes have been made as these values were not valid command_line and were getting parsed unintentionally.  
\- Added new grok patterns to extract severity details, destination IP, and destination port from various log formats.   
2025-11-19 |  Enhancement:  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `proto` raw log field to `event.idm.read_only_udm.network.application_protocol`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `key_size` from `event.idm.read_only_udm.security_result.detection_fields`. As it is accurate to map this value to `event.idm.read_only_udm.principal.file.size` UDM field.  
\- `event.idm.read_only_udm.principal.file.size`: Mapped `key_size` raw log field to `event.idm.read_only_udm.principal.file.size`.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `daemon` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `queue_id`,`class`, `nrcpts` and `msgid` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Modified the mapping logic for `event.idm.read_only_udm.target.process.command_line` to exclude events where the process is `sshd` or `guard_tap` as these events do not contain a valid command_line.  
\- Added a new grok pattern to support valid syslogs which were initially being dropped.  
\- Updated type of value from `HOSTNAME` to `NOTSPACE` for `relay` raw field in grok patterns.  
\- Updated mapping logic for `from` raw field to map it to `network.email.from`.   
2025-10-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Removed mapping of `dvc` from `event.idm.read_only_udm.principal.ip` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dvc` raw log field to `event.idm.read_only_udm.target.ip` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.principal.asset.ip`: Removed mapping of `dvc` from `event.idm.read_only_udm.principal.asset.ip` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- ``event.idm.read_only_udm.target.asset.ip``: Newly mapped `dvc` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.principal.hostname`: Removed mapping of `dvc` from `event.idm.read_only_udm.principal.hostname` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `dvc` raw log field to `event.idm.read_only_udm.target.hostname` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dvc` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field when the `message` field contains `Accepted password for` since the log is a login event.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `proto` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-09-30 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `auid`, `op`, `algo`, `size`, and `fp` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `acct_username` to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.src.ip`: Removed mapping of `srcIp` from `event.idm.read_only_udm.src.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcIp` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.src.port`: Removed mapping of `srcPort` from `event.idm.read_only_udm.src.port` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcPort` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- Added grok pattern to parse new format of logs.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` for successful login events.   
2025-04-10 |  Enhancement:  
\- Added GROK patterns to support new format of syslog logs.  
\- Added GROK patterns to parse IP addresses in correct fields.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Removed mapping of `HOST` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Mapped `HOST` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- Added a null conditional check before mapping `desc` to `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` if both `dstIp` and `prin_ip` are present.   
2025-04-08 |  Enhancement:  
\- Added Grok patterns to parse new format of logs.  
\- metadata.event_timestamp: Newly mapped `ts` raw log field with `metadata.event_timestamp` UDM field.   
2024-12-29 |  Enhancement:  
\- Added support for a new format of syslog logs.  
\- Mapped `prin_ip` to "`principal.ip`.   
2024-12-06 |  Enhancement:  
\- Added support for a new format of syslog logs.   
2024-04-05 |  Enhancement:  
\- Mapped `targetDisplayName` to `target.user.user_display_name`.  
\- When `process` is `sudo`, then mapped `user` to `principal.user.user_display_name`.   
2024-02-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
