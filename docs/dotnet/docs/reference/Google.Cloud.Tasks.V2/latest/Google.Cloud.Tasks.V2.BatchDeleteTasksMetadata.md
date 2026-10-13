---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata
title: Google Cloud Tasks v2 API - Class BatchDeleteTasksMetadata (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:33.634054+00:00
---

# Google Cloud Tasks v2 API - Class BatchDeleteTasksMetadata (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class BatchDeleteTasksMetadata (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class BatchDeleteTasksMetadata : IMessage<BatchDeleteTasksMetadata>, IEquatable<BatchDeleteTasksMetadata>, IDeepCloneable<BatchDeleteTasksMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2 API class BatchDeleteTasksMetadata.

Metadata for the long-running operation returned by [BatchDeleteTasks][google.cloud.tasks.v2.CloudTasks.BatchDeleteTasks]. This message is used to hold metadata information about the batch delete tasks operation; that is, it is put in [google.longrunning.Operation.metadata][google.longrunning.Operation.metadata].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BatchDeleteTasksMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Constructors 

### BatchDeleteTasksMetadata()
    
    
    public BatchDeleteTasksMetadata()

### BatchDeleteTasksMetadata(BatchDeleteTasksMetadata)
    
    
    public BatchDeleteTasksMetadata(BatchDeleteTasksMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)`  
  
  
## Properties 

### EndTime
    
    
    public Timestamp EndTime { get; set; }

Output only. The time when the batch delete finished.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### FailedRequests
    
    
    public MapField<int, Status> FailedRequests { get; }

Output only. A map of failed requests, where the key is the index of the request in BatchDeleteTasksRequest.names and the value is the error status.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[int](https://learn.microsoft.com/dotnet/api/system.int32)[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
### StartTime
    
    
    public Timestamp StartTime { get; set; }

Output only. The time when the batch delete started.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### State
    
    
    public BatchDeleteTasksMetadata.Types.State State { get; set; }

Output only. The state of the batch delete operation.

**Property Value**  
---  
**Type** | **Description**  
`[BatchDeleteTasksMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.BatchDeleteTasksMetadata.Types.State)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
