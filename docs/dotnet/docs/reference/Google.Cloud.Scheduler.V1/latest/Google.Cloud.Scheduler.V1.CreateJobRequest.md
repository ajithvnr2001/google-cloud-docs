---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest
title: Google Cloud Scheduler v1 API - Class CreateJobRequest (3.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:26.840387+00:00
---

# Google Cloud Scheduler v1 API - Class CreateJobRequest (3.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Scheduler v1 API - Class CreateJobRequest (3.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.5.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.4.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.3.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.2.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.1.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/3.0.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/2.3.0/Google.Cloud.Scheduler.V1.CreateJobRequest)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/2.2.0/Google.Cloud.Scheduler.V1.CreateJobRequest)


    
    
    public sealed class CreateJobRequest : IMessage<CreateJobRequest>, IEquatable<CreateJobRequest>, IDeepCloneable<CreateJobRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Scheduler v1 API class CreateJobRequest.

Request message for [CreateJob][google.cloud.scheduler.v1.CloudScheduler.CreateJob].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateJobRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Scheduler.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1)

## Assembly

Google.Cloud.Scheduler.V1.dll

## Constructors 

### CreateJobRequest()
    
    
    public CreateJobRequest()

### CreateJobRequest(CreateJobRequest)
    
    
    public CreateJobRequest(CreateJobRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateJobRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest)`  
  
  
## Properties 

### Job
    
    
    public Job Job { get; set; }

Required. The job to add. The user can optionally specify a name for the job in [name][google.cloud.scheduler.v1.Job.name]. [name][google.cloud.scheduler.v1.Job.name] cannot be the same as an existing job. If a name is not specified then the system will generate a random unique name that will be returned ([name][google.cloud.scheduler.v1.Job.name]) in the response.

**Property Value**  
---  
**Type** | **Description**  
`[Job](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.Job)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The location name. For example: `projects/PROJECT_ID/locations/LOCATION_ID`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Scheduler.V1/latest/Google.Cloud.Scheduler.V1.CreateJobRequest#Google_Cloud_Scheduler_V1_CreateJobRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
