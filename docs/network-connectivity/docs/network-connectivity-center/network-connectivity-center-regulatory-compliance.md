---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/network-connectivity-center-regulatory-compliance/
title: Regulatory support in Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:55:42.727165+00:00
---

# Regulatory support in Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/network-connectivity-center-regulatory-compliance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Resources ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/resources)



Send feedback 

#  Regulatory support in Network Connectivity Center Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the features, configurations and APIs in Network Connectivity Center that align with the controls for supported control packages. This document assumes that you're using [Assured Workloads](https://docs.cloud.google.com/assured-workloads/docs/overview).

Show AllData Boundary for ITAR  
  
---  
  
## Data Boundary for ITAR

### Supported services

The following table lists the Network Connectivity Center APIs and versions that meet the requirements of Data Boundary for ITAR. | Service | Version | Status  
---|---|---  
networkconnectivity.googleapis.com | v1 |  SUPPORTED   
networkconnectivity.googleapis.com | v1alpha1 |  SUPPORTED   
networkconnectivity.googleapis.com | v1beta |  SUPPORTED   
  
### Fields not intended for Sensitive data

The following table provides an illustrative list of field categories and specific fields that aren't suitable for sensitive information. To maintain compliance, avoid placing protected data in these fields. For a complete list, contact your Google Cloud representative.

Category | Fields  
---|---  
Advanced spoke settings | 

  * `spoke.gateway.customLearnedIpRanges.range`
  * `spoke.gateway.services.linkedSseGateway.sseGatewayUri`
  * `spoke.linkedInterconnectAttachments.excludeExportRanges`
  * `spoke.linkedProducerVpcNetwork.peering`
  * `spoke.linkedRouterApplianceInstances.instances.virtualMachine`
  * `spoke.linkedVpnTunnels.includeExportRanges`

  
Configuration updates | 

  * `updateMask.paths`

  
Description and naming | 

  * `gatewayAdvertisedRoute.description`
  * `gatewayAdvertisedRoute.name`
  * `group.description`
  * `group.name`
  * `hub.description`
  * `hub.name`

  
Filtering and sorting | 

  * `filter`
  * `orderBy`

  
Label management | 

  * `gatewayAdvertisedRoute.labels.key`
  * `gatewayAdvertisedRoute.labels.value`
  * `group.labels.key`
  * `group.labels.value`
  * `hub.labels.key`
  * `hub.labels.value`

  
Network specifics | 

  * `spoke.gateway.landingNetwork.network`
  * `spoke.linkedInterconnectAttachments.uris`
  * `spoke.linkedProducerVpcNetwork.network`
  * `spoke.linkedVpcNetwork.uri`
  * `spoke.linkedVpnTunnels.uris`

  
Pagination | 

  * `pageToken`

  
Request context | 

  * `requestId`

  
Resource identification | 

  * `gatewayAdvertisedRouteId`
  * `groupId`
  * `hubId`
  * `name`
  * `parent`
  * `spokeId`

  
Route configuration | 

  * `gatewayAdvertisedRoute.ipRange`
  * `spoke.gateway.ipRangeReservations.ipRange`
  * `spoke.linkedInterconnectAttachments.includeImportRanges`
  * `spoke.linkedRouterApplianceInstances.excludeExportRanges`
  * `spoke.linkedVpcNetwork.includeExportRanges`
  * `spoke.linkedVpnTunnels.excludeImportRanges`

  
  
  
  
## What's next

  * Learn more about [compliance in Google Cloud](https://cloud.google.com/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
