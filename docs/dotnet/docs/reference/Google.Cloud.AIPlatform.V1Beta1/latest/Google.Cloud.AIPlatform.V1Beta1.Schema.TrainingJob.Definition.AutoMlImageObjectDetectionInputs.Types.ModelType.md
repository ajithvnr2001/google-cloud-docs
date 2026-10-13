---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types.ModelType
title: Vertex AI v1beta1 API - Enum AutoMlImageObjectDetectionInputs.Types.ModelType (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:29:38.613550+00:00
---

# Vertex AI v1beta1 API - Enum AutoMlImageObjectDetectionInputs.Types.ModelType (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition.AutoMlImageObjectDetectionInputs.Types.ModelType

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Enum AutoMlImageObjectDetectionInputs.Types.ModelType (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public enum AutoMlImageObjectDetectionInputs.Types.ModelType

## Namespace

[Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schema.TrainingJob.Definition)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Fields   
  
---  
**Name** | **Description**  
`CloudHighAccuracy1` | A model best tailored to be used within Google Cloud, and which cannot be exported. Expected to have a higher latency, but should also have a higher prediction quality than other cloud models.  
`CloudLowLatency1` | A model best tailored to be used within Google Cloud, and which cannot be exported. Expected to have a low latency, but may have lower prediction quality than other cloud models.  
`MobileTfHighAccuracy1` | A model that, in addition to being available within Google Cloud, can also be exported (see ModelService.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have a higher latency, but should also have a higher prediction quality than other mobile models.  
`MobileTfLowLatency1` | A model that, in addition to being available within Google Cloud can also be exported (see ModelService.ExportModel) and used on a mobile or edge device with TensorFlow afterwards. Expected to have low latency, but may have lower prediction quality than other mobile models.  
`MobileTfVersatile1` | A model that, in addition to being available within Google Cloud can also be exported (see ModelService.ExportModel) and used on a mobile or edge device with TensorFlow afterwards.  
`Unspecified` | Should not be set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
