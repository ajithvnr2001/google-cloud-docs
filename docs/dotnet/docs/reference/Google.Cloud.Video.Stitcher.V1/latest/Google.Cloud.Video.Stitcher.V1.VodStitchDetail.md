---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail
title: Video Stitcher v1 API - Class VodStitchDetail (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:22:11.804840+00:00
---

# Video Stitcher v1 API - Class VodStitchDetail (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Video Stitcher v1 API - Class VodStitchDetail (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.3.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.2.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.1.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.0.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/2.0.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.1.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.0.0/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)


    
    
    public sealed class VodStitchDetail : IMessage<VodStitchDetail>, IEquatable<VodStitchDetail>, IDeepCloneable<VodStitchDetail>, IBufferMessage, IMessage

Reference documentation and code samples for the Video Stitcher v1 API class VodStitchDetail.

Information related to the interstitial of a VOD session. This resource is only available for VOD sessions that do not implement Google Ad Manager ad insertion.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VodStitchDetail

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1)

## Assembly

Google.Cloud.Video.Stitcher.V1.dll

## Constructors 

### VodStitchDetail()
    
    
    public VodStitchDetail()

### VodStitchDetail(VodStitchDetail)
    
    
    public VodStitchDetail(VodStitchDetail other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VodStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail)`  
  
  
## Properties 

### AdStitchDetails
    
    
    public RepeatedField<AdStitchDetail> AdStitchDetails { get; }

A list of ad processing details for the fetched ad playlist.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[AdStitchDetail](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.AdStitchDetail)` |   
  
### Name
    
    
    public string Name { get; set; }

The name of the stitch detail in the specified VOD session, in the form of `projects/{project}/locations/{location}/vodSessions/{vod_session_id}/vodStitchDetails/{id}`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### VodStitchDetailName
    
    
    public VodStitchDetailName VodStitchDetailName { get; set; }

[VodStitchDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetailName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetail#Google_Cloud_Video_Stitcher_V1_VodStitchDetail_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[VodStitchDetailName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.VodStitchDetailName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
