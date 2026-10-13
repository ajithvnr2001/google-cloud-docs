---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService
title: Apigee Connect v1 API - Class ConnectionService (2.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:14:02.002259+00:00
---

# Apigee Connect v1 API - Class ConnectionService (2.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Apigee Connect v1 API - Class ConnectionService (2.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.4.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.3.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.2.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/2.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.1.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/1.0.0/Google.Cloud.ApigeeConnect.V1.ConnectionService)


    
    
    public static class ConnectionService

Reference documentation and code samples for the Apigee Connect v1 API class ConnectionService.

Service Interface for the Apigee Connect connection management APIs.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConnectionService

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.ApigeeConnect.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1)

## Assembly

Google.Cloud.ApigeeConnect.V1.dll

## Methods 

### BindService(ConnectionServiceBase)
    
    
    public static ServerServiceDefinition BindService(ConnectionService.ConnectionServiceBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[ConnectionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService)[ConnectionServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, ConnectionServiceBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, ConnectionService.ConnectionServiceBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[ConnectionService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService)[ConnectionServiceBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ApigeeConnect.V1/latest/Google.Cloud.ApigeeConnect.V1.ConnectionService.ConnectionServiceBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
