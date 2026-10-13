---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions
title: Vertex AI v1beta1 API - Class ServiceCollectionExtensions (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:58.780666+00:00
---

# Vertex AI v1beta1 API - Class ServiceCollectionExtensions (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Microsoft.Extensions.DependencyInjection.ServiceCollectionExtensions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ServiceCollectionExtensions (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public static class ServiceCollectionExtensions

Reference documentation and code samples for the Vertex AI v1beta1 API class ServiceCollectionExtensions.

Static class to provide extension methods to configure API clients.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ServiceCollectionExtensions

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Microsoft.Extensions.DependencyInjection](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Microsoft.Extensions.DependencyInjection)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Methods 

### AddDatasetServiceClient(IServiceCollection, Action<DatasetServiceClientBuilder>)
    
    
    public static IServiceCollection AddDatasetServiceClient(this IServiceCollection services, Action<DatasetServiceClientBuilder> action = null)

Adds a singleton [DatasetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DatasetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDatasetServiceClient(IServiceCollection, Action<IServiceProvider, DatasetServiceClientBuilder>)
    
    
    public static IServiceCollection AddDatasetServiceClient(this IServiceCollection services, Action<IServiceProvider, DatasetServiceClientBuilder> action)

Adds a singleton [DatasetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DatasetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DatasetServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDeploymentResourcePoolServiceClient(IServiceCollection, Action<DeploymentResourcePoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddDeploymentResourcePoolServiceClient(this IServiceCollection services, Action<DeploymentResourcePoolServiceClientBuilder> action = null)

Adds a singleton [DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[DeploymentResourcePoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddDeploymentResourcePoolServiceClient(IServiceCollection, Action<IServiceProvider, DeploymentResourcePoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddDeploymentResourcePoolServiceClient(this IServiceCollection services, Action<IServiceProvider, DeploymentResourcePoolServiceClientBuilder> action)

Adds a singleton [DeploymentResourcePoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[DeploymentResourcePoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeploymentResourcePoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEndpointServiceClient(IServiceCollection, Action<EndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddEndpointServiceClient(this IServiceCollection services, Action<EndpointServiceClientBuilder> action = null)

Adds a singleton [EndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEndpointServiceClient(IServiceCollection, Action<IServiceProvider, EndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddEndpointServiceClient(this IServiceCollection services, Action<IServiceProvider, EndpointServiceClientBuilder> action)

Adds a singleton [EndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEvaluationServiceClient(IServiceCollection, Action<EvaluationServiceClientBuilder>)
    
    
    public static IServiceCollection AddEvaluationServiceClient(this IServiceCollection services, Action<EvaluationServiceClientBuilder> action = null)

Adds a singleton [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EvaluationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[EvaluationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EvaluationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddEvaluationServiceClient(IServiceCollection, Action<IServiceProvider, EvaluationServiceClientBuilder>)
    
    
    public static IServiceCollection AddEvaluationServiceClient(this IServiceCollection services, Action<IServiceProvider, EvaluationServiceClientBuilder> action)

Adds a singleton [EvaluationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EvaluationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[EvaluationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.EvaluationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExampleStoreServiceClient(IServiceCollection, Action<ExampleStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddExampleStoreServiceClient(this IServiceCollection services, Action<ExampleStoreServiceClientBuilder> action = null)

Adds a singleton [ExampleStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExampleStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ExampleStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExampleStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExampleStoreServiceClient(IServiceCollection, Action<IServiceProvider, ExampleStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddExampleStoreServiceClient(this IServiceCollection services, Action<IServiceProvider, ExampleStoreServiceClientBuilder> action)

Adds a singleton [ExampleStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExampleStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ExampleStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExampleStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExtensionExecutionServiceClient(IServiceCollection, Action<ExtensionExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddExtensionExecutionServiceClient(this IServiceCollection services, Action<ExtensionExecutionServiceClientBuilder> action = null)

Adds a singleton [ExtensionExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ExtensionExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExtensionExecutionServiceClient(IServiceCollection, Action<IServiceProvider, ExtensionExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddExtensionExecutionServiceClient(this IServiceCollection services, Action<IServiceProvider, ExtensionExecutionServiceClientBuilder> action)

Adds a singleton [ExtensionExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ExtensionExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExtensionRegistryServiceClient(IServiceCollection, Action<ExtensionRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddExtensionRegistryServiceClient(this IServiceCollection services, Action<ExtensionRegistryServiceClientBuilder> action = null)

Adds a singleton [ExtensionRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ExtensionRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddExtensionRegistryServiceClient(IServiceCollection, Action<IServiceProvider, ExtensionRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddExtensionRegistryServiceClient(this IServiceCollection services, Action<IServiceProvider, ExtensionRegistryServiceClientBuilder> action)

Adds a singleton [ExtensionRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ExtensionRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ExtensionRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreAdminServiceClient(IServiceCollection, Action<FeatureOnlineStoreAdminServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreAdminServiceClient(this IServiceCollection services, Action<FeatureOnlineStoreAdminServiceClientBuilder> action = null)

Adds a singleton [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreAdminServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreAdminServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreAdminServiceClient(IServiceCollection, Action<IServiceProvider, FeatureOnlineStoreAdminServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreAdminServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureOnlineStoreAdminServiceClientBuilder> action)

Adds a singleton [FeatureOnlineStoreAdminServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreAdminServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureOnlineStoreAdminServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreAdminServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreServiceClient(IServiceCollection, Action<FeatureOnlineStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreServiceClient(this IServiceCollection services, Action<FeatureOnlineStoreServiceClientBuilder> action = null)

Adds a singleton [FeatureOnlineStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureOnlineStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureOnlineStoreServiceClient(IServiceCollection, Action<IServiceProvider, FeatureOnlineStoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureOnlineStoreServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureOnlineStoreServiceClientBuilder> action)

Adds a singleton [FeatureOnlineStoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureOnlineStoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureOnlineStoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureRegistryServiceClient(IServiceCollection, Action<FeatureRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureRegistryServiceClient(this IServiceCollection services, Action<FeatureRegistryServiceClientBuilder> action = null)

Adds a singleton [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeatureRegistryServiceClient(IServiceCollection, Action<IServiceProvider, FeatureRegistryServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeatureRegistryServiceClient(this IServiceCollection services, Action<IServiceProvider, FeatureRegistryServiceClientBuilder> action)

Adds a singleton [FeatureRegistryServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeatureRegistryServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeatureRegistryServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreOnlineServingServiceClient(IServiceCollection, Action<FeaturestoreOnlineServingServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreOnlineServingServiceClient(this IServiceCollection services, Action<FeaturestoreOnlineServingServiceClientBuilder> action = null)

Adds a singleton [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreOnlineServingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeaturestoreOnlineServingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreOnlineServingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreOnlineServingServiceClient(IServiceCollection, Action<IServiceProvider, FeaturestoreOnlineServingServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreOnlineServingServiceClient(this IServiceCollection services, Action<IServiceProvider, FeaturestoreOnlineServingServiceClientBuilder> action)

Adds a singleton [FeaturestoreOnlineServingServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreOnlineServingServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeaturestoreOnlineServingServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreOnlineServingServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreServiceClient(IServiceCollection, Action<FeaturestoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreServiceClient(this IServiceCollection services, Action<FeaturestoreServiceClientBuilder> action = null)

Adds a singleton [FeaturestoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[FeaturestoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddFeaturestoreServiceClient(IServiceCollection, Action<IServiceProvider, FeaturestoreServiceClientBuilder>)
    
    
    public static IServiceCollection AddFeaturestoreServiceClient(this IServiceCollection services, Action<IServiceProvider, FeaturestoreServiceClientBuilder> action)

Adds a singleton [FeaturestoreServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[FeaturestoreServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.FeaturestoreServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiCacheServiceClient(IServiceCollection, Action<GenAiCacheServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiCacheServiceClient(this IServiceCollection services, Action<GenAiCacheServiceClientBuilder> action = null)

Adds a singleton [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiCacheServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiCacheServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiCacheServiceClient(IServiceCollection, Action<IServiceProvider, GenAiCacheServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiCacheServiceClient(this IServiceCollection services, Action<IServiceProvider, GenAiCacheServiceClientBuilder> action)

Adds a singleton [GenAiCacheServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiCacheServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GenAiCacheServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiCacheServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiTuningServiceClient(IServiceCollection, Action<GenAiTuningServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiTuningServiceClient(this IServiceCollection services, Action<GenAiTuningServiceClientBuilder> action = null)

Adds a singleton [GenAiTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiTuningServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[GenAiTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiTuningServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddGenAiTuningServiceClient(IServiceCollection, Action<IServiceProvider, GenAiTuningServiceClientBuilder>)
    
    
    public static IServiceCollection AddGenAiTuningServiceClient(this IServiceCollection services, Action<IServiceProvider, GenAiTuningServiceClientBuilder> action)

Adds a singleton [GenAiTuningServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiTuningServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[GenAiTuningServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GenAiTuningServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexEndpointServiceClient(IServiceCollection, Action<IndexEndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexEndpointServiceClient(this IServiceCollection services, Action<IndexEndpointServiceClientBuilder> action = null)

Adds a singleton [IndexEndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexEndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IndexEndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexEndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexEndpointServiceClient(IServiceCollection, Action<IServiceProvider, IndexEndpointServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexEndpointServiceClient(this IServiceCollection services, Action<IServiceProvider, IndexEndpointServiceClientBuilder> action)

Adds a singleton [IndexEndpointServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexEndpointServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[IndexEndpointServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexEndpointServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexServiceClient(IServiceCollection, Action<IndexServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexServiceClient(this IServiceCollection services, Action<IndexServiceClientBuilder> action = null)

Adds a singleton [IndexServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[IndexServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddIndexServiceClient(IServiceCollection, Action<IServiceProvider, IndexServiceClientBuilder>)
    
    
    public static IServiceCollection AddIndexServiceClient(this IServiceCollection services, Action<IServiceProvider, IndexServiceClientBuilder> action)

Adds a singleton [IndexServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[IndexServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.IndexServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddJobServiceClient(IServiceCollection, Action<JobServiceClientBuilder>)
    
    
    public static IServiceCollection AddJobServiceClient(this IServiceCollection services, Action<JobServiceClientBuilder> action = null)

Adds a singleton [JobServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.JobServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[JobServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.JobServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddJobServiceClient(IServiceCollection, Action<IServiceProvider, JobServiceClientBuilder>)
    
    
    public static IServiceCollection AddJobServiceClient(this IServiceCollection services, Action<IServiceProvider, JobServiceClientBuilder> action)

Adds a singleton [JobServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.JobServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[JobServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.JobServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLlmUtilityServiceClient(IServiceCollection, Action<LlmUtilityServiceClientBuilder>)
    
    
    public static IServiceCollection AddLlmUtilityServiceClient(this IServiceCollection services, Action<LlmUtilityServiceClientBuilder> action = null)

Adds a singleton [LlmUtilityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.LlmUtilityServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[LlmUtilityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.LlmUtilityServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddLlmUtilityServiceClient(IServiceCollection, Action<IServiceProvider, LlmUtilityServiceClientBuilder>)
    
    
    public static IServiceCollection AddLlmUtilityServiceClient(this IServiceCollection services, Action<IServiceProvider, LlmUtilityServiceClientBuilder> action)

Adds a singleton [LlmUtilityServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.LlmUtilityServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[LlmUtilityServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.LlmUtilityServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMatchServiceClient(IServiceCollection, Action<MatchServiceClientBuilder>)
    
    
    public static IServiceCollection AddMatchServiceClient(this IServiceCollection services, Action<MatchServiceClientBuilder> action = null)

Adds a singleton [MatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MatchServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MatchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MatchServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMatchServiceClient(IServiceCollection, Action<IServiceProvider, MatchServiceClientBuilder>)
    
    
    public static IServiceCollection AddMatchServiceClient(this IServiceCollection services, Action<IServiceProvider, MatchServiceClientBuilder> action)

Adds a singleton [MatchServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MatchServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MatchServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MatchServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMemoryBankServiceClient(IServiceCollection, Action<MemoryBankServiceClientBuilder>)
    
    
    public static IServiceCollection AddMemoryBankServiceClient(this IServiceCollection services, Action<MemoryBankServiceClientBuilder> action = null)

Adds a singleton [MemoryBankServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryBankServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MemoryBankServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryBankServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMemoryBankServiceClient(IServiceCollection, Action<IServiceProvider, MemoryBankServiceClientBuilder>)
    
    
    public static IServiceCollection AddMemoryBankServiceClient(this IServiceCollection services, Action<IServiceProvider, MemoryBankServiceClientBuilder> action)

Adds a singleton [MemoryBankServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryBankServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MemoryBankServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MemoryBankServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMetadataServiceClient(IServiceCollection, Action<MetadataServiceClientBuilder>)
    
    
    public static IServiceCollection AddMetadataServiceClient(this IServiceCollection services, Action<MetadataServiceClientBuilder> action = null)

Adds a singleton [MetadataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MetadataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MetadataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MetadataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMetadataServiceClient(IServiceCollection, Action<IServiceProvider, MetadataServiceClientBuilder>)
    
    
    public static IServiceCollection AddMetadataServiceClient(this IServiceCollection services, Action<IServiceProvider, MetadataServiceClientBuilder> action)

Adds a singleton [MetadataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MetadataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MetadataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MetadataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMigrationServiceClient(IServiceCollection, Action<MigrationServiceClientBuilder>)
    
    
    public static IServiceCollection AddMigrationServiceClient(this IServiceCollection services, Action<MigrationServiceClientBuilder> action = null)

Adds a singleton [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddMigrationServiceClient(IServiceCollection, Action<IServiceProvider, MigrationServiceClientBuilder>)
    
    
    public static IServiceCollection AddMigrationServiceClient(this IServiceCollection services, Action<IServiceProvider, MigrationServiceClientBuilder> action)

Adds a singleton [MigrationServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[MigrationServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.MigrationServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelGardenServiceClient(IServiceCollection, Action<ModelGardenServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelGardenServiceClient(this IServiceCollection services, Action<ModelGardenServiceClientBuilder> action = null)

Adds a singleton [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelGardenServiceClient(IServiceCollection, Action<IServiceProvider, ModelGardenServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelGardenServiceClient(this IServiceCollection services, Action<IServiceProvider, ModelGardenServiceClientBuilder> action)

Adds a singleton [ModelGardenServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ModelGardenServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelGardenServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelMonitoringServiceClient(IServiceCollection, Action<ModelMonitoringServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelMonitoringServiceClient(this IServiceCollection services, Action<ModelMonitoringServiceClientBuilder> action = null)

Adds a singleton [ModelMonitoringServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ModelMonitoringServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelMonitoringServiceClient(IServiceCollection, Action<IServiceProvider, ModelMonitoringServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelMonitoringServiceClient(this IServiceCollection services, Action<IServiceProvider, ModelMonitoringServiceClientBuilder> action)

Adds a singleton [ModelMonitoringServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ModelMonitoringServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelMonitoringServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelServiceClient(IServiceCollection, Action<ModelServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelServiceClient(this IServiceCollection services, Action<ModelServiceClientBuilder> action = null)

Adds a singleton [ModelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ModelServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddModelServiceClient(IServiceCollection, Action<IServiceProvider, ModelServiceClientBuilder>)
    
    
    public static IServiceCollection AddModelServiceClient(this IServiceCollection services, Action<IServiceProvider, ModelServiceClientBuilder> action)

Adds a singleton [ModelServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ModelServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ModelServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNotebookServiceClient(IServiceCollection, Action<NotebookServiceClientBuilder>)
    
    
    public static IServiceCollection AddNotebookServiceClient(this IServiceCollection services, Action<NotebookServiceClientBuilder> action = null)

Adds a singleton [NotebookServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[NotebookServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddNotebookServiceClient(IServiceCollection, Action<IServiceProvider, NotebookServiceClientBuilder>)
    
    
    public static IServiceCollection AddNotebookServiceClient(this IServiceCollection services, Action<IServiceProvider, NotebookServiceClientBuilder> action)

Adds a singleton [NotebookServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[NotebookServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.NotebookServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddOnlineEvaluatorServiceClient(IServiceCollection, Action<OnlineEvaluatorServiceClientBuilder>)
    
    
    public static IServiceCollection AddOnlineEvaluatorServiceClient(this IServiceCollection services, Action<OnlineEvaluatorServiceClientBuilder> action = null)

Adds a singleton [OnlineEvaluatorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[OnlineEvaluatorServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddOnlineEvaluatorServiceClient(IServiceCollection, Action<IServiceProvider, OnlineEvaluatorServiceClientBuilder>)
    
    
    public static IServiceCollection AddOnlineEvaluatorServiceClient(this IServiceCollection services, Action<IServiceProvider, OnlineEvaluatorServiceClientBuilder> action)

Adds a singleton [OnlineEvaluatorServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[OnlineEvaluatorServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.OnlineEvaluatorServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPersistentResourceServiceClient(IServiceCollection, Action<PersistentResourceServiceClientBuilder>)
    
    
    public static IServiceCollection AddPersistentResourceServiceClient(this IServiceCollection services, Action<PersistentResourceServiceClientBuilder> action = null)

Adds a singleton [PersistentResourceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PersistentResourceServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPersistentResourceServiceClient(IServiceCollection, Action<IServiceProvider, PersistentResourceServiceClientBuilder>)
    
    
    public static IServiceCollection AddPersistentResourceServiceClient(this IServiceCollection services, Action<IServiceProvider, PersistentResourceServiceClientBuilder> action)

Adds a singleton [PersistentResourceServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PersistentResourceServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PersistentResourceServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPipelineServiceClient(IServiceCollection, Action<PipelineServiceClientBuilder>)
    
    
    public static IServiceCollection AddPipelineServiceClient(this IServiceCollection services, Action<PipelineServiceClientBuilder> action = null)

Adds a singleton [PipelineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PipelineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PipelineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PipelineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPipelineServiceClient(IServiceCollection, Action<IServiceProvider, PipelineServiceClientBuilder>)
    
    
    public static IServiceCollection AddPipelineServiceClient(this IServiceCollection services, Action<IServiceProvider, PipelineServiceClientBuilder> action)

Adds a singleton [PipelineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PipelineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PipelineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PipelineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPredictionServiceClient(IServiceCollection, Action<PredictionServiceClientBuilder>)
    
    
    public static IServiceCollection AddPredictionServiceClient(this IServiceCollection services, Action<PredictionServiceClientBuilder> action = null)

Adds a singleton [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PredictionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PredictionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddPredictionServiceClient(IServiceCollection, Action<IServiceProvider, PredictionServiceClientBuilder>)
    
    
    public static IServiceCollection AddPredictionServiceClient(this IServiceCollection services, Action<IServiceProvider, PredictionServiceClientBuilder> action)

Adds a singleton [PredictionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PredictionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[PredictionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PredictionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineExecutionServiceClient(IServiceCollection, Action<ReasoningEngineExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineExecutionServiceClient(this IServiceCollection services, Action<ReasoningEngineExecutionServiceClientBuilder> action = null)

Adds a singleton [ReasoningEngineExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReasoningEngineExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineExecutionServiceClient(IServiceCollection, Action<IServiceProvider, ReasoningEngineExecutionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineExecutionServiceClient(this IServiceCollection services, Action<IServiceProvider, ReasoningEngineExecutionServiceClientBuilder> action)

Adds a singleton [ReasoningEngineExecutionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineExecutionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReasoningEngineExecutionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineExecutionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineRuntimeRevisionServiceClient(IServiceCollection, Action<ReasoningEngineRuntimeRevisionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineRuntimeRevisionServiceClient(this IServiceCollection services, Action<ReasoningEngineRuntimeRevisionServiceClientBuilder> action = null)

Adds a singleton [ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReasoningEngineRuntimeRevisionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineRuntimeRevisionServiceClient(IServiceCollection, Action<IServiceProvider, ReasoningEngineRuntimeRevisionServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineRuntimeRevisionServiceClient(this IServiceCollection services, Action<IServiceProvider, ReasoningEngineRuntimeRevisionServiceClientBuilder> action)

Adds a singleton [ReasoningEngineRuntimeRevisionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReasoningEngineRuntimeRevisionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineRuntimeRevisionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineServiceClient(IServiceCollection, Action<ReasoningEngineServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineServiceClient(this IServiceCollection services, Action<ReasoningEngineServiceClientBuilder> action = null)

Adds a singleton [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddReasoningEngineServiceClient(IServiceCollection, Action<IServiceProvider, ReasoningEngineServiceClientBuilder>)
    
    
    public static IServiceCollection AddReasoningEngineServiceClient(this IServiceCollection services, Action<IServiceProvider, ReasoningEngineServiceClientBuilder> action)

Adds a singleton [ReasoningEngineServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ReasoningEngineServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ReasoningEngineServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddScheduleServiceClient(IServiceCollection, Action<ScheduleServiceClientBuilder>)
    
    
    public static IServiceCollection AddScheduleServiceClient(this IServiceCollection services, Action<ScheduleServiceClientBuilder> action = null)

Adds a singleton [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddScheduleServiceClient(IServiceCollection, Action<IServiceProvider, ScheduleServiceClientBuilder>)
    
    
    public static IServiceCollection AddScheduleServiceClient(this IServiceCollection services, Action<IServiceProvider, ScheduleServiceClientBuilder> action)

Adds a singleton [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionServiceClient(IServiceCollection, Action<SessionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSessionServiceClient(this IServiceCollection services, Action<SessionServiceClientBuilder> action = null)

Adds a singleton [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SessionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSessionServiceClient(IServiceCollection, Action<IServiceProvider, SessionServiceClientBuilder>)
    
    
    public static IServiceCollection AddSessionServiceClient(this IServiceCollection services, Action<IServiceProvider, SessionServiceClientBuilder> action)

Adds a singleton [SessionServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SessionServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SessionServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSpecialistPoolServiceClient(IServiceCollection, Action<SpecialistPoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddSpecialistPoolServiceClient(this IServiceCollection services, Action<SpecialistPoolServiceClientBuilder> action = null)

Adds a singleton [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SpecialistPoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SpecialistPoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddSpecialistPoolServiceClient(IServiceCollection, Action<IServiceProvider, SpecialistPoolServiceClientBuilder>)
    
    
    public static IServiceCollection AddSpecialistPoolServiceClient(this IServiceCollection services, Action<IServiceProvider, SpecialistPoolServiceClientBuilder> action)

Adds a singleton [SpecialistPoolServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SpecialistPoolServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[SpecialistPoolServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.SpecialistPoolServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTensorboardServiceClient(IServiceCollection, Action<TensorboardServiceClientBuilder>)
    
    
    public static IServiceCollection AddTensorboardServiceClient(this IServiceCollection services, Action<TensorboardServiceClientBuilder> action = null)

Adds a singleton [TensorboardServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TensorboardServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[TensorboardServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TensorboardServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddTensorboardServiceClient(IServiceCollection, Action<IServiceProvider, TensorboardServiceClientBuilder>)
    
    
    public static IServiceCollection AddTensorboardServiceClient(this IServiceCollection services, Action<IServiceProvider, TensorboardServiceClientBuilder> action)

Adds a singleton [TensorboardServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TensorboardServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[TensorboardServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.TensorboardServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagDataServiceClient(IServiceCollection, Action<VertexRagDataServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagDataServiceClient(this IServiceCollection services, Action<VertexRagDataServiceClientBuilder> action = null)

Adds a singleton [VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VertexRagDataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagDataServiceClient(IServiceCollection, Action<IServiceProvider, VertexRagDataServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagDataServiceClient(this IServiceCollection services, Action<IServiceProvider, VertexRagDataServiceClientBuilder> action)

Adds a singleton [VertexRagDataServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VertexRagDataServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagDataServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagServiceClient(IServiceCollection, Action<VertexRagServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagServiceClient(this IServiceCollection services, Action<VertexRagServiceClientBuilder> action = null)

Adds a singleton [VertexRagServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VertexRagServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVertexRagServiceClient(IServiceCollection, Action<IServiceProvider, VertexRagServiceClientBuilder>)
    
    
    public static IServiceCollection AddVertexRagServiceClient(this IServiceCollection services, Action<IServiceProvider, VertexRagServiceClientBuilder> action)

Adds a singleton [VertexRagServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VertexRagServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VertexRagServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVizierServiceClient(IServiceCollection, Action<VizierServiceClientBuilder>)
    
    
    public static IServiceCollection AddVizierServiceClient(this IServiceCollection services, Action<VizierServiceClientBuilder> action = null)

Adds a singleton [VizierServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VizierServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-1)[VizierServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VizierServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
### AddVizierServiceClient(IServiceCollection, Action<IServiceProvider, VizierServiceClientBuilder>)
    
    
    public static IServiceCollection AddVizierServiceClient(this IServiceCollection services, Action<IServiceProvider, VizierServiceClientBuilder> action)

Adds a singleton [VizierServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VizierServiceClient) to `services`.

**Parameters**  
---  
**Name** | **Description**  
`services` | `[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)`  
The service collection to add the client to. The services are used to configure the client when requested.  
`action` | `[Action](https://learn.microsoft.com/dotnet/api/system.action-2)System.IServiceProvider[VizierServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.VizierServiceClientBuilder)`  
An optional action to invoke on the client builder. This is invoked before services from `services` are used.  
**Returns**  
---  
**Type** | **Description**  
`[IServiceCollection](https://learn.microsoft.com/dotnet/api/microsoft.extensions.dependencyinjection.iservicecollection)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
