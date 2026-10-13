---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Compute Engine v1 API - Class ServiceCollectionExtensions (4.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:34.541998+00:00
---

# Compute Engine v1 API - Class ServiceCollectionExtensions (4.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Compute Engine v1 API - Class ServiceCollectionExtensions (4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Compute Engine v1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.Compute.V1.dll

## Methods 

### AddAcceleratorTypesClient(IServiceCollection, Action<AcceleratorTypesClientBuilder>)
    
    
    public static IServiceCollection AddAcceleratorTypesClient(this IServiceCollection services, Action<AcceleratorTypesClientBuilder> action = null)

Adds a singleton [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AcceleratorTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAcceleratorTypesClient(IServiceCollection, Action<IServiceProvider, AcceleratorTypesClientBuilder>)
    
    
    public static IServiceCollection AddAcceleratorTypesClient(this IServiceCollection services, Action<IServiceProvider, AcceleratorTypesClientBuilder> action)

Adds a singleton [AcceleratorTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AcceleratorTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AcceleratorTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAddressesClient(IServiceCollection, Action<AddressesClientBuilder>)
    
    
    public static IServiceCollection AddAddressesClient(this IServiceCollection services, Action<AddressesClientBuilder> action = null)

Adds a singleton [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAddressesClient(IServiceCollection, Action<IServiceProvider, AddressesClientBuilder>)
    
    
    public static IServiceCollection AddAddressesClient(this IServiceCollection services, Action<IServiceProvider, AddressesClientBuilder> action)

Adds a singleton [AddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AddressesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAdviceClient(IServiceCollection, Action<AdviceClientBuilder>)
    
    
    public static IServiceCollection AddAdviceClient(this IServiceCollection services, Action<AdviceClientBuilder> action = null)

Adds a singleton [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AdviceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAdviceClient(IServiceCollection, Action<IServiceProvider, AdviceClientBuilder>)
    
    
    public static IServiceCollection AddAdviceClient(this IServiceCollection services, Action<IServiceProvider, AdviceClientBuilder> action)

Adds a singleton [AdviceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AdviceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AdviceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAutoscalersClient(IServiceCollection, Action<AutoscalersClientBuilder>)
    
    
    public static IServiceCollection AddAutoscalersClient(this IServiceCollection services, Action<AutoscalersClientBuilder> action = null)

Adds a singleton [AutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AutoscalersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[AutoscalersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AutoscalersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddAutoscalersClient(IServiceCollection, Action<IServiceProvider, AutoscalersClientBuilder>)
    
    
    public static IServiceCollection AddAutoscalersClient(this IServiceCollection services, Action<IServiceProvider, AutoscalersClientBuilder> action)

Adds a singleton [AutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AutoscalersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[AutoscalersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.AutoscalersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddBackendBucketsClient(IServiceCollection, Action<BackendBucketsClientBuilder>)
    
    
    public static IServiceCollection AddBackendBucketsClient(this IServiceCollection services, Action<BackendBucketsClientBuilder> action = null)

Adds a singleton [BackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[BackendBucketsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddBackendBucketsClient(IServiceCollection, Action<IServiceProvider, BackendBucketsClientBuilder>)
    
    
    public static IServiceCollection AddBackendBucketsClient(this IServiceCollection services, Action<IServiceProvider, BackendBucketsClientBuilder> action)

Adds a singleton [BackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[BackendBucketsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendBucketsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddBackendServicesClient(IServiceCollection, Action<BackendServicesClientBuilder>)
    
    
    public static IServiceCollection AddBackendServicesClient(this IServiceCollection services, Action<BackendServicesClientBuilder> action = null)

Adds a singleton [BackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[BackendServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddBackendServicesClient(IServiceCollection, Action<IServiceProvider, BackendServicesClientBuilder>)
    
    
    public static IServiceCollection AddBackendServicesClient(this IServiceCollection services, Action<IServiceProvider, BackendServicesClientBuilder> action)

Adds a singleton [BackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[BackendServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.BackendServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCrossSiteNetworksClient(IServiceCollection, Action<CrossSiteNetworksClientBuilder>)
    
    
    public static IServiceCollection AddCrossSiteNetworksClient(this IServiceCollection services, Action<CrossSiteNetworksClientBuilder> action = null)

Adds a singleton [CrossSiteNetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CrossSiteNetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[CrossSiteNetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CrossSiteNetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddCrossSiteNetworksClient(IServiceCollection, Action<IServiceProvider, CrossSiteNetworksClientBuilder>)
    
    
    public static IServiceCollection AddCrossSiteNetworksClient(this IServiceCollection services, Action<IServiceProvider, CrossSiteNetworksClientBuilder> action)

Adds a singleton [CrossSiteNetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CrossSiteNetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[CrossSiteNetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.CrossSiteNetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDiskTypesClient(IServiceCollection, Action<DiskTypesClientBuilder>)
    
    
    public static IServiceCollection AddDiskTypesClient(this IServiceCollection services, Action<DiskTypesClientBuilder> action = null)

Adds a singleton [DiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DiskTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DiskTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DiskTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDiskTypesClient(IServiceCollection, Action<IServiceProvider, DiskTypesClientBuilder>)
    
    
    public static IServiceCollection AddDiskTypesClient(this IServiceCollection services, Action<IServiceProvider, DiskTypesClientBuilder> action)

Adds a singleton [DiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DiskTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DiskTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DiskTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDisksClient(IServiceCollection, Action<DisksClientBuilder>)
    
    
    public static IServiceCollection AddDisksClient(this IServiceCollection services, Action<DisksClientBuilder> action = null)

Adds a singleton [DisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDisksClient(IServiceCollection, Action<IServiceProvider, DisksClientBuilder>)
    
    
    public static IServiceCollection AddDisksClient(this IServiceCollection services, Action<IServiceProvider, DisksClientBuilder> action)

Adds a singleton [DisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.DisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExternalVpnGatewaysClient(IServiceCollection, Action<ExternalVpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddExternalVpnGatewaysClient(this IServiceCollection services, Action<ExternalVpnGatewaysClientBuilder> action = null)

Adds a singleton [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ExternalVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExternalVpnGatewaysClient(IServiceCollection, Action<IServiceProvider, ExternalVpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddExternalVpnGatewaysClient(this IServiceCollection services, Action<IServiceProvider, ExternalVpnGatewaysClientBuilder> action)

Adds a singleton [ExternalVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ExternalVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ExternalVpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFirewallPoliciesClient(IServiceCollection, Action<FirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddFirewallPoliciesClient(this IServiceCollection services, Action<FirewallPoliciesClientBuilder> action = null)

Adds a singleton [FirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFirewallPoliciesClient(IServiceCollection, Action<IServiceProvider, FirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddFirewallPoliciesClient(this IServiceCollection services, Action<IServiceProvider, FirewallPoliciesClientBuilder> action)

Adds a singleton [FirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFirewallsClient(IServiceCollection, Action<FirewallsClientBuilder>)
    
    
    public static IServiceCollection AddFirewallsClient(this IServiceCollection services, Action<FirewallsClientBuilder> action = null)

Adds a singleton [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FirewallsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFirewallsClient(IServiceCollection, Action<IServiceProvider, FirewallsClientBuilder>)
    
    
    public static IServiceCollection AddFirewallsClient(this IServiceCollection services, Action<IServiceProvider, FirewallsClientBuilder> action)

Adds a singleton [FirewallsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FirewallsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FirewallsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddForwardingRulesClient(IServiceCollection, Action<ForwardingRulesClientBuilder>)
    
    
    public static IServiceCollection AddForwardingRulesClient(this IServiceCollection services, Action<ForwardingRulesClientBuilder> action = null)

Adds a singleton [ForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ForwardingRulesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ForwardingRulesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ForwardingRulesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddForwardingRulesClient(IServiceCollection, Action<IServiceProvider, ForwardingRulesClientBuilder>)
    
    
    public static IServiceCollection AddForwardingRulesClient(this IServiceCollection services, Action<IServiceProvider, ForwardingRulesClientBuilder> action)

Adds a singleton [ForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ForwardingRulesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ForwardingRulesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ForwardingRulesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFutureReservationsClient(IServiceCollection, Action<FutureReservationsClientBuilder>)
    
    
    public static IServiceCollection AddFutureReservationsClient(this IServiceCollection services, Action<FutureReservationsClientBuilder> action = null)

Adds a singleton [FutureReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FutureReservationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FutureReservationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FutureReservationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFutureReservationsClient(IServiceCollection, Action<IServiceProvider, FutureReservationsClientBuilder>)
    
    
    public static IServiceCollection AddFutureReservationsClient(this IServiceCollection services, Action<IServiceProvider, FutureReservationsClientBuilder> action)

Adds a singleton [FutureReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FutureReservationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FutureReservationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.FutureReservationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalAddressesClient(IServiceCollection, Action<GlobalAddressesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalAddressesClient(this IServiceCollection services, Action<GlobalAddressesClientBuilder> action = null)

Adds a singleton [GlobalAddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalAddressesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalAddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalAddressesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalAddressesClient(IServiceCollection, Action<IServiceProvider, GlobalAddressesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalAddressesClient(this IServiceCollection services, Action<IServiceProvider, GlobalAddressesClientBuilder> action)

Adds a singleton [GlobalAddressesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalAddressesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalAddressesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalAddressesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalForwardingRulesClient(IServiceCollection, Action<GlobalForwardingRulesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalForwardingRulesClient(this IServiceCollection services, Action<GlobalForwardingRulesClientBuilder> action = null)

Adds a singleton [GlobalForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalForwardingRulesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalForwardingRulesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalForwardingRulesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalForwardingRulesClient(IServiceCollection, Action<IServiceProvider, GlobalForwardingRulesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalForwardingRulesClient(this IServiceCollection services, Action<IServiceProvider, GlobalForwardingRulesClientBuilder> action)

Adds a singleton [GlobalForwardingRulesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalForwardingRulesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalForwardingRulesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalForwardingRulesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalFrontendSettingsServiceClient(IServiceCollection, Action<GlobalFrontendSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddGlobalFrontendSettingsServiceClient(this IServiceCollection services, Action<GlobalFrontendSettingsServiceClientBuilder> action = null)

Adds a singleton [GlobalFrontendSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalFrontendSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalFrontendSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalFrontendSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalFrontendSettingsServiceClient(IServiceCollection, Action<IServiceProvider, GlobalFrontendSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddGlobalFrontendSettingsServiceClient(this IServiceCollection services, Action<IServiceProvider, GlobalFrontendSettingsServiceClientBuilder> action)

Adds a singleton [GlobalFrontendSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalFrontendSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalFrontendSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalFrontendSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalNetworkEndpointGroupsClient(IServiceCollection, Action<GlobalNetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalNetworkEndpointGroupsClient(this IServiceCollection services, Action<GlobalNetworkEndpointGroupsClientBuilder> action = null)

Adds a singleton [GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalNetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalNetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalNetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalNetworkEndpointGroupsClient(IServiceCollection, Action<IServiceProvider, GlobalNetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalNetworkEndpointGroupsClient(this IServiceCollection services, Action<IServiceProvider, GlobalNetworkEndpointGroupsClientBuilder> action)

Adds a singleton [GlobalNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalNetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalNetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalNetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalOperationsClient(IServiceCollection, Action<GlobalOperationsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalOperationsClient(this IServiceCollection services, Action<GlobalOperationsClientBuilder> action = null)

Adds a singleton [GlobalOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalOperationsClient(IServiceCollection, Action<IServiceProvider, GlobalOperationsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalOperationsClient(this IServiceCollection services, Action<IServiceProvider, GlobalOperationsClientBuilder> action)

Adds a singleton [GlobalOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalOrganizationOperationsClient(IServiceCollection, Action<GlobalOrganizationOperationsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalOrganizationOperationsClient(this IServiceCollection services, Action<GlobalOrganizationOperationsClientBuilder> action = null)

Adds a singleton [GlobalOrganizationOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalOrganizationOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalOrganizationOperationsClient(IServiceCollection, Action<IServiceProvider, GlobalOrganizationOperationsClientBuilder>)
    
    
    public static IServiceCollection AddGlobalOrganizationOperationsClient(this IServiceCollection services, Action<IServiceProvider, GlobalOrganizationOperationsClientBuilder> action)

Adds a singleton [GlobalOrganizationOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalOrganizationOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalOrganizationOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalPublicDelegatedPrefixesClient(IServiceCollection, Action<GlobalPublicDelegatedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalPublicDelegatedPrefixesClient(this IServiceCollection services, Action<GlobalPublicDelegatedPrefixesClientBuilder> action = null)

Adds a singleton [GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalPublicDelegatedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalPublicDelegatedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalPublicDelegatedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalPublicDelegatedPrefixesClient(IServiceCollection, Action<IServiceProvider, GlobalPublicDelegatedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalPublicDelegatedPrefixesClient(this IServiceCollection services, Action<IServiceProvider, GlobalPublicDelegatedPrefixesClientBuilder> action)

Adds a singleton [GlobalPublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalPublicDelegatedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalPublicDelegatedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalPublicDelegatedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalVmExtensionPoliciesClient(IServiceCollection, Action<GlobalVmExtensionPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalVmExtensionPoliciesClient(this IServiceCollection services, Action<GlobalVmExtensionPoliciesClientBuilder> action = null)

Adds a singleton [GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalVmExtensionPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GlobalVmExtensionPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalVmExtensionPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGlobalVmExtensionPoliciesClient(IServiceCollection, Action<IServiceProvider, GlobalVmExtensionPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddGlobalVmExtensionPoliciesClient(this IServiceCollection services, Action<IServiceProvider, GlobalVmExtensionPoliciesClientBuilder> action)

Adds a singleton [GlobalVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalVmExtensionPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GlobalVmExtensionPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.GlobalVmExtensionPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHealthChecksClient(IServiceCollection, Action<HealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddHealthChecksClient(this IServiceCollection services, Action<HealthChecksClientBuilder> action = null)

Adds a singleton [HealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[HealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHealthChecksClient(IServiceCollection, Action<IServiceProvider, HealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddHealthChecksClient(this IServiceCollection services, Action<IServiceProvider, HealthChecksClientBuilder> action)

Adds a singleton [HealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[HealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHostsClient(IServiceCollection, Action<HostsClientBuilder>)
    
    
    public static IServiceCollection AddHostsClient(this IServiceCollection services, Action<HostsClientBuilder> action = null)

Adds a singleton [HostsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HostsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[HostsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HostsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddHostsClient(IServiceCollection, Action<IServiceProvider, HostsClientBuilder>)
    
    
    public static IServiceCollection AddHostsClient(this IServiceCollection services, Action<IServiceProvider, HostsClientBuilder> action)

Adds a singleton [HostsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HostsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[HostsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.HostsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImageFamilyViewsClient(IServiceCollection, Action<ImageFamilyViewsClientBuilder>)
    
    
    public static IServiceCollection AddImageFamilyViewsClient(this IServiceCollection services, Action<ImageFamilyViewsClientBuilder> action = null)

Adds a singleton [ImageFamilyViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageFamilyViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ImageFamilyViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageFamilyViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImageFamilyViewsClient(IServiceCollection, Action<IServiceProvider, ImageFamilyViewsClientBuilder>)
    
    
    public static IServiceCollection AddImageFamilyViewsClient(this IServiceCollection services, Action<IServiceProvider, ImageFamilyViewsClientBuilder> action)

Adds a singleton [ImageFamilyViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageFamilyViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ImageFamilyViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageFamilyViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImageViewsClient(IServiceCollection, Action<ImageViewsClientBuilder>)
    
    
    public static IServiceCollection AddImageViewsClient(this IServiceCollection services, Action<ImageViewsClientBuilder> action = null)

Adds a singleton [ImageViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ImageViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImageViewsClient(IServiceCollection, Action<IServiceProvider, ImageViewsClientBuilder>)
    
    
    public static IServiceCollection AddImageViewsClient(this IServiceCollection services, Action<IServiceProvider, ImageViewsClientBuilder> action)

Adds a singleton [ImageViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ImageViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImageViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImagesClient(IServiceCollection, Action<ImagesClientBuilder>)
    
    
    public static IServiceCollection AddImagesClient(this IServiceCollection services, Action<ImagesClientBuilder> action = null)

Adds a singleton [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ImagesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddImagesClient(IServiceCollection, Action<IServiceProvider, ImagesClientBuilder>)
    
    
    public static IServiceCollection AddImagesClient(this IServiceCollection services, Action<IServiceProvider, ImagesClientBuilder> action)

Adds a singleton [ImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ImagesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ImagesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupManagerResizeRequestsClient(IServiceCollection, Action<InstanceGroupManagerResizeRequestsClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupManagerResizeRequestsClient(this IServiceCollection services, Action<InstanceGroupManagerResizeRequestsClientBuilder> action = null)

Adds a singleton [InstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsClient) to `services` .

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstanceGroupManagerResizeRequestsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupManagerResizeRequestsClient(IServiceCollection, Action<IServiceProvider, InstanceGroupManagerResizeRequestsClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupManagerResizeRequestsClient(this IServiceCollection services, Action<IServiceProvider, InstanceGroupManagerResizeRequestsClientBuilder> action)

Adds a singleton [InstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsClient) to `services` .

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstanceGroupManagerResizeRequestsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagerResizeRequestsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupManagersClient(IServiceCollection, Action<InstanceGroupManagersClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupManagersClient(this IServiceCollection services, Action<InstanceGroupManagersClientBuilder> action = null)

Adds a singleton [InstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstanceGroupManagersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupManagersClient(IServiceCollection, Action<IServiceProvider, InstanceGroupManagersClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupManagersClient(this IServiceCollection services, Action<IServiceProvider, InstanceGroupManagersClientBuilder> action)

Adds a singleton [InstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstanceGroupManagersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupManagersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupsClient(IServiceCollection, Action<InstanceGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupsClient(this IServiceCollection services, Action<InstanceGroupsClientBuilder> action = null)

Adds a singleton [InstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstanceGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceGroupsClient(IServiceCollection, Action<IServiceProvider, InstanceGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInstanceGroupsClient(this IServiceCollection services, Action<IServiceProvider, InstanceGroupsClientBuilder> action)

Adds a singleton [InstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstanceGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceSettingsServiceClient(IServiceCollection, Action<InstanceSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddInstanceSettingsServiceClient(this IServiceCollection services, Action<InstanceSettingsServiceClientBuilder> action = null)

Adds a singleton [InstanceSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstanceSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceSettingsServiceClient(IServiceCollection, Action<IServiceProvider, InstanceSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddInstanceSettingsServiceClient(this IServiceCollection services, Action<IServiceProvider, InstanceSettingsServiceClientBuilder> action)

Adds a singleton [InstanceSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstanceSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceTemplatesClient(IServiceCollection, Action<InstanceTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddInstanceTemplatesClient(this IServiceCollection services, Action<InstanceTemplatesClientBuilder> action = null)

Adds a singleton [InstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstanceTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstanceTemplatesClient(IServiceCollection, Action<IServiceProvider, InstanceTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddInstanceTemplatesClient(this IServiceCollection services, Action<IServiceProvider, InstanceTemplatesClientBuilder> action)

Adds a singleton [InstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstanceTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstanceTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstancesClient(IServiceCollection, Action<InstancesClientBuilder>)
    
    
    public static IServiceCollection AddInstancesClient(this IServiceCollection services, Action<InstancesClientBuilder> action = null)

Adds a singleton [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstancesClient(IServiceCollection, Action<IServiceProvider, InstancesClientBuilder>)
    
    
    public static IServiceCollection AddInstancesClient(this IServiceCollection services, Action<IServiceProvider, InstancesClientBuilder> action)

Adds a singleton [InstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstantSnapshotGroupsClient(IServiceCollection, Action<InstantSnapshotGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInstantSnapshotGroupsClient(this IServiceCollection services, Action<InstantSnapshotGroupsClientBuilder> action = null)

Adds a singleton [InstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstantSnapshotGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstantSnapshotGroupsClient(IServiceCollection, Action<IServiceProvider, InstantSnapshotGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInstantSnapshotGroupsClient(this IServiceCollection services, Action<IServiceProvider, InstantSnapshotGroupsClientBuilder> action)

Adds a singleton [InstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstantSnapshotGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstantSnapshotsClient(IServiceCollection, Action<InstantSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddInstantSnapshotsClient(this IServiceCollection services, Action<InstantSnapshotsClientBuilder> action = null)

Adds a singleton [InstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InstantSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInstantSnapshotsClient(IServiceCollection, Action<IServiceProvider, InstantSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddInstantSnapshotsClient(this IServiceCollection services, Action<IServiceProvider, InstantSnapshotsClientBuilder> action)

Adds a singleton [InstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InstantSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InstantSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectAttachmentGroupsClient(IServiceCollection, Action<InterconnectAttachmentGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectAttachmentGroupsClient(this IServiceCollection services, Action<InterconnectAttachmentGroupsClientBuilder> action = null)

Adds a singleton [InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectAttachmentGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectAttachmentGroupsClient(IServiceCollection, Action<IServiceProvider, InterconnectAttachmentGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectAttachmentGroupsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectAttachmentGroupsClientBuilder> action)

Adds a singleton [InterconnectAttachmentGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectAttachmentGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectAttachmentsClient(IServiceCollection, Action<InterconnectAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectAttachmentsClient(this IServiceCollection services, Action<InterconnectAttachmentsClientBuilder> action = null)

Adds a singleton [InterconnectAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectAttachmentsClient(IServiceCollection, Action<IServiceProvider, InterconnectAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectAttachmentsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectAttachmentsClientBuilder> action)

Adds a singleton [InterconnectAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectGroupsClient(IServiceCollection, Action<InterconnectGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectGroupsClient(this IServiceCollection services, Action<InterconnectGroupsClientBuilder> action = null)

Adds a singleton [InterconnectGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectGroupsClient(IServiceCollection, Action<IServiceProvider, InterconnectGroupsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectGroupsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectGroupsClientBuilder> action)

Adds a singleton [InterconnectGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectLocationsClient(IServiceCollection, Action<InterconnectLocationsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectLocationsClient(this IServiceCollection services, Action<InterconnectLocationsClientBuilder> action = null)

Adds a singleton [InterconnectLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectLocationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectLocationsClient(IServiceCollection, Action<IServiceProvider, InterconnectLocationsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectLocationsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectLocationsClientBuilder> action)

Adds a singleton [InterconnectLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectLocationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectLocationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectRemoteLocationsClient(IServiceCollection, Action<InterconnectRemoteLocationsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectRemoteLocationsClient(this IServiceCollection services, Action<InterconnectRemoteLocationsClientBuilder> action = null)

Adds a singleton [InterconnectRemoteLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectRemoteLocationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectRemoteLocationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectRemoteLocationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectRemoteLocationsClient(IServiceCollection, Action<IServiceProvider, InterconnectRemoteLocationsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectRemoteLocationsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectRemoteLocationsClientBuilder> action)

Adds a singleton [InterconnectRemoteLocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectRemoteLocationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectRemoteLocationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectRemoteLocationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectsClient(IServiceCollection, Action<InterconnectsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectsClient(this IServiceCollection services, Action<InterconnectsClientBuilder> action = null)

Adds a singleton [InterconnectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[InterconnectsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddInterconnectsClient(IServiceCollection, Action<IServiceProvider, InterconnectsClientBuilder>)
    
    
    public static IServiceCollection AddInterconnectsClient(this IServiceCollection services, Action<IServiceProvider, InterconnectsClientBuilder> action)

Adds a singleton [InterconnectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[InterconnectsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.InterconnectsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLicenseCodesClient(IServiceCollection, Action<LicenseCodesClientBuilder>)
    
    
    public static IServiceCollection AddLicenseCodesClient(this IServiceCollection services, Action<LicenseCodesClientBuilder> action = null)

Adds a singleton [LicenseCodesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicenseCodesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[LicenseCodesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicenseCodesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLicenseCodesClient(IServiceCollection, Action<IServiceProvider, LicenseCodesClientBuilder>)
    
    
    public static IServiceCollection AddLicenseCodesClient(this IServiceCollection services, Action<IServiceProvider, LicenseCodesClientBuilder> action)

Adds a singleton [LicenseCodesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicenseCodesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[LicenseCodesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicenseCodesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLicensesClient(IServiceCollection, Action<LicensesClientBuilder>)
    
    
    public static IServiceCollection AddLicensesClient(this IServiceCollection services, Action<LicensesClientBuilder> action = null)

Adds a singleton [LicensesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicensesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[LicensesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicensesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLicensesClient(IServiceCollection, Action<IServiceProvider, LicensesClientBuilder>)
    
    
    public static IServiceCollection AddLicensesClient(this IServiceCollection services, Action<IServiceProvider, LicensesClientBuilder> action)

Adds a singleton [LicensesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicensesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[LicensesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.LicensesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMachineImagesClient(IServiceCollection, Action<MachineImagesClientBuilder>)
    
    
    public static IServiceCollection AddMachineImagesClient(this IServiceCollection services, Action<MachineImagesClientBuilder> action = null)

Adds a singleton [MachineImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImagesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MachineImagesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImagesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMachineImagesClient(IServiceCollection, Action<IServiceProvider, MachineImagesClientBuilder>)
    
    
    public static IServiceCollection AddMachineImagesClient(this IServiceCollection services, Action<IServiceProvider, MachineImagesClientBuilder> action)

Adds a singleton [MachineImagesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImagesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MachineImagesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineImagesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMachineTypesClient(IServiceCollection, Action<MachineTypesClientBuilder>)
    
    
    public static IServiceCollection AddMachineTypesClient(this IServiceCollection services, Action<MachineTypesClientBuilder> action = null)

Adds a singleton [MachineTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MachineTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMachineTypesClient(IServiceCollection, Action<IServiceProvider, MachineTypesClientBuilder>)
    
    
    public static IServiceCollection AddMachineTypesClient(this IServiceCollection services, Action<IServiceProvider, MachineTypesClientBuilder> action)

Adds a singleton [MachineTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MachineTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.MachineTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddManagedRulesetsClient(IServiceCollection, Action<ManagedRulesetsClientBuilder>)
    
    
    public static IServiceCollection AddManagedRulesetsClient(this IServiceCollection services, Action<ManagedRulesetsClientBuilder> action = null)

Adds a singleton [ManagedRulesetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ManagedRulesetsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ManagedRulesetsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ManagedRulesetsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddManagedRulesetsClient(IServiceCollection, Action<IServiceProvider, ManagedRulesetsClientBuilder>)
    
    
    public static IServiceCollection AddManagedRulesetsClient(this IServiceCollection services, Action<IServiceProvider, ManagedRulesetsClientBuilder> action)

Adds a singleton [ManagedRulesetsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ManagedRulesetsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ManagedRulesetsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ManagedRulesetsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkAttachmentsClient(IServiceCollection, Action<NetworkAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddNetworkAttachmentsClient(this IServiceCollection services, Action<NetworkAttachmentsClientBuilder> action = null)

Adds a singleton [NetworkAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworkAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkAttachmentsClient(IServiceCollection, Action<IServiceProvider, NetworkAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddNetworkAttachmentsClient(this IServiceCollection services, Action<IServiceProvider, NetworkAttachmentsClientBuilder> action)

Adds a singleton [NetworkAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworkAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkEdgeSecurityServicesClient(IServiceCollection, Action<NetworkEdgeSecurityServicesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkEdgeSecurityServicesClient(this IServiceCollection services, Action<NetworkEdgeSecurityServicesClientBuilder> action = null)

Adds a singleton [NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEdgeSecurityServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworkEdgeSecurityServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEdgeSecurityServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkEdgeSecurityServicesClient(IServiceCollection, Action<IServiceProvider, NetworkEdgeSecurityServicesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkEdgeSecurityServicesClient(this IServiceCollection services, Action<IServiceProvider, NetworkEdgeSecurityServicesClientBuilder> action)

Adds a singleton [NetworkEdgeSecurityServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEdgeSecurityServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworkEdgeSecurityServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEdgeSecurityServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkEndpointGroupsClient(IServiceCollection, Action<NetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddNetworkEndpointGroupsClient(this IServiceCollection services, Action<NetworkEndpointGroupsClientBuilder> action = null)

Adds a singleton [NetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkEndpointGroupsClient(IServiceCollection, Action<IServiceProvider, NetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddNetworkEndpointGroupsClient(this IServiceCollection services, Action<IServiceProvider, NetworkEndpointGroupsClientBuilder> action)

Adds a singleton [NetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkFirewallPoliciesClient(IServiceCollection, Action<NetworkFirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkFirewallPoliciesClient(this IServiceCollection services, Action<NetworkFirewallPoliciesClientBuilder> action = null)

Adds a singleton [NetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworkFirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkFirewallPoliciesClient(IServiceCollection, Action<IServiceProvider, NetworkFirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkFirewallPoliciesClient(this IServiceCollection services, Action<IServiceProvider, NetworkFirewallPoliciesClientBuilder> action)

Adds a singleton [NetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworkFirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkFirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkProfilesClient(IServiceCollection, Action<NetworkProfilesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkProfilesClient(this IServiceCollection services, Action<NetworkProfilesClientBuilder> action = null)

Adds a singleton [NetworkProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkProfilesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworkProfilesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkProfilesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworkProfilesClient(IServiceCollection, Action<IServiceProvider, NetworkProfilesClientBuilder>)
    
    
    public static IServiceCollection AddNetworkProfilesClient(this IServiceCollection services, Action<IServiceProvider, NetworkProfilesClientBuilder> action)

Adds a singleton [NetworkProfilesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkProfilesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworkProfilesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworkProfilesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworksClient(IServiceCollection, Action<NetworksClientBuilder>)
    
    
    public static IServiceCollection AddNetworksClient(this IServiceCollection services, Action<NetworksClientBuilder> action = null)

Adds a singleton [NetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNetworksClient(IServiceCollection, Action<IServiceProvider, NetworksClientBuilder>)
    
    
    public static IServiceCollection AddNetworksClient(this IServiceCollection services, Action<IServiceProvider, NetworksClientBuilder> action)

Adds a singleton [NetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeGroupsClient(IServiceCollection, Action<NodeGroupsClientBuilder>)
    
    
    public static IServiceCollection AddNodeGroupsClient(this IServiceCollection services, Action<NodeGroupsClientBuilder> action = null)

Adds a singleton [NodeGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NodeGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeGroupsClient(IServiceCollection, Action<IServiceProvider, NodeGroupsClientBuilder>)
    
    
    public static IServiceCollection AddNodeGroupsClient(this IServiceCollection services, Action<IServiceProvider, NodeGroupsClientBuilder> action)

Adds a singleton [NodeGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NodeGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeTemplatesClient(IServiceCollection, Action<NodeTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddNodeTemplatesClient(this IServiceCollection services, Action<NodeTemplatesClientBuilder> action = null)

Adds a singleton [NodeTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NodeTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeTemplatesClient(IServiceCollection, Action<IServiceProvider, NodeTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddNodeTemplatesClient(this IServiceCollection services, Action<IServiceProvider, NodeTemplatesClientBuilder> action)

Adds a singleton [NodeTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NodeTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeTypesClient(IServiceCollection, Action<NodeTypesClientBuilder>)
    
    
    public static IServiceCollection AddNodeTypesClient(this IServiceCollection services, Action<NodeTypesClientBuilder> action = null)

Adds a singleton [NodeTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NodeTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNodeTypesClient(IServiceCollection, Action<IServiceProvider, NodeTypesClientBuilder>)
    
    
    public static IServiceCollection AddNodeTypesClient(this IServiceCollection services, Action<IServiceProvider, NodeTypesClientBuilder> action)

Adds a singleton [NodeTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NodeTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.NodeTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddOrganizationSecurityPoliciesClient(IServiceCollection, Action<OrganizationSecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddOrganizationSecurityPoliciesClient(this IServiceCollection services, Action<OrganizationSecurityPoliciesClientBuilder> action = null)

Adds a singleton [OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OrganizationSecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[OrganizationSecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OrganizationSecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddOrganizationSecurityPoliciesClient(IServiceCollection, Action<IServiceProvider, OrganizationSecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddOrganizationSecurityPoliciesClient(this IServiceCollection services, Action<IServiceProvider, OrganizationSecurityPoliciesClientBuilder> action)

Adds a singleton [OrganizationSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OrganizationSecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[OrganizationSecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.OrganizationSecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPacketMirroringsClient(IServiceCollection, Action<PacketMirroringsClientBuilder>)
    
    
    public static IServiceCollection AddPacketMirroringsClient(this IServiceCollection services, Action<PacketMirroringsClientBuilder> action = null)

Adds a singleton [PacketMirroringsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PacketMirroringsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PacketMirroringsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PacketMirroringsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPacketMirroringsClient(IServiceCollection, Action<IServiceProvider, PacketMirroringsClientBuilder>)
    
    
    public static IServiceCollection AddPacketMirroringsClient(this IServiceCollection services, Action<IServiceProvider, PacketMirroringsClientBuilder> action)

Adds a singleton [PacketMirroringsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PacketMirroringsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PacketMirroringsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PacketMirroringsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPreviewFeaturesClient(IServiceCollection, Action<PreviewFeaturesClientBuilder>)
    
    
    public static IServiceCollection AddPreviewFeaturesClient(this IServiceCollection services, Action<PreviewFeaturesClientBuilder> action = null)

Adds a singleton [PreviewFeaturesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PreviewFeaturesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PreviewFeaturesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PreviewFeaturesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPreviewFeaturesClient(IServiceCollection, Action<IServiceProvider, PreviewFeaturesClientBuilder>)
    
    
    public static IServiceCollection AddPreviewFeaturesClient(this IServiceCollection services, Action<IServiceProvider, PreviewFeaturesClientBuilder> action)

Adds a singleton [PreviewFeaturesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PreviewFeaturesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PreviewFeaturesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PreviewFeaturesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddProjectViewsClient(IServiceCollection, Action<ProjectViewsClientBuilder>)
    
    
    public static IServiceCollection AddProjectViewsClient(this IServiceCollection services, Action<ProjectViewsClientBuilder> action = null)

Adds a singleton [ProjectViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ProjectViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddProjectViewsClient(IServiceCollection, Action<IServiceProvider, ProjectViewsClientBuilder>)
    
    
    public static IServiceCollection AddProjectViewsClient(this IServiceCollection services, Action<IServiceProvider, ProjectViewsClientBuilder> action)

Adds a singleton [ProjectViewsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectViewsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ProjectViewsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectViewsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddProjectsClient(IServiceCollection, Action<ProjectsClientBuilder>)
    
    
    public static IServiceCollection AddProjectsClient(this IServiceCollection services, Action<ProjectsClientBuilder> action = null)

Adds a singleton [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ProjectsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddProjectsClient(IServiceCollection, Action<IServiceProvider, ProjectsClientBuilder>)
    
    
    public static IServiceCollection AddProjectsClient(this IServiceCollection services, Action<IServiceProvider, ProjectsClientBuilder> action)

Adds a singleton [ProjectsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ProjectsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ProjectsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPublicAdvertisedPrefixesClient(IServiceCollection, Action<PublicAdvertisedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddPublicAdvertisedPrefixesClient(this IServiceCollection services, Action<PublicAdvertisedPrefixesClientBuilder> action = null)

Adds a singleton [PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicAdvertisedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PublicAdvertisedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicAdvertisedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPublicAdvertisedPrefixesClient(IServiceCollection, Action<IServiceProvider, PublicAdvertisedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddPublicAdvertisedPrefixesClient(this IServiceCollection services, Action<IServiceProvider, PublicAdvertisedPrefixesClientBuilder> action)

Adds a singleton [PublicAdvertisedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicAdvertisedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PublicAdvertisedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicAdvertisedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPublicDelegatedPrefixesClient(IServiceCollection, Action<PublicDelegatedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddPublicDelegatedPrefixesClient(this IServiceCollection services, Action<PublicDelegatedPrefixesClientBuilder> action = null)

Adds a singleton [PublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicDelegatedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PublicDelegatedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicDelegatedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPublicDelegatedPrefixesClient(IServiceCollection, Action<IServiceProvider, PublicDelegatedPrefixesClientBuilder>)
    
    
    public static IServiceCollection AddPublicDelegatedPrefixesClient(this IServiceCollection services, Action<IServiceProvider, PublicDelegatedPrefixesClientBuilder> action)

Adds a singleton [PublicDelegatedPrefixesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicDelegatedPrefixesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PublicDelegatedPrefixesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.PublicDelegatedPrefixesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionAutoscalersClient(IServiceCollection, Action<RegionAutoscalersClientBuilder>)
    
    
    public static IServiceCollection AddRegionAutoscalersClient(this IServiceCollection services, Action<RegionAutoscalersClientBuilder> action = null)

Adds a singleton [RegionAutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAutoscalersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionAutoscalersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAutoscalersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionAutoscalersClient(IServiceCollection, Action<IServiceProvider, RegionAutoscalersClientBuilder>)
    
    
    public static IServiceCollection AddRegionAutoscalersClient(this IServiceCollection services, Action<IServiceProvider, RegionAutoscalersClientBuilder> action)

Adds a singleton [RegionAutoscalersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAutoscalersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionAutoscalersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionAutoscalersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionBackendBucketsClient(IServiceCollection, Action<RegionBackendBucketsClientBuilder>)
    
    
    public static IServiceCollection AddRegionBackendBucketsClient(this IServiceCollection services, Action<RegionBackendBucketsClientBuilder> action = null)

Adds a singleton [RegionBackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBucketsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionBackendBucketsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBucketsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionBackendBucketsClient(IServiceCollection, Action<IServiceProvider, RegionBackendBucketsClientBuilder>)
    
    
    public static IServiceCollection AddRegionBackendBucketsClient(this IServiceCollection services, Action<IServiceProvider, RegionBackendBucketsClientBuilder> action)

Adds a singleton [RegionBackendBucketsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBucketsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionBackendBucketsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendBucketsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionBackendServicesClient(IServiceCollection, Action<RegionBackendServicesClientBuilder>)
    
    
    public static IServiceCollection AddRegionBackendServicesClient(this IServiceCollection services, Action<RegionBackendServicesClientBuilder> action = null)

Adds a singleton [RegionBackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionBackendServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionBackendServicesClient(IServiceCollection, Action<IServiceProvider, RegionBackendServicesClientBuilder>)
    
    
    public static IServiceCollection AddRegionBackendServicesClient(this IServiceCollection services, Action<IServiceProvider, RegionBackendServicesClientBuilder> action)

Adds a singleton [RegionBackendServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionBackendServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionBackendServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionCommitmentsClient(IServiceCollection, Action<RegionCommitmentsClientBuilder>)
    
    
    public static IServiceCollection AddRegionCommitmentsClient(this IServiceCollection services, Action<RegionCommitmentsClientBuilder> action = null)

Adds a singleton [RegionCommitmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCommitmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionCommitmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCommitmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionCommitmentsClient(IServiceCollection, Action<IServiceProvider, RegionCommitmentsClientBuilder>)
    
    
    public static IServiceCollection AddRegionCommitmentsClient(this IServiceCollection services, Action<IServiceProvider, RegionCommitmentsClientBuilder> action)

Adds a singleton [RegionCommitmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCommitmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionCommitmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCommitmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionCompositeHealthChecksClient(IServiceCollection, Action<RegionCompositeHealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddRegionCompositeHealthChecksClient(this IServiceCollection services, Action<RegionCompositeHealthChecksClientBuilder> action = null)

Adds a singleton [RegionCompositeHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCompositeHealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionCompositeHealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCompositeHealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionCompositeHealthChecksClient(IServiceCollection, Action<IServiceProvider, RegionCompositeHealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddRegionCompositeHealthChecksClient(this IServiceCollection services, Action<IServiceProvider, RegionCompositeHealthChecksClientBuilder> action)

Adds a singleton [RegionCompositeHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCompositeHealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionCompositeHealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionCompositeHealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionDiskTypesClient(IServiceCollection, Action<RegionDiskTypesClientBuilder>)
    
    
    public static IServiceCollection AddRegionDiskTypesClient(this IServiceCollection services, Action<RegionDiskTypesClientBuilder> action = null)

Adds a singleton [RegionDiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDiskTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionDiskTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDiskTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionDiskTypesClient(IServiceCollection, Action<IServiceProvider, RegionDiskTypesClientBuilder>)
    
    
    public static IServiceCollection AddRegionDiskTypesClient(this IServiceCollection services, Action<IServiceProvider, RegionDiskTypesClientBuilder> action)

Adds a singleton [RegionDiskTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDiskTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionDiskTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDiskTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionDisksClient(IServiceCollection, Action<RegionDisksClientBuilder>)
    
    
    public static IServiceCollection AddRegionDisksClient(this IServiceCollection services, Action<RegionDisksClientBuilder> action = null)

Adds a singleton [RegionDisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionDisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionDisksClient(IServiceCollection, Action<IServiceProvider, RegionDisksClientBuilder>)
    
    
    public static IServiceCollection AddRegionDisksClient(this IServiceCollection services, Action<IServiceProvider, RegionDisksClientBuilder> action)

Adds a singleton [RegionDisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionDisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionDisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthAggregationPoliciesClient(IServiceCollection, Action<RegionHealthAggregationPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthAggregationPoliciesClient(this IServiceCollection services, Action<RegionHealthAggregationPoliciesClientBuilder> action = null)

Adds a singleton [RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthAggregationPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionHealthAggregationPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthAggregationPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthAggregationPoliciesClient(IServiceCollection, Action<IServiceProvider, RegionHealthAggregationPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthAggregationPoliciesClient(this IServiceCollection services, Action<IServiceProvider, RegionHealthAggregationPoliciesClientBuilder> action)

Adds a singleton [RegionHealthAggregationPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthAggregationPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionHealthAggregationPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthAggregationPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthCheckServicesClient(IServiceCollection, Action<RegionHealthCheckServicesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthCheckServicesClient(this IServiceCollection services, Action<RegionHealthCheckServicesClientBuilder> action = null)

Adds a singleton [RegionHealthCheckServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthCheckServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionHealthCheckServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthCheckServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthCheckServicesClient(IServiceCollection, Action<IServiceProvider, RegionHealthCheckServicesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthCheckServicesClient(this IServiceCollection services, Action<IServiceProvider, RegionHealthCheckServicesClientBuilder> action)

Adds a singleton [RegionHealthCheckServicesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthCheckServicesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionHealthCheckServicesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthCheckServicesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthChecksClient(IServiceCollection, Action<RegionHealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthChecksClient(this IServiceCollection services, Action<RegionHealthChecksClientBuilder> action = null)

Adds a singleton [RegionHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionHealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthChecksClient(IServiceCollection, Action<IServiceProvider, RegionHealthChecksClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthChecksClient(this IServiceCollection services, Action<IServiceProvider, RegionHealthChecksClientBuilder> action)

Adds a singleton [RegionHealthChecksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthChecksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionHealthChecksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthChecksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthSourcesClient(IServiceCollection, Action<RegionHealthSourcesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthSourcesClient(this IServiceCollection services, Action<RegionHealthSourcesClientBuilder> action = null)

Adds a singleton [RegionHealthSourcesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthSourcesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionHealthSourcesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthSourcesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionHealthSourcesClient(IServiceCollection, Action<IServiceProvider, RegionHealthSourcesClientBuilder>)
    
    
    public static IServiceCollection AddRegionHealthSourcesClient(this IServiceCollection services, Action<IServiceProvider, RegionHealthSourcesClientBuilder> action)

Adds a singleton [RegionHealthSourcesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthSourcesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionHealthSourcesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionHealthSourcesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupManagerResizeRequestsClient(IServiceCollection, Action<RegionInstanceGroupManagerResizeRequestsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupManagerResizeRequestsClient(this IServiceCollection services, Action<RegionInstanceGroupManagerResizeRequestsClientBuilder> action = null)

Adds a singleton [RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagerResizeRequestsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstanceGroupManagerResizeRequestsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagerResizeRequestsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupManagerResizeRequestsClient(IServiceCollection, Action<IServiceProvider, RegionInstanceGroupManagerResizeRequestsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupManagerResizeRequestsClient(this IServiceCollection services, Action<IServiceProvider, RegionInstanceGroupManagerResizeRequestsClientBuilder> action)

Adds a singleton [RegionInstanceGroupManagerResizeRequestsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagerResizeRequestsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstanceGroupManagerResizeRequestsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagerResizeRequestsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupManagersClient(IServiceCollection, Action<RegionInstanceGroupManagersClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupManagersClient(this IServiceCollection services, Action<RegionInstanceGroupManagersClientBuilder> action = null)

Adds a singleton [RegionInstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstanceGroupManagersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupManagersClient(IServiceCollection, Action<IServiceProvider, RegionInstanceGroupManagersClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupManagersClient(this IServiceCollection services, Action<IServiceProvider, RegionInstanceGroupManagersClientBuilder> action)

Adds a singleton [RegionInstanceGroupManagersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstanceGroupManagersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupManagersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupsClient(IServiceCollection, Action<RegionInstanceGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupsClient(this IServiceCollection services, Action<RegionInstanceGroupsClientBuilder> action = null)

Adds a singleton [RegionInstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstanceGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceGroupsClient(IServiceCollection, Action<IServiceProvider, RegionInstanceGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceGroupsClient(this IServiceCollection services, Action<IServiceProvider, RegionInstanceGroupsClientBuilder> action)

Adds a singleton [RegionInstanceGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstanceGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceTemplatesClient(IServiceCollection, Action<RegionInstanceTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceTemplatesClient(this IServiceCollection services, Action<RegionInstanceTemplatesClientBuilder> action = null)

Adds a singleton [RegionInstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstanceTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstanceTemplatesClient(IServiceCollection, Action<IServiceProvider, RegionInstanceTemplatesClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstanceTemplatesClient(this IServiceCollection services, Action<IServiceProvider, RegionInstanceTemplatesClientBuilder> action)

Adds a singleton [RegionInstanceTemplatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceTemplatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstanceTemplatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstanceTemplatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstancesClient(IServiceCollection, Action<RegionInstancesClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstancesClient(this IServiceCollection services, Action<RegionInstancesClientBuilder> action = null)

Adds a singleton [RegionInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstancesClient(IServiceCollection, Action<IServiceProvider, RegionInstancesClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstancesClient(this IServiceCollection services, Action<IServiceProvider, RegionInstancesClientBuilder> action)

Adds a singleton [RegionInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstantSnapshotGroupsClient(IServiceCollection, Action<RegionInstantSnapshotGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstantSnapshotGroupsClient(this IServiceCollection services, Action<RegionInstantSnapshotGroupsClientBuilder> action = null)

Adds a singleton [RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstantSnapshotGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstantSnapshotGroupsClient(IServiceCollection, Action<IServiceProvider, RegionInstantSnapshotGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstantSnapshotGroupsClient(this IServiceCollection services, Action<IServiceProvider, RegionInstantSnapshotGroupsClientBuilder> action)

Adds a singleton [RegionInstantSnapshotGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstantSnapshotGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstantSnapshotsClient(IServiceCollection, Action<RegionInstantSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstantSnapshotsClient(this IServiceCollection services, Action<RegionInstantSnapshotsClientBuilder> action = null)

Adds a singleton [RegionInstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionInstantSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionInstantSnapshotsClient(IServiceCollection, Action<IServiceProvider, RegionInstantSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddRegionInstantSnapshotsClient(this IServiceCollection services, Action<IServiceProvider, RegionInstantSnapshotsClientBuilder> action)

Adds a singleton [RegionInstantSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionInstantSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionInstantSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNetworkEndpointGroupsClient(IServiceCollection, Action<RegionNetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionNetworkEndpointGroupsClient(this IServiceCollection services, Action<RegionNetworkEndpointGroupsClientBuilder> action = null)

Adds a singleton [RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionNetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNetworkEndpointGroupsClient(IServiceCollection, Action<IServiceProvider, RegionNetworkEndpointGroupsClientBuilder>)
    
    
    public static IServiceCollection AddRegionNetworkEndpointGroupsClient(this IServiceCollection services, Action<IServiceProvider, RegionNetworkEndpointGroupsClientBuilder> action)

Adds a singleton [RegionNetworkEndpointGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkEndpointGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionNetworkEndpointGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkEndpointGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNetworkFirewallPoliciesClient(IServiceCollection, Action<RegionNetworkFirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionNetworkFirewallPoliciesClient(this IServiceCollection services, Action<RegionNetworkFirewallPoliciesClientBuilder> action = null)

Adds a singleton [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkFirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionNetworkFirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkFirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNetworkFirewallPoliciesClient(IServiceCollection, Action<IServiceProvider, RegionNetworkFirewallPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionNetworkFirewallPoliciesClient(this IServiceCollection services, Action<IServiceProvider, RegionNetworkFirewallPoliciesClientBuilder> action)

Adds a singleton [RegionNetworkFirewallPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkFirewallPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionNetworkFirewallPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNetworkFirewallPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNotificationEndpointsClient(IServiceCollection, Action<RegionNotificationEndpointsClientBuilder>)
    
    
    public static IServiceCollection AddRegionNotificationEndpointsClient(this IServiceCollection services, Action<RegionNotificationEndpointsClientBuilder> action = null)

Adds a singleton [RegionNotificationEndpointsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNotificationEndpointsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionNotificationEndpointsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNotificationEndpointsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionNotificationEndpointsClient(IServiceCollection, Action<IServiceProvider, RegionNotificationEndpointsClientBuilder>)
    
    
    public static IServiceCollection AddRegionNotificationEndpointsClient(this IServiceCollection services, Action<IServiceProvider, RegionNotificationEndpointsClientBuilder> action)

Adds a singleton [RegionNotificationEndpointsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNotificationEndpointsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionNotificationEndpointsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionNotificationEndpointsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionOperationsClient(IServiceCollection, Action<RegionOperationsClientBuilder>)
    
    
    public static IServiceCollection AddRegionOperationsClient(this IServiceCollection services, Action<RegionOperationsClientBuilder> action = null)

Adds a singleton [RegionOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionOperationsClient(IServiceCollection, Action<IServiceProvider, RegionOperationsClientBuilder>)
    
    
    public static IServiceCollection AddRegionOperationsClient(this IServiceCollection services, Action<IServiceProvider, RegionOperationsClientBuilder> action)

Adds a singleton [RegionOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSecurityPoliciesClient(IServiceCollection, Action<RegionSecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSecurityPoliciesClient(this IServiceCollection services, Action<RegionSecurityPoliciesClientBuilder> action = null)

Adds a singleton [RegionSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionSecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSecurityPoliciesClient(IServiceCollection, Action<IServiceProvider, RegionSecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSecurityPoliciesClient(this IServiceCollection services, Action<IServiceProvider, RegionSecurityPoliciesClientBuilder> action)

Adds a singleton [RegionSecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionSecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSnapshotSettingsClient(IServiceCollection, Action<RegionSnapshotSettingsClientBuilder>)
    
    
    public static IServiceCollection AddRegionSnapshotSettingsClient(this IServiceCollection services, Action<RegionSnapshotSettingsClientBuilder> action = null)

Adds a singleton [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionSnapshotSettingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSnapshotSettingsClient(IServiceCollection, Action<IServiceProvider, RegionSnapshotSettingsClientBuilder>)
    
    
    public static IServiceCollection AddRegionSnapshotSettingsClient(this IServiceCollection services, Action<IServiceProvider, RegionSnapshotSettingsClientBuilder> action)

Adds a singleton [RegionSnapshotSettingsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionSnapshotSettingsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotSettingsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSnapshotsClient(IServiceCollection, Action<RegionSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddRegionSnapshotsClient(this IServiceCollection services, Action<RegionSnapshotsClientBuilder> action = null)

Adds a singleton [RegionSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSnapshotsClient(IServiceCollection, Action<IServiceProvider, RegionSnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddRegionSnapshotsClient(this IServiceCollection services, Action<IServiceProvider, RegionSnapshotsClientBuilder> action)

Adds a singleton [RegionSnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionSnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSslCertificatesClient(IServiceCollection, Action<RegionSslCertificatesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSslCertificatesClient(this IServiceCollection services, Action<RegionSslCertificatesClientBuilder> action = null)

Adds a singleton [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionSslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSslCertificatesClient(IServiceCollection, Action<IServiceProvider, RegionSslCertificatesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSslCertificatesClient(this IServiceCollection services, Action<IServiceProvider, RegionSslCertificatesClientBuilder> action)

Adds a singleton [RegionSslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionSslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslCertificatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSslPoliciesClient(IServiceCollection, Action<RegionSslPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSslPoliciesClient(this IServiceCollection services, Action<RegionSslPoliciesClientBuilder> action = null)

Adds a singleton [RegionSslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionSslPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionSslPoliciesClient(IServiceCollection, Action<IServiceProvider, RegionSslPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddRegionSslPoliciesClient(this IServiceCollection services, Action<IServiceProvider, RegionSslPoliciesClientBuilder> action)

Adds a singleton [RegionSslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionSslPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionSslPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetHttpProxiesClient(IServiceCollection, Action<RegionTargetHttpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetHttpProxiesClient(this IServiceCollection services, Action<RegionTargetHttpProxiesClientBuilder> action = null)

Adds a singleton [RegionTargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionTargetHttpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetHttpProxiesClient(IServiceCollection, Action<IServiceProvider, RegionTargetHttpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetHttpProxiesClient(this IServiceCollection services, Action<IServiceProvider, RegionTargetHttpProxiesClientBuilder> action)

Adds a singleton [RegionTargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionTargetHttpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetHttpsProxiesClient(IServiceCollection, Action<RegionTargetHttpsProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetHttpsProxiesClient(this IServiceCollection services, Action<RegionTargetHttpsProxiesClientBuilder> action = null)

Adds a singleton [RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpsProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionTargetHttpsProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpsProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetHttpsProxiesClient(IServiceCollection, Action<IServiceProvider, RegionTargetHttpsProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetHttpsProxiesClient(this IServiceCollection services, Action<IServiceProvider, RegionTargetHttpsProxiesClientBuilder> action)

Adds a singleton [RegionTargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpsProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionTargetHttpsProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetHttpsProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetTcpProxiesClient(IServiceCollection, Action<RegionTargetTcpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetTcpProxiesClient(this IServiceCollection services, Action<RegionTargetTcpProxiesClientBuilder> action = null)

Adds a singleton [RegionTargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetTcpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionTargetTcpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetTcpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionTargetTcpProxiesClient(IServiceCollection, Action<IServiceProvider, RegionTargetTcpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddRegionTargetTcpProxiesClient(this IServiceCollection services, Action<IServiceProvider, RegionTargetTcpProxiesClientBuilder> action)

Adds a singleton [RegionTargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetTcpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionTargetTcpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionTargetTcpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionUrlMapsClient(IServiceCollection, Action<RegionUrlMapsClientBuilder>)
    
    
    public static IServiceCollection AddRegionUrlMapsClient(this IServiceCollection services, Action<RegionUrlMapsClientBuilder> action = null)

Adds a singleton [RegionUrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionUrlMapsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionUrlMapsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionUrlMapsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionUrlMapsClient(IServiceCollection, Action<IServiceProvider, RegionUrlMapsClientBuilder>)
    
    
    public static IServiceCollection AddRegionUrlMapsClient(this IServiceCollection services, Action<IServiceProvider, RegionUrlMapsClientBuilder> action)

Adds a singleton [RegionUrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionUrlMapsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionUrlMapsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionUrlMapsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionZonesClient(IServiceCollection, Action<RegionZonesClientBuilder>)
    
    
    public static IServiceCollection AddRegionZonesClient(this IServiceCollection services, Action<RegionZonesClientBuilder> action = null)

Adds a singleton [RegionZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionZonesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionZonesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionZonesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionZonesClient(IServiceCollection, Action<IServiceProvider, RegionZonesClientBuilder>)
    
    
    public static IServiceCollection AddRegionZonesClient(this IServiceCollection services, Action<IServiceProvider, RegionZonesClientBuilder> action)

Adds a singleton [RegionZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionZonesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionZonesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionZonesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionsClient(IServiceCollection, Action<RegionsClientBuilder>)
    
    
    public static IServiceCollection AddRegionsClient(this IServiceCollection services, Action<RegionsClientBuilder> action = null)

Adds a singleton [RegionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RegionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRegionsClient(IServiceCollection, Action<IServiceProvider, RegionsClientBuilder>)
    
    
    public static IServiceCollection AddRegionsClient(this IServiceCollection services, Action<IServiceProvider, RegionsClientBuilder> action)

Adds a singleton [RegionsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RegionsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RegionsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReliabilityRisksClient(IServiceCollection, Action<ReliabilityRisksClientBuilder>)
    
    
    public static IServiceCollection AddReliabilityRisksClient(this IServiceCollection services, Action<ReliabilityRisksClientBuilder> action = null)

Adds a singleton [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReliabilityRisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReliabilityRisksClient(IServiceCollection, Action<IServiceProvider, ReliabilityRisksClientBuilder>)
    
    
    public static IServiceCollection AddReliabilityRisksClient(this IServiceCollection services, Action<IServiceProvider, ReliabilityRisksClientBuilder> action)

Adds a singleton [ReliabilityRisksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReliabilityRisksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReliabilityRisksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationBlocksClient(IServiceCollection, Action<ReservationBlocksClientBuilder>)
    
    
    public static IServiceCollection AddReservationBlocksClient(this IServiceCollection services, Action<ReservationBlocksClientBuilder> action = null)

Adds a singleton [ReservationBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationBlocksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReservationBlocksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationBlocksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationBlocksClient(IServiceCollection, Action<IServiceProvider, ReservationBlocksClientBuilder>)
    
    
    public static IServiceCollection AddReservationBlocksClient(this IServiceCollection services, Action<IServiceProvider, ReservationBlocksClientBuilder> action)

Adds a singleton [ReservationBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationBlocksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReservationBlocksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationBlocksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationSlotsClient(IServiceCollection, Action<ReservationSlotsClientBuilder>)
    
    
    public static IServiceCollection AddReservationSlotsClient(this IServiceCollection services, Action<ReservationSlotsClientBuilder> action = null)

Adds a singleton [ReservationSlotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReservationSlotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationSlotsClient(IServiceCollection, Action<IServiceProvider, ReservationSlotsClientBuilder>)
    
    
    public static IServiceCollection AddReservationSlotsClient(this IServiceCollection services, Action<IServiceProvider, ReservationSlotsClientBuilder> action)

Adds a singleton [ReservationSlotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReservationSlotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSlotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationSubBlocksClient(IServiceCollection, Action<ReservationSubBlocksClientBuilder>)
    
    
    public static IServiceCollection AddReservationSubBlocksClient(this IServiceCollection services, Action<ReservationSubBlocksClientBuilder> action = null)

Adds a singleton [ReservationSubBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSubBlocksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReservationSubBlocksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSubBlocksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationSubBlocksClient(IServiceCollection, Action<IServiceProvider, ReservationSubBlocksClientBuilder>)
    
    
    public static IServiceCollection AddReservationSubBlocksClient(this IServiceCollection services, Action<IServiceProvider, ReservationSubBlocksClientBuilder> action)

Adds a singleton [ReservationSubBlocksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSubBlocksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReservationSubBlocksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationSubBlocksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationsClient(IServiceCollection, Action<ReservationsClientBuilder>)
    
    
    public static IServiceCollection AddReservationsClient(this IServiceCollection services, Action<ReservationsClientBuilder> action = null)

Adds a singleton [ReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReservationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReservationsClient(IServiceCollection, Action<IServiceProvider, ReservationsClientBuilder>)
    
    
    public static IServiceCollection AddReservationsClient(this IServiceCollection services, Action<IServiceProvider, ReservationsClientBuilder> action)

Adds a singleton [ReservationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReservationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ReservationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddResourcePoliciesClient(IServiceCollection, Action<ResourcePoliciesClientBuilder>)
    
    
    public static IServiceCollection AddResourcePoliciesClient(this IServiceCollection services, Action<ResourcePoliciesClientBuilder> action = null)

Adds a singleton [ResourcePoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourcePoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ResourcePoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourcePoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddResourcePoliciesClient(IServiceCollection, Action<IServiceProvider, ResourcePoliciesClientBuilder>)
    
    
    public static IServiceCollection AddResourcePoliciesClient(this IServiceCollection services, Action<IServiceProvider, ResourcePoliciesClientBuilder> action)

Adds a singleton [ResourcePoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourcePoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ResourcePoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ResourcePoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRolloutPlansClient(IServiceCollection, Action<RolloutPlansClientBuilder>)
    
    
    public static IServiceCollection AddRolloutPlansClient(this IServiceCollection services, Action<RolloutPlansClientBuilder> action = null)

Adds a singleton [RolloutPlansClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutPlansClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RolloutPlansClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutPlansClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRolloutPlansClient(IServiceCollection, Action<IServiceProvider, RolloutPlansClientBuilder>)
    
    
    public static IServiceCollection AddRolloutPlansClient(this IServiceCollection services, Action<IServiceProvider, RolloutPlansClientBuilder> action)

Adds a singleton [RolloutPlansClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutPlansClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RolloutPlansClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutPlansClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRolloutsClient(IServiceCollection, Action<RolloutsClientBuilder>)
    
    
    public static IServiceCollection AddRolloutsClient(this IServiceCollection services, Action<RolloutsClientBuilder> action = null)

Adds a singleton [RolloutsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RolloutsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRolloutsClient(IServiceCollection, Action<IServiceProvider, RolloutsClientBuilder>)
    
    
    public static IServiceCollection AddRolloutsClient(this IServiceCollection services, Action<IServiceProvider, RolloutsClientBuilder> action)

Adds a singleton [RolloutsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RolloutsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RolloutsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRoutersClient(IServiceCollection, Action<RoutersClientBuilder>)
    
    
    public static IServiceCollection AddRoutersClient(this IServiceCollection services, Action<RoutersClientBuilder> action = null)

Adds a singleton [RoutersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RoutersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRoutersClient(IServiceCollection, Action<IServiceProvider, RoutersClientBuilder>)
    
    
    public static IServiceCollection AddRoutersClient(this IServiceCollection services, Action<IServiceProvider, RoutersClientBuilder> action)

Adds a singleton [RoutersClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutersClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RoutersClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutersClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRoutesClient(IServiceCollection, Action<RoutesClientBuilder>)
    
    
    public static IServiceCollection AddRoutesClient(this IServiceCollection services, Action<RoutesClientBuilder> action = null)

Adds a singleton [RoutesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[RoutesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddRoutesClient(IServiceCollection, Action<IServiceProvider, RoutesClientBuilder>)
    
    
    public static IServiceCollection AddRoutesClient(this IServiceCollection services, Action<IServiceProvider, RoutesClientBuilder> action)

Adds a singleton [RoutesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[RoutesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.RoutesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSecurityPoliciesClient(IServiceCollection, Action<SecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddSecurityPoliciesClient(this IServiceCollection services, Action<SecurityPoliciesClientBuilder> action = null)

Adds a singleton [SecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSecurityPoliciesClient(IServiceCollection, Action<IServiceProvider, SecurityPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddSecurityPoliciesClient(this IServiceCollection services, Action<IServiceProvider, SecurityPoliciesClientBuilder> action)

Adds a singleton [SecurityPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecurityPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SecurityPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SecurityPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddServiceAttachmentsClient(IServiceCollection, Action<ServiceAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddServiceAttachmentsClient(this IServiceCollection services, Action<ServiceAttachmentsClientBuilder> action = null)

Adds a singleton [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ServiceAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddServiceAttachmentsClient(IServiceCollection, Action<IServiceProvider, ServiceAttachmentsClientBuilder>)
    
    
    public static IServiceCollection AddServiceAttachmentsClient(this IServiceCollection services, Action<IServiceProvider, ServiceAttachmentsClientBuilder> action)

Adds a singleton [ServiceAttachmentsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ServiceAttachmentsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ServiceAttachmentsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSnapshotSettingsServiceClient(IServiceCollection, Action<SnapshotSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddSnapshotSettingsServiceClient(this IServiceCollection services, Action<SnapshotSettingsServiceClientBuilder> action = null)

Adds a singleton [SnapshotSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SnapshotSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSnapshotSettingsServiceClient(IServiceCollection, Action<IServiceProvider, SnapshotSettingsServiceClientBuilder>)
    
    
    public static IServiceCollection AddSnapshotSettingsServiceClient(this IServiceCollection services, Action<IServiceProvider, SnapshotSettingsServiceClientBuilder> action)

Adds a singleton [SnapshotSettingsServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettingsServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SnapshotSettingsServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotSettingsServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSnapshotsClient(IServiceCollection, Action<SnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddSnapshotsClient(this IServiceCollection services, Action<SnapshotsClientBuilder> action = null)

Adds a singleton [SnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSnapshotsClient(IServiceCollection, Action<IServiceProvider, SnapshotsClientBuilder>)
    
    
    public static IServiceCollection AddSnapshotsClient(this IServiceCollection services, Action<IServiceProvider, SnapshotsClientBuilder> action)

Adds a singleton [SnapshotsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SnapshotsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SnapshotsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSslCertificatesClient(IServiceCollection, Action<SslCertificatesClientBuilder>)
    
    
    public static IServiceCollection AddSslCertificatesClient(this IServiceCollection services, Action<SslCertificatesClientBuilder> action = null)

Adds a singleton [SslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSslCertificatesClient(IServiceCollection, Action<IServiceProvider, SslCertificatesClientBuilder>)
    
    
    public static IServiceCollection AddSslCertificatesClient(this IServiceCollection services, Action<IServiceProvider, SslCertificatesClientBuilder> action)

Adds a singleton [SslCertificatesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificatesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SslCertificatesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslCertificatesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSslPoliciesClient(IServiceCollection, Action<SslPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddSslPoliciesClient(this IServiceCollection services, Action<SslPoliciesClientBuilder> action = null)

Adds a singleton [SslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SslPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSslPoliciesClient(IServiceCollection, Action<IServiceProvider, SslPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddSslPoliciesClient(this IServiceCollection services, Action<IServiceProvider, SslPoliciesClientBuilder> action)

Adds a singleton [SslPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SslPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SslPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddStoragePoolTypesClient(IServiceCollection, Action<StoragePoolTypesClientBuilder>)
    
    
    public static IServiceCollection AddStoragePoolTypesClient(this IServiceCollection services, Action<StoragePoolTypesClientBuilder> action = null)

Adds a singleton [StoragePoolTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[StoragePoolTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddStoragePoolTypesClient(IServiceCollection, Action<IServiceProvider, StoragePoolTypesClientBuilder>)
    
    
    public static IServiceCollection AddStoragePoolTypesClient(this IServiceCollection services, Action<IServiceProvider, StoragePoolTypesClientBuilder> action)

Adds a singleton [StoragePoolTypesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolTypesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[StoragePoolTypesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolTypesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddStoragePoolsClient(IServiceCollection, Action<StoragePoolsClientBuilder>)
    
    
    public static IServiceCollection AddStoragePoolsClient(this IServiceCollection services, Action<StoragePoolsClientBuilder> action = null)

Adds a singleton [StoragePoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[StoragePoolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddStoragePoolsClient(IServiceCollection, Action<IServiceProvider, StoragePoolsClientBuilder>)
    
    
    public static IServiceCollection AddStoragePoolsClient(this IServiceCollection services, Action<IServiceProvider, StoragePoolsClientBuilder> action)

Adds a singleton [StoragePoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[StoragePoolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.StoragePoolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSubnetworksClient(IServiceCollection, Action<SubnetworksClientBuilder>)
    
    
    public static IServiceCollection AddSubnetworksClient(this IServiceCollection services, Action<SubnetworksClientBuilder> action = null)

Adds a singleton [SubnetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SubnetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSubnetworksClient(IServiceCollection, Action<IServiceProvider, SubnetworksClientBuilder>)
    
    
    public static IServiceCollection AddSubnetworksClient(this IServiceCollection services, Action<IServiceProvider, SubnetworksClientBuilder> action)

Adds a singleton [SubnetworksClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworksClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SubnetworksClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.SubnetworksClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetGrpcProxiesClient(IServiceCollection, Action<TargetGrpcProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetGrpcProxiesClient(this IServiceCollection services, Action<TargetGrpcProxiesClientBuilder> action = null)

Adds a singleton [TargetGrpcProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetGrpcProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetGrpcProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetGrpcProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetGrpcProxiesClient(IServiceCollection, Action<IServiceProvider, TargetGrpcProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetGrpcProxiesClient(this IServiceCollection services, Action<IServiceProvider, TargetGrpcProxiesClientBuilder> action)

Adds a singleton [TargetGrpcProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetGrpcProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetGrpcProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetGrpcProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetHttpProxiesClient(IServiceCollection, Action<TargetHttpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetHttpProxiesClient(this IServiceCollection services, Action<TargetHttpProxiesClientBuilder> action = null)

Adds a singleton [TargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetHttpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetHttpProxiesClient(IServiceCollection, Action<IServiceProvider, TargetHttpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetHttpProxiesClient(this IServiceCollection services, Action<IServiceProvider, TargetHttpProxiesClientBuilder> action)

Adds a singleton [TargetHttpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetHttpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetHttpsProxiesClient(IServiceCollection, Action<TargetHttpsProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetHttpsProxiesClient(this IServiceCollection services, Action<TargetHttpsProxiesClientBuilder> action = null)

Adds a singleton [TargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpsProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetHttpsProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpsProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetHttpsProxiesClient(IServiceCollection, Action<IServiceProvider, TargetHttpsProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetHttpsProxiesClient(this IServiceCollection services, Action<IServiceProvider, TargetHttpsProxiesClientBuilder> action)

Adds a singleton [TargetHttpsProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpsProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetHttpsProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetHttpsProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetInstancesClient(IServiceCollection, Action<TargetInstancesClientBuilder>)
    
    
    public static IServiceCollection AddTargetInstancesClient(this IServiceCollection services, Action<TargetInstancesClientBuilder> action = null)

Adds a singleton [TargetInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetInstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetInstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetInstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetInstancesClient(IServiceCollection, Action<IServiceProvider, TargetInstancesClientBuilder>)
    
    
    public static IServiceCollection AddTargetInstancesClient(this IServiceCollection services, Action<IServiceProvider, TargetInstancesClientBuilder> action)

Adds a singleton [TargetInstancesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetInstancesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetInstancesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetInstancesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetPoolsClient(IServiceCollection, Action<TargetPoolsClientBuilder>)
    
    
    public static IServiceCollection AddTargetPoolsClient(this IServiceCollection services, Action<TargetPoolsClientBuilder> action = null)

Adds a singleton [TargetPoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetPoolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetPoolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetPoolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetPoolsClient(IServiceCollection, Action<IServiceProvider, TargetPoolsClientBuilder>)
    
    
    public static IServiceCollection AddTargetPoolsClient(this IServiceCollection services, Action<IServiceProvider, TargetPoolsClientBuilder> action)

Adds a singleton [TargetPoolsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetPoolsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetPoolsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetPoolsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetSslProxiesClient(IServiceCollection, Action<TargetSslProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetSslProxiesClient(this IServiceCollection services, Action<TargetSslProxiesClientBuilder> action = null)

Adds a singleton [TargetSslProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetSslProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetSslProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetSslProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetSslProxiesClient(IServiceCollection, Action<IServiceProvider, TargetSslProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetSslProxiesClient(this IServiceCollection services, Action<IServiceProvider, TargetSslProxiesClientBuilder> action)

Adds a singleton [TargetSslProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetSslProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetSslProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetSslProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetTcpProxiesClient(IServiceCollection, Action<TargetTcpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetTcpProxiesClient(this IServiceCollection services, Action<TargetTcpProxiesClientBuilder> action = null)

Adds a singleton [TargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetTcpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetTcpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetTcpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetTcpProxiesClient(IServiceCollection, Action<IServiceProvider, TargetTcpProxiesClientBuilder>)
    
    
    public static IServiceCollection AddTargetTcpProxiesClient(this IServiceCollection services, Action<IServiceProvider, TargetTcpProxiesClientBuilder> action)

Adds a singleton [TargetTcpProxiesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetTcpProxiesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetTcpProxiesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetTcpProxiesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetVpnGatewaysClient(IServiceCollection, Action<TargetVpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddTargetVpnGatewaysClient(this IServiceCollection services, Action<TargetVpnGatewaysClientBuilder> action = null)

Adds a singleton [TargetVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetVpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TargetVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetVpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTargetVpnGatewaysClient(IServiceCollection, Action<IServiceProvider, TargetVpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddTargetVpnGatewaysClient(this IServiceCollection services, Action<IServiceProvider, TargetVpnGatewaysClientBuilder> action)

Adds a singleton [TargetVpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetVpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TargetVpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.TargetVpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddUrlMapsClient(IServiceCollection, Action<UrlMapsClientBuilder>)
    
    
    public static IServiceCollection AddUrlMapsClient(this IServiceCollection services, Action<UrlMapsClientBuilder> action = null)

Adds a singleton [UrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UrlMapsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[UrlMapsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UrlMapsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddUrlMapsClient(IServiceCollection, Action<IServiceProvider, UrlMapsClientBuilder>)
    
    
    public static IServiceCollection AddUrlMapsClient(this IServiceCollection services, Action<IServiceProvider, UrlMapsClientBuilder> action)

Adds a singleton [UrlMapsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UrlMapsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[UrlMapsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.UrlMapsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVpnGatewaysClient(IServiceCollection, Action<VpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddVpnGatewaysClient(this IServiceCollection services, Action<VpnGatewaysClientBuilder> action = null)

Adds a singleton [VpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVpnGatewaysClient(IServiceCollection, Action<IServiceProvider, VpnGatewaysClientBuilder>)
    
    
    public static IServiceCollection AddVpnGatewaysClient(this IServiceCollection services, Action<IServiceProvider, VpnGatewaysClientBuilder> action)

Adds a singleton [VpnGatewaysClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnGatewaysClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VpnGatewaysClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnGatewaysClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVpnTunnelsClient(IServiceCollection, Action<VpnTunnelsClientBuilder>)
    
    
    public static IServiceCollection AddVpnTunnelsClient(this IServiceCollection services, Action<VpnTunnelsClientBuilder> action = null)

Adds a singleton [VpnTunnelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnTunnelsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VpnTunnelsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnTunnelsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVpnTunnelsClient(IServiceCollection, Action<IServiceProvider, VpnTunnelsClientBuilder>)
    
    
    public static IServiceCollection AddVpnTunnelsClient(this IServiceCollection services, Action<IServiceProvider, VpnTunnelsClientBuilder> action)

Adds a singleton [VpnTunnelsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnTunnelsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VpnTunnelsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.VpnTunnelsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddWireGroupsClient(IServiceCollection, Action<WireGroupsClientBuilder>)
    
    
    public static IServiceCollection AddWireGroupsClient(this IServiceCollection services, Action<WireGroupsClientBuilder> action = null)

Adds a singleton [WireGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.WireGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[WireGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.WireGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddWireGroupsClient(IServiceCollection, Action<IServiceProvider, WireGroupsClientBuilder>)
    
    
    public static IServiceCollection AddWireGroupsClient(this IServiceCollection services, Action<IServiceProvider, WireGroupsClientBuilder> action)

Adds a singleton [WireGroupsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.WireGroupsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[WireGroupsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.WireGroupsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZoneOperationsClient(IServiceCollection, Action<ZoneOperationsClientBuilder>)
    
    
    public static IServiceCollection AddZoneOperationsClient(this IServiceCollection services, Action<ZoneOperationsClientBuilder> action = null)

Adds a singleton [ZoneOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ZoneOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZoneOperationsClient(IServiceCollection, Action<IServiceProvider, ZoneOperationsClientBuilder>)
    
    
    public static IServiceCollection AddZoneOperationsClient(this IServiceCollection services, Action<IServiceProvider, ZoneOperationsClientBuilder> action)

Adds a singleton [ZoneOperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneOperationsClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ZoneOperationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneOperationsClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZoneVmExtensionPoliciesClient(IServiceCollection, Action<ZoneVmExtensionPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddZoneVmExtensionPoliciesClient(this IServiceCollection services, Action<ZoneVmExtensionPoliciesClientBuilder> action = null)

Adds a singleton [ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ZoneVmExtensionPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZoneVmExtensionPoliciesClient(IServiceCollection, Action<IServiceProvider, ZoneVmExtensionPoliciesClientBuilder>)
    
    
    public static IServiceCollection AddZoneVmExtensionPoliciesClient(this IServiceCollection services, Action<IServiceProvider, ZoneVmExtensionPoliciesClientBuilder> action)

Adds a singleton [ZoneVmExtensionPoliciesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPoliciesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ZoneVmExtensionPoliciesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZoneVmExtensionPoliciesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZonesClient(IServiceCollection, Action<ZonesClientBuilder>)
    
    
    public static IServiceCollection AddZonesClient(this IServiceCollection services, Action<ZonesClientBuilder> action = null)

Adds a singleton [ZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZonesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ZonesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZonesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddZonesClient(IServiceCollection, Action<IServiceProvider, ZonesClientBuilder>)
    
    
    public static IServiceCollection AddZonesClient(this IServiceCollection services, Action<IServiceProvider, ZonesClientBuilder> action)

Adds a singleton [ZonesClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZonesClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ZonesClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Compute.V1/latest/Google.Cloud.Compute.V1.ZonesClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
