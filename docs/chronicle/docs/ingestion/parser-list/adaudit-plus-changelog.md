---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adaudit-plus-changelog/
title: Change log for ADAUDIT_PLUS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:44.224484+00:00
---

# Change log for ADAUDIT_PLUS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/adaudit-plus-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ADAUDIT_PLUS

Date | Changes  
---|---  
2026-06-05 |  Enhancement :  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `facility`, `priority`, `version`, `appname`, `USER_MGMT_TYPE` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `CALLER_USER_DOMAIN`, `CALLER_LOGON_ID`, `ATTRIBUTE_CATEGORY_ID`, `CALLER_DISTINGUISH_NAME`, `CALLER_USER_OU_GUID` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When event_type is `USER_CHANGE_PERMISSIONS` and `has_principal_user` is `true` or `target_user_present` is `true` updated the `event.idm.read_only_udm.metadata.event_type` to `USER_CHANGE_PERMISSIONS .  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `ACCOUNT_DISPLAY_NAME`, `ACCOUNT_DISTINGUISH_NAME`, `ACCOUNT_NAME_OU_GUID` raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- Added support for json format logs.   
2026-02-10 |  Enhancement :  
\- Added grok pattern to parse new format of syslog log.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `USER_SID` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `USER_DISTINGUISH_NAME` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `USER_DISPLAY_NAME` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `LOGON_SERVICE`, `PRE_AUTHENTICATION_TYPE`, `TICKET_OPTIONS`, `TICKET_ENCRYPTION_TYPE`, `EXTRA_COLUMN1` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ERROR_CODE` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `USER_OU_GUID` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `CLIENT_HOST_DOMAIN_NAME` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- Added on_error for date function of `TIME_GENERATED` to avoid failures.   
2025-04-10 |  Enhancement :  
\- Updated `event.idm.read_only_udm.metadata.event_type` to `USER_DELETION` when `target_user_present` is `true`.  
\- Mapped flag `target_user_present` to true whenever `event.idm.read_only_udm.target.user.userid` udm field is not null.  
\- Added flag check `target_user_present` for `target.user.userid` before mapping `event.idm.read_only_udm.metadata.event_type` to `USER_DELETION`.  
\- Validated IP for `shost` using grok pattern.   
2025-03-03 |  Enhancement :  
\- Mapped `CALLER_USER_NAME` , `ATTRIBUTES_TEXT` , `MEMBER_NAME` , `MEMBER_SAM_ACCOUNT_NAME` and `MEMBER_DISPLAY_NAME` to `principal.resource.attribute.labels`.   
2025-02-19 |  Enhancement :  
\- Mapped `EVENT_NUMBER`, `REMARKS`, `EVENT_TYPE`, `ATTRIBUTES_NEW_VALUE`, `ATTRIBUTES_OLD_VALUE`, and `OPERATION_TYPE` to `additional.fields`.  
\- Mapped `EVENT_TYPE_TEXT` to `security_result.detection_fields`.  
\- Mapped `ACCOUNT_NAME` to `principal.user.user_display_name`.   
2024-05-20 |  Enhancement :  
\- If the value of the field `outcome` is similar to `Success`, set `security_result.action` to `ALLOW`.  
\- If the value of the field `msg_data` is similar to `Success`, set `security_result.action` to `ALLOW`.  
\- Added a Grok pattern over `msg_data` to extract `act`, `suid` and `reason`.  
\- Mapped `msg_data` to `security_result.description`.  
\- Mapped `cs1`, `cs3`, `cs4`, `cs5`, `cn1`, `cn2`, and `cn3` to "`additional.fields`.   
2024-01-19 |  Enhancement :  
\- Modified a Grok pattern to parse unparsed logs.  
\- Mapped `IP` to `principal.asset.ip`.  
\- Mapped `_PrincipalIP` to `principal.asset.ip`.  
\- Mapped `host` to `principal.asset.hostname`.  
\- Mapped `principalHost` to `principal.asset.hostname`.  
\- Mapped `SOURCE` to `principal.asset.hostname`.  
\- Mapped `_TargetIP` to `target.asset.ip`.  
\- Mapped `CLIENT_IP_ADDRESS` to `target.asset.hostname`.  
\- Mapped `CLIENT_HOST_NAME` to `target.asset.hostname`.  
\- Mapped `targetHost` to `target.asset.hostname`.   
2023-10-17 |  Bug-Fix :  
\- Added IP check before mapping `IP` to `principal.ip`.  
\- Added IP check before mapping `CLIENT_IP_ADDRESS` to `target.ip`.  
\- Added validation check for `ACCOUNT_SID` before mapping to `principal.group.windows_sid`.  
\- Added validation check for `CALLER_USER_SID` before mapping to `target.group.windows_sid`.  
\- When `principal` is present, set `event_type` to `STATUS_UPDATE`.  
\- Modified a Grok pattern to parse `file_path` from new pattern of `FORMAT_MESSAGE`.  
\- Added a check for `has_target_resource` when `event_type` is `SCHEDULED_TASK_CREATION`.   
2023-03-17 |  Enhancement :  
\- Supported CEF format logs and mapped the following fields:  
\- `IP` mapped to `principal.ip`.  
\- `LOGIN NAME` mapped to `target.user.userid or target.user.email_addresses or target.user.user_display_name`.  
\- `DOMAIN NAME` mapped to `principal.administrative_domain`.  
\- `HOST` mapped to `principal.hostname`.  
\- `ACCESS_MODE` mapped to `security_result.detection_fields`.  
\- `STATUS` mapped to `security_result.summary`.  
\- If `STATUS` is `success` then `security_result.action` mapped to `ALLOW` else if `STATUS` is `denied or incorrect` then `security_result.action` mapped to `BLOCK`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
