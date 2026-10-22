---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-wireless-changelog/
title: Change log for ARUBA_WIRELESS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:46:16.971355+00:00
---

# Change log for ARUBA_WIRELESS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/aruba-wireless-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARUBA_WIRELESS

Date | Changes  
---|---  
2026-04-03 |  Enhancement:  
\- Modified a grok pattern to parse new pattern of SYSLOG logs.  
\- Added support for `event_id` values `135906`, `135908`, `135014`, `135918`, and `135919` by parsing relevant raw log fields.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_code`, `function_name`, and `thread_id` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `station_macaddress` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `station_macaddress` raw log field with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `event_details` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-03-31 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version`, `priority`, `module` and `instance` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: If `syslog_severity` is `LOG_INFO`, updated the value of `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL`.  
\- Added support for new pattern of SYSLOG logs, this is allowing the following UDM fields to be mapped correctly:  
\- `event.idm.read_only_udm.metadata.description`  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.hostname`  
\- `event.idm.read_only_udm.principal.asset.hostname`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.target.process.pid`  
\- `event.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.security_result.severity_details`  
2026-03-18 |  Enhancement:  
\- Added a grok pattern on `event_details` to extract `session_id`, `role`, and `policy`.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles.name`: Newly mapped `role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles.name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `policy` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- Modified a grok pattern to parse dropped logs due to which the following UDM fields are now being parsed correctly:  
\- `event.idm.read_only_udm.metadata.event_type`  
\- `event.idm.read_only_udm.metadata.product_event_type`  
\- `event.idm.read_only_udm.metadata.product_name`  
\- `event.idm.read_only_udm.metadata.vendor_name`  
\- `event.idm.read_only_udm.principal.ip`  
\- `event.idm.read_only_udm.principal.asset.ip`  
\- `event.idm.read_only_udm.security_result.action`  
\- `event.idm.read_only_udm.security_result.summary`  
\- `event.idm.read_only_udm.target.ip`  
\- `event.idm.read_only_udm.target.asset.ip`  
\- `event.idm.read_only_udm.target.process.pid`  
\- `event.idm.read_only_udm.intermediary.hostname`  
\- `event.idm.read_only_udm.intermediary.ip`  
\- `event.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `event.idm.read_only_udm.metadata.log_type`  
\- `event.idm.read_only_udm.network.ip_protocol`  
\- `event.idm.read_only_udm.observer.ip`  
\- `event.idm.read_only_udm.principal.port`  
\- `event.idm.read_only_udm.security_result.severity`  
\- `event.idm.read_only_udm.security_result.severity_details`  
\- `event.idm.read_only_udm.target.application`  
\- `event.idm.read_only_udm.target.port`  
2026-01-08 |  Enhancement:  
\- Added on_error for the missing fields to avoid parsing failure.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_user` data field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `principal_domain` data field to `event.idm.read_only_udm.principal.administrative_domain` UDM field.   
2025-11-27 |  Enhancement:  
\- Newly added grok pattern for the `event_details` data field when event_id is `126002` or `126005`, `126047` or `127048` to parse the logs in correct manner in `aruba_wireless.include` file.  
\- Added conditional check for the `actor_mac` data field to parse the logs in correct manner.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `principalmac` data field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.severity_details`: Newly mapped `syslog_severity` data field to `event.idm.read_only_udm.severity_details` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly updated event_type to `SCAN_UNCATEGORIZED` when `principalmac` and `actor_mac` raw log field is not empty.   
2025-11-26 |  Enhancement:  
\- Added a new grok pattern to parse command execution events from msg_event_details.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `command_status` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when message contains `command executed successfully`.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `command_status` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field when message contains `command executed failed`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.ip` UDM field when `p_host` contains ip address.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field when `p_host` contains ip address.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field when `p_host` contains hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `p_host` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field when `p_host` contains hostname.   
2025-11-03 |  Enhancement:  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `t_user` raw log field(s) with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.ip:` Newly mapped `p_ip` raw log field(s) with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `p_ip` raw log field(s) with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `cmd` raw log field(s) with `event.idm.read_only_udm.target.process.command_line` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `node` raw log field(s) with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.type`: Newly mapped static value `SETTING` with `event.idm.read_only_udm.target.resource.type` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped static value `ALLOW` with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped static value `The command was executed successfully.` with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: If message contains `command executed successfully`, updated to SETTING_MODIFICATION.  
\- A new grok pattern was added to parse command execution events from msg_event_details.   
2025-10-16 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `product_id` field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `time1` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added conditional check for `username`.  
\- event.idm.read_only_udm.metadata.event_type: If event_type_value is empty, updated to `GENERIC_EVENT`.  
\- Added new grok patterns to parse different log structures for `event_id` 522035.  
\- Added gsub to replace `\\r\\n` with a space in the message field.  
\- Added `event_type` to overwrite.   
2025-10-09 |  Enhancement:  
\- Added support for events `125022` and `125024` with new grok patterns to parse additional fields and set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` and `event.idm.read_only_udm.extensions.auth.type` to `AUTHTYPE_UNSPECIFIED` for these events.  
\- Modified grok patterns for event IDs `125022` and `125024` to extract: `auth_status`, `userID`, `srcIP`, `srcPort`, `targetIP`, `targetPort`, and `app_protocol_src`.  
\- Added a grok pattern to extract `node` raw log field.  
\- Utilized `parse_app_protocol.include` to process the `app_protocol_src` field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `app_protocol_output` (derived from `app_protocol_src`) log field to `event.idm.read_only_udm.network.application_protocol`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `userID` log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `srcIP` log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `srcIP` log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `targetIP` log field to `event.idm.read_only_udm.target.ip`.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped `targetIP` log field to `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `security_result_action` (derived from `auth_status`) log field to `event.idm.read_only_udm.security_result.action`.   
2025-09-25 |  Enhancement:  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `msg` raw log field with event.idm.read_only_udm.security_result.summary UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `user` raw log field with event.idm.read_only_udm.principal.user.userid UDM field.  
\- event.idm.read_only_udm.principal.mac, event.idm.read_only_udm.principal.asset.mac: Newly mapped mac raw log field.  
\- event.idm.read_only_udm.target.mac, event.idm.read_only_udm.target.asset.mac: Newly mapped BSSID raw log field.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Newly mapped ESSID raw log field.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped ap_name raw log field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped VLAN, u_encr_alg, and m_encr_alg raw log fields.  
\- event.idm.read_only_udm.metadata.event_type: If principal_machine_id_present and target_machine_id_present are `true`, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.description: Statically set to `Station UP` for event_id `522035`.  
\- The grok filter was updated to support an additional CEF log format.   
2025-09-04 |  Enhancement:  
\- event.idm.read_only_udm.principal.ip: Newly mapped `principal_ip_value` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `p_port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.additional.fields.host_type: Newly added dynamic mapping of `p_port` to key `host_type` with appropriate error handling for `p_port_replace_failed` and `p_port_failed`.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `t_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If `principal_mid_present` is true, updated to `STATUS_UPDATE`.  
\- New Grok patterns were added to extract `t_hostname`, `principal_ip_value`, and `p_port` from raw logs.   
2025-08-05 |  Enhancement:  
\- Added a new grok pattern for the `msg_event_details` field to extract valid value.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `mac_1` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `IP` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `reason` raw log field to `event.idm.read_only_udm.security_result.description`.   
2025-07-29 |  Enhancement:  
\- Added a new grok pattern for the `message` field to parse the dropped logs in `aruba_wireless.include` file.  
\- Newly added grok pattern for `event_details` data field to parse those logs correctly when `event_id` in `126048` and `126049` in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.security_result.confidence_details` : Newly mapped `confidence_level` data field to `event.idm.read_only_udm.security_result.confidence_details` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `wifi_channel`, `band_frequency` data field with `event.idm.read_only_udm.additional.fields` UDM field in `aruba_wireless.include` file.  
\- Newly added condition check for the `user_ip` data field when `event_id` value is equal to `USER` in `aruba_wireless.include` file.  
\- Newly added grok pattern for the `msg_event_details` data field when `event_id` value is not equal to `NULL` and `msg_event_details` is not equal to `NULL` in `aruba_wireless.include` file to fetch the `prin_ip` and `tar_user_id` data field.  
\- `event.idm.read_only_udm.target.user.userid` : Newly mapped `tar_user_id` data field to `event.idm.read_only_udm.target.user.userid` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `prin_ip` data field to `event.idm.read_only_udm.principal.ip` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `tar_user_id` and `prin_ip` data field are not empty.  
\- Newly added grok pattern for the `event_id` data field when `event_id` value is in `125063`, `125067`, `125069`, `125065` in `aruba_wireless.include` file to fetch the `user_id` data field.  
\- `event.idm.read_only_udm.target.user.userid` : Newly mapped `user_id` data field to `event.idm.read_only_udm.target.user.userid` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.principal.user.userid` : Newly mapped `tar_user_id` data field to `event.idm.read_only_udm.principal.user.userid` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_CREATION` when `user_id` data field is not empty.  
\- Newly added grok pattern for the `event_id` data field when `event_id` value is in `125022`, `125024` in `aruba_wireless.include` file to fetch the `tar_user_id`, `prin_ip`, `principal_port` and `target_port` data field.  
\- `event.idm.read_only_udm.principal.ip` : Newly mapped `prin_ip` data field to `event.idm.read_only_udm.principal.ip` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.principal.port` : Newly mapped `principal_port` data field to `event.idm.read_only_udm.principal.port` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.target.port` : Newly mapped `target_port` data field to `event.idm.read_only_udm.target.port` UDM field in `aruba_wireless.include` file.  
\- `event.idm.read_only_udm.metadata.event_type` : Newly set `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` when `prin_ip` and `tar_user_id` data field are not empty.   
2024-12-27 |  Enhancement:  
\- Added a Grok pattern to support new pattern of syslog logs.   
2024-09-04 |  Enhancement:  
\- Added support for a new pattern of SYSLOG logs.   
2024-08-26 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.  
\- Mapped `details` to `metadata.description`.   
2024-06-18 |  Enhancement:  
\- Added support to handle unparsed SYSLOG logs.   
2024-04-18 |  Enhancement :  
\- Added a Grok pattern to extract valid value from `ap_name`.  
\- Mapped `ap_name` to `additional.fields`.   
2023-05-25 |  Bug-Fix :  
\- Parsed logs failing due to a different log pattern.   
2022-09-15 |  Bug-Fix :  
\- Modified grok pattern to parse logs which may have date field in the timestamp of log and also certain logs may not have key `userip` in the log.  
\- Modified `metadata.event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` wherever possible.   
2022-08-23 |  Enhancement-  
\- Migrated customer specific parser to default parser.  
\- Modified mapping for `metadata.event_type` from `GENERIC_EVENT` to `USER_RESOURCE_ACCESS` where event_id is `132053`.   
2022-03-30 |  Enhancement - Added following new Event Ids `124003`, `126037`, `126038`, `199801`, `235008`, `235009`, `304119`, `306602`, `326091`, `326098`, `326271`, `326272`, `326273`, `326274`, `326275`, `326276`, `326277`, `326278`, `326284`, `341004`, `350008`, `351008`, `358000`, `393000`, `399815`, `520013`, `522274`, `541004`  
Changed `metadata.event_type` where the `Event Id` is `126034`, `126064`, `127064`, `132006`, `132030`, `132093`, `132094`, `132197` from `GENERIC_EVENT` to `SCAN_UNCATEGORIZED`  
Changed `metadata.event_type` where the `Event Id` is `132207` from `GENERIC_EVENT` to `NETWORK_CONNECTION`  
Changed `metadata.event_type` where the `Event Id` is `520002` from `GENERIC_EVENT` to `USER_UNCATEGORIZED`  
Mapped `intermediary.hostname`, `intermediary.mac`, `intermediary.ip`, `target.application`, `target.process.pid`  
Mapped `logstash.irm_site`, `logstash.irm_environment`, `logstash.irm_region` to `additional.fields`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
