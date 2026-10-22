---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sourcefire-ids-changelog/
title: Change log for SOURCEFIRE_IDS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:53.567720+00:00
---

# Change log for SOURCEFIRE_IDS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/sourcefire-ids-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for SOURCEFIRE_IDS

Date | Changes  
---|---  
2026-10-05 |  Enhancement:  
\- Added support for new format of JSON logs.  
\- `event.idm.read_only_udm.security_result.severity`: Updated the mapping for `Impact` raw log field to set `event.idm.read_only_udm.security_result.severity` to `HIGH` when `Impact` is `1` and `MEDIUM` when `Impact` is `2`.  
\- `event.idm.read_only_udm.security_result.action`: Updated the mapping for `InlineResult` raw log field to set `event.idm.read_only_udm.security_result.action` to `Allow` when `InlineResult` value is `Would block`.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `OriginalInitiatorIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `ResponderCountry` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `Application` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-04-30 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.product_log_id`: Newly mapped `EventID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `EventType` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.principal.location.country_or_region`: Newly mapped `InitiatorCountry` raw log field with `event.idm.read_only_udm.principal.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_id`: Newly mapped `SignatureID` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_name`: Newly mapped `FirewallRule` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Newly mapped `EventSecond` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `GeneratorID`, `FirewallPolicy` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.network.session_id`: Newly mapped `ConnectionID` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- `event.idm.read_only_udm.security_result.attack_details.tactics` and `event.idm.read_only_udm.security_result.attack_details.techniques`: Newly mapped `MitreAttackGroups` raw log field with `event.idm.read_only_udm.security_result.attack_details.tactics` and `event.idm.read_only_udm.security_result.attack_details.techniques` UDM fields.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `HTTP_URI` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.security_result.action_details`: Newly mapped `InlineResultReason` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `InitiatorIP` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `InitiatorPort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.application`: Newly mapped `ClientApplication` raw log field with `event.idm.read_only_udm.principal.application` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `ResponderIP` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.user.userid`: Newly mapped `UserID` raw log field with `event.idm.read_only_udm.principal.user.userid` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `ResponderPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.network.application_protocol`: Newly mapped `Application` raw log field with `event.idm.read_only_udm.network.application_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.summary`: Newly mapped `IntrusionRuleMessage` raw log field with `event.idm.read_only_udm.security_result.summary` UDM field.  
\- `event.idm.read_only_udm.security_result.rule_version`: Newly mapped `SignatureRevision` raw log field with `event.idm.read_only_udm.security_result.rule_version` UDM field.  
\- `event.idm.read_only_udm.security_result.severity`: Newly mapped `Impact` raw log field with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname`: Newly mapped `Device` raw log field with `event.idm.read_only_udm.observer.hostname` and `event.idm.read_only_udm.observer.asset.hostname` UDM fields.  
\- `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip`: Newly mapped `DeviceIP` raw log field with `event.idm.read_only_udm.intermediary.ip` and `event.idm.read_only_udm.intermediary.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.intermediary.asset.hardware.serial_number`: Newly mapped `DeviceSerialNumber` raw log field with `event.idm.read_only_udm.intermediary.asset.hardware.serial_number` UDM field.  
\- `event.idm.read_only_udm.security_result.description`: Newly mapped `NAP_Policy` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `FirstPacketSecond`, `EventMicrosecond`, `ApplicationID`, `ClientApplicationID`, `InstanceID`, `ClientApplicationRiskIndex`, `ApplicationProductivityIndex`, `ApplicationRiskIndex`, `SensorID`, `ClientApplicationProductivityIndex`, `HTTP_Hostname`, `PriorityID`, `ProtocolID`, `VLAN_ID`, `SnortRuleGroups`, `IntrusionPolicy`, `InitiatorCountryID`, `ResponderCountryID` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2024-12-23 |  Enhancement:  
\- Mapped `destinationPort` to `target.port`.  
\- Mapped `sourcePort` to `principal.port`.   
2024-12-06 |  Enhancement:  
\- Mapped `fileShaHash.data` to `principal.file.sha256`.  
\- Mapped `fileShaHash.blockType`, `fileShaHash.blockLength`, `fileName.data`, `fileName.blockType`, and `fileName.blockLength` to `additional.fields`.   
2024-07-22 |  Enhancement:  
\- Added support to parse a new pattern of JSON logs.  
\- Mapped `MessageSourceAddress` to `principal.ip`.  
\- Mapped `Hostname` to `principal.hostname`.  
\- Mapped `SourceModuleName` and `SourceModuleType` to `principal.resource.attribute.labels`.  
\- Mapped `SyslogFacility`, `SyslogSeverity`, `DeviceUUID`, `GID`, and `Revision` to `security_result.detection_fields`.   
2024-03-07 |  Enhancement:  
\- Mapped `httpURI.data` to `target.url`.  
\- Mapped `sourcePortOrIcmpType` to `principal.port`.  
\- Mapped `destinationPortOrIcmpType` to `target.port`.  
\- Mapped `@computed.blocked` to `security_result.action_details`.  
\- Mapped `blockType`, `policyUuid`, `recordLength`, `accessControlRuleId`, `connectionInstanceId`, `@computed.message`, `egressVRFName.data`, `ingressVRFName.data`, `smptTo.blockType`, `smtpHeaders.blockType`, `smtpFrom.blockType`, `smtpAttachments.blockType`, `egressVRFName.blockType`, `httpURI.blockType`, `httpHostname.blockType`, `ingressVRFName.blockType`, `httpHostname.data`, `smptTo.data`, `smtpHeaders.data`, `smtpAttachments.data`, `smtpFrom.data`, `blockedReasonId` and `@computed.blockedReasonId` to `security_result.detection_fields`.  
\- Aligned `principal.ip` and `principal.hostname` mappings.  
\- Aligned `principal.hostname` and `principal.asset.hostname` mappings.  
\- Aligned `target.ip` and `target.asset.ip` mappings.   
2023-07-06 |  Enhancement -  
\- Handled logs where `recordType = 2`.  
\- Mapped `packetLength`, `packetData`, `packetSecond`, and `packetMicroSecond` to `additional` UDM fields.  
\- Modified `GENERIC_EVENT` `metadata.event_type` to `USER_RESOURCE_ACCESS` for logs where `recordType = 2`.  
\- Handled logs in CEF format.   
2022-11-07 |  Enhancement -  
\- Handled unparsed logs by adding new field mapping.  
\- Mapped `IntrusionPolicy` to `additional.fields`.  
\- Mapped `IngressInterface` to `asset.attribute.labels`.  
\- Mapped `IngressZone` to `location.name`.  
\- Mapped `EgressInterface` to `asset.attribute.labels`.  
\- Mapped `EgressZone` to `location.name`.  
\- Mapped `InlineResult` to `security_result.action`.  
\- Mapped `Client` to `http.user_agent`.  
\- Mapped `ApplicationProtocol` to `network.application_protocol`.  
\- Mapped `Classification` to `security_result.threat_name`.  
\- Mapped `User` to `security_result.action_details`.  
\- Mapped `Message` to `metadata.description`.  
\- Mapped `Severity` to "`security_result.severity`.  
\- Mapped `Priority` to `security_result.priority`.  
\- Mapped `SeverityValue` to `security_result.severity`.   
2022-08-22 |  Enhancement -  
\- Handled unparsed logs by adding new grok pattern.  
\- Modified `GENERIC_EVENT` event_type to `STATUS_UPDATE` wherever possible.   
2022-06-09 |  Bug - Parsed logs of kv format (FTD)  
Mapped following fields-  
\- Mapped `sourceHostname` to `principal.hostname`.  
\- Mapped `DstIP` to `target.ip`.  
\- Mapped `SrcIP` to `principal.ip`.  
\- Mapped `DstPort` to `target.port`.  
\- Mapped `SrcPort` to `principal.port`.  
\- Mapped `Protocol` to `network.ip_protocol`.  
\- Mapped `InitiatorBytes` to `network.sent_bytes`.  
\- Mapped `ResponderBytes` to `network.received_bytes`.  
\- Mapped `NAPPolicy` to `security_result.description`.  
\- Mapped `EventPriority` to `security_result.severity`.  
\- Mapped `AccessControlRuleName` to `security_result.rule_name`.  
\- Mapped `ACPolicy` to `principal.resource.name`.  
\- Mapped `ACCESS_POLICY` to `principal.resource.resource_type`.  
\- Mapped `event_type` according to log values.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
