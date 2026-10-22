---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-as400-changelog/
title: Change log for IBM_AS400 \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:52:03.546882+00:00
---

# Change log for IBM_AS400  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-as400-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_AS400

Date | Changes  
---|---  
2026-09-01 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `column11` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `column9` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `column2` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `column24` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `column42` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.port: Newly mapped `column41` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `column10` (as `job_name`), `column12` (as `job_number`), `column13` (as `process`), `column14` (as `pgm_name`), `column15` (as `pgm_libr`), and `column23` (as `eff_user`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-11-07 |  Enhancement:  
\- Added grok pattern to extract timestamp and `intermediary_hostname` from SYSLOG format logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `event_time` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_userid` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_hostname` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.extensions.auth.type: Set the auth type to AUTHTYPE_UNSPECIFIED.  
\- event.idm.read_only_udm.intermediary: Mapped the extracted `intermediary_hostname` to the `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Added new logic to set `event.idm.read_only_udm.metadata.event_type` to USER_LOGIN based on `has_target_user` and `msg` fields.  
\- Added a drop filter to discard malformed, non-CEF messages.   
2025-03-28 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `process` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `event_info` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_event` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.severity: Newly mapped `sev` raw log field with `event.idm.read_only_udm.severity` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `access_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `actual_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `jrn_seq` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `job_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `job_number` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `eff_user` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `logical_partition` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `auth_user` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cmd_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `object` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `object_library` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `object_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ifs_path` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `specific_data` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `ip_addr` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `action` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `val_job` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `val_user` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `val_jobno` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `pgm_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `pgm_libr` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `workstation` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `causing_user` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `field` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `op_violation` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a conditional null check for `device_vendor` before mapping it to `event.idm.read_only_udm.metadata.vendor_name` UDM field.   
2024-05-24 |  Enhancement:  
\- Added support for CEF format logs.   
2024-04-16 |  Enhancement:  
\- Added a Grok pattern to parse SYSLOG + JSON logs.  
\- Mapped all new JSON fields to corresponding udm.   
2022-04-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
