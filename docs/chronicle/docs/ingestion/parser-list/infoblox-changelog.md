---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-changelog/
title: Change log for INFOBLOX \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:00:17.865608+00:00
---

# Change log for INFOBLOX  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/infoblox-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for INFOBLOX

Date | Changes  
---|---  
2026-08-14 |  Enhancement:  
\- Added a Grok pattern to parse the new format of raw log fields  
\- `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip`: Removed the mapping of `clientIp` from `event.idm.read_only_udm.observer.ip` and `event.idm.read_only_udm.observer.asset.ip` UDM fields for SYSLOG logs since it represents the principal related field not the observer.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `clientIp`, `src_ip` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `src_ip` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `srcPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `dst_port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.name`: Newly mapped `dnsDomain` raw log field with `event.idm.read_only_udm.network.dns.questions.name` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.type`: Newly mapped `queryType` raw log field with `event.idm.read_only_udm.network.dns.questions.type` UDM field.  
\- `event.idm.read_only_udm.network.dns.questions.class`: Newly mapped `dnsClass` raw log field with `event.idm.read_only_udm.network.dns.questions.class` UDM field.  
\- `event.idm.read_only_udm.network.dns.answers.ttl`: Newly mapped `ttl` raw log field with `event.idm.read_only_udm.network.dns.answers.ttl` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `operation` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `dns_error` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `action`, `failure_reason` raw log fields with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dns_record_name`, `soa_rname`, `soa_serial`, `soa_refresh`, `soa_retry`, `soa_expire`, `responseCode` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-17 |  Enhancement:  
\- Modified the grok patterns to parse new format of SYSLOG raw log fields.  
\- `event.idm.read_only_udm.network.dhcp.type`: Newly mapped `dhcp_discover` log field with `event.idm.read_only_udm.network.dhcp.type` UDM field.  
\- `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `clientMac` log field with `event.idm.read_only_udm.principal.asset.mac` UDM field  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `hostname`, `clientHostname` log fields with `event.idm.read_only_udm.principal.asset.hostname` UDM field  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `pid` log field with `event.idm.read_only_udm.principal.process.pid` UDM field  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `TransID` log field with `event.idm.read_only_udm.network.session_id` UDM field  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dhcp_request_status`, `flag`, `uid`, `dhcp_lease_status`, `offered_duration`, `interface` log fields with `event.idm.read_only_udm.additional.fields` UDM field  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `dhcp_discover` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field   
2026-04-16 |  Enhancement:  
\- Added support for additional SYSLOG formats.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `clientMac` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.principal.asset.mac: Newly mapped `clientMac` raw log field with `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `intermediary_IP` raw log field with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `observer_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- event.idm.read_only_udm.observer.process.pid: Newly mapped `observer_pid` raw log field with `event.idm.read_only_udm.observer.process.pid` UDM field.  
\- event.idm.read_only_udm.observer.process.file.full_path: Newly mapped `file` raw log field with `event.idm.read_only_udm.observer.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.ip: Newly mapped target_ip, `dnsServer_Ip` raw log fields with `event.idm.read_only_udm.target.ip` UDM field.  
\- event.idm.read_only_udm.target.asset.ip: Newly mapped target_ip, `dnsServer_Ip` raw log fields with `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `TransID`, `size`, `syslog_priority`, `flag` raw log fields with event.idm.read_only_udm.additional.fields UDM field.  
\- event.idm.read_only_udm.network.application_protocol: If `dhcp_discover` is DHCPDISCOVER, updated the value of `event.idm.read_only_udm.network.application_protocol` to DHCP.  
\- event.idm.read_only_udm.network.dhcp.type: If `dhcp_discover` is DHCPDISCOVER, updated the value of `event.idm.read_only_udm.network.dhcp.type` to DISCOVER.   
2025-08-28 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `event_status` field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `leaseTime` field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `process` field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added grok pattern to validate and extract MAC address into `clientMac1` field.  
\- Added conditional check for `leaseTime` field to avoid mapping of negative values to `event.idm.read_only_udm.network.dhcp.lease_time_seconds` UDM field.   
2025-05-30 |  Enhancement:  
\- Added Grok patterns to support new format of syslog logs.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `dnsServerIp`, `remote_id`, `circuit_id` and `client_socket_address` fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added additional date filter to support new format of timestamps.   
2025-03-20 |  Enhancement:  
\- Added grok patterns to support new format of syslog logs.  
\- Mapped `dstMac` to `target.mac`.  
\- Mapped `clientIp2` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `priority` to `sec_result.severity`.  
\- Mapped `tar_host` to `target.hostname` and `target.asset.hostname`.  
\- Added KV filter to support new format of syslog logs.   
2025-02-27 |  Enhancement:  
\- Removed output merge in `infoblox_nios.include` to avoid duplicate events.   
2025-01-16 |  Enhancement:  
\- Mapped `host` to `principal.ip`  
\- Mapped `geo_src.ip` to `principal.ip`  
\- Mapped `geo_src.country` to `principal.location.country_or_region`  
\- Mapped `geo_src.timezone` to `principal.location.city`  
\- Mapped `geo_src.lat` to `principal.location.region_latitude`  
\- Mapped `geo_src.lon` to `principal.location.region_longitude`  
\- Mapped `geo_src.continent_code` to `principal.resource.attribute.labels`  
\- Mapped `geo_src.country_code2` to `principal.resource.attribute.labels`  
\- Mapped `geo_src.country_code3` to `principal.resource.attribute.labels`  
\- Mapped `geo_src.country_name` to `principal.location.country_or_region`  
\- Added a Grok pattern to parse unparsed logs  
\- Mapped `hostname` to `principal.hostname`  
\- Mapped `ip` to `principal.ip`  
\- Mapped `query` to `additional.fields`  
\- Mapped `protocol` to `network.ip_protocol`  
\- Mapped `src_port` to `principal.port`  
2024-11-27 |  Enhancement:  
\- Mapped `dhcpServerIp` to `network.dhcp.giaddr`  
\- Mapped `description` to `metadata.description`  
\- Mapped `transId` to `network.session_id`  
2024-09-17 |  Enhancement:  
\- Added a Grok pattern to support unparsed logs.   
2024-05-03 |  Enhancement:  
\- Parsed unparsed NIOS logs by adding a new Grok pattern and KV filter.   
2024-04-29 |  Enhancement:  
\- Added a Grok pattern to parse syslog logs.   
2024-02-23 |  Enhancement:  
\- Mapped `queries` section in log to `network.dns.questions`.   
2023-11-07 |  Enhancement  
\- Parsed DNS response logs by adding new Grok patterns.   
2023-10-30 |  Enhancement  
\- Parsed unparsed DNS logs using a Grok pattern.   
2023-03-09 |  \- Mapped `question.type` based on the `record_type` in the log.   
2023-01-16 |  Bug-fix  
\- Added grok pattern for login and logout related logs.  
\- Mapped `USER_LOGIN` to `metadata.event_type` when `desc` is `login_allowed`,`login_denied`.  
\- Mapped `USER_LOGOUT` to `metadata.event_type` when `desc` is `logout`.  
\- Mapped `group` to `target.user.group_identifiers`.  
\- Mapped `to` to `role.name`.  
\- Mapped `trigger_event` to `seecurity_result.summary`.  
\- Mapped `SSO` to `extensions.auth.type` based on `auth`.  
\- Mapped `auth` to `extensions.auth.auth_details`.  
\- Mapped `SERVICE`,`REMOTE` to `extensions.auth.mechanism` based on `apparently_via`.  
\- Mapped `sys_host` to `principal.hostname` when `principal_ip` and `intermediary_ip` is null.  
\- Mapped `dns_question` to `network.dns.questions`.  
\- Mapped `answers1` to `network.dns.answers`.  
\- Mapped `USER_RESOURCE_ACCESS` to `metadata.event_type` when `principal_ip`,`clientMac` and `intermediary_ip` are null and `event_type` is `STATUS_UPDATE`.  
\- Mapped `principal_ip` to `principal.ip`.  
\- Mapped `principal_port` to `principal.port`.   
2022-12-12 |  \- Added a grok pattern for `eventType` = `success`.   
2022-08-05 |  \- Modified `event_type` from `GENERIC_EVENT` to `STATUS_UPDATE` to reduce generic percentage.  
\- Mapped `event.idm.read_only_udm.principal.ip` as `event.idm.read_only_udm.intermediary.ip` where `event.idm.read_only_udm.principal.ip` is null in order to facilitate mapping of `event_type` to `STATUS_UPDATE`.   
2022-07-10 |  Enhancement - Modified grok pattern to parse the logs.  
Handled the dropped logs and mapped them to valid event_types.  
\- Dropped logs had following eventType, which are now handled:  
`forward map`, `Reverse`, `Forward`, `Removed`, `Processed`, `Dynamic`, `Lease`, `Unable`, `reverse map`, `bind`, `map update`, `parse_option_buffer`, `Added`,`DDNS`, `ICMP`,`update-security` ,`update`,`notify`,`general`,`LPF`, `Sending`.  
\- Also, following `process` were dropped earlier are now handled:  
`netauto_discovery`, `ntpd`.  
\- Other condition checks like `msg1` containing `DNS update latency|pool|syslog|declaration|write|Consortium|reserved|duplicate|leases|visit|disconnected` are handled.  
\- Added new code block to handle `forward map`, `Forward map`, `Reverse map` and `reverse map` and made them parse.  
\- Added new code block to handle `bind`, `netauto_discovery` and made them parse.  
\- Changed event type from `GENERIC_EVENT` to `STATUS_UPDATE` wherever possible.   
2022-05-08 |  Bug - Changing the parser logic to map hostname.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
