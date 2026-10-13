---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Confidential Computing v1 API - Class ServiceCollectionExtensions (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:39:44.572909+00:00
---

# Confidential Computing v1 API - Class ServiceCollectionExtensions (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Confidential Computing v1 API - Class ServiceCollectionExtensions (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Confidential Computing v1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.ConfidentialComputing.V1.dll

## Methods 

### AddConfidentialComputingClient(IServiceCollection, Action<ConfidentialComputingClientBuilder>)
    
    
    public static IServiceCollection AddConfidentialComputingClient(this IServiceCollection services, Action<ConfidentialComputingClientBuilder> action = null)

Adds a singleton [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ConfidentialComputingClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddConfidentialComputingClient(IServiceCollection, Action<IServiceProvider, ConfidentialComputingClientBuilder>)
    
    
    public static IServiceCollection AddConfidentialComputingClient(this IServiceCollection services, Action<IServiceProvider, ConfidentialComputingClientBuilder> action)

Adds a singleton [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ConfidentialComputingClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
