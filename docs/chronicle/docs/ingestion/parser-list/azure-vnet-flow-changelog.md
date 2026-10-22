---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-vnet-flow-changelog/
title: Change log for AZURE_VNET_FLOW \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:33:55.524683+00:00
---

# Change log for AZURE_VNET_FLOW  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/azure-vnet-flow-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for AZURE_VNET_FLOW

Date | Changes  
---|---  
2025-07-18 |  \- `event.idm.read_only_udm.intermediary.hostname`: Newly mapped `flow_log_name` (extracted from `record_flowLogResourceID`) raw log field with `event.idm.read_only_udm.intermediary.hostname` UDM field.   
2025-07-03 |  \- Added support to parse the unparsed logs.   
2025-06-28 |  \- Added for loop for flowTuples.  
\- Added CSV filter to `flowtuple` and retrieved `timestamp`, `src_ip`, `dst_ip`, `src_port`, `dst_port`, `network_protocol`, `network_direction`, `Connection_Unencrypted`, `flow_state`, `sentpackets`, `receivedpackets`, `sentbytes`, and `receivedbytes`.  
\- `event.idm.read_only_udm.network.received_bytes`: Newly mapped `receivedbytes` raw log field with `event.idm.read_only_udm.network.received_bytes` UDM field.  
\- `event.idm.read_only_udm.network.received_packets`: Newly mapped `receivedpackets` raw log field with `event.idm.read_only_udm.network.received_packets` UDM field.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `sentbytes` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `sentpackets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- If `network_direction` is `I`, then set `event.idm.read_only_udm.network.direction` to `INBOUND`.  
\- If `network_direction` is `O`, then set `event.idm.read_only_udm.network.direction` to `OUTBOUND`.  
\- `event.idm.read_only_udm.network.direction`: Newly mapped `network_direction` raw log field with `event.idm.read_only_udm.network.direction` UDM field.  
\- If `network_protocol` is `6`, then set `event.idm.read_only_udm.network.ip_protocol` to `TCP`.  
\- If `network_protocol` is `17`, then set `event.idm.read_only_udm.network.ip_protocol` to `UDP`.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `network_protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- If `Connection_Unencrypted` is `X`, then set `Connection_Unencrypted` to `encrypted`.  
\- If `Connection_Unencrypted` is `NX`, then set `Connection_Unencrypted` to `unencrypted`.  
\- If `Connection_Unencrypted` is `NX_HW_NOT_SUPPORTED`, then set `Connection_Unencrypted` to `Hardware is unsupported`.  
\- If `Connection_Unencrypted` is `NX_SW_NOT_READY`, then set `Connection_Unencrypted` to `Software isn't ready`.  
\- If `Connection_Unencrypted` is `NX_NOT_ACCEPTED`, then set `Connection_Unencrypted` to `Drop due to no encryption`.  
\- If `Connection_Unencrypted` is `NX_NOT_SUPPORTED`, then set `Connection_Unencrypted` to `Discovery is unsupported`.  
\- If `Connection_Unencrypted` is `NX_LOCAL_DST`, then set `Connection_Unencrypted` to `Destination is on the same host`.  
\- If `Connection_Unencrypted` is `NX_FALLBACK`, then set `Connection_Unencrypted` to `Fall back to no encryption`.  
\- If `flow_state` is `B`, then set `flow_state` to `Begin`.  
\- If `flow_state` is `C`, then set `flow_state` to `Continue`.  
\- If `flow_state` is `E`, then set `flow_state` to `End`.  
\- If `flow_state` is `D`, then set `flow_state` to `Deny`.  
\- If `flow_state` is `Deny`, then set `security_result_action` to `BLOCK`.  
\- If `flow_state` is `Continue`, then set `security_result_action` to `ALLOW`.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `flow_state`, `Connection_Unencrypted` raw log field with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Removed mapping of `record.time` from `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- `event.idm.read_only_udm.metadata.event_timestamp`: Mapped `timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timestamp` UDM field   
2025-06-19 |  \- Newly created parser for CBN- AZURE_VNET_FLOW.  
\- event1.idm.read_only_udm.metadata.product_log_id: Newly mapped `record_flowLogGUID` raw log field with `event1.idm.read_only_udm.metadata.product_log_id` UDM field  
\- event1.idm.read_only_udm.metadata.product_version: Newly mapped `record_flowLogVersion` raw log field with `event1.idm.read_only_udm.metadata.product_version` UDM field  
\- event1.idm.read_only_udm.metadata.product_event_type: Newly mapped `record_operationName` raw log field with `event1.idm.read_only_udm.metadata.product_event_type` UDM field  
\- event1.idm.read_only_udm.principal.ip: Newly mapped `src_ip` raw log field with `event1.idm.read_only_udm.principal.ip' UDM field  
\- event1.idm.read_only_udm.principal.asset.ip: Newly mapped `src_ip` raw log field with `event1.idm.read_only_udm.principal.asset.ip' UDM field  
\- event1.idm.read_only_udm.principal.mac: Newly mapped `record_macAddress` raw log field with `event1.idm.read_only_udm.principal.mac' UDM field  
\- event1.idm.read_only_udm.principal.asset.mac: Newly mapped `record_macAddress` raw log field with `event1.idm.read_only_udm.principal.asset.mac' UDM field  
\- event1.idm.read_only_udm.principal.port: Newly mapped `src_port` raw log field with `event1.idm.read_only_udm.principal.port' UDM field  
\- event1.idm.read_only_udm.target.ip: Newly mapped `dst_ip` raw log field with `event1.idm.read_only_udm.target.ip' UDM field  
\- event1.idm.read_only_udm.target.asset.ip: Newly mapped `dst_ip` raw log field with `event1.idm.read_only_udm.target.asset.ip' UDM field  
\- event1.idm.read_only_udm.target.port: Newly mapped `dst_port` raw log field with `event1.idm.read_only_udm.target.port' UDM field  
\- event1.idm.read_only_udm.target.application: Newly mapped `appname` raw log field with `event1.idm.read_only_udm.target.application' UDM field  
\- event1.idm.read_only_udm.target.resource.product_object_id: Newly mapped `record_targetResourceID` raw log field with `event1.idm.read_only_udm.target.resource.product_object_id` UDM field  
\- event1.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `virtualNetworks` raw log field with `event1.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `SubscriptionId` raw log field with `event1.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.target.resource.attribute.labels: Newly mapped `resourceGroups` raw log field with `event1.idm.read_only_udm.target.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `NETWORKWATCHERS` raw log field with `event1.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `SubscriptionId` raw log field with `event1.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `ResourceGroup` raw log field with `event1.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.security_result.about.resource.attribute.labels: Newly mapped `FLOWLOGS` raw log field with `event1.idm.read_only_udm.security_result.about.resource.attribute.labels` UDM field  
\- event1.idm.read_only_udm.security_result.detection_fields: Newly mapped `flow.aclID` raw log field with `event1.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event1.idm.read_only_udm.security_result.detection_fields: Newly mapped `flowGroup.rule` raw log field with `event1.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event1.idm.read_only_udm.security_result.detection_fields: Newly mapped `flowTuple` raw log field with `event1.idm.read_only_udm.security_result.detection_fields` UDM field  
\- event1.idm.read_only_udm.security_result.about.resource.name: Newly mapped `record_flowLogResourceID` raw log field with `event1.idm.read_only_udm.security_result.about.resource.name` UDM field  
\- event1.idm.read_only_udm.security_result.rule_type: Newly mapped `record_category` raw log field with `event1.idm.read_only_udm.security_result.rule_type` UDM field   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
