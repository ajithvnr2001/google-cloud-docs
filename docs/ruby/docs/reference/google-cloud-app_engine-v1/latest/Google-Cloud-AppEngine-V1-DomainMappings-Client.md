---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMappings::Client (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:20.304160+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMappings::Client (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::DomainMappings::Client (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::DomainMappings::Client.

Client for the DomainMappings service.

Manages domains serving an application.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DomainMappings Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration "Google::Cloud::AppEngine::V1::DomainMappings::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DomainMappings clients
    ::Google::Cloud::AppEngine::V1::DomainMappings::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DomainMappings Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client#Google__Cloud__AppEngine__V1__DomainMappings__Client_configure_class_ "Google::Cloud::AppEngine::V1::DomainMappings::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration "Google::Cloud::AppEngine::V1::DomainMappings::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration)) 



### #create_domain_mapping
    
    
    def create_domain_mapping(request, options = nil) -> ::Gapic::Operation
    def create_domain_mapping(parent: nil, domain_mapping: nil, override_strategy: nil) -> ::Gapic::Operation

Maps a domain to an application. A user must be authorized to administer a domain in order to map it to an application. For a list of available authorized domains, see [`AuthorizedDomains.ListAuthorizedDomains`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client/).

**Overloads**
    
    
    def create_domain_mapping(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_domain_mapping` via a request object, either of type [CreateDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateDomainMappingRequest "Google::Cloud::AppEngine::V1::CreateDomainMappingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::CreateDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateDomainMappingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_domain_mapping(parent: nil, domain_mapping: nil, override_strategy: nil) -> ::Gapic::Operation

Pass arguments to `create_domain_mapping` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Name of the parent Application resource. Example: `apps/myapp`. 
  * **domain_mapping** ([::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping), ::Hash) — Domain mapping configuration. 
  * **override_strategy** ([::Google::Cloud::AppEngine::V1::DomainOverrideStrategy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainOverrideStrategy)) — Whether the domain creation should override any existing mappings for this domain. By default, overrides are rejected. 



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
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::CreateDomainMappingRequest.new
    
    # Call the create_domain_mapping method.
    result = client.create_domain_mapping request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_domain_mapping
    
    
    def delete_domain_mapping(request, options = nil) -> ::Gapic::Operation
    def delete_domain_mapping(name: nil) -> ::Gapic::Operation

Deletes the specified domain mapping. A user must be authorized to administer the associated domain in order to delete a `DomainMapping` resource.

**Overloads**
    
    
    def delete_domain_mapping(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_domain_mapping` via a request object, either of type [Google::Cloud::AppEngine::V1::DeleteDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteDomainMappingRequest "Google::Cloud::AppEngine::V1::DeleteDomainMappingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::DeleteDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteDomainMappingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_domain_mapping(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_domain_mapping` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the resource to delete. Example: `apps/myapp/domainMappings/example.com`. 



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
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::DeleteDomainMappingRequest.new
    
    # Call the delete_domain_mapping method.
    result = client.delete_domain_mapping request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_domain_mapping
    
    
    def get_domain_mapping(request, options = nil) -> ::Google::Cloud::AppEngine::V1::DomainMapping
    def get_domain_mapping(name: nil) -> ::Google::Cloud::AppEngine::V1::DomainMapping

Gets the specified domain mapping.

**Overloads**
    
    
    def get_domain_mapping(request, options = nil) -> ::Google::Cloud::AppEngine::V1::DomainMapping

Pass arguments to `get_domain_mapping` via a request object, either of type [GetDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetDomainMappingRequest "Google::Cloud::AppEngine::V1::GetDomainMappingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::GetDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetDomainMappingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_domain_mapping(name: nil) -> ::Google::Cloud::AppEngine::V1::DomainMapping

Pass arguments to `get_domain_mapping` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the resource requested. Example: `apps/myapp/domainMappings/example.com`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::GetDomainMappingRequest.new
    
    # Call the get_domain_mapping method.
    result = client.get_domain_mapping request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::DomainMapping.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DomainMappings client object.

**Yields**

  * (config) — Configure the DomainMappings client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AppEngine::V1::DomainMappings::Client.new do |config|
      config.timeout = 10.0
    end

### #list_domain_mappings
    
    
    def list_domain_mappings(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::DomainMapping>
    def list_domain_mappings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::DomainMapping>

Lists the domain mappings on an application.

**Overloads**
    
    
    def list_domain_mappings(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::DomainMapping>

Pass arguments to `list_domain_mappings` via a request object, either of type [ListDomainMappingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListDomainMappingsRequest "Google::Cloud::AppEngine::V1::ListDomainMappingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::ListDomainMappingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListDomainMappingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_domain_mappings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::AppEngine::V1::DomainMapping>

Pass arguments to `list_domain_mappings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Name of the parent Application resource. Example: `apps/myapp`. 
  * **page_size** (::Integer) — Maximum results to return per page. 
  * **page_token** (::String) — Continuation token for fetching the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::ListDomainMappingsRequest.new
    
    # Call the list_domain_mappings method.
    result = client.list_domain_mappings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AppEngine::V1::DomainMapping.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AppEngine::V1::DomainMappings::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AppEngine::V1::DomainMappings::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMappings-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_domain_mapping
    
    
    def update_domain_mapping(request, options = nil) -> ::Gapic::Operation
    def update_domain_mapping(name: nil, domain_mapping: nil, update_mask: nil) -> ::Gapic::Operation

Updates the specified domain mapping. To map an SSL certificate to a domain mapping, update `certificate_id` to point to an `AuthorizedCertificate` resource. A user must be authorized to administer the associated domain in order to update a `DomainMapping` resource.

**Overloads**
    
    
    def update_domain_mapping(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_domain_mapping` via a request object, either of type [UpdateDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateDomainMappingRequest "Google::Cloud::AppEngine::V1::UpdateDomainMappingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::UpdateDomainMappingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateDomainMappingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_domain_mapping(name: nil, domain_mapping: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_domain_mapping` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the resource to update. Example: `apps/myapp/domainMappings/example.com`. 
  * **domain_mapping** ([::Google::Cloud::AppEngine::V1::DomainMapping](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DomainMapping), ::Hash) — A domain mapping containing the updated resource. Only fields set in the field mask will be updated. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Standard field mask for the set of fields to be updated. 



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
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::DomainMappings::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::UpdateDomainMappingRequest.new
    
    # Call the update_domain_mapping method.
    result = client.update_domain_mapping request
    
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
