---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-nsg-flow-changelog/
title: Change log for AZURE_NSG_FLOW \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:44:09.753933+00:00
---

# Change log for AZURE_NSG_FLOW  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-nsg-flow-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_NSG_FLOW

Date | Changes  
---|---  
2026-07-28 |  Enhancement:  
\- `event.idm.read_only_udm.target.cloud.environment`: Removed mapping of `MICROSOFT_AZURE` from `event.idm.read_only_udm.target.cloud.environment` UDM field since `event.idm.read_only_udm.target.cloud.environment` is a deprecated UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.cloud.environment`: Mapped the value of `MICROSOFT_AZURE` with `event.idm.read_only_udm.target.resource.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_type`: Removed mapping of `STORAGE_BUCKET` from `event.idm.read_only_udm.target.resource.resource_type` UDM field and mapped `FIREWALL_RULE` instead as it accurately reflects network configuration changes over standard data access.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `properties.direction` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field since this field represents the network flow.  
\- `event.idm.read_only_udm.network.direction`: Mapped `properties.direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- `event.idm.read_only_udm.security_result.about.labels`: Removed mapping of `properties.type` raw log field from `event.idm.read_only_udm.security_result.about.labels` UDM field since this field represents the action details.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `properties.type` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.principal.network.ip_subnet_range`: Newly mapped `properties.subnetPrefix` raw log field with `event.idm.read_only_udm.principal.network.ip_subnet_range` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `properties.conditions.protocols` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- Renamed the raw log field from subcription to subscription.  
\- Renamed the raw log field from subcriptionid to subscriptionid.  
\- `event.idm.read_only_udm.metadata.event_type`: Updated the conditional check to set `event.idm.read_only_udm.metadata.event_type` to `NETWORK_FLOW` when principal machine data and flow details are present.   
2025-05-20 |  Enhancement:  
\- Modified the conditional statement for `message` to exclude messages that also contain `flowRecords`.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.time` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.flowLogGUID` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.security_result.about.resource.name: Newly mapped `record.flowLogResourceID` raw log field with `event.idm.read_only_udm.security_result.about.resource.name` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `record.flowLogVersion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.principal.mac: Newly mapped `record.macAddress` raw log field with `event.idm.read_only_udm.principal.mac` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record.operationName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `records.flowRecords.flows.aclID` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.flowRecords.flows.flowGroups.rule` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly mapped `record.flowRecords.flows.flowGroups.flowTuples` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2025-02-24 |  Enhancement:  
\- Mapped `properties.primaryIPv4Address` to `principal.ip` and `principal.asset.ip`.  
\- Mapped `properties.macAddress` to `principal.mac`.  
\- Mapped `properties.ruleName` to `security_result.rule_name`.  
\- Mapped `properties.direction`, `properties.conditions.sourcePortRange`, `properties.conditions.destinationPortRange`, `properties_priority` and `properties.type` to `security_result.about.labels`.  
\- Mapped `systemId` to `target.asset_id`.  
\- Mapped `properties_vnetResourceGuid` to `principal.asset_id`.  
\- Mapped `record_resourceId` to `target.resource.product_object_id`.  
\- Mapped `appname` to `target.application`.  
\- Mapped `subcriptionid`, `rscgrp` and `rscname` to `target.resource.attribute.labels`.   
2025-01-16 |  Enhancement:  
\- Changed `match` mapping from `record.time` to `time`.   
2024-11-26 |  Enhancement:  
\- Added support for new format of JSON logs.   
2022-04-18 |  Enhancement:  
\- Added mappings for principal.ip in place of src.ip.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
