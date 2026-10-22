---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/versa-firewall-changelog/
title: Change log for VERSA_FIREWALL \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:23.628491+00:00
---

# Change log for VERSA_FIREWALL  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/versa-firewall-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for VERSA_FIREWALL

Date | Changes  
---|---  
2026-01-29 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname`,`event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `applianceName` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` when `log_type` is `accessLog` or `flowIdLog` because these log types represent the appliance acting as a network intermediary (like a firewall) processing traffic, rather than being the source or final destination of the event.  
\- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `applianceName` raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field when `log_type` is `accessLog` or `flowIdLog`.  
\- `event.idm.read_only_udm.metadata.description: Updated mapping for `event.idm.read_only_udm.metadata.description` from IP flow information (`sourceIPv4Address to destinationIPv4Address`) to the value of the `log_type` raw log field.  
\- Added a gsub to remove `"` characters from raw log fields `protocolInfo`,`ucsReason` and `ecsReason`.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated conditional logic:  
\- `NETWORK_CONNECTION`: Modified the conditional check before mapping the event type to NETWORK_CONNECTION.  
\- `STATUS_UPDATE`: Added a conditional check [has_principal] == `true` before mapping the event type to STATUS_UPDATE.  
\- `GENERIC_EVENT`: Set `GENERIC_EVENT` as fallback when conditions for `NETWORK_CONNECTION` nor `STATUS_UPDATE` conditions are met.   
2025-12-10 |  Enhancement:  
\- event.idm.read_only_udm.principal.nat_ip: Newly mapped `postNATSourceIPv4Address` raw log field with `event.idm.read_only_udm.principal.nat_ip` UDM field.  
\- event.idm.read_only_udm.target.nat_ip: Newly mapped `postNATDestinationIPv4Address` raw log field with `event.idm.read_only_udm.target.nat_ip` UDM field.  
\- event.idm.read_only_udm.principal.nat_port: Newly mapped `postNAPTsourceTransportPort` raw log field with `event.idm.read_only_udm.principal.nat_port` UDM field.  
\- event.idm.read_only_udm.target.nat_port: Newly mapped `postNAPTdestinationTransportPort` raw log field with `event.idm.read_only_udm.target.nat_port` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `natRuleName` raw log field with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `natEvent` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `log_type` raw log field with `event.idm.read_only_udm.additional.fields` UDM field when it's not populated in `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `flowCookie`, `flowId`, `sourceNatPoolName`, `destNatPoolName`, `deviceKey`, `deviceName`, `observationTimeMilliseconds` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.   
2025-10-19 |  Enhancement:  
\- Refactored the merge target for `ipsApplication_field` to use the relative path `additional.fields` instead of the full path `event.idm.read_only_udm.additional.fields`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `threatSeverity`, `dnsfBadCname`, `dnsfEvType`, `dnsfDomain`, `dnsfMsgType`, `dnsfProfileName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.security_result.category_details`: Newly mapped `dnsfIpReputation` raw log field with `event.idm.read_only_udm.security_result.category_details` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `dnsfAction`, `HitCount`, `groupId`, `signatureRev`, `packetTime`, `moduleId` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `dnsfBadResolvedV4Addr` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `dnsfIpGeoLocation` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.   
2025-09-25 |  Enhancement:  
\- `event.idm.read_only_udm.metadata.description`: Changed mapping for `event.idm.read_only_udm.metadata.description` UDM field. It is now conditionally mapped from a combination of `sourceIPv4Address` and `destinationIPv4Address` raw log fields when both are present, else mapped `log_type` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- `event.idm.read_only_udm.target.hostname`: Newly mapped `host` raw log field with `event.idm.read_only_udm.target.hostname` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `eipProfileName`, `traffScope`, `srcSGT`, `destSGT`, `ucsBand`, `ucsReason`, `urlLookupSrc`, `protocolInfo`, `ecsBand`, `ecsReason`, `appAuth` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `ucsScore`, `policyActionName`, `policyActionModule`, `ecsScore` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.intermediary.asset.product_object_id`: Newly mapped `applianceId` raw log field with `event.idm.read_only_udm.intermediary.asset.product_object_id` UDM field.   
2025-06-06 |  Enhancement:  
\- Added a Grok pattern to support new format of SYSLOG + KV logs.  
\- event.idm.ready_only_udm.intermediary.hostname: Newly mapped `inter_hostname` raw log field with `event.idm.ready_only_udm.intermediary.hostname` UDM field  
\- Fixed the code to handle the `network.ip_protocol` field.  
\- Added a conditional check `has_principal`. If `has_principal` is true and either of `destinationIPv4Address`, `remoteSite` , `destinationIPv6Address` , `clientIPv4Address` or `hostname` is not empty then map `metadata.event_type` to `NETWORK_CONNECTION` else map `metadata.event_type` to `GENERIC_EVENT`.  
\- Added a conditional check `msg2`. If `msg2` is not empty then map the log value's else drop the log.  
\- Add a KV filter for `msg2` to filter out the data.   
2024-06-03 |  Enhancement:  
\- Mapped `idpAction` to `security_result.action`.  
\- Mapped `threatType` to `security_result.detection_fields`.  
\- Mapped `ipsDirection` to `security_result.detection_fields`.  
\- Mapped `ipsProfile` to `security_result.detection_fields`.  
\- Mapped `signaturePriority` to `security_result.severity`.  
\- Mapped `signatureMsg` to `security_result.detection_fields`.  
\- Mapped `signatureId` to `security_result.detection_fields`.  
\- Mapped `ipsApplication` to `security_result.detection_fields`.  
\- Mapped `classMsg` to `security_result.description`.  
\- Mapped `ipsProfileRule` to `security_result.rule_name`.  
\- Mapped `ipsProtocol` to `network.ip_protocol`.   
2023-07-03 |  Enhancement: Added support for `entitlementLog`, `monStatsLog`, and `tcpAppMonLog`.   
2022-11-04 |  Enhancement: New parser created.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
