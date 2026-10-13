---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:21.662855+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.

Client for the AutoscalingPolicyService service.

The API interface for managing autoscaling policies in the Dataproc API.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AutoscalingPolicyService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration "Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AutoscalingPolicyService clients
    ::Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AutoscalingPolicyService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client#Google__Cloud__Dataproc__V1__AutoscalingPolicyService__Client_configure_class_ "Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration "Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration)) 



### #create_autoscaling_policy
    
    
    def create_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy
    def create_autoscaling_policy(parent: nil, policy: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Creates new autoscaling policy.

**Overloads**
    
    
    def create_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `create_autoscaling_policy` via a request object, either of type [CreateAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-CreateAutoscalingPolicyRequest "Google::Cloud::Dataproc::V1::CreateAutoscalingPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::CreateAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-CreateAutoscalingPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_autoscaling_policy(parent: nil, policy: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `create_autoscaling_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The "resource name" of the region or location, as described in https://cloud.google.com/apis/design/resource_names.

    * For `projects.regions.autoscalingPolicies.create`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`

    * For `projects.locations.autoscalingPolicies.create`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  * **policy** ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy), ::Hash) — Required. The autoscaling policy to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::CreateAutoscalingPolicyRequest.new
    
    # Call the create_autoscaling_policy method.
    result = client.create_autoscaling_policy request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::AutoscalingPolicy.
    p result

### #delete_autoscaling_policy
    
    
    def delete_autoscaling_policy(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_autoscaling_policy(name: nil) -> ::Google::Protobuf::Empty

Deletes an autoscaling policy. It is an error to delete an autoscaling policy that is in use by one or more clusters.

**Overloads**
    
    
    def delete_autoscaling_policy(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_autoscaling_policy` via a request object, either of type [DeleteAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DeleteAutoscalingPolicyRequest "Google::Cloud::Dataproc::V1::DeleteAutoscalingPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::DeleteAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DeleteAutoscalingPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_autoscaling_policy(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_autoscaling_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names.

    * For `projects.regions.autoscalingPolicies.delete`, the resource name of the policy has the following format: `projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}`

    * For `projects.locations.autoscalingPolicies.delete`, the resource name of the policy has the following format: `projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::DeleteAutoscalingPolicyRequest.new
    
    # Call the delete_autoscaling_policy method.
    result = client.delete_autoscaling_policy request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_autoscaling_policy
    
    
    def get_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy
    def get_autoscaling_policy(name: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Retrieves autoscaling policy.

**Overloads**
    
    
    def get_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `get_autoscaling_policy` via a request object, either of type [GetAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-GetAutoscalingPolicyRequest "Google::Cloud::Dataproc::V1::GetAutoscalingPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::GetAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-GetAutoscalingPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_autoscaling_policy(name: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `get_autoscaling_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The "resource name" of the autoscaling policy, as described in https://cloud.google.com/apis/design/resource_names.

    * For `projects.regions.autoscalingPolicies.get`, the resource name of the policy has the following format: `projects/{project_id}/regions/{region}/autoscalingPolicies/{policy_id}`

    * For `projects.locations.autoscalingPolicies.get`, the resource name of the policy has the following format: `projects/{project_id}/locations/{location}/autoscalingPolicies/{policy_id}`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::GetAutoscalingPolicyRequest.new
    
    # Call the get_autoscaling_policy method.
    result = client.get_autoscaling_policy request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::AutoscalingPolicy.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AutoscalingPolicyService client object.

**Yields**

  * (config) — Configure the AutoscalingPolicyService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicyService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_autoscaling_policies
    
    
    def list_autoscaling_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::AutoscalingPolicy>
    def list_autoscaling_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::AutoscalingPolicy>

Lists autoscaling policies in the project.

**Overloads**
    
    
    def list_autoscaling_policies(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::AutoscalingPolicy>

Pass arguments to `list_autoscaling_policies` via a request object, either of type [ListAutoscalingPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListAutoscalingPoliciesRequest "Google::Cloud::Dataproc::V1::ListAutoscalingPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::ListAutoscalingPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListAutoscalingPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_autoscaling_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::AutoscalingPolicy>

Pass arguments to `list_autoscaling_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — 

Required. The "resource name" of the region or location, as described in https://cloud.google.com/apis/design/resource_names.

    * For `projects.regions.autoscalingPolicies.list`, the resource name of the region has the following format: `projects/{project_id}/regions/{region}`

    * For `projects.locations.autoscalingPolicies.list`, the resource name of the location has the following format: `projects/{project_id}/locations/{location}`

  * **page_size** (::Integer) — Optional. The maximum number of results to return in each response. Must be less than or equal to 1000. Defaults to 100. 
  * **page_token** (::String) — Optional. The page token, returned by a previous call, to request the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::ListAutoscalingPoliciesRequest.new
    
    # Call the list_autoscaling_policies method.
    result = client.list_autoscaling_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataproc::V1::AutoscalingPolicy.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_autoscaling_policy
    
    
    def update_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy
    def update_autoscaling_policy(policy: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Updates (replaces) autoscaling policy.

Disabled check for update_mask, because all updates will be full replacements.

**Overloads**
    
    
    def update_autoscaling_policy(request, options = nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `update_autoscaling_policy` via a request object, either of type [UpdateAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UpdateAutoscalingPolicyRequest "Google::Cloud::Dataproc::V1::UpdateAutoscalingPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::UpdateAutoscalingPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UpdateAutoscalingPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_autoscaling_policy(policy: nil) -> ::Google::Cloud::Dataproc::V1::AutoscalingPolicy

Pass arguments to `update_autoscaling_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **policy** ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy), ::Hash) — Required. The updated autoscaling policy. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::AutoscalingPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-AutoscalingPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::AutoscalingPolicyService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::UpdateAutoscalingPolicyRequest.new
    
    # Call the update_autoscaling_policy method.
    result = client.update_autoscaling_policy request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::AutoscalingPolicy.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
