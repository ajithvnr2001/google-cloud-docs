---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-audit-changelog/
title: Change log for TANIUM_AUDIT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:05.098974+00:00
---

# Change log for TANIUM_AUDIT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tanium-audit-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TANIUM_AUDIT

Date | Changes  
---|---  
2025-11-13 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.last_update_time`: Removed mapping of `modification_time` from `event.idm.read_only_udm.target.resource.attribute.last_update_time` UDM field as `modification_time` represents the event's time, not a resource attribute.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `modification_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `state.type` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `state.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly `mapped state.legacyType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `userId` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `table`, `username` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `rowId`, `revision`, `state.count`, `updatedAt`, `personaId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-05-16 |  Enhancement:  
\- Added support for JSON logs.  
\- Mapped `object_id` to `target.resource.product_object_id`.  
\- Mapped `object_name` to `target.resource.name`.  
\- Mapped `audit_name` to `metadata.description`.  
\- Mapped `creation_time` to `target.resource.attribute.creation_time`.  
\- Mapped `modification_time` to `target.resource.attribute.last_update_time`.  
\- Mapped `last_modified_by` and `modifier_user_id` to `principal.resource.attribute.labels`.  
\- Mapped `User` to `principal.user.userid`.  
\- Mapped `session_id` to `network.session_id`.  
\- Mapped `authentication_type` to `principal.user.attribute.labels`.  
\- Mapped `ip_address` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `audit_row_id`, `type`, and `audit_type` to `additional.fields`.  
\- Mapped `type_name` to `metadata.product_event_type`.  
\- Mapped `object_type_name` to `target.resource.attribute.labels`.   
2023-09-26 |  Enhancement:  
\- Added `on_error` check for date filter.  
\- Added a Grok pattern to support new log format.  
\- Mapped `Issuer`, `ActionName`, `PackageName`, `StartTime`, `Expiration`, `InsertTime` and `DistributeOver` to `additional.fields`.   
2022-06-08 |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
