---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform/
title: Vertex AI API - Module Google::Cloud::AIPlatform (v2.4.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:17:48.560935+00:00
---

# Vertex AI API - Module Google::Cloud::AIPlatform (v2.4.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI API - Module Google::Cloud::AIPlatform (v2.4.2) Stay organized with collections  Save and categorize content based on your preferences. 

2.4.2 (latest)  2.4.1  2.3.0  2.2.0  2.1.1  2.0.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI API module Google::Cloud::AIPlatform.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-ai_platform library.

The following configuration parameters are supported:

  * `credentials` (_type:_ `String, Hash, Google::Auth::Credentials`) - The path to the keyfile as a String, the contents of the keyfile as a Hash, or a Google::Auth::Credentials object.
  * `lib_name` (_type:_ `String`) - The library name as recorded in instrumentation and logging.
  * `lib_version` (_type:_ `String`) - The library version as recorded in instrumentation and logging.
  * `interceptors` (_type:_ `Array<GRPC::ClientInterceptor>`) - An array of interceptors that are run before calls are executed.
  * `timeout` (_type:_ `Numeric`) - Default timeout in seconds.
  * `metadata` (_type:_ `Hash{Symbol=>String}`) - Additional headers to be sent with the call.
  * `retry_policy` (_type:_ `Hash`) - The retry policy. The value is a hash with the following keys: 
    * `:initial_delay` (_type:_ `Numeric`) - The initial delay in seconds.
    * `:max_delay` (_type:_ `Numeric`) - The max delay in seconds.
    * `:multiplier` (_type:_ `Numeric`) - The incremental backoff multiplier.
    * `:jitter` (_type:_ `Numeric`) - The jitter in seconds. Default: 1.0.
    * `:retry_codes` (_type:_ `Array<String>`) - The error codes that should trigger a retry.



**Yields**

  * (::Google::Cloud.configure.ai_platform) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .data_foundry_service
    
    
    def self.data_foundry_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for DataFoundryService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::DataFoundryService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DataFoundryService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the DataFoundryService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the DataFoundryService service. You can determine whether the method will succeed by calling [AIPlatform.data_foundry_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_data_foundry_service_available__class_ "Google::Cloud::AIPlatform.data_foundry_service_available? \(method\)").

#### About DataFoundryService

Service for generating and preparing datasets for Gen AI evaluation.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .data_foundry_service_available?
    
    
    def self.data_foundry_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the DataFoundryService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.data_foundry_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_data_foundry_service_class_ "Google::Cloud::AIPlatform.data_foundry_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the DataFoundryService service, or if the versioned client gem needs an update to support the DataFoundryService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .dataset_service
    
    
    def self.dataset_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for DatasetService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::DatasetService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DatasetService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the DatasetService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the DatasetService service. You can determine whether the method will succeed by calling [AIPlatform.dataset_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_dataset_service_available__class_ "Google::Cloud::AIPlatform.dataset_service_available? \(method\)").

#### About DatasetService

The service that manages Vertex AI Dataset and its child resources.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .dataset_service_available?
    
    
    def self.dataset_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the DatasetService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.dataset_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_dataset_service_class_ "Google::Cloud::AIPlatform.dataset_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the DatasetService service, or if the versioned client gem needs an update to support the DatasetService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .deployment_resource_pool_service
    
    
    def self.deployment_resource_pool_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for DeploymentResourcePoolService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::DeploymentResourcePoolService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeploymentResourcePoolService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the DeploymentResourcePoolService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the DeploymentResourcePoolService service. You can determine whether the method will succeed by calling [AIPlatform.deployment_resource_pool_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_deployment_resource_pool_service_available__class_ "Google::Cloud::AIPlatform.deployment_resource_pool_service_available? \(method\)").

#### About DeploymentResourcePoolService

A service that manages the DeploymentResourcePool resource.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .deployment_resource_pool_service_available?
    
    
    def self.deployment_resource_pool_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the DeploymentResourcePoolService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.deployment_resource_pool_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_deployment_resource_pool_service_class_ "Google::Cloud::AIPlatform.deployment_resource_pool_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the DeploymentResourcePoolService service, or if the versioned client gem needs an update to support the DeploymentResourcePoolService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .endpoint_service
    
    
    def self.endpoint_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for EndpointService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::EndpointService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EndpointService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the EndpointService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the EndpointService service. You can determine whether the method will succeed by calling [AIPlatform.endpoint_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_endpoint_service_available__class_ "Google::Cloud::AIPlatform.endpoint_service_available? \(method\)").

#### About EndpointService

A service for managing Vertex AI's Endpoints.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .endpoint_service_available?
    
    
    def self.endpoint_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the EndpointService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.endpoint_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_endpoint_service_class_ "Google::Cloud::AIPlatform.endpoint_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the EndpointService service, or if the versioned client gem needs an update to support the EndpointService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .evaluation_service
    
    
    def self.evaluation_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for EvaluationService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::EvaluationService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-EvaluationService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the EvaluationService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the EvaluationService service. You can determine whether the method will succeed by calling [AIPlatform.evaluation_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_evaluation_service_available__class_ "Google::Cloud::AIPlatform.evaluation_service_available? \(method\)").

#### About EvaluationService

Vertex AI Online Evaluation Service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .evaluation_service_available?
    
    
    def self.evaluation_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the EvaluationService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.evaluation_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_evaluation_service_class_ "Google::Cloud::AIPlatform.evaluation_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the EvaluationService service, or if the versioned client gem needs an update to support the EvaluationService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .feature_online_store_admin_service
    
    
    def self.feature_online_store_admin_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for FeatureOnlineStoreAdminService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FeatureOnlineStoreAdminService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the FeatureOnlineStoreAdminService service. You can determine whether the method will succeed by calling [AIPlatform.feature_online_store_admin_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_online_store_admin_service_available__class_ "Google::Cloud::AIPlatform.feature_online_store_admin_service_available? \(method\)").

#### About FeatureOnlineStoreAdminService

The service that handles CRUD and List for resources for FeatureOnlineStore.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .feature_online_store_admin_service_available?
    
    
    def self.feature_online_store_admin_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the FeatureOnlineStoreAdminService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.feature_online_store_admin_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_online_store_admin_service_class_ "Google::Cloud::AIPlatform.feature_online_store_admin_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FeatureOnlineStoreAdminService service, or if the versioned client gem needs an update to support the FeatureOnlineStoreAdminService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .feature_online_store_service
    
    
    def self.feature_online_store_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for FeatureOnlineStoreService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::FeatureOnlineStoreService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FeatureOnlineStoreService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the FeatureOnlineStoreService service. You can determine whether the method will succeed by calling [AIPlatform.feature_online_store_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_online_store_service_available__class_ "Google::Cloud::AIPlatform.feature_online_store_service_available? \(method\)").

#### About FeatureOnlineStoreService

A service for fetching feature values from the online store.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .feature_online_store_service_available?
    
    
    def self.feature_online_store_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the FeatureOnlineStoreService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.feature_online_store_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_online_store_service_class_ "Google::Cloud::AIPlatform.feature_online_store_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FeatureOnlineStoreService service, or if the versioned client gem needs an update to support the FeatureOnlineStoreService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .feature_registry_service
    
    
    def self.feature_registry_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for FeatureRegistryService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::FeatureRegistryService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureRegistryService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FeatureRegistryService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the FeatureRegistryService service. You can determine whether the method will succeed by calling [AIPlatform.feature_registry_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_registry_service_available__class_ "Google::Cloud::AIPlatform.feature_registry_service_available? \(method\)").

#### About FeatureRegistryService

The service that handles CRUD and List for resources for FeatureRegistry.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .feature_registry_service_available?
    
    
    def self.feature_registry_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the FeatureRegistryService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.feature_registry_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_feature_registry_service_class_ "Google::Cloud::AIPlatform.feature_registry_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FeatureRegistryService service, or if the versioned client gem needs an update to support the FeatureRegistryService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .featurestore_online_serving_service
    
    
    def self.featurestore_online_serving_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for FeaturestoreOnlineServingService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::FeaturestoreOnlineServingService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreOnlineServingService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FeaturestoreOnlineServingService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the FeaturestoreOnlineServingService service. You can determine whether the method will succeed by calling [AIPlatform.featurestore_online_serving_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_featurestore_online_serving_service_available__class_ "Google::Cloud::AIPlatform.featurestore_online_serving_service_available? \(method\)").

#### About FeaturestoreOnlineServingService

A service for serving online feature values.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .featurestore_online_serving_service_available?
    
    
    def self.featurestore_online_serving_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the FeaturestoreOnlineServingService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.featurestore_online_serving_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_featurestore_online_serving_service_class_ "Google::Cloud::AIPlatform.featurestore_online_serving_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FeaturestoreOnlineServingService service, or if the versioned client gem needs an update to support the FeaturestoreOnlineServingService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .featurestore_service
    
    
    def self.featurestore_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for FeaturestoreService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::FeaturestoreService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeaturestoreService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the FeaturestoreService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the FeaturestoreService service. You can determine whether the method will succeed by calling [AIPlatform.featurestore_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_featurestore_service_available__class_ "Google::Cloud::AIPlatform.featurestore_service_available? \(method\)").

#### About FeaturestoreService

The service that handles CRUD and List for resources for Featurestore.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .featurestore_service_available?
    
    
    def self.featurestore_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the FeaturestoreService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.featurestore_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_featurestore_service_class_ "Google::Cloud::AIPlatform.featurestore_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the FeaturestoreService service, or if the versioned client gem needs an update to support the FeaturestoreService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .gen_ai_cache_service
    
    
    def self.gen_ai_cache_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for GenAiCacheService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::GenAiCacheService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiCacheService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GenAiCacheService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the GenAiCacheService service. You can determine whether the method will succeed by calling [AIPlatform.gen_ai_cache_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_gen_ai_cache_service_available__class_ "Google::Cloud::AIPlatform.gen_ai_cache_service_available? \(method\)").

#### About GenAiCacheService

Service for managing Vertex AI's CachedContent resource.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .gen_ai_cache_service_available?
    
    
    def self.gen_ai_cache_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the GenAiCacheService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.gen_ai_cache_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_gen_ai_cache_service_class_ "Google::Cloud::AIPlatform.gen_ai_cache_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GenAiCacheService service, or if the versioned client gem needs an update to support the GenAiCacheService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .gen_ai_tuning_service
    
    
    def self.gen_ai_tuning_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for GenAiTuningService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::GenAiTuningService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the GenAiTuningService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the GenAiTuningService service. You can determine whether the method will succeed by calling [AIPlatform.gen_ai_tuning_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_gen_ai_tuning_service_available__class_ "Google::Cloud::AIPlatform.gen_ai_tuning_service_available? \(method\)").

#### About GenAiTuningService

A service for creating and managing GenAI Tuning Jobs.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .gen_ai_tuning_service_available?
    
    
    def self.gen_ai_tuning_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the GenAiTuningService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.gen_ai_tuning_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_gen_ai_tuning_service_class_ "Google::Cloud::AIPlatform.gen_ai_tuning_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the GenAiTuningService service, or if the versioned client gem needs an update to support the GenAiTuningService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .index_endpoint_service
    
    
    def self.index_endpoint_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for IndexEndpointService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::IndexEndpointService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexEndpointService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the IndexEndpointService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the IndexEndpointService service. You can determine whether the method will succeed by calling [AIPlatform.index_endpoint_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_index_endpoint_service_available__class_ "Google::Cloud::AIPlatform.index_endpoint_service_available? \(method\)").

#### About IndexEndpointService

A service for managing Vertex AI's IndexEndpoints.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .index_endpoint_service_available?
    
    
    def self.index_endpoint_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the IndexEndpointService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.index_endpoint_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_index_endpoint_service_class_ "Google::Cloud::AIPlatform.index_endpoint_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the IndexEndpointService service, or if the versioned client gem needs an update to support the IndexEndpointService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .index_service
    
    
    def self.index_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for IndexService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::IndexService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-IndexService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the IndexService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the IndexService service. You can determine whether the method will succeed by calling [AIPlatform.index_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_index_service_available__class_ "Google::Cloud::AIPlatform.index_service_available? \(method\)").

#### About IndexService

A service for creating and managing Vertex AI's Index resources.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .index_service_available?
    
    
    def self.index_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the IndexService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.index_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_index_service_class_ "Google::Cloud::AIPlatform.index_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the IndexService service, or if the versioned client gem needs an update to support the IndexService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .job_service
    
    
    def self.job_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for JobService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::JobService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-JobService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the JobService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the JobService service. You can determine whether the method will succeed by calling [AIPlatform.job_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_job_service_available__class_ "Google::Cloud::AIPlatform.job_service_available? \(method\)").

#### About JobService

A service for creating and managing Vertex AI's jobs.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .job_service_available?
    
    
    def self.job_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the JobService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.job_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_job_service_class_ "Google::Cloud::AIPlatform.job_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the JobService service, or if the versioned client gem needs an update to support the JobService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .llm_utility_service
    
    
    def self.llm_utility_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for LlmUtilityService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::LlmUtilityService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-LlmUtilityService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the LlmUtilityService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the LlmUtilityService service. You can determine whether the method will succeed by calling [AIPlatform.llm_utility_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_llm_utility_service_available__class_ "Google::Cloud::AIPlatform.llm_utility_service_available? \(method\)").

#### About LlmUtilityService

Service for LLM related utility functions.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .llm_utility_service_available?
    
    
    def self.llm_utility_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the LlmUtilityService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.llm_utility_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_llm_utility_service_class_ "Google::Cloud::AIPlatform.llm_utility_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the LlmUtilityService service, or if the versioned client gem needs an update to support the LlmUtilityService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .match_service
    
    
    def self.match_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for MatchService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::MatchService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MatchService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the MatchService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the MatchService service. You can determine whether the method will succeed by calling [AIPlatform.match_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_match_service_available__class_ "Google::Cloud::AIPlatform.match_service_available? \(method\)").

#### About MatchService

MatchService is a Google managed service for efficient vector similarity search at scale.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .match_service_available?
    
    
    def self.match_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the MatchService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.match_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_match_service_class_ "Google::Cloud::AIPlatform.match_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the MatchService service, or if the versioned client gem needs an update to support the MatchService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .metadata_service
    
    
    def self.metadata_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for MetadataService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::MetadataService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MetadataService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the MetadataService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the MetadataService service. You can determine whether the method will succeed by calling [AIPlatform.metadata_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_metadata_service_available__class_ "Google::Cloud::AIPlatform.metadata_service_available? \(method\)").

#### About MetadataService

Service for reading and writing metadata entries.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .metadata_service_available?
    
    
    def self.metadata_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the MetadataService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.metadata_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_metadata_service_class_ "Google::Cloud::AIPlatform.metadata_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the MetadataService service, or if the versioned client gem needs an update to support the MetadataService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .migration_service
    
    
    def self.migration_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for MigrationService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::MigrationService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-MigrationService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the MigrationService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the MigrationService service. You can determine whether the method will succeed by calling [AIPlatform.migration_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_migration_service_available__class_ "Google::Cloud::AIPlatform.migration_service_available? \(method\)").

#### About MigrationService

A service that migrates resources from automl.googleapis.com, datalabeling.googleapis.com and ml.googleapis.com to Vertex AI.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .migration_service_available?
    
    
    def self.migration_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the MigrationService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.migration_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_migration_service_class_ "Google::Cloud::AIPlatform.migration_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the MigrationService service, or if the versioned client gem needs an update to support the MigrationService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .model_garden_service
    
    
    def self.model_garden_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ModelGardenService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::ModelGardenService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ModelGardenService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ModelGardenService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ModelGardenService service. You can determine whether the method will succeed by calling [AIPlatform.model_garden_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_model_garden_service_available__class_ "Google::Cloud::AIPlatform.model_garden_service_available? \(method\)").

#### About ModelGardenService

The interface of Model Garden Service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .model_garden_service_available?
    
    
    def self.model_garden_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ModelGardenService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.model_garden_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_model_garden_service_class_ "Google::Cloud::AIPlatform.model_garden_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ModelGardenService service, or if the versioned client gem needs an update to support the ModelGardenService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .model_service
    
    
    def self.model_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ModelService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::ModelService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ModelService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ModelService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ModelService service. You can determine whether the method will succeed by calling [AIPlatform.model_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_model_service_available__class_ "Google::Cloud::AIPlatform.model_service_available? \(method\)").

#### About ModelService

A service for managing Vertex AI's machine learning Models.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .model_service_available?
    
    
    def self.model_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ModelService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.model_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_model_service_class_ "Google::Cloud::AIPlatform.model_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ModelService service, or if the versioned client gem needs an update to support the ModelService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .notebook_service
    
    
    def self.notebook_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for NotebookService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::NotebookService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-NotebookService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the NotebookService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the NotebookService service. You can determine whether the method will succeed by calling [AIPlatform.notebook_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_notebook_service_available__class_ "Google::Cloud::AIPlatform.notebook_service_available? \(method\)").

#### About NotebookService

The interface for Vertex Notebook service (a.k.a. Colab on Workbench).

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .notebook_service_available?
    
    
    def self.notebook_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the NotebookService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.notebook_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_notebook_service_class_ "Google::Cloud::AIPlatform.notebook_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the NotebookService service, or if the versioned client gem needs an update to support the NotebookService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .persistent_resource_service
    
    
    def self.persistent_resource_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for PersistentResourceService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::PersistentResourceService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PersistentResourceService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the PersistentResourceService service. You can determine whether the method will succeed by calling [AIPlatform.persistent_resource_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_persistent_resource_service_available__class_ "Google::Cloud::AIPlatform.persistent_resource_service_available? \(method\)").

#### About PersistentResourceService

A service for managing Vertex AI's machine learning PersistentResource.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .persistent_resource_service_available?
    
    
    def self.persistent_resource_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the PersistentResourceService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.persistent_resource_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_persistent_resource_service_class_ "Google::Cloud::AIPlatform.persistent_resource_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PersistentResourceService service, or if the versioned client gem needs an update to support the PersistentResourceService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .pipeline_service
    
    
    def self.pipeline_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for PipelineService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::PipelineService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PipelineService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PipelineService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the PipelineService service. You can determine whether the method will succeed by calling [AIPlatform.pipeline_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_pipeline_service_available__class_ "Google::Cloud::AIPlatform.pipeline_service_available? \(method\)").

#### About PipelineService

A service for creating and managing Vertex AI's pipelines. This includes both `TrainingPipeline` resources (used for AutoML and custom training) and `PipelineJob` resources (used for Vertex AI Pipelines).

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .pipeline_service_available?
    
    
    def self.pipeline_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the PipelineService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.pipeline_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_pipeline_service_class_ "Google::Cloud::AIPlatform.pipeline_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PipelineService service, or if the versioned client gem needs an update to support the PipelineService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .prediction_service
    
    
    def self.prediction_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for PredictionService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::PredictionService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PredictionService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the PredictionService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the PredictionService service. You can determine whether the method will succeed by calling [AIPlatform.prediction_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_prediction_service_available__class_ "Google::Cloud::AIPlatform.prediction_service_available? \(method\)").

#### About PredictionService

A service for online predictions and explanations.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .prediction_service_available?
    
    
    def self.prediction_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the PredictionService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.prediction_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_prediction_service_class_ "Google::Cloud::AIPlatform.prediction_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the PredictionService service, or if the versioned client gem needs an update to support the PredictionService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reasoning_engine_execution_service
    
    
    def self.reasoning_engine_execution_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ReasoningEngineExecutionService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::ReasoningEngineExecutionService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ReasoningEngineExecutionService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReasoningEngineExecutionService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ReasoningEngineExecutionService service. You can determine whether the method will succeed by calling [AIPlatform.reasoning_engine_execution_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_reasoning_engine_execution_service_available__class_ "Google::Cloud::AIPlatform.reasoning_engine_execution_service_available? \(method\)").

#### About ReasoningEngineExecutionService

A service for executing queries on Reasoning Engine.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reasoning_engine_execution_service_available?
    
    
    def self.reasoning_engine_execution_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ReasoningEngineExecutionService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.reasoning_engine_execution_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_reasoning_engine_execution_service_class_ "Google::Cloud::AIPlatform.reasoning_engine_execution_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReasoningEngineExecutionService service, or if the versioned client gem needs an update to support the ReasoningEngineExecutionService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .reasoning_engine_service
    
    
    def self.reasoning_engine_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ReasoningEngineService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::ReasoningEngineService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ReasoningEngineService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ReasoningEngineService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ReasoningEngineService service. You can determine whether the method will succeed by calling [AIPlatform.reasoning_engine_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_reasoning_engine_service_available__class_ "Google::Cloud::AIPlatform.reasoning_engine_service_available? \(method\)").

#### About ReasoningEngineService

A service for managing Vertex AI's Reasoning Engines.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .reasoning_engine_service_available?
    
    
    def self.reasoning_engine_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ReasoningEngineService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.reasoning_engine_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_reasoning_engine_service_class_ "Google::Cloud::AIPlatform.reasoning_engine_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ReasoningEngineService service, or if the versioned client gem needs an update to support the ReasoningEngineService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .schedule_service
    
    
    def self.schedule_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ScheduleService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::ScheduleService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ScheduleService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ScheduleService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ScheduleService service. You can determine whether the method will succeed by calling [AIPlatform.schedule_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_schedule_service_available__class_ "Google::Cloud::AIPlatform.schedule_service_available? \(method\)").

#### About ScheduleService

A service for creating and managing Vertex AI's Schedule resources to periodically launch shceudled runs to make API calls.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .schedule_service_available?
    
    
    def self.schedule_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ScheduleService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.schedule_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_schedule_service_class_ "Google::Cloud::AIPlatform.schedule_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ScheduleService service, or if the versioned client gem needs an update to support the ScheduleService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .session_service
    
    
    def self.session_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for SessionService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::SessionService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SessionService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SessionService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the SessionService service. You can determine whether the method will succeed by calling [AIPlatform.session_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_session_service_available__class_ "Google::Cloud::AIPlatform.session_service_available? \(method\)").

#### About SessionService

The service that manages Vertex Session related resources.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .session_service_available?
    
    
    def self.session_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the SessionService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.session_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_session_service_class_ "Google::Cloud::AIPlatform.session_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SessionService service, or if the versioned client gem needs an update to support the SessionService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .specialist_pool_service
    
    
    def self.specialist_pool_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for SpecialistPoolService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::SpecialistPoolService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SpecialistPoolService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SpecialistPoolService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the SpecialistPoolService service. You can determine whether the method will succeed by calling [AIPlatform.specialist_pool_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_specialist_pool_service_available__class_ "Google::Cloud::AIPlatform.specialist_pool_service_available? \(method\)").

#### About SpecialistPoolService

A service for creating and managing Customer SpecialistPools. When customers start Data Labeling jobs, they can reuse/create Specialist Pools to bring their own Specialists to label the data. Customers can add/remove Managers for the Specialist Pool on Cloud console, then Managers will get email notifications to manage Specialists and tasks on CrowdCompute console.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .specialist_pool_service_available?
    
    
    def self.specialist_pool_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the SpecialistPoolService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.specialist_pool_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_specialist_pool_service_class_ "Google::Cloud::AIPlatform.specialist_pool_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SpecialistPoolService service, or if the versioned client gem needs an update to support the SpecialistPoolService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .tensorboard_service
    
    
    def self.tensorboard_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for TensorboardService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::TensorboardService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TensorboardService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the TensorboardService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the TensorboardService service. You can determine whether the method will succeed by calling [AIPlatform.tensorboard_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_tensorboard_service_available__class_ "Google::Cloud::AIPlatform.tensorboard_service_available? \(method\)").

#### About TensorboardService

TensorboardService

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .tensorboard_service_available?
    
    
    def self.tensorboard_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the TensorboardService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.tensorboard_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_tensorboard_service_class_ "Google::Cloud::AIPlatform.tensorboard_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the TensorboardService service, or if the versioned client gem needs an update to support the TensorboardService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .vertex_rag_data_service
    
    
    def self.vertex_rag_data_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for VertexRagDataService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::VertexRagDataService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VertexRagDataService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the VertexRagDataService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the VertexRagDataService service. You can determine whether the method will succeed by calling [AIPlatform.vertex_rag_data_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vertex_rag_data_service_available__class_ "Google::Cloud::AIPlatform.vertex_rag_data_service_available? \(method\)").

#### About VertexRagDataService

A service for managing user data for RAG.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .vertex_rag_data_service_available?
    
    
    def self.vertex_rag_data_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the VertexRagDataService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.vertex_rag_data_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vertex_rag_data_service_class_ "Google::Cloud::AIPlatform.vertex_rag_data_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the VertexRagDataService service, or if the versioned client gem needs an update to support the VertexRagDataService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .vertex_rag_service
    
    
    def self.vertex_rag_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for VertexRagService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::VertexRagService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VertexRagService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the VertexRagService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the VertexRagService service. You can determine whether the method will succeed by calling [AIPlatform.vertex_rag_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vertex_rag_service_available__class_ "Google::Cloud::AIPlatform.vertex_rag_service_available? \(method\)").

#### About VertexRagService

A service for retrieving relevant contexts.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .vertex_rag_service_available?
    
    
    def self.vertex_rag_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the VertexRagService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.vertex_rag_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vertex_rag_service_class_ "Google::Cloud::AIPlatform.vertex_rag_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the VertexRagService service, or if the versioned client gem needs an update to support the VertexRagService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .vizier_service
    
    
    def self.vizier_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for VizierService.

By default, this returns an instance of [Google::Cloud::AIPlatform::V1::VizierService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the VizierService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the VizierService service. You can determine whether the method will succeed by calling [AIPlatform.vizier_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vizier_service_available__class_ "Google::Cloud::AIPlatform.vizier_service_available? \(method\)").

#### About VizierService

Vertex AI Vizier API.

Vertex AI Vizier is a service to solve blackbox optimization problems, such as tuning machine learning hyperparameters and searching over deep learning architectures.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .vizier_service_available?
    
    
    def self.vizier_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the VizierService service is supported by the current client. If true, you can retrieve a client object by calling [AIPlatform.vizier_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform/latest/Google-Cloud-AIPlatform#Google__Cloud__AIPlatform_vizier_service_class_ "Google::Cloud::AIPlatform.vizier_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the VizierService service, or if the versioned client gem needs an update to support the VizierService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "2.4.2"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
