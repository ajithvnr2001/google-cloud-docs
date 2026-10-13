---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest
title: Video Stitcher v1 API - Class CreateLiveSessionRequest (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:58.391535+00:00
---

# Video Stitcher v1 API - Class CreateLiveSessionRequest (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Video Stitcher v1 API - Class CreateLiveSessionRequest (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.3.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.2.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.1.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.0.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/2.0.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.1.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.0.0/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)


    
    
    public sealed class CreateLiveSessionRequest : IMessage<CreateLiveSessionRequest>, IEquatable<CreateLiveSessionRequest>, IDeepCloneable<CreateLiveSessionRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Video Stitcher v1 API class CreateLiveSessionRequest.

Request message for VideoStitcherService.createLiveSession.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateLiveSessionRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1)

## Assembly

Google.Cloud.Video.Stitcher.V1.dll

## Constructors 

### CreateLiveSessionRequest()
    
    
    public CreateLiveSessionRequest()

### CreateLiveSessionRequest(CreateLiveSessionRequest)
    
    
    public CreateLiveSessionRequest(CreateLiveSessionRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateLiveSessionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest)`  
  
  
## Properties 

### LiveSession
    
    
    public LiveSession LiveSession { get; set; }

Required. Parameters for creating a live session.

**Property Value**  
---  
**Type** | **Description**  
`[LiveSession](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.LiveSession)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The project and location in which the live session should be created, in the form of `projects/{project_number}/locations/{location}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsLocationName
    
    
    public LocationName ParentAsLocationName { get; set; }

[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.CreateLiveSessionRequest#Google_Cloud_Video_Stitcher_V1_CreateLiveSessionRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
