---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny
title: Cloud Bigtable V2 Client - Class MultiClusterRoutingUseAny (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:32.637168+00:00
---

# Cloud Bigtable V2 Client - Class MultiClusterRoutingUseAny (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class MultiClusterRoutingUseAny (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class MultiClusterRoutingUseAny.

Read/write requests are routed to the nearest cluster in the instance, and will fail over to the nearest cluster that is available in the event of transient errors or delays. Clusters in a region are considered equidistant. Choosing this option sacrifices read-your-writes consistency to improve availability.

Generated from protobuf message `google.bigtable.admin.v2.AppProfile.MultiClusterRoutingUseAny`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2 \ AppProfile

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ cluster_ids` |  `string[]`   
The set of clusters to route to. The order is ignored; clusters will be tried in order of distance. If left empty, all clusters are eligible.  
`↳ row_affinity` |  `[MultiClusterRoutingUseAny\RowAffinity](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny.RowAffinity)`   
Row affinity sticky routing based on the row key of the request. Requests that span multiple rows are routed non-deterministically.  
  
### getClusterIds

The set of clusters to route to. The order is ignored; clusters will be tried in order of distance. If left empty, all clusters are eligible.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<string>` |   
  
### setClusterIds

The set of clusters to route to. The order is ignored; clusters will be tried in order of distance. If left empty, all clusters are eligible.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRowAffinity

Row affinity sticky routing based on the row key of the request.

Requests that span multiple rows are routed non-deterministically.

**Returns**  
---  
**Type** | **Description**  
`[MultiClusterRoutingUseAny\RowAffinity](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny.RowAffinity)|null` |   
  
### hasRowAffinity

### setRowAffinity

Row affinity sticky routing based on the row key of the request.

Requests that span multiple rows are routed non-deterministically.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MultiClusterRoutingUseAny\RowAffinity](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AppProfile.MultiClusterRoutingUseAny.RowAffinity)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAffinity

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
