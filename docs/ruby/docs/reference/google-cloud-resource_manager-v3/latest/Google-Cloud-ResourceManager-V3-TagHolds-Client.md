---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client/
title: Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagHolds::Client (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:32.440417+00:00
---

# Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagHolds::Client (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Resource Manager V3 API - Class Google::Cloud::ResourceManager::V3::TagHolds::Client (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.9.0  0.8.2  0.7.0  0.6.2  0.5.1  0.4.0  0.3.0  0.2.0  0.1.3 

Reference documentation and code samples for the Resource Manager V3 API class Google::Cloud::ResourceManager::V3::TagHolds::Client.

Client for the TagHolds service.

Allow users to create and manage TagHolds for TagValues. TagHolds represent the use of a Tag Value that is not captured by TagBindings but should still block TagValue deletion (such as a reference in a policy condition). This service provides isolated failure domains by cloud location so that TagHolds can be managed in the same location as their usage.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ResourceManager::V3::TagHolds::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the TagHolds Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration "Google::Cloud::ResourceManager::V3::TagHolds::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all TagHolds clients
    ::Google::Cloud::ResourceManager::V3::TagHolds::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the TagHolds Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client#Google__Cloud__ResourceManager__V3__TagHolds__Client_configure_class_ "Google::Cloud::ResourceManager::V3::TagHolds::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration "Google::Cloud::ResourceManager::V3::TagHolds::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration)) 



### #create_tag_hold
    
    
    def create_tag_hold(request, options = nil) -> ::Gapic::Operation
    def create_tag_hold(parent: nil, tag_hold: nil, validate_only: nil) -> ::Gapic::Operation

Creates a TagHold. Returns ALREADY_EXISTS if a TagHold with the same resource and origin exists under the same TagValue.

**Overloads**
    
    
    def create_tag_hold(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_tag_hold` via a request object, either of type [CreateTagHoldRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-CreateTagHoldRequest "Google::Cloud::ResourceManager::V3::CreateTagHoldRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ResourceManager::V3::CreateTagHoldRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-CreateTagHoldRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_tag_hold(parent: nil, tag_hold: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_tag_hold` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the TagHold's parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 
  * **tag_hold** ([::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold), ::Hash) — Required. The TagHold to be created. 
  * **validate_only** (::Boolean) — Optional. Set to true to perform the validations necessary for creating the resource, but not actually perform the action. 



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
    
    
    require "google/cloud/resource_manager/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ResourceManager::V3::TagHolds::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ResourceManager::V3::CreateTagHoldRequest.new
    
    # Call the create_tag_hold method.
    result = client.create_tag_hold request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_tag_hold
    
    
    def delete_tag_hold(request, options = nil) -> ::Gapic::Operation
    def delete_tag_hold(name: nil, validate_only: nil) -> ::Gapic::Operation

Deletes a TagHold.

**Overloads**
    
    
    def delete_tag_hold(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_tag_hold` via a request object, either of type [DeleteTagHoldRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-DeleteTagHoldRequest "Google::Cloud::ResourceManager::V3::DeleteTagHoldRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ResourceManager::V3::DeleteTagHoldRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-DeleteTagHoldRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_tag_hold(name: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `delete_tag_hold` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the TagHold to delete. Must be of the form: `tagValues/{tag-value-id}/tagHolds/{tag-hold-id}`. 
  * **validate_only** (::Boolean) — Optional. Set to true to perform the validations necessary for deleting the resource, but not actually perform the action. 



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
    
    
    require "google/cloud/resource_manager/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ResourceManager::V3::TagHolds::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ResourceManager::V3::DeleteTagHoldRequest.new
    
    # Call the delete_tag_hold method.
    result = client.delete_tag_hold request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new TagHolds client object.

**Yields**

  * (config) — Configure the TagHolds client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ResourceManager::V3::TagHolds::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ResourceManager::V3::TagHolds::Client.new do |config|
      config.timeout = 10.0
    end

### #list_tag_holds
    
    
    def list_tag_holds(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ResourceManager::V3::TagHold>
    def list_tag_holds(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ResourceManager::V3::TagHold>

Lists TagHolds under a TagValue.

**Overloads**
    
    
    def list_tag_holds(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ResourceManager::V3::TagHold>

Pass arguments to `list_tag_holds` via a request object, either of type [ListTagHoldsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-ListTagHoldsRequest "Google::Cloud::ResourceManager::V3::ListTagHoldsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ResourceManager::V3::ListTagHoldsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-ListTagHoldsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_tag_holds(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ResourceManager::V3::TagHold>

Pass arguments to `list_tag_holds` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the parent TagValue. Must be of the form: `tagValues/{tag-value-id}`. 
  * **page_size** (::Integer) — Optional. The maximum number of TagHolds to return in the response. The server allows a maximum of 300 TagHolds to return. If unspecified, the server will use 100 as the default. 
  * **page_token** (::String) — Optional. A pagination token returned from a previous call to `ListTagHolds` that indicates where this listing should continue from. 
  * **filter** (::String) — 

Optional. Criteria used to select a subset of TagHolds parented by the TagValue to return. This field follows the syntax defined by aip.dev/160; the `holder` and `origin` fields are supported for filtering. Currently only `AND` syntax is supported. Some example queries are:

    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group`
    * `origin = 35678234`
    * `holder = //compute.googleapis.com/compute/projects/myproject/regions/us-east-1/instanceGroupManagers/instance-group AND origin = 35678234`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ResourceManager::V3::TagHold](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHold)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/resource_manager/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ResourceManager::V3::TagHolds::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ResourceManager::V3::ListTagHoldsRequest.new
    
    # Call the list_tag_holds method.
    result = client.list_tag_holds request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ResourceManager::V3::TagHold.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::ResourceManager::V3::TagHolds::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::ResourceManager::V3::TagHolds::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-resource_manager-v3/latest/Google-Cloud-ResourceManager-V3-TagHolds-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
