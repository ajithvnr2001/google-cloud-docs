---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService
title: Cloud Dataplex v1 API - Class ContentService (3.15.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:21:44.663020+00:00
---

# Cloud Dataplex v1 API - Class ContentService (3.15.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Dataplex v1 API - Class ContentService (3.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.15.0 (latest)  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public static class ContentService

Reference documentation and code samples for the Cloud Dataplex v1 API class ContentService.

ContentService manages Notebook and SQL Scripts for Dataplex Universal Catalog.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ContentService

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Dataplex.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1)

## Assembly

Google.Cloud.Dataplex.V1.dll

## Methods 

### BindService(ContentServiceBase)
    
    
    public static ServerServiceDefinition BindService(ContentService.ContentServiceBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[ContentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService)[ContentServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService.ContentServiceBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, ContentServiceBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, ContentService.ContentServiceBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[ContentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService)[ContentServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dataplex.V1/latest/Google.Cloud.Dataplex.V1.ContentService.ContentServiceBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
