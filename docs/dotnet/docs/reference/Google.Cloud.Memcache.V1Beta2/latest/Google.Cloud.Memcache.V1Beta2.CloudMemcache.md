---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache
title: Google Cloud Memorystore for Memcached v1beta2 API - Class CloudMemcache (2.0.0-beta07) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:41.819194+00:00
---

# Google Cloud Memorystore for Memcached v1beta2 API - Class CloudMemcache (2.0.0-beta07)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Memcached v1beta2 API - Class CloudMemcache (2.0.0-beta07) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.0.0-beta07 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache)
  * [ 2.0.0-beta06 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/2.0.0-beta06/Google.Cloud.Memcache.V1Beta2.CloudMemcache)
  * [ 1.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/1.0.0-beta05/Google.Cloud.Memcache.V1Beta2.CloudMemcache)


    
    
    public static class CloudMemcache

Reference documentation and code samples for the Google Cloud Memorystore for Memcached v1beta2 API class CloudMemcache.

Configures and manages Cloud Memorystore for Memcached instances.

The `memcache.googleapis.com` service implements the Google Cloud Memorystore for Memcached API and defines the following resource model for managing Memorystore Memcached (also called Memcached below) instances:

  * The service works with a collection of cloud projects, named: `/projects/*`
  * Each project has a collection of available locations, named: `/locations/*`
  * Each location has a collection of Memcached instances, named: `/instances/*`
  * As such, Memcached instances are resources of the form: `/projects/{project_id}/locations/{location_id}/instances/{instance_id}`



Note that location_id must be a GCP `region`; for example:

  * `projects/my-memcached-project/locations/us-central1/instances/my-memcached`



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CloudMemcache

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Memcache.V1Beta2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2)

## Assembly

Google.Cloud.Memcache.V1Beta2.dll

## Methods 

### BindService(CloudMemcacheBase)
    
    
    public static ServerServiceDefinition BindService(CloudMemcache.CloudMemcacheBase serviceImpl)

Creates service definition that can be registered with a server

**Parameter**  
---  
**Name** | **Description**  
`serviceImpl` | `[CloudMemcache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache)[CloudMemcacheBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache.CloudMemcacheBase)`  
An object implementing the server-side handling logic.  
**Returns**  
---  
**Type** | **Description**  
`[ServerServiceDefinition](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServerServiceDefinition.html)` |   
  
### BindService(ServiceBinderBase, CloudMemcacheBase)
    
    
    public static void BindService(ServiceBinderBase serviceBinder, CloudMemcache.CloudMemcacheBase serviceImpl)

Register service method with a service binder with or without implementation. Useful when customizing the service binding logic. Note: this method is part of an experimental API that can change or be removed without any prior notice.

**Parameters**  
---  
**Name** | **Description**  
`serviceBinder` | `[ServiceBinderBase](https://cloud.google.com/dotnet/docs/reference/Grpc.Core/latest/Grpc.Core.ServiceBinderBase.html)`  
Service methods will be bound by calling `AddMethod` on this object.  
`serviceImpl` | `[CloudMemcache](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache)[CloudMemcacheBase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Memcache.V1Beta2/latest/Google.Cloud.Memcache.V1Beta2.CloudMemcache.CloudMemcacheBase)`  
An object implementing the server-side handling logic.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
