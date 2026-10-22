---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pta-changelog/
title: Change log for CYBERARK_PTA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:49.627999+00:00
---

# Change log for CYBERARK_PTA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cyberark-pta-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CYBERARK_PTA

Date | Changes  
---|---  
2026-07-28 |  Enhancement:  
\- Added grok pattern matching on `temp_data` to extract `timestamp` and `inter_ip` from syslog headers in CEF log entries.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `deviceCustomDate1` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` when principal machine data and has target user are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when principal host is present.   
2026-06-22 |  Enhancement:  
-`event.idm.read_only_udm.security_result.description`: Removed mapping of `suspiciousSessionActivity` from `event.idm.read_only_udm.security_result.description` UDM field since `suspiciousSessionActivity` raw log field represents executed command.  
-`event.idm.read_only_udm.target.process.command_line`: Mapped `suspiciousSessionActivity` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.   
2026-05-28 |  Enhancement:  
\- Added grok pattern to support LEEF log format.  
\- `event.idm.read_only_udm.metadata.id`: Newly mapped `leef_eventid` raw log field with `event.idm.read_only_udm.metadata.id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `eventID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `leef_version` raw log fields with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `vendor_data` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `devTime` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `suser` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `usrName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `inter_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.about.url`: Newly mapped `externalLink` raw log field with `event.idm.read_only_udm.about.url` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `Cat` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `suspiciousSessionActivity` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `sev` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.url_back_to_product`: Newly mapped `ptaLink` raw log field with `event.idm.read_only_udm.security_result.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `externalLinkLabel`, `suspiciousSessionActivityLabel`, `eventIdLabel`, `linkLabel`, `suserLabel`, `extraDataLabel`, `extraData`,`prod_version` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` and `USER_UNCATEGORIZED` when necessary raw log fields are present.   
2024-08-13 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
