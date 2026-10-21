---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-changelog/
title: Change log for ONEPASSWORD \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:43:11.979565+00:00
---

# Change log for ONEPASSWORD  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/onepassword-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ONEPASSWORD

Date | Changes  
---|---  
2025-10-01 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `items.details`, `has_more` and `cursor` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Modified the date filter to explicitly set `target` to `event.idm.read_only_udm.metadata.event_timestamp` and added on_error handling.  
\-   
2025-07-16 |  Enhancement:  
\- Added a conditional check before mapping `item.aux_info` gsub ,to check if that is a object.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `lt` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.   
2025-07-03 |  Enhancement:  
\- Replace the value of `item.actor_details.uuid` in `item_actor_details_uuid`.  
\- Added a conditional check before mapping `item_actor_details_uuid` to `event.idm.read_only_udm.principal.user.userid`.   
2025-06-11 |  Enhancement:  
\- Replaced array format of `message` with a `msg` field.  
\- Added a json filter on `msg` field if `not_json` flag is true.  
\- Replaced `item.account_uuid` with `item_account_uuid`.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `item_account_uuid` field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- Replaced `item.actor_type` with `item_actor_type`.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `item_actor_type` field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- Added `has_user` flag before mapping `item.actor_details.uuid` to `event.idm.read_only_udm.principal.user.userid`.  
\- Added a conditional checks if `has_user` flag is equals to true and `event.idm.read_only_udm.metadata.event_type` is `STATUS_UPDATE` then map `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-07-08 |  Enhancement:  
\- Mapped `item.actor_details.uuid` to `principal.user.userid`.  
\- Mapped `item.actor_details.name` to `principal.user.user_display_name`.  
\- Mapped `item.actor_details.email` to `principal.email`.  
\- Mapped `item.actor_uuid` to `security_result.about.resource.attribute.labels`.  
\- Mapped `item.object_type` to `additional.fields`.  
\- Mapped `item.object_uuid` to `security_result.about.resource.attribute.labels`.  
\- Mapped `item.aux_info` to `additional.fields`.  
\- Mapped `item.aux_uuid` to `security_result.about.resource.attribute.labels`.  
\- Mapped `item.session.uuid` to `network.session_id`.  
\- Mapped `item.session.device_uuid` to `target.resource.product_object_id`.  
\- Mapped `item.session.ip` to `principal.ip`.   
2023-06-07 |  Enhancement:  
\- Remapped `target_user.name` to `target.user.user_display_name`.  
\- Remapped `target_user.email` to `target.user.email_addresses`.  
\- Remapped `target_user.uuid` to `target.user.userid`.  
\- If user fields are not present, changed `metadata.event_type` to `STATUS_UPDATE`.   
2023-05-05 |  Enhancement:  
\- Added gsub function to correct format and parse the unparsed logs.   
2023-04-27 |  Enhancement:  
\- Provided parsing support for multiple fields in `items` array by using loop.   
2023-02-15 |  Enhancement: Mapped/Modified the following fields-  
\- Unmapped `user.uuid` and `uuid`.  
\- Modified mapping of `target_user.email` from `target.user.userid` to `principal.user.email_addresses`.  
\- Modified mapping of `target_user.uuid` from `target.user.product_object_id` to `principal.user.userid`.   
2023-02-06 |  Enhancement:  
\- Mapped `metadata.vendor_name` and `metadata.product_name`.   
2023-01-15 |  Enhancement:  
\- Mapped `uuid` to `principal.userid`.  
\- If `user.uuid` and `uuid` are present then map `uuid` to `additional.fields`.  
\- Mapped `location.region` to `principal.location.name`.  
\- Mapped `metadata.product_version` to `client.app_version`.  
\- Mapped `principal.asset.platform_software.platform_version` to `client.platform_version`.  
\- Mapped `type`,`action`,`used_version`,` to `additional.fields".  
\- Mapped `client.platform_name` to `principal.resource.attribute.labels`.  
\- Mapped `vault_uuid` to `security_result.about.resource.attribute.labels`.  
\- Mapped `country` to `principal.location.country_or_region`.  
\- If `category` is equal to `success`, then map `security_result.action` to `ALLOW`.  
\- Mapped `category` to `security_result.category_details`.  
\- Re-Mapped `target_user.email` to `target.user.userid`.  
\- Re-Mapped `target_user.uuid` to `target.user.product_object_id`.  
\- Re-Mapped `item_uuid` to `about.resource.attribute.labels`.   
2022-10-07 |  Newly created parser   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
