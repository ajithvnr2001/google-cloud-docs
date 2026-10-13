---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring-Dashboard/
title: Cloud Monitoring API - Module Google::Cloud::Monitoring::Dashboard (v1.11.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:35.377730+00:00
---

# Cloud Monitoring API - Module Google::Cloud::Monitoring::Dashboard (v1.11.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring-Dashboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring API - Module Google::Cloud::Monitoring::Dashboard (v1.11.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.1 (latest)  1.11.0  1.10.0  1.9.3  1.8.3  1.7.0  1.6.1  1.5.0  1.4.1  1.3.1 

Reference documentation and code samples for the Cloud Monitoring API module Google::Cloud::Monitoring::Dashboard.

## Methods 

### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-monitoring-dashboard library.

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

  * (::Google::Cloud.configure.monitoring_dashboard) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .dashboards_service
    
    
    def self.dashboards_service(version: :v1, transport: :grpc, &block) -> ::Object

Create a new client object for DashboardsService.

By default, this returns an instance of [Google::Cloud::Monitoring::Dashboard::V1::DashboardsService::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-monitoring-dashboard-v1/latest/Google-Cloud-Monitoring-Dashboard-V1-DashboardsService-Client) for a gRPC client for version V1 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the DashboardsService service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the DashboardsService service. You can determine whether the method will succeed by calling [Dashboard.dashboards_service_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring-Dashboard#Google__Cloud__Monitoring__Dashboard_dashboards_service_available__class_ "Google::Cloud::Monitoring::Dashboard.dashboards_service_available? \(method\)").

#### About DashboardsService

Manages Stackdriver dashboards. A dashboard is an arrangement of data display widgets in a specific layout.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .dashboards_service_available?
    
    
    def self.dashboards_service_available?(version: :v1, transport: :grpc) -> boolean

Determines whether the DashboardsService service is supported by the current client. If true, you can retrieve a client object by calling [Dashboard.dashboards_service](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring/latest/Google-Cloud-Monitoring-Dashboard#Google__Cloud__Monitoring__Dashboard_dashboards_service_class_ "Google::Cloud::Monitoring::Dashboard.dashboards_service \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the DashboardsService service, or if the versioned client gem needs an update to support the DashboardsService service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v1)_ — The API version to connect to. Optional. Defaults to `:v1`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
