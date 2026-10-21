---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/attivo-changelog/
title: Change log for ATTIVO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:35:46.241677+00:00
---

# Change log for ATTIVO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/attivo-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ATTIVO

Date | Changes  
---|---  
2026-01-29 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `Alert.severity`, `severity` and `CEFSeverity` raw log field to event.idm.read_only_udm.security_result.severity_details.  
\- Modified the logic for mapping the `dhost` field. The parser now attempts to extract an IP address from `dhost`. If an IP is found, it is mapped to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`. If `dhost` is not an IP address, it is mapped to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`. This mapping is now applied in all cases, removing the previous condition based on the `service` field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dhost` raw log field to event.idm.read_only_udm.target.ip.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `dhost` raw log field to event.idm.read_only_udm.target.hostname.   
2025-12-22 |  Enhancement:  
\- Expanded the range of `CEFSeverity` values (including `Very-High`, `High`) that result in event.idm.read_only_udm.security_result.severity being set to `HIGH`.  
\- Refined the validation condition for mapping `usrname` to event.idm.read_only_udm.principal.user.email_addresses to check for valid email format and length.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `domain_name` raw log field to event.idm.read_only_udm.principal.administrative_domain.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `source_device_name`, `forwarder_ip`, `suser`, `subscriberId`, `referenceId`, `adEventIds` and `shostname` raw log field to event.idm.read_only_udm.additional.fields.   
2025-10-03 |  Enhancement:  
\- Add a grok pattern to parse new log formats.  
\- Added a gsub for `Attacker HostName` to `Attacker_HostName`, `Attacker MAC` to `Attacker_MAC`, `Attacker UserNames` to `Attacker_UserNames`, `Source Device Name` to `Source_Device_Name`, `Attivo AlertID` to `Attivo_AlertID`, `MITRE Technique ID` to `MITRE_Technique_ID`, `MITRE Technique Name` to `MITRE_Technique_Name`, `MITRE Tactic Name` to `MITRE_Tactic_Name`, `Target IP Domain` to `Target_IP_Domain`, `Target Ports` to `Target_Ports`, `Target IP Ports` to `Target_IP_Ports`, `TargetIP List` to `TargetIP_List`, `Forwarder IP` to `Forwarder_IP`, `Dest UserName` to `Dest_UserName`, `Attacker IP Domain` to `Attacker_IP_Domain`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `VLANID`, `Forwarder_IP`, `VTSummaryResult`, `WebRootReputation`, `Forwarder`, `Target_IP_Ports`, `TargetIP_List` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `Dest_UserName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.administrative_domain`: Newly mapped `Attacker_IP_Domain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `attacker_ip`, `detail_target_ip` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `target_host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `target_ip` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.platform_version`: Newly mapped `target_os` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `detail_source_ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `phase` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `Attacker_HostName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `Attacker_MAC` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Attacker_UserNames` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `Source_Device_Name` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `Attivo_AlertID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `MITRE_Technique_Name` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `MITRE_Tactic_Name` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `Target_Ports` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.administrative_domain`: Newly mapped `Target_IP_Domain` raw log field with `event.idm.read_only_udm.target.administrative_domain` UDM field.   
2025-08-06 |  Enhancement:  
\- Added a new gsub block to add support for logs split into multiple lines.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `forwarder` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2025-07-01 |  Enhancement:  
\- Added a Grok to parse SYSLOG + KV (CEF) format of logs with any timezone pattern.  
\- Added a Grok to extract `process` and `pid` from `msg` raw log field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `process` log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `pid` log field to `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `timezone` log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.port: Newly mapped `spt` raw log field to `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `rt` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- Modified condition for dropping invalid logs by adding a `valid_log` flag.  
\- Set `has_principal` to `true` if `principal.ip` or `principal.hostname` is present.  
\- Set `has_target` to `true` if `target.ip` or `target.hostname` is present.  
\- Merged both conditions to map `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- Modified conditions to map `event.idm.read_only_udm.metadata.event_type` to `NETWORK_UNCATEGORIZED` and `STATUS_UPDATE`.  
\- Added mappings for `target.asset.ip` wherever `target.ip` is mapped and `principal.asset.ip` wherever `principal.ip` is mapped.   
2025-01-10 |  Enhancement:  
\- Added a new Grok pattern to parse the unparsed logs.  
\- Added a JSON block to parse the unparsed logs.  
\- Mapped `Alert.subject` to `metadata.description`.  
\- Mapped `Alert.body` to `metadata.description`.  
\- Mapped `Alert.app` to `principal.application`.  
\- Mapped `Alert.dest_ip` to `target.ip` and `target.assest.ip`.  
\- Mapped `Alert.dest_host` to `target.hostname`.  
\- Mapped `Alert.src_hostname` to `principal.hostname`.  
\- Mapped `Alert.src_ip_domain` to `principal.domain.name`.  
\- Mapped `Alert.dest_ip_domain` to `target.domain.name`.  
\- Mapped `Alert.id` to `metadata.product_log_id`.  
\- Mapped `Alert.des_os` to `target.asset.platform_software.platform_version`.  
\- Mapped `Alert.src_ip` to `principal.ip` and `prinicipal.asset.ip`.  
\- Mapped `Alert.src_mac` to `prinicipal.mac`.  
\- Mapped `Alert.id` to `metadata.product_log_id`.  
\- Mapped `Alert.bootsink_ip` to `intermediary.ip`.  
\- Mapped `Alert.forwarder` and `Alert.service` to `additional.fields`.  
\- Mapped `techinque_id` to `security_result.attack_details.tactics.id`.  
\- Mapped `techinque_name` to `security_result.attack_details.tactics.name`.  
\- Mapped `Alert.severity` to `security_result.severity`.  
\- Mapped `Alert.src_category` to `security_result.threat_name`.   
2024-04-19 |  Enhancement:  
\- Added support for new event types `NETWORK_UNCATEGORIZED` and `SCAN_NETWORK`.  
\- Added support for certain new attributes.   
2023-08-14 |  Enhancement:  
\- Added conditional check for `ips`.  
\- If `ips` format matches IP address format, then map `ips` to `principal.ip`, else map it to `intermediary.hostname`.   
2023-07-21 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
