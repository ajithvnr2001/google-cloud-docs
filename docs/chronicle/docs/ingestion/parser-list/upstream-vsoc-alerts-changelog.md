---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upstream-vsoc-alerts-changelog/
title: Change log for UPSTREAM_VSOC_ALERTS \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:29:33.515101+00:00
---

# Change log for UPSTREAM_VSOC_ALERTS  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/upstream-vsoc-alerts-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for UPSTREAM_VSOC_ALERTS

Date | Changes  
---|---  
2025-09-02 |  Enhancement:  
\- A new grok filter was added to handle different formats of the incoming message field-  
\- For messages that both start and end with a colon(:).  
\- For messages that only end with a colon(:).  
\- For messages that only start with a colon(:).  
\- event.idm.read_only_udm.metadata.product_log_id: Newly mapped `record.recordId` raw log field(s) with `event.idm.read_only_udm.metadata.product_log_id` UDM field.  
\- event.idm.read_only_udm.principal.asset_id: Newly mapped `record.assetType`, `record.assetId.value` raw log field(s) with `event.idm.read_only_udm.principal.asset_id` UDM field.  
\- event.idm.read_only_udm.principal.application: Newly mapped `record.serviceName` raw log field(s) with `event.idm.read_only_udm.principal.application` UDM field.  
\- event.idm.read_only_udm.security_result.rule_name: Newly mapped `record.detectorName` raw log field(s) with `event.idm.read_only_udm.security_result.rule_name` UDM field.  
\- event.idm.read_only_udm.security_result.rule_type: Newly mapped `record.detectorType` raw log field(s) with `event.idm.read_only_udm.security_result.rule_type` UDM field.  
\- event.idm.read_only_udm.metadata.log_type: Newly mapped `record.name` raw log field(s) with `event.idm.read_only_udm.metadata.log_type` UDM field.  
\- event.idm.read_only_udm.metadata.product_event_type: Newly mapped `record.name` raw log field(s) with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- event.idm.read_only_udm.metadata.description: Newly mapped `record.description` raw log field(s) with `event.idm.read_only_udm.metadata.description` UDM field.  
\- event.idm.read_only_udm.security_result.severity_details: Newly mapped `record.severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity_details` UDM field.  
\- event.idm.read_only_udm.about.investigation.status: Newly mapped `record.status` raw log field(s) with `event.idm.read_only_udm.about.investigation.status` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.latitude: Newly mapped `record.location.coordinates.1` raw log field(s) with `event.idm.read_only_udm.principal.location.region_coordinates.latitude` UDM field.  
\- event.idm.read_only_udm.principal.location.region_coordinates.longitude: Newly mapped `record.location.coordinates.0` raw log field(s) with `event.idm.read_only_udm.principal.location.region_coordinates.longitude` UDM field.  
\- event.idm.read_only_udm.metadata.event_timestamp: Newly mapped `record.createdAt` raw log field(s) with `event.idm.read_only_udm.metadata.event_timestamp` UDM field.  
\- event.idm.read_only_udm.metadata.ingested_timestamp: Newly mapped `record.processedAt` raw log field(s) with `event.idm.read_only_udm.metadata.ingested_timestamp` UDM field.  
\- event.idm.read_only_udm.security_result.rule_id: Newly mapped `record.detectorId` raw log field(s) with `event.idm.read_only_udm.security_result.rule_id` UDM field.  
\- event.idm.read_only_udm.principal.process.pid: Newly mapped `record.serviceId` raw log field(s) with `event.idm.read_only_udm.principal.process.pid` UDM field.  
\- event.idm.read_only_udm.metadata.product_version: Newly mapped `record.apiVersion` raw log field(s) with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- event.idm.read_only_udm.metadata.url_back_to_product: Newly mapped `record.url` raw log field(s) with `event.idm.read_only_udm.metadata.url_back_to_product` UDM field.  
\- event.idm.read_only_udm.security_result.severity: Newly mapped `severity`, `record.severity` raw log field(s) with `event.idm.read_only_udm.security_result.severity` UDM field.  
\- event.idm.read_only_udm.network.http.method: Newly mapped `record.endpointDetails.method` raw log field(s) with `event.idm.read_only_udm.network.http.method` UDM field.  
\- event.idm.read_only_udm.principal.asset.first_discover_time: Newly mapped `record.firstOccurrence` raw log field(s) with `event.idm.read_only_udm.principal.asset.first_discover_time` UDM field.  
\- event.idm.read_only_udm.principal.asset.last_discover_time: Newly mapped `record.lastOccurrence` raw log field(s) with `event.idm.read_only_udm.principal.asset.last_discover_time` UDM field.  
\- event.idm.read_only_udm.principal.asset.system_last_update_time: Newly mapped `record.updatedAt` raw log field(s) with `event.idm.read_only_udm.principal.asset.system_last_update_time` UDM field.  
\- event.idm.read_only_udm.additional.fields: Newly mapped `record.id`, `record.location.type`, `record.endpointDetails.url`, `record.endpointDetails.host`, `record.endpointDetails.path`, `record.endpointDetails.apiTitle`, `record.endpointDetails.contact`, `record.endpointDetails.description`, `record.endpointDetails.updatedAt`, `record.additionalSignals.name`, `record.additionalSignals.value`, `record.additionalSignals.type`, `record.additionalSignals.source`, `affectedAssets`, `record.affectedAssets` raw log field(s) with `event.idm.read_only_udm.additional.fields` UDM field.  
\- event.idm.read_only_udm.principal.asset.attribute.labels: Newly mapped `vehicleModel`, `record.vehicleModel`, `record.shortVin`, `shortVin`, `record.location.coordinates.2`, `location.coordinates.2` raw log field(s) with `event.idm.read_only_udm.principal.asset.attribute.labels` UDM field.   
2024-10-24 |  \- Newly created parser.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
