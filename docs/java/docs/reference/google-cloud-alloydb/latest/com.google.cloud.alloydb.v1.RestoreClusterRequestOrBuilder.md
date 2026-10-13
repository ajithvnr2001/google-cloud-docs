---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequestOrBuilder
title: Interface RestoreClusterRequestOrBuilder (0.88.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:16:08.726720+00:00
---

# Interface RestoreClusterRequestOrBuilder (0.88.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RestoreClusterRequestOrBuilder (0.88.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.88.0 (latest)  0.84.0  0.83.0  0.82.0  0.80.0  0.77.0  0.76.0  0.74.0  0.72.0  0.71.0  0.70.0  0.69.0  0.67.0  0.65.0  0.64.0  0.63.0  0.62.0  0.61.0  0.59.0  0.57.0  0.56.0  0.53.0  0.52.0  0.51.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    public interface RestoreClusterRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupSource()
    
    
    public abstract BackupSource getBackupSource()

Backup source.

`.google.cloud.alloydb.v1.BackupSource backup_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BackupSource)` | The backupSource.  
  
### getBackupSourceOrBuilder()
    
    
    public abstract BackupSourceOrBuilder getBackupSourceOrBuilder()

Backup source.

`.google.cloud.alloydb.v1.BackupSource backup_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[BackupSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.BackupSourceOrBuilder)` |   
  
### getCluster()
    
    
    public abstract Cluster getCluster()

Required. The resource being created

`.google.cloud.alloydb.v1.Cluster cluster = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.Cluster)` | The cluster.  
  
### getClusterId()
    
    
    public abstract String getClusterId()

Required. ID of the requesting object.

`string cluster_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The clusterId.  
  
### getClusterIdBytes()
    
    
    public abstract ByteString getClusterIdBytes()

Required. ID of the requesting object.

`string cluster_id = 2 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for clusterId.  
  
### getClusterOrBuilder()
    
    
    public abstract ClusterOrBuilder getClusterOrBuilder()

Required. The resource being created

`.google.cloud.alloydb.v1.Cluster cluster = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[ClusterOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ClusterOrBuilder)` |   
  
### getContinuousBackupSource()
    
    
    public abstract ContinuousBackupSource getContinuousBackupSource()

ContinuousBackup source. Continuous backup needs to be enabled in the source cluster for this operation to succeed.

`.google.cloud.alloydb.v1.ContinuousBackupSource continuous_backup_source = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupSource](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ContinuousBackupSource)` | The continuousBackupSource.  
  
### getContinuousBackupSourceOrBuilder()
    
    
    public abstract ContinuousBackupSourceOrBuilder getContinuousBackupSourceOrBuilder()

ContinuousBackup source. Continuous backup needs to be enabled in the source cluster for this operation to succeed.

`.google.cloud.alloydb.v1.ContinuousBackupSource continuous_backup_source = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ContinuousBackupSourceOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.ContinuousBackupSourceOrBuilder)` |   
  
### getParent()
    
    
    public abstract String getParent()

Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The parent.  
  
### getParentBytes()
    
    
    public abstract ByteString getParentBytes()

Required. The name of the parent resource. For the required format, see the comment on the Cluster.name field.

` string parent = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for parent.  
  
### getRequestId()
    
    
    public abstract String getRequestId()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The requestId.  
  
### getRequestIdBytes()
    
    
    public abstract ByteString getRequestIdBytes()

Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server ignores the request if it has already been completed. The server guarantees that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if the original operation with the same request ID was received, and if so, ignores the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).

`string request_id = 5 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for requestId.  
  
### getSourceCase()
    
    
    public abstract RestoreClusterRequest.SourceCase getSourceCase()

**Returns**  
---  
**Type** | **Description**  
`[RestoreClusterRequest.SourceCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-alloydb/latest/com.google.cloud.alloydb.v1.RestoreClusterRequest.SourceCase)` |   
  
### getValidateOnly()
    
    
    public abstract boolean getValidateOnly()

Optional. If set, performs request validation, for example, permission checks and any other type of validation, but does not actually execute the create request.

`bool validate_only = 6 [(.google.api.field_behavior) = OPTIONAL];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The validateOnly.  
  
### hasBackupSource()
    
    
    public abstract boolean hasBackupSource()

Backup source.

`.google.cloud.alloydb.v1.BackupSource backup_source = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupSource field is set.  
  
### hasCluster()
    
    
    public abstract boolean hasCluster()

Required. The resource being created

`.google.cloud.alloydb.v1.Cluster cluster = 3 [(.google.api.field_behavior) = REQUIRED]; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cluster field is set.  
  
### hasContinuousBackupSource()
    
    
    public abstract boolean hasContinuousBackupSource()

ContinuousBackup source. Continuous backup needs to be enabled in the source cluster for this operation to succeed.

`.google.cloud.alloydb.v1.ContinuousBackupSource continuous_backup_source = 8;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the continuousBackupSource field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
