---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations
title: Google.LongRunning - Class Operations (3.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:32.887875+00:00
---

# Google.LongRunning - Class Operations (3.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google.LongRunning - Class Operations (3.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.4.0/Google.LongRunning.Operations)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.3.0/Google.LongRunning.Operations)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.2.0/Google.LongRunning.Operations)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.1.0/Google.LongRunning.Operations)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/3.0.0/Google.LongRunning.Operations)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/2.3.0/Google.LongRunning.Operations)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/2.2.0/Google.LongRunning.Operations)


    
    
    public static class Operations

Reference documentation and code samples for the Google.LongRunning class Operations.

Manages long-running operations with an API service.

When an API method normally takes long time to complete, it can be designed to return [Operation][google.longrunning.Operation] to the client, and the client can use this interface to receive the real response asynchronously by polling the operation resource, or pass the operation resource to another API (such as Pub/Sub API) to receive the response. Any API service that returns long-running operations should implement the `Operations` interface so developers can have a consistent client experience.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Operations

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.LongRunning](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning)

## Assembly

Google.LongRunning.dll

## Methods 

### BindService(OperationsBase)
    
    
    public static ServerServiceDefinition BindService(Operations.OperationsBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations)[OperationsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, OperationsBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, Operations.OperationsBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[Operations](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations)[OperationsBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operations.OperationsBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
