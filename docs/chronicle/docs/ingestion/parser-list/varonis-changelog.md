---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/varonis-changelog/
title: Change log for VARONIS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:32.486313+00:00
---

# Change log for VARONIS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/varonis-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VARONIS

Date | Changes  
---|---  
2026-07-21 |  Enhancement:  
\- Added support for new pattern of Syslog and JSON logs by adding new grok patterns.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `alertid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `alert_title` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `affobj` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: When `evtstatus` is `Success`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `alerturl`, `alert_category`, `alert_component` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `alert_summary` log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `alert_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_details` log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `desc` log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `file_url` log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `user_domain` log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `dvcip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`: When `alert_title` matches `Executive access to sensitive files` or `Abnormal download of sensitive data` and `filepath` is not null, updated the value of `event.idm.read_only_udm.metadata.event_type` to `FILE_OPEN`.   
2026-06-05 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `datetime` log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `target_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `process` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dvchost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `evt_typ` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `cs2` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field, when `cs2Label` is `RuleName`.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `cn1` to `event.idm.read_only_udm.security_result.rule_id`, when `cn1Label` is `RuleID`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `uid`, `suid`, `sha256`, `sequence_num`, `record_num`, `datetime2`, `appname`, `cs2`, `cn1`, `cs3`, `cs4`, `cs5`, `cs6`, `facility`, `priority`, `mnemonic`, `cnt`, `disconnected_code` raw log fields.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `oldFilePermission`, `filePermission` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when both principal and target machine data is present.  
\- Added the Grok patterns to parse new pattern of SYSLOG logs.   
2026-03-18 |  \- `event.idm.read_only_udm.target.file.names`: Newly mapped `fname` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `cs7` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field when `cs7Label` is `AlertUrl`  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `device_product` log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.   
2025-10-08 |  \- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `fname` raw log field to `event.idm.read_only_udm.target.file.full_path`.'  
\- Modified severity mapping logic for `event.idm.read_only_udm.security_result.severity` to better categorize raw `sev` and `severity` values into `CRITICAL`, `HIGH`, `MEDIUM`, and `LOW`.  
\- Updated `event.idm.read_only_udm.security_result.severity` to `LOW` when `sev` or `severity` is `5`, `6`, `7`, `informational`, `INFORMATIONAL`, `NOTICE`, `DEBUG` or `LOW` instead of `0`, `1`, `2`, `3`, `LOW` previously.  
\- Updated `event.idm.read_only_udm.security_result.severity` from `INFORMATIONAL` to `LOW` when `sev` or `severity` is `informational`, `INFORMATIONAL` previously.  
\- Updated `event.idm.read_only_udm.security_result.severity` to `MEDIUM` when `sev` or `severity` is `3`,`4`, `ERROR`, `WARNING` or `MEDIUM` instead of `4`, `5`, `6`, `MEDIUM` previously.  
\- Updated `event.idm.read_only_udm.security_result.severity` to `HIGH` when `sev` or `severity` is `2`, `ALERT` or `HIGH` instead of `7`, `8`, `HIGH` previously.  
\- Removed `event.idm.read_only_udm.security_result.severity` to `CRITICAL` when `8`, `9`, `10`, `VERY-HIGH`,`CRITICAL`.  
\- Refined email recipient parsing by adding regex validation `(^.+@.+$)` for `Email_Recipients` and `mailRecipient` fields before mapping to `event.idm.read_only_udm.network.email.to`.  
\- Updated `FILE_OPEN` event type detection to also trigger when the `fname` field is present.   
2025-09-04 |  \- Added a new Grok pattern to parse `CEF` pattern syslog logs.   
2025-08-25 |  \- Added a new Grok pattern to parse `LEEF` pattern syslog logs.   
2025-02-06 |  \- Added a new Grok pattern for `LEEF` log type.  
\- Mapped `description` to `metadata.description`.  
\- Mapped `usrName` to `principal.user.userid`.  
\- Mapped `Event_Type` to `metadata.product_event_type`.  
\- Mapped `domain` to `prinicipal.administrative_domain`.  
\- Mapped `proto`, `cat`, `Event_Additional_Data`, `Event_Status`, `Email_Attachment_Name`, `Email_Date`, `Account_of_Changed_Permissions`, `Permissions_Changes`, `Permissions_before_Change`, and `Permissions_after_Change` to `additional.fields`.  
\- Mapped `Affected_Object_Path` to `taregt.file.full_path`.  
\- Mapped `Affected_Object` to `security_result.detection_fields`.  
\- Mapped `src` to `principal.ip` and `principal.assest.ip`.  
\- Mapped `Alert_ID` to `security_result.rule_id`.  
\- Mapped `Email_Recipients` to `network.email.to`.  
\- Mapped `Email_Item`, `Mailbox_Access_by_Owner`, `Threshold_Value`, `Threshold_First_Timestamp`, `Event_by_MailboxOwner`, and `Email_Sender` to `additional.fields`.  
\- Mapped `Email_Sender` to `network.email.from`.  
\- Mapped `accountName` to `target.user.userid`.  
\- Mapped `Device_Name` to `taregt.hostname` and taregt.asset.hostname".  
\- Mapped `Event_Type_ID` to `metadata.product_log_id`.  
\- Mapped `Event_File_Server_Domain` to `target.administrative_domain`.  
\- Mapped `Alert_Page_URL` to `taregt.url`.  
\- Mapped `devTime` to `metadata.event_timestamp`.  
\- Mapped `sev` to `security_result.severity`.   
2022-10-08 |  \- Added grok pattern for `LEEF` log type.  
\- Mapped `severity` to `security_result.severity`.  
\- Mapped `device_version` to `metadata.product_version`.  
\- Mapped `administrative_domain` to `target.administrative_domain`  
\- Added conditional check for `intermediary_host`.   
2022-10-07 |  Bug-Fix:  
\- Mapped `rt` to `metadata.event_timestamp` if `rt` is not null.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
