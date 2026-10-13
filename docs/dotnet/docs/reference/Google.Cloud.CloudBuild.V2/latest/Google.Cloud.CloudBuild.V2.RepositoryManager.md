---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager
title: Cloud Build v2 API - Class RepositoryManager (1.5.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:38:26.641862+00:00
---

# Cloud Build v2 API - Class RepositoryManager (1.5.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Build v2 API - Class RepositoryManager (1.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.5.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.4.0/Google.Cloud.CloudBuild.V2.RepositoryManager)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.3.0/Google.Cloud.CloudBuild.V2.RepositoryManager)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.2.0/Google.Cloud.CloudBuild.V2.RepositoryManager)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.1.0/Google.Cloud.CloudBuild.V2.RepositoryManager)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/1.0.0/Google.Cloud.CloudBuild.V2.RepositoryManager)


    
    
    public static class RepositoryManager

Reference documentation and code samples for the Cloud Build v2 API class RepositoryManager.

Manages connections to source code repositories.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > RepositoryManager

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.CloudBuild.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2)

## Assembly

Google.Cloud.CloudBuild.V2.dll

## Methods 

### BindService(RepositoryManagerBase)
    
    
    public static ServerServiceDefinition BindService(RepositoryManager.RepositoryManagerBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[RepositoryManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager)[RepositoryManagerBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager.RepositoryManagerBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, RepositoryManagerBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, RepositoryManager.RepositoryManagerBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[RepositoryManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager)[RepositoryManagerBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.CloudBuild.V2/latest/Google.Cloud.CloudBuild.V2.RepositoryManager.RepositoryManagerBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
