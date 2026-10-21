---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lastpass-changelog/
title: Change log for LASTPASS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:13:43.669910+00:00
---

# Change log for LASTPASS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/lastpass-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for LASTPASS

Date | Changes  
---|---  
2026-05-11 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `lastpass_raw.IP_Address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `principal.user.userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `lastpass_raw.Username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `target.resource.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `lastpass_raw.Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `lastpass_raw.Action` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `lastpass_raw.Data` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `additional.fields`, `metadata.product_event_type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `security_result.detection_fields` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Updated the naming convention to avoid conflict with raw log fields:  
\- Changed the naming convention from `security_result` to `event_security_result`.  
\- Changed the naming convention from `additional` to `event_additional`.  
\- Changed the naming convention from `target` to `event_target`.  
\- Changed the naming convention from `principal` to `event_principal`.  
\- Changed the naming convention from `metadata` to `event_metadata`.   
2025-05-29 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly Mapped `Datetime` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM Field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly Mapped `UserId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM Field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly Mapped `UserId` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM Field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly Mapped `ActionText` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM Field.  
\- `event.idm.read_only_udm.security_result.description`: Newly Mapped `Event` raw log field with `event.idm.read_only_udm.security_result.description` UDM Field.  
\- `event.idm.read_only_udm.network.session_id`: Newly Mapped `VID` raw log field with `event.idm.read_only_udm.network.session_id` UDM Field.  
\- `event.idm.read_only_udm.principal.ip`: Newly Mapped `Ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly Mapped `Ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM Field.  
\- `event.idm.read_only_udm.additional.fields.key`: Newly Mapped `EventType` raw log field with `event.idm.read_only_udm.additional.fields.key` UDM Field.   
2024-03-22 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
