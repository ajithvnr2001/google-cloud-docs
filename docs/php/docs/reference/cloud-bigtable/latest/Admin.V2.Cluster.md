---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster
title: Cloud Bigtable V2 Client - Class Cluster (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:36.631896+00:00
---

# Cloud Bigtable V2 Client - Class Cluster (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class Cluster (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class Cluster.

A resizable group of nodes in a particular cloud location, capable of serving all [Tables](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Table) in the parent [Instance](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Instance).

Generated from protobuf message `google.bigtable.admin.v2.Cluster`

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
`↳ name` |  `string`   
The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`.  
`↳ location` |  `string`   
Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.  
`↳ state` |  `int`   
Output only. The current state of the cluster.  
`↳ serve_nodes` |  `int`   
The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.  
`↳ node_scaling_factor` |  `int`   
Immutable. The node scaling factor of this cluster.  
`↳ cluster_config` |  `[Cluster\ClusterConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.ClusterConfig)`   
Configuration for this cluster.  
`↳ default_storage_type` |  `int`   
Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.  
`↳ encryption_config` |  `[Cluster\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.EncryptionConfig)`   
Immutable. The encryption configuration for CMEK-protected clusters.  
  
### getName

The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the cluster. Values are of the form `projects/{project}/instances/{instance}/clusters/[a-z][-a-z0-9]*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLocation

Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setLocation

Immutable. The location where this cluster's nodes and storage reside. For best performance, clients should be located as close as possible to this cluster. Currently only zones are supported, so values should be of the form `projects/{project}/locations/{zone}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the cluster.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.State).  
  
### setState

Output only. The current state of the cluster.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getServeNodes

The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setServeNodes

The number of nodes in the cluster. If no value is set, Cloud Bigtable automatically allocates nodes based on your data footprint and optimized for 50% storage utilization.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNodeScalingFactor

Immutable. The node scaling factor of this cluster.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [NodeScalingFactor](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.NodeScalingFactor).  
  
### setNodeScalingFactor

Immutable. The node scaling factor of this cluster.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [NodeScalingFactor](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.NodeScalingFactor).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getClusterConfig

Configuration for this cluster.

**Returns**  
---  
**Type** | **Description**  
`[Cluster\ClusterConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.ClusterConfig)|null` |   
  
### hasClusterConfig

### setClusterConfig

Configuration for this cluster.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Cluster\ClusterConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.ClusterConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDefaultStorageType

Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [StorageType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.StorageType).  
  
### setDefaultStorageType

Immutable. The type of storage used by this cluster to serve its parent instance's tables, unless explicitly overridden.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [StorageType](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.StorageType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionConfig

Immutable. The encryption configuration for CMEK-protected clusters.

**Returns**  
---  
**Type** | **Description**  
`[Cluster\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.EncryptionConfig)|null` |   
  
### hasEncryptionConfig

### clearEncryptionConfig

### setEncryptionConfig

Immutable. The encryption configuration for CMEK-protected clusters.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Cluster\EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Cluster.EncryptionConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConfig

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
