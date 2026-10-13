---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run/
title: Cloud Run API - Module Google::Cloud::Run (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:32:09.185293+00:00
---

# Cloud Run API - Module Google::Cloud::Run (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run API - Module Google::Cloud::Run (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.1  1.3.0  1.2.1  1.1.0  1.0.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run API module Google::Cloud::Run.

## Methods 

### .builds
    
    
    def self.builds(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Builds.

By default, this returns an instance of [Google::Cloud::Run::V2::Builds::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Builds-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Builds service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Builds service. You can determine whether the method will succeed by calling [Run.builds_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_builds_available__class_ "Google::Cloud::Run.builds_available? \(method\)").

#### About Builds

Cloud Run Build Control Plane API

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .builds_available?
    
    
    def self.builds_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Builds service is supported by the current client. If true, you can retrieve a client object by calling [Run.builds](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_builds_class_ "Google::Cloud::Run.builds \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Builds service, or if the versioned client gem needs an update to support the Builds service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .configure
    
    
    def self.configure() -> ::Google::Cloud::Config

Configure the google-cloud-run-client library.

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

  * (::Google::Cloud.configure.run) 



**Returns**

  * (::Google::Cloud::Config) — The default configuration used by this library 



### .executions
    
    
    def self.executions(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Executions.

By default, this returns an instance of [Google::Cloud::Run::V2::Executions::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Executions-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Executions service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Executions service. You can determine whether the method will succeed by calling [Run.executions_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_executions_available__class_ "Google::Cloud::Run.executions_available? \(method\)").

#### About Executions

Cloud Run Execution Control Plane API.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .executions_available?
    
    
    def self.executions_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Executions service is supported by the current client. If true, you can retrieve a client object by calling [Run.executions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_executions_class_ "Google::Cloud::Run.executions \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Executions service, or if the versioned client gem needs an update to support the Executions service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .instances
    
    
    def self.instances(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Instances.

By default, this returns an instance of [Google::Cloud::Run::V2::Instances::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Instances-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Instances service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Instances service. You can determine whether the method will succeed by calling [Run.instances_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_instances_available__class_ "Google::Cloud::Run.instances_available? \(method\)").

#### About Instances

The Cloud Run Instances API allows you to manage Cloud Run Instances.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .instances_available?
    
    
    def self.instances_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Instances service is supported by the current client. If true, you can retrieve a client object by calling [Run.instances](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_instances_class_ "Google::Cloud::Run.instances \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Instances service, or if the versioned client gem needs an update to support the Instances service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .jobs
    
    
    def self.jobs(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Jobs.

By default, this returns an instance of [Google::Cloud::Run::V2::Jobs::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Jobs service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Jobs service. You can determine whether the method will succeed by calling [Run.jobs_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_jobs_available__class_ "Google::Cloud::Run.jobs_available? \(method\)").

#### About Jobs

Cloud Run Job Control Plane API.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .jobs_available?
    
    
    def self.jobs_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Jobs service is supported by the current client. If true, you can retrieve a client object by calling [Run.jobs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_jobs_class_ "Google::Cloud::Run.jobs \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Jobs service, or if the versioned client gem needs an update to support the Jobs service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .revisions
    
    
    def self.revisions(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Revisions.

By default, this returns an instance of [Google::Cloud::Run::V2::Revisions::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Revisions-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Revisions service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Revisions service. You can determine whether the method will succeed by calling [Run.revisions_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_revisions_available__class_ "Google::Cloud::Run.revisions_available? \(method\)").

#### About Revisions

Cloud Run Revision Control Plane API.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .revisions_available?
    
    
    def self.revisions_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Revisions service is supported by the current client. If true, you can retrieve a client object by calling [Run.revisions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_revisions_class_ "Google::Cloud::Run.revisions \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Revisions service, or if the versioned client gem needs an update to support the Revisions service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .services
    
    
    def self.services(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Services.

By default, this returns an instance of [Google::Cloud::Run::V2::Services::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Services-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Services service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Services service. You can determine whether the method will succeed by calling [Run.services_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_services_available__class_ "Google::Cloud::Run.services_available? \(method\)").

#### About Services

Cloud Run Service Control Plane API

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .services_available?
    
    
    def self.services_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Services service is supported by the current client. If true, you can retrieve a client object by calling [Run.services](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_services_class_ "Google::Cloud::Run.services \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Services service, or if the versioned client gem needs an update to support the Services service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .tasks
    
    
    def self.tasks(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for Tasks.

By default, this returns an instance of [Google::Cloud::Run::V2::Tasks::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the Tasks service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the Tasks service. You can determine whether the method will succeed by calling [Run.tasks_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_tasks_available__class_ "Google::Cloud::Run.tasks_available? \(method\)").

#### About Tasks

Cloud Run Task Control Plane API.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .tasks_available?
    
    
    def self.tasks_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the Tasks service is supported by the current client. If true, you can retrieve a client object by calling [Run.tasks](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_tasks_class_ "Google::Cloud::Run.tasks \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the Tasks service, or if the versioned client gem needs an update to support the Tasks service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



### .worker_pools
    
    
    def self.worker_pools(version: :v2, transport: :grpc, &block) -> ::Object

Create a new client object for WorkerPools.

By default, this returns an instance of [Google::Cloud::Run::V2::WorkerPools::Client](https://cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-WorkerPools-Client) for a gRPC client for version V2 of the API. However, you can specify a different API version by passing it in the `version` parameter. If the WorkerPools service is supported by that API version, and the corresponding gem is available, the appropriate versioned client will be returned. You can also specify a different transport by passing `:rest` or `:grpc` in the `transport` parameter.

Raises an exception if the currently installed versioned client gem for the given API version does not support the given transport of the WorkerPools service. You can determine whether the method will succeed by calling [Run.worker_pools_available?](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_worker_pools_available__class_ "Google::Cloud::Run.worker_pools_available? \(method\)").

#### About WorkerPools

Cloud Run WorkerPool Control Plane API.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (::Object) — A client object for the specified version. 



### .worker_pools_available?
    
    
    def self.worker_pools_available?(version: :v2, transport: :grpc) -> boolean

Determines whether the WorkerPools service is supported by the current client. If true, you can retrieve a client object by calling [Run.worker_pools](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-client/latest/Google-Cloud-Run#Google__Cloud__Run_worker_pools_class_ "Google::Cloud::Run.worker_pools \(method\)"). If false, that method will raise an exception. This could happen if the given API version does not exist or does not support the WorkerPools service, or if the versioned client gem needs an update to support the WorkerPools service.

**Parameters**

  * **version** (::String, ::Symbol) _(defaults to: :v2)_ — The API version to connect to. Optional. Defaults to `:v2`. 
  * **transport** (:grpc, :rest) _(defaults to: :grpc)_ — The transport to use. Defaults to `:grpc`. 



**Returns**

  * (boolean) — Whether the service is available. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
