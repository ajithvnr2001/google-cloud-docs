---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech
title: Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech (2.0.0-beta18) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:43.847587+00:00
---

# Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech (2.0.0-beta18)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Text-to-Speech v1beta1 API - Class TextToSpeech (2.0.0-beta18) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta18 (latest)  2.0.0-beta17  1.0.0-beta04 
    
    
    public static class TextToSpeech

Reference documentation and code samples for the Google Cloud Text-to-Speech v1beta1 API class TextToSpeech.

Service that implements Google Cloud Text-to-Speech API.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TextToSpeech

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.TextToSpeech.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1)

## Assembly

Google.Cloud.TextToSpeech.V1Beta1.dll

## Methods 

### BindService(TextToSpeechBase)
    
    
    public static ServerServiceDefinition BindService(TextToSpeech.TextToSpeechBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[TextToSpeech](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech)[TextToSpeechBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech.TextToSpeechBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, TextToSpeechBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, TextToSpeech.TextToSpeechBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[TextToSpeech](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech)[TextToSpeechBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.TextToSpeech.V1Beta1/latest/Google.Cloud.TextToSpeech.V1Beta1.TextToSpeech.TextToSpeechBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
