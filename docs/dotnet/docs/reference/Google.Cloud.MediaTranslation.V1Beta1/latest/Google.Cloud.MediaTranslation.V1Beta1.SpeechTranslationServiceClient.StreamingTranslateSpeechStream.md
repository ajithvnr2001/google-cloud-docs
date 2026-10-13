---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient.StreamingTranslateSpeechStream
title: Media Translation v1beta1 API - Class SpeechTranslationServiceClient.StreamingTranslateSpeechStream (2.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:46:23.452302+00:00
---

# Media Translation v1beta1 API - Class SpeechTranslationServiceClient.StreamingTranslateSpeechStream (2.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient.StreamingTranslateSpeechStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Media Translation v1beta1 API - Class SpeechTranslationServiceClient.StreamingTranslateSpeechStream (2.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient.StreamingTranslateSpeechStream)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/2.0.0-beta05/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient.StreamingTranslateSpeechStream)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/1.0.0-beta03/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient.StreamingTranslateSpeechStream)


    
    
    public abstract class SpeechTranslationServiceClient.StreamingTranslateSpeechStream : BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>, IDisposable

Reference documentation and code samples for the Media Translation v1beta1 API class SpeechTranslationServiceClient.StreamingTranslateSpeechStream.

Bidirectional streaming methods for [StreamingTranslateSpeech(CallSettings, BidirectionalStreamingSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.SpeechTranslationServiceClient#Google_Cloud_MediaTranslation_V1Beta1_SpeechTranslationServiceClient_StreamingTranslateSpeech_Google_Api_Gax_Grpc_CallSettings_Google_Api_Gax_Grpc_BidirectionalStreamingSettings_).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [BidirectionalStreamingBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html)[StreamingTranslateSpeechRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.StreamingTranslateSpeechRequest)[StreamingTranslateSpeechResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1.StreamingTranslateSpeechResponse) > SpeechTranslationServiceClient.StreamingTranslateSpeechStream

## Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## Inherited Members

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.TryWriteAsync(StreamingTranslateSpeechRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.WriteAsync(StreamingTranslateSpeechRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.TryWriteAsync(StreamingTranslateSpeechRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.WriteAsync(StreamingTranslateSpeechRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.TryWriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteCompleteAsync)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.WriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteCompleteAsync)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.GetResponseStream()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GetResponseStream)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.Dispose()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_Dispose)

[BidirectionalStreamingBase<StreamingTranslateSpeechRequest, StreamingTranslateSpeechResponse>.GrpcCall](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GrpcCall)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.MediaTranslation.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.MediaTranslation.V1Beta1/latest/Google.Cloud.MediaTranslation.V1Beta1)

## Assembly

Google.Cloud.MediaTranslation.V1Beta1.dll

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
