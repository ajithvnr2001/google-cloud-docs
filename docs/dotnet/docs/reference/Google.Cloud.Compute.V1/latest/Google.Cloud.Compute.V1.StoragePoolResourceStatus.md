---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus
title: Compute Engine v1 API - Class StoragePoolResourceStatus (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:34:03.850248+00:00
---

# Compute Engine v1 API - Class StoragePoolResourceStatus (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class StoragePoolResourceStatus (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public sealed class StoragePoolResourceStatus : IMessage<StoragePoolResourceStatus>, IEquatable<StoragePoolResourceStatus>, IDeepCloneable<StoragePoolResourceStatus>, IBufferMessage, IMessage

Reference documentation and code samples for the Compute Engine v1 API class StoragePoolResourceStatus.

[Output Only] Contains output only fields.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StoragePoolResourceStatus

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StoragePoolResourceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StoragePoolResourceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StoragePoolResourceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Compute.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1)

## Assembly

Google.Cloud.Compute.V1.dll

## Constructors 

### StoragePoolResourceStatus()
    
    
    public StoragePoolResourceStatus()

### StoragePoolResourceStatus(StoragePoolResourceStatus)
    
    
    public StoragePoolResourceStatus(StoragePoolResourceStatus other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StoragePoolResourceStatus](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolResourceStatus)`  
  
  
## Properties 

### DiskCount
    
    
    public long DiskCount { get; set; }

[Output Only] Number of disks used.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ExapoolMaxReadIops
    
    
    public long ExapoolMaxReadIops { get; set; }

Output only. [Output Only] Maximum allowed read IOPS for this Exapool.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ExapoolMaxReadThroughput
    
    
    public long ExapoolMaxReadThroughput { get; set; }

Output only. [Output Only] Maximum allowed read throughput in MiB/s for this Exapool.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ExapoolMaxWriteIops
    
    
    public long ExapoolMaxWriteIops { get; set; }

Output only. [Output Only] Maximum allowed write IOPS for this Exapool.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ExapoolMaxWriteThroughput
    
    
    public long ExapoolMaxWriteThroughput { get; set; }

Output only. [Output Only] Maximum allowed write throughput in MiB/s for this Exapool.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### HasDiskCount
    
    
    public bool HasDiskCount { get; }

Gets whether the "disk_count" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExapoolMaxReadIops
    
    
    public bool HasExapoolMaxReadIops { get; }

Gets whether the "exapool_max_read_iops" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExapoolMaxReadThroughput
    
    
    public bool HasExapoolMaxReadThroughput { get; }

Gets whether the "exapool_max_read_throughput" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExapoolMaxWriteIops
    
    
    public bool HasExapoolMaxWriteIops { get; }

Gets whether the "exapool_max_write_iops" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasExapoolMaxWriteThroughput
    
    
    public bool HasExapoolMaxWriteThroughput { get; }

Gets whether the "exapool_max_write_throughput" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasLastResizeTimestamp
    
    
    public bool HasLastResizeTimestamp { get; }

Gets whether the "last_resize_timestamp" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasMaxTotalProvisionedDiskCapacityGb
    
    
    public bool HasMaxTotalProvisionedDiskCapacityGb { get; }

Gets whether the "max_total_provisioned_disk_capacity_gb" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPoolUsedCapacityBytes
    
    
    public bool HasPoolUsedCapacityBytes { get; }

Gets whether the "pool_used_capacity_bytes" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPoolUsedIops
    
    
    public bool HasPoolUsedIops { get; }

Gets whether the "pool_used_iops" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPoolUsedThroughput
    
    
    public bool HasPoolUsedThroughput { get; }

Gets whether the "pool_used_throughput" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasPoolUserWrittenBytes
    
    
    public bool HasPoolUserWrittenBytes { get; }

Gets whether the "pool_user_written_bytes" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTotalProvisionedDiskCapacityGb
    
    
    public bool HasTotalProvisionedDiskCapacityGb { get; }

Gets whether the "total_provisioned_disk_capacity_gb" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTotalProvisionedDiskIops
    
    
    public bool HasTotalProvisionedDiskIops { get; }

Gets whether the "total_provisioned_disk_iops" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTotalProvisionedDiskThroughput
    
    
    public bool HasTotalProvisionedDiskThroughput { get; }

Gets whether the "total_provisioned_disk_throughput" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### LastResizeTimestamp
    
    
    public string LastResizeTimestamp { get; set; }

Output only. [Output Only] Timestamp of the last successful resize inRFC3339 text format.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaxTotalProvisionedDiskCapacityGb
    
    
    public long MaxTotalProvisionedDiskCapacityGb { get; set; }

[Output Only] Maximum allowed aggregate disk size in GiB.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### PoolUsedCapacityBytes
    
    
    public long PoolUsedCapacityBytes { get; set; }

[Output Only] Space used by data stored in disks within the storage pool (in bytes). This will reflect the total number of bytes written to the disks in the pool, in contrast to the capacity of those disks.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### PoolUsedIops
    
    
    public long PoolUsedIops { get; set; }

[Output Only] Sum of all the disks' provisioned IOPS, minus some amount that is allowed per disk that is not counted towards pool's IOPS capacity. For more information, see <https://cloud.google.com/compute/docs/disks/storage-pools>.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### PoolUsedThroughput
    
    
    public long PoolUsedThroughput { get; set; }

[Output Only] Sum of all the disks' provisioned throughput in MiB/s.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### PoolUserWrittenBytes
    
    
    public long PoolUserWrittenBytes { get; set; }

[Output Only] Amount of data written into the pool, before it is compacted.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TotalProvisionedDiskCapacityGb
    
    
    public long TotalProvisionedDiskCapacityGb { get; set; }

[Output Only] Sum of all the disks' provisioned capacity (in GiB) in this storage pool. A disk's provisioned capacity is the same as its total capacity.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TotalProvisionedDiskIops
    
    
    public long TotalProvisionedDiskIops { get; set; }

[Output Only] Sum of all the disks' provisioned IOPS.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### TotalProvisionedDiskThroughput
    
    
    public long TotalProvisionedDiskThroughput { get; set; }

[Output Only] Sum of all the disks' provisioned throughput in MiB/s, minus some amount that is allowed per disk that is not counted towards pool's throughput capacity.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
