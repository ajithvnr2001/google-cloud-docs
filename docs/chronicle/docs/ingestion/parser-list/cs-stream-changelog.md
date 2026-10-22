---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-stream-changelog/
title: Change log for CS_STREAM \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:52.167076+00:00
---

# Change log for CS_STREAM  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cs-stream-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CS_STREAM

Date | Changes  
---|---  
2026-08-24 |  Enhancement:  
\- Parser overhaul version to make it more efficient and increase fields coverage. You can see the full list of changes in the parser documentation page https://docs.cloud.google.com/chronicle/docs/ingestion/default-parsers/cs-stream.   
2026-03-16 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_data.IOCType` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Refactored the logic to determine the value of `event.idm.read_only_udm.security_result.action` UDM field based on the following conditions:  
\- Set to `BLOCK` if `event_data.PatternDispositionValue` is `2048` AND `event_data.PatternDispositionFlags.ProcessBlocked` is `true` AND `event_data.PatternDispositionFlags.PolicyDisabled` is `false`.  
\- Set to `BLOCK` if `event_data.PatternDispositionValue` is `4096` AND `event_data.PatternDispositionFlags.RegistryOperationBlocked` is `true` AND `event_data.PatternDispositionFlags.PolicyDisabled` is `false`.   
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.target.application`: Newly mapped `event_data.SsoApplicationIdentifier` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `event_data.LocationCountryCode` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `event_data.ActivityBrowser` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_data.ActivityId`, `event_data.SourceEndpointIpReputation`, `event_data.DataDomains`, `event_data.SourceIpIspClassification`, `event_data.SourceIpIspDomain`, `event_data.ActivityOperatingSystem`, `event_data.ModelAnomalyIndicators`, `event_data.SourceEndpointIpReputationList`, `event_data.SourceIpAsnCode`, `event_data.SourceIpAsnOrganization` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-03-04 |  Enhancement:  
\- `event.idm.read_only_udm.target.file.sha256`: Removed mapping of `event_data.IOCValue` from `event.idm.read_only_udm.target.file.sha256` UDM field. As it is more suited to be mapped to `event.idm.read_only_udm.about.file.sha256`.  
\- `event.idm.read_only_udm.about.file.sha256`: If `event_data.IOCType` is `hash_sha256` and `event_data.IOCValue` is a valid SHA256 hash, Set the value of `event_data.IOCValue` to `event.idm.read_only_udm.about.file.sha256`.   
2026-02-19 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `event_data.RuleId` log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `event_data.RuleName` log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_set`: Newly mapped `event_data.RuleTopic` log field with `event.idm.read_only_udm.security_result.rule_set` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `event_data.ItemId` log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_data.HasNewlyDetectedCredentials` (key: `HasNewlyDetectedCredentials`), `event_data.NotificationId` (key: `NotificationId`), `event_data.MatchedTimestamp` (key: `MatchedTimestamp`) log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `event_data.ItemPostedTimestamp` (key: `ItemPostedTimestamp`), `event_data.ItemType` (key: `ItemType`) log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`:  
\- If `event_data_rulepriority` is `DEBUG`, `INFO`, `AUDIT`, updated the value of `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL`.  
\- If `event_data_rulepriority` is `ERROR`, updated the value of `event.idm.read_only_udm.security_result.severity` to `ERROR`.  
\- If `event_data_rulepriority` is `CRITICAL`, updated the value of `event.idm.read_only_udm.security_result.severity` to `CRITICAL`.  
\- If `event_data_rulepriority` is `LOW`, updated the value of `event.idm.read_only_udm.security_result.severity` to `LOW`.  
\- If `event_data_rulepriority` is `MEDIUM`, `WARN` updated the value of `event.idm.read_only_udm.security_result.severity` to `MEDIUM`.  
\- If `event_data_rulepriority` is `HIGH`, updated the value of `event.idm.read_only_udm.security_result.severity` to `HIGH`.   
2026-02-12 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_data.PatternDispositionFlags.Detect`, `event_data.PatternDispositionFlags.OperationBlocked`, `event_data.PatternDispositionFlags.QuarantineFile`, `event_data.PatternDispositionFlags.BootupSafeguardEnabled`, `event_data.PatternDispositionFlags.PolicyDisabled`, `event_data.PatternDispositionFlags.KillParent` and `event_data.PatternDispositionFlags.SuspendParent` raw log fields to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-10 |  Enhancement:  
\- Refactored the logic to determine the value of `event.idm.read_only_udm.security_result.action` UDM field based on the following conditions:  
\- Set to `QUARANTINE` if `event_data.PatternDispositionFlags.QuarantineFile` is `true`.  
\- Set to `ALLOW` if `event_data.PatternDispositionFlags.OperationBlocked` is `false` AND `event_data.PatternDispositionFlags.PolicyDisabled` is `false`.  
\- Set to `ALLOW` if `event_data.PatternDispositionFlags.OperationBlocked` is `true` AND `event_data.PatternDispositionFlags.PolicyDisabled` is `true`.  
\- Set to `BLOCK` if `event_data.PatternDispositionFlags.OperationBlocked` is `true` AND `event_data.PatternDispositionFlags.PolicyDisabled` is `false`.  
\- Otherwise, the value is set to `ALLOW`, `BLOCK`, `QUARANTINE`, or `ALLOW_WITH_MODIFICATION` based on specific values of the `event_data.PatternDispositionValue` field.  
\- `event.idm.read_only_udm.additional.fields` : Newly mapped `event.PatternDispositionFlags.QuarantineMachine` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.process.pid`: Newly mapped `event_data.ProcessId` raw log field to `event.idm.read_only_udm.principal.process.pid`.  
\- `event.idm.read_only_udm.principal.process.parent_process.pid`: Newly mapped `event_data.ParentProcessId` raw log field to `event.idm.read_only_udm.principal.process.parent_process.pid`.  
\- `event.idm.read_only_udm.target.file.md5`: Newly mapped `event_data.MD5String` raw log field to `event.idm.read_only_udm.target.file.md5`.  
\- `event.idm.read_only_udm.target.file.sha1`: Newly mapped `event_data.SHA1String` raw log field to `event.idm.read_only_udm.target.file.sha1`.  
\- `event.idm.read_only_udm.principal.user.group_identifiers`: Newly mapped `event_data.LogonDomain` raw log field to `event.idm.read_only_udm.principal.user.group_identifiers`.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.names`: Newly mapped `event_data.ParentImageFileName` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.names`.  
\- `event.idm.read_only_udm.principal.process.parent_process.command_line`: Newly mapped `event_data.ParentCommandLine` raw log field to `event.idm.read_only_udm.principal.process.parent_process.command_line`.  
\- `event.idm.read_only_udm.about`: Newly mapped `event_data.AssociatedFile` raw log field to `event.idm.read_only_udm.about`.  
\- `event.idm.read_only_udm.principal.process.parent_process.file.full_path`: Newly mapped `event_data.ParentImageFilePath` raw log field to `event.idm.read_only_udm.principal.process.parent_process.file.full_path`.  
\- `event.idm.read_only_udm.security_result.risk_score`: Newly mapped `event_data.RiskScore` raw log field to `event.idm.read_only_udm.security_result.risk_score`.  
\- `event.idm.read_only_udm.target.file.names`: Newly mapped `event_data.FilesAccessed.FileName`, `event_data.FilesWritten.FileName` raw log fields to `event.idm.read_only_udm.target.file.names`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_data.FilesAccessed.Timestamp`, `event_data.FilesAccessed.FilePath`, `event_data.FilesWritten.Timestamp`, `event_data.FilesWritten.FilePath`, `event_data.DnsRequests.InterfaceIndex`, `event_data.DnsRequests.LoadTime`, `event_data.DnsRequests.DomainName`, `event_data.DnsRequests.RequestType`, `event_data.PatternDispositionFlags.Detect`, `event_data.PatternDispositionFlags.Indicator`, `event_data.PatternDispositionFlags.InddetMask`, `event_data.PatternDispositionFlags.SensorOnly`, `event_data.PatternDispositionFlags.Rooting`, `event_data.PatternDispositionFlags.KillSubProcess`, `event_data.PatternDispositionFlags.ProcessBlocked`, `event_data.PatternDispositionFlags.RegistryOperationBlocked`, `event_data.PatternDispositionFlags.CriticalProcessDisabled`, `event_data.PatternDispositionFlags.BootupSafeguardEnabled`, `event_data.PatternDispositionFlags.FsOperationBlocked`, `event_data.PatternDispositionFlags.HandleOperationDowngraded`, `event_data.PatternDispositionFlags.KillActionFailed`, `event_data.PatternDispositionFlags.BlockingUnsupportedOrDisabled`, `event_data.PatternDispositionFlags.ContainmentFileSystem`, `event_data.ProcessStartTime`, `event_data.ProcessEndTime`, `event_data.GrandParentImageFileName`, `event_data.GrandParentCommandLine`, `event_data.AggregateId`, `event_data.GrandParentImageFilePath`, `event_data.PlatformId`, `event_data.CloudIndicator` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Updated the replace mutation for `event.idm.read_only_udm.target.file.sha256` to use `%{event_data.IOCValue}` for correct variable interpolation.   
2025-11-27 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `event_data_simpleName` raw log field with event.idm.read_only_udm.metadata.product_event_type UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `ComputerName` raw log field with event.idm.read_only_udm.principal.hostname UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ComputerName` raw log field with event.idm.read_only_udm.principal.asset.hostname UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `LocalAddressIP4`, `aip` raw log field with event.idm.read_only_udm.principal.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `LocalAddressIP4`, `aip` raw log field with event.idm.read_only_udm.principal.asset.ip UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `aid` raw log field with event.idm.read_only_udm.principal.asset.asset_id UDM field.  
\- event.idm.read_only_udm.target.file.full_path: Newly mapped `TargetFileName` raw log field with event.idm.read_only_udm.target.file.full_path UDM field.  
\- event.idm.read_only_udm.principal.platform: Newly mapped `event_data_platform` raw log field with event.idm.read_only_udm.principal.platform UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `id` raw log field with event.idm.read_only_udm.metadata.product_log_id UDM field.  
\- event.idm.read_only_udm.metadata.product_deployment_id: Newly mapped `cid` raw log field with event.idm.read_only_udm.metadata.product_deployment_id UDM field.  
\- event.idm.read_only_udm.target.file.size: Newly mapped `Size` raw log field with event.idm.read_only_udm.target.file.size UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `name` raw log field with event.idm.read_only_udm.metadata.description UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `ExtendedAttributeName`, `ConfigStateHash`, `ContextProcessId`, `ExtendedAttributeStatus`, `ExtendedAttributeValueReadable`, `FileIdentifier`, `ConfigBuild`, `ExtendedAttributeModificationType`, `Entitlements`, `EventOrigin`, `VnodeType`, `EffectiveTransmissionClass` raw log fields with event.idm.read_only_udm.additional.fields UDM field.   
2025-10-02 |  Enhancement:  
\- Newly added for loop for `event_data.MitreAttack` raw log field to handle multiple values.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `event_data.ComputerName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `event_data.SensorId` raw log field with `event.idm.read_only_udm.principal.asset_id` and `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `event_data.MobileDetectionId`, `event_data.ContextTimeStamp` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_data.TacticId`, `value.TacticID`, `value.TechniqueID`, `value.FingerPrint`, `value.Name`, `value.PatternID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.tls.server.certificate.issuer`: Newly mapped `value.Issuer` raw log field with `event.idm.read_only_udm.network.tls.server.certificate.issuer` UDM field.   
2025-08-08 |  Enhancement:  
\- event.idm.read_only_udm.principal.hostname and event.idm.read_only_udm.principal.asset.hostname: Newly mapped `endpointName` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- event.idm.read_only_udm.principal.ip and event.idm.read_only_udm.principal.asset.ip: Newly mapped `ClientIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- event.idm.read_only_udm.metadata.event_type: Setting `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `has_principal` is `true`.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `endpointName` from `event.idm.read_only_udm.security_result.detection_fields` UDM fields.   
2025-07-28 |  Enhancement:  
\- event.idm.read_only_udm.metadata.vendor_name: Newly mapped a default value `CrowdStrike` when vendor is empty.  
\- event.idm.read_only_udm.metadata.product_name: Newly mapped a default value `FalconHost` when product is empty.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `event_data.HostnameField` raw log field to `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `event_data.HostnameField` raw log field to `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `event_data.SessionId` raw log field to `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly mapped `event_data.AgentIdString` raw log field to `event.idm.read_only_udm.principal.asset.asset_id` UDM field with a prefix `Asset_ID: `.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `url` raw log field to `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `event_data.Attributes.status_code` raw log field to `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `event_data.Attributes.request_method` raw log field to `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly mapped `event_data.Attributes.user_agent` raw log field to `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.target.application: Newly mapped `event_data.Source` raw log field to `event.idm.read_only_udm.target.application` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `meta.version` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Mapped `meta.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field  
\- event.idm.read_only_udm.target.url: Newly mapped `event_data.Attributes.request_path` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.metadata.event_type: If event_type is STATUS_UPDATE and has_principal == `true` and event_data.Attributes.scopes =~ `read`, updated to USER_RESOURCE_ACCESS.  
\- Added a drop filter TAG_MALFORMED_MESSAGE for logs that are neither valid JSON nor match the LEEF grok pattern.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `objective` and `outcome` raw log field(s) with event.idm.read_only_udm.security_result.detection_fields UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `EndTimestamp`, `event_data.UTCTimestamp` and `event_data.Commands` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Removed redundant mapping of `event.idm.read_only_udm.additional.fields` and `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-07-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `event_data.PlatformName` raw log field to `event.idm.read_only_udm.principal.platform`.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `event_data.PatternDispositionDescription` raw log field to `event.idm.read_only_udm.security_result.description`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event_data.PatternDispositionFlags.QuarantineFile` raw log field to `event.idm.read_only_udm.security_result.action` when `event_data.PatternDispositionFlags.QuarantineFile` is `true`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `event_data.PatternDispositionValue`,`event_data.PatternDispositionFlags.SuspendProcess` , and `event_data.PatternDispositionFlags.KillProcess` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Corrected the mapping of event_data.PatternId to the event.idm.read_only_udm.security_result.detection_fields UDM field to handle cases where it has a string value.   
2025-07-03 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `SCAN_FILE` when `has_principal` is `true` and `has_target_file` is `true`.  
\- `event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `SCAN_UNCATEGORIZED` when `has_principal` is `false` and `description` raw log field is not related to user.   
2025-03-12 |  Enhancement:  
\- Removed the mapping of `deviceId` from `principal.asset.asset_id`.  
\- Added the mapping of `deviceId` to `additional.fields`.  
\- Mapped `connectionDirection` to `additional.fields`.   
2025-02-14 |  Enhancement:  
\- Mapped `md5` to `target.process.file.md5`.  
\- Mapped `ipv4Addresses` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `domainNames` to `additional.fields.value.list_value.values`.  
\- Mapped `exeWrittenFilePath` to `principal.process.file.full_path`.  
\- Mapped `sev` to `security_result.severity`.  
\- Mapped `exeWrittenFileName` and `fileName` to `target.file.names`.  
\- Mapped `patternDisposition` and `objective` to `security_result.detection_fields`.   
2025-02-12 |  Enhancement:  
\- If `event_data.SeverityName` is between 0 and 19 (inclusive), then `security_result.severity` is mapped to `INFORMATIONAL`.  
\- If `event_data.SeverityName` is between 20 and 39 (inclusive), then `security_result.severity` is mapped to `LOW`.  
\- If `event_data.SeverityName` is between 40 and 59 (inclusive), then `security_result.severity` is mapped to `MEDIUM`.  
\- If `event_data.SeverityName` is between 60 and 79 (inclusive), then `security_result.severity` is mapped to `HIGH`.  
\- If `event_data.SeverityName` is between 80 and 99 (inclusive), then `security_result.severity` is mapped to `CRITICAL`.   
2025-02-10 |  Bug-fix:  
\- Added Grok patterns to parse `event_data.IOCValue`.  
\- Mapped `NetworkAccesse.LocalAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `NetworkAccesse.LocalPort` to `principal.port`.  
\- Mapped `NetworkAccesse.ConnectionDirection` to `network.direction`.  
\- Mapped `NetworkAccesse.Protocol` to `network.ip_protocol`.  
\- Mapped `NetworkAccesse.RemoteAddress` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `NetworkAccesse.RemotePort` to `target.port`.  
\- Mapped `NetworkAccesse.AccessType` to `additional.fields`.  
\- Mapped `NetworkAccesse.IsIPV6` to `security_result.detection_fields`.  
\- Mapped `NetworkAccesse.AccessTimestamp` to `security_result.detection_fields`.   
2025-02-02 |  Enhancement:  
\- Added support for LEEF logs.   
2025-01-28 |  Enhancement:  
\- Added support to map `eventData.severityName` only if it is not empty.   
2025-01-10 |  Enhancement:  
\- When `OperationBlocked` is `true`, mapped `security_result.action` to `BLOCK`.  
\- When `OperationBlocked` is `false`, mapped `security_result.action` to `ALLOW`.  
\- When `event_type` is `IdentityProtectionEvent`, then mapped `event_data.IncidentDescription` to `security_result.summary`.  
\- When `event_type` is `IdentityProtectionEvent`, then mapped `event_data.SeverityName` to `security_result.severity`.   
2025-01-09 |  Enhancement:  
\- Mapped `event_data.Technique` to `security_result.rule_name`.  
\- Mapped `event_data.CommandLine` to `target.process.command_line`.  
\- If `event_data.IOCType` is `ipv4`, then mapped `event_data.IOCValue` to `target.ip` and `target.asset.ip`.  
\- If `event_data.IOCType` is `hash_sha256`, then mapped `event_data.IOCValue` to `target.file.sha256`.   
2024-12-12 |  Enhancement:  
\- Mapped `event.SeverityName` to `security_result.severity`.  
\- Mapped `event.Description` to `security_result.summary`.  
\- Mapped `security_result.action` based on `event.PatternDispositionFlags.OperationBlocked`.   
2024-10-29 |  Enhancement:  
\- Added support for JSON format of logs.  
\- Mapped `request` to `network.http.referral_url`.  
\- Mapped `networkDetectionType` to `security_result.detection_fields`.   
2022-07-18 |  Enhancement:  
\- Added following mapping for the LEEF format logs:  
\- The field `version` mapped to `metadata.product_version`.  
\- The field `usrName` and `userName` to `principal.user.email_addresses` if it is an email else mapped to `principal.user.userid`.  
\- The field `severityName` mapped to `security_result.severity`.  
\- The field `cat` mapped to `security_result.category_details`.  
\- The field `incidentType` mapped to `security_result.summary`.  
\- The field `falconHostLink` mapped to `security_result.about.url`.  
\- The field `numberOfCompromisedEntities` mapped to `security_result.detection_fields[n]`.  
\- The field `identityProtectionIncidentId` mapped to `security_result.detection_fields[n]`.  
\- The field `numbersOfAlerts` mapped to `security_result.detection_fields[n]`.  
\- The field `state` mapped to `security_result.detection_fields[n]`.  
\- Added following mapping for the CEF format logs:  
\- The field `version` mapped to `metadata.product_version`.  
\- The field `deviceCustomDate1` mapped to `metadata.event_type`.  
\- The field `msg` mapped to `metadata.description`.  
\- The field `cs1` mapped to `security_result.summary` if the value of `cs1Label` is `incidentType` else mapped to `security_result.detection_fields[n]`.  
\- The field `cs2` mapped to `security_result.detection_fields[n]`.  
\- The field `cs3` mapped to `security_result.detection_fields[n]`.  
\- The field `cs1` mapped to `security_result.about.url` if the value of `cs4Label` is `falconHostLink` else mapped to `security_result.detection_fields[n]`.  
\- The field `cn1` mapped to `security_result.detection_fields[n]`.  
\- The field `cn2` mapped to `security_result.detection_fields[n]`.  
\- The field `cn3` mapped to `security_result.detection_fields[n]`.  
\- The field `duser` to `principal.user.email_addresses` if it is an email else mapped to `principal.user.userid`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
