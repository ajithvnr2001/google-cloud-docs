---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-netwitness-changelog/
title: Change log for RSA_NETWITNESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:27.717931+00:00
---

# Change log for RSA_NETWITNESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/rsa-netwitness-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for RSA_NETWITNESS

Date | Changes  
---|---  
2026-09-25 |  \- Added support for CEF and JSON format of logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `_time` and `rt` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `device_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `device_event_class_id` and `event_name` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `host`, `src`, `remote_ip`, and `remoteAddress` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `spt` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `userGroup` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `userRole` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` and `value` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `cribl_pipe` and `sourceServiceName` raw log fields with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `deviceExternalId` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `dvcpid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `deviceProcessName` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `file` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `key` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `uri` and `queryString` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sessionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Set `event.idm.read_only_udm.network.application_protocol` UDM field to `HTTP` when `event_name` is `HttpRequest` or `method` is `GET`, `POST`, `PUT`, or `DELETE`.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `referrer` and `referrerURL` raw log fields with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `userAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `X-Forwarded-For` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `outcome` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `outcome` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `_dataId`, `cef_version`, `device_product`, `scope`, `deviceFacility`, `arguments`, `id1`, `id2`, `size`, `flags`, `threshold`, `fieldName`, `where`, `queryPriority`, `deviceId`, `predicateIds`, and `_dc` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` UDM field to `USER_LOGIN`, `USER_LOGOUT`, `NETWORK_HTTP`, `USER_RESOURCE_ACCESS`, or `STATUS_UPDATE` based on user and machine data.   
2022-10-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
