---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client/
title: Cloud Build V1 API - Class Google::Cloud::Build::V1::CloudBuild::Client (v1.14.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:45:55.922182+00:00
---

# Cloud Build V1 API - Class Google::Cloud::Build::V1::CloudBuild::Client (v1.14.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Build V1 API - Class Google::Cloud::Build::V1::CloudBuild::Client (v1.14.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.0 (latest)  1.13.1  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.27.1  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.3 

Reference documentation and code samples for the Cloud Build V1 API class Google::Cloud::Build::V1::CloudBuild::Client.

Client for the CloudBuild service.

Creates and manages builds on Google Cloud Platform.

The main concept used by this API is a `Build`, which describes the location of the source to build, how to build the source, and where to store the built artifacts, if any.

A user can list previously-requested builds or get builds by their ID to determine the status of the build.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Build::V1::CloudBuild::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the CloudBuild Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration "Google::Cloud::Build::V1::CloudBuild::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all CloudBuild clients
    ::Google::Cloud::Build::V1::CloudBuild::Client.configure do |config|
      config.timeout = 10.0
    end

### #approve_build
    
    
    def approve_build(request, options = nil) -> ::Gapic::Operation
    def approve_build(name: nil, approval_result: nil) -> ::Gapic::Operation

Approves or rejects a pending build.

If approved, the returned long-running operation (LRO) will be analogous to the LRO returned from a CreateBuild call.

If rejected, the returned LRO will be immediately done.

**Overloads**
    
    
    def approve_build(request, options = nil) -> ::Gapic::Operation

Pass arguments to `approve_build` via a request object, either of type [ApproveBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ApproveBuildRequest "Google::Cloud::Build::V1::ApproveBuildRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::ApproveBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ApproveBuildRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def approve_build(name: nil, approval_result: nil) -> ::Gapic::Operation

Pass arguments to `approve_build` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the target build. For example: "projects/{$project_id}/builds/{$build_id}" 
  * **approval_result** ([::Google::Cloud::Build::V1::ApprovalResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ApprovalResult), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Approval decision and metadata. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::ApproveBuildRequest.new
    
    # Call the approve_build method.
    result = client.approve_build request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #cancel_build
    
    
    def cancel_build(request, options = nil) -> ::Google::Cloud::Build::V1::Build
    def cancel_build(name: nil, project_id: nil, id: nil) -> ::Google::Cloud::Build::V1::Build

Cancels a build in progress.

**Overloads**
    
    
    def cancel_build(request, options = nil) -> ::Google::Cloud::Build::V1::Build

Pass arguments to `cancel_build` via a request object, either of type [Google::Cloud::Build::V1::CancelBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CancelBuildRequest "Google::Cloud::Build::V1::CancelBuildRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::CancelBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CancelBuildRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def cancel_build(name: nil, project_id: nil, id: nil) -> ::Google::Cloud::Build::V1::Build

Pass arguments to `cancel_build` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Build` to cancel. Format: `projects/{project}/locations/{location}/builds/{build}`
  * **project_id** (::String) — Required. ID of the project. 
  * **id** (::String) — Required. ID of the build. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::CancelBuildRequest.new
    
    # Call the cancel_build method.
    result = client.cancel_build request
    
    # The returned object is of type Google::Cloud::Build::V1::Build.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the CloudBuild Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client#Google__Cloud__Build__V1__CloudBuild__Client_configure_class_ "Google::Cloud::Build::V1::CloudBuild::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration "Google::Cloud::Build::V1::CloudBuild::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration)) 



### #create_build
    
    
    def create_build(request, options = nil) -> ::Gapic::Operation
    def create_build(parent: nil, project_id: nil, build: nil) -> ::Gapic::Operation

Starts a build with the specified configuration.

This method returns a long-running `Operation`, which includes the build ID. Pass the build ID to `GetBuild` to determine the build status (such as `SUCCESS` or `FAILURE`).

**Overloads**
    
    
    def create_build(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_build` via a request object, either of type [Google::Cloud::Build::V1::CreateBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateBuildRequest "Google::Cloud::Build::V1::CreateBuildRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::CreateBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateBuildRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_build(parent: nil, project_id: nil, build: nil) -> ::Gapic::Operation

Pass arguments to `create_build` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — The parent resource where this build will be created. Format: `projects/{project}/locations/{location}`
  * **project_id** (::String) — Required. ID of the project. 
  * **build** ([::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Required. Build resource to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::CreateBuildRequest.new
    
    # Call the create_build method.
    result = client.create_build request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_build_trigger
    
    
    def create_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger
    def create_build_trigger(parent: nil, project_id: nil, trigger: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Creates a new `BuildTrigger`.

**Overloads**
    
    
    def create_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `create_build_trigger` via a request object, either of type [Google::Cloud::Build::V1::CreateBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateBuildTriggerRequest "Google::Cloud::Build::V1::CreateBuildTriggerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::CreateBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateBuildTriggerRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_build_trigger(parent: nil, project_id: nil, trigger: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `create_build_trigger` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — The parent resource where this trigger will be created. Format: `projects/{project}/locations/{location}`
  * **project_id** (::String) — Required. ID of the project for which to configure automatic builds. 
  * **trigger** ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Required. `BuildTrigger` to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::CreateBuildTriggerRequest.new
    
    # Call the create_build_trigger method.
    result = client.create_build_trigger request
    
    # The returned object is of type Google::Cloud::Build::V1::BuildTrigger.
    p result

### #create_worker_pool
    
    
    def create_worker_pool(request, options = nil) -> ::Gapic::Operation
    def create_worker_pool(parent: nil, worker_pool: nil, worker_pool_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a `WorkerPool`.

**Overloads**
    
    
    def create_worker_pool(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_worker_pool` via a request object, either of type [Google::Cloud::Build::V1::CreateWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateWorkerPoolRequest "Google::Cloud::Build::V1::CreateWorkerPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::CreateWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CreateWorkerPoolRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_worker_pool(parent: nil, worker_pool: nil, worker_pool_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_worker_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this worker pool will be created. Format: `projects/{project}/locations/{location}`. 
  * **worker_pool** ([::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Required. `WorkerPool` resource to create. 
  * **worker_pool_id** (::String) — Required. Immutable. The ID to use for the `WorkerPool`, which will become the final component of the resource name.

This value should be 1-63 characters, and valid characters are /[a-z][0-9]-/. 

  * **validate_only** (::Boolean) — If set, validate the request and preview the response, but do not actually post it. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::CreateWorkerPoolRequest.new
    
    # Call the create_worker_pool method.
    result = client.create_worker_pool request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_build_trigger
    
    
    def delete_build_trigger(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_build_trigger(name: nil, project_id: nil, trigger_id: nil) -> ::Google::Protobuf::Empty

Deletes a `BuildTrigger` by its project ID and trigger ID.

**Overloads**
    
    
    def delete_build_trigger(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_build_trigger` via a request object, either of type [DeleteBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DeleteBuildTriggerRequest "Google::Cloud::Build::V1::DeleteBuildTriggerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::DeleteBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DeleteBuildTriggerRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_build_trigger(name: nil, project_id: nil, trigger_id: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_build_trigger` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Trigger` to delete. Format: `projects/{project}/locations/{location}/triggers/{trigger}`
  * **project_id** (::String) — Required. ID of the project that owns the trigger. 
  * **trigger_id** (::String) — Required. ID of the `BuildTrigger` to delete. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::DeleteBuildTriggerRequest.new
    
    # Call the delete_build_trigger method.
    result = client.delete_build_trigger request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_worker_pool
    
    
    def delete_worker_pool(request, options = nil) -> ::Gapic::Operation
    def delete_worker_pool(name: nil, etag: nil, allow_missing: nil, validate_only: nil) -> ::Gapic::Operation

Deletes a `WorkerPool`.

**Overloads**
    
    
    def delete_worker_pool(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_worker_pool` via a request object, either of type [DeleteWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DeleteWorkerPoolRequest "Google::Cloud::Build::V1::DeleteWorkerPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::DeleteWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DeleteWorkerPoolRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_worker_pool(name: nil, etag: nil, allow_missing: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `delete_worker_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the `WorkerPool` to delete. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`. 
  * **etag** (::String) — Optional. If provided, it must match the server's etag on the workerpool for the request to be processed. 
  * **allow_missing** (::Boolean) — If set to true, and the `WorkerPool` is not found, the request will succeed but no action will be taken on the server. 
  * **validate_only** (::Boolean) — If set, validate the request and preview the response, but do not actually post it. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::DeleteWorkerPoolRequest.new
    
    # Call the delete_worker_pool method.
    result = client.delete_worker_pool request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_build
    
    
    def get_build(request, options = nil) -> ::Google::Cloud::Build::V1::Build
    def get_build(name: nil, project_id: nil, id: nil) -> ::Google::Cloud::Build::V1::Build

Returns information about a previously requested build.

The `Build` that is returned includes its status (such as `SUCCESS`, `FAILURE`, or `WORKING`), and timing information.

**Overloads**
    
    
    def get_build(request, options = nil) -> ::Google::Cloud::Build::V1::Build

Pass arguments to `get_build` via a request object, either of type [GetBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetBuildRequest "Google::Cloud::Build::V1::GetBuildRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::GetBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetBuildRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_build(name: nil, project_id: nil, id: nil) -> ::Google::Cloud::Build::V1::Build

Pass arguments to `get_build` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Build` to retrieve. Format: `projects/{project}/locations/{location}/builds/{build}`
  * **project_id** (::String) — Required. ID of the project. 
  * **id** (::String) — Required. ID of the build. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::GetBuildRequest.new
    
    # Call the get_build method.
    result = client.get_build request
    
    # The returned object is of type Google::Cloud::Build::V1::Build.
    p result

### #get_build_trigger
    
    
    def get_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger
    def get_build_trigger(name: nil, project_id: nil, trigger_id: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Returns information about a `BuildTrigger`.

**Overloads**
    
    
    def get_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `get_build_trigger` via a request object, either of type [GetBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetBuildTriggerRequest "Google::Cloud::Build::V1::GetBuildTriggerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::GetBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetBuildTriggerRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_build_trigger(name: nil, project_id: nil, trigger_id: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `get_build_trigger` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Trigger` to retrieve. Format: `projects/{project}/locations/{location}/triggers/{trigger}`
  * **project_id** (::String) — Required. ID of the project that owns the trigger. 
  * **trigger_id** (::String) — Required. Identifier (`id` or `name`) of the `BuildTrigger` to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::GetBuildTriggerRequest.new
    
    # Call the get_build_trigger method.
    result = client.get_build_trigger request
    
    # The returned object is of type Google::Cloud::Build::V1::BuildTrigger.
    p result

### #get_default_service_account
    
    
    def get_default_service_account(request, options = nil) -> ::Google::Cloud::Build::V1::DefaultServiceAccount
    def get_default_service_account(name: nil) -> ::Google::Cloud::Build::V1::DefaultServiceAccount

Returns the `DefaultServiceAccount` used by the project.

**Overloads**
    
    
    def get_default_service_account(request, options = nil) -> ::Google::Cloud::Build::V1::DefaultServiceAccount

Pass arguments to `get_default_service_account` via a request object, either of type [GetDefaultServiceAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetDefaultServiceAccountRequest "Google::Cloud::Build::V1::GetDefaultServiceAccountRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::GetDefaultServiceAccountRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetDefaultServiceAccountRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_default_service_account(name: nil) -> ::Google::Cloud::Build::V1::DefaultServiceAccount

Pass arguments to `get_default_service_account` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the `DefaultServiceAccount` to retrieve. Format: `projects/{project}/locations/{location}/defaultServiceAccount`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::DefaultServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DefaultServiceAccount)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::DefaultServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-DefaultServiceAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::GetDefaultServiceAccountRequest.new
    
    # Call the get_default_service_account method.
    result = client.get_default_service_account request
    
    # The returned object is of type Google::Cloud::Build::V1::DefaultServiceAccount.
    p result

### #get_worker_pool
    
    
    def get_worker_pool(request, options = nil) -> ::Google::Cloud::Build::V1::WorkerPool
    def get_worker_pool(name: nil) -> ::Google::Cloud::Build::V1::WorkerPool

Returns details of a `WorkerPool`.

**Overloads**
    
    
    def get_worker_pool(request, options = nil) -> ::Google::Cloud::Build::V1::WorkerPool

Pass arguments to `get_worker_pool` via a request object, either of type [GetWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetWorkerPoolRequest "Google::Cloud::Build::V1::GetWorkerPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::GetWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-GetWorkerPoolRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_worker_pool(name: nil) -> ::Google::Cloud::Build::V1::WorkerPool

Pass arguments to `get_worker_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the `WorkerPool` to retrieve. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::GetWorkerPoolRequest.new
    
    # Call the get_worker_pool method.
    result = client.get_worker_pool request
    
    # The returned object is of type Google::Cloud::Build::V1::WorkerPool.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new CloudBuild client object.

**Yields**

  * (config) — Configure the CloudBuild client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Build::V1::CloudBuild::Client.new do |config|
      config.timeout = 10.0
    end

### #list_build_triggers
    
    
    def list_build_triggers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::BuildTrigger>
    def list_build_triggers(parent: nil, project_id: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::BuildTrigger>

Lists existing `BuildTrigger`s.

**Overloads**
    
    
    def list_build_triggers(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::BuildTrigger>

Pass arguments to `list_build_triggers` via a request object, either of type [ListBuildTriggersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListBuildTriggersRequest "Google::Cloud::Build::V1::ListBuildTriggersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::ListBuildTriggersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListBuildTriggersRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_build_triggers(parent: nil, project_id: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::BuildTrigger>

Pass arguments to `list_build_triggers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — The parent of the collection of `Triggers`. Format: `projects/{project}/locations/{location}`
  * **project_id** (::String) — Required. ID of the project for which to list BuildTriggers. 
  * **page_size** (::Integer) — Number of results to return in the list. 
  * **page_token** (::String) — Token to provide to skip to a particular spot in the list. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::ListBuildTriggersRequest.new
    
    # Call the list_build_triggers method.
    result = client.list_build_triggers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V1::BuildTrigger.
      p item
    end

### #list_builds
    
    
    def list_builds(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::Build>
    def list_builds(parent: nil, project_id: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::Build>

Lists previously requested builds.

Previously requested builds may still be in-progress, or may have finished successfully or unsuccessfully.

**Overloads**
    
    
    def list_builds(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::Build>

Pass arguments to `list_builds` via a request object, either of type [ListBuildsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListBuildsRequest "Google::Cloud::Build::V1::ListBuildsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::ListBuildsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListBuildsRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_builds(parent: nil, project_id: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::Build>

Pass arguments to `list_builds` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — The parent of the collection of `Builds`. Format: `projects/{project}/locations/{location}`
  * **project_id** (::String) — Required. ID of the project. 
  * **page_size** (::Integer) — Number of results to return in the list. 
  * **page_token** (::String) — The page token for the next page of Builds.

If unspecified, the first page of results is returned.

If the token is rejected for any reason, INVALID_ARGUMENT will be thrown. In this case, the token should be discarded, and pagination should be restarted from the first page of results.

See https://google.aip.dev/158 for more. 

  * **filter** (::String) — The raw filter text to constrain the results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::Build](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Build)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::ListBuildsRequest.new
    
    # Call the list_builds method.
    result = client.list_builds request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V1::Build.
      p item
    end

### #list_worker_pools
    
    
    def list_worker_pools(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::WorkerPool>
    def list_worker_pools(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::WorkerPool>

Lists `WorkerPool`s.

**Overloads**
    
    
    def list_worker_pools(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::WorkerPool>

Pass arguments to `list_worker_pools` via a request object, either of type [ListWorkerPoolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListWorkerPoolsRequest "Google::Cloud::Build::V1::ListWorkerPoolsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::ListWorkerPoolsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ListWorkerPoolsRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_worker_pools(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Build::V1::WorkerPool>

Pass arguments to `list_worker_pools` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent of the collection of `WorkerPools`. Format: `projects/{project}/locations/{location}`. 
  * **page_size** (::Integer) — The maximum number of `WorkerPool`s to return. The service may return fewer than this value. If omitted, the server will use a sensible default. 
  * **page_token** (::String) — A page token, received from a previous `ListWorkerPools` call. Provide this to retrieve the subsequent page. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::ListWorkerPoolsRequest.new
    
    # Call the list_worker_pools method.
    result = client.list_worker_pools request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Build::V1::WorkerPool.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Build::V1::CloudBuild::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Build::V1::CloudBuild::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-CloudBuild-Operations)) 



### #receive_trigger_webhook
    
    
    def receive_trigger_webhook(request, options = nil) -> ::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse
    def receive_trigger_webhook(name: nil, body: nil, project_id: nil, trigger: nil, secret: nil) -> ::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse

ReceiveTriggerWebhook [Experimental] is called when the API receives a webhook request targeted at a specific trigger.

**Overloads**
    
    
    def receive_trigger_webhook(request, options = nil) -> ::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse

Pass arguments to `receive_trigger_webhook` via a request object, either of type [ReceiveTriggerWebhookRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ReceiveTriggerWebhookRequest "Google::Cloud::Build::V1::ReceiveTriggerWebhookRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::ReceiveTriggerWebhookRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ReceiveTriggerWebhookRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def receive_trigger_webhook(name: nil, body: nil, project_id: nil, trigger: nil, secret: nil) -> ::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse

Pass arguments to `receive_trigger_webhook` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `ReceiveTriggerWebhook` to retrieve. Format: `projects/{project}/locations/{location}/triggers/{trigger}`
  * **body** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Api-HttpBody), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — HTTP request body. 
  * **project_id** (::String) — Project in which the specified trigger lives 
  * **trigger** (::String) — Name of the trigger to run the payload against 
  * **secret** (::String) — Secret token used for authorization if an OAuth token isn't provided. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ReceiveTriggerWebhookResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-ReceiveTriggerWebhookResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::ReceiveTriggerWebhookRequest.new
    
    # Call the receive_trigger_webhook method.
    result = client.receive_trigger_webhook request
    
    # The returned object is of type Google::Cloud::Build::V1::ReceiveTriggerWebhookResponse.
    p result

### #retry_build
    
    
    def retry_build(request, options = nil) -> ::Gapic::Operation
    def retry_build(name: nil, project_id: nil, id: nil) -> ::Gapic::Operation

Creates a new build based on the specified build.

This method creates a new build using the original build request, which may or may not result in an identical build.

For triggered builds:

  * Triggered builds resolve to a precise revision; therefore a retry of a triggered build will result in a build that uses the same revision.



For non-triggered builds that specify `RepoSource`:

  * If the original build built from the tip of a branch, the retried build will build from the tip of that branch, which may not be the same revision as the original build.
  * If the original build specified a commit sha or revision ID, the retried build will use the identical source.



For builds that specify `StorageSource`:

  * If the original build pulled source from Cloud Storage without specifying the generation of the object, the new build will use the current object, which may be different from the original build source.
  * If the original build pulled source from Cloud Storage and specified the generation of the object, the new build will attempt to use the same object, which may or may not be available depending on the bucket's lifecycle management settings.



**Overloads**
    
    
    def retry_build(request, options = nil) -> ::Gapic::Operation

Pass arguments to `retry_build` via a request object, either of type [RetryBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-RetryBuildRequest "Google::Cloud::Build::V1::RetryBuildRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::RetryBuildRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-RetryBuildRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def retry_build(name: nil, project_id: nil, id: nil) -> ::Gapic::Operation

Pass arguments to `retry_build` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Build` to retry. Format: `projects/{project}/locations/{location}/builds/{build}`
  * **project_id** (::String) — Required. ID of the project. 
  * **id** (::String) — Required. Build ID of the original build. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::RetryBuildRequest.new
    
    # Call the retry_build method.
    result = client.retry_build request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #run_build_trigger
    
    
    def run_build_trigger(request, options = nil) -> ::Gapic::Operation
    def run_build_trigger(name: nil, project_id: nil, trigger_id: nil, source: nil) -> ::Gapic::Operation

Runs a `BuildTrigger` at a particular source revision.

To run a regional or global trigger, use the POST request that includes the location endpoint in the path (ex. v1/projects/{projectId}/locations/{region}/triggers/{triggerId}:run). The POST request that does not include the location endpoint in the path can only be used when running global triggers.

**Overloads**
    
    
    def run_build_trigger(request, options = nil) -> ::Gapic::Operation

Pass arguments to `run_build_trigger` via a request object, either of type [RunBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-RunBuildTriggerRequest "Google::Cloud::Build::V1::RunBuildTriggerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::RunBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-RunBuildTriggerRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def run_build_trigger(name: nil, project_id: nil, trigger_id: nil, source: nil) -> ::Gapic::Operation

Pass arguments to `run_build_trigger` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the `Trigger` to run. Format: `projects/{project}/locations/{location}/triggers/{trigger}`
  * **project_id** (::String) — Required. ID of the project. 
  * **trigger_id** (::String) — Required. ID of the trigger. 
  * **source** ([::Google::Cloud::Build::V1::RepoSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-RepoSource), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Source to build against this trigger. Branch and tag names cannot consist of regular expressions. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::RunBuildTriggerRequest.new
    
    # Call the run_build_trigger method.
    result = client.run_build_trigger request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_build_trigger
    
    
    def update_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger
    def update_build_trigger(project_id: nil, trigger_id: nil, trigger: nil, update_mask: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Updates a `BuildTrigger` by its project ID and trigger ID.

**Overloads**
    
    
    def update_build_trigger(request, options = nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `update_build_trigger` via a request object, either of type [UpdateBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-UpdateBuildTriggerRequest "Google::Cloud::Build::V1::UpdateBuildTriggerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::UpdateBuildTriggerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-UpdateBuildTriggerRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_build_trigger(project_id: nil, trigger_id: nil, trigger: nil, update_mask: nil) -> ::Google::Cloud::Build::V1::BuildTrigger

Pass arguments to `update_build_trigger` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project_id** (::String) — Required. ID of the project that owns the trigger. 
  * **trigger_id** (::String) — Required. ID of the `BuildTrigger` to update. 
  * **trigger** ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Required. `BuildTrigger` to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Protobuf-FieldMask), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Update mask for the resource. If this is set, the server will only update the fields specified in the field mask. Otherwise, a full update of the mutable resource fields will be performed. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Build::V1::BuildTrigger](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-BuildTrigger)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::UpdateBuildTriggerRequest.new
    
    # Call the update_build_trigger method.
    result = client.update_build_trigger request
    
    # The returned object is of type Google::Cloud::Build::V1::BuildTrigger.
    p result

### #update_worker_pool
    
    
    def update_worker_pool(request, options = nil) -> ::Gapic::Operation
    def update_worker_pool(worker_pool: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Updates a `WorkerPool`.

**Overloads**
    
    
    def update_worker_pool(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_worker_pool` via a request object, either of type [UpdateWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-UpdateWorkerPoolRequest "Google::Cloud::Build::V1::UpdateWorkerPoolRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Build::V1::UpdateWorkerPoolRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-UpdateWorkerPoolRequest), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_worker_pool(worker_pool: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_worker_pool` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **worker_pool** ([::Google::Cloud::Build::V1::WorkerPool](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-WorkerPool), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Required. The `WorkerPool` to update.

The `name` field is used to identify the `WorkerPool` to update. Format: `projects/{project}/locations/{location}/workerPools/{workerPool}`. 

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Protobuf-FieldMask), [::Hash](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-build-v1/latest/Google-Cloud-Build-V1-Hash)) — Optional. A mask specifying which fields in `worker_pool` to update. 
  * **validate_only** (::Boolean) — If set, validate the request and preview the response, but do not actually post it. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/build/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Build::V1::CloudBuild::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Build::V1::UpdateWorkerPoolRequest.new
    
    # Call the update_worker_pool method.
    result = client.update_worker_pool request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
