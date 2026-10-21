---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dns-changelog/
title: Change log for INFOBLOX_DNS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:45:01.513641+00:00
---

# Change log for INFOBLOX_DNS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-dns-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for INFOBLOX_DNS

Date | Changes  
---|---  
2026-05-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- Added a grok pattern on `temp_data` field to extract `inter_host`, `time1` and `app_name` fields.  
\- `event.idm.read_only_udm.network.dns.questions.class`: Newly mapped `InfobloxDNSQClass` raw log field with `event.idm.read_only_udm.network.dns.questions.class` UDM field.  
\- `event.idm.read_only_udm.network.dns.authoritative`: Newly mapped `InfobloxDNSQFlags` raw log field with `event.idm.read_only_udm.network.dns.authoritative` UDM field.  
\- `event.idm.read_only_udm.network.dns.response_code`: Newly mapped `InfobloxDNSRCode` raw log field with `event.idm.read_only_udm.network.dns.response_code` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_DNS` when necessary raw log fields are present.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `app_name`, `InfobloxDNSView`, `InfobloxAnCount`, `InfobloxNsCount`, `InfobloxDNSQFlags` and `InfobloxArCount` raw log fields with `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `time1` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2026-01-27 |  Enhancement:  
\- Added a grok pattern to support new format of logs.  
\- event.idm.read_only_udm.target.mac: Newly mapped from the `target_mac` raw log field to `event.idm.read_only_udm.target.mac` UDM field.  
\- event.idm.read_only_udm.network.dns.authority.name: Newly mapped `dns_authority_domain` raw log field to `event.idm.read_only_udm.network.dns.authority.name` UDM field.  
\- event.idm.read_only_udm.network.dns.authority.ttl: Newly mapped `authority_ttl_data` raw log field to `event.idm.read_only_udm.network.dns.authority.ttl` UDM field.  
\- event.idm.read_only_udm.network.dns.authority.class: Newly mapped `authority_dns_class` raw log field to `event.idm.read_only_udm.network.dns.authority.class` UDM field.  
\- event.idm.read_only_udm.network.dns.authority.type: Newly mapped `authority_dns_query_type` raw log field to `event.idm.read_only_udm.network.dns.authority.type` UDM field.  
\- event.idm.read_only_udm.network.dns.authority.data: Newly mapped `authority_data` raw log field to `event.idm.read_only_udm.network.dns.authority.data` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped from `site_id`, `id`, `flags`, `number_of_query`, `number_of_answer`, `number_of_authority`, `number_of_additional` raw log fields.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `inter_ip` raw log field to `event.idm.read_only_udm.intermediary.ip` UDM field.   
2025-10-17 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `actor_details` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `action` raw log field to `event.idm.read_only_udm.security_result.action_details`.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `object_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `object_name` raw log field to `event.idm.read_only_udm.target.user.userid` (when `object_type` is `AdminMember`).  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `object_name` raw log field to `event.idm.read_only_udm.target.resource.name` (when `object_type` is not `AdminMember`).  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `dns_view`, `rpz_type` and `DnsView` raw log field to `event.idm.read_only_udm.security_result.detection_fields`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped based on the `disabled` raw log field to `event.idm.read_only_udm.security_result.action`.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `fqdn` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `rpz_severity` raw log field to event.idm.read_only_udm.security_result.severity_details.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `rpz_policy` raw log field to `event.idm.read_only_udm.security_result.rule_name`.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `name` raw log field to `event.idm.read_only_udm.target.user.user_display_name` (when `object_type` is `AdminMember` and `action` is `Created`).  
\- `event.idm.read_only_udm.target.user.group_identifiers`: Newly mapped `group_id` raw log field to `event.idm.read_only_udm.target.user.group_identifiers`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `allow_recursion`, `ddns_principal_group`, `mgm_private`, `network_view`, `view`, `zone_format`, `create_ptr_for_bulk_hosts`, `create_ptr_for_hosts`, `is_multimaster`, `locked`, `ms_ad_integrated`, `auth_type`, `use_ssh_keys`, and `exclude_subobj` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.target.resource.name`: Mapped `name` raw log field to `event.idm.read_only_udm.target.resource.name` when `object_type` is `DnsView` and `action` is `Created`.   
2025-08-26 |  Enhancement:  
\- Added Grok patterns to support new formats of logs.  
\- Updated Grok patterns to extract `process` and `pid` from syslog header.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `process` log field to `event.idm.read_only_udm.intermediary.application`.  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped `pid` log field to `event.idm.read_only_udm.intermediary.process.pid`.  
\- event.idm.read_only_udm.network.dns.authority.name: Newly mapped `nameserver` log field to `event.idm.read_only_udm.network.dns.authority.name`.   
2024-09-24 |  Enhancement:  
\- Changed mapping of syslog header `hostname` from `target.hostname` to `intermediary.hostname`.  
\- Removed trailing period character from `dns.answers.data`.   
2024-08-19 |  Enhancement:  
\- Added conditional check for `intermediary_ip`.  
\- Renamed `dns_domain` to `dns_answer_domain`.  
\- Added for loop to retrieve `dns_query_type`, `ttl_data`, `dns_domain`, `dns_class`, `intermediary_ip`, and `intermediary_host`.  
\- Mapped `dns_domain` to `dns.answers.name`.  
\- Mapped `ttl_data` to `dns.answers.ttl`.  
\- Mapped `dns_query_type` to `dns.answer.type`  
\- Mapped `dns_class` to `dns.answer.class`".  
\- Mapped `intermediary_ip` or `intermediary_host` to `dns.answer.data`.   
2023-10-17 |  Enhancement:  
\- Added a Grok pattern to handle unparsed logs.   
2023-06-19 |  Enhancement:  
Wrote a Grok pattern to extract `hostname`,`ip` and `port` and changed `event_type`accordingly.   
2023-01-19 |  Enhancement:  
\- Added Grok pattern to support new Syslog.  
\- Added mapping for following:  
\- If log contains any ip protocol, such as TCP or UDP, value is mapped to `network.ip_protocol`..  
\- If log contains any intermediary IP address or hostname, value is mapped to `intermediary.ip/intermediary.hostname`.   
2022-09-09 |  Enhancement:  
\- Modified and properly mapped the field `syslog_timestamp` to `metadata.event_timestamp`.   
2022-08-25 |  Enhancement:  
\- Mapped the field `syslog_timestamp` to `metadata.event_timestamp`.  
\- Added grok and conditional checks for the field `smac` mapped to `principal.mac`.  
\- Added conditional checks for the field `dns_domain` mapped to `network.dns.questions`.  
\- Added conditional checks for the field `name1` mapped to `network.dns.answers.name`.  
\- Added conditional checks for the field `ttl1` mapped to `network.dns.answers.ttl`.   
2022-07-15 |  Bugfix - Removed last character if it is dot from network.dns.questions.name, network.dns.answers.name, network.dns.answers.data   
2022-06-02 |  Bug-fix - IP was not extracted properly from syslog log so modified the grok to extract it properly.  
Enhancement - Provided support for CEF format logs.  
Mapped the following new fields:-  
InfobloxB1OPHIPAddress to principal.ip  
InfobloxDNSQType to dns.questions.type  
destinationDnsDomain to dns.questions.name  
InfobloxB1Region to principal.location.country_or_region   
2022-04-28 |  Removed extra word `query:` from `network.dns.questions.name` field.   
2022-02-09 |  Enhancement:  
Wrote a grok to extract `hostname` and changed `event_type`accordingly.  
\- Mapped `src_host` to `principal.hostname`.  
\- Mapped appropriate `event_type`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
