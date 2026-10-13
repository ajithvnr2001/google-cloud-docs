---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest
title: Dataflow v1beta3 API - Class ListSnapshotsRequest (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:18.674411+00:00
---

# Dataflow v1beta3 API - Class ListSnapshotsRequest (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dataflow v1beta3 API - Class ListSnapshotsRequest (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta03 
    
    
    public sealed class ListSnapshotsRequest : IMessage<ListSnapshotsRequest>, IEquatable<ListSnapshotsRequest>, IDeepCloneable<ListSnapshotsRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Dataflow v1beta3 API class ListSnapshotsRequest.

Request to list snapshots.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ListSnapshotsRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataflow.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3)

## Assembly

Google.Cloud.Dataflow.V1Beta3.dll

## Constructors 

### ListSnapshotsRequest()
    
    
    public ListSnapshotsRequest()

### ListSnapshotsRequest(ListSnapshotsRequest)
    
    
    public ListSnapshotsRequest(ListSnapshotsRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ListSnapshotsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataflow.V1Beta3/latest/Google.Cloud.Dataflow.V1Beta3.ListSnapshotsRequest)`  
  
  
## Properties 

### JobId
    
    
    public string JobId { get; set; }

If specified, list snapshots created from this job.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Location
    
    
    public string Location { get; set; }

The location to list snapshots in.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectId
    
    
    public string ProjectId { get; set; }

The project ID to list snapshots for.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
