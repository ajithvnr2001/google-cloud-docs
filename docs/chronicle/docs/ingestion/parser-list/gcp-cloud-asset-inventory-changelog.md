---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloud-asset-inventory-changelog/
title: Change log for GCP_CLOUD_ASSET_INVENTORY \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:42:43.479610+00:00
---

# Change log for GCP_CLOUD_ASSET_INVENTORY  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/gcp-cloud-asset-inventory-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for GCP_CLOUD_ASSET_INVENTORY

Date | Changes  
---|---  
2026-05-08 |  \- Newly created parser.  
\- `event.idm.read_only_udm.target.resource.attribute.last_update_time`: Newly mapped `asset.updateTime` raw log field with `event.idm.read_only_udm.target.resource.attribute.last_update_time` UDM field.  
\- `event.idm.read_only_udm.metadata.product_event_type`: Newly mapped `asset.resource.discoveryName` raw log field with `event.idm.read_only_udm.metadata.product_event_type` UDM field.  
\- `event.idm.read_only_udm.metadata.product_version`: Newly mapped `asset.resource.version` raw log field with `event.idm.read_only_udm.metadata.product_version` UDM field.  
\- `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip`: Newly mapped `asset.resource.data.connectionEndpoints.ipAddress`, `priorAsset.resource.data.connectionEndpoints.ipAddress` raw log fields with `event.idm.read_only_udm.principal.ip` and `event.idm.read_only_udm.principal.asset.ip` UDM field.  
\- `event.idm.read_only_udm.target.location.country_or_region`: Newly mapped `asset.resource.location` raw log field with `event.idm.read_only_udm.target.location.country_or_region` UDM field.  
\- `event.idm.read_only_udm.target.url`: Newly mapped `asset.resource.data.selfLink` raw log field with `event.idm.read_only_udm.target.url` UDM field.  
\- `event.idm.read_only_udm.target.resource.name`: Newly mapped `asset.name` raw log field with `event.idm.read_only_udm.target.resource.name` UDM field.  
\- `event.idm.read_only_udm.target.resource.product_object_id`: Newly mapped `priorAsset.resource.data.id` raw log field with `event.idm.read_only_udm.target.resource.product_object_id` UDM field.  
\- `event.idm.read_only_udm.target.resource.resource_subtype`: Newly mapped `priorAsset.resource.discoveryName` raw log field with `event.idm.read_only_udm.target.resource.resource_subtype` UDM field.  
\- `event.idm.read_only_udm.additional.fields`: Newly mapped `priorAssetState`, `asset.resource.data.id`, `priorAsset.resource.data.creationTimestamp`, `priorAsset.updateTime`, and `window.startTime` raw log fields with `event.idm.read_only_udm.additional.fields` UDM field.  
\- `event.idm.read_only_udm.target.resource.attribute.labels`: Newly mapped `asset.resource.data.creationTimestamp`, `asset.resource.data.name`, `asset.assetType`, `asset.resource.data.connectionPreference`, `asset.resource.data.fingerprint`, `asset.resource.data.description`, `asset.resource.discoveryDocumentUri`, `asset.resource.data.network`, `asset.resource.parent`, `asset.resource.data.region`, `asset.ancestors`, `asset.resource.data.subnetworks`, `asset.resource.data.connectionEndpoints`, `priorAsset.resource.data.connectionPreference`, `priorAsset.resource.data.description`, `priorAsset.resource.data.fingerprint`, `priorAsset.resource.data.name`, `priorAsset.resource.data.network`, `priorAsset.resource.discoveryDocumentUri`, `priorAsset.resource.data.selfLink`, `priorAsset.resource.version`, `priorAsset.resource.parent`, `priorAsset.name`, `priorAsset.assetType`, `priorAsset.resource.data.region`, `priorAsset.resource.location`, `priorAsset.ancestors`, `priorAsset.resource.data.subnetworks`, and `priorAsset.resource.data.connectionEndpoints` raw log fields with `event.idm.read_only_udm.target.resource.attribute.labels` UDM field.  
\- `event.idm.read_only_udm.target.resource_ancestors.name`: Newly mapped `priorAsset.resource.parent` raw log field with `event.idm.read_only_udm.target.resource_ancestors.name` UDM field.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `STATUS_UPDATE` when principal machine data is present.  
\- `event.idm.read_only_udm.metadata.event_type`: Newly set `event.idm.read_only_udm.metadata.event_type` to `GENERIC_EVENT` when no principal machine data , target machine data and user data are present.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
