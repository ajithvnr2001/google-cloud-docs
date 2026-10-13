---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest
title: Google Cloud Tasks v2 API - Class CreateQueueRequest (3.7.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:31.667633+00:00
---

# Google Cloud Tasks v2 API - Class CreateQueueRequest (3.7.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Tasks v2 API - Class CreateQueueRequest (3.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.7.0 (latest)  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CreateQueueRequest : IMessage<CreateQueueRequest>, IEquatable<CreateQueueRequest>, IDeepCloneable<CreateQueueRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Tasks v2 API class CreateQueueRequest.

Request message for [CreateQueue][google.cloud.tasks.v2.CloudTasks.CreateQueue].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateQueueRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Tasks.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2)

## Assembly

Google.Cloud.Tasks.V2.dll

## Constructors 

### CreateQueueRequest()
    
    
    public CreateQueueRequest()

### CreateQueueRequest(CreateQueueRequest)
    
    
    public CreateQueueRequest(CreateQueueRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateQueueRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest)`  
  
  
## Properties 

### Parent
    
    
    public string Parent { get; set; }

Required. The location name in which the queue will be created. For example: `projects/PROJECT_ID/locations/LOCATION_ID`

The list of allowed locations can be obtained by calling Cloud Tasks' implementation of [ListLocations][google.cloud.location.Locations.ListLocations].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.CreateQueueRequest#Google_Cloud_Tasks_V2_CreateQueueRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
### Queue
    
    
    public Queue Queue { get; set; }

Required. The queue to create.

[Queue's name][google.cloud.tasks.v2.Queue.name] cannot be the same as an existing queue.

**Property Value**  
---  
**Type** | **Description**  
`[Queue](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Tasks.V2/latest/Google.Cloud.Tasks.V2.Queue)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-29 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-29 UTC."],[],[]] 
