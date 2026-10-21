---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-casb-changelog/
title: Change log for PAN_CASB \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:36:22.742307+00:00
---

# Change log for PAN_CASB  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/pan-casb-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for PAN_CASB

Date | Changes  
---|---  
2026-05-29 |  Enhancement:  
\- Added a Grok pattern to parse the new format of SYSLOG logs.  
\- `event.idm.read_only_udm.metadata.collected_timestamp:` Newly mapped `TimeReceived` raw log field with `event.idm.read_only_udm.metadata.collected_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp:` Newly mapped `TimeGenerated` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.network.http.method:` Newly mapped `HTTPMethod` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id:` Newly mapped `SequenceNo` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.additional.fields:` Newly mapped `URLCounter`, `ParentStarttime`, `InlineMLVerdict`, `SigFlags`, `PacketID`, `IMSI`, `ParentSessionID`, `ContentVersion` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-04-08 |  Enhancement:  
\- Added support for new format of GlobalProtect event type logs.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `event.idm.read_only_udm.security_result.action` UDM field to `ALLOW` when `column28` is `success`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `column6`, `column7`, `column9`, `column10`, `column13`, `column21`, `column24`, `column27`, `column31`, `column32`, `column33`, `column34`, `column35`, `column36`, `column37`, `column38`, `column39`, `column41`, `column42`, `column43` and `column44` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `column3` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `column8` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `column5` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.network.session_duration.seconds`: Newly mapped `column30` raw log field with `event.idm.read_only_udm.network.session_duration.seconds` UDM field.  
\- `event.idm.read_only_udm.network.tls.next_protocol`: Newly mapped `column11` raw log field with `event.idm.read_only_udm.network.tls.next_protocol` UDM field.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `column46` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM field.  
\- `event.idm.read_only_udm.observer.resource.name`: Newly mapped `column45` raw log field with `event.idm.read_only_udm.observer.resource.name` UDM field.  
\- `event.idm.read_only_udm.observer.resource.product_object_id`: Newly mapped `column47` raw log field with `event.idm.read_only_udm.observer.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.asset_id`: Newly mapped `column19` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM field.  
\- `event.idm.read_only_udm.principal.asset.hardware.serial_number`: Newly mapped `column20` raw log field with `event.idm.read_only_udm.principal.asset.hardware.serial_number` UDM field.  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped `column14` raw log field with `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `column15`, `column16`, `column17`, `column18` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `column13` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.platform`: Newly mapped `column22` raw log field with `event.idm.read_only_udm.principal.platform` UDM field.  
\- `event.idm.read_only_udm.principal.platform_version`: Newly mapped `column23` raw log field with `event.idm.read_only_udm.principal.platform_version` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `column4` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.principal.user.product_object_id`: Newly mapped `column2` raw log field with `event.idm.read_only_udm.principal.user.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `column12` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `column25` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `column26` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `column40` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `column29` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.   
2025-07-09 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `VirtualSystemID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ApplicationTechnology` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `LogType`-`Subtype` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM Field .  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Subtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field when `Subtype` is null.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `action_value` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM Field.  
\- event.idm.read_only_udm.security_result.threat_name: Newly Mapped `ThreatNameFirewall` raw log field with `event.idm.read_only_udm.security_result.threat_name` UDM Field.  
\- event.idm.read_only_udm.network.session_id: Newly Mapped `SessionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM Field.  
\- event.idm.read_only_udm.principal.hostname: Newly Mapped `DeviceName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM Field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly Mapped `DeviceName` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM Field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly Mapped `Location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM Field.  
\- event.idm.read_only_udm.target.application: Newly Mapped `TunneledApplication` raw log field with `event.idm.read_only_udm.target.application` UDM Field.  
\- event.idm.read_only_udm.target.url: Newly Mapped `URLDomain` raw log field with `event.idm.read_only_udm.target.url` UDM Field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `SourceUserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Changed the key name from `ThreatCategory` to `thr_category` for raw log field `ThreatCategory`.   
2025-07-07 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action: Newly Mapped `action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- Set `action` to `ALLOW` when column28 is `allow`, `alert`, `override`.  
\- Set `action` to `BLOCK` when column28 is `drop-packet`, `drop`, `deny`, `drop ICMP`, `block`, `block-url`, `block-ip`, `block-continue`, `block-override`, `override-lockout`, `random-drop`, `sinkhole`.  
\- Set `action` to `FAIL` when column28 is `reset-client`, `reset-server`, `reset-both`.  
\- event.idm.read_only_udm.principal.location.country_or_region: Newly Mapped `column35` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM Field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly Mapped `column61` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM Field.  
\- event.idm.read_only_udm.security_result.category_details: Newly Mapped `column94`, `column97` and `column98` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM Field.  
\- event.idm.read_only_udm.event1.idm.read_only_udm.network.session_id: Newly Mapped `column21` raw log field with `event.idm.read_only_udm.event1.idm.read_only_udm.network.session_id` UDM Field.   
2025-06-13 |  Enhancement:  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `ThreatCategory` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `LogType`-`SubType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM Field and ,when `SubType` is null added the `SubType` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.file.names: Newly Mapped `FileName` raw log field with `event.idm.read_only_udm.principal.file.names` UDM Field.  
\- event.idm.read_only_udm.principal.file.mime_type: Newly Mapped `FileType` raw log field with `event.idm.read_only_udm.principal.file.mime_type` UDM Field   
2025-05-22 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `LogType` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.   
2025-04-19 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly Mapped HTTP2Connection raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `LogSetting` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `InboundInterface` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `OutboundInterface` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Application` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `VirtualLocation` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `CaptivePortal` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Subtype` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `URLCategoryList` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `SessionID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `RepeatCount` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ConfigVersion` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `URLCategory` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `DirectionOfAttack` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `SequenceNo` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `PacketID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `DestinationAddress` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `VirtualSystemName` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `IMSI` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ParentSessionID` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Tunnel` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ApplicationRisk` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ContentVersion` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `TimeGeneratedHighResolution` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `ApplicationCategory` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `ApplicationSubcategory` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `LogType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `SourceLocation` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `CloudHostname` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `CortexDataLakeTenantID` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `FlowType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `InboundInterfaceDetailsType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `LogSource` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `OutboundInterfaceDetailsType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `PanoramaSN` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `PlatformType` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `Action` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `DGHierarchyLevel1` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `DGHierarchyLevel2` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `DGHierarchyLevel3` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `DGHierarchyLevel4` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.security_result.severity: Newly Mapped `Severity` raw log field with `event.idm.read_only_udm.security_result.severity` UDM Field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly Mapped `RuleUUID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM Field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly Mapped `Rule` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM Field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly Mapped `Protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM Field.  
\- event.idm.read_only_udm.target.location.name: Newly Mapped `ToZone` raw log field with `event.idm.read_only_udm.target.location.name` UDM Field.  
\- event.idm.read_only_udm.principal.ip : Newly Mapped `SourceAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `SourceAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM Field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `DestinationAddress` raw log field with `event.idm.read_only_udm.target.ip` UDM Field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `DestinationAddress` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM Field.  
\- event.idm.read_only_udm.principal.nat_ip: Newly Mapped `NATSource` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM Field.  
\- event.idm.read_only_udm.target.nat_ip: Newly Mapped `NATDestination` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM Field.  
\- event.idm.read_only_udm.principal.user.userid : Newly Mapped `SourceUser` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- event.idm.read_only_udm.target.user.userid: Newly Mapped `DestinationUser` raw log field with `event.idm.read_only_udm.target.user.userid` UDM Field.  
\- event.idm.read_only_udm.principal.port : Newly Mapped `SourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM Field.  
\- event.idm.read_only_udm.target.port: Newly Mapped `DestinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM Field.  
\- event.idm.read_only_udm.principal.nat_port: Newly Mapped `NATSourcePort` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM Field.  
\- event.idm.read_only_udm.target.nat_port: Newly Mapped `NATDestinationPort` raw log field with `event.idm.read_only_udm.target.nat_port` UDM Field.  
\- event.idm.read_only_udm.target.url: Newly Mapped `URL` raw log field with `event.idm.read_only_udm.target.url` UDM Field.  
\- event.idm.read_only_udm.principal.asset.asset_id: Newly Mapped `DeviceSN` raw log field with `event.idm.read_only_udm.principal.asset.asset_id` UDM Field.  
\- event.idm.read_only_udm.principal.location.name: Newly Mapped `FromZone` raw log field with `event.idm.read_only_udm.principal.location.name` UDM Field.  
\- event.idm.read_only_udm.target.location.country_or_region: Newly Mapped `DestinationLocation` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM Field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `X-Forwarded-For` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- event.idm.read_only_udm.principal.hostname: Newly Mapped `DeviceName` raw log field with `event.idm.read_only_udm.principal.hostname` UDM Field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly Mapped `DeviceName` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM Field.  
\- event.idm.read_only_udm.target.location.country_or_region : Newly Mapped `Location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM Field.  
\- event.idm.read_only_udm.principal.administrative_domain: Newly Mapped `SourceUserDomain` raw log field with `event.idm.read_only_udm.principal.administrative_domain` UDM Field.  
\- event.idm.read_only_udm.principal.user.userid: Newly Mapped `SourceUserName` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM Field.  
\- event.idm.read_only_udm.target.application: Newly Mapped `TunneledApplication` raw log field with `event.idm.read_only_udm.target.application` UDM Field.  
\- event.idm.read_only_udm.target.url : Newly Mapped `URLDomain` raw log field with `event.idm.read_only_udm.target.url` UDM Field.  
\- event.idm.read_only_udm.metadata.vendor_name: Newly Mapped `VendorName` raw log field with `event.idm.read_only_udm.metadata.vendor_name` UDM Field.   
2025-02-19 |  Enhancement:  
\- Added support to parse new format of logs.   
2025-02-06 |  Enhancement:  
\- Added support to parse LEEF format of logs.   
2024-12-10 |  Enhancement:  
\- Added support to parse SYSLOG+CSV format of logs.   
2022-11-25 |  -Fix Added to support for logs having multiple events.Used Disambiguation_Key  
Mapped alertId to idm.read_only_udm.metadata.product_log_id  
Mapped event_type  
Mapped vendor_name  
Mapped Product_event_type  
Mapped description and ur_back_to_product  
Mapped accountId to target.hostname  
Mapped region to target.location.country_or_region  
Mapped resourceName to target.resource.name,resourceId to target.resource.product_object_id,target.resource.attribute,target.resource.attribute.cloud  
Mapped target.resource.attribute.cloud.environment,accountname to target.resource.attribute.cloud.environment.project.id  
Mapped target.resource.attribute.labels.  
Mapped security_result.rule_id,security_result.rule_name,security_result.detection_fields  
Mapped security_result.description  
Mapped groupId to target.user  
Mapped privateIpaddress to target.ip and macAddress to target.mac   
2022-10-07 |  Newly Created Parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
