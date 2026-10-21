---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wazuh-changelog/
title: Change log for WAZUH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:31:02.559397+00:00
---

# Change log for WAZUH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/wazuh-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for WAZUH

Date | Changes  
---|---  
2025-03-21 |  Enhancement:  
\- Mapped `syscheck.log_event_type` to `principal.resource.attribute.labels`.  
\- If `metadata.event_type` is `GENERIC_EVENT` and `has_principal` is `true`, then set `metadata.event_type` to `STATUS_UPDATE`.   
2025-01-17 |  Enhancement:  
\- Mapped `data.vulnerability.severity` to `security_result.severity`.  
\- Mapped `data.vulnerability.cvss.cvss3.base_score` to `extensions.vulns.vulnerabilities`.  
\- Mapped `data.vulnerability.cve` to `security_result.detection_fields`.  
\- Mapped `data.vulnerability.enumeration` to `security_result.detection_fields`.  
\- Added support to parse several additional fields.   
2024-12-23 |  Enhancement:  
\- Mapped `agent_ip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `agent_name` to `principal.hostname` and `principal.asset.hostname`.  
\- If `syscheck.log_event_type` is `modified`, then set `metadata.event_type` to `FILE_MODIFICATION`.  
\- If `syscheck.log_event_type` is `deleted`, then set `metadata.event_type` to `FILE_DELETION`.   
2024-12-04 |  Enhancement:  
\- Mapped `data.audit.type`, `data.audit.id`, `data.audit.arch`, `data.audit.syscall`, `data.audit.success`, `data.audit.exit`, `data.audit.ppid`, `data.audit.pid`, `data.audit.tid`, `data.audit.auid`, `data.audit.uid`, `data.audit.gid`, `data.audit.euid`, `data.audit.suid`, `data.audit.fsuid`, `data.audit.egid`, `data.audit.sgid`, `data.audit.fsgid`, `data.audit.tty`, `data.audit.session`, `data.audit.command`, `data.audit.exe`, `data.audit.key`, `data.audit.execve.a0`, `data.audit.execve.a1`, `data.audit.cwd`, `data.audit.file.name`, `data.audit.file.inode` , and `data.audit.file.mode` to `additional.fields`.  
\- Mapped `data.command` to `target.process.file.full_path`.   
2024-09-12 |  Enhancement:  
\- Mapped `data.win.eventdata.status`, `data.win.eventdata.logonGuid` to `additional.fields`.  
\- Mapped `data.win.eventdata.ipPort` to `target.port`.  
\- Mapped `data.win.eventdata.serviceName` to `target.resource.name`.  
\- Mapped `data.win.eventdata.ipAddress` to `target.ip` and `target.asset.ip`.   
2024-08-08 |  Enhancement:  
\- Mapped `data.win.eventdata.logonType` to `additional.fields`.  
\- Mapped `data.win.system.providerGuid` to `principal.resource.id`.  
\- Mapped `data.win.system.opcode` to `additional.fields`.  
\- Mapped `data.win.system.version` to `additional.fields`.  
\- Mapped `data.win.system.task` to `additional.fields`.  
\- Mapped `data.win.system.threadID` to `additional.fields`.  
\- Mapped `data.win.system.providerName` to `additional.fields`.  
\- Mapped `data.win.system.processID` to `principal.process.pid`.  
\- Mapped `data.win.eventdata.targetLogonId` to `additional.fields`.  
\- Mapped `data.win.eventdata.targetDomainName` to `target.administrative_domain`.  
\- Mapped `data.win.eventdata.targetUserName` to `target.user.userid`.  
\- Mapped `data.win.eventdata.targetUserSid` to `target.user.windows_sid`.  
\- Mapped `data.win.system.eventRecordID` to `additional.fields`.  
\- Mapped `data.win.system.keywords` to `additional.fields`.  
\- Mapped `data.win.system.channel` to `additional.fields`.  
\- Mapped `data.win.system.eventID` to `metadata.product_event_type`.  
\- Mapped `data.win.system.computer` to `principal.asset.hostname` and `principal.hostname`.  
\- Mapped `data.win.system.level` to `security_result.severity`.   
2024-03-04 |  Enhancement:  
\- Added support for SVROSSEC syslog logs.  
\- Mapped `file_path` to `target.file.full_path`.  
\- Mapped `registry_key` to `target.registry.registry_key`.  
\- Mapped `user_name` to `principal.user.userid`.  
\- Mapped `log_description` to `metadata.description`.  
\- Mapped `action_data` to `security_result.action_details`.  
\- Mapped `src_host` to `principal.hostname`.  
\- Mapped `rule_id` to `security_result.rule_id`.  
\- Mapped `classification` to `security_result.detection_fields`.  
\- Mapped `rule_summary` to `security_result.summary`.  
\- Aligned mappings for `principal.hostname` and `principal.asset.hostname`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.   
2023-07-17 |  \- Added a Grok pattern to parse unparsed syslog logs.  
\- Added null check for `predecoder.hostname`.   
2022-10-14 |  \- Increased parsing percentage.  
\- Added support to parse syslog pattern.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
