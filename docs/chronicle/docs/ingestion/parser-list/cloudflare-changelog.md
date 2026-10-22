---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-changelog/
title: Change log for CLOUDFLARE \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:26:56.199380+00:00
---

# Change log for CLOUDFLARE  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/cloudflare-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for CLOUDFLARE

Date | Changes  
---|---  
2026-08-14 |  Enhancement:  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `clientIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `rayName` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `clientCountryName` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `clientRequestPath` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Newly mapped `clientRequestHTTPHost` raw log field with `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.network.http.method`: Newly mapped `clientRequestHTTPMethodName` raw log field with `event.idm.read_only_udm.network.http.method` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol_version`: Newly mapped `version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `originatorRayName`, `ClientRefererScheme`, `edgeColoName`, `ref` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `botScoreSrcName`, `botScore` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: If `client_request_http_protocol` is `HTTP`, updated the value of `event.idm.read_only_udm.network.application_protocol` to `HTTP`.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `kind` raw log field with `event.idm.read_only_udm.principal.application` UDM field.   
2026-08-01 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `BotScore`, `WAFFlags`, `WAFRCEAttackScore`, `WAFSQLiAttackScore`, `WAFXSSAttackScore` from `event.idm.read_only_udm.additional.fields` UDM field to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `BotScore`, `WAFFlags`, `WAFRCEAttackScore`, `WAFSQLiAttackScore`, `WAFXSSAttackScore` raw log field to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `EdgeRequestHost` raw log field to `event.idm.read_only_udm.intermediary.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `EdgeEndTimestamp` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Updated conditional checks for `ClientTLSCipher`, `ClientSSLCipher`, and `ClientSSLProtocol` to exclude empty, `none`, or `NONE` values before mapping them to `event.idm.read_only_udm.network.tls.cipher` and `event.idm.read_only_udm.network.tls.version` UDM fields.   
2026-07-13 |  Enhancement:  
`event.idm.read_only_udm.metadata.event_type`: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_HTTP` when `event.idm.read_only_udm.metadata.product_name` is `Cloudflare Gateway HTTP` or `Cloudflare WAF`.   
2026-06-18 |  Enhancement:  
\- Initialized the label for the `ApplicationNames` field to an empty string to ensure proper handling when the `ApplicationNames` raw log field contains multiple values.   
2026-06-10 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: For DNS logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare Gateway DNS`.  
\- `event.idm.read_only_udm.metadata.product_name`: For HTTP logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare Gateway HTTP`.  
\- `event.idm.read_only_udm.metadata.product_name`: For ZT Network Session logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare ZT Network Session`.  
\- `event.idm.read_only_udm.metadata.product_name`: For WAF logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare WAF`.  
\- `event.idm.read_only_udm.metadata.product_name`: For Audit logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare Audit`.  
\- `event.idm.read_only_udm.metadata.product_name`: For Network logs updated `event.idm.read_only_udm.metadata.product_name` to `Cloudflare Gateway Network`.   
2026-05-20 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields`: Removed mapping of `ConnectionCloseReason` raw log field from `event.idm.read_only_udm.additional.fields` UDM field to map to a more appropriate UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `ConnectionCloseReason` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.network.received_bytes`: Mapped `BytesReceived` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `event.idm.read_only_udm.security_result.action` UDM field as `BLOCK` when `Action` raw log field is `blockByRule`.   
2026-03-05 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `VirtualNetworkID` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.principal.resource.name`: Newly mapped `VirtualNetworkName` raw log field with `event.idm.read_only_udm.principal.resource.name` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `ApplicationIDs` (key: `ApplicationIDs`), `ApplicationStatuses` (key: `ApplicationStatuses`), `ApplicationNames` (key: `ApplicationName_index`), `CategoryIDs` (key: `CategoryIDs`), `ForensicCopyStatus` (key: `ForensicCopyStatus`), `Quarantined` (key: `Quarantined`), `UntrustedCertificateAction` (key: `UntrustedCertificateAction`), `RegistrationID` (key: `RegistrationID`), `HTTPVersion` (key: `HTTPVersion`) raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.application`: Newly mapped the first value of `ApplicationNames` raw log field with `event.idm.read_only_udm.target.application` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `BlockedFileReason` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `CategoryNames` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `DestinationIPCountryCode` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `SourceIPCountryCode` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.network.http.response_code`: Newly mapped `HTTPStatusCode` raw log field with `event.idm.read_only_udm.network.http.response_code` UDM field.  
\- `event.idm.read_only_udm.principal.resource.attribute.labels`: Newly mapped `SourceIPContinentCode` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `DestinationIPContinentCode` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `SourceInternalIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.asset.attribute.labels` : Corrected the label name for mapping of raw log field `DeviceName` which resulted in mapping of `DeviceName` to `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.   
2026-02-11 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_name`: Previously, this field was always set to `Web Application Firewall`. Now, it is only set to `Web Application Firewall` if the condition [no_id] is true. Otherwise, its value will be determined by other logic in the parser.  
\- `event.idm.read_only_udm.metadata.vendor_name`: This field is now set to `Cloudflare` within both branches of the if [no_id] conditional block.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `ActionInfo` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.   
2026-01-23 |  Enhancement:  
\- `event.idm.read_only_udm.principal.user.attribute.labels`: Newly mapped `ActorType` raw log field with `event.idm.read_only_udm.principal.user.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `ActorEmail` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- Added conditional check for `ActorEmail` to map to `event.idm.read_only_udm.principal.user.userid` if it is not a valid email address.   
2025-12-18 |  Enhancement:  
\- Added a gsub to message `\\r\\n` to message.  
\- Added a condition to check if `Action` is not equal to null before mapping `sec_action` to `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Mapped `ClientCountry` raw log field to `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.url`: Mapped `ClientRequestURL` raw log field to `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Mapped `LeakedCredentialCheckResult`, `MatchIndex`,`metadata_version`,`metadata_type`,`OriginatorRayID`,`ClientRequestQuery` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Mapped `Metadata.ruleset_version` raw log field to `event.idm.read_only_udm.security_result.rule_version` UDM field.   
2025-10-23 |  Enhancement:  
\- event.idm.read_only_udm.network.application_protocol: Removed mapping of `ClientRequestProtocol` from `event.idm.read_only_udm.network.application_protocol` to avoid redundant mapping.  
\- event.idm.read_only_udm.additional.fields: Mapped `ClientRequestProtocol` raw log field to `event.idm.read_only_udm.additional.fields`.  
\- Mapped `OriginDNSResponseTimeMs`, `OriginRequestHeaderSendDurationMs`, `OriginSSLProtocol`, `OriginTCPHandshakeDurationMs`, `ClientTCPRTTMs`, `EdgeRateLimitID`, `EdgeTimeToFirstByteMs`, `ParentRayID`, `SmartRouteColoID`, `UpperTierColoID`, `WorkerCPUTime`, `WorkerStatus`, `WorkerSubrequest`, `WorkerSubrequestCount`, `WorkerWallTimeUs`, `ZoneName` raw log fields to `event.idm.read_only_udm.additional.fields`.  
\- event.idm.read_only_udm.principal.location.state: Newly mapped `ClientRegionCode` raw log field to `event.idm.read_only_udm.principal.location.state`.  
\- Added a condition to map `SecurityLevel` raw log field to `event.idm.read_only_udm.security_result.action_details`.   
2025-10-08 |  Enhancement:  
\- The action is set to `ALLOW` for `SecurityAction` values of `allow`, `bypass`, `skip`, or if it is empty.  
\- The action is set to `CHALLENGE` for `SecurityAction` values of `challenge`, `jschallenge`, and `managedChallenge`.  
\- The action is set to `ALLOW_WITH_MODIFICATION` for `SecurityAction` values of `challengeSolved`, `jschallengeSolved`, `managedChallengeNonInteractiveSolved`, `managedChallengeInteractiveSolved`, `challengeBypassed`, `jschallengeBypassed`, and `managedChallengeBypassed`.   
2025-08-01 |  Enhancement:  
\- event.idm.read_only_udm.additional.fields: Newly mapped `CacheReserveUsed`, `CacheTieredFill`, `EdgeCFConnectingO2O`, `EdgePathingOp`, `EdgePathingSrc`, `EdgePathingStatus`, `EdgeResponseBodyBytes`, `EdgeResponseCompressionRatio`, `OriginResponseDurationMs`, `OriginResponseHeaderReceiveDurationMs` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped ClientMTLSAuthStatus raw log field(s) with event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- Updated UDM fields mapping to parse raw log fields as integers:  
\- event.idm.read_only_udm.security_result.labels, event.idm.read_only_udm.security_result.about.resource.attribute.labels: Removed mapping of `WAFAttackScore` from `event.idm.read_only_udm.security_result.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `WAFAttackScore` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.labels, event.idm.read_only_udm.security_result.about.resource.attribute.labels: Removed mapping of `WAFFlags` from `event.idm.read_only_udm.security_result.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `WAFFlags` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.labels, event.idm.read_only_udm.security_result.about.resource.attribute.labels: Removed mapping of `WAFRCEAttackScore` from `event.idm.read_only_udm.security_result.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `WAFRCEAttackScore` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.labels, event.idm.read_only_udm.security_result.about.resource.attribute.labels: Removed mapping of `WAFSQLiAttackScore` from `event.idm.read_only_udm.security_result.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `WAFSQLiAttackScore` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.labels, event.idm.read_only_udm.security_result.about.resource.attribute.labels: Removed mapping of `WAFXSSAttackScore` from `event.idm.read_only_udm.security_result.labels` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `WAFXSSAttackScore` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Removed mapping of `BotScore` from `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Mapped `BotScore` raw log field to `event.idm.read_only_udm.additional.fields` UDM field.  
\- Added logic to default event.idm.read_only_udm.metadata.event_type to GENERIC_EVENT if it is not set by previous parsing logic.   
2025-06-24 |  Enhancement:  
\- for field `ProtocolState` the key is updated from `IPProtocol` to `ProtocolState`.  
\- Renamed `ClientTCPHandshakeDurationMs` to `log.ClientTCPHandshakeDurationMs`, `ClientTLSHandshakeDurationMs` to `log.ClientTLSHandshakeDurationMs`, `ConnectionCloseReason` to `log.ConnectionCloseReason`, `ConnectionReuse` to `log.ConnectionReuse`, `DestinationTunnelID` to `log.DestinationTunnelID`, `EgressColoName` to `log.EgressColoName`, `EgressRuleID` to `log.EgressRuleID`, `EgressRuleName` to `log.EgressRuleName`, `IngressColoName` to `log.IngressColoName`, `Offramp` to `log.Offramp`, `OriginTLSCertificateIssuer` to `log.OriginTLSCertificateIssuer`, `OriginTLSCertificateValidationResult` to `log.OriginTLSCertificateValidationResult`, `OriginTLSCipher` to `log.OriginTLSCipher`, `OriginTLSHandshakeDurationMs` to `log.OriginTLSHandshakeDurationMs`, `OriginTLSVersion` to `log.OriginTLSVersion`, `RuleEvaluationDurationMs` to `log.RuleEvaluationDurationMs`, `SessionEndTime` to `log.SessionEndTime`, `WAFAction` to `log.WAFAction`, `WAFProfile` to `log.WAFProfile`, `WAFFlags` to `log.WAFFlags`, `WAFRuleID` to `log.WAFRuleID`, `WAFAttackScore` to `log.WAFAttackScore`, `WAFRCEAttackScore` to `log.WAFRCEAttackScore`, `WAFSQLiAttackScore` to `log.WAFSQLiAttackScore`, `WAFXSSAttackScore` to `log.WAFXSSAttackScore`, `SecurityRuleID` to `log.SecurityRuleID`, `ClientRequestSource` to `log.ClientRequestSource`, `CacheCacheStatus` to `log.CacheCacheStatus`, `CacheResponseBytes` to `log.CacheResponseBytes`, `CacheResponseStatus` to `log.CacheResponseStatus`, `ClientDeviceType` to `log.ClientDeviceType`, `EdgeColoCode` to `log.EdgeColoCode`, `EdgeColoID` to `log.EdgeColoID`, `OriginResponseBytes` to `log.OriginResponseBytes`, `OriginResponseStatus` to `log.OriginResponseStatus`, `OriginResponseTime` to `log.OriginResponseTime`, `ZoneID` to `log.ZoneID`, `PostureCheckName` to `log.PostureCheckName`, `PostureCheckType` to `log.PostureCheckType`, `PostureEvaluatedResult` to `log.PostureEvaluatedResult`, `ClientASN` to `log.ClientASN`, `ClientRequestScheme` to `log.ClientRequestScheme`, `ClientASNDescription` to `log.ClientASNDescription`, `ClientIPClass` to `log.ClientIPClass`, `IPSourceSubnet` to `log.IPSourceSubnet`, `SourceASN` to `log.SourceASN`, `SourceASNName` to `log.SourceASNName`, `SourceGeoHash` to `log.SourceGeoHash`, `IPDestinationSubnet` to `log.IPDestinationSubnet`, `DestinationASN` to `log.DestinationASN`, `DestinationASNName` to `log.DestinationASNName`, `DestinationGeoHash` to `log.DestinationGeoHash`, `Connection` to `log.Connection`, `IntegrationDisplayName` to `log.IntegrationDisplayName`, `IntegrationPolicyVendor` to `log.IntegrationPolicyVendor`, `Ref` to `log.Ref`, `Source` to `log.Source`, `ColoCity` to `log.ColoCity`, `ColoName` to `log.ColoName`, `ColoCode` to `log.ColoCode`, `ColoCountry` to `log.ColoCountry`, `ColoGeoHash` to `log.ColoGeoHash`, `TCPFlagsString` to `log.TCPFlagsString`, `TCPOptions` to `log.TCPOptions`, `TCPAcknowledgementNumber` to `log.TCPAcknowledgementNumber`, `TCPChecksum` to `log.TCPChecksum`, `TCPDataOffset` to `log.TCPDataOffset`, `TCPFlags` to `log.TCPFlags`, `TCPMSS` to `log.TCPMSS`, `TCPSACKBlocks` to `log.TCPSACKBlocks`, `TCPSACKPermitted` to `log.TCPSACKPermitted`, `TCPSequenceNumber` to `log.TCPSequenceNumber`, `TCPTimestampECR` to `log.TCPTimestampECR`, `TCPTimestampValue` to `log.TCPTimestampValue`, `TCPUrgentPointer` to `log.TCPUrgentPointer`, `TCPWindowScale` to `log.TCPWindowScale`, `TCPWindowSize` to `log.TCPWindowSize`, `UDPChecksum` to `log.UDPChecksum`, `UDPPayloadLength` to `log.UDPPayloadLength`, `Verdict` to `log.Verdict`, `MitigationReason` to `log.MitigationReason`, `MitigationScope` to `log.MitigationScope`, `MitigationSystem` to `log.MitigationSystem`, `IPTTL` to `log.IPTTL`, `IPTTLBuckets` to `log.IPTTLBuckets`, `IPTotalLength` to `log.IPTotalLength`, `IPTotalLengthBuckets` to `log.IPTotalLengthBuckets`, `IPv4Checksum` to `log.IPv4Checksum`, `IPv4DSCP` to `log.IPv4DSCP`, `IPv4DontFragment` to `log.IPv4DontFragment`, `IPv4ECN` to `log.IPv4ECN`, `IPv4Identification` to `log.IPv4Identification`, `IPv4Options` to `log.IPv4Options`, `IPv6DSCP` to `log.IPv6DSCP`, `IPv6ECN` to `log.IPv6ECN`, `IPv6ExtensionHeaders` to `log.IPv6ExtensionHeaders`, `IPv6FlowLabel` to `log.IPv6FlowLabel`, `IPv6Identification` to `log.IPv6Identification`, `GREChecksum` to `log.GREChecksum`, `GREEtherType` to `log.GREEtherType`, `GREHeaderLength` to `log.GREHeaderLength`, `GREKey` to `log.GREKey`, `GRESequenceNumber` to `log.GRESequenceNumber`, `GREVersion` to `log.GREVersion`, `ICMPChecksum` to `log.ICMPChecksum`, `ICMPType` to `log.ICMPType`, `ICMPCode` to `log.ICMPCode`, `AttackCampaignID` to `log.AttackCampaignID`, `AttackID` to `log.AttackID`, `AttackVector` to `log.AttackVector`, `SampleInterval` to `log.SampleInterval`, `IPProtocol` to `log.IPProtocol`, `ProtocolState` to `log.ProtocolState`, `RulesetID` to `log.RulesetID`, `RulesetOverrideID` to `log.RulesetOverrideID`, `BotScore` to `log.BotScore`, `AssetMetadata.anonymous` to `log.anonymous`, and `AssetMetadata.nativeApp` to `log.nativeApp`.  
\- Updated the mapping of `event.idm.read_only_udm.additional.fields` to utilize a generalized map for fields `Application`, `ClientAsn`, `ColoCode`, `OriginProto`, `Status`, `ProxyProtocol`, `ClientTCPHandshakeDurationMs`, `ClientTLSHandshakeDurationMs`, `ConnectionCloseReason`, `ConnectionReuse`, `DestinationTunnelID`, `EgressColoName`, `EgressRuleID`, `EgressRuleName`, `IngressColoName`, `Offramp`, `OriginTLSCertificateIssuer`, `OriginTLSCertificateValidationResult`, `OriginTLSCipher`, `OriginTLSHandshakeDurationMs`, `OriginTLSVersion`, `RuleEvaluationDurationMs`, `SessionEndTime`, `ClientRequestSource`, `CacheCacheStatus`, `CacheResponseBytes`, `CacheResponseStatus`, `ClientDeviceType`, `EdgeColoCode`, `EdgeColoID`, `OriginResponseBytes`, `OriginResponseStatus`, `OriginResponseTime`, `ZoneID`, `PostureCheckName`, `PostureCheckType`, `PostureEvaluatedResult`, `ClientASN`, `ClientRequestScheme`, `ClientASNDescription`, `ClientIPClass`, `Ref`, `Source`, `IntegrationDisplayName`, `IntegrationPolicyVendor`, `ColoCity`, `ColoName`, `ColoCountry`, `ColoGeoHash`, `TCPFlagsString`, `TCPOptions`, `TCPAcknowledgementNumber`, `TCPChecksum`, `TCPDataOffset`, `TCPFlags`, `TCPMSS`, `TCPSACKBlocks`, `TCPSACKPermitted`, `TCPSequenceNumber`, `TCPTimestampECR`, `TCPTimestampValue`, `TCPUrgentPointer`, `TCPWindowScale`, `TCPWindowSize`, `UDPChecksum`, `UDPPayloadLength`, `Verdict`, `MitigationReason`, `MitigationScope`, `MitigationSystem`, `IPTTL`, `IPTTLBuckets`, `IPTotalLength`, `IPTotalLengthBuckets`, `IPv4Checksum`, `IPv4DSCP`, `IPv4DontFragment`, `IPv4ECN`, `IPv4Identification`, `IPv4Options`, `IPv6DSCP`, `IPv6ECN`, `IPv6ExtensionHeaders`, `IPv6FlowLabel`, `IPv6Identification`, `GREChecksum`, `GREEtherType`, `GREHeaderLength`, `GREKey`, `GRESequenceNumber`, `GREVersion`, `ICMPChecksum`, `ICMPType`, `ICMPCode`, `AttackCampaignID`, `AttackID`, `AttackVector`, `SampleInterval`, `IPProtocol`, and `ProtocolState`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.detection_fields` to utilize a generalized map for fields `anonymous`, `nativeApp`, `BotScore`, `RulesetID`, `RulesetOverrideID`, `ClientMatchedIpFirewall`, `Event`, `OriginBytes`, `IpFirewall`, `ConnectTimestamp`, `DisconnectTimestamp`, `PostureExpectedJSON.os`, `PostureExpectedJSON.operator`, `PostureExpectedJSON.connection_id`, `PostureReceivedJSON.os`, `PostureReceivedJSON.overall`, `PostureReceivedJSON.version`, and `PostureReceivedJSON.state`.  
\- Updated the mapping of `event.idm.read_only_udm.security_result.about.labels` and `event.idm.read_only_udm.security_result.about.resource.attribute.labels` to utilize a generalized map for fields `WAFAction`, `SecurityRuleID`, `WAFRuleID`, `WAFProfile`, `WAFAttackScore`, `WAFFlags`, `WAFRCEAttackScore`, `WAFSQLiAttackScore`, and `WAFXSSAttackScore`.  
\- Updated the mapping of `event.idm.read_only_udm.principal.resource.attribute.labels` to utilize a generalized map for fields `IPSourceSubnet`, `SourceASN`, `SourceASNName`, and `SourceGeoHash`.  
\- Updated the mapping of `event.idm.read_only_udm.target.resource.attribute.labels` to utilize a generalized map for fields `IPDestinationSubnet`, `DestinationASN`, `DestinationASNName`, `DestinationGeoHash`, and `Connection`.  
\- Updated the mapping of `event.idm.read_only_udm.principal.user.attribute.labels` to utilize a generalized map for fields `agreedToTerms`, `ipWhitelisted`, `isEnforcedIn2Sv`, `isEnrolledIn2Sv`, `isDelegatedAdmin`, `changePasswordAtNextLogin`, `includeInGlobalAddressList`, `isAdmin`, `suspended`, `lastLoginTime`, `site_admin`.  
\- Removed redundant code for `event.idm.read_only_udm.network.sent_bytes`, `event.idm.read_only_udm.principal.ip`, `event.idm.read_only_udm.principal.asset.ip`, `event.idm.read_only_udm.principal.port`, `event.idm.read_only_udm.target.port`, `event.idm.read_only_udm.target.ip`, `event.idm.read_only_udm.target.asset.ip`, `event.idm.read_only_udm.target.hostname`, `event.idm.read_only_udm.network.ip_protocol`, `event.idm.read_only_udm.metadata.product_log_id`, `event.idm.read_only_udm.network.http.method`, `event.idm.read_only_udm.network.http.response_code`, `event.idm.read_only_udm.network.sent_bytes`, `event.idm.read_only_udm.network.http.user_agent`, `event.idm.read_only_udm.network.http.parsed_user_agent`, and `event.idm.read_only_udm.network.session_id`.  
\- Added a common field `target_ip` and mapped it to `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`.  
\- Added a common field `target_port` and mapped it to `event.idm.read_only_udm.target.port`.  
\- Added a common field `target_hostname` and mapped it to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`.  
\- Added a common field `principal_ip` and mapped it to `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`.  
\- Added a common field `principal_port` and mapped it to `event.idm.read_only_udm.principal.port`.  
\- Added a common field `network_sent_bytes` and mapped it to `event.idm.read_only_udm.network.sent.bytes`.  
\- Added conditonal check for fields `log.ClientCountry`, `log.OriginIP`, `log.OriginPort`, `log.Timestamp`, `log.ClientPort`, `log.ClientBytes`, `log.ClientProto`, `security_result`  
\- Added on_error for `QueryName`.  
\- If `event_type_value` is not set, `has_principal` is `true`, and `has_target` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION`.  
\- If `event_type_value` is not set and `has_principal_user` is `true`, then set `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.  
\- If `event_type_value` is not set, `has_principal` is `true`, and `has_target` is `false`, then set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE`.  
\- If `event_type_value` is not set, `has_principal` is `false`, `has_target` is `false`, and `has_principal_user` is `false`, then set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT`.   
2025-06-09 |  Enhancement:  
\- event.idm.read_only_udm.security_result.action_details : Newly Mapped `Action` raw log field with `event.idm.read_only_udm.security_result.action_details`.  
\- Added conditional check before mapping to `event.idm.read_only_udm.security_result.action.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ClientRequestScheme` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ClientASN` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Ref` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `Source` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `EdgeColoCode` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ClientASNDescription` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `ClientIPClass` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.src.hostname: Newly Mapped `ClientRequestHost` raw log field with `event.idm.read_only_udm.src.hostname` UDM field.  
\- event.idm.read_only_udm.src.file.full_path: Newly Mapped `ClientRequestPath` raw log field with `event.idm.read_only_udm.src.file.full_path` UDM field.  
\- event.idm.read_only_udm.network.http.user_agent: Newly Mapped `ClientUserAgent` raw log field with `event.idm.read_only_udm.network.http.user_agent` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly Mapped `Description` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly Mapped `Kind` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly Mapped `RayID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.network.application_protocol: Newly Mapped `client_request_proto` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- event.idm.read_only_udm.network.application_protocol_version: Newly Mapped `version` raw log field with `event.idm.read_only_udm.network.application_protocol_version` UDM field.   
2025-03-20 |  Enhancement:  
\- Added a null check before mapping `UserID` to `principal.user.product_object_id`.  
\- Added a regex expression check before mapping `QueryName` to `questions.name`.  
\- Added a condition check to set `metadata.event_type` to `STATUS_UPDATE`.   
2025-03-03 |  Enhancement:  
\- Mapped `log.Application`, `log.ClientAsn`, `log.ColoCode`, `log.OriginProto`, `log.Status` and `log.ProxyProtocol` to `additional.fields`.  
\- Mapped `log.ClientBytes` to `network.sent_bytes`.  
\- Mapped `log.ClientCountry` to `principal.location.country_or_region`.  
\- Mapped `log.ClientIP` to `principal.ip and principal.asset.ip`.  
\- Mapped `log.ClientMatchedIpFirewall` to `security_result.detection_fields`.  
\- Mapped `log.ClientPort` to `principal.port`.  
\- Mapped `log.ClientProto` to `network.ip_protocol`.  
\- Mapped `log.Event` to `security_result.detection_fields`.  
\- Mapped `log.OriginBytes` to `security_result.detection_fields`.  
\- Mapped `log.OriginIP` to `intermediary.ip`.  
\- Mapped `log.OriginPort` to `intermediary.port`.  
\- Mapped `log.IpFirewall` to `security_result.detection_fields`.  
\- Mapped `log.Timestamp` to `metadata.event_timestamp`.  
\- Mapped `log.ConnectTimestamp` to `security_result.detection_fields`.  
\- Mapped `log.DisconnectTimestamp` to `security_result.detection_fields`.   
2025-01-15 |  Enhancement:  
\- Mapped `AppDomain` to `target.administrative_domain`.  
\- Mapped `AppUUID` to `target.resource.product_object_id`.  
\- Mapped `UserUID` to `target.user.product_object_id`.  
\- Mapped `CreatedAt` to `metadata.event_timestamp`.  
\- Mapped `Connection` to `target.resource.attribute.labels`.  
\- Mapped `Country` to `target.location.country_or_region`.  
\- Mapped `IPAddress` to `target.ip` and `target.asset.ip`.  
\- Mapped `TemporaryAccessDuration` to `network.session_duration.seconds`.  
\- If only `target` is present and `event_type_value` is `NETWORK_CONNECTION`, then mapped `metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-11-05 |  Enhancement:  
\- Added support for a new pattern of JSON logs.   
2024-11-04 |  Enhancement:  
\- When `Action` contains `skip`, `SKIP`, or `Skip`, then set `security_result.action` to `ALLOW`.   
2024-10-29 |  Enhancement:  
\- Added support for unparsed logs.  
\- Mapped `IPSourceAddress` to `principal.ip`, and `principal.asset.ip`.  
\- Mapped `IPDestinationAddress` to `target.ip`, and `target.asset.ip`.  
\- Mapped `DestinationPort` to `target.port`.  
\- Mapped `SourcePort` to `principal.port`.  
\- Mapped `IPProtocol` to `network.ip_protocol`.  
\- Mapped `IPDestinationSubnet`, `DestinationASNNAME`, `DestinationASN`, and `DestinationGeoHash` to `target.resource.attribute.labels`.  
\- Mapped `IPSourceSubnet`, `SourceASNNAME`, `SourceASN`, and `SourceGeoHash` to `principal.resource.attribute.labels`.  
\- MApped `SourceCountry` to `principal.location.country_or_region`.  
\- Mapped `DestinationCountry` to `target.location.country_or_region`.  
\- Mapped `ColoCity`, `ColoCode`, `ColoCountry`, `ColoGeoHash`, `ColoName`, `GREChecksum`, `GREEtherType`, `GREHeaderLength`, `GREKey`, `GRESequenceNumber`, and `GREVersion` to `additional.fields`.  
\- Mapped `ICMPChecksum`, `ICMPType`, `ICMPCode`, `IPProtocol`, `ProtocolState`, `IPTTL`, `IPTTLBuckets`, `IPTotalLength`, `IPTotalLengthBuckets`, `IPv4Checksum`, `IPv4DSCP`, `IPv4DontFragment`, `IPv4ECN`, `IPv4Identification`, `IPv6DSCP`, `IPv6ECN`, `IPv6FlowLabel`, and `IPv6Identification` to `additional.fields`.  
\- Mapped `MitigationScope`, `MitigationSystem`, `SampleInterval`, `TCPAcknowledgementNumber`, `TCPChecksum`, `TCPDataOffset`, `TCPFlags`, `TCPFlagsString`, `TCPMSS`, `TCPSACKPermitted`, `TCPSequenceNumber`, `TCPTimestampECR`, `TCPTimestampValue`, `TCPUrgentPointer`, `TCPWindowScale`, `TCPWindowSize`, `UDPChecksum`, `UDPPayloadLength`, and `Verdict` to `additional.fields`.  
\- When `Outcome` is `drop`, then set `security_result.action` to `BLOCK`.  
\- When `Direction` is `ingress`, then set `network.direction` to `INBOUND`.  
\- Mapped `AttackCampaignID`, `AttackID`, and `AttackVector` to `additional.fields`.  
\- Mapped `RuleID` to `security_result.rule_id`.  
\- Mapped `RuleName` to `security_result.rule_name`.  
\- Mapped `RulesetID` and `RulesetOverrideID` to `security_result_detection_fields`.   
2024-10-24 |  Bug-Fix:  
\- When `Action` contains `bypass`, then set `security_result.action` to `ALLOW`.  
\- Mapped `ClientVersion` to `metadata.product_version`.  
\- Mapped `DeviceID` to `principal.asset_id`.  
\- Mapped `DeviceManufacturer` to `principal.asset.hardware`.  
\- Mapped `DeviceModel` to `principal.asset.hardware`.  
\- Mapped `DeviceName` to `principal.asset.attribute.labels`.  
\- Mapped `DeviceSerialNumber` to `principal.resource.attribute.labels`.  
\- Mapped `DeviceType` to `principal.resource.name`.  
\- Mapped `Email` to `principal.user.email_addresses`".  
\- Mapped `OSVersion` to `principal.platform_version`.  
\- Mapped `PolicyID` to `security_result.rule_id`.  
\- Mapped `PostureCheckName` to `additional.fields`.  
\- Mapped `PostureCheckType` to `additional.fields`.  
\- Mapped `PostureEvaluatedResult` to `additional.fields`.  
\- Mapped `PostureExpectedJSON.os` to `security_result.detection_fields`.  
\- Mapped `PostureExpectedJSON.operator` to `security_result.detection_fields`.  
\- Mapped `PostureExpectedJSON.connection_id` to `security_result.detection_fields`.  
\- Mapped `PostureReceivedJSON.os` to `security_result.detection_fields`.  
\- Mapped `PostureReceivedJSON.overall` to `security_result.detection_fields`.  
\- Mapped `PostureReceivedJSON.version` to `security_result.detection_fields`.  
\- Mapped `PostureReceivedJSON.state` to `security_result.detection_fields`.  
\- Mapped `PostureReceivedJSON.last_seen` to `date`.  
\- If both `principal` and `event_type_value` are present, then mapped `metadata.event_type` to `USER_UNCATEGORIZED`.   
2024-10-15 |  Enhancement:  
\- Mapped `ClientRequestSource` to `additional.fields`.   
2024-10-03 |  Enhancement:  
\- Mapped `SecurityActions`, `SecurityRuleIDs`, and `SecuritySources` to `additional.fields`.  
\- Mapped `SecurityAction`, `SecurityRuleID` to `security_result.about.resource.attribute.labels`.  
\- Mapped `SecurityRuleID` to `security_result.threat_id`.  
\- Mapped `SecurityRuleDescription` to `security_result.threat_name` and `security_result.rule_name`.   
2024-02-19 |  Bug-Fix:  
\- When there is no principal and target machine data, then mapped `metadata.event_type` to `GENERIC_EVENT`.  
\- When `Datetime` field is missing and `Timestamp` field is present, then mapped `Timestamp` to `metadata.event_timestamp`.  
\- Mapped `ClientIP` to `principal.ip`.  
\- Mapped `RayID` to `metadata.product_log_id`.  
\- Mapped `EdgeResponseStatus` to `network.http.response_code`.  
\- Mapped `ClientRequestMethod` to `network.http.method`.  
\- Mapped `ClientRequestURI` to `target.uri`.  
\- Mapped `ClientRequestHost` to `target.hostname`.   
2024-01-31 |  Enhancement:  
\- Mapped `BotScore` to `security_result.detection_fields`.  
\- Aligned `principal.hostname`, `target.hostname`, `principal.asset.hostname`, and `target.asset.hostname` mappings.  
\- Aligned `principal.ip`, `target.ip`, `principal.asset.ip`, and `target.asset.ip` mappings.   
2024-01-08 |  Enhancement:  
\- When `Action` contains `allow`, then set `security_result.action` to `ALLOW`.  
\- Added mapping of `DeviceName` to `principal.hostname`, `principal.asset.hostname`.  
\- Added mapping of `SourceIP` to `principal.ip` for DNS logs.  
\- Added a null conditional check before mapping `principal` to `event.idm.read_only_udm.principal`.  
\- Added a null conditional check before mapping `target` to `event.idm.read_only_udm.target`.   
2023-11-22 |  Enhancement:  
\- Mapped `WAFRuleID` to `security_result.threat_id`.  
\- Mapped `WAFRuleMessage` to `security_result.threat_name`.  
\- Mapped `WAFRCEAttackScore`, `WAFSQLiAttackScore`, `WAFXSSAttackScore`, `WAFAttackScore`, `WAFFlags` to `security_result.about.resource.attribute.labels`.   
2023-10-09 |  Enhancement:  
\- When `SecurityAction` value is null or not present, then set `security_result.action` to `ALLOW`.   
2023-09-26 |  Enhancement:  
\- Modified mappings from using deprecated UDM fields to alternative fields.  
\- Added mapping from `security_result.about.labels` to `security_result.about.resource.attribute.labels`.  
\- Added mapping from `about.labels` to `security_result.about.resource.attribute.labels`.  
\- Added mapping from `target.resource.id` to `target.resource.product_object_id`.   
2023-04-25 |  Enhancement to map the following raw log fields to UDM fields:  
\- Initialized `EdgeStartTimestamp`, `ClientIP`, `ClientRequestHost`, `ClientRequestURI`, `ClientRequestMethod`, `Datetime`, `ActorEmail`, and `ActorIP` to null.  
\- Mapped `AssetExternalID` to `principal.asset_id`.  
\- Mapped `AssetDisplayName` to `principal.asset.attribute.labels`.  
\- Mapped `AssetLink` to `principal.url`.  
\- Mapped `AssetMetadata.userKey` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.clientId` to `principal.user.userid`.  
\- Mapped `AssetMetadata.anonymous` to `security_result.detection_fields`.  
\- Mapped `AssetMetadata.nativeApp` to `security_result.detection_fields`.  
\- Mapped `DetectedTimestamp` to `metadata.event_timestamp`.  
\- Mapped `FindingTypeDisplayName` to `security_result.description`.  
\- Mapped `FindingTypeID` to `security_result.rule_id`.  
\- Mapped `FindingTypeSeverity` to `security_result.severity`.  
\- Mapped `InstanceID` to `principal.resource.product_object_id`.  
\- Mapped `IntegrationDisplayName` to `additional.fields`.  
\- Mapped `IntegrationID` to `metadata.product_deployment_id`.  
\- Mapped `IntegrationPolicyVendor` to `additional.fields`.  
\- Mapped `AssetMetadata.customerId` to `principal.user.userid`.  
\- Mapped `AssetMetadata.primaryEmail` to `principal.user.email_addresses`.  
\- Mapped `AssetMetadata.agreedToTerms` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.ipWhitelisted` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.lastLoginTime` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.isEnforcedIn2Sv` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.isEnrolledIn2Sv` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.isDelegatedAdmin` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.changePasswordAtNextLogin` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.includeInGlobalAddressList` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.isAdmin` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.suspended` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.url` to `principal.url`.  
\- Mapped `AssetMetadata.site_admin` to `principal.user.attribute.labels`.  
\- Mapped `AssetMetadata.login` to `principal.user.userid`.  
\- Mapped `AssetMetadata.owner.id` to `principal.user.userid`.  
\- Mapped `AssetMetadata.name.fullName` to `principal.user.user_display_name`.  
\- Mapped `AssetMetadata.name.givenName` to `principal.user.first_name`.  
\- Mapped `AssetMetadata.name.familyName` to `principal.user.last_name`.  
\- Mapped `Allowed` to `security_result.action`.  
\- Mapped `AppDomain` to `target.administrative_domain`.  
\- Mapped `AppUUID` to `target.resource.product_object_id`.  
\- Mapped `Connection` to `target.resource.attribute.labels`.  
\- Mapped `Country` to `target.location.country_or_region`.  
\- Mapped `CreatedAt` to `metadata.event_timestamp`.  
\- Mapped `IPAddress` to `target.ip`.  
\- Mapped `RayID` to `metadata.product_log_id`.  
\- Mapped `Email` to `principal.user.email_addresses` and `target.user.email_addresses`.  
\- Mapped `TemporaryAccessDuration` to `network.session_duration.seconds`.  
\- Mapped `UserUID` to `target.user.product_object_id`.  
\- Mapped `UserAgent` to `network.http.parsed_user_agent`.  
\- Mapped `ClientRequestUserAgent` to `network.http.parsed_user_agent`.  
\- Mapped `PolicyName` to `security_result.rule_name`.  
\- Mapped `SessionID` to `network.session_id`.  
\- Mapped `Transport` to `network.ip_protocol`.  
\- Mapped `SNI` to `tls.client.server_name`.  
\- Mapped `DeviceName` to `principal.asset.attribute.labels`.  
\- Mapped `BytesReceived` to `network.received_bytes`.  
\- Mapped `BytesSent` to `network.sent_bytes`.  
\- Mapped `Protocol` to `network.ip_protocol`.  
\- Mapped `ClientTCPHandshakeDurationMs` to `additional.fields`.  
\- Mapped `ClientTLSCipher` to `network.tls.cipher`.  
\- Mapped `ClientTLSHandshakeDurationMs` to `additional.fields`.  
\- Mapped `ClientTLSVersion` to `network.tls.version`.  
\- Mapped `ConnectionCloseReason` to `additional.fields`.  
\- Mapped `ConnectionReuse` to `additional.fields`.  
\- Mapped `DestinationTunnelID` to `additional.fields`.  
\- Mapped `EgressIP` to `principal.ip`.  
\- Mapped `EgressPort` to `principal.port`.  
\- Mapped `EgressRuleID` to `additional.fields`.  
\- Mapped `EgressRuleName` to `additional.fields`.  
\- Mapped `IngressColoName` to `additional.fields`.  
\- Mapped `Offramp` to `additional.fields`.  
\- Mapped `OriginIP` to `target.ip`.  
\- Mapped `OriginPort` to `target.port`.  
\- Mapped `OriginTLSCertificateIssuer` to `additional.fields`.  
\- Mapped `OriginTLSCertificateValidationResult` to `additional.fields`.  
\- Mapped `OriginTLSCipher` to `additional.fields`.  
\- Mapped `OriginTLSHandshakeDurationMs` to `additional.fields`.  
\- Mapped `OriginTLSVersion` to `additional.fields`.  
\- Mapped `RuleEvaluationDurationMs` to `additional.fields`.  
\- Mapped `SessionEndTime` to `additional.fields`.  
\- Mapped `SessionStartTime` to `metadata.event_timestamp`.  
\- Mapped `SourceIP` to `src.ip`.  
\- Mapped `SourcePort` to `src.port`.  
\- Mapped `UserID` to `principal.user.product_object_id`.  
\- Mapped `VirtualNetworkID` to `principal.resource.product_object_id`.   
2023-04-06 |  Enhancement - Declared the fields `WAFRuleMessage`, `WAFAction`, `QueryType`, `RayID`, `Email` at global level.  
\- Mapped `metadata.event_type` as `NETWORK_UNCATEGORIZED` where the field `QueryName` and `QueryNameReversed` are null.  
\- Added on error checks for the following fields: RData[n].type, RData[n].data, EdgeResponseBytes, ClientRequestBytes, EdgeResponseStatus.  
\- Added string conversion for the fields `SourcePort` and `DestinationPort`.   
2022-10-10 |  Enhancement  
\- Mapped `metadata.product_name` to `Web Application Firewall`.  
\- Mapped `metadata.vendor_name` to `Cloudflare`.   
2022-05-23 |  Enhancement to map following raw logs elements to UDM elements:  
Mapped `ClientASN` to `network.asn`.  
Mapped `ClientSSLCipher` to `network.tls.cipher`.  
Mapped `ClientSSLProtocol` to `network.tls.version`.  
Mapped `EdgeResponseContentType` to `target.file.mime_type`.  
Mapped `OriginIP` to `intermediary.ip`.  
Mapped `FirewallMatchesActions` to `security_result.action`.  
Mapped `FirewallMatchesRuleIDs` to `security_result.rule_id`.  
Mapped `FirewallMatchesSources` to `security_result.rule_name`.  
Mapped `WAFRuleID`, `WAFProfile` to `security_result.about.labels`.  
Mapped `CacheCacheStatus`, `CacheResponseBytes`, `CacheResponseStatus`, `ClientDeviceType`, `EdgeColoCode`, `EdgeColoID`, `OriginResponseBytes`, `OriginResponseStatus`, `OriginResponseTime`, `ZoneID` to `additional.fields`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
