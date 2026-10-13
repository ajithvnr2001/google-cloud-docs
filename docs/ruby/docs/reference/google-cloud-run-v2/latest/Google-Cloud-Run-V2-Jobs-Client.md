---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::Jobs::Client (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:50:30.872624+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::Jobs::Client (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::Jobs::Client (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::Jobs::Client.

Client for the Jobs service.

Cloud Run Job Control Plane API.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Run::V2::Jobs::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Jobs Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration "Google::Cloud::Run::V2::Jobs::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Jobs clients
    ::Google::Cloud::Run::V2::Jobs::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Jobs Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client#Google__Cloud__Run__V2__Jobs__Client_configure_class_ "Google::Cloud::Run::V2::Jobs::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration "Google::Cloud::Run::V2::Jobs::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration)) 



### #create_job
    
    
    def create_job(request, options = nil) -> ::Gapic::Operation
    def create_job(parent: nil, job: nil, job_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a Job.

**Overloads**
    
    
    def create_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_job` via a request object, either of type [CreateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-CreateJobRequest "Google::Cloud::Run::V2::CreateJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::CreateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-CreateJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_job(parent: nil, job: nil, job_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location and project in which this Job should be created. Format: projects/{project}/locations/{location}, where {project} can be project id or number. 
  * **job** ([::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job), ::Hash) — Required. The Job instance to create. 
  * **job_id** (::String) — Required. The unique identifier for the Job. The name of the job becomes {parent}/jobs/{job_id}. 
  * **validate_only** (::Boolean) — Indicates that the request should be validated and default values populated, without persisting the request or creating any resources. 



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
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::CreateJobRequest.new
    
    # Call the create_job method.
    result = client.create_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_job
    
    
    def delete_job(request, options = nil) -> ::Gapic::Operation
    def delete_job(name: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Deletes a Job.

**Overloads**
    
    
    def delete_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_job` via a request object, either of type [DeleteJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-DeleteJobRequest "Google::Cloud::Run::V2::DeleteJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::DeleteJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-DeleteJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_job(name: nil, validate_only: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The full name of the Job. Format: projects/{project}/locations/{location}/jobs/{job}, where {project} can be project id or number. 
  * **validate_only** (::Boolean) — Indicates that the request should be validated without actually deleting any resources. 
  * **etag** (::String) — A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. 



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
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::DeleteJobRequest.new
    
    # Call the delete_job method.
    result = client.delete_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the IAM Access Control policy currently in effect for the given Job. This result does not include any inherited policies.

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #get_job
    
    
    def get_job(request, options = nil) -> ::Google::Cloud::Run::V2::Job
    def get_job(name: nil) -> ::Google::Cloud::Run::V2::Job

Gets information about a Job.

**Overloads**
    
    
    def get_job(request, options = nil) -> ::Google::Cloud::Run::V2::Job

Pass arguments to `get_job` via a request object, either of type [GetJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-GetJobRequest "Google::Cloud::Run::V2::GetJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::GetJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-GetJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_job(name: nil) -> ::Google::Cloud::Run::V2::Job

Pass arguments to `get_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The full name of the Job. Format: projects/{project}/locations/{location}/jobs/{job}, where {project} can be project id or number. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::GetJobRequest.new
    
    # Call the get_job method.
    result = client.get_job request
    
    # The returned object is of type Google::Cloud::Run::V2::Job.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Jobs client object.

**Yields**

  * (config) — Configure the Jobs client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Run::V2::Jobs::Client.new do |config|
      config.timeout = 10.0
    end

### #list_jobs
    
    
    def list_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Run::V2::Job>
    def list_jobs(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Run::V2::Job>

Lists Jobs. Results are sorted by creation time, descending.

**Overloads**
    
    
    def list_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Run::V2::Job>

Pass arguments to `list_jobs` via a request object, either of type [ListJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ListJobsRequest "Google::Cloud::Run::V2::ListJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::ListJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ListJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_jobs(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Run::V2::Job>

Pass arguments to `list_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location and project to list resources on. Format: projects/{project}/locations/{location}, where {project} can be project id or number. 
  * **page_size** (::Integer) — Maximum number of Jobs to return in this call. 
  * **page_token** (::String) — A page token received from a previous call to ListJobs. All other parameters must match. 
  * **show_deleted** (::Boolean) — If true, returns deleted (but unexpired) resources along with active ones. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::ListJobsRequest.new
    
    # Call the list_jobs method.
    result = client.list_jobs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Run::V2::Job.
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
    
    
    def operations_client() -> ::Google::Cloud::Run::V2::Jobs::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Run::V2::Jobs::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Jobs-Operations)) 



### #run_job
    
    
    def run_job(request, options = nil) -> ::Gapic::Operation
    def run_job(name: nil, validate_only: nil, etag: nil, overrides: nil) -> ::Gapic::Operation

Triggers creation of a new Execution of this Job.

**Overloads**
    
    
    def run_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `run_job` via a request object, either of type [RunJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RunJobRequest "Google::Cloud::Run::V2::RunJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::RunJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RunJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def run_job(name: nil, validate_only: nil, etag: nil, overrides: nil) -> ::Gapic::Operation

Pass arguments to `run_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The full name of the Job. Format: projects/{project}/locations/{location}/jobs/{job}, where {project} can be project id or number. 
  * **validate_only** (::Boolean) — Indicates that the request should be validated without actually deleting any resources. 
  * **etag** (::String) — A system-generated fingerprint for this version of the resource. May be used to detect modification conflict during updates. 
  * **overrides** ([::Google::Cloud::Run::V2::RunJobRequest::Overrides](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-RunJobRequest-Overrides), ::Hash) — Overrides specification for a given execution of a job. If provided, overrides will be applied to update the execution or task spec. 



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
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::RunJobRequest.new
    
    # Call the run_job method.
    result = client.run_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the IAM Access control policy for the specified Job. Overwrites any existing policy.

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Returns permissions that a caller has on the specified Project.

There are no permissions required for making this API call.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_job
    
    
    def update_job(request, options = nil) -> ::Gapic::Operation
    def update_job(job: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Updates a Job.

**Overloads**
    
    
    def update_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_job` via a request object, either of type [UpdateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-UpdateJobRequest "Google::Cloud::Run::V2::UpdateJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::UpdateJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-UpdateJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_job(job: nil, validate_only: nil, allow_missing: nil) -> ::Gapic::Operation

Pass arguments to `update_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **job** ([::Google::Cloud::Run::V2::Job](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Job), ::Hash) — Required. The Job to be updated. 
  * **validate_only** (::Boolean) — Indicates that the request should be validated and default values populated, without persisting the request or updating any resources. 
  * **allow_missing** (::Boolean) — Optional. If set to true, and if the Job does not exist, it will create a new one. Caller must have both create and update permissions for this call if this is set to true. 



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
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Jobs::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::UpdateJobRequest.new
    
    # Call the update_job method.
    result = client.update_job request
    
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
