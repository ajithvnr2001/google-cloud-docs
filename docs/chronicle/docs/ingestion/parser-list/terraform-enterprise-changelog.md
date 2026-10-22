---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/terraform-enterprise-changelog/
title: Change log for TERRAFORM_ENTERPRISE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:37.887135+00:00
---

# Change log for TERRAFORM_ENTERPRISE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/terraform-enterprise-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TERRAFORM_ENTERPRISE

Date | Changes  
---|---  
2025-06-23 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `data.attributes.created-at` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `data.attributes.terraform-version` raw log field with`event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `data.attributes.status` raw log field with `event.idm.read_only_udm.security_result.0.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data.attributes.actions.is-cancelable`, `data.attributes.actions.is-confirmable`, `data.attributes.actions.is-discardable`, `data.attributes.actions.is-force-cancelable`, `data.attributes.allow-config-generation`, `data.attributes.allow-empty-apply`, `data.attributes.auto-apply`, `data.attributes.has-changes`, `data.attributes.is-destroy`, `data.attributes.permissions.can-apply`, `data.attributes.permissions.can-cancel`, `data.attributes.permissions.can-comment`, `data.attributes.permissions.can-discard`, `data.attributes.permissions.can-force-cancel`, `data.attributes.permissions.can-force-execute`, `data.attributes.permissions.can-override-policy-check`, `data.attributes.plan-only`, `data.attributes.refresh`, `data.attributes.refresh-only`, `data.attributes.save-plan`, `data.attributes.status-timestamps.cost-estimated-at`, `data.attributes.status-timestamps.cost-estimating-at`, `data.attributes.status-timestamps.plan-queueable-at`, `data.attributes.status-timestamps.plan-queued-at`, `data.attributes.status-timestamps.planned-and-finished-at`, `data.attributes.status-timestamps.planned-at`, `data.attributes.status-timestamps.planning-at`, `data.attributes.status-timestamps.post-plan-completed-at`, `data.attributes.status-timestamps.post-plan-running-at`, `data.attributes.status-timestamps.queuing-at`, `data.attributes.trigger-reason`, `data.attributes.updated-at`, `data.relationships.run-events.data`, `data.relationships.task-stages.data`, `data.relationships.policy-checks.data`, `data.relationships.comments.data` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data.relationships.workspace.data.id` , `data.relationships.workspace.data.type`, `data.relationships.apply.data.id`, `data.relationships.apply.data.type`, `data.relationships.apply.links.related`, `data.relationships.configuration-version.data.id`, `data.relationships.configuration-version.data.type`, `data.relationships.configuration-version.links.related`, `data.relationships.cost-estimate.data.id`, `data.relationships.cost-estimate.data.type`, `data.relationships.cost-estimate.links.related`, `data.relationships.plan.data.id`, `data.relationships.plan.data.type`, `data.relationships.plan.links.related`, `data.relationships.run-events.links.related`, `data.relationships.task-stages.links.related`, `data.relationships.policy-checks.links.related`, `data.relationships.comments.links.related`, `data.id`, `data.type`, `data.links.self` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-03-12 |  Enhancement:  
\- Mapped `insertId` to `metadata.product_log_id`.  
\- Mapped `jsonPayload.comm` to `principal.process.file.names`.  
\- Mapped `jsonPayload.source_realtime_timestamp` to `additional.fields`.  
\- Mapped `jsonPayload.container_name` to `target.resource.name`.  
\- Mapped `jsonPayload.machine_id` to `principal.asset.asset_id`.  
\- Mapped `jsonPayload.priority` to `security_result.priority_details`.  
\- Mapped `jsonPayload.exe` to `principal.process.file.full_path`.  
\- Mapped `jsonPayload.cmdline` to `principal.process.command_line`.  
\- Mapped `jsonPayload.container_tag` to `principal.resource.attribute.labels`.  
\- Mapped `jsonPayload.gid` to `principal.user.group_identifiers`.  
\- Mapped `jsonPayload.uid` to `additional.fields`.  
\- Mapped `jsonPayload.cap_effective` to `principal.process.access_mask`.  
\- Mapped `jsonPayload.transport` to `additional.fields`.  
\- Mapped `jsonPayload.syslog_identifier` to `additional.fields`.  
\- Mapped `jsonPayload.pid` to `principal.process.pid`.  
\- Mapped `jsonPayload.image_name` to `additional.fields`.  
\- Mapped `jsonPayload.image_name` to `target.ip` and `target.asset.ip`.  
\- Mapped `jsonPayload.image_name` to `target.resource.name` and `target.resource.attribute.labels`.  
\- Mapped `method` to `network.http.method`.  
\- Mapped `severity_detail` to `security_result.severity`.  
\- Mapped `time_stamp` to `metadata.event_timestamp`.  
\- Mapped `path` to `target.url`.  
\- Mapped `format` to `additional.fields`.  
\- Mapped `status` to `network.http.response_code`.  
\- Mapped `duration` to `additional.fields`.  
\- Mapped `view` to `additional.fields`.  
\- Mapped `db` to `additional.fields`.  
\- Mapped `dd.trace_id` to `additional.fields`.  
\- Mapped `dd.span_id` to `additional.fields`.  
\- Mapped `dd.env` to `additional.fields`.  
\- Mapped `dd.service` to `additional.fields`.  
\- Mapped `dd.version` to `additional.fields`.  
\- Mapped `ddsource` to `additional.fields`.  
\- Mapped `uuid` to `additional.fields`.  
\- Mapped `remote_ip` to `principal.ip`.  
\- Mapped `request_id` to `network.session_id`.  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `user` to `principal.user.userid`.  
\- Mapped `auth_source` to `additional.fields`.  
\- Mapped `jsonPayload.container_id_full` to `principal.resource.product_object_id`.  
\- Mapped `jsonPayload.systemd_cgroup` to `additional.fields`.  
\- Mapped `jsonPayload.systemd_slice` to `additional.fields`.  
\- Mapped `jsonPayload.hostname` to `principal.hostname`.  
\- Mapped `jsonPayload.selinux_context` to `additional.fields`.  
\- Mapped `resource.type` to `principal.resource.resource_subtype`.  
\- Mapped `resource.labels.location` to `target.resource.attribute.cloud.availability_zone`.  
\- Mapped `resource.labels.project_id` to `target.resource_ancestors.product_object_id`.  
\- Mapped `resource.labels.namespace` to `target.namespace`.  
\- Mapped `resource.labels.node_id` to `additional.fields`.  
\- Mapped `logName` to `metadata.url_back_to_product`.  
\- Mapped `receiveTimestamp` to `metadata.collected_timestamp`.   
2025-02-10 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2025-01-23 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-06-26 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
