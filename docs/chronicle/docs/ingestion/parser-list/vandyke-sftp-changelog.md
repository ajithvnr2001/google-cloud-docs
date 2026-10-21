---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vandyke-sftp-changelog/
title: Change log for VANDYKE_SFTP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:02:23.436360+00:00
---

# Change log for VANDYKE_SFTP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vandyke-sftp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VANDYKE_SFTP

Date | Changes  
---|---  
2025-05-15 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_type: Removed mapping of `STATUS_UPDATE` from `event.idm.read_only_udm.metadata.event_type` UDM field and mapped to `USER_LOGIN` if it is a login event.  
\- event.idm.read_only_udm.metadata.event_type: Removed mapping of `STATUS_UPDATE` from `event.idm.read_only_udm.metadata.event_type` UDM field and mapped to `USER_LOGOUT` if it is a logout event.  
\- Added Grok patterns to support new pattern of logs.  
\- event.idm.read_only_udm.principal.user.userid: Removed mapping of `user_id` from `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Removed mapping of `username` from `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Mapped `username` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `ALLOW` with `event.idm.read_only_udm.security_result.action` if it is a successful login event.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `BLOCK` with `event.idm.read_only_udm.security_result.action` if it is a failed login event.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-13 |  Enhancement:  
\- Added `gsub` filters to remove carriage returns (\r\n) and newlines (\n) from the `message` field.  
\- Modified the grok pattern for the `port` field from %{DATA:port} to %{INT:port} to ensure the port is parsed as an integer.   
2025-03-13 |  Enhancement:  
\- Added a Grok pattern to extract `prinicipal.user.userid`.  
\- Mapped `reason` to `security_result.summary`.  
\- Mapped `srcip` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `username` to `principal.user.user_display_name`.   
2025-02-11 |  Enhancement:  
\- Added a Grok pattern for new syslog format.   
2022-03-25 |  \- Newly created parser.  
\- Supports JSON + SYSLOG format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
