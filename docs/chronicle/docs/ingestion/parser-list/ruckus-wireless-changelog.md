---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ruckus-wireless-changelog/
title: Change log for RUCKUS_WIRELESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:54:35.841367+00:00
---

# Change log for RUCKUS_WIRELESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ruckus-wireless-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RUCKUS_WIRELESS

Date | Changes  
---|---  
2025-10-31 |  \- Added new Grok patterns to parse the unparsed logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `sequenceId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `uid`, `p_user`, `prin_user`, `user` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `auid`, `subj`, `p_uid` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `cwd` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `acct`, `t_user`, `user` raw log fields with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `t_uid` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `cmd`, `cmd_line` raw log fields with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `exe` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.auth_details`: Newly mapped `grantors`, `auth_method` raw log fields with `event.idm.read_only_udm.extensions.auth.auth_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Statically mapped to `ALLOW` or `BLOCK` based on the value of the `res` field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Statically mapped to `AUTHTYPE_UNSPECIFIED` for certain event types and messages.  
\- `event.idm.read_only_udm.security_result.description`: Mapped from `pam_msg` or `audit_msg` based on parsing success and description field.  
\- `event.idm.read_only_udm.security_result.action_details`: Mapped from the `op` field.   
2024-07-02 |  \- Added new Grok patterns to parse the unparsed logs.  
\- Mapped `summary` to `security_result.description`.   
2023-01-06 |  Added new grok patterns to parse the unparsed logs.   
2022-09-12 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
