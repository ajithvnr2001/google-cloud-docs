---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplicationOrBuilder
title: Interface DiskAsyncReplicationOrBuilder (1.109.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:39:36.461192+00:00
---

# Interface DiskAsyncReplicationOrBuilder (1.109.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-compute/latest/com.google.cloud.compute.v1.DiskAsyncReplicationOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface DiskAsyncReplicationOrBuilder (1.109.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.109.0 (latest)  1.105.0  1.104.0  1.103.0  1.101.0  1.98.0  1.97.0  1.95.0  1.93.0  1.92.0  1.91.0  1.90.0  1.88.0  1.86.0  1.85.0  1.84.0  1.83.0  1.82.0  1.80.0  1.78.0  1.77.0  1.74.0  1.73.0  1.72.0  1.70.0  1.69.0  1.68.0  1.67.0  1.66.0  1.65.0  1.64.0  1.63.0  1.62.0  1.61.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.50.0  1.49.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.9.1  1.8.1  1.7.2  1.6.0-beta 
    
    
    public interface DiskAsyncReplicationOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConsistencyGroupPolicy()
    
    
    public abstract String getConsistencyGroupPolicy()

Output only. [Output Only] URL of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy = 1991097;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consistencyGroupPolicy.  
  
### getConsistencyGroupPolicyBytes()
    
    
    public abstract ByteString getConsistencyGroupPolicyBytes()

Output only. [Output Only] URL of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy = 1991097;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consistencyGroupPolicy.  
  
### getConsistencyGroupPolicyId()
    
    
    public abstract String getConsistencyGroupPolicyId()

Output only. [Output Only] ID of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy_id = 261065057;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The consistencyGroupPolicyId.  
  
### getConsistencyGroupPolicyIdBytes()
    
    
    public abstract ByteString getConsistencyGroupPolicyIdBytes()

Output only. [Output Only] ID of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy_id = 261065057;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for consistencyGroupPolicyId.  
  
### getDisk()
    
    
    public abstract String getDisk()

The other disk asynchronously replicated to or from the current disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:

  * <https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk>
  * projects/project/zones/zone/disks/disk
  * zones/zone/disks/disk



`optional string disk = 3083677;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The disk.  
  
### getDiskBytes()
    
    
    public abstract ByteString getDiskBytes()

The other disk asynchronously replicated to or from the current disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:

  * <https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk>
  * projects/project/zones/zone/disks/disk
  * zones/zone/disks/disk



`optional string disk = 3083677;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for disk.  
  
### getDiskId()
    
    
    public abstract String getDiskId()

Output only. [Output Only] The unique ID of the other disk asynchronously replicated to or from the current disk. This value identifies the exact disk that was used to create this replication. For example, if you started replicating the persistent disk from a disk that was later deleted and recreated under the same name, the disk ID would identify the exact version of the disk that was used.

`optional string disk_id = 60990205;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The diskId.  
  
### getDiskIdBytes()
    
    
    public abstract ByteString getDiskIdBytes()

Output only. [Output Only] The unique ID of the other disk asynchronously replicated to or from the current disk. This value identifies the exact disk that was used to create this replication. For example, if you started replicating the persistent disk from a disk that was later deleted and recreated under the same name, the disk ID would identify the exact version of the disk that was used.

`optional string disk_id = 60990205;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for diskId.  
  
### hasConsistencyGroupPolicy()
    
    
    public abstract boolean hasConsistencyGroupPolicy()

Output only. [Output Only] URL of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy = 1991097;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the consistencyGroupPolicy field is set.  
  
### hasConsistencyGroupPolicyId()
    
    
    public abstract boolean hasConsistencyGroupPolicyId()

Output only. [Output Only] ID of the DiskConsistencyGroupPolicy if replication was started on the disk as a member of a group.

`optional string consistency_group_policy_id = 261065057;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the consistencyGroupPolicyId field is set.  
  
### hasDisk()
    
    
    public abstract boolean hasDisk()

The other disk asynchronously replicated to or from the current disk. You can provide this as a partial or full URL to the resource. For example, the following are valid values:

  * <https://www.googleapis.com/compute/v1/projects/project/zones/zone/disks/disk>
  * projects/project/zones/zone/disks/disk
  * zones/zone/disks/disk



`optional string disk = 3083677;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the disk field is set.  
  
### hasDiskId()
    
    
    public abstract boolean hasDiskId()

Output only. [Output Only] The unique ID of the other disk asynchronously replicated to or from the current disk. This value identifies the exact disk that was used to create this replication. For example, if you started replicating the persistent disk from a disk that was later deleted and recreated under the same name, the disk ID would identify the exact version of the disk that was used.

`optional string disk_id = 60990205;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the diskId field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
