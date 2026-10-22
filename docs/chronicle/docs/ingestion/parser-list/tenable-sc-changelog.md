---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-sc-changelog/
title: Change log for TENABLE_SC \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:36.942261+00:00
---

# Change log for TENABLE_SC  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/tenable-sc-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for TENABLE_SC

Date | Changes  
---|---  
2026-09-16 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `stigSeverity`, `temporalScore`, `cvssV3BaseScore`, `cvssV3TemporalScore`, `cvssV3Vector`, `sc_uniqueness`, `exploitEase`, and `plugin_id` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `cvssV4BaseScore`, `cvssV4Vector`, `cvssV4ThreatScore`, `cvssV4ThreatVector`, `cvssV4Supplemental`, `exploitFrameworks`, `bid`, `recastRiskRuleComment`, `acceptRiskRuleComment`, and `attachment` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-08-27 |  Enhancement:  
\- Added support for `JSON` format.  
\- Added a Grok pattern to parse the raw log fields.  
\- `event.idm.read_only_udm.metadata.event_type`: If `log_msg` is `Successful logout`, updated the value of `event.idm.read_only_udm.metadata.event_type` to USER_LOGOUT, else if `has_principal` is true or `has_principal_ip` is true, updated the value of `event.idm.read_only_udm.metadata.event_type` to STATUS_UPDATE.  
\- `event.idm.read_only_udm.security_result.action`: If `log_msg` is `Successful logout`, updated the value of `event.idm.read_only_udm.security_result.action` to ALLOW.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `msg_netbiosName`, `alert_id`, `function_name`, `line_number`, `custom_severity`, `severity_id`, and `device capability` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `msg_seeAlso` and `msg_state` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `severity_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `vendor_severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.metadata.url_back_to_product`: Newly mapped `msg_SC_address` raw log field with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `alert_name` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path`: Newly mapped `target_path` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.file.full_path`: Newly mapped `source_file` raw log field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `scanner_id` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Updated the `date` filter's match patterns to parse the raw log fields.   
2026-08-10 |  Enhancement:  
\- Added grok patterns to support new format of syslog logs.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `sc_host`, `msg.dnsName` raw log fields with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `security_severity` and `msg.severity.name` raw log fields to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.first_discovered_time: Newly mapped `msg.firstSeen` raw log field with `event.idm.read_only_udm.security_result.first_discovered_time` UDM field.  
\- event.idm.read_only_udm.security_result.last_discovered_time: Newly mapped `msg.lastSeen` raw log field with `event.idm.read_only_udm.security_result.last_discovered_time` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `msg.ip`, `msg.ips` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.principal.mac, event.idm.read_only_udm.principal.asset.mac: Newly mapped `msg.macAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- event.idm.read_only_udm.principal.port: Newly mapped `msg.port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `msg.protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `msg.uuid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `msg.severity.description` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `msg.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `msg.hostUUID` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `msg.synopsis` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.principal.asset.platform_software.platform_version: Newly mapped `msg.operatingSystem` raw log field with `event.idm.read_only_udm.principal.asset.platform_software.platform_version` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly mapped `app_protocol` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.target.user.userid, event.idm.read_only_udm.principal.user.userid: Newly mapped `username` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field when it's a login event or logout event else mapped with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `request_id` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.action: Newly mapped `security_action` field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_type_field` field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg.description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: When it's a login event and user data is present, updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGIN`.  
\- event.idm.read_only_udm.metadata.event_type: When it's a logout event and user data is present, updated `event.idm.read_only_udm.metadata.event_type` to `USER_LOGOUT`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `vprContext.id`, `vprContext.name`, `vprContext.type`, `vprContext.value` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_category`, `status_code`, `msg.epssScore`,`msg.exploitAvailable`,`msg.hasBeenMitigated`,`msg.paranoidScanEnabled`,`msg.patchPubDate`,`msg.pluginID`,`msg.pluginInfo`,`msg.pluginModDate`,`msg.pluginName`,`msg.pluginPubDate`,`msg.pluginText`,`msg.recastRisk`,`msg.repository.dataFormat`,`msg.repository.id`,`msg.repository.name`,`msg.solution`,`msg.thoroughScanEnabled`,`msg.uniqueness`,`msg.vprScore`,`msg.vulnPubDate`,`msg.vulnUniqueness`,`msg.xref`,`msg.vulnUUID`,`msg.acceptRisk`,`msg.acrScore`,`msg.assetExposureScore`,`msg.cvssVector`,`msg.cve`,`msg.baseScore`,`msg.cgiScanEnabled`,`internet exposure`,`device type`,`msg.riskFactor`,`msg.checkType`,`msg.family.id`,`msg.family.name`,`msg.family.type`,`msg.hostUniqueness`,`msg.seolDate`,`_meta`,`window_start`,`window_end`,`is_first_run`,`run_ts`,`total_records`,`active_records`,`fixed_records`,`duration_seconds` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-08-11 |  Enhancement:  
\- Added GROK pattern for `msg` field.  
\- Modified the grok pattern from `DATA` to `IP` to specifically capture IP addresses in the `target_ips` field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `facility`, `Tenable_Message_Type`, `Alert_ID_Tenable`, `AD_Object`, `Tenable_deviance_ID`, `Tenable_Profile_ID`, `Tenable_Event_ID`, `LimitMemberCount`, and `GroupMemberCount` raw log fields to event.idm.read_only_udm.security_result.detection_fields.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `Forest_Name` raw log field to event.idm.read_only_udm.target.resource.name.  
\- event.idm.read_only_udm.target.administrative_domain: Newly mapped `Domain_Name` raw log field to event.idm.read_only_udm.target.administrative_domain.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `Tenable_Codename` raw log field to event.idm.read_only_udm.security_result.rule_name.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `Severity_Level` raw log field to event.idm.read_only_udm.security_result.severity.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `AD_Reason_Codename` raw log field to event.idm.read_only_udm.security_result.description.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `GroupCn` raw log field to event.idm.read_only_udm.target.group.group_display_name.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `PrivilegesPath` raw log field to event.idm.read_only_udm.target.resource.attribute.labels.  
\- event.idm.read_only_udm.target.resource.parent: Newly mapped `ParentContainer` raw log field to event.idm.read_only_udm.target.resource.parent.   
2025-07-21 |  Enhancement:  
\- event.idm.read_only_udm.principal.application: Newly mapped `principal_application` raw log field to `event.idm.read_only_udm.principal.application UDM field`.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `security_severity_details` raw log field to `event.idm.read_only_udm.security_result.severity_details UDM field`.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `log_msg` raw log field to `event.idm.read_only_udm.metadata.description UDM field`.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `process_id` raw log field to `event.idm.read_only_udm.principal.process.pid UDM field`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `session_id` raw log field to `event.idm.read_only_udm.network.session_id UDM field`.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `target_user_id` raw log field to `event.idm.read_only_udm.target.user.userid UDM field`.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `security_description` raw log field to `event.idm.read_only_udm.security_result.description UDM field`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `error_code` raw log field to `event.idm.read_only_udm.security_result.detection_fields UDM field`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp UDM field`.  
\- event.idm.read_only_udm.metadata.collected_timestamp: Newly mapped `collected_time` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp UDM field`.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `product_event_type` raw log field to `event.idm.read_only_udm.metadata.product_event_type UDM field`.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `version` raw log field to `event.idm.read_only_udm.metadata.product_version UDM field`.  
\- event.idm.read_only_udm.about.url: Newly mapped `uri_query` raw log field to `event.idm.read_only_udm.about.url UDM field`.  
\- event.idm.read_only_udm.target.application: Newly mapped `target_application` raw log field to `event.idm.read_only_udm.target.application UDM field`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `product` and `log_type` raw log field to `event.idm.read_only_udm.additional.fields UDM field`.  
\- Refactored event type classification logic to enhance accuracy for NETWORK_CONNECTION, USER_LOGIN, and STATUS_UPDATE events.  
\- Updated severity mapping to classify `warning` as `MEDIUM`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `principal_hostname` raw log field to `event.idm.read_only_udm.principal.hostname UDM field`.  
\- event.idm.read_only_udm.target.ip: Newly mapped `target_ip` raw log field (extracted from log_msg) to `event.idm.read_only_udm.target.ip UDM field`.   
2025-07-17 |  Enhancement:  
\- Added support for JSON+SYSLOG format.  
\- Introduced new grok patterns to extract fields from the JSON msg attribute.  
\- event.idm.read_only_udm.principal.asset.network_domain: Newly mapped `domain` raw log field to `event.idm.read_only_udm.principal.asset.network_domain` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly mapped `admin_domain` raw log field to `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `principal_ip` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `principal_ips` raw log field to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ip` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `target_ips` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `principal_userid` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.hostname, event.idm.read_only_udm.principal.asset.hostname: Newly mapped `principal_hostname` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.hostname, event.idm.read_only_udm.target.asset.hostname: Newly mapped `target_hostname` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `hostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.intermediary.process.pid: Newly mapped `proc_id` raw log field to `event.idm.read_only_udm.intermediary.process.pid` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `appname` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `rule_type` raw log field to `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `security_action_details` raw log field to `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `security_severity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.security_result.threat_id: Newly mapped `threat_id` raw log field to `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `priority` raw log field to `event.idm.read_only_udm.security_result.priority_details` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `msg` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `total_plugins`, `added`, `updated` and `removed` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Added grok pattern to extract `target_user_id` raw log field and mapped it to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- Dynamically sets metadata.event_type to NETWORK_CONNECTION, USER_UNCATEGORIZED, or STATUS_UPDATE based on the presence of principal user/ip and target ip fields.   
2024-11-21 |  Enhancement:  
\- Added support for new format of syslog logs.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
