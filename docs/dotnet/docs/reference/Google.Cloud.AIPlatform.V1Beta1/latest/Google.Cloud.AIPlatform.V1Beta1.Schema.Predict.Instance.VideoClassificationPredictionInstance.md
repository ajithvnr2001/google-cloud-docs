---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance
title: Vertex AI v1beta1 API - Class VideoClassificationPredictionInstance (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:20.318208+00:00
---

# Vertex AI v1beta1 API - Class VideoClassificationPredictionInstance (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class VideoClassificationPredictionInstance (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public sealed class VideoClassificationPredictionInstance : IMessage<VideoClassificationPredictionInstance>, IEquatable<VideoClassificationPredictionInstance>, IDeepCloneable<VideoClassificationPredictionInstance>, IBufferMessage, IMessage

Reference documentation and code samples for the Vertex AI v1beta1 API class VideoClassificationPredictionInstance.

Prediction input format for Video Classification.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > VideoClassificationPredictionInstance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[VideoClassificationPredictionInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[VideoClassificationPredictionInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[VideoClassificationPredictionInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Constructors 

### VideoClassificationPredictionInstance()
    
    
    public VideoClassificationPredictionInstance()

### VideoClassificationPredictionInstance(VideoClassificationPredictionInstance)
    
    
    public VideoClassificationPredictionInstance(VideoClassificationPredictionInstance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[VideoClassificationPredictionInstance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.Predict.Instance.VideoClassificationPredictionInstance)`  
  
  
## Properties 

### Content
    
    
    public string Content { get; set; }

The Google Cloud Storage location of the video on which to perform the prediction.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MimeType
    
    
    public string MimeType { get; set; }

The MIME type of the content of the video. Only the following are supported: video/mp4 video/avi video/quicktime

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeSegmentEnd
    
    
    public string TimeSegmentEnd { get; set; }

The end, exclusive, of the video's time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with "s" appended at the end. Fractions are allowed, up to a microsecond precision, and "inf" or "Infinity" is allowed, which means the end of the video.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TimeSegmentStart
    
    
    public string TimeSegmentStart { get; set; }

The beginning, inclusive, of the video's time segment on which to perform the prediction. Expressed as a number of seconds as measured from the start of the video, with "s" appended at the end. Fractions are allowed, up to a microsecond precision.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
