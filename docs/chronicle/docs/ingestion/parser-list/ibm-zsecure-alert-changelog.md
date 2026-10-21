---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zsecure-alert-changelog/
title: Change log for IBM_ZSECURE_ALERT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:40:54.939371+00:00
---

# Change log for IBM_ZSECURE_ALERT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/ibm-zsecure-alert-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IBM_ZSECURE_ALERT

Date | Changes  
---|---  
2025-06-19 |  \- Newly added gsub for `kv_data` to parse the logs.  
\- Newly added grok pattern to parse the logs which were in `LEEF` format.  
\- Newly added KV filter to parse the logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp` : Newly mapped `device_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid` : Newly mapped `usrName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name` : Newly mapped `name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line` : Newly mapped `job` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `intent`, `class`, `prof`, `res`, `function`, and `owner` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `auth` and ,`logstr` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details` : Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details` : Newly mapped `allow` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary` : Newly mapped `sum` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.action` : Nelwy mapped `desc` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Nelwy mapped `used`, `oGID` and , `oUID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path` : Newly mapped `path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Newly mapped `usrPriv` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version` : Newly mapped `product_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type` : Newly mapped `event.idm.read_only_udm.metadata.event_type` as `USER_RESOURCE_ACCESS` when `has_principal_user` and `has_target_resource` are `true`.   
2025-03-14 |  Newly created parser.  
Supported log format: SYSLOG.  
Mapped the following fields:  
\- `priority` to `security_result.detection_fields`  
\- `timestamp` to `metadata.event_timestamp`  
\- `hostname` to `principal.hostname` and `principal.asset.hostname`  
\- `app_name` to `target.application`  
\- `parameter` to `target.resource.attribute.labels`  
\- `class` to `target.resource.attribute.labels`  
\- `profile` to `target.resource.attribute.labels`  
\- `uacc` to `target.resource.attribute.labels`  
\- `parm` to `target.resource.attribute.labels`  
\- `action` to `security_result.action_details`  
\- `racf_user` to `target.resource.attribute.labels`  
\- `racf_name` to `target.resource.attribute.labels`  
\- `racfcmd` to `target.resource.attribute.labels`  
\- `dnsname` to `target.resource.attribute.labels`  
\- `volume` to `target.resource.attribute.labels`  
\- `poe` to `target.resource.attribute.labels`  
\- `resource` to `target.resource.attribute.labels`  
\- `granted` to `additional.fields`  
\- `allowed` to `additional.fields`  
\- `intent` to `additional.fields`  
\- `userid` to `principal.user.userid`  
\- `name` to `principal.user.user_display_name`  
\- `jobname` to `additional.fields`  
\- `system` to `additional.fields`  
\- `attempts` to `additional.fields`  
\- `terminal` to `principal.asset.attribute.labels`  
\- `srcip` to `principal.ip` and `principal.asset.ip`  
\- `msg` to `security_result.description`  
\- `mesg` to `security_result.detection_fields`  
\- `wto_msg` to `security_result.detection_fields`  
\- `desc` to `security_result.detection_fields`  
\- `svcno` to `target.resource.attribute.labels`  
\- `esrno` to `target.resource.attribute.labels`  
\- `curr_address` to `target.resource.attribute.labels`  
\- `curr_apf` to `target.resource.attribute.labels`  
\- `unix_path` to `target.file.full_path`  
\- Set `event_type` to `USER_RESOURCE_ACCESS` if principal, target and action are present.  
\- Set `event_type` to `STATUS_UPDATE` if only principal is present.  
\- Set `event_type` to `GENERIC_EVENT` if none of the above conditions are met.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
