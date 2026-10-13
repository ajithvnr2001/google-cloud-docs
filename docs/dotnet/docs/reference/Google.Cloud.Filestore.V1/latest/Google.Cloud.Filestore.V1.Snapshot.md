---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot
title: Cloud Filestore v1 API - Class Snapshot (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:58.297064+00:00
---

# Cloud Filestore v1 API - Class Snapshot (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Filestore v1 API - Class Snapshot (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.7.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.6.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.5.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.4.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.3.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.2.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.1.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.0.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.2.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.1.0/Google.Cloud.Filestore.V1.Snapshot)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.0.0/Google.Cloud.Filestore.V1.Snapshot)


    
    
    public sealed class Snapshot : IMessage<Snapshot>, IEquatable<Snapshot>, IDeepCloneable<Snapshot>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Filestore v1 API class Snapshot.

A Filestore snapshot.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Snapshot

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Filestore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1)

## Assembly

Google.Cloud.Filestore.V1.dll

## Constructors 

### Snapshot()
    
    
    public Snapshot()

### Snapshot(Snapshot)
    
    
    public Snapshot(Snapshot other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time when the snapshot was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Description
    
    
    public string Description { get; set; }

A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### FilesystemUsedBytes
    
    
    public long FilesystemUsedBytes { get; set; }

Output only. The amount of bytes needed to allocate a full copy of the snapshot content

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Resource labels to represent user provided metadata.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name of the snapshot, in the format `projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SnapshotName
    
    
    public SnapshotName SnapshotName { get; set; }

[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.SnapshotName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot#Google_Cloud_Filestore_V1_Snapshot_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.SnapshotName)` |   
  
### State
    
    
    public Snapshot.Types.State State { get; set; }

Output only. The snapshot state.

**Property Value**  
---  
**Type** | **Description**  
`[Snapshot](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.Snapshot.Types.State)` |   
  
### Tags
    
    
    public MapField<string, string> Tags { get; }

Optional. Input only. Immutable. Tag key-value pairs bound to this resource. Each key must be a namespaced name and each value a short name. Example: "123456789012/environment" : "production", "123456789013/costCenter" : "marketing" See the documentation for more information:

  * Namespaced name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_key>
  * Short name: <https://cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#retrieving_tag_value>



**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
