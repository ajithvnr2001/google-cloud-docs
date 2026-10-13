---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail
title: Video Stitcher v1 API - Class VodAdTagDetail (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:15.949233+00:00
---

# Video Stitcher v1 API - Class VodAdTagDetail (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Video Stitcher v1 API - Class VodAdTagDetail (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.3.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.2.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.1.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.0.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/2.0.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.1.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.0.0/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)


    
    
    public sealed class VodAdTagDetail : IMessage<VodAdTagDetail>, IEquatable<VodAdTagDetail>, IDeepCloneable<VodAdTagDetail>, IBufferMessage, IMessage

Reference documentation and code samples for the Video Stitcher v1 API class VodAdTagDetail.

Information related to the details for one ad tag. This resource is only available for VOD sessions that do not implement Google Ad Manager ad insertion.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VodAdTagDetail

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1)

## Assembly

Google.Cloud.Video.Stitcher.V1.dll

## Constructors 

### VodAdTagDetail()
    
    
    public VodAdTagDetail()

### VodAdTagDetail(VodAdTagDetail)
    
    
    public VodAdTagDetail(VodAdTagDetail other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VodAdTagDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail)`  
  
  
## Properties 

### AdRequests
    
    
    public RepeatedField<AdRequest> AdRequests { get; }

A list of ad requests for one ad tag.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdRequest)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the ad tag detail for the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodAdTagDetails/{id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VodAdTagDetailName
    
    
    public VodAdTagDetailName VodAdTagDetailName { get; set; }

[VodAdTagDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetailName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetail#Google_Cloud_Video_Stitcher_V1_VodAdTagDetail_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[VodAdTagDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodAdTagDetailName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
