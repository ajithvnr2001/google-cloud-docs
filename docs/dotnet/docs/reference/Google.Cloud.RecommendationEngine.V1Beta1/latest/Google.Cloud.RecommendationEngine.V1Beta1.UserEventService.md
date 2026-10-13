---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService
title: Recommendations AI v1beta1 API - Class UserEventService (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:30.796334+00:00
---

# Recommendations AI v1beta1 API - Class UserEventService (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Recommendations AI v1beta1 API - Class UserEventService (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/2.0.0-beta06/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService)
  * [ 1.0.0-beta03 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/1.0.0-beta03/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService)


    
    
    public static class UserEventService

Reference documentation and code samples for the Recommendations AI v1beta1 API class UserEventService.

Service for ingesting end user actions on the customer website.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > UserEventService

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.RecommendationEngine.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1)

## Assembly

Google.Cloud.RecommendationEngine.V1Beta1.dll

## Methods 

### BindService(UserEventServiceBase)
    
    
    public static ServerServiceDefinition BindService(UserEventService.UserEventServiceBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[UserEventService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService)[UserEventServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService.UserEventServiceBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, UserEventServiceBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, UserEventService.UserEventServiceBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[UserEventService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService)[UserEventServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.RecommendationEngine.V1Beta1/latest/Google.Cloud.RecommendationEngine.V1Beta1.UserEventService.UserEventServiceBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
