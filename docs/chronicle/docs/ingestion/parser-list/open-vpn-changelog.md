---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/open-vpn-changelog/
title: Change log for OPEN_VPN \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:17:28.611895+00:00
---

# Change log for OPEN_VPN  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/open-vpn-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OPEN_VPN

Date | Changes  
---|---  
2026-07-03 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `IV_TCPNL`, `IV_PROTO`, `depth`, `CN`, `IV_SSO`, `IV_NCP`, `IV_GUI_VER`, `IV_VER`, `IV_LZ4v2`, `IV_LZO`, `IV_COMP_STUB`, `IV_COMP_STUBv2` from `event.idm.read_only_udm.about.labels` UDM field as this UDM field is deprecated.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Mapped `IV_TCPNL`, `IV_PROTO`, `depth`, `CN`, `IV_SSO`, `IV_NCP`, `IV_GUI_VER`, `IV_VER`, `IV_LZ4v2`, `IV_LZO`, `IV_COMP_STUB`, `IV_COMP_STUBv2` raw log fields with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses` and `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `useremail` field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `useremail` has valid email otherwise mapped `useremail` field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `labels.compute.googleapis.com/resource_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `resource.labels.instance_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone`: Newly mapped `resource.labels.zone` raw log field with `event.idm.read_only_udm.target.resource.attribute.cloud.availability_zone` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `receiveTimestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `insertId`, `logName`, `log_source`, `app_id`, `interface` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `resource.labels.project_id` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Newly mapped `resource.type` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when user data and principal machine data are present.   
2024-11-27 |  Enhancement  
\- Added Grok patterns to parse unparsed logs.  
\- Mapped `username1` field to `target.user.userid`.  
\- Mapped `msg1` field to `metadat.description`.  
\- Mapped `metadata.event_type` to `USER_UNCATEGORIZED` when target.user.userid is set.  
\- Mapped `metadata.product_event_type` to `Peer Connection Initiated` for the logs having `Peer Connection Initiated` in the `operation` field.   
2023-11-27 |  Enhancement  
\- Added support for JSON format logs.  
\- Mapped `HOSTNAME` to `principal.hostname`.  
\- Mapped `PID` to `principal.process.pid`.  
\- Mapped `CMDLINE` to `principal.process.command_line`.  
\- Mapped `SYSTEMD_UNIT` to `additional.fields`.  
\- Mapped `SYSTEMD_SLICE` to `additional.fields`.  
\- Mapped `SYSTEMD_INVOCATION_ID` to `additional.fields`.  
\- Mapped `SYSLOG_IDENTIFOER` to `additional.fields`.  
\- Mapped `COMM` to `additional.fields`.  
\- Added GROK pattern to map `MESSAGE`  
2022-04-28 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
