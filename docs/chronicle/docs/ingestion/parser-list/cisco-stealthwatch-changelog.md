---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stealthwatch-changelog/
title: Change log for CISCO_STEALTHWATCH \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:36:15.635508+00:00
---

# Change log for CISCO_STEALTHWATCH  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cisco-stealthwatch-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CISCO_STEALTHWATCH

Date | Changes  
---|---  
2026-01-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `eventData_id` raw log field to `event.idm.read_only_udm.metadata.product_event_type`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `host.ip`, `leef.src` raw log fields to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `host.ip`, `leef.src` raw log fields to `event.idm.read_only_udm.principal.asset.ip`.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version`.  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `process.pid` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `process.name` raw log field to `event.idm.read_only_udm.principal.process.file.full_path`.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `leef.fullmessage` raw log field to `event.idm.read_only_udm.metadata.description`.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `leef.flowCollectorName` raw log field to `event.idm.read_only_udm.observer.hostname`.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `leef.sourceHG` raw log field to `event.idm.read_only_udm.principal.location.country_or_region`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `leef.dst` raw log field to `event.idm.read_only_udm.target.ip`.  
\- `event.idm.read_only_udm.target.asset.ip`: Newly mapped `leef.dst` raw log field to `event.idm.read_only_udm.target.asset.ip`.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `leef.alarmSev` raw log field to `event.idm.read_only_udm.security_result.severity_details`.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `leef.targetHostSnapshot` raw log field to `event.idm.read_only_udm.target.url`.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `leef.start` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `leef.cat` raw log field to `event.idm.read_only_udm.security_result.category_details`.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `leef.flowCollectorIP` raw log field to `event.idm.read_only_udm.observer.ip`.  
\- `event.idm.read_only_udm.observer.asset.ip`: Newly mapped `leef.flowCollectorIP` raw log field to `event.idm.read_only_udm.observer.asset.ip`.  
\- `event.idm.read_only_udm.principal.url`: Newly mapped `leef.sourceHostSnapshot` raw log field to `event.idm.read_only_udm.principal.url`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `leef.msg` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `leef.domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `log.syslog.severity.name` raw log field to `event.idm.read_only_udm.security_result.severity`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `leef.alarmID`, `leef.alarmStatus`, `leef_version`, `service.type`, `log.syslog.severity.code`, `Log_Type`, `delimiter`, `syslog_pri`, `log.syslog.facility.code`, `log.syslog.facility.name`, `event.original` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Added conditional mapping for `security_result.severity` based on `log.syslog.severity.name`.   
2025-09-12 |  Enhancement:  
\- Modified grok patterns to handle JSON format.  
\- Added mutate filters to remove `\r\n` and `\n` characters from the message.  
\- Added mutate filter to rename the root `event` field to `eventData` in JSON logs.  
\- Added mutate filter to unnest the `eventData` object.  
\- Updated the date filter to support `ISO8601` format for the `time` field.  
\- Added conditional logic to map `source_name` to IP fields if it's an IP address, otherwise map it to hostname fields.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_name` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_name` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `source_name` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `source_name` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.security_result.url_back_to_product: Newly mapped `url` raw log field to `event.idm.read_only_udm.security_result.url_back_to_product`.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `observations` raw log field to `event.idm.read_only_udm.security_result.rule_id`.   
2025-07-29 |  Enhancement:  
\- Added grok patterns to parse unparsed logs.  
\- event.idm.read_only_udm.target.hostname: Newly mapped target_hostname raw log field to event.idm.read_only_udm.target.hostname.  
\- event.idm.read_only_udm.target.mac: Newly mapped target_mac_address raw log field to event.idm.read_only_udm.target.mac.  
\- event.idm.read_only_udm.principal.mac: Newly mapped source_mac_address raw log field to event.idm.read_only_udm.principal.mac.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped alarm_severity_id raw log field to event.idm.read_only_udm.security_result.severity.  
\- event.idm.read_only_udm.principal.user.user_display_name: Newly mapped source_username raw log field to event.idm.read_only_udm.principal.user.user_display_name.  
\- Consolidated all mapping for event.idm.read_only_udm.additional.fields.   
2024-10-29 |  Enhancement:  
\- Added support to handle JSON logs.   
2024-09-26 |  Enhancement:  
\- Added support to parse CEF format logs.   
2024-06-11 |  Enhancement:  
\- Updated the Grok pattern to parse the `emc1502` value and mapped it to `principal.hostname`.   
2023-06-19 |  Enhancement:  
\- Mapped `sourceIPv4Address` to `principal.ip`.  
\- Mapped `SourceModuleType` to `observer.application`.  
\- Mapped `SourceModuleName` to `target.resource.name`.  
\- Mapped `MessageSourceAddress` to `principal.ip`.  
\- Mapped `SourcePort` to `principal.port`.  
\- Mapped `Version` to `metadata.product_version`.  
\- Mapped `DestPort` to `target.port`.  
\- Mapped `DestIPv4Address` to `target.ip`.  
\- Mapped `ProtocolIdentifier` to `network.ip_protocol`.  
\- Mapped `inputSNMPIface`, `outputSNMPIface`, `InPackets` to `additional.fields`.   
2023-02-10 |  FIX -  
\- Added new Grok patterns to parse NFS and SMB protocol type logs.   
2022-07-06 |  Enhancement-Added mappings for unparsed log (audit, alarm).  
FC_Name mapped to principal.user.userid.  
src mapped to principal.ip.  
dst mapped to target.ip.  
Source_HG mapped to principal.location.country_or_region.  
category mapped to security_result.category_details.  
details mapped to metadata.description.  
vendor_severity Minor mapped to security_result.severity (INFORMATIONAL).  
vendor_severity Major mapped to security_result.severity (ERROR).  
Added Event_type USER_UNCATEGORIZED for unparsed log.  
Added additional field Alarm_ID.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
