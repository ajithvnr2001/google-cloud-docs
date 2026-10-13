---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Google Cloud OS Login v1beta API - Class ServiceCollectionExtensions (3.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:19.670303+00:00
---

# Google Cloud OS Login v1beta API - Class ServiceCollectionExtensions (3.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud OS Login v1beta API - Class ServiceCollectionExtensions (3.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta10 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 3.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/3.0.0-beta09/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/2.0.0-beta05/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)


    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Google Cloud OS Login v1beta API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.OsLogin.V1Beta.dll

## Methods 

### AddOsLoginServiceClient(IServiceCollection, Action<OsLoginServiceClientBuilder>)
    
    
    public static IServiceCollection AddOsLoginServiceClient(this IServiceCollection services, Action<OsLoginServiceClientBuilder> action = null)

Adds a singleton [OsLoginServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.OsLoginServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[OsLoginServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.OsLoginServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddOsLoginServiceClient(IServiceCollection, Action<IServiceProvider, OsLoginServiceClientBuilder>)
    
    
    public static IServiceCollection AddOsLoginServiceClient(this IServiceCollection services, Action<IServiceProvider, OsLoginServiceClientBuilder> action)

Adds a singleton [OsLoginServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.OsLoginServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[OsLoginServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.OsLogin.V1Beta/latest/Google.Cloud.OsLogin.V1Beta.OsLoginServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
