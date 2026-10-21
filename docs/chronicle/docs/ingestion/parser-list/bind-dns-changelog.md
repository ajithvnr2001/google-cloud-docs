---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bind-dns-changelog/
title: Change log for BIND_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T13:20:49.481257+00:00
---

# Change log for BIND_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/bind-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for BIND_DNS

Date | Changes  
---|---  
2026-01-11 |  Enhancement:  
\- Added support for a new pattern of logs.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `cisco_tag` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `generic_message` raw log field to `event.idm.read_only_udm.metadata.description` when `cisco_tag` is present.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `protocol` raw log field to `event.idm.read_only_udm.network.ip_protocol`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- event.idm.read_only_udm.target.port: Newly mapped `target_port` raw log field to `event.idm.read_only_udm.target.port`.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `permit` raw log field to `event.idm.read_only_udm.security_result.action` (set to `BLOCK` if permit is `Deny`).  
\- Added date format `MMM dd yyyy HH:mm:ss` to the `date` filter.  
\- Added specific handling to convert `query_type` `TYPE65535` to its integer value `65535`.   
2025-11-28 |  Enhancement:  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.hostname`.  
\- `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `inter_host` raw log field to `event.idm.read_only_udm.intermediary.asset.hostname`.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `tar_app` raw log field to `event.idm.read_only_udm.target.application`.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `src_user` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `src_pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `usr_login`, `USER` raw log fields to `event.idm.read_only_udm.target.user.userid`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `usr_type`, `client_internal_ref`, `key_name`, `transfer_type`, `transfer_messages`, `records_transferred`, `bytes_transferred`, `duration_seconds`, `transfer_rate_bytes_per_sec`, `zone_serial`, `question_name`, `dns_view`, `requested_transfer_type`, `ixfr_delta_size_bytes`, `max_ratio_database_size_bytes`, `actual_transfer_type`, `dnszone_name`, `param_key`, `param_value`, `dns_name`, `dnszone_type`, `dnszone_is_rpz`, `dnszone_response_policy`, `dnszone_rpz_log`, `dnszone_order`, `ddns_scavenging`, `dnsview_name`, `rr_ttl`, `value1`, `value2`, `value3`, `value4`, `value5`, `value6`, `value7`, `rr_type`, `old_value2`, `old_value3`, `old_value4`, `PWD`, `dnsview_order`, `dnsview_match_to`, `dnsview_recursion`, `dns_class`, `current_serial`, `zone_serial_at_start`, `dns_transfer_details` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `rr_full_name_utf`, `tar_res` raw log fields to `event.idm.read_only_udm.target.resource.name`.  
\- `event.idm.read_only_udm.target.process.command_line`: Newly mapped `COMMAND` raw log field to `event.idm.read_only_udm.target.process.command_line`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped message content raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- Added support for multiple new SYSLOG formats.  
\- Added KV data processing for fields `kv_data` and `kv_data1`.  
\- Conditional logic added to set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`, `STATUS_UPDATE`, or `GENERIC_EVENT` based on parsed fields.  
\- Added mappings for `event.idm.read_only_udm.metadata.product_event_type` based on log message content, including types like `Created AdminMember`, `Deleted AdminMember`, `Created ForwardZone`, `Deleted ForwardZone`, `Created AuthZone`, `Deleted AuthZone`, `Created DnsView`, `Deleted DnsView`, `Created ResponsePolicyZone`, and `Deleted ResponsePolicyZone`.   
2025-06-19 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `dns_flags` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added a new grok patterns to parse an additional log formats and also parse logs that were `GENERIC_EVENT`.  
\- Implemented conditional flag checks to determine `event_type` mapping for `NETWORK_CONNECTION` and `STATUS_UPDATE`.  
\- Added checks to ensure `principal_machine_present` and `target_present` are only mapped to true if they are present and true in the source.  
\- Added a condition to check for the existence of the `device` field before mapping it to `_principal.hostname` and `_principal.asset.hostname`.  
\- Added a check to ensure the `_principal` local variable is not empty before renaming it to `event.idm.read_only_udm.principal`.  
\- Updated `dhcp_qtype_mapping.include`: Added condition to map qtype_value to `256` if the value is `TYPE256`.   
2025-05-30 |  Enhancement:  
\- Modified the grok pattern to fetch query_value and mapped it to `event.idm.read_only_udm.network.dns.questions.name` UDM field.   
2025-04-30 |  \- Added new Grok patterns to parse the unparsed logs.  
\- `event.idm.read_only_udm.metadata.event.timestamp` \- Newly mapped event_date` raw log field with `event.idm.read_only_udm.metadata.event_timestamp' UDM field.  
\- `event.idm.read_only_udm.additional.fields` \- Newly mapped `edns_udp_size` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-11-25 |  Bug-fix:  
\- Changed mapping of `client_string` from `principal.mac` to `security_result.detection_fields`.  
\- Changed mapping of `tar_host` from `target.hostname` to `observer.hostname`.  
\- Changed mapping of `response_ip` from `target.ip` to `observer.ip`.  
\- Mapped `query` to `target.hostname`.   
2024-10-30 |  Enhancement:  
\- Mapped `mac_address` to `principal.mac` and `dns_record_type` to `security_result.detection_fields`.   
2024-07-08 |  Enhancement:  
\- Added new Grok patterns to parse unparsed fields in the log.  
\- Mapped `view` to `additional.fields`.  
\- Mapped `domain_name` to `network.dns.questions.type`.  
\- Mapped `src_host` to `principal.hostname`.   
2024-02-24 |  Enhancement:  
\- Added new Grok patterns to parse unparse fields in the log.  
\- If `principal.hostname` is present, then mapped `metadata.event_type` to `STATUS_UPDATE`.  
\- If `generic_message` is similar to `checkhints`, then added a Grok pattern to extract `tar_host` and `response_ip`.  
\- If `generic_message` is similar to `update` or `zone transfer`, then added a Grok pattern to extract `tar_host` and `action`.  
\- If `generic_message` is similar to `REFUSED unexpected RCODE`, then added a Grok pattern to extract `tar_host`, `src_ip`, and `src_port`.  
\- If `generic_message` is similar to `check_mk`, then added a Grok pattern to extract `src_app`, `src_ip`, `src_port`, `response_ip` and `response_port`.   
2024-01-30 |  Enhancement  
\- Added a new Grok pattern to extract `query`.   
2023-12-20 |  Enhancement  
\- Added new Grok patterns to parse new format logs.  
\- Mapped `pid` to `principal.process.pid`.  
\- Mapped `response_ip_2` to `target.ip`.  
\- If action value is similar to `denied` or `deny`, mapped `security_result.action` to `BLOCK`.  
\- If action value is similar to `allowed` or `allow`, mapped `security_result.action` to `ALLOW`.   
2023-09-19 |  Enhancement  
\- Added new Grok patterns to parse dropped logs.   
2023-07-10 |  Enhancement  
\- Added a new Grok pattern to handle syslog format logs.   
2022-11-16 |  Enhancement  
\- Added a new Grok pattern for failing query-error logs.  
\- Updated Grok patterns to parse logs which have additional data after port number.  
\- Concatenated `query_int_1` and `query_int_2` to `query`.  
\- Mapped `dns_resp_2` and `error_loc` to `description`.  
\- Added conditions in `dhcp_qtype_mapping.include` to check for Types TYPE0, TYPE65521, TYPE65400 and converted them to integer values.   
2022-04-22 |  Enhancement - Parsed logs that failed earlier   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
