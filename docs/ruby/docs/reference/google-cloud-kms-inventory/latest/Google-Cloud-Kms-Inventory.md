---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory/
title: KMS Inventory API - Module Google::Cloud::Kms::Inventory (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:39:10.018150+00:00
---

# KMS Inventory API - Module Google::Cloud::Kms::Inventory (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  KMS Inventory API - Module Google::Cloud::Kms::Inventory (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.0  1.3.2  1.2.1  1.1.0  1.0.0  0.1.0 

Reference documentation and code samples for the KMS Inventory API module Google::Cloud::Kms::Inventory.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-kms-inventory library.

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

  * (::Google::Cloud.configure.kms_inventory) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .key_dashboard_service
    
    
    def self.key_dashboard_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for KeyDashboardService.

By default, this returns an instance of [Google::Cloud::Kms::Inventory::V1::KeyDashboardService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyDashboardService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the KeyDashboardService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the KeyDashboardService service. You can determine whether the method will succeed by calling [Inventory.key_dashboard_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory#Google__Cloud__Kms__Inventory_key_dashboard_service_available__class_ "Google::Cloud::Kms::Inventory.key_dashboard_service_available? \(method\)").

#### About KeyDashboardService

Provides a cross-region view of all Cloud KMS keys in a given Cloud project.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .key_dashboard_service_available?
    
    
    def self.key_dashboard_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the KeyDashboardService service is supported by the current client. If true, you can retrieve a client object by calling [Inventory.key_dashboard_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory#Google__Cloud__Kms__Inventory_key_dashboard_service_class_ "Google::Cloud::Kms::Inventory.key_dashboard_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the KeyDashboardService service, or if the versioned client gem needs an update to support the KeyDashboardService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .key_tracking_service
    
    
    def self.key_tracking_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for KeyTrackingService.

By default, this returns an instance of [Google::Cloud::Kms::Inventory::V1::KeyTrackingService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory-v1/latest/Google-Cloud-Kms-Inventory-V1-KeyTrackingService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the KeyTrackingService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the KeyTrackingService service. You can determine whether the method will succeed by calling [Inventory.key_tracking_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory#Google__Cloud__Kms__Inventory_key_tracking_service_available__class_ "Google::Cloud::Kms::Inventory.key_tracking_service_available? \(method\)").

#### About KeyTrackingService

Returns information about the resources in an org that are protected by a given Cloud KMS key via CMEK.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .key_tracking_service_available?
    
    
    def self.key_tracking_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the KeyTrackingService service is supported by the current client. If true, you can retrieve a client object by calling [Inventory.key_tracking_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-inventory/latest/Google-Cloud-Kms-Inventory#Google__Cloud__Kms__Inventory_key_tracking_service_class_ "Google::Cloud::Kms::Inventory.key_tracking_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the KeyTrackingService service, or if the versioned client gem needs an update to support the KeyTrackingService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "1.5.1"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
