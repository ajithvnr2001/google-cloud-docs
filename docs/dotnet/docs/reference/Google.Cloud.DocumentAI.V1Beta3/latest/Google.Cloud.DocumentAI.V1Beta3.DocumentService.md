---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService
title: Cloud Document AI v1beta3 API - Class DocumentService (2.0.0-beta30) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:44.922184+00:00
---

# Cloud Document AI v1beta3 API - Class DocumentService (2.0.0-beta30)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Document AI v1beta3 API - Class DocumentService (2.0.0-beta30) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta30 (latest)  2.0.0-beta29  1.0.0-beta04 
    
    
    public static class DocumentService

Reference documentation and code samples for the Cloud Document AI v1beta3 API class DocumentService.

Service to call Cloud DocumentAI to manage document collection (dataset).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DocumentService

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DocumentAI.V1Beta3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3)

## Assembly

Google.Cloud.DocumentAI.V1Beta3.dll

## Methods 

### BindService(DocumentServiceBase)
    
    
    public static ServerServiceDefinition BindService(DocumentService.DocumentServiceBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[DocumentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService)[DocumentServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService.DocumentServiceBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, DocumentServiceBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, DocumentService.DocumentServiceBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[DocumentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService)[DocumentServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DocumentAI.V1Beta3/latest/Google.Cloud.DocumentAI.V1Beta3.DocumentService.DocumentServiceBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-16 UTC."],[],[]] 
