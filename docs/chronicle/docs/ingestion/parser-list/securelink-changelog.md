---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/securelink-changelog/
title: Change log for SECURELINK \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:29.477982+00:00
---

# Change log for SECURELINK  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/securelink-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SECURELINK

Date | Changes  
---|---  
2026-09-03 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `localPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `portType`, `requireLocalPort`, `launchHostType`, `auditDisabled` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `key` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field if it contains email related data, else mapped with `event.idm.read_only_udm.target.user.userid` when it contains user related data.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `NETWORK_CONNECTION` to `event.idm.read_only_udm.metadata.event_type` UDM field when `message` contains principal machine data and target machine data, else mapped to `STATUS_UPDATE` when `message` contains principal machine data.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `event_time` log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added KV filter for `Text` raw log field to parse the raw log fields.   
2025-04-02 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.  
\- Added a condition check before mapping `resource_name` to `event.idm.read_only_udm.network.application_protocol`.  
\- When `method` is `DELETE`, then assigned `target_host` to `principal_host`.   
2023-09-13 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.  
\- Mapped `msg` to `metadata.description`.  
\- Mapped `dst_ip` to `target.ip`.  
\- Mapped `src_ip` to `principal.ip`.  
\- Mapped `proto` to `network.ip_protocol`.  
\- Mapped `priority` to `security_result.severity_details`.  
\- Mapped `classification` to `additional.fields`.  
\- Mapped `url` to `target.url`.   
2023-08-09 |  Bug-Fix:  
\- Modified Grok pattern to parse the `key` field.   
2022-07-13 |  Enhancement:  
\- Modified grok pattern to parse `systemd`, `journal`, `sshd`, `sudo`, `su`, `CROND`, `suricata`, `ntpd`, `kernel`, `suricata-config`, `stunnel` logtypes.  
\- Changed metadata.event_type from `GENERIC_EVENT` to `STATUS_UPDATE` where principal.hostname is not null.  
\- Changed metadata.event_type from `GENERIC_EVENT` to `USER_UNCATEGORIZED` where target.user.userid is not null.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
