---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kolide-changelog/
title: Change log for KOLIDE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:37.408260+00:00
---

# Change log for KOLIDE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kolide-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KOLIDE

Date | Changes  
---|---  
2026-02-27 |  \- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `kolide_event.filePath` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.asset_id`: Newly mapped `kolide_event.h_uuid` raw log field with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `kolide_event.log_message` and `kolide_event.data.description` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `kolide_event.data.actor_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `kolide_event.data.ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `kolide_event.createdAt`, `kolide_event.itemId`, `kolide_event.unixTime` and `kolide_event.s_number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `kolide_event.data.actor_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `kolide_event.data.actor_type` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- Converted `kolide_event.kolide_decorations.device_id` type to string which resulted in mapping of `kolide_event.kolide_decorations.device_id` raw log field with `event.idm.read_only_udm.principal.asset.labels` UDM field.   
2026-01-16 |  \- event.idm.read_only_udm.target.resource.name: Newly mapped `added_name` raw log field to `event.idm.read_only_udm.target.resource.name` udm field.  
\- event.idm.read_only_udm.principal.asset.labels: Newly mapped `added_version` raw log field to `event.idm.read_only_udm.principal.asset.labels` udm field.  
\- event.idm.read_only_udm.principal.asset.labels: Newly mapped `added_installed_at_epoch` raw log field to `event.idm.read_only_udm.principal.asset.labels` udm field.  
\- event.idm.read_only_udm.principal.asset.labels: Newly mapped `added_locale` raw log field to `event.idm.read_only_udm.principal.asset.labels` udm field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `added_description` raw log field to `event.idm.read_only_udm.metadata.description` udm field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `added_path` raw log field to `event.idm.read_only_udm.target.file.full_path` udm field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `added_permissions` raw log field to `event.idm.read_only_udm.security_result.detection_fields` udm field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `referenced_by_preferences` raw log field to `event.idm.read_only_udm.security_result.detection_fields` udm field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `added_identifier` raw log field to `event.idm.read_only_udm.security_result.detection_fields` udm field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `added_persistent` raw log field to `event.idm.read_only_udm.security_result.detection_fields` udm field.  
\- event.idm.read_only_udm.target.application: Newly mapped `added_browser_type` raw log field to `event.idm.read_only_udm.target.application` udm field.  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `added_manifest_hash` raw log field to `event.idm.read_only_udm.target.file.md5` udm field.  
\- event.idm.read_only_udm.target.user.role_name: Newly mapped `added_profile` raw log field to `event.idm.read_only_udm.target.user.role_name` udm field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `added_uid` raw log field to `event.idm.read_only_udm.target.user.userid` udm field.  
\- event.idm.read_only_udm.target.url: Newly mapped `added_url` raw log field to `event.idm.read_only_udm.target.url` udm field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `epoch` raw log field to `event.idm.read_only_udm.additional.fields` udm field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `type` raw log field to `event.idm.read_only_udm.additional.fields` udm field.   
2025-01-29 |  \- Added a new Grok pattern to `calendarTime`.  
\- Mapped `calendarTime` to `metadata.event_timestamp`.   
2023-10-25 |  \- Mapped `decorations.hostname` to `principal.asset.hostname`.  
\- Changed `principal_asset_name` mapping from `principal.asset.hostname` to `additional.fields`.   
2023-10-13 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
