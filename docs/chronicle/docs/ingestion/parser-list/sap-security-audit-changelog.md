---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-security-audit-changelog/
title: Change log for SAP_SECURITY_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:29.590484+00:00
---

# Change log for SAP_SECURITY_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sap-security-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SAP_SECURITY_AUDIT

Date | Changes  
---|---  
2026-03-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: If `txsubclsid` and `TXSUBCLSID` is `Dialog logon`, removed mapping of `slguser` or `SLGUSER` from `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: If `txsubclsid` or `TXSUBCLSID` is `Dialog logon`, mapped `slguser` or `SLGUSER` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: If `txsubclsid` or `TXSUBCLSID` is `Dialog logon`, mapped `useralias` or `USERALIAS` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: If `txsubclsid` or `TXSUBCLSID` is `User Master Changes`, newly mapped `useralias` or `USERALIAS` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: If `txsubclsid` or `TXSUBCLSID` is `User Master Changes`, newly mapped `slguser` or `SLGUSER` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: If `txsubclsid` or `TXSUBCLSID` is not `Dialog logon` or `User Master Changes`, mapped `slguser` or `SLGUSER` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: If `txsubclsid` or `TXSUBCLSID` is not `Dialog logon` or `User Master Changes`, and `slguser` or `SLGUSER` is empty, mapped `useralias` or `USERALIAS` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: If `txsubclsid` or `TXSUBCLSID` is not `Dialog logon` or `User Master Changes`, newly mapped `useralias` or `USERALIAS` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` when `slguser` or `SLGUSER` is not empty.  
\- `event.idm.read_only_udm.security_result.action`: If `msg` or `MSG` is `AU1`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.action`: If `msg` or `MSG` is `AU6`, `AUI`, or `AUJ`, updated the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- `event.idm.read_only_udm.security_result.action`: If `msg` or `MSG` has other values, updated the value of `event.idm.read_only_udm.security_result.action` to `UNKNOWN_ACTION`.   
2026-01-28 |  \- Newly created parser.  
\- Added support for JSON format logs.  
\- Initialized various raw log fields to avoid undeclared field errors.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `slgltrm2` and `SLGLTRM2` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field. If the `slgltrm2` and `SLGLTRM2` value is a valid IP address, it is mapped to the `principal.ip` and `principal.asset.ip` UDM fields. If not, it is mapped to the `principal.hostname` and `principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `termIpv6` and `TERM_IPV6` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field. If `termIpv6` and `TERM_IPV6` is not empty, is not equal to `slgltrm2` and `SLGLTRM2`, and contains a valid IP address, it is merged into `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `slgrepna` and `SLGREPNA` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `sid` and `SID` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `instance` and `INSTANCE` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `salDate`, `salTime` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `SAL_DATE`, `SAL_TIME` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped from `slguser` if present, else from `useralias` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Mapped from `SLGUSER` if present, else from `USERALIAS` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `class` and `CLASS` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `salData` and `SAL_DATA` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `epp` and `EPP` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `subid`, `SUBID`, `SLGMAND` and `slgmand` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `taskno` and `TASKNO` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `slgtc`, `SLGTC`, `SUBCLASID` and `subclasid` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `txsubclsid` and `TXSUBCLSID` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severityS` and `SEVERITY_S` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `txseverity` and `TXSEVERITY` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `counter`, `COUNTER`, `severity`, `SEVERITY`, `msg`, `MSG`, `fileNo`, `FILE_NO`, `tasktype`, `TASKTYPE`, `slgdattim`, `SLGDATTIM`, `logTstmp`, `LOG_TSTMP`, `area`, `AREA`, `param1`, `PARAM1`, `param2`, `PARAM2`, `PARAM3`, `param3`, `PARAMX`, `paramx`, `src`, `SRC`, `xstring`, `XSTRING`, `smtp_addr` and `SMTP_ADDR` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
