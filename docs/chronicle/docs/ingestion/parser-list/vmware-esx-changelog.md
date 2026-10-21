---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-esx-changelog/
title: Change log for VMWARE_ESX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T05:34:15.932381+00:00
---

# Change log for VMWARE_ESX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/vmware-esx-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VMWARE_ESX

Date | Changes  
---|---  
2026-08-26 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.command_line`: Removed mapping of `command` from `event.idm.read_only_udm.principal.process.command_line` UDM field in order to introduce accurate mapping.  
\- `event.idm.read_only_udm.target.process.command_line`: Mapped `command` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priority` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event.idm.read_only_udm.metadata.event_type` to PROCESS_LAUNCH when target process details and principal machine details are present.   
2026-07-07 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Added support to parse the `timestamp` raw log field with a new date format.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `prod_version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `build_num`, `build_option`, `last_start_time` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.   
2026-05-13 |  Enhancement:  
\- Added a grok pattern on `_raw` and `message_to_process` to parse the raw log correctly.  
\- Modified the existing grok pattern to parse the `login_time` field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `host_ip` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `reason` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `connection_info`, `cribl_breaker`, `debuglogsource`, `debuglocation`, `debugwg`, `debugpipe` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when required data is present in the logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `uniqueID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-20 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `subject` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `command` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `object`, `unique_identifier` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `status` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Added grok patterns on `message_to_process`.   
2026-03-31 |  Enhancement:  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` raw log field with event.idm.read_only_udm.principal.process.pid UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ver`, `duration_ms`, `process_component`, `correlation_id`, `logger_name`, `measurement_pt`, `provider_info`, `thread` raw log fields with `event.idm.read_only_udm.additional.fields UDM field.  
\- Added a conditional check before the already existing mapping of `intermediaryip` to `event.idm.read_only_udm.intermediary.ip`.  
\- Added a conditional check before the already existing mapping of `intermediaryip` to `event.idm.read_only_udm.intermediary.hostname`.   
2026-03-10 |  Enhancement:  
\- Added a Grok pattern on `message_to_process` to extract `auth_mechanism_detail`, `auth_context`, and `src_uid`.  
\- `event.idm.read_only_udm.target.user.product_object_id`: Newly mapped `src_uid` raw log field with `event.idm.read_only_udm.target.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels`: Newly mapped `auth_mechanism_detail` (key: `auth_mechanism_detail`), `auth_context` (key: `auth_context`) raw log fields with `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- Added support for ``sshd-session`` in the `service` field, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.extensions.auth.type`  
\- `event.idm.read_only_udm.principal.application`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.description`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.target.asset.hostname`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.hostname`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.process.command_line`  
\- `event.idm.read_only_udm.target.process.pid`  
2026-02-12 |  Enhancement:  
\- Added a specific grok pattern for logs containing `logged in` and `logged out` to override previous mapping logic, ensuring these structurally similar events are now parsed with updated UDM field assignments.  
\- Added a conditional check `pattern_failed_for_logged_in_and_logged_out` before main grok block.  
\- Added a conditional check `pattern_failed_for_logged_in_and_logged_out` in drop logic to prevent logs from dropping.  
\- Added a conditional check for `host_target_value` in the drop logic in `vmware_esx_hostd.include` file to prevent logs from dropping.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `iporhost` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field because the user/client (principal) is initiating the login to the host (target) and therefore, the hostname identifies the target of the login attempt.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `host_target` raw log field(s) with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `host_target` raw log field(s) with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.process.pid`: Removed mapping of `parent_pid` from `event.idm.read_only_udm.principal.process.pid` UDM field because it is process ID of the process running on the target entity.  
\- `event.idm.read_only_udm.target.process.pid`: Newly mapped `tar_pid` raw log field(s) with `event.idm.read_only_udm.target.process.pid` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Removed mapping of `target_username` from `event.idm.read_only_udm.target.user.userid` UDM field because the user is the actor (the one doing the logging in), so it's not target.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `USER1`, `user_principal` raw log field(s) with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Removed mapping of `dst_tar_ip` from `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field because IP address correctly associates the source IP address with the user and client that together constitute the entity initiating the login.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `ip_principal` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_principal` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `OPID` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `SID` raw log field(s) with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `loggedOUT`, `loggedIN` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `network_user_agent`, `UserAgent` raw log field(s) with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If `loggedOUT` is not empty, `has_principal_ip` is `true`, and `has_target` is `true`, updated to `USER_LOGOUT`.  
\- `event.idm.read_only_udm.metadata.event_type`: If `loggedIN` is not empty, `has_principal_ip` is `true`, and `has_target` is `true`, updated to `USER_LOGIN`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator_id`,`SUB`,`Event_id`,`number of API invocations` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- The following fields have been added as a result of the above mentioned changes:  
\- event.idm.read_only_udm.additional.fields  
\- event.idm.read_only_udm.network.http.user_agent  
\- event.idm.read_only_udm.principal.asset.ip  
\- event.idm.read_only_udm.principal.ip  
\- event.idm.read_only_udm.principal.user.userid  
\- event.idm.read_only_udm.target.hostname  
\- event.idm.read_only_udm.target.asset.hostname  
\- event.idm.read_only_udm.target.process.pid   
2026-01-27 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Changed mapping for `event.idm.read_only_udm.target.application` to `service` raw log field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Mapped `product_service` (internal field derived from `service`) to `event.idm.read_only_udm.metadata.product_event_type` UDM field, applied conditionally.   
2026-01-21 |  Enhancement:  
\- Modified the grok pattern for `message_to_process` to extract `login_status`  
\- Added a grok pattern for `hostd_result` to extract `login_status`, `user`, `srcip` fields.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `message_to_process` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field when `message_to_process` contains `Accepted password` then `event.idm.read_only_udm.metadata.product_event_type` UDM field is set to `Accepted password` else if `message_to_process` contains `Rejected password` then `event.idm.read_only_udm.metadata.product_event_type` UDM field is set to `Rejected password`.   
2025-12-29 |  Enhancement:  
\- Added grok pattern to support new pattern of SYSLOG logs.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `vmw_vcenter` raw log field to `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `vmw_object_id` raw log field to `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `vmw_cluster` and `vmw_datacenter` raw log field to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `vmw_vr_ops_id` and `vmw_vcenter_id` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type to USER_LOGOUT and `event.idm.read_only_udm.extensions.auth.type` to MACHINE when `event_action` is `logged out`.   
2025-12-23 |  Enhancement:  
\- Added a new grok pattern to parse `Rejected password` events.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `srcip` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `session` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originator` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-12-22 |  Enhancement:  
\- Added a grok pattern to parse the new log format.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `target_url` raw log field with `event.idm.read_only_udm.target.url` UDM field.   
2025-12-15 |  Enhancement:  
\- Added new grok patterns to support additional log formats and extract new fields: event_code, session_ts, event_type, log_level, user_data, source_device, eventId_1, and session.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped session_ts raw log field to event.idm.read_only_udm.metadata.collected_timestamp.  
\- event.idm.read_only_udm.target.application: Newly mapped `service` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `source_device` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `location_1` raw log field to `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `priority_1` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `eventId_1`, `user_data`, `event_code` and `facility` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `session`, `log_level` and `event_type` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-11-27 |  Enhancement:  
\- Added grok pattern to support new pattern of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `ts` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `User` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `api_invocations`, `login_time`, `eventId`, and `facility` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `sub` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.location.name`: Newly mapped `location_1` raw log field to `event.idm.read_only_udm.target.location.name` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `user_1` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `sid` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.network.http.user_agent`: Newly mapped `useragent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `priority_1` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_action` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-10-30 |  Enhancement:  
\- `event.idm.read_only_udm.observer.hostname`: Removed mapping of `logstash.collect.host` from `event.idm.read_only_udm.observer.hostname` UDM field as it contains an IP address.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `logstash.collect.host` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `syslog_facility_code`, `logstash.irm_site`, `logstash.irm_environment`, `syslog_pri`, `syslog_severity_code`, `syslog_facility` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `logstash.irm_region` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `syslog_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `logstash.process.timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.   
2025-05-30 |  Enhancement:  
\- Added grok pattern to support new pattern of SYSLOG logs.  
\- Replaced vmware_esx_fdm.include with actual code.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field  
\- event.idm.read_only_udm.principal.port: Newly mapped `src_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field   
2025-05-23 |  Enhancement:  
\- event.idm.read_only_udm.principal.user.last_login_time: Newly mapped `login_date_time` raw log field with `event.idm.read_only_udm.principal.user.last_login_time` UDM field  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM field  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field  
\- event.idm.read_only_udm.target.hostname: Newly mapped `tar_hostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field  
\- event.idm.read_only_udm.additional.fields: Newly mapped `target_cloud_environment` raw log field with `event.idm.read_only_udm.additional.fields` UDM field  
\- Added the grok patterns in order to extract the values from `event.idm.read_only_udm.metadata.description` UDM field.   
2025-05-05 |  Enhancement:  
\- Added Gsub to replace `\\n` with ` ` on `message` to parse the logs.  
\- Added Grok pattern to extract `interm_hostname` from the log.  
\- Added conditional check before dropping logs.  
\- event.idm.read_only_udm.intermediary.ip, event.idm.read_only_udm.intermediary.hostname: Newly mapped `interm_hostname` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field if it is a valid IP else mapped it to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Changes made in `vmware_esx_dfwpktlogs_firewall.include` file :  
\- Added `on_error` handling to the existing mapping of `syslog_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field and updated `has_intermediary` flag.  
\- Added `on_error` handling to the existing mapping of `iporhost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field and updated `has_intermediary` flag.  
\- Changes made in `vmware_esx_rhttpproxy.include` file :  
\- Added `on_error` handling to the existing mapping of `syslog_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field and updated `has_intermediary` flag.  
\- Added `on_error` handling to the existing mapping of `iporhost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field and updated `has_intermediary` flag.  
\- Changes made in `vmware_esx_vrops.include` file :  
\- Added `on_error` handling to the existing mapping of `syslog_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field and updated `has_intermediary` flag.  
\- Added `on_error` handling to the existing mapping of `iporhost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field and updated `has_intermediary` flag.   
2025-04-29 |  Enhancement:  
\- Added Support to parse the new pattern of unparsed logs.  
\- event.idm.read_only_udm.principal.process.pid: Newly Mapped `parent_pid` raw log field with `event.idm.read_only_udm.principal.process.pid` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped httpdDetails` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `ip` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- event.idm.read_only_udm.principal.assest.ip: Newly Mapped `ip` raw log field with `event.idm.read_only_udm.principal.assest.ip` UDM Field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `result` raw log field with `event.idm.read_only_udm.security_result` UDM Field.   
2025-04-21 |  Enhancement:  
\- Added Grok patterns to parse the unparsed raw logs.  
\- Added `has_principal` flag for `principal_hostname`,`iporhost`,`fields.host`,`host.hostname` raw log fields.  
\- Added `has_principal_ip` flag for `host.ip`,`syslog_ip` raw log fields.  
\- Added `has_target` flag for `syslog_host` raw log field.  
\- Changes made in `vmware_esx_named_dns.include` file :  
\- Added a `has_principal_value` flag as a conditional check before drop condition.  
\- Changes made in `vmware_esx_rhttpproxy.include` file :  
\- Added a Grok pattern to parse the unparsed raw logs.  
\- Changes made in `vmware_esx_vpxa.include` file :  
\- Added a Grok pattern to parse the unparsed raw logs.  
\- Added a separate mutate block for `sub`,`task_service`,`op_id`,`application`,`iporhost` raw log fields.  
\- Added `has_principal_ip_value`, `has_principal_value`, `has_principal_host` and `has_target_ip`, `has_target`, `has_target_process` flags before mapping `PROCESS_LAUNCH` event type.  
\- Added `has_principal_ip_value`, `has_principal_value` flags before mapping `STATUS_UPDATE` event type.   
2025-04-01 |  Enhancement:  
\- Updated changelog.txt file.   
2025-03-12 |  Enhancement:  
\- Added Grok patterns to parse login and logout events  
\- Mapped `op_id` to `metadata.product_log_id`.  
\- Mapped `sid` to `network.session_id`.  
\- Mapped `target_username` is mapped to `target.user.userid`.  
\- Set `metadata.event_type` to `USER_LOGIN` and `USER_LOGOUT` for successful `logged in` and `log out` events respectively.  
\- Mapped `iporhost` to `principal.hostname`.  
\- Mapped `dst_tar_ip` to `target.ip` and `target.asset.ip`.  
\- Mapped `iporhost` to `principal.hostname` and `principal.asset.hostname`.   
2025-02-11 |  Enhancement:  
\- Added Grok patterns to parse `login/logout` events correctly.   
2024-07-01 |  Enhancement:  
\- Added support for a new pattern of Syslog logs.   
2024-06-11 |  Enhancement:  
\- Added support for a new pattern of Syslog logs.   
2024-06-03 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-05-09 |  Enhancement:  
\- Added support for new pattern of `snmpd` and `Rhttpproxy` logs.  
\- Mapped `prod_event_type` to `metadata.product_event_type`.  
\- Mapped `context` to `additional.fields`.   
2024-02-07 |  Bug-Fix:  
\- Added new Grok patterns to support the SYSLOG logs which are getting dropped.  
\- Mapped `newVersion` and `filter` to `security_result.detection_fields`.  
\- Mapped `description` to `security_result.description`.   
2023-10-10 |  Enhancement:  
Modified the following JSON key names using the gsub function:  
\- `service` to `serv`.  
\- `event` to `log_event`.  
\- `@timestamp` to `timestamp`.  
\- `@version` to `version`.  
Added new Grok patterns to handle the JSON logs with new fields.  
Matched the `timestamp` to `RFC 3339` and `TIMESTAMP_ISO8601` formats.  
Mapped `host.hostname` to `principal.hostname`.  
Mapped `host.ip` to `principal.ip`.  
Mapped `type`, `serv.type`, `log.syslog.facility.code`, `log.syslog.facility.name`, `log.syslog.severity.code`, `log.syslog.severity.name`, and `log.syslog.priority` to `additional.fields`.  
Mapped `process.name` to `service`.  
Mapped `version` to `metadata.product_version`.  
Mapped `severity` to `security_result.severity`.   
2023-09-25 |  Enhancement:  
\- Added new Grok patterns to handle the new type of SYSLOG for VMware ESXi.  
\- Mapped `app_name` to `principal.application`.  
\- Mapped `severity` to `security_result.severity`.   
2023-07-17 |  Bug_fix - Mapped `username` to `target.user.userid`.  
Mapped `pid` to `principal.process.pid`.  
Mapped `description` to `metadata.description`.   
2023-06-12 |  Bug_fix - Modified mapping of `session` for type `vmauthd`. Mapped it to `network.session_id`.   
2022-09-01 |  Bug_fix - Unmapped principal.namespace from its hardcoded value.   
2022-08-24 |  Enhancement - - Added new date type to parse dates of format `yyyy-MM-ddTHH:mm:s`.   
2022-08-03 |  Enhancement - Added the grok patterns to handle the logs with service :- hostd, vmon andd vrops.   
2022-07-26 |  Enhancement -  
Where `service` is equal to `Rhttpproxy`  
\- Modified mapping for `principal.namespace`.  
\- Mapped `namespace` to `additional.fields`.  
Where `service` is equal to `crond`  
\- Mapped `parent_pid` to `target.process.parent_process.pid`.   
2022-07-05 |  Bugfix - Updated the parser to match the timestamp in `yyyy-MM-ddTHH:mm:ss.SSSS` format.   
2022-06-13 |  Enhancement - Modified/Added the grok patterns to handle the logs with service :- hostd, sendmail, sshd, sudo, vmcad, vmon, vpxd, vrops.  
Bugfix - Modified `metadata.event_type` for `vmauthd` logs from `USER_LOGIN` to `GENERIC_EVENT`.   
2022-05-02 |  Bugfix - As per the user requirement, target.hostname mapping changed to principal.ip for the logs which have service as `Hostd`.   
2022-04-13 |  Enhancement-Parsed the logs having the following service names: hostd-probe, vmkernel, vmkwarning, Fdm, netcpa, root, hpHelper, snmpd, etc.  
Mapped logstash.ingest.timestamp to metadata.ingested_timestamp,  
logstash.ingest.host and logstash.process.host to intermediary.hostname,  
logstash.collect.host to observer.hostname.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
