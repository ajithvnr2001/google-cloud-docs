---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iis-changelog/
title: Change log for IIS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:21.866953+00:00
---

# Change log for IIS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/iis-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for IIS

Date | Changes  
---|---  
2026-09-29 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `cs_host` raw log field from `event.idm.read_only_udm.additional.fields` UDM field, when server or computer hostname log fields are not present in the raw log.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `cs_host` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields, when server or computer hostname log fields are not present in the raw log.   
2026-07-14 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/iis`.   
2026-06-09 |  Enhancement:  
\- Modified the Grok pattern in order to parse the new format of SYSLOG logs.   
2026-05-17 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields correctly for the new pattern of SYSLOG logs.  
\- Added a Grok pattern to the raw log field `user_details` to parse the `uid`, `principal_host` and `src_port` raw log fields.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `scope_id`, `user_agent_details`, `scope_id_1`, `scope_id_2` raw log fields to event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_host` and `src_host` to event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname UDM fields.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_host` to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `server_ip` to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.port: Newly mapped `server_port` to `event.idm.read_only_udm.intermediary.port` UDM field.  
\- event.idm.read_only_udm.principal.resource.name: Newly mapped `service_name` to `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `server_address` to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip`, `client_ip_1`, `client_ip_2` and `src_host` to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.target.url: Newly mapped `request_path` and `requested_url` to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.network.direction: Newly mapped `network_direction` to `event.idm.read_only_udm.network.direction` UDM field when the value of `network_direction` is `RPC_OUT_DATA`.   
2026-04-07 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields correctly for the new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.network.session_duration`: Newly mapped `time_taken` raw log field with `event.idm.read_only_udm.network.session_duration` UDM field.   
2026-03-19 |  Enhancement:  
\- Added a grok pattern to parse a new pattern of logs. Due to this change, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.additional.fields`  
\- `event.idm.read_only_udm.intermediary.ip`  
\- `event.idm.read_only_udm.metadata.collected_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.application_protocol`  
\- `event.idm.read_only_udm.network.direction`  
\- `event.idm.read_only_udm.network.http.method`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.annotation.key`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.annotation.value`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_engine_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.device_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.family`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.locale`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.os`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.os_variant`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.platform`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.sub_family`  
\- `event.idm.read_only_udm.network.http.referral_url`  
\- `event.idm.read_only_udm.network.http.response_code`  
\- `event.idm.read_only_udm.network.http.user_agent`  
\- `event.idm.read_only_udm.network.received_bytes`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.network.session_duration.seconds`  
\- `event.idm.read_only_udm.network.tls.version`  
\- `event.idm.read_only_udm.observer.ip`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.principal.user.userid`  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels.key`  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels.value`  
\- `event.idm.read_only_udm.security_result.category_details`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.port`  
\- `event.idm.read_only_udm.target.resource.name`  
\- `event.idm.read_only_udm.target.url`  
\- `event.idm.read_only_udm.target.user.userid`  
2026-02-13 |  Enhancement:  
\- Modified grok patterns to support extraction of `time_taken_1` and `x_forwarded_for` to ensure their mapping to `event.idm.read_only_udm.network.session_duration.seconds` and `event.idm.read_only_udm.intermediary.ip` respectively.  
\- Updated mapping for `event.idm.read_only_udm.target.port`: Added validation to the raw field `s-port` to ensure it contains a valid port number before mapping.  
\- Updated mapping for `event.idm.read_only_udm.principal.user.userid`: Modified conditional logic to prevent mapping when the raw field `_user` contains just a hyphen (-).  
\- Refactored parser logic for `server.type`, `log.file.path` and `log.offset`: Intermediate variables (`server_type`, `log_file_path`, `log_offset`) are now used before mapping to `event.idm.read_only_udm.additional.fields[`server_type`]`, `event.idm.read_only_udm.target.file.full_path` and `event.idm.read_only_udm.metadata.product_log_id` respectively.  
\- Refactored the parser logic for the mapping of `event.idm.read_only_udm.network.http.response_status_code` to avoid mapping of invalid values.  
\- All these changes fixed the issues related to the incorrect parsing of the log fields and also fixed some failing logs. As a result, the following UDM fields are now being mapped correctly:  
\- `event.idm.read_only_udm.metadata.collected_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.collected_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.product_version`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.network.application_protocol`  
\- `event.idm.read_only_udm.network.direction`  
\- `event.idm.read_only_udm.network.http.method`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.annotation[].key`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.annotation[].value`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_engine_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.browser_version`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.family`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.os`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.platform`  
\- `event.idm.read_only_udm.network.http.parsed_user_agent.sub_family`  
\- `event.idm.read_only_udm.network.http.referral_url`  
\- `event.idm.read_only_udm.network.http.user_agent`  
\- `event.idm.read_only_udm.network.sent_bytes`  
\- `event.idm.read_only_udm.observer.ip[]`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.asset.ip[]`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.ip[]`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.principal.process.pid`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels[].key`  
\- `event.idm.read_only_udm.principal.resource.attribute.labels[].value`  
\- `event.idm.read_only_udm.security_result[].description`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.asset.ip[]`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.ip[]`  
\- `event.idm.read_only_udm.target.url`  
2026-02-04 |  Enhancement:  
\- Added a condition to drop invalid logs.  
\- event.idm.read_only_udm.additional.fields: Changed key name for `sc_substatus` to `sc-substatus` in `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Changed mapping for `time_taken` to `time-taken` in `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AUID` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-01-22 |  Enhancement:  
\- Added a grok pattern to parse `sent_bytes` and `received_bytes` fields correctly.  
\- event.idm.read_only_udm.principal.asset.hardware.cpu_platform: Newly mapped `host.architecture` raw log field(s) with `event.idm.read_only_udm.principal.asset.hardware.cpu_platform` UDM field.  
\- event.idm.read_only_udm.principal.platform_patch_level: Newly mapped `host.os.kernel` raw log field(s) with `event.idm.read_only_udm.principal.platform_patch_level` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `host.os.version` raw log field(s) with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `host.os.platform` raw log field(s) with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.additional.fields[`os_name`]: Newly mapped `host.os.name` raw log field(s) with `event.idm.read_only_udm.additional.fields[`os_name`]` UDM field.  
\- event.idm.read_only_udm.additional.fields[`os_build`]: Newly mapped `host.os.build` raw log field(s) with `event.idm.read_only_udm.additional.fields[`os_build`]` UDM field.  
\- event.idm.read_only_udm.additional.fields[`geo_name`]: Newly mapped `host.geo.name` raw log field(s) with `event.idm.read_only_udm.additional.fields[`geo_name`]` UDM field.  
\- event.idm.read_only_udm.observer.asset_id: Newly mapped `agent.type`, `host.id` raw log field(s) with `event.idm.read_only_udm.observer.asset_id` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `log.file.path` raw log field(s) with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `agent.version` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `agent.id` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `agent.type` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels[`ecs:version`]: Newly mapped `ecs.version` raw log field(s) with `event.idm.read_only_udm.principal.asset.attribute.labels[`ecs:version`]` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `host.ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `host.ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `host.mac` raw log field(s) with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped `host.mac` raw log field(s) with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `tags` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.   
2025-10-24 |  Enhancement:  
\- Added grok pattern to support new pattern of SYSLOG logs.   
2025-10-08 |  Enhancement:  
\- Added support for a new log format, including fields like `ftp_command`, `ses`, and `http_response`.  
\- event.idm.read_only_udm.principal.application: Newly mapped `ftp_command` raw log field to `event.idm.read_only_udm.principal.application`.  
\- Modified the processing of the user_agent field to replace all occurrences of `+` with a `space` before mapping its value to event.idm.read_only_udm.network.http.user_agent.   
2025-09-26 |  Enhancement:  
\- Added support for JSON format.  
\- Enhanced grok patterns to parse new log format variations.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `source` and `IIS_source` raw log field to event.idm.read_only_udm.principal.resource.attribute.labels.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `cribl_breaker` and `total_CPU` raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cribl_pipe`, `DC`, `SubFleetName` and `total_memory` raw log field to event.idm.read_only_udm.additional.fields.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `Hostname` raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `host` raw log field to event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field to event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform: Newly mapped `OS_type` raw log field to event.idm.read_only_udm.principal.asset.platform_software.platform.  
\- event.idm.read_only_udm.target.ip: Newly mapped `Connection_IP` raw log field to event.idm.read_only_udm.target.ip.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `Connection_IP` raw log field to event.idm.read_only_udm.target.asset.ip.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `_time` raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `name` raw log field to event.idm.read_only_udm.target.resource.name.   
2025-09-24 |  Enhancement:  
\- Exchanged `entity` field with `information` field in grok patterns to extract `admin_domain` and `user_id`.  
\- Added grok pattern on `entity` field to extract `admin_domain` and `user_id` using grok patterns.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `admin_domain` field(s) with event.idm.read_only_udm.principal.administrative_domain UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` if present else mapped `entity` field(s) with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds: Newly mapped `time_taken_1` field(s) with event.idm.read_only_udm.network.session_duration.seconds UDM field.   
2025-09-17 |  Enhancement:  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `EventReceivedTime` raw log field(s) with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `facility` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `priority` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip1, principal_ip2` log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `principal_ip1, principal_ip2` log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` log field(s) with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Added conditional check if `request_url` is `/Login.aspx`.  
\- New grok patterns were added to parse new formats of the `message_data` field.  
\- New grok patterns were added to parse new formats of the SYSLOG.  
\- New grok patterns were added to parse different formats of the `user_agent` field, extracting `tls_version`, `only_agent`, `token_data`, `referrer_url`, `target_host`, and `target_port`.  
\- Added grok pattern to ensure `prin_ip` field is a valid IP address before mapping.   
2025-07-30 |  Enhancement:  
\- event.idm.read_only_udm.network.http.user_agent : Newly mapped `csUser-Agent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.parsed_user_agent : Newly mapped `csUser-Agent` raw log field with `event.idm.read_only_udm.network.http.parsed_user_agent` UDM field.  
\- event.idm.read_only_udm.network.http.referral_url : Newly mapped `csReferer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- event.idm.read_only_udm.additional.fields : Newly mapped `cs-uri-query` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.user.userid : Newly mapped `s_principal_user_userid` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain : Newly mapped `j_admin_domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.network.session_duration.nanos : Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.nanos` if duration < 1000 UDM field.  
\- event.idm.read_only_udm.network.session_duration.seconds : Newly mapped `duration` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` if duration > 1000 UDM field.  
\- event.idm.read_only_udm.network.sent_bytes : Newly mapped `bytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.   
2025-07-10 |  Enhancement:  
\- Added a grok pattern to retrieve relevant data.  
\- Replaced `host.hostname` to `host_hostname`.  
\- Added conditional check for `event1.idm.read_only_udm.network.http.parsed_user_agent`.  
\- Removed rebase fordate format `yyyy-MM-dd HH:mm:ss`.  
\- `event1.idm.read_only_udm.additional.fields`: Newly mapped `time_taken`, `time-taken`, `sc_win32_status`, `sc-win32-status`, `sc-substatus`, and `sc_substatus` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field`.   
2025-05-29 |  Enhancement:  
\- Added grok pattern to support new pattern of SYSLOG logs.  
\- Added grok pattern to retrieve `cloud_ray_id` and `x_forwarded_for`.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `cloud_ray_id` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event1.idm.read_only_udm.additional.fields: Newly mapped `X-ARR-LOG-ID` raw log field with `event1.idm.read_only_udm.additional.fields` UDM field.  
\- event1.idm.read_only_udm.intermediary.ip: Newly mapped `x_forwarded_for` raw log field with `event1.idm.read_only_udm.intermediary.ip` UDM field.  
\- event1.idm.read_only_udm.principal.user.userid: Newly mapped `uid` raw log field with `event1.idm.read_only_udm.principal.user.userid` UDM field.  
\- event1.idm.read_only_udm.network.session_id: Newly mapped `ses` raw log field with `event1.idm.read_only_udm.network.session_id` UDM field.  
\- event1.idm.read_only_udm.target.process.file.full_path: Newly mapped `exe` raw log field with `event1.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event1.idm.read_only_udm.target.hostname and event1.idm.read_only_udm.target.asset.hostname: Newly mapped `hostname` raw log field with `event1.idm.read_only_udm.target.hostname` and `event1.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event1.idm.read_only_udm.target.process.command_line: Newly mapped `comm` raw log field with `event1.idm.read_only_udm.target.process.command_line` UDM field.  
\- security_result.action_details: Newly mapped `res` raw log field with `security_result.action_details` UDM field.  
\- event1.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `subj` raw log field with `event1.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event1.idm.read_only_udm.target.user.userid: Newly mapped `UID` raw log field with `event1.idm.read_only_udm.target.user.userid` UDM field.  
\- event1.idm.read_only_udm.network.tls.version: Newly mapped `tls_version` raw log field with `event1.idm.read_only_udm.network.tls.version` UDM field.  
\- event1.idm.read_only_udm.target.group.product_object_id: Newly mapped `GID` raw log field with `event1.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- event1.idm.read_only_udm.metadata.product_event_type: Newly mapped `type` raw log field with `event1.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event1.idm.read_only_udm.principal.process.pid: Newly mapped `pid` raw log field with `event1.idm.read_only_udm.principal.process.pid` UDM field.  
\- event1.idm.read_only_udm.target.user.user_display_name: Newly mapped `OUID` raw log field with `event1.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event1.idm.read_only_udm.target.user.userid: Newly mapped `ouid` raw log field with `event1.idm.read_only_udm.target.user.userid` UDM field.   
2025-05-28 |  Enhancement:  
\- Added grok patterns to parse the unparsed logs.  
-`event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip`: Newly mapped to `SourceAddress` raw log field with `event1.idm.read_only_udm.principal.ip` and `event1.idm.read_only_udm.principal.asset.ip` UDM field.  
-`event1.idm.read_only_udm.principal.port`: Newly mapped to `SourcePort` raw log field with `event1.idm.read_only_udm.principal.port` UDM field.  
-`event1.idm.read_only_udm.target.ip` and `event1.idm.read_only_udm.target.asset.ip`: Newly mapped to `DestAddress` raw log field with `event1.idm.read_only_udm.target.ip` and `event1.idm.read_only_udm.target.asset.ip` UDM field.  
-`event1.idm.read_only_udm.target.port`: Newly mapped to `DestPort` raw log field with `event1.idm.read_only_udm.target.port` UDM field.   
2025-05-25 |  Enhancement:  
\- Added grok pattern to populate UDM fields.   
2025-03-03 |  Enhancement:  
\- Added grok pattern to parse targetip and targetport.  
\- Mapped `targetip` to `target.ip`.  
\- Mapped `targetport` to `target.port`.   
2025-02-20 |  Enhancement:  
\- Added an additional condition check [xff_ip] != [src_ip] to remove the IP address from the principal.ip field.   
2025-01-27 |  Enhancement:  
\- Added support to parse XML logs.   
2024-06-20 |  Enhancement:  
\- Mapped `streamid` to `additional.fields`.   
2024-06-11 |  Enhancement:  
\- Added a Grok pattern to parse unparsed logs.   
2024-02-18 |  Enhancement:  
\- Modified Grok pattern field names to map the value correctly.  
\- Modified name from `intermediary_devicename` to `observer_devicename`.  
\- Modified name from `src_ip` to `observer_ip`.  
\- Modified name from `dst_ip` to `principal_or_intermediary_ip`.  
\- Modified name from `xff_ips` to `principal_xff_ips`.  
\- Mapped `observer_ip` to `observer.ip`.  
\- Mapped `observer_devicename` to `observer.hostname`.  
\- Mapped `principal_xff_ips` to `principal.ip`.  
\- If `principal_xff_ips` is present, then mapped `principal_or_intermediary_ip` to `intermediary.ip`.  
\- If `principal_xff_ips` is not present, then mapped `principal_or_intermediary_ip` to `principal.ip`.   
2024-02-12 |  Enhancement:  
\- Added new Grok patterns to support the network logs with kv data.  
\- Mapped `sc-substatus` to `additional.fields`.   
2024-01-09 |  Enhancement:  
\- Added new Grok patterns to support the network logs with key-value data.  
\- Mapped `dst_ip2` to `target.ip`.  
\- Mapped `X-BackEndCookie`,`exchangecookie`, `OutlookSession`, `MapiContext`, `MapiRouting`, `content_type` and `MapiSequence` to `additional.fields`.   
2023-12-19 |  Enhancement:  
\- Mapped `Configuration` as a value to `metadata.product_event_type` if `EventType` is equal to `VERBOSE`.  
\- Mapped `Message` to `security_result.description`.  
\- Mapped `PhysicalPath` to `target.file.full_path`.  
\- Mapped `OldValue`, `NewValue`, `Configuration` and `ConfigPath` to `additional.fields`.   
2023-12-06 |  Enhancement:  
\- Mapped `@timestamp` to `metadata.event_timestamp`.  
\- Mapped `host.hostname` to `target.hostname`.  
\- Mapped `logstash.process.host` to `intermediary.hostname`.  
\- Mapped `logstash.collect.host` to `observer.hostname`.  
\- Mapped `_user` to `principal.user.userid`.  
\- Mapped `http_response` to `network.http.response_code`.  
\- Mapped `referer` to `network.http.referral_url`.  
\- Mapped `syslog_severity` to `security_result.severity_details`.  
\- Mapped `message` to `security_result.description`.  
\- When `_request_url` is `/login.aspx` and `_entity` is `AutoLogout=1`, then set `metadata.event_type` to `USER_LOGOUT`.  
\- When `_request_url` is `/login.aspx`, then set `metadata.event_type` to `USER_LOGIN`.   
2023-10-27 |  Enhancement:  
\- Mapped `Noun.hostname` and `Noun.asset.hostname` to the same value.  
\- Mapped `cIP` to `target.ip`.  
\- Mapped `csUriStem` to "`target.url`.  
\- Mapped `sPort` to `principal.port`.  
\- Mapped `csUserAgent` to `http.user_agent`.  
\- Mapped `sIP` to `principal.ip`.  
\- Mapped `csMethod` to `network.http.method`.  
\- Mapped `scStatus` to `http.response_code`.  
\- Mapped `sComputerName` to `target.hostname`.  
\- Mapped `_resourceId` to `target.resource.id`.  
\- Mapped `scBytes` to `network.sent_bytes`.  
\- Mapped `csBytes` to `network.received_bytes`.  
\- Mapped `sSiteName`, `TenantId`, `EventProcessedUtcTime`, `ManagementGroupName`, and `EventEnqueuedUtcTime` to `additional.fields`.  
\- Mapped `TimeGenerated` to `about.resource.attribute.labels`.  
\- Mapped `SourceSystem` to `security_result.detection_fields`.   
2023-06-23 |  Enhancement:  
Bug-Fix:  
\- Change in log Format  
\- Defined the grok for the changed log pattern  
\- Mapped cs-host to principal.application  
\- Mapped uristem & cs-uri-stem using if-else to target.url  
\- Mapped cs-version to network.tls.version_protocol  
\- Replaced the value of severity with the value in the field Level  
\- Replaced the value of sitename with s-sitename  
\- Replaced the value of UserSid with UserID  
\- Mapped AgentDevice as label key and value  
\- Mapped `app_name` to principal.application  
\- Mapped `ChannelID` to security_result.about.resource.attribute  
\- Mapped `Level` to security_result.severity  
\- Mapped `ExecutionProcessID` to principal.process.pid  
\- Mapped `ExecutionThreadID` to principal.process.product_specific_process_id  
\- Mapped `Domain` to principal.user.userid  
\- Mapped `UserID` to principal.user.windows_sid  
\- Mapped `AccountType` to principal.user.role_name   
2023-05-12 |  Enhancement - Parsed failing JSON logs  
\- Mapped `cshost` to `principal.hostname`  
\- Mapped `csusername` to `principal.user.user_display_name`.  
\- Mapped `sip` to `target.ip`.  
\- Mapped `uristem` to `target.url`.  
\- Mapped `sport` to `target.port`.  
\- Mapped `csversion` to `network.tls.version_protocol`.  
\- Mapped `csuseragent` to `network.http.user_agent`.  
\- Mapped `csip` to `principal.ip`.  
\- Mapped `xforwardedfor` to `principal.ip`.  
\- Mapped `csmethod` to `network.http.method`.  
\- Mapped `csreferer` to `network.http.referral_url`.  
\- Mapped `scstatus` to `network.http.response_code`.  
\- Mapped `computername` to `target.asset.hostname`.  
\- Mapped `scbyte` to `network.sent_bytes`.  
\- Mapped `csbyte` to `network.received_bytes`.  
\- Mapped `date` and `time` to `metadata.event_timestamp`.   
2023-03-01 |  Enhancement:  
\- Added support for JSON format logs having keys like: `c-*`, `s-*`, `cs-*`, `sc-*`.   
2022-10-25 |  Enhancement:  
\- Extracted `uri_query`,`intermediary_device_name`,`principal_username`,`sent_bytes`,`received_bytes` from log.  
\- Changed `dst_port` to `src_port`.  
\- Mapped `src_port` to `principal.port`.  
\- Updated `target.url` mapping to `request_url`+?+`uri_query`.  
\- Mapped `token_data` to `security_result.detection_fields` as `Cookie`.  
\- Mapped `sent_bytes` to `network.sent_bytes`.  
\- Mapped `received_bytes` to `network.received_bytes`.  
\- Mapped `intermediary_devicename` to `target.hostname` if `target_host` is empty, else mapped it to `intermediary.hostname`.  
\- Mapped `principal_username` to `principal.user.userid`.  
\- Mapped `Devicename` to `target.hostname` only when `target_host` is empty.  
\- Mapped `src_ip` to `principal.ip` if `xff_ips` is empty.  
\- If `xff_ips` is not empty:  
\- Mapped `src_ip` to `intermediary.ip`.  
\- Mapped `xff_ips` to `principal.ip`.  
\- Added a Grok pattern for additional logs types.   
2022-10-01 |  Enhancement:  
\- Wrote grok to parse unparse syslogs".  
\- Mapped `Severity` to `security_result.severity`.  
\- Mapped `UserName` to `target.user.userid`.  
\- Mapped `UserSid` to `target.user.windows_sid`.  
\- Mapped `ProviderKey` to `security_result.about.resource.attribute.labels`.  
\- Mapped `LayerKey` to `security_result.about.resource.attribute.labels`.  
\- Mapped `LayerName` to `security_result.about.resource.attribute.labels`.  
\- Mapped `LayerId` to `security_result.about.resource.attribute.labels`.  
\- Mapped `Weight` to `security_result.about.resource.attribute.labels`.  
\- Mapped `Conditions` to `security_result.about.resource.attribute.labels`.  
\- Mapped `Action` to `security_result.about.resource.attribute.labels`.  
\- Mapped `CalloutKey` to `security_result.about.resource.attribute.labels`.  
\- Mapped `CalloutName` to `security_result.about.resource.attribute.labels`.  
\- Mapped `Channel` to `security_result.about.resource.attribute.labels`.  
\- Mapped `FilterId` to `security_result.about.resource.attribute.labels`.  
\- Mapped `FilterKey` to `security_result.about.resource.attribute.labels`.  
\- Mapped `FilterName` to `security_result.about.resource.attribute.labels`.  
\- Mapped `FilterType` to `security_result.about.resource.attribute.labels`.  
\- Mapped `ProviderGuid` to `security_result.about.resource.attribute.labels`.  
\- Mapped `ProviderName` to `security_result.about.resource.attribute.labels`.  
\- Mapped `SourceName` to `security_result.about.resource.attribute.labels`.  
\- Mapped `SyslogSeverity` to `security_result.about.resource.attribute.labels`.  
\- Mapped `Category` to `security_result.category_details`.  
\- Mapped `EventType` to `metadata.product_event_type`.  
\- Mapped `EventID` to `metadata.product_log_id`.  
\- Mapped `ProcessID` to `principal.process.pid`.  
\- Mapped `SourceModuleName` to `target.resource.name`.  
\- Mapped `SourceModuleType` to `observer.application`.   
2022-09-30 |  Enhancement:  
\- Mapped xff header IPs to intermediary.ip.  
\- Mapped hostname to target.hostname.  
\- Added extra grok pattern to correctly parse certain logs with extra information and Mapped that extra information in additional fields.  
\- Mapped ASP.NET_Session_id to network.session_id.   
2022-03-30 |  Enhancement:  
\- Parse additional fields.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
