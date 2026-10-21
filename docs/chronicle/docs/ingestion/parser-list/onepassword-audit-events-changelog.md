---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-audit-events-changelog/
title: Change log for ONEPASSWORD_AUDIT_EVENTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T01:32:40.417823+00:00
---

# Change log for ONEPASSWORD_AUDIT_EVENTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-audit-events-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONEPASSWORD_AUDIT_EVENTS

Date | Changes  
---|---  
2026-05-11 |  Enhancement:  
\- Added support for JSON format logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor_details.uuid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actor_details.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `actor_details.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `session.ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `session.device_uuid` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.location.city`: Newly mapped `location.city` raw log field with `event.idm.read_only_udm.principal.location.city` UDM field.  
\- `event.idm.read_only_udm.principal.location.state`: Newly mapped `location.region` raw log field with `event.idm.read_only_udm.principal.location.state` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `location.country` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.latitude`: Newly mapped `location.latitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- `event.idm.read_only_udm.principal.location.region_coordinates.longitude`: Newly mapped `location.longitude` raw log field with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `object_uuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session.uuid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the event type to `USER_UNCATEGORIZED`, `STATUS_UPDATE`, `GENERIC_EVENT` based on the required data.  
\- Added on_error condition to drop non-JSON format logs with tag `TAG_MALFORMED_MESSAGE`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `aux_uuid` and `object_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `account_uuid` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `actor_type` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `action` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.last_login_time`: Newly mapped `session.login_time` raw log field with `event.idm.read_only_udm.principal.user.last_login_time` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `actor_uuid` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.   
2025-02-17 |  \- Fixed issue for parsing `aux_info`.  
\- Mapped `item.timestamp` to `metadata.event_timestamp`.   
2024-11-06 |  \- Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
