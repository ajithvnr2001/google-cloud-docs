---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arcsight-cef-changelog/
title: Change log for ARCSIGHT_CEF \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:34:40.892331+00:00
---

# Change log for ARCSIGHT_CEF  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/arcsight-cef-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for ARCSIGHT_CEF

Date | Changes  
---|---  
2026-07-23 |  Enhancement:  
\- Modified a grok pattern to parse the raw log fields properly.  
\- `event.idm.read_only_udm.network.http.referral_url`: Newly mapped `PanOSReferer` raw log field with `event.idm.read_only_udm.network.http.referral_url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `fileId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-02-24 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.action`:  
\- If `act` contains `succ` or `act` is `allow`, Set the value of `event.idm.read_only_udm.security_result.action` to `ALLOW`.  
\- If `act` contains `block`, Set the value of `event.idm.read_only_udm.security_result.action` to `BLOCK`.  
\- If `act` contains `fail`, Set the value of `event.idm.read_only_udm.security_result.action` to `FAIL`.  
\- `event.idm.read_only_udm.observer.hostname`: Newly mapped `PanOSApplianceOrCloud` raw log field to `event.idm.read_only_udm.observer.hostname` UDM field.  
\- `event.idm.read_only_udm.target.file.mime_type`: Newly mapped `PanOSFileType` raw log field with `event.idm.read_only_udm.target.file.mime_type` UDM field.  
\- `event.idm.read_only_udm.network.email.from`: If `PanOSSenderEmail` is a valid email address, Set the value of `PanOSSenderEmail` to `event.idm.read_only_udm.network.email.from` UDM field.  
\- `event.idm.read_only_udm.network.email.subject`: Newly mapped `PanOSEmailSubject` raw log field with `event.idm.read_only_udm.network.email.subject` UDM field.  
\- `event.idm.read_only_udm.network.email.to`: If `PanOSRecipientEmail` is a valid email address, Set the value of `PanOSRecipientEmail` to `event.idm.read_only_udm.network.email.to` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `PanOSNSSAINetworkSliceType` (key: `PanOSNSSAINetworkSliceType`), `PanOSURLCounter` (key: `PanOSURLCounter`), `PanOSReportID` (key: `PanOSReportID`), `PanOSDGHierarchyLevel2` (key: `PanOSDGHierarchyLevel2`), `PanOSVirtualSystemName` (key: `PanOSVirtualSystemName`), `PanOSSigFlags` (key: `PanOSSigFlags`), `PanOSPartialHash` (key: `PanOSPartialHash`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added grok patterns to fix incorrectly parsing fields.   
2026-01-19 |  Enhancement:  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `PanOSPacketsSent` raw log field to `event.idm.read_only_udm.network.sent_packets`.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `PanOSPacketsReceived` raw log field to `event.idm.read_only_udm.network.received_packets`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `PanOSTimeGeneratedHighResolution`, `PanOSLinkChangeCount`, `PanOSHTTP2Connection`, `PanOSChunksReceived`, `PanOSChunksSent`, `PanOSChunksTotal`, `PanOSEndpointAssociationID`, `PanOSTunnel`, `PanOSParentStarttime`, `PanOSParentSessionID`, `PanOSIMEI`, `PanOSIMSI`, `PanOSDestinationUUID`, `PanOSSourceUUID`, `PanOSDGHierarchyLevel4`, `PanOSDGHierarchyLevel3`, `PanOSSourceLocation`, `externalId`, `PanOSSessionStartTime`, `PanOSBytes`, `cnt`, `start` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- Modified handling of the `cs2` field. When the raw `cs2` field value contains `Allow`, this value is now mapped into `event.idm.read_only_udm.additional.fields`, using the value of `cs2Label` as the key. The standard mapping of `cs2` to `event.idm.read_only_udm.additional.fields` (with key `cs2Label`) is skipped in this specific `Allow` case. To avoid mapping incorrect `event.idm.read_only_udm.security_result.action`.   
2026-01-13 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.type`: Removed mapping of resource_1 and resource_2 raw log fields from `event.idm.read_only_udm.principal.resource.type`. As it is an application not resource.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `resource_1` \+ `resource_2` raw log fields to `event.idm.read_only_udm.principal.application`.   
2025-12-17 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.type`: Newly mapped resource_1 + resource_2 raw log field to `event.idm.read_only_udm.principal.resource.type`.  
\- `event.idm.read_only_udm.principal.hostname`: Newly mapped src_host raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- `event.idm.read_only_udm.principal.asset.hostname`: Newly mapped src_host raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped src_ip raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.principal.asset.ip`: Newly mapped src_ip raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- Added a new grok pattern to parse CEF logs where the event name field contains pipe symbols.   
2025-12-02 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip`: Newly mapped `src` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- `event.idm.read_only_udm.target.ip`: Newly mapped `dst` raw log field to `event.idm.read_only_udm.target.ip`.   
2025-11-27 |  Enhancement:  
\- Added support for JSON wrapped CEF format, typically from Cribl.  
\- Enhanced parser to detect JSON messages containing `cribl_pipe` and `CEF`.  
\- The CEF message is now extracted from the `cribl.message` field within the JSON for further processing.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `catdt`, `cribl.cribl_pipe` ,`cribl.ecs.version` ,`cribl.agent.vf_ingestion.name` ,`cribl.agent.vf_ingestion.hostname` ,`cribl.agent.vf_ingestion.environment` ,`cribl.agent.vf_ingestion.type` ,`cribl.organization.name` ,`cribl.organization.id` ,`cribl.kafka_source` and `cribl.kafkaTopic` to `event.idm.read_only_udm.additional.fields`  
2025-11-20 |  Enhancement:  
\- Updated logic to remove `event.idm.read_only_udm.principal.ip` when `shost` is not a standalone IP address.  
\- Updated logic to remove `event.idm.read_only_udm.principal.asset.ip` when `shost` is not a standalone IP address.   
2025-11-12 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.event_type`: Updated to STATUS_UPDATE if a principal MAC address (amac) is present, otherwise defaults to GENERIC_EVENT.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `version` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.principal.hostname`: The value from the `shost` raw log field is now truncated to 255 characters if its length is greater than or equal to 255.   
2025-11-05 |  Enhancement:  
\- Enhanced `shost` parsing: Modified logic to map shost field correctly.  
\- Enhanced `dhost` parsing: Added logic to extract IP addresses from `dhost` when it is a valid IP address.  
\- event.idm.read_only_udm.observer.application: Newly mapped `at` raw log field to `event.idm.read_only_udm.observer.application`.  
\- event.idm.read_only_udm.observer.ip: Newly mapped `agt` raw log field to `event.idm.read_only_udm.observer.ip`.  
\- event.idm.read_only_udm.observer.hostname: Newly mapped `ahost` raw log field to `event.idm.read_only_udm.observer.hostname`.  
\- event.idm.read_only_udm.about.file.mime_type: Newly mapped `fileType` raw log field to `event.idm.read_only_udm.about.file.mime_type`.  
\- event.idm.read_only_udm.principal.location.region_longitude: Newly mapped `slong` raw log field to `event.idm.read_only_udm.principal.location.region_longitude`.  
\- event.idm.read_only_udm.principal.location.region_latitude: Newly mapped `slat` raw log field to `event.idm.read_only_udm.principal.location.region_latitude`.  
\- event.idm.read_only_udm.security_result.priority_details: Newly mapped `priority` raw log field to `event.idm.read_only_udm.security_result.priority_details`.  
\- event.idm.read_only_udm.security_result.attack_details.techniques: Newly mapped `categoryTechnique` raw log field to `event.idm.read_only_udm.security_result.attack_details.techniques`.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `sessionId` raw log field to `event.idm.read_only_udm.network.session_id`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `eventAnnotationModificationTime`, `eventAnnotationAuditTrail`, `eventAnnotationVersion`, `eventAnnotationFlags`, `eventAnnotationEndTime`, `eventAnnotationManagerReceiptTime`, `type`, `end`, `mrt`, `generatorID`, `cryptoSignature`, `customerID`, `customerURI`, `modelConfidence`, `relevance`, `assetCriticality`, `ruleThreadId`, `locality`, `atz`, `deviceZoneID`, `deviceZoneURI`, `dtz`, `deviceFacility`, `eventAnnotationStageUpdateTime`, `_cefVer`, `arcSightEventPath`, `baseEventIds` and `av` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-10-27 |  Enhancement:  
\- Added support for NON-CEF json logs.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `client_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `ident` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `ident` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.principal.user.userid: Newly mapped `auth` raw log field to `event.idm.read_only_udm.principal.user.userid`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `timestamp` raw log field to `event.idm.read_only_udm.metadata.event_timestamp`.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `http_method` raw log field to `event.idm.read_only_udm.network.http.method`.  
\- event.idm.read_only_udm.network.http.referral_url: Newly mapped `http_uri` raw log field to `event.idm.read_only_udm.network.http.referral_url`.  
\- event.idm.read_only_udm.network.http.response_code: Newly mapped `http_status_code` raw log field to `event.idm.read_only_udm.network.http.response_code`.  
\- event.idm.read_only_udm.network.received_bytes: Newly mapped `response_bytes` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- event.idm.read_only_udm.intermediary: Newly mapped `host` raw log field to `event.idm.read_only_udm.intermediary`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `sourcetype`, `source` and `cribl_test` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `source_ip` raw log field to `event.idm.read_only_udm.principal.ip`.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `source_ip` raw log field to `event.idm.read_only_udm.principal.asset.ip`.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `source_host` raw log field to `event.idm.read_only_udm.principal.hostname`.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `source_host` raw log field to `event.idm.read_only_udm.principal.asset.hostname`.  
\- event.idm.read_only_udm.target.hostname: Newly mapped `destination_host` raw log field to `event.idm.read_only_udm.target.hostname`.  
\- event.idm.read_only_udm.target.asset.hostname: Newly mapped `destination_host` raw log field to `event.idm.read_only_udm.target.asset.hostname`.  
\- Added grok patterns to extract `source_ip` and `source_host` from the `shost` field for CEF logs.  
\- Added grok pattern to extract `destination_host` from the `dhost` field for CEF logs.  
\- Added grok patterns to extract `intermediary_hostname` from the `temp_data` field for CEF logs.   
2025-08-04 |  Enhancement:  
\- event.idm.read_only_udm.about.ip: Removed mapping of `dvc` from `event.idm.read_only_udm.about.ip` UDM field as the `dvc` field represents an intermediary system, not a system the event is directly about.  
\- event.idm.read_only_udm.intermediary.ip: Newly mapped `dvc`log fields with `event.idm.read_only_udm.intermediary.ip` UDM field.  
\- event.idm.read_only_udm.about.hostname: Removed mapping of `dvchost` from `event.idm.read_only_udm.about.hostname` UDM field as `dvchost` value in the raw logs represents an intermediary system communicating with the host and not the actual about.  
\- event.idm.read_only_udm.intermediary.hostname: Newly mapped `dvchost` log fields with `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `amac` raw log field to `event.idm.read_only_udm.principal.mac`using regex validation `^(([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2})$` Invalid values are captured in `event.idm.read_only_udm.additional.fields` with the key `amac` to prevent data loss.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `geid` raw log field to `event.idm.read_only_udm.metadata.product_log_id`.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `aid` and `art` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `categorySignificance`, `categoryBehavior`, `categoryObject`, and `deviceSeverity` raw log fields to `event.idm.read_only_udm.security_result.detection_fields`.  
\- event.idm.read_only_udm.security_result.outcomes: Newly mapped `categoryOutcome` raw log field to `event.idm.read_only_udm.security_result.outcomes`.  
\- Added a grok pattern to handle negative integer values and mapped `in` raw log field to `event.idm.read_only_udm.network.received_bytes`.  
\- Added a grok pattern to handle negative integer values and mapped `out` raw log field to `event.idm.read_only_udm.network.sent_bytes`.   
2025-06-05 |  Enhancement:  
\- Added support to remove unnecessary brackets from `event.idm.read_only_udm.metadata.product_event_type`.   
2025-03-11 |  Enhancement:  
\- Mapped `cn3` to `network.duration.seconds`.  
\- Mapped `PanOSTenantID` to `additional.fields`.  
\- Added support for `User Login` events.   
2025-01-31 |  Enhancement:  
\- Mapped `cn3` to `additional.fields`.  
\- Mapped `PanOSCortexDataLakeTenantID` to `additional.fields`.   
2025-01-17 |  Enhancement:  
\- Mapped `target_user` to `target.user.userid`.  
\- Mapped `principal_ip` to `principal.ip`.  
\- Mapped `PanOSStage`, `PanOSConnectionError`, and `PanOSEventDetails` to `additional.fields`.  
\- Mapped `outcome` to `security_result.action_details`.   
2024-12-12 |  Enhancement:  
\- Mapped `Name` to `additional.fields`.  
\- Mapped `PanOSDescription` to `metadata.description`.  
\- Mapped `PanOSSourceUser` to `principal.user.userid`.  
\- Mapped `outcome` to `security_result.action_details`.  
\- If `outcome` equals `success`, mapped `security_result.action` to `ALLOW`.   
2024-07-30 |  Enhancement:  
\- Mapped `app` to `target.application`.  
\- Mapped `flexString2`, `PanOSFileHash`, and `filePath` to `additional.fields`.  
\- Mapped `threat_name` to `security_result.threat_name`.  
\- Mapped `threat_id` to `security_result.threat_id`.  
\- When `device_event_class_id` is not `THREAT`, then mapped `cat` to `additional.fields`.   
2024-06-18 |  Enhancement:  
\- Added support to parse unparsed logs failing due to validation error.   
2024-04-03 |  Enhancement:  
\- Mapped `principal_ip1` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `deviceExternalId` to `about.asset.hardware.serial_number`.  
\- When principal data and target data is present, then set `metadata.event_type` to `NETWORK_CONNECTION`.  
\- When principal data and target resource data is present, then set `metadata.event_type` to `USER_RESOURCE_ACCESS`.  
\- When principal data is present, then set `metadata.event_type` to `STATUS_UPDATE`.   
2024-02-18 |  Enhancement -  
\- Added support to parse `PAN_FIREWALL` logs.  
\- Mapped `metadata.event_type` to `NETWORK_CONNECTION` if `device_event_class_id` is in `TRAFFIC`, `THREAT`, `URL`, `WILDFIRE`, `DATA`, `TUNNEL`.  
\- Mapped `PanOSConfigVersion` to `security_result.detection_fields`.  
\- Mapped `deviceOutboundInterface`, `deviceInboundInterface` to `additional.fields`.   
2024-02-12 |  Enhancement -  
\- Mapped `query` to `additional fields`.  
\- Added a Grok pattern to parse logs with query value `json_data`.   
2023-04-27 |  Enhancement -  
\- Mapped `proto` to `network.ip_protocol`.   
2022-11-15 |  Enhancement -  
\- Mapped `PanOSThreatCategory` to `security_result.category_details`.  
\- Mapped `PanOSThreatID` to `security_result.threat_id`,  
\- Mapped `PanOSContentVersion` to `security_result.detection_fields`.  
\- Mapped `PanOSRuleUUID` to `metadata.product_log_id`.  
\- Mapped `PanOSDestinationLocation` to `target.location.country_or_region`.  
\- Mapped `PanOSDGHierarchyLevel1` to `security_result.detection_fields`.   
2022-08-26 |  Enhancement - Migrated the custom parsers into default parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
