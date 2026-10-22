---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-flow-changelog/
title: Change log for OCI_FLOW \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:51:39.295741+00:00
---

# Change log for OCI_FLOW  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/oci-flow-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OCI_FLOW

Date | Changes  
---|---  
2026-06-22 |  Enhancement:  
\- Removed invalid GENERIC events by updating the parsing logic for nested json raw logs.  
\- `event.idm.read_only_udm.security_result.action`: Mapped `action` field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: When principal machine data and user data are present updated `event.idm.read_only_udm.metadata.event_type` to `USER_UNCATEGORIZED`.   
2026-06-18 |  Enhancement:  
\- `event.idm.read_only_udm.principal.resource.attribute.cloud.environment`: Removed mapping `UNSPECIFIED_CLOUD_ENVIRONMENT` as it is not a valid enum value for `event.idm.read_only_udm.principal.resource.attribute.cloud.environment` UDM field.  
\- `event.idm.read_only_udm.security_result.action`: Newly mapped `action` raw log field with `event.idm.read_only_udm.security_result.action` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`:  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `NETWORK_CONNECTION` when both principal and target machine data are present.  
\- Set the `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when only principal machine data is present.  
\- `event.idm.read_only_udm.network.sent_bytes`: Newly mapped `bytesOut` raw log field with `event.idm.read_only_udm.network.sent_bytes` UDM field.  
\- `event.idm.read_only_udm.network.sent_packets`: Newly mapped `packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM field.  
\- `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip`: Newly mapped `destinationAddress` raw log field with `event.idm.read_only_udm.target.ip` and `event.idm.read_only_udm.target.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.target.port`: Newly mapped `destinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `sourceAddress` raw log field with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM fields.  
\- `event.idm.read_only_udm.principal.port`: Newly mapped `sourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM field.  
\- `event.idm.read_only_udm.principal.resource.product_object_id`: Newly mapped `flowid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.network.ip_protocol`: Newly mapped `protocol` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM field.  
\- `event.idm.read_only_udm.security_result.detection_fields`: Newly mapped `endTime`, `startTime`, `status`, `version` raw log fields with `event.idm.read_only_udm.security_result.detection_fields` UDM field.   
2026-06-04 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- `event.idm.read_only_udm.additional.fields`: Newly Mapped `oracle_managed`, `oracle_filtercid`, `oracle_instancecid` and `oracle_vcnOcid` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.observer.resource.resource_subtype`: Newly Mapped `resource_type` raw log field with `event.idm.read_only_udm.observer.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.observer.resource.attribute.labels`: Newly Mapped `resource_id` raw log field with `event.idm.read_only_udm.observer.resource.attribute.labels` UDM field.   
2025-08-05 |  Enhancement:  
\- Added support for new pattern of JSON logs.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `record_sourcetype` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `event_flow_id` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `oracle_filtercid` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `oracle_instancecid` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `oracle_loggroupid` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `data_protocol` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `oracle_tenantid` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.security_result.detection_fields: Newly Mapped `oracle_numPktsUnmatchedV4` raw log field with `event.idm.read_only_udm.security_result.detection_fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `event_data_version` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `event_data_endTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.additional.fields: Newly Mapped `event_data_startTime` raw log field with `event.idm.read_only_udm.additional.fields` UDM Field.  
\- event.idm.read_only_udm.principal.resource.product_object_id: Newly Mapped `oracle_vnicocid` raw log field with `event.idm.read_only_udm.principal.resource.product_object_id` UDM Field.  
\- event.idm.read_only_udm.metadata.product_log_id : Newly Mapped `event_id` raw log field with `event.idm.read_only_udm.metadata.product_log_id` UDM Field.  
\- event.idm.read_only_udm.metadata.event_timstamp : Newly Mapped `event_timestamp` raw log field with `event.idm.read_only_udm.metadata.event_timstamp` UDM Field.  
\- event.idm.read_only_udm.observer.resource.product_object_id: Newly Mapped `oracle_logid` raw log field with `event.idm.read_only_udm.observer.resource.product_object_id` UDM Field.  
\- event.idm.read_only_udm.metadata.product_version: Newly Mapped `event_specversion` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM Field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly Mapped `event_type` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM Field.  
\- event.idm.read_only_udm.security_result.action_details: Newly Mapped `event_data_status` raw log field with `event.idm.read_only_udm.security_result.action_details` UDM Field.  
\- event.idm.read_only_udm.principal.namespace: Newly Mapped `oracle_compartmentid` raw log field with `event.idm.read_only_udm.principal.namespace` UDM Field.  
\- event.idm.read_only_udm.target.resource.product_object_id: Newly Mapped `oracle_vniccompartmentocid` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM Field.  
\- event.idm.read_only_udm.principal.resource.attribute.labels: Newly Mapped `oracle_vnicsubnetocid` raw log field with `event.idm.read_only_udm.principal.resource.attribute.labels` UDM Field.  
\- event.idm.read_only_udm.metadata.ingested_timestamp: Newly Mapped `oracle_ingestedtime` raw log field with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM Field.  
\- event.idm.read_only_udm.principal.ip: Newly Mapped `data_sourceAddress` raw log field with `event.idm.read_only_udm.principal.ip` UDM Field.  
\- event.idm.read_only_udm.principal.asset.ip: Newly Mapped `data_sourceAddress` raw log field with `event.idm.read_only_udm.principal.asset.ip` UDM Field.  
\- event.idm.read_only_udm.target.ip: Newly Mapped `data_destinationAddress` raw log field with `event.idm.read_only_udm.target.ip` UDM Field.  
\- event.idm.read_only_udm.target.asset.ip: Newly Mapped `data_destinationAddress` raw log field with `event.idm.read_only_udm.target.asset.ip` UDM Field.  
\- event.idm.read_only_udm.target.port: Newly Mapped `data_destinationPort` raw log field with `event.idm.read_only_udm.target.port` UDM Field.  
\- event.idm.read_only_udm.principal.port: Newly Mapped `data_sourcePort` raw log field with `event.idm.read_only_udm.principal.port` UDM Field.  
\- event.idm.read_only_udm.network.ip_protocol: Newly Mapped `data_protocolName` raw log field with `event.idm.read_only_udm.network.ip_protocol` UDM Field.  
\- event.idm.read_only_udm.network.sent_packets: Newly Mapped `data_packets` raw log field with `event.idm.read_only_udm.network.sent_packets` UDM Field.  
\- event.idm.read_only_udm.network.received_packets: Newly Mapped `data_bytesOut` raw log field with `event.idm.read_only_udm.network.received_packets` UDM Field.   
2024-09-15 |  Enhancement:  
\- Added support for new pattern of JSON logs.   
2023-04-29 |  Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
