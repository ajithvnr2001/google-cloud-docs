---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teamviewer-changelog/
title: Change log for TEAMVIEWER \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:03.684578+00:00
---

# Change log for TEAMVIEWER  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teamviewer-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TEAMVIEWER

Date | Changes  
---|---  
2025-12-01 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Removed mapping of `AffectedItem` from `event.idm.read_only_udm.metadata.product_log_id` UDM field in order to introduce a more accurate mapping.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `AffectedItem` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- Updated on_error for `details.PropertyName`, `details.PropertyCategory`, `details.NewValue`, `details.OldValue` raw log fields with `no_property_name`, `no_property_category`, `no_new_value` and `no_old_value` to handle null values.   
2025-11-19 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Author` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `AuthorEmail` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `AffectedItem` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EventType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `details.PropertyName`, `details.PropertyCategory`, `details.NewValue`, `details.OldValue` raw log field(s) with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.group.group_display_name`: Newly mapped `details.NewValue` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.target.group.product_object_id`: Newly mapped `details.NewValue` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `details.NewValue` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `details.NewValue` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `has_target` is `true` or `src_user_present` is `true`, updated to `USER_UNCATEGORIZED`.   
2024-10-30 |  Enhancement:  
\- Added support for the new log format.   
2022-08-02 |  Enhancement:  
\- Added grok to avoid mapping of invalid value in `target.user.user_display_name`  
\- Changed the field `metadata.event_type` from `GENERIC_EVENT` to `USER_UNCATEGORIZED` and `USER_RESOURCE_ACCESS`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
