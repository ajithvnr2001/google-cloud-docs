---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization/
title: Binary Authorization API - Module Google::Cloud::BinaryAuthorization (v2.2.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:27:11.811088+00:00
---

# Binary Authorization API - Module Google::Cloud::BinaryAuthorization (v2.2.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Binary Authorization API - Module Google::Cloud::BinaryAuthorization (v2.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.2.1 (latest)  2.2.0  2.1.0  2.0.2  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1 

Reference documentation and code samples for the Binary Authorization API module Google::Cloud::BinaryAuthorization.

## Methods 

### .binauthz_management_service
    
    
    def self.binauthz_management_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for BinauthzManagementService.

By default, this returns an instance of [Google::Cloud::BinaryAuthorization::V1::BinauthzManagementService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Cloud-BinaryAuthorization-V1-BinauthzManagementService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the BinauthzManagementService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the BinauthzManagementService service. You can determine whether the method will succeed by calling [BinaryAuthorization.binauthz_management_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_binauthz_management_service_available__class_ "Google::Cloud::BinaryAuthorization.binauthz_management_service_available? \(method\)").

#### About BinauthzManagementService

Google Cloud Management Service for Binary Authorization admission policies and attestation authorities.

This API implements a REST model with the following objects:

  * Policy
  * Attestor



**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .binauthz_management_service_available?
    
    
    def self.binauthz_management_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the BinauthzManagementService service is supported by the current client. If true, you can retrieve a client object by calling [BinaryAuthorization.binauthz_management_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_binauthz_management_service_class_ "Google::Cloud::BinaryAuthorization.binauthz_management_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the BinauthzManagementService service, or if the versioned client gem needs an update to support the BinauthzManagementService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-binary_authorization library.

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

  * (::Google::Cloud.configure.binary_authorization) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .system_policy
    
    
    def self.system_policy(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for SystemPolicy.

By default, this returns an instance of [Google::Cloud::BinaryAuthorization::V1::SystemPolicy::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Cloud-BinaryAuthorization-V1-SystemPolicy-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the SystemPolicy service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the SystemPolicy service. You can determine whether the method will succeed by calling [BinaryAuthorization.system_policy_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_system_policy_available__class_ "Google::Cloud::BinaryAuthorization.system_policy_available? \(method\)").

#### About SystemPolicy

API for working with the system policy.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .system_policy_available?
    
    
    def self.system_policy_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the SystemPolicy service is supported by the current client. If true, you can retrieve a client object by calling [BinaryAuthorization.system_policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_system_policy_class_ "Google::Cloud::BinaryAuthorization.system_policy \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the SystemPolicy service, or if the versioned client gem needs an update to support the SystemPolicy service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .validation_helper
    
    
    def self.validation_helper(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for ValidationHelper.

By default, this returns an instance of [Google::Cloud::BinaryAuthorization::V1::ValidationHelper::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Cloud-BinaryAuthorization-V1-ValidationHelper-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the ValidationHelper service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the ValidationHelper service. You can determine whether the method will succeed by calling [BinaryAuthorization.validation_helper_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_validation_helper_available__class_ "Google::Cloud::BinaryAuthorization.validation_helper_available? \(method\)").

#### About ValidationHelper

BinAuthz Attestor verification

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .validation_helper_available?
    
    
    def self.validation_helper_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the ValidationHelper service is supported by the current client. If true, you can retrieve a client object by calling [BinaryAuthorization.validation_helper](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization/latest/Google-Cloud-BinaryAuthorization#Google__Cloud__BinaryAuthorization_validation_helper_class_ "Google::Cloud::BinaryAuthorization.validation_helper \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the ValidationHelper service, or if the versioned client gem needs an update to support the ValidationHelper service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "2.2.1"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
