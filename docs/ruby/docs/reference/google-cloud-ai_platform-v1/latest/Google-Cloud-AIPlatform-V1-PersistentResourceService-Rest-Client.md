---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:38.212782+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.

REST client for the PersistentResourceService service.

A service for managing Vertex AI's machine learning PersistentResource.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AIPlatform::V1::PersistentResourceService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the PersistentResourceService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all PersistentResourceService clients
    ::Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the PersistentResourceService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client#Google__Cloud__AIPlatform__V1__PersistentResourceService__Rest__Client_configure_class_ "Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration)) 



### #create_persistent_resource
    
    
    def create_persistent_resource(request, options = nil) -> ::Gapic::Operation
    def create_persistent_resource(parent: nil, persistent_resource: nil, persistent_resource_id: nil) -> ::Gapic::Operation

Creates a PersistentResource.

**Overloads**
    
    
    def create_persistent_resource(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_persistent_resource` via a request object, either of type [CreatePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreatePersistentResourceRequest "Google::Cloud::AIPlatform::V1::CreatePersistentResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreatePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreatePersistentResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_persistent_resource(parent: nil, persistent_resource: nil, persistent_resource_id: nil) -> ::Gapic::Operation

Pass arguments to `create_persistent_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to create the PersistentResource in. Format: `projects/{project}/locations/{location}`
  * **persistent_resource** ([::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource), ::Hash) — Required. The PersistentResource to create. 
  * **persistent_resource_id** (::String) — Required. The ID to use for the PersistentResource, which become the final component of the PersistentResource's resource name.

The maximum length is 63 characters, and valid characters are `/^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$/`. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreatePersistentResourceRequest.new
    
    # Call the create_persistent_resource method.
    result = client.create_persistent_resource request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_persistent_resource
    
    
    def delete_persistent_resource(request, options = nil) -> ::Gapic::Operation
    def delete_persistent_resource(name: nil) -> ::Gapic::Operation

Deletes a PersistentResource.

**Overloads**
    
    
    def delete_persistent_resource(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_persistent_resource` via a request object, either of type [DeletePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeletePersistentResourceRequest "Google::Cloud::AIPlatform::V1::DeletePersistentResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeletePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeletePersistentResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_persistent_resource(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_persistent_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the PersistentResource to be deleted. Format: `projects/{project}/locations/{location}/persistentResources/{persistent_resource}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeletePersistentResourceRequest.new
    
    # Call the delete_persistent_resource method.
    result = client.delete_persistent_resource request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_persistent_resource
    
    
    def get_persistent_resource(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::PersistentResource
    def get_persistent_resource(name: nil) -> ::Google::Cloud::AIPlatform::V1::PersistentResource

Gets a PersistentResource.

**Overloads**
    
    
    def get_persistent_resource(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::PersistentResource

Pass arguments to `get_persistent_resource` via a request object, either of type [GetPersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetPersistentResourceRequest "Google::Cloud::AIPlatform::V1::GetPersistentResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetPersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetPersistentResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_persistent_resource(name: nil) -> ::Google::Cloud::AIPlatform::V1::PersistentResource

Pass arguments to `get_persistent_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetPersistentResourceRequest.new
    
    # Call the get_persistent_resource method.
    result = client.get_persistent_resource request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::PersistentResource.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new PersistentResourceService REST client object.

**Yields**

  * (config) — Configure the PersistentResourceService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_persistent_resources
    
    
    def list_persistent_resources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::PersistentResource>
    def list_persistent_resources(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::PersistentResource>

Lists PersistentResources in a Location.

**Overloads**
    
    
    def list_persistent_resources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::PersistentResource>

Pass arguments to `list_persistent_resources` via a request object, either of type [ListPersistentResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListPersistentResourcesRequest "Google::Cloud::AIPlatform::V1::ListPersistentResourcesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListPersistentResourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListPersistentResourcesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_persistent_resources(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::PersistentResource>

Pass arguments to `list_persistent_resources` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to list the PersistentResources from. Format: `projects/{project}/locations/{location}`
  * **page_size** (::Integer) — Optional. The standard list page size. 
  * **page_token** (::String) — Optional. The standard list page token. Typically obtained via [ListPersistentResourcesResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListPersistentResourcesResponse#Google__Cloud__AIPlatform__V1__ListPersistentResourcesResponse_next_page_token_instance_ "Google::Cloud::AIPlatform::V1::ListPersistentResourcesResponse#next_page_token \(method\)") of the previous [PersistentResourceService.ListPersistentResource][] call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListPersistentResourcesRequest.new
    
    # Call the list_persistent_resources method.
    result = client.list_persistent_resources request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::PersistentResource.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResourceService-Rest-Operations)) 



### #reboot_persistent_resource
    
    
    def reboot_persistent_resource(request, options = nil) -> ::Gapic::Operation
    def reboot_persistent_resource(name: nil) -> ::Gapic::Operation

Reboots a PersistentResource.

**Overloads**
    
    
    def reboot_persistent_resource(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reboot_persistent_resource` via a request object, either of type [RebootPersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RebootPersistentResourceRequest "Google::Cloud::AIPlatform::V1::RebootPersistentResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::RebootPersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-RebootPersistentResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def reboot_persistent_resource(name: nil) -> ::Gapic::Operation

Pass arguments to `reboot_persistent_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the PersistentResource resource. Format: `projects/{project_id_or_number}/locations/{location_id}/persistentResources/{persistent_resource_id}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::RebootPersistentResourceRequest.new
    
    # Call the reboot_persistent_resource method.
    result = client.reboot_persistent_resource request
    
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



### #update_persistent_resource
    
    
    def update_persistent_resource(request, options = nil) -> ::Gapic::Operation
    def update_persistent_resource(persistent_resource: nil, update_mask: nil) -> ::Gapic::Operation

Updates a PersistentResource.

**Overloads**
    
    
    def update_persistent_resource(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_persistent_resource` via a request object, either of type [UpdatePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdatePersistentResourceRequest "Google::Cloud::AIPlatform::V1::UpdatePersistentResourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdatePersistentResourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdatePersistentResourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_persistent_resource(persistent_resource: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_persistent_resource` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **persistent_resource** ([::Google::Cloud::AIPlatform::V1::PersistentResource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-PersistentResource), ::Hash) — Required. The PersistentResource to update.

The PersistentResource's `name` field is used to identify the PersistentResource to update. Format: `projects/{project}/locations/{location}/persistentResources/{persistent_resource}`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Specify the fields to be overwritten in the PersistentResource by the update method. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::PersistentResourceService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdatePersistentResourceRequest.new
    
    # Call the update_persistent_resource method.
    result = client.update_persistent_resource request
    
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
