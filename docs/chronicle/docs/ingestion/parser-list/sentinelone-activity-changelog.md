---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-activity-changelog/
title: Change log for SENTINELONE_ACTIVITY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:33:46.217322+00:00
---

# Change log for SENTINELONE_ACTIVITY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sentinelone-activity-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SENTINELONE_ACTIVITY

Date | Changes  
---|---  
2026-06-11 |  Enhancement:  
\- Added support for `SYSLOG+KV` format.  
\- Modified grok patterns to handle Syslog format and added kv filter to parse header and body data.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `syslog_timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `body_createdAt` raw log field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field when `syslog_timestamp` is null.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `syslog_version` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.intermediary.ip`: Newly mapped `syslog_hostname` and `body_mgmtAddress` raw log fields to `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `syslog_hostname` raw log fields to `event.idm.read_only_udm.intermediary.hostname` UDM field when its not an IP address.  
\- `event.idm.read_only_udm.metadata.product_name`: Newly mapped `syslog_app` raw log field to `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `log_description` raw log field to `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `header_accountName` raw log field to `event.idm.read_only_udm.principal.namespace` UDM field.  
\- `event.idm.read_only_udm.principal.namespace`: Newly mapped `body_accountName` raw log field to `event.idm.read_only_udm.principal.namespace` UDM field when `header_accountName` is null.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `header_deviceAddress` raw log field with `event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `header_deviceHostName` raw log field to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.description`: Newly mapped `header_eventDesc` raw log field to `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `header_eventID` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `header_siteName` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field.  
\- `event.idm.read_only_udm.principal.location.name`: Newly mapped `body_siteName` raw log field to `event.idm.read_only_udm.principal.location.name` UDM field when `header_siteName` is null.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `header_sourceAgentId` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `body_agentId` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field when `header_sourceAgentId` is null.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `header_sourceAgentUuid` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `header_sourceGroupId` raw log field to `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.group.product_object_id`: Newly mapped `body_groupId` raw log field to `event.idm.read_only_udm.principal.group.product_object_id` UDM field when `header_sourceGroupId` is null.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `header_sourceGroupName` raw log field to `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.group.group_display_name`: Newly mapped `body_groupName` raw log field to `event.idm.read_only_udm.principal.group.group_display_name` UDM field when `header_sourceGroupName` is null.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `header_sourceHostName` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.hostname`, `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `body_computerName` raw log field to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields when `header_sourceHostName` is null.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `header_sourceIpAddresses` and `body_ipAddress` raw log fields to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `header_sourceMacAddresses` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM fields.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `header_sourceOsRevision` raw log field to `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `header_sourceOsType` raw log field to `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.user.windows_sid`: Newly mapped `header_sourceUserId` raw log field to `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `header_sourceUserName` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `header_eventSeverity` raw log field to `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.security_result.severity_details`: Newly mapped `header_eventSeverity` raw log field to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.metadata.vendor_name`: Newly mapped `header_vendor` raw log field to `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `body_activityType` raw log field to `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.target.asset.product_object_id`: Newly mapped `body_activityUuid` raw log field to `event.idm.read_only_udm.target.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `body_fullScopeDetails` raw log field to `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.principal.file.sha256`: Newly mapped `body_hash` raw log field to `event.idm.read_only_udm.principal.file.sha256` UDM field.  
\- `event.idm.read_only_udm.metadata.collected_timestamp`: Newly mapped `body_updatedAt` raw log field to `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `body_userId` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `sourceThreatCount` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `notificationScope`, `siteId`, `sourceDnsDomain`, `sourceMgmtPrecievedAddress`, `sourceNetworkState`, `agentUpdatedVersion`, `cat`, `comments`, `assetType`, `assetVersionsList`, `buildVersion`, `externalServiceId`, `fullScopeDetailsPath`, `scopeLevel`, `scopeName`, `sourceType`, `osFamily`, `secondaryDescription` and `syslog_procid` raw log fields to `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `activityId`, `deviceHostFqdn`, `originatorName`, `originatorVersion`, `sourceFqdn`, `syslog_msgid` and `syslog_pri` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-06-04 |  \- Added gsub to convert raw log into proper JSON format logs.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped `dataSource.vendor` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `data.event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `activity_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.user.windows_sid: Newly mapped `data.agent.last_logged_in_user_sid` raw log field with `event.idm.read_only_udm.principal.user.windows_sid` UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `data.agent.os_name` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.principal.platform_version: Newly mapped `data.agent.os_revision` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `data.agent.uuid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.group.product_object_id: Newly mapped `data.group_id` raw log field with `event.idm.read_only_udm.principal.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.group.group_display_name: Newly mapped `data.group_name` raw log field with `event.idm.read_only_udm.principal.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.principal.ip, event.idm.read_only_udm.principal.asset.ip: Newly mapped `data.ip_address`, `interface.gateway_ip`, `interface.inet6`, `interface.inet4`, `data.agent.external_ip` raw log fields with `event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.mac, event.idm.read_only_udm.principal.asset.mac: Newly mapped `interface.physical` raw log field with `event.idm.read_only_udm.principal.mac and event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly mapped `interface name`, `data.agent.os_type`, `data.os_type`, `data.device_name`, `data.scope_level`, `data.scope_name`, `data.agent.group.name`, `data.computer_name`, `data.group_name`, `data.full_scope_details`, `data.full_scope_details_path` raw log fields with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.last_update_time: Newly mapped `updated_at` raw log field with `event.idm.read_only_udm.principal.asset.attribute.last_update_time` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `account_id` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.namespace: Newly mapped `account_name` raw log field with `event.idm.read_only_udm.principal.namespace` UDM field.  
\- event.idm.read_only_udm.target.ip, event.idm.read_only_udm.target.asset.ip: Newly mapped `serverIP` raw log field with `event.idm.read_only_udm.target.ip and event.idm.read_only_udm.target.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.location.name: Newly mapped `site_name` raw log field with `event.idm.read_only_udm.principal.location.name` UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `agent_id` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `data.agent.computer_name` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `data.agent.computer_name` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `data.rule_type` raw log field with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `data.rule_id` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.principal.user.group_identifiers: Newly mapped `data.agent.group.id`, `group_id` raw log fields with `event.idm.read_only_udm.principal.user.group_identifiers` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `dataSource.category`, `data.agent.active_threat_count` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.principal.user.attribute.labels: Newly mapped `data.agent.last_logged_in_user_name`, `account.name`, `account.id`, `data.agent.last_active_date` raw log fields with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `activity_uuid`, `secondary_description`, `data.agent.registered_at`, `context`, `dataSource.name`, `data.build_version`, `data.agent.network_status`, `data.registered_at`, `product_id`, `data.agent.agent_version`, `data.interface`, `site_id`, `site.id`, `data.event_time`, `primary_description`, `check`, `created_at`, `data.creator`, `data.device_class`, `data.event_type`, `data.mgmt_address`, `data.minor_class`, `data.source_type`, `data.uid`, `data.c`, `data.version`, `data.lmp_version`, `data.notification_processing_mode`, `data.profile_uuids`, `data.vendor_id`, `time`, `sca:RetentionType`, `activity_id`, `logfile`, `data.agent.id`, `parser`, `data.site_name`, `dataset` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set the `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED` when necessary raw log fields are present.   
2025-10-10 |  \- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `createdAt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.last_updated_time: Newly mapped `updatedAt` raw log field with `event.idm.read_only_udm.security_result.last_updated_time` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `activityUuid`, `activityID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `primaryDescription`, event_name raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `rt` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `activityType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `device_product` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `data.ipAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `data.ipAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `data.sourceprocesscommandline` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.principal.process.file.names: Newly mapped `data.sourceprocessname` raw log field with `event.idm.read_only_udm.principal.process.file.names` UDM field.  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `agentId` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `data.computerName` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `data.computerName` raw log field with `event.idm.read_only_udm.target.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.namespace: Newly mapped `accountName` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.target.location.name: Newly mapped `siteName, `data.siteName` raw log field with `event.idm.read_only_udm.target.location.name` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Newly mapped `accountId` raw log field with `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.target.user.user_display_name: Newly mapped `data.accountName` raw log field with `event.idm.read_only_udm.target.user.user_display_name` UDM field.  
\- event.idm.read_only_udm.target.group.product_object_id: Newly mapped `data.newGroupId` raw log field with `event.idm.read_only_udm.target.group.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.group.group_display_name: Newly mapped `data.newGroupName` raw log field with `event.idm.read_only_udm.target.group.group_display_name` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `id`, `notificationScope`, `data.scopeLevel`, `data.fullScopeDetailsPath`, `siteId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `data.sourceType` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `data.alertid` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `data.ruledescription`, `data.oldGroupName`, `data.oldGroupId`, `data.newGroupId`, `data.newGroupName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `data.fullScopeDetails` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal and has_target are `true`, updated to NETWORK_CONNECTION.  
\- event.idm.read_only_udm.metadata.event_type: If has_principal is `true`, updated to STATUS_UPDATE.  
\- event.idm.read_only_udm.metadata.event_type: If has_user is `true`, updated to USER_LOGIN.  
\- event.idm.read_only_udm.metadata.event_type: If none of the above conditions are met, updated to GENERIC_EVENT.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
