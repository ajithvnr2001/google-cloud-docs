---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest
title: Google Cloud Tasks v2 API - Class DeleteQueueRequest (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:03.521400+00:00
---

# Google Cloud Tasks v2 API - Class DeleteQueueRequest (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class DeleteQueueRequest (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class DeleteQueueRequest : IMessage<DeleteQueueRequest>, IEquatable<DeleteQueueRequest>, IDeepCloneable<DeleteQueueRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2 API class DeleteQueueRequest.

Request message for [DeleteQueue][google.cloud.tasks.v2.CloudTasks.DeleteQueue].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteQueueRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Constructors 

### DeleteQueueRequest()
    
    
    public DeleteQueueRequest()

### DeleteQueueRequest(DeleteQueueRequest)
    
    
    public DeleteQueueRequest(DeleteQueueRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

Required. The queue name. For example: `projects/PROJECT_ID/locations/LOCATION_ID/queues/QUEUE_ID`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### QueueName
    
    
    public QueueName QueueName { get; set; }

[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.DeleteQueueRequest#Google_Cloud_Tasks_V2_DeleteQueueRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[QueueName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.QueueName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
