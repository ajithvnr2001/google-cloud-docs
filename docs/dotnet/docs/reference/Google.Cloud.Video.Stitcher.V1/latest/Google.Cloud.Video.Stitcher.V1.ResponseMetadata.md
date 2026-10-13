---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata
title: Video Stitcher v1 API - Class ResponseMetadata (3.4.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:29.163033+00:00
---

# Video Stitcher v1 API - Class ResponseMetadata (3.4.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Video Stitcher v1 API - Class ResponseMetadata (3.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.4.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.3.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.2.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.1.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/3.0.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/2.0.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.1.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/1.0.0/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)


    
    
    public sealed class ResponseMetadata : IMessage<ResponseMetadata>, IEquatable<ResponseMetadata>, IDeepCloneable<ResponseMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Video Stitcher v1 API class ResponseMetadata.

Metadata for the response of an ad request.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ResponseMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ResponseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ResponseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ResponseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Video.Stitcher.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1)

## Assembly

Google.Cloud.Video.Stitcher.V1.dll

## Constructors 

### ResponseMetadata()
    
    
    public ResponseMetadata()

### ResponseMetadata(ResponseMetadata)
    
    
    public ResponseMetadata(ResponseMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ResponseMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Video.Stitcher.V1/latest/Google.Cloud.Video.Stitcher.V1.ResponseMetadata)`  
  
  
## Properties 

### Body
    
    
    public string Body { get; set; }

The body of the response.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Duration
    
    
    public Duration Duration { get; set; }

Total time elapsed for the response.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### Error
    
    
    public string Error { get; set; }

Error message received when making the ad request.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Headers
    
    
    public Struct Headers { get; set; }

Headers from the response.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### SizeBytes
    
    
    public int SizeBytes { get; set; }

Size in bytes of the response.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### StatusCode
    
    
    public string StatusCode { get; set; }

Status code for the response.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
