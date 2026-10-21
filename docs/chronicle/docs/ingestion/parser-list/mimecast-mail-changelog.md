---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-changelog/
title: Change log for MIMECAST_MAIL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:23:53.849274+00:00
---

# Change log for MIMECAST_MAIL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mimecast-mail-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MIMECAST_MAIL

Date | Changes  
---|---  
2025-07-01 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `spf.allow`,`spf.info`,`dkim.allow`, `dkim.info`, `dmarc.allow`, `dmarc.info` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `TlsVer`raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `Cphr`raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.   
2025-04-23 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field basing on `Action` raw log field.  
\- `event.idm.read_only_udm.security_result.action`: When `Action` raw log field value is `warn` then `event.idm.read_only_udm.security_result.action` UDM field value is `ALLOW_WITH_MODIFICATION`.  
\- `event.idm.read_only_udm.security_result.action`: When `Action` raw log field value is `hold` then `event.idm.read_only_udm.security_result.action` UDM field value is `QUARANTINE`.  
\- `event.idm.read_only_udm.security_result.action`: When `Delivered` raw log field value is `false` then `event.idm.read_only_udm.security_result.action` UDM field value is `fail` else if `Delivered` raw log field value is `true` then `event.idm.read_only_udm.security_result.action` UDM field value is `ALLOW`.   
2025-02-06 |  Enhancement:  
\- Changed mapping of `filename_for_malachite` from `target.process.file.full_path` to `principal.resource.name`.  
\- Changed mapping of `fileName` from `principal.process.file.full_path` to `target.process.file.full_path`.   
2025-01-23 |  Enhancement:  
\- Mapped `md5` to `target.file.md5`.  
\- Changed mapping of `filename_for_malachite` from `principal.resource.name` to `target.process.file.full_path`.  
\- Mapped `urlCategory` to `principal.url_metadata.categories`.  
\- Mapped `credentialTheft` to `security_result.detection_fields`.  
\- Mapped `reason` to `security_result.summary`.   
2024-11-13 |  Enhancement:  
\- Mapped `URL` to `principal.url`.   
2024-08-05 |  Enhancement:  
\- Mapped `sourceIp` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `url` to `principal.url`.  
\- Mapped `msgid` to `network.email.mail_id`.  
\- Mapped `subject` to `network.email.subject`.  
\- Mapped `senderDomain`, `AttNames`, and `AttCnt` to `security_result.detection_fields`.   
2023-03-31 |  Enhancement:  
\- Mapped `filename_for_malachite` to `principal.resource.name`.  
\- Mapped `fileName` to `principal.process.file.full_path`.  
\- Mapped `sha256` to `target.file.sha256`.  
\- Mapped `sha1` to `target.file.sha1`.  
\- Added conditional check for `aCode`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
