---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ios-changelog/
title: Change log for CISCO_IOS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:31:24.362137+00:00
---

# Change log for CISCO_IOS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-ios-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_IOS

Date | Changes  
---|---  
2026-05-27 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page `https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-ios`.   
2026-04-14 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Removed mapping of `userName` from `event.idm.read_only_udm.principal.user.userid` UDM field because `userName` is the identifier of the account on the target system that the login process is attempting to authenticate.  
\- `event.idm.read_only_udm.target.user.userid`: Mapped `userName` field with `event.idm.read_only_udm.target.user.userid` UDM field if `cisco_mnemonic` contains `SSH2_USERAUTH`.  
\- `event.idm.read_only_udm.security_result.severity`: Removed mapping of `severity` from `LOW` if `cisco_severity` is `0` because at `0` the system is unusable.  
\- `event.idm.read_only_udm.security_result.severity`: Mapped `severity` to `CRITICAL` if `cisco_severity` is `0`.  
\- Modified a grok pattern to parse the raw log correctly.  
\- Added grok patterns to populate the valid IP addresses.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Modified the `timestamp` field by appending `timezone` in order to parse the `event.idm.read_only_udm.metadata.event_timestamp` correctly.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` and `prin_ip` fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN` for the SSH login events.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` from `STATUS_UPDATE` to `USER_UNCATEGORIZED` based on required data.   
2026-02-11 |  Enhancement:  
\- A new grok pattern is used to extract `User` and logged command from the `cisco_message` and mapped to `event.idm.read_only_udm.target.user.userid`.  
\- Added grok patterns to parse new formats of SYSLOG logs, allowing the following UDM fields to be mapped correctly:  
\- `events.idm.read_only_udm.intermediary.hostname`  
\- `events.idm.read_only_udm.metadata.description`  
\- `events.idm.read_only_udm.metadata.event_timestamp.nanos`  
\- `events.idm.read_only_udm.metadata.event_timestamp.seconds`  
\- `events.idm.read_only_udm.metadata.event_type`  
\- `events.idm.read_only_udm.metadata.log_type`  
\- `events.idm.read_only_udm.metadata.product_event_type`  
\- `events.idm.read_only_udm.metadata.product_log_id`  
\- `events.idm.read_only_udm.metadata.product_name`  
\- `events.idm.read_only_udm.metadata.vendor_name`  
\- `events.idm.read_only_udm.principal.asset.ip`  
\- `events.idm.read_only_udm.principal.ip`  
\- `events.idm.read_only_udm.principal.process.command_line`  
\- `events.idm.read_only_udm.security_result.rule_name`  
\- `events.idm.read_only_udm.security_result.severity`  
\- `events.idm.read_only_udm.security_result.severity_details`  
\- `events.idm.read_only_udm.target.user.userid`  
2026-01-24 |  Enhancement:  
\- Added a grok pattern to parse the log.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `application` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2026-01-20 |  Enhancement:  
\- Added a new grok pattern to parse the new format of raw log.  
\- event.idm.read_only_udm.metadata.event_type: If `principal_userid_present` flag is `true` then mapped `USER_UNCATEGORIZED` to `event.idm.read_only_udm.metadata.event_type` UDM field.   
2025-12-30 |  Enhancement:  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `userName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_host` raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If cisco_tag is SEC_LOGIN-4-LOGIN_FAILED and target_userid_present is true, updated to USER_LOGIN.  
\- A new grok pattern was added to optionally parse intermediary_host from the log.   
2025-12-05 |  Enhancement:  
\- Modified a grok pattern to parse unparsed logs.  
\- Added few grok patterns to parse new pattern of logs.  
\- event.idm.read_only_udm.target.mac: Newly mapped `target_mac` raw log field with `event.idm.read_only_udm.target.mac` UDM field.  
\- event.idm.read_only_udm.target.asset.mac: Newly mapped `target_mac` raw log field with `event.idm.read_only_udm.target.asset.mac` UDM field.   
2025-11-07 |  Enhancement:  
\- Added a grok pattern to parse the `hostname`.   
2025-10-23 |  Enhancement:  
\- A new grok pattern was added to parse specific syslog formats and extract fields like product_log_id, inter_host, date_time, zone, cisco_tag, and cisco_message.   
2025-10-15 |  Enhancement:  
\- Added a grok pattern to parse new log formats.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `fqdn` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.   
2025-10-06 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` raw log field(s) with event.idm.read_only_udm.intermediary.hostname UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `intermediary_host` raw log field(s) with event.idm.read_only_udm.intermediary.asset.hostname UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `domain` raw log field(s) with event.idm.read_only_udm.principal.administrative_domain UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `zone` raw log field(s) with event.idm.read_only_udm.additional.fields UDM field, using the key `Timezone`.  
\- Added conditional check for `userName`. If `userName` matches the `domain\user` format, it is parsed to extract the `user`. This `user` part is then mapped to `event.idm.read_only_udm.principal.user.userid`. If `userName` does not match this format, the original `userName` value is mapped to `event.idm.read_only_udm.principal.user.userid  
\- The parser logic has been updated to support new log formats.  
\- The parser was also updated to extract `domain` and `dst_user` from messages where the user is in the format `domain\user`.  
\- `event.idm.read_only_udm.metadata.event_type`: If cisco_tag is SEC_LOGIN-5-LOGIN_SUCCESS, updated to USER_LOGIN.  
\- For SEC_LOGIN-5-LOGIN_SUCCESS events, this extracted user is mapped to event.idm.read_only_udm.target.user.userid.   
2025-08-21 |  Enhancement:  
\- Modified grok patterns to correctly extract `product_log_id` separately from `intermediary_host`. This changes the value populated in `event.idm.read_only_udm.intermediary.hostname` for some log formats.  
\- Refined the condition for mapping `dst_user` to `event.idm.read_only_udm.target.user.userid` to exclude `from` as a value.   
2025-08-05 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.hostname` if `src_ip` is not a valid IP.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `src_ip` raw log field to `event.idm.read_only_udm.principal.asset.hostname` if `src_ip` is not a valid IP.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `description` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- Added new grok patterns to parse different syslog formats.  
\- Added grok pattern to extract date/time components from `cisco_message`.  
\- Enhanced grok patterns for `cisco_message` to extract description and improve handling of whitespace variations.  
\- Updated `userName` empty check to include spaces.   
2025-07-09 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.ip: Removed mapping of `src_ip` from `event.idm.read_only_udm.principal.ip` UDM field and mapped `inter_host` to `event.idm.read_only_udm.intermediary.ip` UDM field as the IP value in the header represents an intermediary device involved in the event, not the principal device that initiated the action.  
\- Moved the grok pattern to properly parse the logs as Ip value in the header getting mapped to `principal.ip` but the requirement is to map it to `intermediary.ip`.  
\- Added grok pattern for `description` field to parse additional information like `interface`.  
\- event.idm.read_only_udm.intermediary.labels: Newly mapped `interface` log fields with `event.idm.read_only_udm.intermediary.labels` UDM field.  
\- Added grok pattern for `cisco_message` field to parse additional information like `tty_number`, `cipher` and `hmac_algorithm`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `tty_number` and `hmac_algorithm` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.network.tls.cipher: Newly mapped `cipher` log fields with `event.idm.read_only_udm.network.tls.cipher` UDM field.  
\- Added a grok pattern for `src_ip` field to identify IP addresses.   
2025-06-30 |  Enhancement:  
\- Added a Grok pattern to parse a new format of syslog logs.  
\- Modified `date_time` raw log field to parse `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-06-23 |  \- Modified Grok pattern to parse additional information like `process_name` and `pid` from a new format of syslog logs.  
\- Modified variable name of IP address coming in the header from `source_facility` to `device_os` to map it to `event.idm.read_only_udm.additional.fields` UDM field instead of `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields. This is done because the value `CISCO-IOS-XR` is name of a device OS and not a hostname.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `device_os` and `device_component` log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added gsub and a date pattern to parse `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Modified variable name of IP address coming in the header from `src_ip` to `inter_host` to map it to `event.idm.read_only_udm.intermediary.ip` UDM field instead of `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields. This is done because IP Address/ Hostname data in the header belongs to `intermediary` UDM field instead of `principal` UDM field.   
2025-05-29 |  Bug-Fix:  
\- event.idm.read_only_udm.intermediary.ip, event.idm.read_only_udm.intermediary.asset.ip: Removed mapping of `target_ip` from `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM field and mapped `target_host` instead.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `sec_action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- if `sec_action` is `denied` then set to `BLOCK`.  
\- if `sec_action` is `permitted` then set to `ALLOW`.  
\- event.idm.read_only_udm.network.sent_bytes: Newly mapped `session_packet` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- Added support to parse a new format of syslog logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `missed_packets` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-05-14 |  Enhancement:  
\- Added support to handle timezone like `SGT`, `JST`, `HKG`, and `CN` for `event.idm.read_only_udm.metadata.event_timestamp` UDM field mapping by including timezone.   
2025-05-08 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity: Removed mapping of `ALERT` from `event.idm.read_only_udm.security_result.severity` UDM field and mapped `LOW` instead.   
2025-04-29 |  Enhancement:  
\- event.idm.read_only_udm.intermediary.hostname: Removed mapping of `inter_host`, `target_host`, `intermediary_host` from `event.idm.read_only_udm.intermediary.hostname` UDM field, when `inter_host`, `target_host`, `intermediary_host` are valid IP's.  
\- event.idm.read_only_udm.intermediary.ip: Mapped `inter_host`, `target_host`, `intermediary_host` raw log fields with `event.idm.read_only_udm.intermediary.ip` UDM field when `inter_host`, `target_host`, `intermediary_host` are valid IP's.  
\- Added a Grok pattern to parse a new format of syslog logs.  
\- event.idm.read_only_udm.principal.hostname: Removed mapping of `source_facility` from `event.idm.read_only_udm.principal.hostname` UDM field by modifying Grok pattern.  
\- event.idm.read_only_udm.intermediary.hostname: Mapped `inter_host` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field by modifying Grok pattern.   
2025-04-24 |  Enhancement:  
\- Added support to handle `event.idm.read_only_udm.metadata.event_timestamp` UDM field mapping by including timezone.   
2025-04-10 |  Enhancement:  
\- Added a Grok patterns to parse a new format of SYSLOG logs.  
\- event.idm.read_only_udm.metadata.event_timestamp: Added a new date pattern to map `ts` to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-03-18 |  Enhancement:  
\- Added a grok pattern to parse a new format of syslog logs.   
2025-03-17 |  Enhancement:  
\- Added a grok pattern to extract user name, and source port from the cisco_message field.  
\- Mapped the extracted user name to principal.user.userid.  
\- Based on existing mapping src_port will be mapped to principal.port.   
2025-03-14 |  Enhancement:  
\- Added grok patterns to parse a new format of syslog logs.   
2025-03-12 |  Enhancement:  
\- Added Grok patterns to parse new format of logs.  
\- Mapped `tls_cipher` to `network.tls.cipher`.  
\- Mapped `tls_client` to `network.tls.client.supported_ciphers`.  
\- Mapped `Chassis_data` to `additional.fields`.  
\- Mapped `timezone` to `additional.fields`.  
\- Mapped `cisco_message` to `network.application_protocol`.   
2025-03-11 |  Enhancement:  
\- Added new Grok patterns to parse new format of syslogs.  
\- Matched `date_time` to `ISO8601`.  
\- Mapped `metadata.event_type` to `USER_LOGIN` and `USER_LOGOUT` for successful authentication and logout events, respectively.  
\- Mapped `extensions.auth.type` to `AUTHTYPE_UNSPECIFIED`  
2025-03-04 |  Enhancement:  
\- Added support for a new format of (SYSLOG + KV) logs.  
\- Mapped `type` to `metadata.product_event_type`.  
\- Mapped `client_mac` to `principal.mac` and `principal.asset.mac`.  
\- Mapped `sequence_id`,`vap`, `band`, `channel`, `rssi`, `aid` and `radio` to `additional.fields`.   
2025-02-11 |  Enhancement:  
\- Added support for a new syslog log format.   
2025-01-23 |  Enhancement:  
\- Added support for a new syslog log format.   
2025-01-02 |  Enhancement:  
\- Added support for a new syslog log format.   
2024-12-27 |  Enhancement:  
\- Added support for a new syslog log format.   
2024-11-25 |  Enhancement:  
\- Added a Grok pattern to parse new logs.  
\- Mapped hostname in syslog header to `intermediary.hostname` from `target.hostname`.   
2024-11-19 |  Enhancement:  
\- Added support for a new format of syslog logs.   
2024-10-28 |  Enhancement:  
\- Added a Grok pattern to parse new logs.   
2024-10-24 |  Enhancement:  
\- Added a Grok pattern to parse new logs.   
2024-10-01 |  Enhancement:  
\- Added a Grok pattern to parse new logs.   
2024-07-04 |  Enhancement:  
\- Added support for a new pattern of syslog logs.   
2024-04-02 |  Enhancement:  
\- Added a new Grok pattern to parse new log type.  
\- Mapped the new fields to corresponding UDM fields.   
2023-10-04 |  Enhancement:  
\- Added a new Grok pattern to parse new log type.  
\- Mapped `source_facility` to `principal.hostname`.   
2023-08-11 |  Enhancement:  
\- Mapped `intermediary.ip` when message contains `HOST=`.  
\- Mapped `principal.user.userid` when message contains `User:`.  
\- Mapped `principal.process.command_line` when message contains `command:`.  
\- Mapped `target.user.userid` when message contains `username`.  
\- Mapped `metadata.event_type` to a more specific `metadata.event_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
