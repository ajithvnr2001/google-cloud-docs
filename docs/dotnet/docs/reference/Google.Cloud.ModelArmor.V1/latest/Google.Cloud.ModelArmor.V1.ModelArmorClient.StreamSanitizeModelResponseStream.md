---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.StreamSanitizeModelResponseStream
title: Model Armor v1 API - Class ModelArmorClient.StreamSanitizeModelResponseStream (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:16:44.899120+00:00
---

# Model Armor v1 API - Class ModelArmorClient.StreamSanitizeModelResponseStream (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient.StreamSanitizeModelResponseStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1 API - Class ModelArmorClient.StreamSanitizeModelResponseStream (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta07 
    
    
    public abstract class ModelArmorClient.StreamSanitizeModelResponseStream : BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>, IDisposable

Reference documentation and code samples for the Model Armor v1 API class ModelArmorClient.StreamSanitizeModelResponseStream.

Bidirectional streaming methods for [StreamSanitizeModelResponse(CallSettings, BidirectionalStreamingSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.ModelArmorClient#Google_Cloud_ModelArmor_V1_ModelArmorClient_StreamSanitizeModelResponse_Google_Api_Gax_Grpc_CallSettings_Google_Api_Gax_Grpc_BidirectionalStreamingSettings_).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [BidirectionalStreamingBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html)[SanitizeModelResponseRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.SanitizeModelResponseRequest)[SanitizeModelResponseResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1.SanitizeModelResponseResponse) > ModelArmorClient.StreamSanitizeModelResponseStream

## Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## Inherited Members

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.TryWriteAsync(SanitizeModelResponseRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.WriteAsync(SanitizeModelResponseRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.TryWriteAsync(SanitizeModelResponseRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.WriteAsync(SanitizeModelResponseRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.TryWriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteCompleteAsync)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.WriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteCompleteAsync)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.GetResponseStream()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GetResponseStream)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.Dispose()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_Dispose)

[BidirectionalStreamingBase<SanitizeModelResponseRequest, SanitizeModelResponseResponse>.GrpcCall](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GrpcCall)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1/latest/Google.Cloud.ModelArmor.V1)

## Assembly

Google.Cloud.ModelArmor.V1.dll

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
