---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-alert-changelog/
title: Change log for FIREEYE_ALERT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:46.981016+00:00
---

# Change log for FIREEYE_ALERT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/fireeye-alert-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for FIREEYE_ALERT

Date | Changes  
---|---  
2025-08-12 |  Enhancement:  
\- A mutate filter with gsub is applied to the `message` field to replace `event` with `event1` when the log contains "CEF:   
2025-02-26 |  Enhancement:  
\- Added support for a new pattern of syslog logs.  
\- Reduced generic_event count to 0.   
2024-10-16 |  Enhancement:  
\- Added support for new pattern of syslog logs.   
2024-08-23 |  Enhancement:  
\- Added support to parse new format of field `suser`.  
\- Added support to parse new format of field `duser`.   
2024-08-22 |  Enhancement:  
\- Mapped `appliance`, `msg` to `additional.fields`.  
\- Mapped `alert.action` to `security_result.action_details`.  
\- When `has_email_info` is true, then set `metadata.event_type` to `EMAIL_TRANSACTION`.   
2024-08-09 |  Enhancement:  
\- Added support for the KV logs.   
2024-02-26 |  Enhancement:  
\- Mapped `alert.explanation.os-changes.os.name` to `principal.platform`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.sha1sum` to `principal.file.sha1`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.md5sum` to `principal.file.md5`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.ppid` to `principal.process.parent_process.pid`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.imagepath` to `target.file.full_path`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.tid` to `target.process.pid`.  
\- Mapped `alert.explanation.os-changes.file.processinfo.pid` to `principal.process.pid`.  
\- Mapped `alert.explanation.malware-detected.malware.tests.sha256` to `target.process.file.sha256`.  
\- Mapped `alert.explanation.malware-detected.malware.tests.sha1` to `target.process.file.sha1`.  
\- Mapped `alert.explanation.malware-detected.malware.tests.md5sum` to `target.process.file.md5`.  
\- Mapped `alert.explanation.os-changes.os.build`, `alert.ack`, `alert.sc-version`, `alert.explanation.analysis`, `alert.retroactive`, `alert.explanation.os-changes.malicious-alert.classtype`, `alert.explanation.os-changes.malicious-alert.display-msg`, `alert.explanation.os-changes.html.timestamp`, `alert.explanation.os-changes.html.timestamp`, `alert.explanation.os-changes.html.url`, `alert.explanation.os-changes.html.mode`, `alert.explanation.os-changes.html.sequence`, `alert.explanation.os-changes.html.id`, `alert.explanation.os-changes.html.value`, `alert.explanation.malware-detected.malware.tests.downloaded-at`, `alert.explanation.malware-detected.malware.tests.submitted-at`, `alert.explanation.malware-detected.malware.tests.executed-at`, `alert.explanation.malware-detected.malware.tests.sha512`, `alert.explanation.malware-detected.malware.tests.type`, `alert.explanation.malware-detected.malware.tests.http-header`, and `alert.explanation.malware-detected.malware.tests.original` to `security_result.detection_fields`.   
2024-02-15 |  Enhancement:  
\- Mapped `alert.explanation.malware-detected.malware.http-header` to `security_result.detection_fields`.  
\- Mapped `alert.explanation.malware-detected.malware.name` to `security_result.category_details`.  
\- Mapped `alert.explanation.malware-detected.malware.objurl` to `security_result.about.url`.  
\- Aligned `target.ip`, `target.hostname`, `target.asset.ip` and `target.asset.hostname` mappings.  
\- Aligned `principal.ip`, `principal.hostname` and `principal.asset.ip`, `principal.asset.hostname` mappings.   
2024-01-12 |  Enhancement:  
\- Mapped `alert.explanation.cnc-services.cnc-service.channel`, `content_type`, `content_length`, and `cache_control` to `additional.fields`.  
\- Mapped `alert.explanation.cnc-services.cnc-service.url` to `target.url`.  
\- Mapped `ver_proto` to `network.tls.version_protocol`.  
\- Mapped `src_data` to `principal.ip`.  
\- Mapped `http_user_agent` to `network.http.user_agent`.  
\- Mapped `method` to `network.http.method`.   
2023-12-05 |  Enhancement:  
\- Mapped `alert.explanation.malware-detected.malware.name`, `alert.explanation.malware-detected.malware.sid`, `alert.explanation.malware-detected.malware.stype`, `alert.explanation.cnc-services.cnc-service.type` to `security_result.detection_fields`.   
2023-11-09 |  Enhancement:  
\- Mapped `alert.explanation.malware-detected.malware.http-header` to `security_result.detection_fields`.  
\- Mapped `alert.explanation.malware-detected.malware.objurl` to `security_result.about.url`.   
2023-09-29 |  Enhancement:  
\- Adjusted the parser to support JSON format logs along with SYSLOG + JSON.  
\- Mapped `alert.explanation.malware-detected.malware.1.objurl` to `security_result.about.url`.   
2022-08-26 |  Enhancement:  
\- Mapped `action_taken` to `security_result.summary`.  
\- Mapped `sig-revision`, `sig-name` , `sig-id`, `attack-mode`, `mvx-status` to `security_result.about.labels`.  
\- Mapped `ips-detected.cve-id` to `principal.asset.vulnerabilities`.  
\- Mapped `sensor` to `intermediary.hostname`.  
\- Mapped `appliance-id`, `match-count` to `additional.fields`.   
2022-08-09 |  Enhancement:  
\- Mapped `alert.dst.smtp-to` to `network.email.to`.  
\- Added conditional check for `sec_result.category_details`.  
\- Mapped `process_md5` to `target.process.file.md5`.  
\- Mapped `endpoint_type` to `security_result.about.labels`.  
\- Mapped `name` to `metadata.description`.  
\- Mapped `source_info.ip` to `principal.ip`.  
\- Mapped `id` to `principal.resource.id`.  
\- Mapped `customer_id` to `target.resource.id`.  
\- Mapped `group` to `security_result.category_details`.  
\- Mapped `process` to `principal.process.pid`.  
\- Mapped `principal_host` to `principal.hostname`.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `severity` to `security_result.severity`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
