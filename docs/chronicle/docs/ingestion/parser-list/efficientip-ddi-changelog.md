---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/efficientip-ddi-changelog/
title: Change log for EFFICIENTIP_DDI \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:28:13.127177+00:00
---

# Change log for EFFICIENTIP_DDI  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/efficientip-ddi-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for EFFICIENTIP_DDI

Date | Changes  
---|---  
2026-07-06 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Modified mapping of `EFFICIENTIP_DDI DHCP` from `event.idm.read_only_udm.metadata.product_name` UDM field and mapped `EFFICIENTIP_DDI` instead.  
\- Modified a grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `system` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `subsystem` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `device` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `serial` and `cam_status` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `scsi_status`, `scsi_sense` and `CDB` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: If `type` is `error`, updated the value of `event.idm.read_only_udm.security_result.severity` to `ERROR`, else if `type` is info set to `INFORMATIONAL`, else if type is `warn` set to `WARNING`.   
2026-07-03 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields.  
\- Added a grok pattern on `data` to extract `raw_dns_flags`, `answer_ip`, `a_record_name`, `cname_ttl`, `cname_record_type`, `cname_target` fields.  
\- `event.idm.read_only_udm.about.hostname`: Newly mapped `client_name` raw log field with `event.idm.read_only_udm.about.hostname` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.data`: Newly mapped `answer_ip` and `cname_target` raw log field with `event.idm.read_only_udm.network.dns.answers.data` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.name`: Newly mapped `a_record_name` and `queried_domain` raw log field with `event.idm.read_only_udm.network.dns.answers.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.type`: Newly mapped `record_type` and `cname_record_type` raw log field with `event.idm.read_only_udm.network.dns.answers.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.class`: Newly mapped `qclass` raw log field with `event.idm.read_only_udm.network.dns.answers.class` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.ttl`: Newly mapped `cname_ttl` raw log field with `event.idm.read_only_udm.network.dns.answers.ttl` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `raw_dns_flags` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-05-06 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields accurately.  
\- Added a grok pattern on the `desc` raw log field to extract the `key_office`, `view_office`, and `updating_zone` raw log fields.  
\- `event.idm.read_only_udm.metadata.description` : Newly mapped `RR_msg` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `client_id`, `key_office`, `rrset_type`, `syslog_priority`, `updating_zone`, and `view_office` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: If the `updating_zone` or `adding an RR` is present in the log, updated the value of `event.idm.read_only_udm.metadata.product_event_type` to `DNS_CHANGE`.   
2025-11-04 |  Enhancement:  
\- Added grok pattern to parse new format of syslog logs.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `session_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.ip` UDM field.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dst_ip` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM field.   
2025-09-11 |  Enhancement:  
\- Added GROK patterns to retrieve `src_ip1`, `dst_ip`, `host`, `intermediary_details`, and `src_mac`.  
\- Modified GROK pattern to retrieve `process_id`.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `src_mac` raw log field with event.idm.read_only_udm.principal.mac UDM field.  
\- event.idm.read_only_udm.principal.hostname: Removed existing `host` mapping for dhcpd log and mapped it to event.idm.read_only_udm.intermediary.hostname. (Incorrect existing mapping)  
\- event.idm.read_only_udm.principal.hostname: Retrived new `host` from dhcpd log and mapped event.idm.read_only_udm.principal.hostname.  
\- event.idm.read_only_udm.principal.asset.hostname: Removed existing `host` mapping for dhcpd log. (Incorrect mapping)  
\- event.idm.read_only_udm.principal.asset.hostname: Retrived `host` from dhcpd log and mapped event.idm.read_only_udm.principal.asset.hostname.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `src_ip1` raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip1` raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- Removed redundant code for `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.principal.asset_id: Removed asset_id from event.idm.read_only_udm.principal.asset_id. (incorrect mapping for dhcpd logs)  
\- Renamed asset_id to host in grok pattern for dhcpd logs.   
2025-07-03 |  Enhancement:  
\- Added grok pattern to parse new format of logs.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process_id` with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- Mapped `has_principal` to `true` when `event.idm.read_only_udm.principal.mac` is present.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `src_ip` with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- Added a conditional check to see if log has `dhcp` in it before setting event_type to `NETWORK_DHCP`.  
\- Added an IP validation before mapping intermediary, If the value is IP `intermediary` is mapped to `event.idm.read_only_udm.intermediary.ip` else mapped to `event.idm.read_only_udm.intermediary.hostname`.   
2025-06-26 |  Enhancement:  
\- Added Grok pattern to extract `domain_name` from `description`.  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname : Newly mapped `domain_name` with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, if `principal.hostname` and `principal.asset.hostname` is not mapped else it is mapped to `event.idm.read_only_udm.additional.fields`.  
\- Removed duplicate `dns_domain` in same grok pattern overwrite. This has been removed because it is redundant.   
2025-05-13 |  Enhancement:  
\- Added Grok patterns to parse new format of logs.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` UDM field as `NETWORK_DNS` when `has_dns_questions` is `true`, else `STATUS_UPDATE` when `has_principal` is `true` and `GENERIC_EVENT` for any other case.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` UDM field as `USER_UNCATEGORIZED` when `has_user` is `true`, else `STATUS_UPDATE` when `has_principal` is `true` and `GENERIC_EVENT` for any other case.   
2024-11-07 |  Enhancement:  
\- Mapped `hostname` to `principal.hostname` and `principal.asset.hostname`.  
\- When `data.code` is `1`, then set `additional.fields.key` to `subnet_mask`.  
\- When `data.code` is `2`, then set `additional.fields.key` to `time_offset`.  
\- When `data.code` is `4`, then set `additional.fields.key` to `time_server`.  
\- When `data.code` is `3`, then set `additional.fields.key` to `default_router`.  
\- When `data.code` is `6`, then set `additional.fields.key` to `dns`.  
\- When `data.code` is `12`, then set `additional.fields.key` to `hostname`.  
\- When `data.code` is `15`, then set `additional.fields.key` to `domain`.  
\- When `data.code` is `42`, then set `additional.fields.key` to `ntp`.  
\- When `data.code` is `51`, then set `additional.fields.key` to `lease_time`.  
\- When `data.code` is `58` or `59`, then set `additional.fields.key` to `renewal_time`.  
\- When `data.code` is `60`, then set `additional.fields.key` to `class_identifier`.  
\- When `data.code` is `61`, then set `additional.fields.key` to `client_identifier`.  
\- When `data.code` is `69`, then set `additional.fields.key` to `smtp`.  
\- When `data.code` is `70`, then set `additional.fields.key` to `pop3`.  
\- When `data.code` is `81`, then set `additional.fields.key` to `fqdn`.  
\- When `data.code` is `100`, then set `additional.fields.key` to `posix`.  
\- When `data.code` is `101`, then set `additional.fields.key` to `time_zone`.  
\- When `data.code` is `119`, then set `additional.fields.key` to `dns_searchlist`.  
\- When `data.code` is `121`, then set `additional.fields.key` to `static_route`.   
2024-08-21 |  Enhancement:  
\- When `activity-type` is dns related, then mapped `metadata.event_type` to `NETWORK_DNS`.   
2024-06-11 |  Enhancement:  
\- Handled unparsed JSON logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
