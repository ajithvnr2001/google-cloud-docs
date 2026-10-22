---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-epo-changelog/
title: Change log for MCAFEE_EPO \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:39.688715+00:00
---

# Change log for MCAFEE_EPO  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/mcafee-epo-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for MCAFEE_EPO

Date | Changes  
---|---  
2026-07-29 |  Enhancement:  
\- Added support for the timestamp format for the `ReceivedUTC` raw log field in the `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Removed mapping of `ThreatEventID` from `event.idm.read_only_udm.security_result.detection_fields` UDM field as it represents a threat ID.  
\- `event.idm.read_only_udm.security_result.threat_id`: Mapped `ThreatEventID` raw log field to `event.idm.read_only_udm.security_result.threat_id` UDM field.  
\- `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `AnalyzerIPV6` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.src.ip`, `event.idm.read_only_udm.src.asset.ip`: Newly mapped `SourceIPV6` raw log field with `event.idm.read_only_udm.src.ip` and `event.idm.read_only_udm.src.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`: Newly mapped `TargetIPV6` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.observer.ip`: Newly mapped `observer.ip` raw log field with `event.idm.read_only_udm.observer.ip` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `ThreatActionTaken` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.   
2026-04-07 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.command_line`: Newly mapped `SourceDescription` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.last_modification_time`: Newly mapped `SourceModifyTime_data` raw log field with `event.idm.read_only_udm.principal.process.file.last_modification_time` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.last_access_time`: Newly mapped `SourceAccessTime_data` raw log field with `event.idm.read_only_udm.principal.process.file.last_access_time` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.first_seen_time`: Newly mapped `SourceCreateTime_data` raw log field with `event.idm.read_only_udm.principal.process.file.first_seen_time` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `TargetTrusted`, `TargetSigned` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AnalyzerRuleID` , `SourceProcessTrusted` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels` : Newly mapped `TargetPath` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.mac`, `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `RawMACAddress` raw log field with `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.   
2026-03-18 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.severity`: when `severity_source` is `1` or `2`, updated the value of `event.idm.read_only_udm.security_result.severity` to `HIGH` to maintain consistency with `ThreatSeverity` mappings.  
\- `event.idm.read_only_udm.security_result.severity`: when `severity_source` is `5`, `6`, or `7`, updated the value of `event.idm.read_only_udm.security_result.severity` to `LOW` to maintain consistency with `ThreatSeverity` mappings.   
2026-01-21 |  Enhancement:  
\- event.idm.read_only_udm.target.asset.asset_id: Newly mapped `serverid` raw log field with `event.idm.read_only_udm.target.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `analyzername` raw log field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.principal.asset.product_object_id: Newly mapped `autoguid` raw log field with `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `targetfilename` raw log field with `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `targetprocessname` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `targethostname` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `analyzerversion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `sourceusername` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `sourcehostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `agentguid` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- event.idm.read_only_udm.target.namespace: Newly mapped `tenantid` raw log field with `event.idm.read_only_udm.target.namespace` UDM field.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `sourceprocessname` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly mapped `threatname` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM field.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `analyzerhostname` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `autoid` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.url: Newly mapped `sourceurl` raw log field with `event.idm.read_only_udm.principal.url` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `threatseverity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.category_details: Newly mapped `threatcategory` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- event.idm.read_only_udm.intermediary.application: Newly mapped `analyzer` raw log field with `event.idm.read_only_udm.intermediary.application` UDM field.   
2025-10-07 |  Enhancement:  
\- Modified the logic for mapping the `threat_action_taken` raw log field to `event.idm.read_only_udm.security_result.action` UDM field.  
\- Raw logs with `threat_action_taken` equal to `IDS_ALERT_ACT_TAK_DEL` now map event.idm.read_only_udm.security_result.action to BLOCK instead of UNKNOWN_ACTION.  
\- Raw logs with `threat_action_taken` equal to `IDS_ALERT_ACT_TAK_CONT` are now mapped, setting event.idm.read_only_udm.security_result.action to BLOCK.   
2025-09-19 |  Enhancement:  
\- `event.idm.read_only_udm.observer.hostname`: Removed mapping of `sys_host` from `event.idm.read_only_udm.observer.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Mapped `sys_host` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Removed mapping of `MachineName` from `event.idm.read_only_udm.intermediary.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.principal.hostname`: Mapped `MachineName` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field in order to introduce a more accurate mapping for the raw log field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `AgentVersion`, `TimeZoneBias`, `product_family`, `product_name`, `UserInfo`, `OPGData`, `TimeSZone`, `SourceProcessSigned`, `SourceProcessSigner`, `TargetDriveType`, `Version`, `Description`, `tenant_Id`, `bpsId`, `tenantGUID`, `tenantNodePath` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `RawMACAddress` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.user.user_display_name`: Newly mapped `UserName` raw log field to `event.idm.read_only_udm.principal.user.user_display_name` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.md5`: Newly mapped `SourceProcessHash` raw log field to `event.idm.read_only_udm.principal.process.file.md5` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path`: Newly mapped `SourceFilePath` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.size`: Newly mapped `SourceFileSize` raw log field to `event.idm.read_only_udm.principal.process.file.size` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `AnalyzerContentVersion`, `AccessRequested` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-09-02 |  Enhancement:  
\- Added new grok patterns to handle log formats containing `EPO.EPOProductEventsMT`, `EPO_Events.EPOEvents`, or `EPO.OrionAuditLog` data fields.  
\- Added gsub for `event_message` data field to change raw log field of `TenantID` to `TenantId` raw log field.  
\- All new mappings from the JSON payload within the block for messages matching `EPO.EPOProductEventsMT`, `EPO_Events.EPOEvents`, or `EPO.OrionAuditLog` are applied only if the respective raw field exists and is not empty.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `SiteName`, `SourceHostName` raw log field(s) to `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `AutoID` raw log field to `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `HostName`, `TargetHostName` raw log field(s) to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.namespace`: Newly mapped `TenantId` raw log field to `event.idm.read_only_udm.target.namespace` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `host` raw log field to `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped `ProductCode` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.target.user.userid`: Newly mapped `UserName`, `TargetUserName` raw log field to `event.idm.read_only_udm.target.user.userid` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `AnalyzerVersion` raw log field to `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `SourceUserName` raw log field to `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.principal.asset.product_object_id`: Newly mapped `AutoGUID` raw log field to `event.idm.read_only_udm.principal.asset.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `ThreatName` raw log field to `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.mac`: Newly mapped `SourceMAC` raw log field to `event.idm.read_only_udm.principal.mac` UDM field.  
\- `event.idm.read_only_udm.target.mac`: Newly mapped `TargetMAC` raw log field to `event.idm.read_only_udm.target.mac` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `VerMin`, `VerBld`, `Type`, `VerRev`, `VerMjr`, `SPHotFix`, `ExtraDATNames`, `AnalyzerIPV4`, `SourceIPV4`, `AnalyzerEngineVersion`, `TargetProtocol`, `AnalyzerName`, `ThreatActionTaken`, and `DetectedUTC` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.asset_id`: Newly mapped `AgentGUID` raw log field to `event.idm.read_only_udm.target.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac`: Newly mapped `SourceMAC` raw log field to `event.idm.read_only_udm.principal.mac` and `event.idm.read_only_udm.principal.asset.mac` UDM field.  
\- `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac`: Newly mapped `TargetMAC` raw log field to `event.idm.read_only_udm.target.mac` and `event.idm.read_only_udm.target.asset.mac` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `event.idm.read_only_udm.security_result.severity` to `HIGH` if `TVDSeverity` or `ThreatSeverity` is `1` or `2`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `event.idm.read_only_udm.security_result.severity` to `MEDIUM` if `TVDSeverity` or `ThreatSeverity` is `3` or `4`.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `event.idm.read_only_udm.security_result.severity` to `LOW` if `TVDSeverity` or `ThreatSeverity` is `5`, `6`, or `7`.  
\- `event.idm.read_only_udm.security_result.severity_details` : Newly mapped `TVDSeverity` and `ThreatSeverity` raw log fields to `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields` : Newly mapped `ThreatEventID`, `ThreatType`, `ThreatHandled`, `AnalyzerDATVersion`, `ServerID`, `AnalyzerDetectionMethod` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details` : Newly mapped `ThreatCategory` raw log field to `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname`: Newly mapped `AnalyzerHostname` raw log field to `event.idm.read_only_udm.intermediary.hostname` and `event.idm.read_only_udm.intermediary.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.intermediary.application` : Newly mapped `Analyzer` raw log field to `event.idm.read_only_udm.intermediary.application` UDM field.  
\- `event.idm.read_only_udm.intermediary.mac` and `event.idm.read_only_udm.intermediary.asset.mac`: Newly mapped `AnalyzerMAC` raw log field to `event.idm.read_only_udm.intermediary.mac` and `event.idm.read_only_udm.intermediary.asset.mac` UDM field.  
\- `event.idm.read_only_udm.principal.url` : Newly mapped `SourceURL` raw log field to `event.idm.read_only_udm.principal.url` UDM field.  
\- `event.idm.read_only_udm.target.port` : Newly mapped `TargetPort` raw log field to `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.process.file.full_path` : Newly mapped `SourceProcessName` raw log field to `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.process.file.full_path` : Newly mapped `TargetProcessName` raw log field to `event.idm.read_only_udm.target.process.file.full_path` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `TargetIPV4` raw log field to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.file.full_path` : Newly mapped `TargetFileName` raw log field to `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id` : Newly mapped `TVDEventID` raw log field to `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.collected_timestamp` : Newly mapped `DetectedUTC` raw log field to `event.idm.read_only_udm.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.target.user.attribute.labels` : Newly mapped `Version`, `NodeID` raw log field to `event.idm.read_only_udm.target.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Default update to `NETWORK_CONNECTION` if `has_principal` and `has_target` are `true` and no other event type logic is met.  
\- The update to the date filter to map the `sys_time` data field to `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-08-26 |  Enhancement:  
\- Added XML path support for the `Analyzer` raw log field.  
\- Modified logic to update `event.idm.read_only_udm.security_result.action` based on different values of the `ThreatActionTaken` raw field, including mapping IDS_ALERT_ACT_TAK_DEL to `UNKNOWN_ACTION`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `AnalyzerVersion`, `analyzer_engine_version`, `Time_Zone_Bias`, `attack_vector_type`, `product_family` and `blade_name` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `AMCoreContentVersion`, `DurationBeforeDetection`, `AnalyzerContentCreationDate`, `ThreatDetectedOnCreation`, `AnalyzerDetectionMethod`, `cleanable`, `first_action_status`, `first_attempted_action`, `analyzer_dat_version`, `analyzer_gti_query` and `second_attempted_action` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `threat_action_taken` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.observer.namespace: Newly mapped `analyzer_name` raw log field with `event.idm.read_only_udm.observer.namespace` UDM field.  
\- event.idm.read_only_udm.target.file.last_modification_time: Newly mapped `target_modify_time` raw log field with `event.idm.read_only_udm.target.file.last_modification_time` UDM field.  
\- event.idm.read_only_udm.target.file.last_access_time: Newly mapped `target_access_time` raw log field with `event.idm.read_only_udm.target.file.last_access_time` UDM field.  
\- event.idm.read_only_udm.target.file.first_seen_time: Newly mapped `target_create_time` raw log field with `event.idm.read_only_udm.target.file.first_seen_time` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `natural_lang_description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `ThreatSeverity` raw log field with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `DetectionMessage` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2025-08-12 |  Enhancement:  
\- Mapped the following raw log fields to `event.idm.read_only_udm.additional.fields`: `Error`, `ProductID`, `InitiatorID`, `InitiatorType`, `SiteName`, and `Locale`."   
2025-05-12 |  Enhancement:  
\- Added Grok pattern to support the `Trellix` pattern of logs with (SYSLOG + KV) format and relevant corresponding raw log fields.  
\- event.idm.read_only_udm.metadata.vendor_name: Set the value of `event.idm.read_only_udm.metadata.vendor_name` to `Trellix` for `Trellix` pattern of logs.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `sys_host` raw log field with `event.idm.read_only_udm.observer.hostname` UDM field.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped `product_name` field with `event.idm.read_only_udm.metadata.product_name` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `event_name` and `workflowid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `alertId` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `agentGUID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.summary: Newly mapped `alertType` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `eventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.principal.hostname & event.idm.read_only_udm.principal.asset.hostname: Newly mapped `host` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields and set `has_principal` to `true`.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Newly mapped `sourceIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to `true`.  
\- event.idm.read_only_udm.target.ip & event.idm.read_only_udm.target.asset.ip: Newly mapped `targetIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields and set `has_target` to `true`.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `operatingSystem` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `eventname` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `eventTimestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.target.process.file.full_path: Newly mapped `eventObject` raw log field with `event.idm.read_only_udm.target.process.file.full_path` UDM field and set `has_target_resource` to `true`.  
\- event.idm.read_only_udm.principal.process.file.full_path: Newly mapped `eventProgramName` raw log field with `event.idm.read_only_udm.principal.process.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `eventProgramUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.process.command_line: Newly mapped `eventCommandLine` raw log field with `event.idm.read_only_udm.principal.process.command_line` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `threatSeverity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: Set the value of `event.idm.read_only_udm.metadata.event_type` to `USER_RESOURCE_ACCESS` if `has_user` is `true` and `has_target_resource` is `true`.  
\- event.idm.read_only_udm.metadata.event_type: Set the value of `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` if `has_principal` is `true`.   
2025-05-02 |  Enhancement:  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `ThreatSeverity` and `Severity` raw log fields with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `Name` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.target.file.md5: Newly mapped `TargetHash` raw log field with `event.idm.read_only_udm.target.file.md5` UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Removed mapping of `filename` from `event.idm.read_only_udm.target.file.full_path` UDM field.  
\- event.idm.read_only_udm.principal.file.full_path: Mapped `filename` field with `event.idm.read_only_udm.principal.file.full_path` UDM field.  
\- event.idm.read_only_udm.target.administrative_domain: Removed mapping of `domain` from `event.idm.read_only_udm.target.administrative_domain` UDM field.  
\- event.idm.read_only_udm.principal.administrative_domain: Mapped `domain` field with `event.idm.read_only_udm.principal.administrative_domain` UDM field.  
\- event.idm.read_only_udm.target.user.userid: Removed mapping of `userid` from `event.idm.read_only_udm.target.user.userid` UDM field.  
\- event.idm.read_only_udm.principal.user.userid: Mapped `userid` field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- Added a new Grok pattern to add support for logs getting dropped even after having some important data.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `custom_date` field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.principal.ip & event.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields and set `has_principal` to `true`.   
2025-04-24 |  Enhancement:  
\- If `ThreatActionTaken` raw log field value is `IDS_ALERT_ACT_TAK_DEN`, then set `security_result.action` as `BLOCK`.   
2025-03-19 |  Enhancement:  
\- Removed the mapping of `username` from `target.user.userid` and changed to `principal.user.userid`.  
\- Removed the mapping of `agentdomainname` from `target.administrative_domain` and changed to `principal.administrative_domain`.  
\- Mapped `filepath` to `principal.file.full_path`.  
\- Mapped `Actionname` to `security_result.detection_fields`.  
\- Added IP Address check for `agentipaddress`.   
2024-11-20 |  Enhancement:  
\- Added additional field mapping for XML logs.   
2024-10-01 |  Enhancement:  
\- When `tvdeventid` is `1027` or `scantype` is `*Scan*`, then mapped `username` to `target.user.userid`.  
\- When `tvdeventid` is `1027` or `scantype` is `*Scan*`, then mapped `agentdomainname` to `target.administrative_domain`.  
\- When `tvdeventid` is `1027` or `scantype` is `Endpoint Security Threat Prevention`, then mapped `domain` and `userid` from `UserName` to `target.administrative_domain` and `target.user.userid` respectively.   
2024-08-29 |  Enhancement:  
\- Added support to handle dropped logs.   
2024-08-12 |  Enhancement:  
\- Changed mapping for `Description` from `metadata.description` to `security_result.description`.  
\- Mapped `Name` to `metadata.description`.  
\- Mapped `ThreatAction` to `security_result.action_details`.   
2024-08-07 |  Enhancement:  
\- Added support to handle unparsed JSON logs.  
\- Mapped `ActionID`, `ReasonID`, `RatingID`, `ListID`, `PhishingRatingID`, `DownloadRatingID`, `SpamRatingID`, `PopupRatingID`, `BadLinkRatingID`, `ExploitRatingID`, and `ContentID` to `additional.fields`.   
2023-10-15 |  Enhancement:  
\- Handeled XML logs having `product_name` as `MOVE AV Agentless` or `MSME`.   
2023-06-20 |  Enhancement:  
\- Added grok pattern to handle xml logs.   
2023-01-02 |  Enhancement - Added gsub to remove empty namespace with prefix.   
2022-12-16 |  Bug-fix  
\- Added code block to handle `is_DLPAGENT11600`.  
\- Added code block for product names specific.  
\- Added `GENERIC_EVENT` wherever possible if principal and target UDM fields are null.  
\- Mapped normalized_ip_address to `principal.ip`.  
\- Mapped normalized_mac_address to `principal.mac` wherever possible.   
2022-09-14 |  Enhancement - Merged The customer specific-version to default by Handling Log formats of type Key-value pairs.  
\- Provided on_error check for `Content.ParentProcessFileName`.   
2022-09-09 |  Enhancement - Parsed logs of type `Solidifier` which were being dropped earlier.  
\- Logs are present in CSV format so following additional mappings have been defined for the particular columns :  
\- Mapped `column8` to `principal.hostname`.  
\- Mapped `column11` to `principal.mac`.  
\- Mapped `column25` to `target.process.file.full_path`.  
\- Mapped `column30` to `security_result.action`. It is mapped to `BLOCK` if value contains `deny` else mapped as `ALLOW` in case of some other value apart from none.  
\- Mapped `metadata.event_type` to `STATUS_UPDATE`.   
2022-08-11 |  Bug-Fix -  
\- Remapped AnalyzerHostname to intermediary.hostname.  
\- Remapped sys_host to observer.hostname.   
2022-07-27 |  Enhancement - Mapped the following field:  
\- Mapped `csv_mcafee_security.column4` to `principal.asset.first_seen_time`.   
2022-07-14 |  Enhancement - Mapped the following fields:  
\- Mapped `product_version` to `metadata.product_version`.  
\- Mapped `FileSHA1Hash` to `target.process.file.sha1`.  
\- Added code block to handle event_id `35103`.  
\- Changed event_type from `GENERIC_EVENT` to `STATUS_UPDATE` wherever possible.   
2022-05-05 |  Enhancement - Mapped the following fields:  
\- SourceHostname to principal.hostname. If SourceHostname is null mapped AnalyserHostname to principal.hostname.  
\- MachineName to observer.hostname.  
\- AnalyserHostname to intermediate.hostname.  
\- IP header csv 9 to principal.ip.  
\- IP header csv 17 to target.ip.  
\- ThreatName header csv 28 to security_result.threat_name commonly for all.   
2022-04-12 |  Added generic string for Vendor name and replaced different product names to a generic value string.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
