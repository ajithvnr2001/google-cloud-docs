---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardicore-centra-changelog/
title: Change log for GUARDICORE_CENTRA \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:56.321063+00:00
---

# Change log for GUARDICORE_CENTRA  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/guardicore-centra-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GUARDICORE_CENTRA

Date | Changes  
---|---  
2026-04-09 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `Time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `Timestamp` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field to `BLOCK` if `Action` is `Blocked`, or to `ALLOW` if `Action` is `Allowed`.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `ConnectionType` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `Protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `Source.IP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `Source.Port` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `Source.AssetName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Source.UserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.names`: Newly mapped `Source.ProcessName` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `Source.ProcessPath` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `Destination.IP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `Destination.Port` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.target.process.file.names`: Newly mapped `Destination.ProcessName` raw log field with `event.idm.read_only_udm.target.process.file.names` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `ID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `DeviceVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `SignatureID` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `Description` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `DisplayHostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `PolicyRule` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `PolicyRuleSet` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `Source.ApplicationName` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `Source.UserIdentity` raw log field with `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `Worksite` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `Source.AssetLabels`, `Platform`, `Type`, `Source.AssetLabelGroups`, `Environment` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.attribute.roles`: Newly mapped `Role` raw log field with `event.idm.read_only_udm.principal.user.attribute.roles` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `ConnectionVerdict` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `DeviceVendor`, `DeviceProduct`, `Count` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `Destination.ApplicationName` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.resource.resource_subtype`: Newly mapped `Application` raw log field with `event.idm.read_only_udm.principal.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.target.user.user_display_name`: Newly mapped `Destination.UserIdentity` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Destination.AssetLabels`, `Destination.AssetLabelGroups` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `Incidents`, `syslog_priority` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path`: Newly mapped `Destination.ProcessPath` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `Destination.UserName` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Destination.AssetName`, `FQDN` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- Added a Grok pattern for `message` to parse the raw log fields.   
2025-06-10 |  Enhancement:  
\- Added Gsub for `kv_data`.  
\- Added conditional check for `kv_data`.  
\- Added Grok patterns for field `src` to check if `src` is a IP or not.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `Assetname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `Assetname` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.target.asset.asset_id`: Newly mapped `Assetid` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `IPAddresses` raw log fields with `event.idm.read_only_udm.principal.ip` UDM field.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `IPAddresses` raw log fields with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `prin_port` raw log fields with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped `vCenterhost` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `vCenterhost` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `Location` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `Addedlabels`, `Removedlabels`, and `Resultinglabels` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.group.attribute.labels`: Newly mapped `ResultinglabelGroups`,`AddedLabelGroups`, and `RemovedLabelGroups` raw log field with `event.idm.read_only_udm.target.group.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `Changecause` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `Changedby` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- When `severity` is equal to `0`, `1`, `2`, or `3` then mapped `LOW` to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- When `severity` is equal to `4`, `5`, or `6` then mapped `MEDIUM` to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- When `severity` is equal to `7` or `8` then mapped `HIGH` to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- When `severity` is equal to `9` or "10 then mapped `CRITICAL` to `event.idm.read_only_udm.security_result.severity` UDM field.   
2025-03-28 |  Enhancement:  
\- Added Grok patterns to extract KV data from the logs.  
\- Added `else if` conditional check for `cs1` and `cs1Label`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cs1` and `cs1Label` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `act` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.ip,event.idm.read_only_udm.principal.asset.ip: Newly mapped `src` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.ip,event.idm.read_only_udm.target.asset.ip: Newly mapped `dst` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.target.port: Newly mapped `dpt` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- event.idm.read_only_udm.target.host,event.idm.read_only_udm.target.asset.hostname: Newly mapped `dhost` raw log field with `event.idm.read_only_udm.target.host` and `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly mapped `proto` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- event.idm.read_only_udm.target.asset.platform_software.platform: Newly mapped `os_type` raw log field with `event.idm.read_only_udm.target.asset.platform_software.platform` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `cs4` and `cs4Label` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `Aplicacion` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.target.resource.name: Newly mapped `ConexionServ_RedRespaldoicio` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Ambiente` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.resource_subtype: Newly mapped `Servicio` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- event.idm.read_only_udm.target.platform_version: Newly mapped `os_name` raw log field with `event.idm.read_only_udm.target.platform_version` UDM field.  
\- event.idm.read_only_udm.target.process.command_line, event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `dproc` raw log field with `event.idm.read_only_udm.target.process.command_line` UDM field else mapped it to `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `cs15Label` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `cs6Label` and `cs6` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `cs7Label` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `Entorno` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `Gestion` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `cs10` and `cs10Label` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `duser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `cs16Label` and `cs16` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.intermediary.asset.ip: Newly mapped `dvc` raw log field with `event.idm.read_only_udm.intermediary.asset.ip` UDM field.   
2024-12-04 |  Enhancement:  
\- Mapped start to `metadata.event_timestamp`.   
2024-11-05 |  Enhancement:  
\- Added support for new pattern of CEF logs.   
2024-10-09 |  Enhancement:  
\- Added support to parse the unparsed logs.  
\- Changed mapping of `os_name` , `enforcement` ,and `AssetType` from `additional.fields` to `security_result.detection_fields`.   
2024-08-30 |  Enhancement:  
\- Modified the Grok pattern to parse new log types.  
\- Mapped `source.vm.name` to `principal.hostname`.  
\- Mapped `bucket_id`, `policy_verdict`, `network_profile`, `source_process_hash`, and `display_provider` to `security_result.detection_fields`.  
\- Mapped `display_type` to `principal.platform`.   
2024-04-19 |  Enhancement:  
\- Added support for CEF logs.   
2023-09-08 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
