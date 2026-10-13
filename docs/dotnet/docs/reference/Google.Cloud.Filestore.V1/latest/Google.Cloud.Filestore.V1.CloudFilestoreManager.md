---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager
title: Cloud Filestore v1 API - Class CloudFilestoreManager (2.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:21.166291+00:00
---

# Cloud Filestore v1 API - Class CloudFilestoreManager (2.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Filestore v1 API - Class CloudFilestoreManager (2.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.7.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.6.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.5.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.4.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.3.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.2.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.1.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/2.0.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.2.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.1.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/1.0.0/Google.Cloud.Filestore.V1.CloudFilestoreManager)


    
    
    public static class CloudFilestoreManager

Reference documentation and code samples for the Cloud Filestore v1 API class CloudFilestoreManager.

Configures and manages Filestore resources.

Filestore Manager v1.

The `file.googleapis.com` service implements the Filestore API and defines the following resource model for managing instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of instances and backups, named: `/instances/*` and `/backups/*` respectively.
  * As such, Filestore instances are resources of the form: `/projects/{project_number}/locations/{location_id}/instances/{instance_id}` and backups are resources of the form: `/projects/{project_number}/locations/{location_id}/backup/{backup_id}`



Note that location_id must be a Google Cloud `zone` for instances, but a Google Cloud `region` for backups; for example:

  * `projects/12345/locations/us-central1-c/instances/my-filestore`
  * `projects/12345/locations/us-central1/backups/my-backup`



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudFilestoreManager

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Filestore.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1)

## Assembly

Google.Cloud.Filestore.V1.dll

## Methods 

### BindService(CloudFilestoreManagerBase)
    
    
    public static ServerServiceDefinition BindService(CloudFilestoreManager.CloudFilestoreManagerBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[CloudFilestoreManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager)[CloudFilestoreManagerBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager.CloudFilestoreManagerBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, CloudFilestoreManagerBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, CloudFilestoreManager.CloudFilestoreManagerBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[CloudFilestoreManager](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager)[CloudFilestoreManagerBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Filestore.V1/latest/Google.Cloud.Filestore.V1.CloudFilestoreManager.CloudFilestoreManagerBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
