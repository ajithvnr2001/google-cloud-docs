---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::GenAiTuningService::Client (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:39:15.455624+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::GenAiTuningService::Client (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::GenAiTuningService::Client (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.

Client for the GenAiTuningService service.

A service for creating and managing GenAI Tuning Jobs.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AIPlatform::V1::GenAiTuningService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the GenAiTuningService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration "Google::Cloud::AIPlatform::V1::GenAiTuningService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all GenAiTuningService clients
    ::Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.configure do |config|
      config.timeout = 10.0
    end

### #cancel_tuning_job
    
    
    def cancel_tuning_job(request, options = nil) -> ::Google::Protobuf::Empty
    def cancel_tuning_job(name: nil) -> ::Google::Protobuf::Empty

Cancels a TuningJob. Starts asynchronous cancellation on the TuningJob. The server makes a best effort to cancel the job, but success is not guaranteed. Clients can use [GenAiTuningService.GetTuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client#Google__Cloud__AIPlatform__V1__GenAiTuningService__Client_get_tuning_job_instance_ "Google::Cloud::AIPlatform::V1::GenAiTuningService::Client#get_tuning_job \(method\)") or other methods to check whether the cancellation succeeded or whether the job completed despite cancellation. On successful cancellation, the TuningJob is not deleted; instead it becomes a job with a [TuningJob.error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob#Google__Cloud__AIPlatform__V1__TuningJob_error_instance_ "Google::Cloud::AIPlatform::V1::TuningJob#error \(method\)") value with a [google.rpc.Status.code](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Rpc-Status#Google__Rpc__Status_code_instance_ "Google::Rpc::Status#code \(method\)") of 1, corresponding to `Code.CANCELLED`, and [TuningJob.state](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob#Google__Cloud__AIPlatform__V1__TuningJob_state_instance_ "Google::Cloud::AIPlatform::V1::TuningJob#state \(method\)") is set to `CANCELLED`.

**Overloads**
    
    
    def cancel_tuning_job(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel_tuning_job` via a request object, either of type [CancelTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CancelTuningJobRequest "Google::Cloud::AIPlatform::V1::CancelTuningJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CancelTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CancelTuningJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def cancel_tuning_job(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel_tuning_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the TuningJob to cancel. Format: `projects/{project}/locations/{location}/tuningJobs/{tuning_job}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CancelTuningJobRequest.new
    
    # Call the cancel_tuning_job method.
    result = client.cancel_tuning_job request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the GenAiTuningService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client#Google__Cloud__AIPlatform__V1__GenAiTuningService__Client_configure_class_ "Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration "Google::Cloud::AIPlatform::V1::GenAiTuningService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration)) 



### #create_tuning_job
    
    
    def create_tuning_job(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob
    def create_tuning_job(parent: nil, tuning_job: nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Creates a TuningJob. A created TuningJob right away will be attempted to be run.

**Overloads**
    
    
    def create_tuning_job(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Pass arguments to `create_tuning_job` via a request object, either of type [CreateTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateTuningJobRequest "Google::Cloud::AIPlatform::V1::CreateTuningJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateTuningJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_tuning_job(parent: nil, tuning_job: nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Pass arguments to `create_tuning_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to create the TuningJob in. Format: `projects/{project}/locations/{location}`
  * **tuning_job** ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob), ::Hash) — Required. The TuningJob to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateTuningJobRequest.new
    
    # Call the create_tuning_job method.
    result = client.create_tuning_job request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::TuningJob.
    p result

### #get_tuning_job
    
    
    def get_tuning_job(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob
    def get_tuning_job(name: nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Gets a TuningJob.

**Overloads**
    
    
    def get_tuning_job(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Pass arguments to `get_tuning_job` via a request object, either of type [Google::Cloud::AIPlatform::V1::GetTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetTuningJobRequest "Google::Cloud::AIPlatform::V1::GetTuningJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetTuningJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetTuningJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_tuning_job(name: nil) -> ::Google::Cloud::AIPlatform::V1::TuningJob

Pass arguments to `get_tuning_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the TuningJob resource. Format: `projects/{project}/locations/{location}/tuningJobs/{tuning_job}`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetTuningJobRequest.new
    
    # Call the get_tuning_job method.
    result = client.get_tuning_job request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::TuningJob.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new GenAiTuningService client object.

**Yields**

  * (config) — Configure the GenAiTuningService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_tuning_jobs
    
    
    def list_tuning_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::TuningJob>
    def list_tuning_jobs(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::TuningJob>

Lists TuningJobs in a Location.

**Overloads**
    
    
    def list_tuning_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::TuningJob>

Pass arguments to `list_tuning_jobs` via a request object, either of type [ListTuningJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListTuningJobsRequest "Google::Cloud::AIPlatform::V1::ListTuningJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListTuningJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListTuningJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_tuning_jobs(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AIPlatform::V1::TuningJob>

Pass arguments to `list_tuning_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to list the TuningJobs from. Format: `projects/{project}/locations/{location}`
  * **filter** (::String) — Optional. The standard list filter. 
  * **page_size** (::Integer) — Optional. The standard list page size. 
  * **page_token** (::String) — Optional. The standard list page token. Typically obtained via [ListTuningJobsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListTuningJobsResponse#Google__Cloud__AIPlatform__V1__ListTuningJobsResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListTuningJobsResponse#next_page_token \(method\)") of the previous GenAiTuningService.ListTuningJob][] call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListTuningJobsRequest.new
    
    # Call the list_tuning_jobs method.
    result = client.list_tuning_jobs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::TuningJob.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AIPlatform::V1::GenAiTuningService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::GenAiTuningService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GenAiTuningService-Operations)) 



### #rebase_tuned_model
    
    
    def rebase_tuned_model(request, options = nil) -> ::Gapic::Operation
    def rebase_tuned_model(parent: nil, tuned_model_ref: nil, tuning_job: nil, artifact_destination: nil, deploy_to_same_endpoint: nil) -> ::Gapic::Operation

Rebase a TunedModel.

**Overloads**
    
    
    def rebase_tuned_model(request, options = nil) -> ::Gapic::Operation

Pass arguments to `rebase_tuned_model` via a request object, either of type [RebaseTunedModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RebaseTunedModelRequest "Google::Cloud::AIPlatform::V1::RebaseTunedModelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::RebaseTunedModelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RebaseTunedModelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def rebase_tuned_model(parent: nil, tuned_model_ref: nil, tuning_job: nil, artifact_destination: nil, deploy_to_same_endpoint: nil) -> ::Gapic::Operation

Pass arguments to `rebase_tuned_model` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location into which to rebase the Model. Format: `projects/{project}/locations/{location}`
  * **tuned_model_ref** ([::Google::Cloud::AIPlatform::V1::TunedModelRef](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TunedModelRef), ::Hash) — Required. TunedModel reference to retrieve the legacy model information. 
  * **tuning_job** ([::Google::Cloud::AIPlatform::V1::TuningJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-TuningJob), ::Hash) — Optional. The TuningJob to be updated. Users can use this TuningJob field to overwrite tuning configs. 
  * **artifact_destination** ([::Google::Cloud::AIPlatform::V1::GcsDestination](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GcsDestination), ::Hash) — Optional. The Google Cloud Storage location to write the artifacts. 
  * **deploy_to_same_endpoint** (::Boolean) — Optional. By default, bison to gemini migration will always create new model/endpoint, but for gemini-1.0 to gemini-1.5 migration, we default deploy to the same endpoint. See details in this Section. 



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::GenAiTuningService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::RebaseTunedModelRequest.new
    
    # Call the rebase_tuned_model method.
    result = client.rebase_tuned_model request
    
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
