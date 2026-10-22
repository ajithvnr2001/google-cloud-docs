---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vrealize-changelog/
title: Change log for VMWARE_VREALIZE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:22.601590+00:00
---

# Change log for VMWARE_VREALIZE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-vrealize-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_VREALIZE

Date | Changes  
---|---  
2026-09-04 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- Added a grok pattern on `sub_msg` to extract `rule_id`, `originator_id`, `data`, `msg`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Newly mapped `update` raw log field with `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `msg_type` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `sub_msg` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-07-29 |  Enhancement:  
\- Added support for new format of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `vmw_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `vmw_vcenter` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `vmw_vr_ops_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_identifier` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `generator` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `syslog_identifier` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `target_user_id` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `process_pid` raw log field with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `vmw_object_id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator_id`, `pri_facility`, `event_time`, `syslog_version`, `syslog_pri` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `vmw_cluster`, `vmw_datacenter`, `vmw_vcenter_id` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `severity_level` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `pri_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `BLOCK` value with `event.idm.read_only_udm.security_result.action` UDM field when `action_message` matches with `fail`.  
\- `event.idm.read_only_udm.extensions.auth.type`: Newly mapped `AUTHTYPE_UNSPECIFIED` value with `event.idm.read_only_udm.extensions.auth.type` UDM field when `has_principal_host` is true, `has_target_user` is true, and `action_message` matches with `authentication failed`.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly mapped `USER_LOGIN` value with `event.idm.read_only_udm.metadata.event_type` UDM field when `has_principal_host` is true and `has_target_user` is true and `action_message` matches with `authentication failed`.   
2025-08-05 |  Enhancement:  
\- Added support for new format of syslog + json Logs by adding grok pattern.   
2025-07-22 |  Enhancement:  
\- Added grok patterns to parse new format of logs.  
\- event.idm.read_only_udm.target.resource.attribute.labels : Newly mapped `etag` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes : Newly mapped `request_length` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.network.received_bytes : Newly mapped `server_response_length` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- event.idm.read_only_udm.intermediary.ip : Newly mapped `server_conn_src_ip` and `vs_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `persistent_session_id`, `client_rtt`, `server_response_time_first_byte`, `server_response_time_last_byte`, `response_length`, `response_time_first_byte`, `response_time_last_byte`, `compression_percentage`, `client_insights`, `request_headers`, `server_ssl_session_id`, `server_connection_reused`, `response_headers`, `request_id`, `servers_tried`, `jwt_log`, `max_ingress_latency_fe`, `conn_est_time_fe`, `max_ingress_latency_be`, `conn_est_time_be`. raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2023-06-25 |  Enhancement:  
\- Added support for a new format of JSON logs.   
2023-06-20 |  Enhancement -  
-Added Grok pattern for failing logs.  
-Mapped `ts` to `event_timestamp`.  
-Mapped `isLocal`, `updateType`, `subClusterUuid`, `valueLength` to `event.idm.read_only_udm.additional.fields`.   
2023-05-26 |  Enhancement -  
Added Grok pattern for failing logs.   
2023-05-23 |  Enhancement -  
\- Added Grok pattern to parse syslog logs and added mapping for the following fields:  
\- `client_ip` mapped to `principal.ip`.  
\- `host` mapped to `principal.hostname`.  
\- `referer` mapped to `principal.url`.  
\- `client_src_port` mapped to `principal.port`.  
\- `server_ip` mapped to `target.ip`.  
\- `server_name` mapped to `target.hostname`.  
\- `server_src_port` mapped to `target.port`.  
\- `ssl_session_id` mapped to `network.session_id`.  
\- `ssl_version` mapped to `tls.version_protocol`.  
\- `ssl_cipher` mapped to `network.tls.cipher`.  
\- `method` mapped to `network.http.method`.  
\- `user_agent` mapped to `network.http.user_agent`.  
\- `response_code` mapped to `network.http.response_code`.  
\- `uri_path` mapped to `network.http.referral_url`.  
\- `requested_protocol` mapped to `network.application_protocol`.  
\- `log_id` mapped to `metadata.product_log_id`.  
\- `sec_ch_ua`, `csrf_token`, `vs_name`, `virtualservice`, `request_state`, `request_content_type`,  
`response_content_type`, `compression`, `pool`, `pool_name`, `service_engine` mapped to `additionl.fields`.  
\- `headers_sent_to_server.Cookie`, `headers_received_from_server.set-cookie`,  
`headers_received_from_server.Access-Control-Allow-Origin` mapped to `target.resource.attribute.labels`.  
\- `headers_received_from_server.Content-Security-Policy` mapped to `principal.resource.attribute.labels`.   
2023-04-20 |  Enhancement - Added mapping for the following fields:  
\- `tenantId`, `values.actorExternalId`, `actorUuid`, `actorId`, `values.deviceType`, `objectName`, `objectType`, `objectId`. Mapped to `additional.fields`.   
2023-03-27 |  Enhancement - Added mapping for the following fields:  
\- `uuid` mapped to `metadata.product_log_id`.  
\- `tenantId` mapped to `principal.resource.attribute.labels`.  
\- `actorId` mapped to `principal.user.userid`.  
\- `actorUserName` mapped to `principal.user.user_display_name`.  
\- `actorUuid` mapped to `principal.resource.attribute.labels`.  
\- `actorDomain` mapped to `principal.hostname`.  
\- `sourceIp` mapped to `principal.ip`.  
\- `automation_tag` mapped to `product_event_type`.  
\- `objectName` mapped to `target.resource.attribute.labels`.  
\- `objectType` mapped to `target.resource.attribute.labels`.  
\- `clientId` mapped to `target.user.userid`.  
\- `values.deviceType` mapped to `principal.resource.attribute.labels`.  
\- `objectId` mapped mapped to `target.resource.attribute.labels`.  
\- `values.resourceType` mapped to `principal.resource.resource_subtype`.  
\- `values.success` mapped to `security_result.action`.   
2022-07-06 |  Enhancement - Added Mapping for the following field:  
\- `hostname` mapped to `principal.hostname`.  
\- Changed metadata.event_type from `GENERIC_EVENT` to `STATUS_UPDATE` where `principal.ip` or `target.ip` or `principal.hostname` not null.   
2022-04-27 |  \- Mapped complete value for question_name to the field `network.dns.questions.name`  
2022-03-30 |  \- Newly created parser.  
\- Added support for SYSLOG format.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
