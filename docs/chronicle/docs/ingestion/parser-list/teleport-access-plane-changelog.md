---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teleport-access-plane-changelog/
title: Change log for TELEPORT_ACCESS_PLANE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T19:19:12.318639+00:00
---

# Change log for TELEPORT_ACCESS_PLANE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/teleport-access-plane-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TELEPORT_ACCESS_PLANE

Date | Changes  
---|---  
2026-09-08 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Event_data.ei`, `Event_data.user_kind`, `Event_data.server_version`, `Event_data.with_mfa`, `Event_data.private_key_policy`, `Event_data.identity.private_key_policy`, `Event_data.server_sub_kind`, `Event_data.session_recording`, `Event_data.session_start`, `Event_data.session_stop`, `Event_data.enhanced_recording`, `Event_data.interactive`, `loginName`, `kubernetesGrpVal`, `req`, `participant`, `app_protocol_src` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Event_data.proposed_state`, `Event_data.expires`, `Event_data.max_duration` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Event_data.user_cluster_name`, `Event_data.resource_api_group`, `Event_data.kubernetes_cluster`, `Event_data.kubernetes_labels.Environment`, `Event_data.kubernetes_labels.Stack`, `Event_data.kubernetes_labels.Jurisdiction`, `Event_data.kubernetes_labels.teleport_internal_resource_id` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels`: Newly mapped `Event_data.server_labels.environment`, `Event_data.server_labels.Environment`, `Event_data.server_labels.stack`, `Event_data.server_labels.Stack`, `Event_data.server_labels.Jurisdiction`, `Event_data.server_labels.teleport_internal_resource_id` raw log fields with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Event_data.server_hostname`, `Event_data.app_public_addr`, `Event_data.public_addr` raw log fields with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `event_data_user`, `approver_email` raw log fields with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `event_data_user`, `event_data_reviewer` raw log fields with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `Event_data.sid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `Event_data.namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Event_data.server_id`, `Event_data.id` raw log fields with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Event_data.app_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `Event_data.app_uri`, `Event_data.request_path` raw log fields with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `remote_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `Event_data.proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `Event_data.verb` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `Event_data.response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `Event_data.resource_kind` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Event_data.reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `Event_data.state` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.target.user.email_addresses`: Newly mapped `kubernetesUser` raw log field with `event.idm.read_only_udm.target.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `kubernetesUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `kubernetesGrp` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `userrole` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: If `event_data_state` is APPROVED, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW.  
\- `event.idm.read_only_udm.metadata.event_type`: When `Event_type` is app.session.start, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGIN and when `Event_type` is session.end, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGOUT.   
2026-08-28 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `fields.argv`, `fields.return_code`, `fields.participants`, `fields.initial_command` , `port1` extracted from `fields.addr.local`, `fields.ei`, `fields.trace.component`, `fields.version`, `fields.session_start`, `fields.session_stop`, `fields.operation`, `fields.enhanced_recording`, `fields.interactive`, `fields.session_recording`, `fields.private_key_policy`, `fields.server_sub_kind`, `fields.user_kind`, and `fields.size` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `fields.sid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `fields.user_traits.logins`, `fields.user_cluster_name` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.namespace`: Newly mapped `fields.namespace` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `fields.src_addr`, `fields_remote_ip` extracted from `fields.addr.remote`, and `ip1` extracted from `fields.addr.local` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `fields_remote_port` extracted from `fields.addr.remote` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `fields.dst_addr` and `target_server_ip` extracted from `fields.server_addr` raw log fields with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `fields.dst_port` and `target_port` extracted from `fields.server_addr` raw log fields with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `fields.user` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `fields.login` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `fields.path` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `fields.program` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `fields.pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.process.parent_process.pid`: Newly mapped `fields.ppid` raw log field with `event.idm.read_only_udm.target.process.parent_process.pid` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `fields.proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `fields.user_roles` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `fields.server_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `fields.server_id` raw log field with `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `fields.cgroup_id` and `fields.server_labels` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `fields.server_hostname`, `hostname` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `fields.action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `fields.initial_command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set `event.idm.read_only_udm.metadata.event_type` to `PROCESS_LAUNCH` when `event_type_` is `session.command` and principal or target machine data is present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when `event_type_` is `session.network` and principal and target machine data are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT` when `event_type_` is `session.end` and principal or target user details are present.  
\- Set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `event_type_` is `session.start` and principal or target user details are present.   
2026-08-17 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `Uid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `Event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Event_time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `Event_data.identity.user` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field when `Event_data.identity.user` is an email address.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Event_data.identity.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field when `Event_data.identity.user` is not an email address.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Event_data.identity.client_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `Event_data.identity.roles` raw log field with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Event_data.identity.logins` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `Event_data.certificate_authority.subject_key_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `Event_data.cluster_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Event_data.certificate_authority.type`, `Event_data.certificate_authority.domain`, `Event_data.identity.route_to_cluster`, `Event_data.identity.teleport_cluster` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `Event_data.cert_type` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Event_data.code`, `Event_data.identity.bot_internal` and `Event_data.identity.expires` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine and principal user data are present and `Event_type` is cert.create, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_RESOURCE_CREATION.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `code`, `ei`, `orig_log_filename` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `app_name` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `app_public_addr` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `app_uri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `status_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Added a grok pattern for new log format.   
2025-09-04 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.product_object_id` : Newly mapped `bot_instance_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id UDM field.  
\- `event.idm.read_only_udm.principal.application` : Newly mapped `bot_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.name` : Newly mapped `cluster_name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` : Newly mapped `server_hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname` : Newly mapped `server_hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id` : Newly mapped `server_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type` : Newly mapped `event` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `login` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.namespace` : Newly mapped `namespace` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.network.session_id` : Newly mapped `sid` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.roles` : Newly mapped `server_labels.Role` raw log field with `event.idm.read_only_udm.target.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.target.application` : Newly mapped `server_labels.aws_application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels` : Newly mapped `user` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels` : Newly mapped `impersonator` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.ingestion_labels` : Newly mapped `server_id` raw log field with `event.idm.read_only_udm.metadata.ingestion_labels` UDM field.  
\- `event.idm.read_only_udm.target.asset.attribute.labels` : Newly mapped `server_labels.Environment`, `server_labels.OS`, `server_labels.Version`, `server_labels.aws_backup`, `server_labels.aws_cost_center`, `server_labels.aws_environment`, `server_labels.aws_role`, `server_labels.aws_terraform`, `server_labels.aws_tier`, `server_labels.aws_zone` and `server_labels.aws_name` raw log field with `event.idm.read_only_udm.target.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `ei`, `private_key_policy`, `server_labels.Uptime`, `user_kind`, `server_version`, and `code` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-02-19 |  Enhancement:  
\- Added support for JSON logs.   
2023-11-17 |  Enhancement:  
\- Mapped `remote_addr` to `target.ip`.  
\- Mapped `port` to `target.port`.   
2023-05-09 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
