---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tipping-point-changelog/
title: Change log for TIPPING_POINT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:52:38.456415+00:00
---

# Change log for TIPPING_POINT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tipping-point-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TIPPING_POINT

Date | Changes  
---|---  
2026-02-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `column1` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column7` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `column8` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `column9` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `column10` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `column16` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column2` (key: `field1`), `column3` (key: `field2`), `column11` (key: `hit_count`), `column12` (key: `source_zone_name`), `column13` (key: `destination_zone_name`), `column14` (key: `incoming_physical_port`), `column15` (key: `vlan_id`), `column17` (key: `tipping_point_taxonomy_id`), `column20` (key: `sequence_number`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM fields.  
\- Modified a grok pattern to parse the raw fields from syslog.  
\- Added a conditional block to parse CSV data from `csv_data`.  
\- Fields `principal_application`, `field1`, `field2`, `security_action_details`, `description` are now populated from `column1`, `column2`, `column3`, `column4`, `column5` of the parsed CSV data, respectively.  
\- `event.idm.read_only_udm.metadata.event_timestamp`:  
\- If `column6` has 13 digits, Set the value to `column6`.  
\- If `column6` does not have 13 digits, Set the value to `rt_timestamp` from `column18`.  
\- `event.idm.read_only_udm.security_result.detection_fields`:  
\- If `column6` does not have 13 digits, Set the value of `event.idm.read_only_udm.security_result.detection_fields` to `column6` (key: `signature_protocol`).   
2026-01-22 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `hostname`, `suser`, `duser`, `sntdom`, `dntdom` raw log field(s) with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `user_role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `category` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `status_value` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Changed mapping for `event.idm.read_only_udm.target.hostname` to additionally map `dvchost` raw log field when `target.hostname` is empty.  
\- Updated `column1` grok pattern to support an additional log format for parsing `priority`, `timestamp`, `hostname`, `eventFormat`, `eventFormatVersion`.  
\- Added a new grok pattern to the `second_grok_failed` block for parsing `timestamp1`, `hostname`, `description`.   
2026-01-19 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.application`: Removed mapping of `intermediary_hostname` from `event.idm.read_only_udm.intermediary.application` UDM field, because this value represents the originating security device's hostname and is now correctly mapped to `event.idm.read_only_udm.intermediary.hostname` for accurate asset tracking and rule enforcement.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `intermediary_hostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-11-27 |  Enhancement:  
\- Added new grok patterns to parse new log formats.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `actionnumber` field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-11-25 |  Enhancement:  
\- Added new grok patterns to parse new log formats.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `signature_id`, `field1`, `field2`, `path`, `rule_details` field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip_1` field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `principal_application` field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `intermediary_application` field with `event.idm.read_only_udm.intermediary.application` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_host_ip_or_hostname` field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `intermediary_host_ip_or_hostname` field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `security_action_details` field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time1` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-09-17 |  Enhancement:  
\- Added GROK pattern to parse unparsed log.  
\- Consolidated redundant code for `"event.idm.read_only_udm.security_result.detection_fields`, `event.idm.read_only_udm.additional.fields`, `event.idm.read_only_udm.metadata.description`, `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `ip_address` raw log field to `event.idm.read_only_udm.principal.asset.ip` UDM field.   
2025-09-11 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Removed mapping for `event.idm.read_only_udm.security_result.action` when `actionnumber` or `action` is `3`,`9`,`12` mapped to `BLOCK`.  
\- event.idm.read_only_udm.security_result.action: Added mapping for `event.idm.read_only_udm.security_result.action` when `actionnumber` or `action` is `3`,`9`,`12` mapped to `ALLOW`.  
\- event.idm.read_only_udm.network.application_protocol: When protocol is `HTTP` then mapped `HTTP` to `event.idm.read_only_udm.network.application_protocol` UDM field.   
2025-08-07 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `product_event_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `target_resource_name` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `destination_zone_name`, `hit_count`, `incoming_physical_port`, `sequence_number`, `source_zone_name`, `tipping_point_taxonomy_id`, `vlan_id` raw log fields with `event.idm.read_only_udm.additional.fields UDM field`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `signature_uuid`, `signature_name`, `signature_number`, `signature_protocol` raw log fields with `event.idm.read_only_udm.security_result.detection_fields UDM field`.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` when `actionnumber` or `action` is in `1`,`3`,`6`,`9`,`12`,`16`,`18` mapped to `BLOCK` else if `actionnumber` is in `2`,`4`,`5`,`7`,`10`,`11`,`13` mapped to `ALLOW` else if `actionnumber` is in `0`,`17` mapped to `UNKNOWN`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` to `event.idm.read_only_udm.network.ip_protocol` if `protocol` (uppercased) is one of EIGRP, ESP, ETHERIP, GRE, ICMP, IGMP, IP6IN4, PIM, TCP, UDP, VRRP.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `protocol` to `event.idm.read_only_udm.network.application_protocol` when protocol is `HTTP` or `HTTPS`.  
\- `event.idm.read_only_udm.metadata.event_type`: Setting `event_type` to `NETWORK_CONNECTION` when `has_network` is `true` and `error_ip` is `false` and `error_target_ip` is `false`.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `intermediary_host` to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- Added gsubs to replace newline characters with spaces.   
2025-01-09 |  Enhancement:  
\- Added support for the new pattern of syslog logs.   
2024-10-15 |  Enhancement:  
\- Added support for the new pattern of syslog logs.   
2024-06-11 |  Enhancement:  
\- Added support for the new pattern of CSV logs.   
2024-04-02 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
