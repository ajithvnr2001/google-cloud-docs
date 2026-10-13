---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequestOrBuilder
title: Interface DeleteNodePoolRequestOrBuilder (2.102.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:42:18.422371+00:00
---

# Interface DeleteNodePoolRequestOrBuilder (2.102.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-container/latest/com.google.container.v1.DeleteNodePoolRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DeleteNodePoolRequestOrBuilder (2.102.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.102.0 (latest)  2.98.0  2.97.0  2.96.0  2.94.0  2.91.0  2.90.0  2.88.0  2.86.0  2.85.0  2.84.0  2.83.0  2.81.0  2.79.0  2.78.0  2.77.0  2.76.0  2.75.0  2.73.0  2.71.0  2.70.0  2.67.0  2.66.0  2.65.0  2.63.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.0  2.56.0  2.55.0  2.54.0  2.52.0  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.2  2.4.1  2.3.8 
    
    
    public interface DeleteNodePoolRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getClusterId() (deprecated)
    
    
    public abstract String getClusterId()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.cluster_id is deprecated. See google/container/v1/cluster_service.proto;l=5046_

Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.

`string cluster_id = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterId.  
  
### getClusterIdBytes() (deprecated)
    
    
    public abstract ByteString getClusterIdBytes()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.cluster_id is deprecated. See google/container/v1/cluster_service.proto;l=5046_

Deprecated. The name of the cluster. This field has been deprecated and replaced by the name field.

`string cluster_id = 3 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterId.  
  
### getName()
    
    
    public abstract String getName()

The name (project, location, cluster, node pool id) of the node pool to delete. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.

`string name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

The name (project, location, cluster, node pool id) of the node pool to delete. Specified in the format `projects/*/locations/*/clusters/*/nodePools/*`.

`string name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getNodePoolId() (deprecated)
    
    
    public abstract String getNodePoolId()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.node_pool_id is deprecated. See google/container/v1/cluster_service.proto;l=5050_

Deprecated. The name of the node pool to delete. This field has been deprecated and replaced by the name field.

`string node_pool_id = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nodePoolId.  
  
### getNodePoolIdBytes() (deprecated)
    
    
    public abstract ByteString getNodePoolIdBytes()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.node_pool_id is deprecated. See google/container/v1/cluster_service.proto;l=5050_

Deprecated. The name of the node pool to delete. This field has been deprecated and replaced by the name field.

`string node_pool_id = 4 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nodePoolId.  
  
### getProjectId() (deprecated)
    
    
    public abstract String getProjectId()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.project_id is deprecated. See google/container/v1/cluster_service.proto;l=5036_

Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.

`string project_id = 1 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The projectId.  
  
### getProjectIdBytes() (deprecated)
    
    
    public abstract ByteString getProjectIdBytes()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.project_id is deprecated. See google/container/v1/cluster_service.proto;l=5036_

Deprecated. The Google Developers Console [project ID or project number](https://cloud.google.com/resource-manager/docs/creating-managing-projects). This field has been deprecated and replaced by the name field.

`string project_id = 1 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for projectId.  
  
### getZone() (deprecated)
    
    
    public abstract String getZone()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.zone is deprecated. See google/container/v1/cluster_service.proto;l=5042_

Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.

`string zone = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The zone.  
  
### getZoneBytes() (deprecated)
    
    
    public abstract ByteString getZoneBytes()

**Deprecated.** _google.container.v1.DeleteNodePoolRequest.zone is deprecated. See google/container/v1/cluster_service.proto;l=5042_

Deprecated. The name of the Google Compute Engine [zone](https://cloud.google.com/compute/docs/zones#available) in which the cluster resides. This field has been deprecated and replaced by the name field.

`string zone = 2 [deprecated = true];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for zone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
