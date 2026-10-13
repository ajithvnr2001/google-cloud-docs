---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest
title: Google Cloud Bigtable Administration v2 API - Class DeleteSnapshotRequest (3.36.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:57:27.445503+00:00
---

# Google Cloud Bigtable Administration v2 API - Class DeleteSnapshotRequest (3.36.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Bigtable Administration v2 API - Class DeleteSnapshotRequest (3.36.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.36.0 (latest)  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0 
    
    
    public sealed class DeleteSnapshotRequest : IMessage<DeleteSnapshotRequest>, IEquatable<DeleteSnapshotRequest>, IDeepCloneable<DeleteSnapshotRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Bigtable Administration v2 API class DeleteSnapshotRequest.

Request message for [google.bigtable.admin.v2.BigtableTableAdmin.DeleteSnapshot][google.bigtable.admin.v2.BigtableTableAdmin.DeleteSnapshot]

Note: This is a private alpha release of Cloud Bigtable snapshots. This feature is not currently available to most Cloud Bigtable customers. This feature might be changed in backward-incompatible ways and is not recommended for production use. It is not subject to any SLA or deprecation policy.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteSnapshotRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.Admin.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2)

## Assembly

Google.Cloud.Bigtable.Admin.V2.dll

## Constructors 

### DeleteSnapshotRequest()
    
    
    public DeleteSnapshotRequest()

### DeleteSnapshotRequest(DeleteSnapshotRequest)
    
    
    public DeleteSnapshotRequest(DeleteSnapshotRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteSnapshotRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The unique name of the snapshot to be deleted. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/snapshots/{snapshot}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SnapshotName
    
    
    public SnapshotName SnapshotName { get; set; }

[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.SnapshotName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.DeleteSnapshotRequest#Google_Cloud_Bigtable_Admin_V2_DeleteSnapshotRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[SnapshotName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.Admin.V2/latest/Google.Cloud.Bigtable.Admin.V2.SnapshotName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
