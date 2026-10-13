---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService
title: Analytics Hub v1beta1 API - Class AnalyticsHubService (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:37.345083+00:00
---

# Analytics Hub v1beta1 API - Class AnalyticsHubService (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Analytics Hub v1beta1 API - Class AnalyticsHubService (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/2.0.0-beta06/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)
  * [ 1.0.0-beta01 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/1.0.0-beta01/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)


    
    
    public static class AnalyticsHubService

Reference documentation and code samples for the Analytics Hub v1beta1 API class AnalyticsHubService.

The `AnalyticsHubService` API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AnalyticsHubService

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BigQuery.DataExchange.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1)

## Assembly

Google.Cloud.BigQuery.DataExchange.V1Beta1.dll

## Methods 

### BindService(AnalyticsHubServiceBase)
    
    
    public static ServerServiceDefinition BindService(AnalyticsHubService.AnalyticsHubServiceBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[AnalyticsHubService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)[AnalyticsHubServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, AnalyticsHubServiceBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, AnalyticsHubService.AnalyticsHubServiceBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[AnalyticsHubService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService)[AnalyticsHubServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BigQuery.DataExchange.V1Beta1/latest/Google.Cloud.BigQuery.DataExchange.V1Beta1.AnalyticsHubService.AnalyticsHubServiceBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
