---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zimperium-changelog/
title: Change log for ZIMPERIUM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:48.066236+00:00
---

# Change log for ZIMPERIUM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/zimperium-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ZIMPERIUM

Date | Changes  
---|---  
2026-06-18 |  Enhancement:  
\- Added a grok pattern to parse the new format of SYSLOG + JSON logs.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `forensics.network_threat.my_ip` and `threat.general.gateway_ip`, `threat.general.external_ip` raw log fields to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `device_info.device_id` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels`: Newly mapped `device_manufacturer` raw log field to `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.asset.last_discover_time`: Newly mapped `threat.general.device_time` raw log field to `event.idm.read_only_udm.principal.asset.last_discover_time` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `device_mac` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `collection_time` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `threat.general.detected_url` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.intermediary.application`: Newly mapped `program` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.about.mac`: Newly mapped `forensics.close_networks.BSSID` raw log field to `event.idm.read_only_udm.about.mac` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `forensics.close_networks.capabilities`, `forensics.close_networks.level`, `forensics.close_networks.SSID`, `forensics.close_networks.frequency`, `forensics.general` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `risk_posture`, `forensics.baseline_traceroute`, `forensics.mitm_traceroute`, `forensics.os`, `forensics.time_interval`, `threat.general.time_interval`, `forensics.attack_time.date`, `device_info.mdm_alt_ids.id`, `device_info.mdm_alt_ids.serialnumber`, `device_info.mdm_alt_ids.uuid`, `threat.status`, `threat.mitigation_reason`, `threat.triggered_actions`, `threat.general.ip_of_detected_url`, `threat.general.android_enterprise_management_state`, `threat.general.android_enterprise_access_network_states`, `threat.general.action_triggered`, `forensics.network_threat.arp_tables.before`, `threat.general.threat_type`, `threat.child_threat_uuids`, `device_info.mdm_device_id`, `forensics.event_id`, `forensics.zdid`, `forensics.threat_uuid`, `forensics._id.$oid`, `additional_public_forensics`, `threat.general.attacker_ssid`, `threat.general.attacker_bssid`, `device_info.tag1`, `device_info.tag2`, `user_info.user_role`, `threat.general.network_interface` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when the log contains user related data.  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when the log contains principal machine related data log.   
2025-11-27 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Mapped multiple raw log fields to this UDM field. These were previously mapped to various deprecated label structures. The raw fields include: `sample`, all fields from `forensics.suspicious_profile` and `forensics.untrusted_profile`, `forensics.sideloaded_app_name`, `forensics.dynamic_internal_name`, `forensics.network_threat.basestation`, `forensics.network_threat.routing_table`, `forensics.network_threat.interface`, `forensics.network_threat.net_stat`, `forensics.dynamic_trigger`, `forensics.network_subnet`, `forensics.type`, `forensics.forensics_ziap_version`, `forensics.BSSID`, `forensics.network_encryption`, `forensics.responses`, `forensics.SSID`, `sideloaded_app_filehash_data`, `threat.general.sideloaded_app_name`, `team_id`, and `team_name`.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Removed mapping of `device_info.device_time`, `device_info.zdid`, `device_info.jailbroken`, and `threat.general.base_station` from this UDM field.  
\- `event.idm.read_only_udm.principal.asset.labels`: Mapped `device_info.device_time`, `device_info.zdid`, `device_info.jailbroken`, and `threat.general.base_station` raw log fields to this UDM field.  
\- Renamed from `sideloaded_app_name_label` to `forensics_sideloaded_app_name_label`.  
\- Updated conditional check for `forensics.network_subnet`, `forensics.BSSID`, `forensics.network_encryption`, and `forensics.SSID` to ensure the fields are not empty strings before mapping.  
\- Updated the data structure for label values to use a typed format (e.g., `value.string_value`) to align with the requirements for the `event.idm.read_only_udm.additional.fields` field.   
2025-11-24 |  Enhancement:  
\- Updated the conditional logic for populating event.idm.read_only_udm.principal.asset.product_object_id. The logic now uses device_info.mdm_device_id as a fallback if the device_info.imei field is not present, rather than checking if it was an empty string.  
\- Removed the initialization of device_info.imei to an empty string, allowing the parser to correctly check for the field's existence.   
2025-11-20 |  Enhancement:  
\- `event.idm.read_only_udm.principal.asset.labels`: Removed mapping of `device_info.zdid`, `device_info.jailbroken`, `threat.general.base_station` from `event.idm.read_only_udm.principal.asset.labels` UDM field since it is a deprecated field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped `device_info.zdid`, `device_info.jailbroken`, `threat.general.base_station` raw log field(s) to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.about.labels`: Removed mapping of `sample_field`, `forensics.profile.name`, `forensics.sideloaded_app_name`, `forensics.profile.type`, `forensics.profile.external_id`, `forensics.profile.category`, `forensics.profile.description`, `forensics.profile.information`, `forensics.untrusted_profile.name`, `forensics.untrusted_profile.type`, `forensics.untrusted_profile.external_id`, `forensics.untrusted_profile.category`, `forensics.untrusted_profile.description`, `forensics.untrusted_profile.information`, `forensics.dynamic.internal_name`, `forensics.network_threat.basestation`, `forensics.network_threat.routing_table`, `forensics.network_threat.interface`, `forensics.network_threat.net_stat`, `forensics.dynamic.trigger`, `forensics.network.subnet`, `forensics.type`, `forensics.forensics.ziap_version`, `forensics.BSSID`, `forensics.network.encryption`, `forensics.responses`, `forensics.SSID`, `team_id`, `team_name` from `event.idm.read_only_udm.about.labels` UDM field since it is a deprecated field.  
\- `event.idm.read_only_udm.about.resource.attribute.labels`: Mapped these raw log fields to `event.idm.read_only_udm.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `data.file_hash`, `threat.general.sideloaded_app_name` from `event.idm.read_only_udm.security_result.about.labels` UDM field since it is a deprecated field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Mapped `data.file_hash`, `threat.general.sideloaded_app_name` raw log field(s) to `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped the `forensics.severity` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.asset.platform_software.platform`: Mapped the `forensics.os` and `device_info.os` raw log fields to `event.idm.read_only_udm.principal.asset.platform_software.platform` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Mapped the `device_info.device_time` raw log field to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.group.product_object_id`: Mapped the `device_info.device_group_id` raw log field to `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Added fallback mapping for `device_info.mdm_device_id` when `device_info.imei` is unavailable.  
\- Added conditional check for `system_token` to not be empty.   
2025-02-26 |  Enhancement:  
\- Mapped `sideloaded_app_filehash` to `security_result.about.labels`.   
2025-02-11 |  Enhancement:  
\- Mapped `threat.general.file_hash` to `event.idm.read_only_udm.principal.file.sha1`.   
2024-12-19 |  Enhancement:  
\- Changed the mapping of `data.value` from `security_result.threat_name` to `security_result.about.url`.   
2024-12-02 |  Enhancement:  
\- Mapped `device_info.device_group_name` to `target.group.group_display_name`.   
2024-11-21 |  Enhancement:  
\- Mapped `additional_public_forensics.Package Name` to `security_result.threat_name`.   
2024-04-16 |  Enhancement:  
\- Mapped `hostname` from syslog header to `intermediary.hostname`.  
\- Mapped `forensics.sideloaded_app_name` to `about.labels`.  
\- Mapped `threat.general.sideloaded_app_name` to `security_result.about.labels`.   
2023-08-18 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
