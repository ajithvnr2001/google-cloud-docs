---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.UpdateClusterRequestOrBuilder
title: Interface UpdateClusterRequestOrBuilder (0.19.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:48:08.645010+00:00
---

# Interface UpdateClusterRequestOrBuilder (0.19.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.UpdateClusterRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface UpdateClusterRequestOrBuilder (0.19.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.19.0 (latest)  0.15.0  0.14.0  0.13.0  0.11.0  0.8.0  0.7.0  0.5.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface UpdateClusterRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCluster()
    
    
    public abstract Cluster getCluster()

Required. Cluster to update.

` .google.cloud.hypercomputecluster.v1beta.Cluster cluster = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.Cluster)` | The cluster.  
  
### getClusterOrBuilder()
    
    
    public abstract ClusterOrBuilder getClusterOrBuilder()

Required. Cluster to update.

` .google.cloud.hypercomputecluster.v1beta.Cluster cluster = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-hypercomputecluster/latest/com.google.cloud.hypercomputecluster.v1beta.ClusterOrBuilder)` |   
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. A unique identifier for this request. A random UUID is recommended. This request is idempotent if and only if `request_id` is provided.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. A unique identifier for this request. A random UUID is recommended. This request is idempotent if and only if `request_id` is provided.

` string request_id = 3 [(.google.api.field_behavior) = OPTIONAL, (.google.api.field_info) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getUpdateMask()
    
    
    public abstract FieldMask getUpdateMask()

Optional. Mask specifying which fields in the cluster to update. All paths must be specified explicitly - wildcards are not supported. At least one path must be provided.

`.google.protobuf.FieldMask update_mask = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMask](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html)` | The updateMask.  
  
### getUpdateMaskOrBuilder()
    
    
    public abstract FieldMaskOrBuilder getUpdateMaskOrBuilder()

Optional. Mask specifying which fields in the cluster to update. All paths must be specified explicitly - wildcards are not supported. At least one path must be provided.

`.google.protobuf.FieldMask update_mask = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[FieldMaskOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMaskOrBuilder.html)` |   
  
### hasCluster()
    
    
    public abstract boolean hasCluster()

Required. Cluster to update.

` .google.cloud.hypercomputecluster.v1beta.Cluster cluster = 2 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cluster field is set.  
  
### hasUpdateMask()
    
    
    public abstract boolean hasUpdateMask()

Optional. Mask specifying which fields in the cluster to update. All paths must be specified explicitly - wildcards are not supported. At least one path must be provided.

`.google.protobuf.FieldMask update_mask = 1 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the updateMask field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
