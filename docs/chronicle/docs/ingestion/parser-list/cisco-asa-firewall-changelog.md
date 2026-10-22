---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-asa-firewall-changelog/
title: Change log for CISCO_ASA_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:44:56.949514+00:00
---

# Change log for CISCO_ASA_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-asa-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_ASA_FIREWALL

Date | Changes  
---|---  
2026-09-21 |  \- Enhanced GROK pattern to accommodate the updated log format for Cisco ASA Firewall events.   
2026-09-10 |  \- Enhanced GROK pattern to accommodate the updated log format for event `733101`.   
2026-09-09 |  \- Enhanced GROK pattern to accommodate the updated log format for event `106023`.   
2026-09-01 |  \- Update the parser to separate the intermediary blocks for the hostname and IP UDM fields for Cisco event 113016, 317007, 317077, 317078, 604101, 713050, 713262, 402116, and 340002.   
2026-08-25 |  \- Enhanced GROK pattern to accommodate the updated log format for Cisco ASA Firewall events.   
2026-07-27 |  \- Updated the field mapping for the Cisco ASA Firewall parser. Please refer to the [parser documentation page](https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cisco-asa-firewall#udm_mapping_delta) for information regarding the updated UDM mappings.  
\- Added support of new events as part of Cisco ASA Firewall Refresher.   
2026-07-24 |  For Cisco ASA firewall events `106103`, `302013`, `302015`, `302016`, `722032`, `722033` and `722034`, the following mappings were changed to introduce more accurate mappings.  
\- `additional.fields[username]` : Removed mapping of `username` from `additional.fields[username]` UDM field for event `106103`, `302015` and `302016`.  
\- `principal.user.userid` : Mapped `username` raw log field with `principal.user.userid` UDM field for event `106103`, `302015` and `302016`.  
\- `target.ip`: Removed mapping of `dst_ip` raw log field from `target.ip` UDM field for event `722032`, `722033` and `722034`.  
\- `principal.ip`: Mapped `dst_ip` raw log field with `principal.ip` UDM field for event `722032`, `722033` and `722034`.  
\- `target.asset.ip`: Removed mapping of `dst_ip` raw log field from `target.asset.ip` UDM field for event `722032`, `722033` and `722034`.  
\- `principal.asset.ip`: Mapped `dst_ip` raw log field with `principal.asset.ip` UDM field for event `722032`, `722033` and `722034`.  
\- `target.user.userid`: Removed mapping of `user_name` from `target.user.userid` UDM field for event `722032`, `722033` and `722034`.  
\- `principal.user.userid`: Mapped `user_name` raw log field with `principal.user.userid` UDM field for event `722032`, `722033` and `722034`.  
\- `principal.asset.hostname`: Removed mapping of `sysloghost` from `principal.asset.hostname` UDM field for event `722032`, `722033` and `722034`.  
\- `principal.hostname`: Removed mapping of `sysloghost` from `principal.hostname` UDM field for event `722032`, `722033` and `722034`.  
\- `target.asset.hostname`: Mapped `sysloghost` raw log field with `target.asset.hostname` UDM field for event `722032`, `722033` and `722034`.  
\- `target.hostname`: Mapped `sysloghost` raw log field with `target.hostname` UDM field for event `722032`, `722033` and `722034`.   
2026-07-02 |  \- metadata.event_type: Removed mapping of `NETWORK_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead, for event id `602101` as it better reflects the nature of the event.   
2026-06-18 |  For Cisco ASA firewall events `113004` and `722036`, the following mappings were changed to introduce more accurate mappings.  
\- `principal.hostname` : Removed mapping of `sysloghost` from `principal.hostname` UDM field.  
\- `principal.asset.hostname` : Removed mapping of `sysloghost` from `principal.asset.hostname` UDM field.  
\- `principal.ip`: Mapped `dst_ip` raw log field with `principal.ip` UDM field for event `722036`.  
\- `target.ip`: Removed mapping of `dst_ip` raw log field from `target.ip` UDM field for event `722036`.  
\- `principal.asset.ip`: Mapped `dst_ip` raw log field with `principal.asset.ip` UDM field for event `722036`.  
\- `target.asset.ip`: Removed mapping of `dst_ip` raw log field from `target.asset.ip` UDM field for event `722036`.  
\- `security_result.summary`: Removed mapping of `summary` from `security_result.summary` UDM field for event `722036`.  
\- `network.received_bytes`: Mapped `received_bytes` raw log field with `network.received_bytes` UDM field for event `722036`.  
\- `metadata.event_type`: Removed mapping of `NETWORK_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `STATUS_UPDATE` instead, for event id `722036` as it better reflects the nature of the event.   
2026-06-02 |  Added support for new event ID 109210 and update the sysloghost mapping for event ID 113004 .  
\- `109210`: Added support for the event `109210` and relevant corresponding raw log fields.  
\- `113004`: If the hostname field contains an IP address, it will map to intermediary.ip and principal.ip. If it contains an actual hostname, it will map to principal.hostname and intermediary.hostname.   
2026-06-01 |  \- For Cisco ASA firewall events `302013` and `302015`, the following mappings were changed to introduce more accurate mappings for outbound directions.  
\- principal.ip: Removed mapping of `src_ip` from `principal.ip` UDM field.  
\- target.ip: Mapped `src_ip` raw log field with `target.ip` UDM field.  
\- principal.asset.ip: Removed mapping of `src_ip` from `principal.asset.ip` UDM field.  
\- target.asset.ip: Mapped `src_ip` raw log field with `target.asset.ip` UDM field.  
\- principal.port: Removed mapping of `src_port` from `principal.port` UDM field.  
\- target.port: Mapped `src_port` raw log field with `target.port` UDM field.  
\- principal.nat_ip: Removed mapping of `src_mapped_ip` from `principal.nat_ip` UDM field.  
\- target.nat_ip: Mapped `src_mapped_ip` raw log field with `target.nat_ip` UDM field.  
\- principal.user.userid: Removed mapping of `src_fwuser` from `principal.user.userid` UDM field.  
\- target.user.userid: Mapped `src_fwuser` raw log field with `target.user.userid` UDM field.  
\- target.ip: Removed mapping of `dst_ip` from `target.ip` UDM field.  
\- principal.ip: Mapped `dst_ip` raw log field with `principal.ip` UDM field.  
\- target.asset.ip: Removed mapping of `dst_ip` from `target.asset.ip` UDM field.  
\- principal.asset.ip: Mapped `dst_ip` raw log field with `principal.asset.ip` UDM field.  
\- target.port: Removed mapping of `dst_port` from `target.port` UDM field.  
\- principal.port: Mapped `dst_port` raw log field with `principal.port` UDM field.  
\- target.nat_ip: Removed mapping of `dst_mapped_ip` from `target.nat_ip` UDM field.  
\- principal.nat_ip: Mapped `dst_mapped_ip` raw log field with `principal.nat_ip` UDM field.  
\- target.user.userid: Removed mapping of `dst_fwuser` from `target.user.userid` UDM field.  
\- principal.user.userid: Mapped `dst_fwuser` raw log field with `principal.user.userid` UDM field.  
\- additional_fields[src_mapped_port]: Newly mapped `src_mapped_port` raw log field with `additional_fields[src_mapped_port]` UDM field.  
\- additional_fields[dst_mapped_port]: Newly mapped `dst_mapped_port` raw log field with `additional_fields[dst_mapped_port]` UDM field.   
2026-05-27 |  \- metadata.event_type: Removed mapping of `NETWORK_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead, for event id `722032`, `722033` and `722034` as it better reflects the nature of the event.  
\- network.ip_protocol: Newly mapped `protocol` raw log field with `network.ip_protocol` UDM field for event id `722032`, `722033` and `722034`.   
2026-04-21 |  \- metadata.event_type: Removed mapping of `USER_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `NETWORK_CONNECTION` instead, for event id `725006` as it better reflects the nature of the event.   
2025-12-16 |  \- `302037`: Added support for the event `302037` and relevant corresponding raw log fields.   
2025-12-08 |  \- principal.ip: Removed mapping of `Server IP` from `principal.ip` UDM field and mapped `User IP` instead for event `113005`.  
\- target.ip: Removed mapping of `User IP` from `target.ip` UDM field and mapped `Server IP` instead for event `113005`.   
2025-11-14 |  \- metadata.event_type: Removed mapping of `NETWORK_UNCATEGORIZED` from `metadata.event_type` UDM field and mapped `USER_LOGIN` instead, for event id `113015` as it better reflects the nature of the event.   
2025-11-11 |  \- Enhanced GROK pattern to accommodate the updated log format for event `716002`.   
2025-10-30 |  \- Enhanced GROK pattern to accommodate the updated log format for event `113039`.  
\- Revised event type to `USER_LOGIN` for event `716038`, as it better reflects the nature of the event.  
\- target.ip: Removed mapping of `IP` from `target.ip` UDM field for event `716038`.  
\- principal.ip: Mapped `IP` raw log field with `principal.ip` UDM field for event `716038`.   
2025-10-29 |  \- Enhanced GROK pattern to accommodate the updated log format for event `605005` & `722041`.   
2025-10-03 |  \- `324303`: Added support for the event `324303` and relevant corresponding raw log fields.   
2025-09-19 |  \- For cisco asa firewall events 722022, 722023, 722028, 722012, 113039, 606001, 611101, 611102, 611103, 611310, 611311, 716002, 716039, 772003, and 772004, the following mappings were changed in order to introduce more accurate mappings:  
\- principal.hostname: Removed mapping of `Cisco syslog host` from `principal.hostname` UDM field.  
\- target.hostname: Mapped `Cisco syslog host` raw log field with `target.hostname` UDM field.  
\- target.ip: Removed mapping of `Message Ip` from `target.ip` UDM field.  
\- principal.ip: Mapped `Message Ip` raw log field with `principal.ip` UDM field.  
\- For cisco asa firewall events 722022, 722023, 722028, and 722012 (message ID: 14), the following mappings were changed in order to introduce more accurate mappings:  
\- target.user.userid: Removed mapping of `Message User Id` from `target.user.userid` UDM field.  
\- principal.user.userid: Mapped `Message User Id` raw log field with `principal.user.userid` UDM field.  
\- target.user.group_identifiers: Removed mapping of `Message Group Name` from `target.user.group_identifiers` UDM field.  
\- principal.user.group_identifiers: Mapped `Message Group Name` raw log field with `principal.user.group_identifiers` UDM field.  
\- metadata.event_type : Removed mapping of `USER_LOGIN/USER_LOGOUT` from metadata.event_type UDM field and mapped `NETWORK_CONNECTION` instead.  
\- extensions.auth.type : Removed the static value mapping of `MACHINE` for extensions.auth.type UDM field.   
2025-09-17 |  \- Improved error handling to cover various edge cases across multiple scenarios.   
2025-08-26 |  \- security_result.severity: Removed the value `INFORMATIONAL` from `security_result.severity` UDM field and mapped the value `HIGH` instead when the `cisco_severity` is equal to 1.  
\- security_result.severity: Removed the value `INFORMATIONAL` from `security_result.severity` UDM field and mapped the value `LOW` instead when the `cisco_severity` is equal to 4.  
\- security_result.severity: Removed the value `INFORMATIONAL` from `security_result.severity` UDM field and mapped the value `LOW` instead when the `cisco_severity` is equal to 5.   
2025-06-10 |  Updated the GROK pattern to correctly parse the `principal.user.userid` UDM field for events 746012 and 746013.   
2025-06-05 |  Updated a GROK pattern to handle unparsed logs for `cisco_message_number` 721016\.   
2025-05-30 |  Added a GROK pattern to support multiple format logs for event 113011.   
2025-05-13 |  Added a GROK pattern to support multiple format logs for event 109100, 113009.   
2025-03-28 |  Updated a GROK pattern to handle unparsed logs issue for `cisco_message_number` 113022\.   
2025-01-09 |  \- Event 317077,317078  
\- Modified the Grok pattern to parse logs with trailing spaces in protocol field.   
2024-12-16 |  \- Modified the Grok pattern to parse the fields `src_interface_name` and `dst_interface_name`, which contains a colon inside their values.   
2024-10-09 |  \- Added support for message number 313005 and 710003 for action field to security_result.action = `BLOCK`.   
2024-08-16 |  \- Added support for `cisco_message_number` 302014 for `security_result.action_details` as `Teardown TCP connection`.   
2024-06-13 |  \- Updated Grok pattern for `cisco_message_number` 721018.  
\- Added support for `cisco_message_number` 317078\.   
2024-04-24 |  Updated Grok pattern for `cisco_message_number` 713016, 212005.   
2023-12-15 |  Updated Grok pattern for `cisco_message_number` 302014, 302015, and 302016.   
2023-12-13 |  Updated the Grok pattern to handle unparsed logs issue.   
2023-11-29 |  Aligned `principal/target.hostname` and `principal/target.asset.hostname` mapping.   
2023-09-06 |  \- Updated Grok pattern for `cisco_message_number` 302013\.   
2023-08-09 |  \- Updated Grok pattern for `cisco_message_number` 302014, 302015, and 302016.   
2023-06-14 |  Updated the parser to include `parse_network_http_user_agent` to use `Parsed User Agent` and `User Agent`.   
2023-05-17 |  \- Added support for logs with `<` and `>` characters where `cisco_message_number=722051`.   
2023-05-02 |  \- Updated mapping for the `ori_src_ip` and `ori_dst_ip` fields.   
2023-03-29 |  Changed validation for NETWORK_CONNECTION event.  
\- Extracted `asa_device_ip` from syslog header and mapped it to `observer.ip`.  
\- Changed mapping of user IP address from `target.ip` to `principal.ip` for  
cisco_message_number=113015.  
\- Updated Grok pattern for cisco_message_number=402116, 402119, 419003,  
713025,713034,104002.  
\- Added Grok pattern for cisco_message_number=713024, 210007.   
2022-12-20 |  Enhancement  
\- Updated the Grok pattern for cisco_message_number=113005, 737026.  
\- Added new Grok pattern for cisco_message_number=109201.  
\- Mapped metadata.event_type as USER_UNCATEGORIZED when principal.user.userid is not null.  
\- Mapped metadata.event_type as STATUS_UNCATEGORIZED when principal.ip is not null.   
2022-10-12 |  Bugfix  
\- Added new Grok pattern for cisco_message_number=302015 for outbound connection.   
2022-09-28 |  Promoted CISCO_ASA_FIREWALL parser to default. As part of promotion  
customer's symlink are also being removed.  
For the field mapping differences, see [https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/field-maps/cisco-firewall-map-changes>field mapping changes](https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/<code)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
