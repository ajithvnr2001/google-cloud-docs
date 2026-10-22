---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-junos-changelog/
title: Change log for JUNIPER_JUNOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:40.730157+00:00
---

# Change log for JUNIPER_JUNOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/juniper-junos-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for JUNIPER_JUNOS

Date | Changes  
---|---  
2026-09-07 |  Enhancement:  
\- Added support for new format of JSON+SYSLOG logs.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `appname` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `proc_id` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `priority`, `facility`, `status`, `message_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set to `USER_UNCATEGORIZED` when user data is present, else set to `STATUS_UPDATE` when principal machine data is present else set to `GENERIC_EVENT`.   
2025-10-10 |  Enhancement-  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `interface` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.process.pid` : Newly mapped `p_id` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- Modified a grok pattern to capture `lldp_status` instead of `sub_type` from the raw log for specific message formats.  
\- Added a `security_result` element where `detection_fields` includes key `neighbor_count` mapped from the `neighbor_count` variable.  
\- Added a `security_result` element where `detection_fields` includes key `lldp_status` mapped from the `lldp_status` variable.   
2024-06-18 |  Enhancement-  
\- Added support to handle unparsed SYSLOG logs.   
2024-06-07 |  Enhancement-  
\- Added Grok patterns to parse the new pattern of SYSLOG logs.  
\- When `protocol-name` has a valid IP protocol, then mapped `protocol-name` to `network.ip_protocol`.   
2024-05-02 |  Enhancement-  
\- Added Grok patterns to support new SYSLOG + KV format logs.   
2023-10-25 |  Enhancement-  
\- Added Grok patterns to parse unparsed logs.  
\- Mapped `source_port` to `principal.port`.  
\- Mapped `source_address` to `principal.ip`.  
\- Mapped `user_name` to `target.user.userid`.  
\- Mapped `application_name` to `target.application`.  
\- Mapped `p_id` to `target.process.pid`.  
\- Added `invalid_pattern` check before KV mapping.  
\- Added a Grok pattern to map `security_result.description` when `description_present` is false.   
2023-08-17 |  Enhancement-  
\- Added Grok pattern to parsed unparsed logs.  
\- Mapped `msg` to `security_result.summary`.  
\- Mapped `src_ip` to `principal.ip`.  
\- Mapped `user` to `target.user.userid`.  
\- Mapped `username` to `principal.user.userid`.  
\- Mapped `command` to `target.process.command_line`.  
\- Mapped `src_port` to `principal.port`.  
\- Mapped `ssh2` to `security_result.detection_fields`.  
\- Mapped `sha256` to `principal.process.file.sha256`.  
\- Mapped `desc` to `sec_result.summary`.  
\- Mapped `mac-address` to `principal.mac`.  
\- Mapped `host` to `principal.hostname` if event_type is `STATUS_UPDATE`.   
2023-01-15 |  Enhancement-  
\- Modified Grok pattern to support unparsed logs containing type `UI_CMDLINE_READ_LINE`, `UI_COMMIT_PROGRESS`, `UI_CHILD_START`,  
`UI_CFG_AUDIT_OTHER`, `UI_LOGIN_EVENT`, `UI_CHILD_STATUS`, `UI_LOGOUT_EVENT`, `UI_LOAD_EVENT`,  
`JTASK_IO_CONNECT_FAILED`, `UI_AUTH_EVENT`, `UI_NETCONF_CMD`, `UI_COMMIT_NO_MASTER_PASSWORD`, `UI_CFG_AUDIT_SET`, `UI_JUNOSCRIPT_CMD`,  
`SNMPD_AUTH_FAILURE`, `UI_CFG_AUDIT_NEW`, `UI_COMMIT` , `LIBJNX_LOGIN_ACCOUNT_LOCKED`, `UI_COMMIT_COMPLETED`,  
`PAM_USER_LOCK_LOGIN_REQUESTS_DENIED`, `RTPERF_CPU_USAGE_OK`, `RTPERF_CPU_THRESHOLD_EXCEEDED`, `LIBJNX_LOGIN_ACCOUNT_UNLOCKED`,  
`JSRPD_SET_OTHER_INTF_MON_FAIL`, `JSRPD_SET_SCHED_MON_FAILURE`, `UI_CHILD_WAITPID`, `UI_DBASE_LOGIN_EVENT`.   
2022-05-02 |  New default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
