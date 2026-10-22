---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-bitbucket-changelog/
title: Change log for ATLASSIAN_BITBUCKET \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:37.813065+00:00
---

# Change log for ATLASSIAN_BITBUCKET  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/atlassian-bitbucket-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ATLASSIAN_BITBUCKET

Date | Changes  
---|---  
2026-09-01 |  \- Added grok patterns to parse new format of syslogs.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `access_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `access_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `app_log_level` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: If `repo_path` is present, Set the value of `event.idm.read_only_udm.target.resource.resource_type` to `REPOSITORY`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `auditType.actionI18nKey`, `auditType.level`, `method`, `node`, `access_request_id`, `access_auth`, `access_duration`, `ssh_client_version`, `access_status`, `app_thread`, `app_request_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp.epochSecond`, `access_time` raw log fields with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`: Newly mapped `timestamp.nano` raw log field with `event.idm.read_only_udm.metadata.event_timestamp.nanos` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `author.id`, `access_user` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `author.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `author.name`, `access_user` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `author.type`, `extraAttributes.name`, `extraAttributes.value`, `extraAttributes.nameI18nKey` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `source`, `raw_client_ips` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `auditType.area`, `app_logger` raw log fields with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `auditType.category`, `auditType.categoryI18nKey` raw log fields with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `auditType.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `app_message` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `affectedObjects.id`, `affectedObjects.name`, `affectedObjects.type` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `system`, `http_url`, `app_http_url` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `access_session_id` raw log fields with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `access_bytes_in` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `access_bytes_out` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http_method` raw log fields with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `http_version` raw log fields with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `http_referer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `http_user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `access_status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `access_request` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `ssh_command` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `repo_path` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `app_log_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.   
2026-06-01 |  \- `event.idm.read_only_udm.security_result.summary`: Removed mapping of `security_summary` raw log field from `event.idm.read_only_udm.security_result.summary` UDM field when `security_summary` contains empty data.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `value1.links.commits.href`, `value1.links.diff.href`, `value1.links.html.href`, `value1.new.default_merge_strategy`, `value1.new.links.commits.href`, `value1.new.links.html.href`, `value1.new.links.pullrequest_create.href`, `value1.new.links.self.href`, `value1.new.name`, `value1.new.target.author.raw`, `value1.new.target.author.type`, `value1.new.target.author.user.account_id`, `value1.new.target.author.user.display_name`, `value1.new.target.author.links.avatar.href`, `value1.new.target.author.html.href`, `value1.new.target.author.self.href`, `value1.new.target.author.nickname`, `value1.new.target.author.user.type`, `value1.new.target.author.user.uuid`, `value1.old.default_merge_strategy`, `value1.old.links.commits.href`, `value1.old.links.html.href`, `value1.old.links.pullrequest_create.href`, `value1.old.links.self.href`, `value1.old.target.author.raw`, `value1.old.target.author.type`, `value1.old.target.hash`, `value1.old.target.links.html.href`, `value1.old.target.links.self.href`, `value1.old.target.message`, `value1.old.target.type`, `value1.closed`, `value1.created`, `value1.forced`, `value1.new.merge_strategies`, `value1.old.merge_strategies`, `value1.old.name`, `value1.name`, `value1.new.sync_strategies`, `value1.old.sync_strategies`, `value1.new.target.hash`, `value1.new.target.links.html.href`, `value1.new.target.links.self.href`, `value1.new.target.message`, `value1.new.target.summary.html`, `value1.new.target.summary.markup`, `value1.new.target.summary.raw`, `value1.new.target.summary.type`, `value1.new.target.type`, `value1.new.type`, `value1.old.target.summary.html`, `value1.old.target.summary.markup`, `value1.old.target.summary.raw`, `value1.old.target.summary.type`, `value1.old.type`, `value1.truncated`, `value1.new.target.author.user.links.avatar.href`, `value1.new.target.author.user.links.html.href`, `value1.new.target.author.user.self.href`, `value1.new.target.author.user.nickname`, `value2.author.raw`, `value2.author.type`, `value2.date`, `value2.hash`, `value2.links.approve.href`, `value2.links.comments.href`, `value2.links.diff.href`, `value2.links.patch.href`, `value2.links.self.href`, `value2.links.statuses.href`, `value2.message`, `value2.summary.html`, `value2.summary.markup`, `value2.summary.raw`, `value2.summary.type`, `value2.type`, `value3.hash`, `value3.links.html.href`, `value3.links.self.href`, `value3.type`, `repository.owner.links.self.href`, `repository.owner.links.avatar.href`, `repository.owner.links.html.href`, `repository.workspace.type`, `repository.workspace.uuid`, `repository.workspace.name`, `repository.workspace.slug`, `repository.workspace.links.avatar.href`, `repository.workspace.links.html.href`, `repository.workspace.links.self.href`, `repository.project.type`, `repository.project.links.self.href`, `repository.project.links.html.href`, `repository.project.links.avatar.href`, `actor.links.self.href`, `actor.type`, `actor.nickname`, `value1.new.target.author.user.links.self.href` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `value1.old.target.date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `value1.new.target.date` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `repository.type`, `repository.links.self.href`, `repository.links.avatar.href`, `repository.name`, `repository.scm`, `repository.owner.display_name`, `repository.owner.type`, `repository.owner.uuid`, `repository.owner.username`, `repository.is_private`, `repository.project.key`, `repository.project.uuid`, `repository.project.name` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `repository.full_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `repository.links.html.href` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `repository.uuid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `actor.display_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `actor.links.avatar.href` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `actor.links.html.href` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor.uuid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `actor.account_id` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Mapped `USER_RESOURCE_ACCESS` to `event.idm.read_only_udm.metadata.event_type` UDM field when `event_type` has `target resource` related data and `principal machine` data or `principal user` data.   
2023-06-12 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
