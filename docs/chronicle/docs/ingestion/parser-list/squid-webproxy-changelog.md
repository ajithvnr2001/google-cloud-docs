---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/squid-webproxy-changelog/
title: Change log for SQUID_WEBPROXY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:09.761834+00:00
---

# Change log for SQUID_WEBPROXY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/squid-webproxy-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SQUID_WEBPROXY

Date | Changes  
---|---  
2026-09-30 |  Enhancement:  
\- Added new grok patterns to extract the `elapsed_time_ms`, `hier_direct`, `content_type`, `error_desc` log fields.  
\- `event.idm.read_only_udm.security_result.action`: If `action` is `TCP_REFRESH_MODIFIED`, updated the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `error_desc` log field with `event.idm.read_only_udm.security_result.description` UDM field.   
2026-06-22 |  Enhancement:  
\- Updated grok pattern on `url` to extract `tgthost`, `tgtport`, and `app_proto`.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine, target machine are present and application protocol is `HTTP` or `HTTPS` updated the value of `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP`.  
\- 'event.idm.read_only_udm.security_result.action: When `returnCode` is 400 updated `event.idm.read_only_udm.security_result.action` to `BLOCK`.   
2026-04-23 |  Enhancement:  
\- Added a Grok pattern to parse the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `elapsed_time_ms`, `number` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `content_type` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Added gsub above the if condition of `user_agent` field to not populate `-` and empty values with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- Added a condition to check `method` field to not populate `-` and empty values.   
2026-04-16 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `protocol_version_details` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `agent.vf_ingestion.hostname` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.first_discovered_time`: Newly mapped `evts.created` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_priority`, `agent.vf_ingestion.type`, `agent.vf_ingestion.name`, `agent.vf_ingestion.environment`, `organization.id`, `organization.name`, `my_timestamp`, `_time`, `cribl_pipe` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `app_proto_details` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional logic to map `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` if `app_proto_details` contains `HTTP` or `HTTPS`.   
2025-10-28 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `syslogdate` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `response_code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `sent_bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `heir_status` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field if it doesn't contain `-` or `NONE` values.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.additional.fields` UDM field if its not null.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly mapped `protocol_version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `phost` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent: Newly mapped `version_details` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `headerip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `headerip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.   
2025-08-07 |  Enhancement:  
\- Modified the grok pattern to parse timestamp with extra spaces.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped from a combination of `day1`, `month1`, `year1`, `time1`, and `timezone1` raw log fields when timestamp_value is not present.  
\- Added conditional check for time_value: If `time_value` is empty, the timestamp is derived from `day1`, `month1`, `year1`, `time1`, and `timezone1`.   
2025-07-22 |  Enhancement:  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped time_value raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `transaction.timing.gmt_time`, `transaction.timing.local_time` and `result_code` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a date filter to parse `timestamp_value` when it matches the `dd/MMM/yyyy:HH:mm:ss Z` format.  
\- Refactored parser logic to dynamically map multiple raw log fields to `event.idm.read_only_udm.additional.fields` and `event.idm.read_only_udm.target.resource.attribute.labels` for improved maintainability.  
\- Updated event type logic: Events have both a principal and target are now classified as NETWORK_CONNECTION.   
2025-07-11 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `env.application` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `env.host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `env.host` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `env.instance` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `env.class`, `env.cname`, `env.nom`, `env.site`, `env.st`, `env.uniq_hname` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `http.access_control.ident`, `http.request.status`, `http.request.headers_size`, `http.request.hierarchy_status`, `http.request.http_version`, `http.response.content_type`, `http.response.headers_size`, `http.response.type`, `http.response.peer_code`, `http.response.xpowby`, `http.response.xrid`,`http.timing.peer_rsp_time`, `http.timing.peer_total_time`, `http.timing.rsp_time`, `transaction.connection.client_remote_port`, `transaction.connection.peer_local_port`, `transaction.connection.peer_remote_port`, `transaction.timing.dns_lookup`, `transaction.timing.epoch` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `http.access_control.user` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `http.request.method` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `http.request.url` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `http.request.xff` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.network.http.referer`: Newly mapped `http.request.referer` raw log field with `event.idm.read_only_udm.network.http.referer` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `http.request.total_size` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `http.request.url_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `http.response.code` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `http.response.total_size` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `transaction.connection.client_local_ip` and `transaction.connection.client_remote_ip` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `transaction.connection.client_local_ip` and `transaction.connection.client_remote_ip` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `transaction.connection.client_local_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `transaction.connection.peer_local_ip` and `transaction.connection.peer_remote_ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `transaction.connection.peer_local_ip` and `transaction.connection.peer_remote_ip` raw log fields with `event.idm.read_only_udm.target.asset.ip` UDM field.   
2025-07-09 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- Replaced `squid_webproxy.include` with actual code.  
\- Removed redundant code for `event.idm.read_only_udm.network.http.user_agent`.  
\- Added `on_error` for all `replace` block.  
\- If `has_principal` is `true` and (has_target is `true` or has_target_url is `true`) and app_proto is `HTTP` or `HTTPS`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP`.  
\- If `app_proto` is "` and has_principal is `true` and method is not `" and has_target is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_UNCATEGORIZED`.  
\- If `has_target` is `true` and has_target is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `has_principal` is `true` and has_target is `false` and method is not "", then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UNCATEGORIZED`.  
\- If `has_principal` is `true` and has_target is `false`, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- If none of the above conditions are met, then set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2025-04-08 |  Enhancement:  
\- Added a Grok pattern in order to parse the logs with syslog format.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `squid_instance`, `tcp_tunnel`, `hier_direct` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a condition to check if `url` raw log field is not null before mapping with `event.idm.read_only_udm.target.url` UDM field.   
2025-03-26 |  Enhancement:  
\- Added a Grok pattern to parse new format of syslog logs.  
\- Mapped `user_agent` to `network.http.user_agent` and `network.http.parsed_user_agent`.   
2025-02-27 |  Enhancement:  
\- When `action` is `TCP_MISS` then mapped `ALLOW` to `security_result.action`.   
2024-11-04 |  Enhancement:  
\- Added support to map data from JSON logs.  
\- Mapped `region` to `principal.cloud.availability_zone`.  
\- Mapped `source_type` to `additional.fields`.   
2024-09-11 |  Enhancement:  
\- Mapped `when` to `metadata.event_timestamp` as primary timestamp.   
2024-08-15 |  Enhancement:  
\- Mapped `timestamp_value` to `metadata.event_timestamp`.   
2024-04-03 |  Enhancement:  
\- Mapped `user_agent` to `network.http.user_agent`.  
\- Mapped `recv_bytes` to `network.received_bytes`.  
\- Mapped `sent_bytes` to `network.sent_bytes`.  
\- Mapped `src_port` to `principal.port`.  
\- Aligned mappings for `principal.ip` and `principal.asset.ip`.  
\- Aligned mappings for `target.ip` and `target.asset.ip`.  
\- Aligned mappings for `target.hostname` and `target.asset.hostname`.   
2022-10-30 |  Enhancement, Bug-fix:  
\- Added a Grok pattern to parse dropped logs.  
\- Added a Grok pattern to map the hostname of the Squid proxy server to `intermediary.hostname`.   
2022-09-19 |  Enhancement:  
\- Parsed syslog of type squid.  
\- Mapped `insertId` to `metadata.product_log_id`.  
\- Mapped `logName` to `target.process.file.full_path`.  
\- Mapped `instance_id` to `additional.fields`.  
\- Mapped `project_id` to `additional.fields`.  
\- Mapped `zone` to `additional.fields`.  
\- Mapped `type` to `additional.fields`.  
\- Mapped `agent.ephemeral_id` to `additional.fields`.  
\- Mapped `agent.hostname` to `principal.hostname`.  
\- Mapped `agent.version` to `metadata.product_version`.  
\- Mapped `host.mac` to `principal.mac`.  
\- Mapped `host.ip` to `principal.ip`.  
\- Mapped `event_action` to `security_result.action_details`.  
\- Mapped `event_message` to `metadata.description`.  
\- Mapped `host.architecture` to `principal.asset.hardware`.  
\- Mapped `host.id` to `principal.asset.asset_id`.  
\- Mapped `host.os.version` to `principal.platform_version`.  
\- Mapped `host.os.kernel` to `principal.platform_patch_level`.  
\- Mapped `host.os.codename` to `additional.fields`.  
\- Mapped `syslog_severity` to `security_result.severity_details`.  
\- Mapped `syslog_severity_code` to `security_result.severity`.  
\- Mapped `host.os.platform` to `principal.platform`.  
\- Mapped `log.file.path` to `target.process.file.full_path`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
