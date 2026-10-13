---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient.StreamSanitizeUserPromptStream
title: Model Armor v1beta API - Class ModelArmorClient.StreamSanitizeUserPromptStream (1.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:04.578025+00:00
---

# Model Armor v1beta API - Class ModelArmorClient.StreamSanitizeUserPromptStream (1.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient.StreamSanitizeUserPromptStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Model Armor v1beta API - Class ModelArmorClient.StreamSanitizeUserPromptStream (1.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta06 (latest)  1.0.0-beta05 
    
    
    public abstract class ModelArmorClient.StreamSanitizeUserPromptStream : BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>, IDisposable

Reference documentation and code samples for the Model Armor v1beta API class ModelArmorClient.StreamSanitizeUserPromptStream.

Bidirectional streaming methods for [StreamSanitizeUserPrompt(CallSettings, BidirectionalStreamingSettings)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.ModelArmorClient#Google_Cloud_ModelArmor_V1Beta_ModelArmorClient_StreamSanitizeUserPrompt_Google_Api_Gax_Grpc_CallSettings_Google_Api_Gax_Grpc_BidirectionalStreamingSettings_).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > [BidirectionalStreamingBase](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html)[SanitizeUserPromptRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptRequest)[SanitizeUserPromptResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta.SanitizeUserPromptResponse) > ModelArmorClient.StreamSanitizeUserPromptStream

## Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

## Inherited Members

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.TryWriteAsync(SanitizeUserPromptRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.WriteAsync(SanitizeUserPromptRequest)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.TryWriteAsync(SanitizeUserPromptRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.WriteAsync(SanitizeUserPromptRequest, WriteOptions)](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteAsync__0_Grpc_Core_WriteOptions_)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.TryWriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_TryWriteCompleteAsync)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.WriteCompleteAsync()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_WriteCompleteAsync)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.GetResponseStream()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GetResponseStream)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.Dispose()](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_Dispose)

[BidirectionalStreamingBase<SanitizeUserPromptRequest, SanitizeUserPromptResponse>.GrpcCall](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.BidirectionalStreamingBase-2.html#Google_Api_Gax_Grpc_BidirectionalStreamingBase_2_GrpcCall)

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ModelArmor.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ModelArmor.V1Beta/latest/Google.Cloud.ModelArmor.V1Beta)

## Assembly

Google.Cloud.ModelArmor.V1Beta.dll

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-05 UTC."],[],[]] 
