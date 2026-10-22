---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openssh-changelog/
title: Change log for OPENSSH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:26.787629+00:00
---

# Change log for OPENSSH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/openssh-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPENSSH

Date | Changes  
---|---  
2024-01-23 |  Enhancement:  
\- Modified a Grok pattern to parse the entire value in `target.user.userid`.   
2023-10-05 |  Enhancement:  
\- Modified the existing mapping: `target.file.sha256` mapped to `network.tls.client.certificate.sha256`.   
2023-08-25 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs and mapped the fields accordingly.   
2023-05-05 |  Enhancement:  
\- Modified the existing mapping, `principal.hostname` mapped to `target.hostanme`.   
2022-10-25 |  Enhancement:  
Added and modified GROK pattern for `message` and `description` fields.  
Mapped `pwd` to `target.file.full_path`.  
Mapped `Sha256` to `target.file.sha256`.  
Mapped `command` to `target.process.command_line`.  
Mapped `tty` to `security_result.about.resource.attribute.labels`.  
Mapped `metadata.event_type` as `STATUS_UPDATE` wherever possible.   
2022-05-18 |  User login action logs such as `auth success - with public key, auth success - with password, auth fail with password` are handled.  
Mapped `USER_LOGIN` to `metadata.event_type`.  
Mapped `User name` to `target.user.userid`.  
Mapped `Source ip` to `principal.ip`.  
Mapped `Source port` to `principal.port`.  
Mapped `MECHANISM_UNSPECIFIED` to `extensions.auth.mechanism`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
