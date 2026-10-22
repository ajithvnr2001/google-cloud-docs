---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zoom-operation-logs-changelog/
title: Change log for ZOOM_OPERATION_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:47.469442+00:00
---

# Change log for ZOOM_OPERATION_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zoom-operation-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZOOM_OPERATION_LOGS

Date | Changes  
---|---  
2026-09-21 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `payload.object.topic` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `payload.object.host_id` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.object.start_time`, `payload.object.duration`, `payload.object.timezone`, `payload.object.uuid`, `payload.object.participant.join_time` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `payload.object.participant.user_name` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `payload.object.participant.user_id`, `payload.object.participant.participant_user_id` raw log fields to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `payload.object.participant.public_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `payload.object.participant.participant_uuid`, `payload.object.participant.id` raw log fields to `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `payload.object.participant.email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Sets `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` and `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED` when both (`has_target_user` or `has_principal_user`) and `has_principal` evaluating flags are true.   
2026-07-14 |  Enhancement:  
\- Added a Grok pattern for the `operation_detail` field to support the new JSON+Syslog log format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `zoom_action`, `device_serial_number`, `old_company_id`, `old_company_name`, `new_company_name`, `new_company_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field as key-value pairs.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `device_name` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.asset_id`, `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `device_id` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM fields.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `device_platform` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action_result` raw log field with `event.idm.read_only_udm.security_result.action` UDM field if it contains a valid UDM action value.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action_result` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `action_status` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If principal machine data is present, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_HEARTBEAT`.   
2025-11-06 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Removed mapping of `payload_object_status_id`,`payload_object_status_name` from `event.idm.read_only_udm.target.user.attribute.labels` as this is mapped to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `payload_object_status_id`, `payload_object_status_name`,`account_id` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Conditional value mapping added for `payload_object_login_type`: The raw value `101` is now mapped to the string `Native Login (Non-SSO)` within `event.idm.read_only_udm.additional.fields`.   
2025-10-10 |  Enhancement:  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `payload.object.settings.chat.allow_users_to_chat_with_others.enable`, `payload.old_object.settings.chat.allow_users_to_chat_with_others.enable` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels`.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `payload.account_id` raw log field to `event.idm.read_only_udm.principal.group.product_object_id`.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `payload.account_id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id`.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `payload.operator`, `payload.object.email` raw log field to `event.idm.read_only_udm.principal.user.email_addresses`.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `payload.operator_id`, `payload.object.id` raw log field to `event.idm.read_only_udm.principal.user.product_object_id`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.creation_type`, `payload.object.login_type`, `payload.object.date_time`, `payload.object.date_time_ms`, `payload.object.user_access`, `payload.object.channel_settings.concurrent_message_capacity`, `payload.object.channel_settings.multi_channel_engagements.enable`, `payload.object.channel_settings.multi_channel_engagements.max_agent_load` and `payload.time_stamp` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `payload.object.id` raw log field to `event.idm.read_only_udm.target.user.product_object_id`.  
\- `event.idm.read_only_udm.target.user.first_name`: Newly mapped `payload.object.first_name` raw log field to `event.idm.read_only_udm.target.user.first_name`.  
\- `event.idm.read_only_udm.target.user.last_name`: Newly mapped `payload.object.last_name` raw log field to `event.idm.read_only_udm.target.user.last_name`.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `payload.object.client_type` raw log field to `event.idm.read_only_udm.principal.application`.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `payload.object.email`, `payload.object.user_email` raw log field to `event.idm.read_only_udm.target.user.email_addresses`.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `payload.object.role_id`, `payload.object.status_id`, `payload.object.status_name`, `payload.object.type` raw log field to `event.idm.read_only_udm.target.user.attribute.labels`.  
\- `event.idm.read_only_udm.target.user.role_name`: Newly mapped `payload.object.role_name` raw log field to `event.idm.read_only_udm.target.user.role_name`.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `payload.object.country_iso_code` raw log field to `event.idm.read_only_udm.target.location.country_or_region`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Zoom` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Mapped to `SSO` if `payload.object.login_type` is `100` during login, otherwise mapped to `AUTHTYPE_UNSPECIFIED`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `payload.object.user_id` raw log field to `event.idm.read_only_udm.target.user.userid`.  
\- event.idm.read_only_udm.metadata.event_type: Mapped to USER_CREATION (for `user.created`), USER_DELETION (for `user.deleted`), USER_LOGIN (for `user.signed_in`) and USER_UNCATEGORIZED (for other user-related events).   
2025-01-20 |  Enhancement:  
\- Mapped `ip_address` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `client_type` to `additional.fields`.  
\- Mapped `type` to `additional.fields`.  
\- Mapped `version` to `metadata.product_version`.   
2024-11-21 |  Enhancement:  
\- Added support for the array format of the logs.   
2022-11-04 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
