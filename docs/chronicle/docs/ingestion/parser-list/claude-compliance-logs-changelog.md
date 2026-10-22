---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claude-compliance-logs-changelog/
title: Change log for CLAUDE_COMPLIANCE_LOGS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:41.310399+00:00
---

# Change log for CLAUDE_COMPLIANCE_LOGS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/claude-compliance-logs-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLAUDE_COMPLIANCE_LOGS

Date | Changes  
---|---  
2026-09-09 |  \- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `created_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-08-05 |  \- Added support for the new format of JSON and Syslog + JSON logs.  
\- `event1.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `data_value.created_at` raw log field with `event1.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event1.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event1.idm.read_only_udm.target.url` UDM field.  
\- `event1.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event1.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event1.idm.read_only_udm.network.http.method`: Newly mapped `request_method` raw log field with `event1.idm.read_only_udm.network.http.method` UDM field.  
\- `event1.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field with `event1.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip`: Newly mapped `actor.ip_address` raw log field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event1.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event1.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event1.idm.read_only_udm.network.http.user_agent` and `event1.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `actor.user_agent` raw log field with `event1.idm.read_only_udm.network.http.user_agent` and `event1.idm.read_only_udm.network.http.parsed_user_agent` UDM fields.  
\- `event1.idm.read_only_udm.additional.fields`: Newly mapped `request_body`, `organization_id`, `organization_uuid`, `request_id`, `actor_type`, `actor_api_key_id`, `has_more`, `first_id`, and `last_id` raw log fields with `event1.idm.read_only_udm.additional.fields` UDM field.   
2026-07-17 |  \- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `chat.user.id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `chat.user.email_address` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `message.id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `message.role`, `message.created_at`, `message.content.truncated`, `message.content.text`, and `message.content.type` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `chat.created_at`, `chat.updated_at`, `chat.project_id`, `chat.organization_id`, and `chat.organization_uuid` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `chat.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `chat.name` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.ingestion_labels`: Newly mapped `_metadata.source`, `_metadata.collector`, and `_metadata.version` raw log fields with `event.idm.read_only_udm.metadata.ingestion_labels` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `_metadata.collection_timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.about.resource.product_object_id`: Newly mapped `message.files.id` raw log field with `event.idm.read_only_udm.about.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.about.file.full_path`: Newly mapped `message.files.filename` raw log field with `event.idm.read_only_udm.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Newly mapped `message.files.mime_type` raw log field with `event.idm.read_only_udm.about.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.file.size`: Newly mapped `message.files.size_bytes` raw log field with `event.idm.read_only_udm.about.file.size` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `message.files.created_at` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal user data is present and both `chat.id` and `message.id` are not null, set `event.idm.read_only_udm.metadata.event_type` to `USER_COMMUNICATION`.   
2026-06-26 |  \- Initialized the `ingested_at` and `timestamp` raw log fields to an empty string in the state data to prevent potential errors.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Mapped `actor.user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.   
2026-05-18 |  \- Newly created parser.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `ingested_at` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `name`, and `chat_name` raw log fields with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_email_address`, `user_email`, `actor_user_email`, `email_address`, `actor_unauthenticated_email_address`, and `actor_unauthenticated_email_adds` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: if `type` is `sso_login_initiated` then Newly mapped `actor_unauthenticated_email_address`, and `actor_unauthenticated_email_adds` raw log fields with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `actor_ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `actor_ip_address` raw log field with `event.idm.read_only_udm.target.ip` and UDM fields when `type` is `sso_login_initiated`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor_user_id`, and `user_id` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.role_name`: Newly mapped `role` raw log field with `event.idm.read_only_udm.principal.user.role_name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `source_type` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `path`, and `file_path` raw log fields with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `filename` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- `event.idm.read_only_udm.target.file.size`: Newly mapped `size_bytes` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `mime_type`, and `content_type` raw log fields with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `claude_chat_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `skill_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `actor_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `request_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.about.file.mime_type`: Newly mapped `artifacts_artifact_type` raw log field with `event.idm.read_only_udm.about.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.about.resource.product_object_id`: Newly mapped `artifacts_id` raw log field with `event.idm.read_only_udm.about.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.about.file.names`: Newly mapped `artifacts_title` raw log field with `event.idm.read_only_udm.about.file.names` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `created_at`, `content_type`, `content_text`, `updates.current_value`, `updates.previous_value`, `updates.type`, `request_body`, `request_id`, `actor_type`, `gso_log_type`, `updated_at`, `deleted_at`, `claude_project_id`, `chat_id`, `file_id`, and `actor.api_key_id`,`organization_name' raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `organization_id`, `organization_uuid` , `project_id`, `project_name` and `environment` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `integration_type`, `skill_id`, and `claude_file_id` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`when principal user and principal machine are present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when target user and target machine details are present and `type` is `sso_login_initiated`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
