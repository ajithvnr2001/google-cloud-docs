---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner/latest/Google-Cloud-CapacityPlanner/
title: Capacity Planner API - Module Google::Cloud::CapacityPlanner (v0.4.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:25.361364+00:00
---

# Capacity Planner API - Module Google::Cloud::CapacityPlanner (v0.4.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner/latest/Google-Cloud-CapacityPlanner/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Capacity Planner API - Module Google::Cloud::CapacityPlanner (v0.4.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.1 (latest)  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Capacity Planner API module Google::Cloud::CapacityPlanner.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-capacity_planner library.

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

  * (::Google::Cloud.configure.capacity_planner) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .usage_service
    
    
    def self.usage_service(version: :v1beta, transport: :grpc, &block) -> ::Object

Create a new client object for UsageService.

By default, this returns an instance of [Google::Cloud::CapacityPlanner::V1beta::UsageService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner-v1beta/latest/Google-Cloud-CapacityPlanner-V1beta-UsageService-Client) for a gRPC client for version V1beta of the API. However, you can specify a different API version by passing it in the `version` parameter. If the UsageService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the UsageService service. You can determine whether the method will succeed by calling [CapacityPlanner.usage_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner/latest/Google-Cloud-CapacityPlanner#Google__Cloud__CapacityPlanner_usage_service_available__class_ "Google::Cloud::CapacityPlanner.usage_service_available? \(method\)").

#### About UsageService

Provides access to historical and forecasted usage data.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1beta)_ — The API version to connect to. Optional. Defaults to `:v1beta`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .usage_service_available?
    
    
    def self.usage_service_available?(version: :v1beta, transport: :grpc) -> boolean

Determines whether the UsageService service is supported by the current client. If true, you can retrieve a client object by calling [CapacityPlanner.usage_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-capacity_planner/latest/Google-Cloud-CapacityPlanner#Google__Cloud__CapacityPlanner_usage_service_class_ "Google::Cloud::CapacityPlanner.usage_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the UsageService service, or if the versioned client gem needs an update to support the UsageService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1beta)_ — The API version to connect to. Optional. Defaults to `:v1beta`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



## Constants 

### VERSION

**value:** "0.4.1"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
