---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Google Cloud Natural Language v1 API - Class ServiceCollectionExtensions (3.8.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:14.610065+00:00
---

# Google Cloud Natural Language v1 API - Class ServiceCollectionExtensions (3.8.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Natural Language v1 API - Class ServiceCollectionExtensions (3.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.8.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.7.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.6.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.5.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.4.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.3.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.2.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.1.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/3.0.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.3.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/2.2.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)


    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Google Cloud Natural Language v1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.Language.V1.dll

## Methods 

### AddLanguageServiceClient(IServiceCollection, Action<LanguageServiceClientBuilder>)
    
    
    public static IServiceCollection AddLanguageServiceClient(this IServiceCollection services, Action<LanguageServiceClientBuilder> action = null)

Adds a singleton [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.LanguageServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[LanguageServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.LanguageServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLanguageServiceClient(IServiceCollection, Action<IServiceProvider, LanguageServiceClientBuilder>)
    
    
    public static IServiceCollection AddLanguageServiceClient(this IServiceCollection services, Action<IServiceProvider, LanguageServiceClientBuilder> action)

Adds a singleton [LanguageServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.LanguageServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[LanguageServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Language.V1/latest/Google.Cloud.Language.V1.LanguageServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
