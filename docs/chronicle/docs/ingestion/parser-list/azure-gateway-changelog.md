---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-gateway-changelog/
title: Change log for AZURE_GATEWAY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:36:57.599958+00:00
---

# Change log for AZURE_GATEWAY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-gateway-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_GATEWAY

Date | Changes  
---|---  
2026-09-21 |  Enhancement:  
\- `event.idm.read_only_udm.additional.fields` : Removed mapping of `properties.policyScopeName` from `event.idm.read_only_udm.additional.fields` UDM field to introduce more specific UDM mapping.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.policyScopeName` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.details.data`, `properties.policyScope`, `properties.engine`, and `properties.policyId` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.   
2026-07-22 |  Enhancement:  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.ruleGroup` and `properties.ruleSetVersion` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.site` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.security_result.about.file.full_path`: Newly mapped `properties.details.file` raw log field with `event.idm.read_only_udm.security_result.about.file.full_path` UDM field.  
\- `event.idm.read_only_udm.security_result.about.resource.attribute.labels`: Newly mapped `record.properties.details.line` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.   
2026-06-24 |  Enhancement:  
\- `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname`: Removed mapping of `properties.originalHost` and `properties.host` from `event.idm.read_only_udm.principal.hostname` and `event.idm.read_only_udm.principal.asset.hostname` UDM fields, as these fields represent the destination hostname and are more appropriate in the target entity.  
\- `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname`: Mapped `properties.originalHost` and `properties.host` raw log fields to `event.idm.read_only_udm.target.hostname` and `event.idm.read_only_udm.target.asset.hostname` UDM fields, When `properties.host` is not available, consider using `properties.originalHost`.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `properties.noOfConnectionRequests` and `properties.WAFPolicyID` raw log fields to `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `properties.serverStatus`, `properties.serverConnectTime`, and `properties.serverHeaderTime` raw log fields to `event.idm.read_only_udm.additional.fields`.   
2025-06-05 |  Enhancement:  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `category` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `operationName`, `properties.engine`, `properties.policyId`, `properties.policyScope`, and `properties.policyScopeName` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly mapped `resourceId` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- event.idm.read_only_udm.security_result.action_details: Newly mapped `properties.action` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM field.  
\- event.idm.read_only_udm.principal.ip: Newly mapped `properties.clientIp` raw log field with `event.idm.read_only_udm.principal.ip` UDM field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly mapped `properties.clientIp` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- event.idm.read_only_udm.principal.hostname: Newly mapped `properties.hostname` raw log field with `event.idm.read_only_udm.principal.hostname` UDM field.  
\- event.idm.read_only_udm.principal.asset.hostname: Newly mapped `properties.hostname` raw log field with `event.idm.read_only_udm.principal.asset.hostname` UDM field.  
\- event.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `properties.instanceId` raw log field with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `properties.message` raw log field with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.target.url: Newly mapped `properties.requestUri` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `properties.ruleGroup`, `properties.ruleSetType` and `properties.ruleSetVersion` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `properties.ruleId` raw log field with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.network.session_id: Newly mapped `properties.transactionId` raw log field with `event.idm.read_only_udm.network.session_id` UDM field.  
\- event.idm.read_only_udm.security_result.about.file.full_path: Newly mapped `properties.details.file` raw log field with `event.idm.read_only_udm.security_result.about.file.full_path` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `properties.details.line` raw log field with `event.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field.  
\- event.idm.read_only_udm.security_result.description: Newly mapped `properties.details.message` raw log field with `event.idm.read_only_udm.security_result.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Set `event.idm.read_only_udm.security_result.severity` to `INFORMATIONAL` when `security_result.severity` is `INFORMATION`.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when `has_principal` and `has_target` are `true`.  
\- event.idm.read_only_udm.metadata.event_type: Set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when `has_principal` is `true` and `has_target` is `false`.   
2025-02-24 |  Enhancement:  
\- Added a Grok pattern to parse failed logs.  
\- Added condition check before renaming `properties.userAgent` to `network.http.parsed_user_agent`.  
\- Mapped `properties_action` to `security_result.action_details`.   
2024-12-18 |  Enhancement:  
\- When `properties_action` is `Detected`, then mapped `security_result_action` to `ALLOW`.   
2024-12-05 |  Enhancement:  
\- When `properties_action` is `allowed`, then mapped `security_result_action` to `ALLOW`.  
\- When `properties_action` is `Blocked`, then mapped `security_result_action` to `BLOCK`.  
\- When `properties_action` is `Matched`, `Detected`, then mapped `security_result_action` to `UNKNOWN_ACTION`.  
\- Mapped `dest_ip` to `target.ip`.  
\- Mapped `hostname` to `target.hostname`.   
2024-11-05 |  Enhancement:  
\- Mapped `instanceId` to `principal.application`.  
\- Mapped `properties.clientPort` to `principal.port`.  
\- Mapped `properties.ruleSetType` to `security_result.detection_fields`.  
\- Mapped `properties.ruleId` to `security_result.rule_id`.  
\- Mapped `properties.message` to `metadata.description`.   
2024-06-20 |  Enhancement:  
\- Added support for a new pattern of unparsed JSON logs.  
\- Mapped `instanceId` to `principal.application`.  
\- Mapped `sslEnabled` and `upstreamSourcePort` to `additional.fields`.   
2024-04-19 |  Enhancement:  
\- Added support for multiple event JSON logs.   
2023-12-22 |  Enhancement:  
\- Mapped `resourceid` to `target.resource.id`.  
\- Mapped `properties.operationStatus` to `security_result.category_details`.  
\- Mapped `properties.configuration.Name` to `principal.hostname`.  
\- Mapped `properties.message` to `metadata.description`.  
\- Mapped `properties.configuration.RemoteStie` to `target.hostname`.  
\- Mapped `level` to `security_result.severity_details`.  
\- Mapped `properties.configuration.Ikeversion` to `principal.resource.attribute.labels`.  
\- Mapped `properties.configuration.LocalTunnelEndpoint` to `principal.ip`.  
\- Mapped `properties.configuration.RemoteTunnelEndpoint` to `target.ip`.  
\- Mapped `properties.configuration.LocalSubnets`, `properties.configuration.RemoteSubnets`, `properties.configuration.VirtualNetworkRanges`, and `properties.configuration.VirtualNetworkSubnets` to `principal.resource.attribute.labels`.  
\- Mapped `properties.configuration.VIPAddress` to `principal.ip`.  
\- Mapped `properties.configuration.BgpConfiguration.GatewayConfig.PeerAddress` to `targrt.ip`.  
\- Mapped `properties.configuration.BgpConfiguration.GatewayConfig.PeerType` and `properties.configuration.BgpConfiguration.GatewayConfig.Asn` to `security_result.detection_fields`.   
2023-11-16 |  \- Created new parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
