---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-dlp-changelog/
title: Change log for DIGITALGUARDIAN_DLP \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:45.262679+00:00
---

# Change log for DIGITALGUARDIAN_DLP  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/digitalguardian-dlp-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for DIGITALGUARDIAN_DLP

Date | Changes  
---|---  
2025-03-27 |  \- `SYSLOG+XML`: Added support for `SYSLOG+XML` format.  
\- Added a new Grok pattern to support XML logs.  
\- Added gsub to replace `metadata` with `meta_data`.  
\- Added gsub to replace `:m` and `m:` with ``.  
\- Added XML filters to parse unparsed XML logs.  
\- event.idm.read_only_udm.network.email.to: Newly mapped `recipient_address` raw log field with `event.idm.read_only_udm.network.email.to` UDM field if `recipient_type` is `To` or `TO`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `recipient_name` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field if `recipient_type` is `To` or `TO`.  
\- event.idm.read_only_udm.network.email.from: Newly mapped `recipient_address` raw log field with `event.idm.read_only_udm.network.email.from` UDM field if `recipient_type` is `Resource`.  
\- event.idm.read_only_udm.target.user.attribute.labels: Newly mapped `recipient_name` raw log field with `event.idm.read_only_udm.target.user.attribute.labels` UDM field if `recipient_type` is `Resource`.  
\- event.idm.read_only_udm.network.email.cc: Newly mapped `recipient_address` raw log field with `event.idm.read_only_udm.network.email.cc` UDM field if `recipient_type` is `CC`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `recipient_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if `recipient_type` is `CC`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `attachment_display_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `attachment_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Classification` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Classification_value` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `xmlns_m` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Configuration` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Host_Product_Version` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Host_Product` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Item_Type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `Product_Version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `Product_Edition` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `Product_Name` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `McAfee_product_code` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `os` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `WINDOWS` raw log field with `event.idm.read_only_udm.principal.platform` UDM field if the `os` field contains `Windows`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `machine_name` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `source` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added a Grok pattern to extract `ipv6`.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `ipv6` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `ipv4` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `machine` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `eventtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `date_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- Added a conditional check before adding drop tag.  
\- Added `on_error` check where `Application` is mapped to `event.idm.read_only_udm.principal.process.command_line`.  
\- Added `on_error` check where `parent_application` is mapped to `event.idm.read_only_udm.principal.process.parent_process.command_line`.  
\- Added a conditional check before mapping `command_line` to `event.idm.read_only_udm.target.process.command_line`.  
\- Added a `on_error` check where `Unique ID` is mapped to `event.idm.read_only_udm.metadata.product_log_id`.  
\- Added a `on_error` check where `DigitalGuardian` is mapped to `event.idm.read_only_udm.metadata.vendor_name`.  
\- Added a conditional check where `event.idm.read_only_udm.metadata.event_type` is mapped to `FILE_UNCATEGORIZED`.  
\- Added a conditional check where `event.idm.read_only_udm.metadata.event_type` is mapped to `NETWORK_UNCATEGORIZED`.  
\- Added a conditional check where `event.idm.read_only_udm.metadata.event_type` is mapped to `PROCESS_UNCATEGORIZED`.  
\- Added a conditional check to set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.   
2023-06-02 |  \- Changed mapping for the field `dg_recipients.uad_mr` from `src.user.email_addresses` to `network.email.to`.   
2022-11-30 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
