---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-horizon-changelog/
title: Change log for VMWARE_HORIZON \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:50:47.911498+00:00
---

# Change log for VMWARE_HORIZON  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-horizon-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_HORIZON

Date | Changes  
---|---  
2026-03-15 |  Enhancement  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `SecurityID` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `AccountName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `AccountDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `ObjectServer` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.user.windows_sid`: Newly mapped `ObjectName` raw log field with `event.idm.read_only_udm.target.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `HandleID` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `ProcessID` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `ProcessName` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `LogonID` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `ObjectType` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AccessMask` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TransactionID`, `PrivilegesUsedforAccessCheck`, `Accesses`, `AccessReasons`, `Properties`, `RestrictedSIDCount` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped to `USER_RESOURCE_ACCESS` if event contains user resource information.  
\- Added a Grok pattern for `message` field to parse the raw log fields.  
\- Added gsubs for `msg` field to extract key-value pairs.  
\- Added a kv filter to parse the reformatted `msg` field.  
\- Added new Grok for `message` field allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.description`  
2025-07-17 |  Enhancement  
\- Added support for parsing new format of SYSLOG+kv logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ProductLogId` raw log field with `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `DesktopId` raw log field with `event.idm.read_only_udm.principal.resource.id`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `DesktopDisplayName` from `event.idm.read_only_udm.principal.hostname` as it is more appropriate to map it to `event.idm.read_only_udm.principal.resource.name`.  
\- event.idm.read_only_udm.principal.resource.name: Mapped `DesktopDisplayName` raw log field with `event.idm.read_only_udm.principal.resource.name`.  
\- Removed duplicate mapping of `DesktopDisplayName` raw log field from `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `MachineName` raw log field with `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.target.user.user_display_name: Removed mapping of `UserDisplayName` from `event.idm.read_only_udm.target.user.user_display_name` as it is not a target userdisplayname.  
\- event.idm.read_only_udm.principal.user.userid: mapped `UserDisplayName` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `UserId` raw log field with `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when `has_user` is `true`.   
2025-02-06 |  Enhancement  
\- Added support for a new pattern of SYSLOG logs.  
\- Mapped `usr` to `target.user.userid`.  
\- Mapped `MachineId` to `principal.asset.asset_id`.  
\- Mapped `int_host` to `intermediary.hostname`.  
\- Mapped `ip_1` to `principal.ip`.  
\- Mapped `port_number` to `principal.port`.  
\- Added a conditional check when mapping `event_type` to `USER_LOGOUT`, `USER_LOGIN`, `STATUS_UNCATEGORIZED`, `STATUS_SHUTDOWN`, and `STATUS_UPDATE`.   
2024-10-25 |  Feature Request:  
Enhancement  
\- Added support to parse unparsed logs.   
2022-08-15 |  Feature Request:  
\- Changed mapping for `MachineName` from `principal.asset.hostname` to `intermediary.hostname`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
