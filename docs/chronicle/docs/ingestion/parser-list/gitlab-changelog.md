---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gitlab-changelog/
title: Change log for GITLAB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:47.796001+00:00
---

# Change log for GITLAB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gitlab-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GITLAB

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `meta.user_id` raw log field to `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `meta.project` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `meta.user` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `controller`, `format`, `cpu_s`, `mem_total_bytes`, `db_duration_s`, `view_duration_s`, `duration_s`, `rate_limiting_gates` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `request_urgency`, `meta.caller_id`, `meta.feature_category`, `meta.organization_id`, `meta.root_namespace` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `worker_id` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `pid` raw log field to `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `remote_ip`, `meta.remote_ip` raw log fields to `event.idm.read_only_udm.intermediary.ip` UDM fields.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `ua` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `ua` raw log field to `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `meta.client_id` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `params.key`, `params.value` raw log fields to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-07-21 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `owners.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `owners.0.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Added a conditional check before already existing mapping of `user.email` to `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- Added a conditional check before already existing mapping of `object_attributes.last_commit.author.email` to `event.idm.read_only_udm.target.user.email_addresses`.  
\- Added a conditional check before already existing mapping of `details.author_name` to `event.idm.read_only_udm.principal.user.email_addresses`.   
2026-07-05 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `before`, `after`, `ref`, `ref_protected`, `checkout_sha`, `user_avatar`, `total_commits_count`, `commit.id`, `commit.timestamp`, `commit.url`, `commit.author.name`, `commit.author.email`, `commit.message`, `refs` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `name`, `project_name` raw log fields with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `path`, `project_namespace_id`, `project_visibility`, `project_path`, `change.before`, `change.after`, `change.ref`, `owner_name`, `key` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `path_with_namespace`, `project_path_with_namespace`, `project.ssh_url` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `project_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.user.role_name`: Newly mapped `access_level` raw log field with `event.idm.read_only_udm.target.user.role_name` UDM field.  
\- `event.idm.read_only_udm.target.group.attribute.labels`: Newly mapped `full_path`, `old_path`, `old_full_path` raw log fields with `event.idm.read_only_udm.target.group.attribute.labels` UDM field.  
\- Added support for additional date formats for the `updated_at` field.   
2026-06-25 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.id`: Removed mapping of `user.id` raw log field from `event.idm.read_only_udm.principal.resource.id` UDM field since the UDM field is deprecated.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Mapped `user.id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Removed mapping of `object_kind` raw log field from `event.idm.read_only_udm.target.resource.type` UDM field since the UDM field is deprecated.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Mapped `object_kind` raw log field with `event.idm.read_only_udm.target.resource.resource_type` UDM field when `object_kind` has a valid enum resource_type value.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `user_email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `user_username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `group_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `group_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `event_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles`: Newly mapped `group_access` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `object_attributes.sha` raw log field with `event.idm.read_only_udm.target.file.sha1` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `object_attributes.status` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.last_discovered_time`: Newly mapped `object_attributes.finished_at` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `object_attributes.created_at`,`merge_request.title`,`expires_at`, `object_attributes.stages`, `build.runner.tags`, `build.runner.is_shared`, `build.runner.active`, `build.runner.runner_type`, `build.runner.description`, `build.runner.id`, `commit.id`, `commit.message`, `commit.title`, `commit.url`, `project.visibility_level`, `project.ci_config_path`, `object_attributes.duration`, `object_attributes.queued_duration`, `object_attributes.protected_ref`, `object_attributes.source`, `merge_request.id`, `merge_request.iid` and `merge_request.url` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `object_kind`,`group_path`, `group_plan`, `object_attributes_id`, `object_attributes_iid`, `object_attributes_ref`, `object_attributes_tag`, `object_attributes_ref_status_name`, `object_attributes_before_sha`, `merge_request_target_project_id` and `merge_request_target_branch` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `build.artifacts_file.size`, `build.artifacts_file.filename`, `build.allow_failure`, `build.manual`, `build.when`, `build.queued_duration`, `build.duration`, `build.finished_at`, `build.started_at`, `build.created_at`, `build.status`, `build.name`, `build.stage`, `build.id`, `commit_author_name`, `commit_author_email`, `merge_request_source_branch` and `merge_request_source_project_id` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `build.user.email`, `build.user.avatar_url`, `build.user.username`, `build.user.name` and `build.user.id` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `merge_request_detailed_merge_status`, `merge_request_merge_status`, `merge_request_state` and `object_attributes_detailed_status` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-05-19 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.attribute.labels: Removed additional mapping of `user.email` from `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.url: Removed mapping of `repository.homepage` from `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Mapped `repository.homepage` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `project.id` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Mapped `project.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `project.name` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Mapped `project.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `object_attributes.last_commit.timestamp` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Mapped `object_attributes.last_commit.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.description: Removed mapping of `object_attributes.last_commit.message` from `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Mapped `object_attributes.last_commit.message` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.metadata.description: Removed mapping of `merge_request.last_commit.message` from `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Mapped `merge_request.last_commit.message` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Removed mapping of `merge_request.last_commit.timestamp` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Mapped `merge_request.last_commit.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `object_attributes.updated_at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `severity_level` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `object_attributes.description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `object_attributes.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `merge_request.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `merge_request.state` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `object_attributes.state` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `merge_request.source.web_url` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `merge_request.source.http_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `object_attributes.source.http_url` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `object_attributes.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `merge_request.source.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `scan_result_policy_id` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-05-07 |  Enhancement:  
\- event.idm.read_only_udm.target.resource.type: Newly mapped `object_kind` raw log field with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `user.avatar_url` raw log field with `security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.email_addresses: Newly mapped `user.email` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` and `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `user.id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user.name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.role_description: Newly mapped `repository.description` raw log field with `event.idm.read_only_udm.target.user.role_description` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `repository.homepage` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `repository.name` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `repository.url` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.avatar_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `project.default_branch` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `project.description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.git_http_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.git_ssh_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `project.homepage` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `project.http_url` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `project.id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.namespace: Newly mapped `project.namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.path_with_namespace` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.ssh_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.src.url: Newly mapped `project.url` raw log field with `event.idm.read_only_udm.src.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `project.web_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `object_attributes.source.avatar_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `object_attributes.last_commit.author.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.src.user.userid: Newly mapped `object_attributes.last_commit.author.name` raw log field with `event.idm.read_only_udm.src.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `object_attributes.last_commit.id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `object_attributes.last_commit.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `object_attributes.last_commit.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `object_attributes.last_commit.title` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `object_attributes.last_commit.url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `merge_request.source.avatar_url` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.target.user.email_addresses: Newly mapped `merge_request.last_commit.author.email` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- event.idm.read_only_udm.src.user.userid: Newly mapped `merge_request.last_commit.author.name` raw log field with `event.idm.read_only_udm.src.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.resource.id: Newly mapped `merge_request.last_commit.id` raw log field with `event.idm.read_only_udm.principal.resource.id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `merge_request.last_commit.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `merge_request.last_commit.timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `merge_request.last_commit.title` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `merge_request.last_commit.url` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.   
2025-03-05 |  Enhancement:  
\- Added support for unparsed logs.   
2025-01-22 |  Enhancement:  
\- Added support for unparsed logs.   
2024-12-19 |  Enhancement:  
\- Fixed the issue for `metadata.event_type`.   
2024-04-08 |  Enhancement:  
\- Mapped `custom_message.action` to `security_result.summary`.  
\- Mapped `ip_address` to `principal.ip`.  
\- Mapped `applicationProtocol` to `network.application_protocol`.  
\- Mapped `details.author_name`` to `principal.user.email_addresses"  
\- Mapped `author_id` to `principal.user.userid`.  
\- Mapped `target_id` to `target.resource.id`.  
\- Mapped `details.entity_path` to `target.file.full_path`.  
\- Mapped `event_type` to `product_event_type`.  
\- Mapped `target_type`, `entity_type` and `target_details` to `resource.attribute.labels`.   
2023-10-20 |  \- Mapped the fields starting with `db_` to `additional_fields`.  
\- Mapped the fields starting with `redis_` to `additional_fields`.  
\- Mapped `severity` or `jsonPayload.severity` to `security_result.severity` when the value is either `ERROR` or `NOTICE`.  
\- Mapped `jsonPayload.correlation_id` to `principal.asset_id`.  
\- Mapped `unmapped fields of jsonPayload` to `additional_fields`.  
\- Mapped `jsonPayload.worker_id` to `principal.application`.  
\- Mapped `jsonPayload.method` to `network.http.method`.  
\- Mapped `jsonPayload.pid` to `target.process.pid`.  
\- Mapped `jsonPayload.status` to `network.http.response_code`.  
\- Mapped `resource.labels.zone` to `target.cloud.availability_zone`.  
\- Mapped `resource.type` to `target.cloud.environment`.  
\- Mapped `jsonPayload.meta_user` to `target.user.userid`.  
\- Mapped `jsonPayload.username` to `principal.user.userid`.  
\- Mapped `jsonPayload.remote_ip` to `principal.ip`.  
\- Mapped `jsonPayload.ua` to `network.http.user_agent`.  
\- Mapped `jsonPayload.meta_client_id` to `target.user.userid`.  
\- Mapped `jsonPayload.path` to `target.process.file.full_path`.  
\- Mapped `protoPayload.authenticationInfo.principalEmail` to `principal.user.email_addresses`.  
\- Mapped additional fields in `protoPayload` to `additional.fields`.  
\- Provided a conditional check that required mapping is present before mapping the `metadata.event_type`.   
2023-10-10 |  \- Mapped `jsonPayload.details.as` to `principal.resource.attribute.labels` and `principal.user.role_name`.  
\- Set `principal_role.type` to `ADMINISTRATOR` for logs having `jsonPayload.details.as` equals to `Owner`.  
\- Set `principal_role.type` to `SERVICE_ACCOUNT` for logs having `jsonPayload.details.as` set to either `Developer`, `Maintainer`, or `Reporter`.  
\- Set `principal_role.type` to `TYPE_UNSPECIFIED` for logs having `jsonPayload.details.as` equals to `Guest`.  
\- Mapped `jsonPayload.details.add` to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.entity_type` to `target.resource.attribute.labels`.   
2023-08-31 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
