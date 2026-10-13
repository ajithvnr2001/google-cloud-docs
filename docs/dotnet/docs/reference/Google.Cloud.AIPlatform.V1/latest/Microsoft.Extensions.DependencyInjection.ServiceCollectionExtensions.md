---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Vertex AI v1 API - Class ServiceCollectionExtensions (3.77.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:35:20.186663+00:00
---

# Vertex AI v1 API - Class ServiceCollectionExtensions (3.77.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1 API - Class ServiceCollectionExtensions (3.77.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.77.0 (latest)  3.76.0  3.75.0  3.74.0  3.73.0  3.72.0  3.71.0  3.70.0  3.69.0  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.28.0  2.27.0  2.26.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Vertex AI v1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.AIPlatform.V1.dll

## Methods 

### AddDataFoundryServiceClient(IServiceCollection, Action<DataFoundryServiceClientBuilder>)
    
    
    public static IServiceCollection AddDataFoundryServiceClient(this IServiceCollection services, Action<DataFoundryServiceClientBuilder> action = null)

Adds a singleton [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DataFoundryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDataFoundryServiceClient(IServiceCollection, Action<IServiceProvider, DataFoundryServiceClientBuilder>)
    
    
    public static IServiceCollection AddDataFoundryServiceClient(this IServiceCollection services, Action<IServiceProvider, DataFoundryServiceClientBuilder> action)

Adds a singleton [DataFoundryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DataFoundryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DataFoundryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDatasetServiceClient(IServiceCollection, Action<DatasetServiceClientBuilder>)
    
    
    public static IServiceCollection AddDatasetServiceClient(this IServiceCollection services, Action<DatasetServiceClientBuilder> action = null)

Adds a singleton [DatasetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DatasetServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DatasetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DatasetServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDatasetServiceClient(IServiceCollection, Action<IServiceProvider, DatasetServiceClientBuilder>)
    
    
    public static IServiceCollection AddDatasetServiceClient(this IServiceCollection services, Action<IServiceProvider, DatasetServiceClientBuilder> action)

Adds a singleton [DatasetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DatasetServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DatasetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DatasetServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDeploymentResourcePoolServiceClient(IServiceCollection, Action<DeploymentResourcePoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddDeploymentResourcePoolServiceClient(this IServiceCollection services, Action<DeploymentResourcePoolServiceClientBuilder> action = null)

Adds a singleton [DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DeploymentResourcePoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDeploymentResourcePoolServiceClient(IServiceCollection, Action<IServiceProvider, DeploymentResourcePoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddDeploymentResourcePoolServiceClient(this IServiceCollection services, Action<IServiceProvider, DeploymentResourcePoolServiceClientBuilder> action)

Adds a singleton [DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DeploymentResourcePoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.DeploymentResourcePoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEndpointServiceClient(IServiceCollection, Action<EndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddEndpointServiceClient(this IServiceCollection services, Action<EndpointServiceClientBuilder> action = null)

Adds a singleton [EndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEndpointServiceClient(IServiceCollection, Action<IServiceProvider, EndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddEndpointServiceClient(this IServiceCollection services, Action<IServiceProvider, EndpointServiceClientBuilder> action)

Adds a singleton [EndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEvaluationServiceClient(IServiceCollection, Action<EvaluationServiceClientBuilder>)
    
    
    public static IServiceCollection AddEvaluationServiceClient(this IServiceCollection services, Action<EvaluationServiceClientBuilder> action = null)

Adds a singleton [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EvaluationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEvaluationServiceClient(IServiceCollection, Action<IServiceProvider, EvaluationServiceClientBuilder>)
    
    
    public static IServiceCollection AddEvaluationServiceClient(this IServiceCollection services, Action<IServiceProvider, EvaluationServiceClientBuilder> action)

Adds a singleton [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EvaluationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.EvaluationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreAdminServiceClient(IServiceCollection, Action<FeatureOnlineStoreAdminServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreAdminServiceClient(this IServiceCollection services, Action<FeatureOnlineStoreAdminServiceClientBuilder> action = null)

Adds a singleton [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreAdminServiceClient(IServiceCollection, Action<IServiceProvider, FeatureOnlineStoreAdminServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreAdminServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureOnlineStoreAdminServiceClientBuilder> action)

Adds a singleton [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreAdminServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreServiceClient(IServiceCollection, Action<FeatureOnlineStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreServiceClient(this IServiceCollection services, Action<FeatureOnlineStoreServiceClientBuilder> action = null)

Adds a singleton [FeatureOnlineStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureOnlineStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreServiceClient(IServiceCollection, Action<IServiceProvider, FeatureOnlineStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureOnlineStoreServiceClientBuilder> action)

Adds a singleton [FeatureOnlineStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureOnlineStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureOnlineStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureRegistryServiceClient(IServiceCollection, Action<FeatureRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureRegistryServiceClient(this IServiceCollection services, Action<FeatureRegistryServiceClientBuilder> action = null)

Adds a singleton [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureRegistryServiceClient(IServiceCollection, Action<IServiceProvider, FeatureRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureRegistryServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureRegistryServiceClientBuilder> action)

Adds a singleton [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeatureRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreOnlineServingServiceClient(IServiceCollection, Action<FeaturestoreOnlineServingServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreOnlineServingServiceClient(this IServiceCollection services, Action<FeaturestoreOnlineServingServiceClientBuilder> action = null)

Adds a singleton [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreOnlineServingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeaturestoreOnlineServingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreOnlineServingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreOnlineServingServiceClient(IServiceCollection, Action<IServiceProvider, FeaturestoreOnlineServingServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreOnlineServingServiceClient(this IServiceCollection services, Action<IServiceProvider, FeaturestoreOnlineServingServiceClientBuilder> action)

Adds a singleton [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreOnlineServingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeaturestoreOnlineServingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreOnlineServingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreServiceClient(IServiceCollection, Action<FeaturestoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreServiceClient(this IServiceCollection services, Action<FeaturestoreServiceClientBuilder> action = null)

Adds a singleton [FeaturestoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeaturestoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreServiceClient(IServiceCollection, Action<IServiceProvider, FeaturestoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreServiceClient(this IServiceCollection services, Action<IServiceProvider, FeaturestoreServiceClientBuilder> action)

Adds a singleton [FeaturestoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeaturestoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.FeaturestoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiCacheServiceClient(IServiceCollection, Action<GenAiCacheServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiCacheServiceClient(this IServiceCollection services, Action<GenAiCacheServiceClientBuilder> action = null)

Adds a singleton [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiCacheServiceClient(IServiceCollection, Action<IServiceProvider, GenAiCacheServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiCacheServiceClient(this IServiceCollection services, Action<IServiceProvider, GenAiCacheServiceClientBuilder> action)

Adds a singleton [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiCacheServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiTuningServiceClient(IServiceCollection, Action<GenAiTuningServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiTuningServiceClient(this IServiceCollection services, Action<GenAiTuningServiceClientBuilder> action = null)

Adds a singleton [GenAiTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiTuningServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GenAiTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiTuningServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiTuningServiceClient(IServiceCollection, Action<IServiceProvider, GenAiTuningServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiTuningServiceClient(this IServiceCollection services, Action<IServiceProvider, GenAiTuningServiceClientBuilder> action)

Adds a singleton [GenAiTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiTuningServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GenAiTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.GenAiTuningServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexEndpointServiceClient(IServiceCollection, Action<IndexEndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexEndpointServiceClient(this IServiceCollection services, Action<IndexEndpointServiceClientBuilder> action = null)

Adds a singleton [IndexEndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexEndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IndexEndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexEndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexEndpointServiceClient(IServiceCollection, Action<IServiceProvider, IndexEndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexEndpointServiceClient(this IServiceCollection services, Action<IServiceProvider, IndexEndpointServiceClientBuilder> action)

Adds a singleton [IndexEndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexEndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[IndexEndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexEndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexServiceClient(IServiceCollection, Action<IndexServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexServiceClient(this IServiceCollection services, Action<IndexServiceClientBuilder> action = null)

Adds a singleton [IndexServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IndexServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexServiceClient(IServiceCollection, Action<IServiceProvider, IndexServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexServiceClient(this IServiceCollection services, Action<IServiceProvider, IndexServiceClientBuilder> action)

Adds a singleton [IndexServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[IndexServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.IndexServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddJobServiceClient(IServiceCollection, Action<JobServiceClientBuilder>)
    
    
    public static IServiceCollection AddJobServiceClient(this IServiceCollection services, Action<JobServiceClientBuilder> action = null)

Adds a singleton [JobServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.JobServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[JobServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.JobServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddJobServiceClient(IServiceCollection, Action<IServiceProvider, JobServiceClientBuilder>)
    
    
    public static IServiceCollection AddJobServiceClient(this IServiceCollection services, Action<IServiceProvider, JobServiceClientBuilder> action)

Adds a singleton [JobServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.JobServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[JobServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.JobServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLlmUtilityServiceClient(IServiceCollection, Action<LlmUtilityServiceClientBuilder>)
    
    
    public static IServiceCollection AddLlmUtilityServiceClient(this IServiceCollection services, Action<LlmUtilityServiceClientBuilder> action = null)

Adds a singleton [LlmUtilityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.LlmUtilityServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[LlmUtilityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.LlmUtilityServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLlmUtilityServiceClient(IServiceCollection, Action<IServiceProvider, LlmUtilityServiceClientBuilder>)
    
    
    public static IServiceCollection AddLlmUtilityServiceClient(this IServiceCollection services, Action<IServiceProvider, LlmUtilityServiceClientBuilder> action)

Adds a singleton [LlmUtilityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.LlmUtilityServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[LlmUtilityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.LlmUtilityServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMatchServiceClient(IServiceCollection, Action<MatchServiceClientBuilder>)
    
    
    public static IServiceCollection AddMatchServiceClient(this IServiceCollection services, Action<MatchServiceClientBuilder> action = null)

Adds a singleton [MatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MatchServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MatchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MatchServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMatchServiceClient(IServiceCollection, Action<IServiceProvider, MatchServiceClientBuilder>)
    
    
    public static IServiceCollection AddMatchServiceClient(this IServiceCollection services, Action<IServiceProvider, MatchServiceClientBuilder> action)

Adds a singleton [MatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MatchServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MatchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MatchServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMetadataServiceClient(IServiceCollection, Action<MetadataServiceClientBuilder>)
    
    
    public static IServiceCollection AddMetadataServiceClient(this IServiceCollection services, Action<MetadataServiceClientBuilder> action = null)

Adds a singleton [MetadataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetadataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MetadataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetadataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMetadataServiceClient(IServiceCollection, Action<IServiceProvider, MetadataServiceClientBuilder>)
    
    
    public static IServiceCollection AddMetadataServiceClient(this IServiceCollection services, Action<IServiceProvider, MetadataServiceClientBuilder> action)

Adds a singleton [MetadataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetadataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MetadataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MetadataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMigrationServiceClient(IServiceCollection, Action<MigrationServiceClientBuilder>)
    
    
    public static IServiceCollection AddMigrationServiceClient(this IServiceCollection services, Action<MigrationServiceClientBuilder> action = null)

Adds a singleton [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MigrationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MigrationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMigrationServiceClient(IServiceCollection, Action<IServiceProvider, MigrationServiceClientBuilder>)
    
    
    public static IServiceCollection AddMigrationServiceClient(this IServiceCollection services, Action<IServiceProvider, MigrationServiceClientBuilder> action)

Adds a singleton [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MigrationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.MigrationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelGardenServiceClient(IServiceCollection, Action<ModelGardenServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelGardenServiceClient(this IServiceCollection services, Action<ModelGardenServiceClientBuilder> action = null)

Adds a singleton [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelGardenServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelGardenServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelGardenServiceClient(IServiceCollection, Action<IServiceProvider, ModelGardenServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelGardenServiceClient(this IServiceCollection services, Action<IServiceProvider, ModelGardenServiceClientBuilder> action)

Adds a singleton [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelGardenServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelGardenServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelServiceClient(IServiceCollection, Action<ModelServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelServiceClient(this IServiceCollection services, Action<ModelServiceClientBuilder> action = null)

Adds a singleton [ModelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ModelServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelServiceClient(IServiceCollection, Action<IServiceProvider, ModelServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelServiceClient(this IServiceCollection services, Action<IServiceProvider, ModelServiceClientBuilder> action)

Adds a singleton [ModelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ModelServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ModelServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNotebookServiceClient(IServiceCollection, Action<NotebookServiceClientBuilder>)
    
    
    public static IServiceCollection AddNotebookServiceClient(this IServiceCollection services, Action<NotebookServiceClientBuilder> action = null)

Adds a singleton [NotebookServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.NotebookServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NotebookServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.NotebookServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNotebookServiceClient(IServiceCollection, Action<IServiceProvider, NotebookServiceClientBuilder>)
    
    
    public static IServiceCollection AddNotebookServiceClient(this IServiceCollection services, Action<IServiceProvider, NotebookServiceClientBuilder> action)

Adds a singleton [NotebookServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.NotebookServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NotebookServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.NotebookServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPersistentResourceServiceClient(IServiceCollection, Action<PersistentResourceServiceClientBuilder>)
    
    
    public static IServiceCollection AddPersistentResourceServiceClient(this IServiceCollection services, Action<PersistentResourceServiceClientBuilder> action = null)

Adds a singleton [PersistentResourceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PersistentResourceServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PersistentResourceServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PersistentResourceServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPersistentResourceServiceClient(IServiceCollection, Action<IServiceProvider, PersistentResourceServiceClientBuilder>)
    
    
    public static IServiceCollection AddPersistentResourceServiceClient(this IServiceCollection services, Action<IServiceProvider, PersistentResourceServiceClientBuilder> action)

Adds a singleton [PersistentResourceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PersistentResourceServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PersistentResourceServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PersistentResourceServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPipelineServiceClient(IServiceCollection, Action<PipelineServiceClientBuilder>)
    
    
    public static IServiceCollection AddPipelineServiceClient(this IServiceCollection services, Action<PipelineServiceClientBuilder> action = null)

Adds a singleton [PipelineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PipelineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PipelineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PipelineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPipelineServiceClient(IServiceCollection, Action<IServiceProvider, PipelineServiceClientBuilder>)
    
    
    public static IServiceCollection AddPipelineServiceClient(this IServiceCollection services, Action<IServiceProvider, PipelineServiceClientBuilder> action)

Adds a singleton [PipelineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PipelineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PipelineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PipelineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPredictionServiceClient(IServiceCollection, Action<PredictionServiceClientBuilder>)
    
    
    public static IServiceCollection AddPredictionServiceClient(this IServiceCollection services, Action<PredictionServiceClientBuilder> action = null)

Adds a singleton [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPredictionServiceClient(IServiceCollection, Action<IServiceProvider, PredictionServiceClientBuilder>)
    
    
    public static IServiceCollection AddPredictionServiceClient(this IServiceCollection services, Action<IServiceProvider, PredictionServiceClientBuilder> action)

Adds a singleton [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.PredictionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineExecutionServiceClient(IServiceCollection, Action<ReasoningEngineExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineExecutionServiceClient(this IServiceCollection services, Action<ReasoningEngineExecutionServiceClientBuilder> action = null)

Adds a singleton [ReasoningEngineExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReasoningEngineExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineExecutionServiceClient(IServiceCollection, Action<IServiceProvider, ReasoningEngineExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineExecutionServiceClient(this IServiceCollection services, Action<IServiceProvider, ReasoningEngineExecutionServiceClientBuilder> action)

Adds a singleton [ReasoningEngineExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReasoningEngineExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineServiceClient(IServiceCollection, Action<ReasoningEngineServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineServiceClient(this IServiceCollection services, Action<ReasoningEngineServiceClientBuilder> action = null)

Adds a singleton [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineServiceClient(IServiceCollection, Action<IServiceProvider, ReasoningEngineServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineServiceClient(this IServiceCollection services, Action<IServiceProvider, ReasoningEngineServiceClientBuilder> action)

Adds a singleton [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ReasoningEngineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddScheduleServiceClient(IServiceCollection, Action<ScheduleServiceClientBuilder>)
    
    
    public static IServiceCollection AddScheduleServiceClient(this IServiceCollection services, Action<ScheduleServiceClientBuilder> action = null)

Adds a singleton [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ScheduleServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ScheduleServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddScheduleServiceClient(IServiceCollection, Action<IServiceProvider, ScheduleServiceClientBuilder>)
    
    
    public static IServiceCollection AddScheduleServiceClient(this IServiceCollection services, Action<IServiceProvider, ScheduleServiceClientBuilder> action)

Adds a singleton [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ScheduleServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.ScheduleServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionServiceClient(IServiceCollection, Action<SessionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSessionServiceClient(this IServiceCollection services, Action<SessionServiceClientBuilder> action = null)

Adds a singleton [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SessionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SessionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SessionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionServiceClient(IServiceCollection, Action<IServiceProvider, SessionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSessionServiceClient(this IServiceCollection services, Action<IServiceProvider, SessionServiceClientBuilder> action)

Adds a singleton [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SessionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SessionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SessionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSpecialistPoolServiceClient(IServiceCollection, Action<SpecialistPoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddSpecialistPoolServiceClient(this IServiceCollection services, Action<SpecialistPoolServiceClientBuilder> action = null)

Adds a singleton [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSpecialistPoolServiceClient(IServiceCollection, Action<IServiceProvider, SpecialistPoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddSpecialistPoolServiceClient(this IServiceCollection services, Action<IServiceProvider, SpecialistPoolServiceClientBuilder> action)

Adds a singleton [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.SpecialistPoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTensorboardServiceClient(IServiceCollection, Action<TensorboardServiceClientBuilder>)
    
    
    public static IServiceCollection AddTensorboardServiceClient(this IServiceCollection services, Action<TensorboardServiceClientBuilder> action = null)

Adds a singleton [TensorboardServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.TensorboardServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TensorboardServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.TensorboardServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTensorboardServiceClient(IServiceCollection, Action<IServiceProvider, TensorboardServiceClientBuilder>)
    
    
    public static IServiceCollection AddTensorboardServiceClient(this IServiceCollection services, Action<IServiceProvider, TensorboardServiceClientBuilder> action)

Adds a singleton [TensorboardServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.TensorboardServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TensorboardServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.TensorboardServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagDataServiceClient(IServiceCollection, Action<VertexRagDataServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagDataServiceClient(this IServiceCollection services, Action<VertexRagDataServiceClientBuilder> action = null)

Adds a singleton [VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagDataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VertexRagDataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagDataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagDataServiceClient(IServiceCollection, Action<IServiceProvider, VertexRagDataServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagDataServiceClient(this IServiceCollection services, Action<IServiceProvider, VertexRagDataServiceClientBuilder> action)

Adds a singleton [VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagDataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VertexRagDataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagDataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagServiceClient(IServiceCollection, Action<VertexRagServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagServiceClient(this IServiceCollection services, Action<VertexRagServiceClientBuilder> action = null)

Adds a singleton [VertexRagServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VertexRagServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagServiceClient(IServiceCollection, Action<IServiceProvider, VertexRagServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagServiceClient(this IServiceCollection services, Action<IServiceProvider, VertexRagServiceClientBuilder> action)

Adds a singleton [VertexRagServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VertexRagServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VertexRagServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVizierServiceClient(IServiceCollection, Action<VizierServiceClientBuilder>)
    
    
    public static IServiceCollection AddVizierServiceClient(this IServiceCollection services, Action<VizierServiceClientBuilder> action = null)

Adds a singleton [VizierServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VizierServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VizierServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VizierServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVizierServiceClient(IServiceCollection, Action<IServiceProvider, VizierServiceClientBuilder>)
    
    
    public static IServiceCollection AddVizierServiceClient(this IServiceCollection services, Action<IServiceProvider, VizierServiceClientBuilder> action)

Adds a singleton [VizierServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VizierServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VizierServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1/latest/Google.Cloud.AIPlatform.V1.VizierServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
