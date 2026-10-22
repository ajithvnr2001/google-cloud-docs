---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kiteworks-changelog/
title: Change log for KITEWORKS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:17.992496+00:00
---

# Change log for KITEWORKS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/kiteworks-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for KITEWORKS

Date | Changes  
---|---  
2026-08-11 |  Enhancement:  
\- Added support for new format of JSON logs.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `payload.user_id` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `payload.user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` and `event.idm.read_only_udm.network.http.parsed_user_agent` UDM fields.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `payload.node_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `payload.client_name` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `payload.client_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `payload.host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `payload.domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.user.email_addresses`: Newly mapped `payload.username` raw log field with `event.idm.read_only_udm.principal.user.email_addresses` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `payload.username` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `payload.ip_address` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `payload.created` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `endpoint_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `payload.data.folder.guid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `endpoint_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `payload.event_name` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `payload.data.folder.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `payload.data.folder.path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `payload.data.session` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `webhookId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `payload.single_line` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.mechanism`: Newly mapped `payload.data.flow` raw log field with `event.idm.read_only_udm.extensions.auth.mechanism` UDM field.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `payload.data.token_type` raw log field with `event.idm.read_only_udm.extensions.auth.type` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `payload.tenant_id`, `tenantId` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `payload.endpoint_version`, `payload.event_id`, `payload.geolocation_id`, `payload.guid`, `payload.node_storage_id`, `payload.transaction_id`, `payload.data.queue_name`, `payload.data.rmq_node`, `payload.data.subfolders`, `payload.data.folder.id`, `subscriptionId`, `payload.data.context`, `payload.data.geolocation_source.source`, `payload.data.geolocation_source.source_with_kw`, `payload.appname`, `payload.procid`, `payload.flag`, `payload.data_keywords`, `payload.indirect_users`, `payload.client_device`, `payload.parent_folder_id`, `payload.data.folder.ec_object_id`, `payload.data.folder.ec_source`, `payload.data.user`, `payload.data.method`, `payload.data.policies` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `payload.severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: When `payload.successful` is true, set the value to ALLOW. When `payload.successful` is false, set the value to BLOCK.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when network http, principal and target related data is present else setting it to `USER_UNCATEGORIZED` when only principal user related data is present else setting it to `STATUS_UPDATE` when only principal related data is present else setting it to `GENERIC_EVENT` when none of the above conditions are met.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `KITEWORKS` value with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `KITEWORKS` value with `event.idm.read_only_udm.metadata.product_name` UDM field.   
2025-11-14 |  Enhancement:  
\- Mapped Kiteworks JSON formatted logs to UDM fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `subscriptionId`, `payload.data.context`, `payload.data.geolocation_source.source`, `payload.data.geolocation_source.source_with_kw`, `payload.appname`, `payload.procid`, `payload.flag`, `payload.tenant_id` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.intermediary`: Newly mapped `intermediary_host` raw log field(s) with `event.idm.read_only_udm.intermediary` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `payload.description` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `webhookId` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.http.parsed_user_agent`: Newly mapped `payload.user_agent` raw log field(s) with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `payload.user_agent` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `payload.data.session` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `payload.client_name` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `payload.client_id` raw log field(s) with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `payload.host` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `payload.user_ip`, `payload.source_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `payload.user_type` raw log field(s) with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `payload.user_id` raw log field(s) with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `payload.user_name` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `payload.successful` raw log field(s) with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `payload.severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `payload.application` raw log field(s) with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `payload.app_host` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `tenantId` raw log field(s) with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `payload.event_field` is `user_logged_out`, updated to `USER_LOGOUT`.  
\- `event.idm.read_only_udm.extensions.auth.type`: If `msg` or `payload.event_field` has a value, updated to `MACHINE`.  
\- Parsing logic updated to prioritize direct JSON parsing of the entire log message. If JSON parsing fails, it falls back to the previous grok-based syslog parsing logic.  
\- Added logic to parse `payload.timestamp` using the `ISO8601` format.   
2025-09-26 |  \- Added support for new format of logs.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `log_message`, `description`, `full_log` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped `host_ip`, `data.node_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `host_ip`, `data.node_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `host`, `app_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `http_user_agent`, `user_agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `http_user_agent`, `user_agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid`, `process_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `request_time_seconds` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- event.idm.read_only_udm.network.session_duration.nanos: Newly mapped `request_time_nanos` raw log field with `event.idm.read_only_udm.network.session_duration.nanos` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `status` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.email.mail_id: Newly mapped `msgid` raw log field with `event.idm.read_only_udm.network.email.mail_id` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `app_protocol_output`, `http_version` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `method_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `bytes_sent` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `request_length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `http_referer_filtered` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `remote_addr`, `user_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `remote_addr`, `user_ip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `context`, `data.reference_id`, `id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `remote_user`, `from`, `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `to` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `data_file_path`, `data_file` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `data_file_size` raw log field with `event.idm.read_only_udm.target.file.size` UDM field.  
\- event.idm.read_only_udm.target.file.mime_type: Newly mapped `data_file_mime` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `data_file_hash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `hash_label` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `url_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session`, `data.session` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `data_file_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.file.names: Newly mapped `data_file_name` raw log field with `event.idm.read_only_udm.target.file.names` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `cipher` raw log field with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `event_data` field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped agent.id`,`agent.name`,`decoder.name`,`rule.main`,`request_filtered_label`, `groups_label`, `http_x_forwarded_for`, `msec`, `body_bytes_sent`, `queue_id`, `size`, `class`, `nrcpts`, `dsn`, `ctladdr`, `xdelay`, `mailer`, `pri`, `delay`, `data.file.file_id`, `tenant_id`, `user_type`, `client_device`, `flag`, `data.file.file_uploader.profile.id`, `data.file.file_uploader.profile.name`, `data.is_folder_upload`, `data.context`, `data.geolocation_source.source`, `data.geolocation_source.source_with_kw`, `data.file.file_uploader.guid`, `daemon`, `verify`, `bits`, `STARTTLS`, `ec_object_id`, `rule.firedtimes`, `location`, `data.file.version`, `data.file.ec_object_id`, `data.parent_folder.path`, and `data.parent_folder.ec_source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.tls.version: Newly mapped `version` raw log field with `event.idm.read_only_udm.network.tls.version` UDM field.  
\- event.idm.read_only_udm.intermediary: Newly mapped `intermediary1`, `intermediary` raw log field with `event.idm.read_only_udm.intermediary` UDM field.  
\- event.idm.read_only_udm.about: Newly mapped `about` raw log field with `event.idm.read_only_udm.about` UDM field.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped `user_name` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `manager.name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true` and has_target is `true` and has_target_file is `true`, updated to FILE_CREATION.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true` and has_target is `true` and app_protocol_output matches `HTTP`, updated to NETWORK_HTTP.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true` and has_target is `true`, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal_user is `true`, updated to USER_UNCATEGORIZED.   
2023-11-10 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
