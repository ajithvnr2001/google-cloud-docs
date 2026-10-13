---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Google Cloud Support v2beta API - Class ServiceCollectionExtensions (1.0.0-beta05) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:17:00.797309+00:00
---

# Google Cloud Support v2beta API - Class ServiceCollectionExtensions (1.0.0-beta05)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Support v2beta API - Class ServiceCollectionExtensions (1.0.0-beta05) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta05 (latest)  1.0.0-beta04 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Google Cloud Support v2beta API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.Support.V2Beta.dll

## Methods 

### AddCaseAttachmentServiceClient(IServiceCollection, Action<CaseAttachmentServiceClientBuilder>)
    
    
    public static IServiceCollection AddCaseAttachmentServiceClient(this IServiceCollection services, Action<CaseAttachmentServiceClientBuilder> action = null)

Adds a singleton [CaseAttachmentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseAttachmentServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CaseAttachmentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseAttachmentServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCaseAttachmentServiceClient(IServiceCollection, Action<IServiceProvider, CaseAttachmentServiceClientBuilder>)
    
    
    public static IServiceCollection AddCaseAttachmentServiceClient(this IServiceCollection services, Action<IServiceProvider, CaseAttachmentServiceClientBuilder> action)

Adds a singleton [CaseAttachmentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseAttachmentServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CaseAttachmentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseAttachmentServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCaseServiceClient(IServiceCollection, Action<CaseServiceClientBuilder>)
    
    
    public static IServiceCollection AddCaseServiceClient(this IServiceCollection services, Action<CaseServiceClientBuilder> action = null)

Adds a singleton [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CaseServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCaseServiceClient(IServiceCollection, Action<IServiceProvider, CaseServiceClientBuilder>)
    
    
    public static IServiceCollection AddCaseServiceClient(this IServiceCollection services, Action<IServiceProvider, CaseServiceClientBuilder> action)

Adds a singleton [CaseServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CaseServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CaseServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCommentServiceClient(IServiceCollection, Action<CommentServiceClientBuilder>)
    
    
    public static IServiceCollection AddCommentServiceClient(this IServiceCollection services, Action<CommentServiceClientBuilder> action = null)

Adds a singleton [CommentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CommentServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CommentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CommentServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCommentServiceClient(IServiceCollection, Action<IServiceProvider, CommentServiceClientBuilder>)
    
    
    public static IServiceCollection AddCommentServiceClient(this IServiceCollection services, Action<IServiceProvider, CommentServiceClientBuilder> action)

Adds a singleton [CommentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CommentServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CommentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.CommentServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeedServiceClient(IServiceCollection, Action<FeedServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeedServiceClient(this IServiceCollection services, Action<FeedServiceClientBuilder> action = null)

Adds a singleton [FeedServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.FeedServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeedServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.FeedServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeedServiceClient(IServiceCollection, Action<IServiceProvider, FeedServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeedServiceClient(this IServiceCollection services, Action<IServiceProvider, FeedServiceClientBuilder> action)

Adds a singleton [FeedServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.FeedServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeedServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.FeedServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSupportEventSubscriptionServiceClient(IServiceCollection, Action<SupportEventSubscriptionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSupportEventSubscriptionServiceClient(this IServiceCollection services, Action<SupportEventSubscriptionServiceClientBuilder> action = null)

Adds a singleton [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.SupportEventSubscriptionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SupportEventSubscriptionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.SupportEventSubscriptionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSupportEventSubscriptionServiceClient(IServiceCollection, Action<IServiceProvider, SupportEventSubscriptionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSupportEventSubscriptionServiceClient(this IServiceCollection services, Action<IServiceProvider, SupportEventSubscriptionServiceClientBuilder> action)

Adds a singleton [SupportEventSubscriptionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.SupportEventSubscriptionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SupportEventSubscriptionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Support.V2Beta/latest/Google.Cloud.Support.V2Beta.SupportEventSubscriptionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-30 UTC."],[],[]] 
