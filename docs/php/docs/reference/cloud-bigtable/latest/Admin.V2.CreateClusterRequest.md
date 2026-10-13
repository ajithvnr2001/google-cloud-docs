---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateClusterRequest
title: Cloud Bigtable V2 Client - Class CreateClusterRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:13:47.136118+00:00
---

# Cloud Bigtable V2 Client - Class CreateClusterRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateClusterRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class CreateClusterRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class CreateClusterRequest.

Request message for BigtableInstanceAdmin.CreateCluster.

Generated from protobuf message `google.bigtable.admin.v2.CreateClusterRequest`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The unique name of the instance in which to create the new cluster. Values are of the form `projects/{project}/instances/{instance}`.  
`↳ cluster_id` |  `string`   
Required. The ID to be used when referring to the new cluster within its instance, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.  
`↳ cluster` |  `[Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)`   
Required. The cluster to be created. Fields marked `OutputOnly` must be left blank.  
  
### getParent

Required. The unique name of the instance in which to create the new cluster. Values are of the form `projects/{project}/instances/{instance}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The unique name of the instance in which to create the new cluster. Values are of the form `projects/{project}/instances/{instance}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClusterId

Required. The ID to be used when referring to the new cluster within its instance, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setClusterId

Required. The ID to be used when referring to the new cluster within its instance, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCluster

Required. The cluster to be created.

Fields marked `OutputOnly` must be left blank.

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)|null` |   
  
### hasCluster

### clearCluster

### setCluster

Required. The cluster to be created.

Fields marked `OutputOnly` must be left blank.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. The unique name of the instance in which to create the new cluster. Values are of the form `projects/{project}/instances/{instance}`. Please see BigtableInstanceAdminClient::instanceName() for help formatting this field.  
`clusterId` |  `string`   
Required. The ID to be used when referring to the new cluster within its instance, e.g., just `mycluster` rather than `projects/myproject/instances/myinstance/clusters/mycluster`.  
`cluster` |  `[Cluster](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster)`   
Required. The cluster to be created. Fields marked `OutputOnly` must be left blank.  
**Returns**  
---  
**Type** | **Description**  
`[CreateClusterRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.CreateClusterRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
