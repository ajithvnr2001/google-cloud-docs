---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-email-security-changelog/
title: Change log for CISCO_EMAIL_SECURITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:56.856149+00:00
---

# Change log for CISCO_EMAIL_SECURITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-email-security-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_EMAIL_SECURITY

Date | Changes  
---|---  
2026-09-07 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Mapped `inter_host` to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `shost` from `event.idm.read_only_udm.additional.fields` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Mapped `shost` to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `ExternalMsgID` from `event.idm.read_only_udm.security_result.about.labels` UDM field in order to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.network.email.mail_id`: Mapped `ExternalMsgID` raw log field to `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.   
2026-07-08 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `appname`, `priority`, `cef_version`, `facility` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.   
2026-06-11 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `cef_event` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `cef_sev_details` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_tag`, `shost` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified the grok patterns to parse the raw log fields.  
\- Added support for field name to parse metadata.event_timestamp correctly.   
2026-03-30 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `properties.host` raw log field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `properties.ip` raw log field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check for setting event.idm.read_only_udm.metadata.event_type to STATUS_UPDATE.  
\- Added an ip check before mapping `src` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`, which also maps the following fields:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.email.from`  
\- `event.idm.read_only_udm.network.email.reply_to`  
\- `event.idm.read_only_udm.network.email.subject`  
\- `event.idm.read_only_udm.network.email.to`  
\- `event.idm.read_only_udm.principal.asset.asset_id`  
\- `event.idm.read_only_udm.principal.asset_id`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.detection_fields.key`  
\- `event.idm.read_only_udm.security_result.detection_fields.value`  
\- `event.idm.read_only_udm.security_result.summary`.   
2025-12-12 |  Enhancement:  
\- Modified Grok patterns to parse the logs in the correct manner.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `deviceInboundInterface` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-09-26 |  Enhancement:  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` : Removed the mapping of `dvc` raw log with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` : Mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.ip` : Removed the mapping of `ESAHeloIP` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` : Mapped `ESAHeloIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp` : Newly mapped `startTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `endTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added new grok pattern for the `message` field to parse the dropped logs and map all the raw fields to the respective UDM fields.   
2025-09-17 |  Enhancement:  
\- Modified grok pattern for `ESAAttachmentDetails` to handle additional fields in log formats.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ESADKIMVerdict`, `ESADMARCVerdict`, and `SDRRepScore` raw log fields to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `result` and `sender` raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `Verdict` raw log field to event.idm.read_only_udm.security_result.summary.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `ESATLSInConnStatus` raw log field to event.idm.read_only_udm.security_result.description.   
2025-08-16 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `deviceDirection` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a grok pattern to match the field `start` to match the timestamp.  
\- Added a grok pattern for `message`.   
2025-07-24 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `ESAOFVerdict` , `ESADLPVerdict` , `ESAMFVerdict` , `ESATLSOutConnStatus` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Updated mapped `ts_year` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-05-29 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `start` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `shost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `shost` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `ESAMailFlowPolicy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.metadata.additional.fields: Newly mapped `ESAAMPVerdict`, `ESAASVerdict`, `ESAAVVerdict`, `ESACFVerdict`, `ESAGMVerdict`, `deviceOutboundInterface`, `end`, `ESAMsgSize`, `cfp1Label`, and `cfp1` raw log fields with `event.idm.read_only_udm.metadata.additional.fields` UDM field.   
2025-04-16 |  Enhancement:  
\- Added Grok pattern to parse CEF:0 format of logs.  
\- Added ip check to `dvc` and `ESAHeloIP` before mapping them to UDM fields.  
\- Declared `inner_message` to null if it is empty.   
2025-01-23 |  Enhancement:  
\- Mapped `urls` and `WbrsScore` to `security_result.detection_fields`.   
2024-12-16 |  Enhancement:  
\- Added support for the new SYSLOG log pattern.  
\- Added a new Grok pattern for `inner_message`.  
\- Mapped `message_id2` to `network.email.mail_id`.  
\- Mapped `injection_connection_id` to `network.session_id`.  
\- Mapped `action` to `security_result.action_details`.  
\- Mapped `address_clean` to `network.email.to`.  
\- Mapped `receiver` to `network.email.to`.  
\- Added a condition check for the `from` field before mapping it to `network.email.from`.  
\- Mapped `reply_to` to `network.email.reply_to`.  
\- Added `on_error` for `gsub` function for `description`.  
\- Mapped `inner_message` to `metadata.description`.   
2024-10-30 |  Bug-Fix:  
\- Changed mapping of `host_msg` from `principal.hostname` to `intermediary.hostname`.  
\- When `host_msg` is an IP address, then mapped `host_msg` to `intermediary.ip`.   
2024-09-05 |  Enhancement:  
\- Mapped `host_msg` to `principal.hostname` and `principal.asset.hostname`.   
2023-10-05 |  Bug-Fix:  
\- Renamed the `product_event` from `amp` to `SIEM_AMPenginelogs`.   
2023-09-15 |  Enhancement:  
\- Added support for `SIEM_proxylogs`,`SIEM_webrootlogs`,`SIEM_AMPenginelogs` of json logs.   
2023-09-04 |  Enhancement  
\- Added a Grok pattern to parse unparsed logs and mapped the fields accordingly.  
\- Added support for new pattern of JSON logs.   
2022-12-16 |  Enhancement  
\- Modified conditional checks for the fields mapped to `network.email.to`, `network.email.from`, `principal.user.email_addresses`, `target.user.email_addresses` and `network.email.reply_to`.  
\- Added support for json logs :  
\- Mapped the field `host` to `principal.hostname`.  
\- Mapped the field `domain` to `target.administrative_domain`.  
\- Mapped the field `mail_id` to `network.email.mail_id`.  
\- Mapped the field `mailto` to `network.email.to` and `target.user.email_addresses`.  
\- Mapped the field `source` to `network.ip_protocol`.  
\- Mapped the field `reputation` to `security_result.confidence_details`.  
\- Mapped the field `log_type` to `security_result.severity` and `security_result.severity_details`.  
\- Mapped the field `cribl_pipe` to `additional.fields`.   
2022-09-22 |  Enhancement  
\- Added a grok pattern for unparsed logs, having the field `product_event` as empty.   
2022-08-02 |  Enhancement  
\- Added conditions for newly added event_type `STATUS_UPDATE`, `USER_UNCATEGORIZED`, `SCAN_PROCESS`  
\- Mapped `attack` to `security_result.category_details`  
\- Enahanced parser to parse `ESAAttachmentDetails` field of different types of logs.   
2022-06-09 |  Enhancement- Mapped `from_user` to `principal.user.user_display_name`.  
\- Updated `metadata.product_event_type` from `Consolidated Log Event` to `ESA_CONSOLIDATED_LOG_EVENT`.   
2022-06-07 |  Enhancement- Mapped suser to network.email.bounce_address.   
2022-05-17 |  Enhancement - Mapped duser to network.email.to.  
\- Added on_error for product_version and product_description fields to avoid null value mapping to UDM.  
\- Added additional logic to parse logs starting with `DAY TIMESTAMP YEAR` format, for example: Wed Feb 18 00:34:12 2021.   
2022-05-05 |  Enhancement-Used grok for network.email.from   
2022-03-31 |  Enhancement-Added mappings for new fields.  
\- ESAReplyTo mapped to network.email.reply_to.  
\- duser mapped to network.email.to.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
