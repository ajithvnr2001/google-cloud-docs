---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Network Connectivity v1 API - Class ServiceCollectionExtensions (2.14.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:37.626060+00:00
---

# Network Connectivity v1 API - Class ServiceCollectionExtensions (2.14.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Network Connectivity v1 API - Class ServiceCollectionExtensions (2.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.14.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.13.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.13.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.12.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.12.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.11.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.11.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.10.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.10.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.9.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.8.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.7.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.6.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.5.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.4.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.3.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.2.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.1.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/2.0.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.2.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.1.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/1.0.0/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions)


    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Network Connectivity v1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.NetworkConnectivity.V1.dll

## Methods 

### AddCrossNetworkAutomationServiceClient(IServiceCollection, Action<CrossNetworkAutomationServiceClientBuilder>)
    
    
    public static IServiceCollection AddCrossNetworkAutomationServiceClient(this IServiceCollection services, Action<CrossNetworkAutomationServiceClientBuilder> action = null)

Adds a singleton [CrossNetworkAutomationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CrossNetworkAutomationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CrossNetworkAutomationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CrossNetworkAutomationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCrossNetworkAutomationServiceClient(IServiceCollection, Action<IServiceProvider, CrossNetworkAutomationServiceClientBuilder>)
    
    
    public static IServiceCollection AddCrossNetworkAutomationServiceClient(this IServiceCollection services, Action<IServiceProvider, CrossNetworkAutomationServiceClientBuilder> action)

Adds a singleton [CrossNetworkAutomationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CrossNetworkAutomationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CrossNetworkAutomationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.CrossNetworkAutomationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDataTransferServiceClient(IServiceCollection, Action<DataTransferServiceClientBuilder>)
    
    
    public static IServiceCollection AddDataTransferServiceClient(this IServiceCollection services, Action<DataTransferServiceClientBuilder> action = null)

Adds a singleton [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DataTransferServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDataTransferServiceClient(IServiceCollection, Action<IServiceProvider, DataTransferServiceClientBuilder>)
    
    
    public static IServiceCollection AddDataTransferServiceClient(this IServiceCollection services, Action<IServiceProvider, DataTransferServiceClientBuilder> action)

Adds a singleton [DataTransferServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DataTransferServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.DataTransferServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHubServiceClient(IServiceCollection, Action<HubServiceClientBuilder>)
    
    
    public static IServiceCollection AddHubServiceClient(this IServiceCollection services, Action<HubServiceClientBuilder> action = null)

Adds a singleton [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.HubServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[HubServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.HubServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHubServiceClient(IServiceCollection, Action<IServiceProvider, HubServiceClientBuilder>)
    
    
    public static IServiceCollection AddHubServiceClient(this IServiceCollection services, Action<IServiceProvider, HubServiceClientBuilder> action)

Adds a singleton [HubServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.HubServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[HubServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.HubServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInternalRangeServiceClient(IServiceCollection, Action<InternalRangeServiceClientBuilder>)
    
    
    public static IServiceCollection AddInternalRangeServiceClient(this IServiceCollection services, Action<InternalRangeServiceClientBuilder> action = null)

Adds a singleton [InternalRangeServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.InternalRangeServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InternalRangeServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.InternalRangeServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInternalRangeServiceClient(IServiceCollection, Action<IServiceProvider, InternalRangeServiceClientBuilder>)
    
    
    public static IServiceCollection AddInternalRangeServiceClient(this IServiceCollection services, Action<IServiceProvider, InternalRangeServiceClientBuilder> action)

Adds a singleton [InternalRangeServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.InternalRangeServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InternalRangeServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.InternalRangeServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPolicyBasedRoutingServiceClient(IServiceCollection, Action<PolicyBasedRoutingServiceClientBuilder>)
    
    
    public static IServiceCollection AddPolicyBasedRoutingServiceClient(this IServiceCollection services, Action<PolicyBasedRoutingServiceClientBuilder> action = null)

Adds a singleton [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoutingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PolicyBasedRoutingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoutingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPolicyBasedRoutingServiceClient(IServiceCollection, Action<IServiceProvider, PolicyBasedRoutingServiceClientBuilder>)
    
    
    public static IServiceCollection AddPolicyBasedRoutingServiceClient(this IServiceCollection services, Action<IServiceProvider, PolicyBasedRoutingServiceClientBuilder> action)

Adds a singleton [PolicyBasedRoutingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoutingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PolicyBasedRoutingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.NetworkConnectivity.V1/latest/Google.Cloud.NetworkConnectivity.V1.PolicyBasedRoutingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
