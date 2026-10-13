---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:34.238661+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.

REST client for the ControlService service.

Service for performing CRUD operations on Controls. Controls allow for custom logic to be implemented in the serving path. Controls need to be attached to a Serving Config to be considered during a request.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1beta::ControlService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ControlService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ControlService clients
    ::Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ControlService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client#Google__Cloud__DiscoveryEngine__V1beta__ControlService__Rest__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration)) 



### #create_control
    
    
    def create_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control
    def create_control(parent: nil, control: nil, control_id: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Creates a Control.

By default 1000 controls are allowed for a data store. A request can be submitted to adjust this limit. If the [Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control "Google::Cloud::DiscoveryEngine::V1beta::Control \(class\)") to create already exists, an ALREADY_EXISTS error is returned.

**Overloads**
    
    
    def create_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `create_control` via a request object, either of type [Google::Cloud::DiscoveryEngine::V1beta::CreateControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CreateControlRequest "Google::Cloud::DiscoveryEngine::V1beta::CreateControlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::CreateControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CreateControlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_control(parent: nil, control: nil, control_id: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `create_control` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Full resource name of parent data store. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. 
  * **control** ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control), ::Hash) — Required. The Control to create. 
  * **control_id** (::String) — Required. The ID to use for the Control, which will become the final component of the Control's resource name.

This value must be within 1-63 characters. Valid characters are /[a-z][0-9]-_/. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::CreateControlRequest.new
    
    # Call the create_control method.
    result = client.create_control request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::Control.
    p result

### #delete_control
    
    
    def delete_control(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_control(name: nil) -> ::Google::Protobuf::Empty

Deletes a Control.

If the [Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control "Google::Cloud::DiscoveryEngine::V1beta::Control \(class\)") to delete does not exist, a NOT_FOUND error is returned.

**Overloads**
    
    
    def delete_control(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_control` via a request object, either of type [DeleteControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DeleteControlRequest "Google::Cloud::DiscoveryEngine::V1beta::DeleteControlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::DeleteControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DeleteControlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_control(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_control` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Control to delete. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::DeleteControlRequest.new
    
    # Call the delete_control method.
    result = client.delete_control request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_control
    
    
    def get_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control
    def get_control(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Gets a Control.

**Overloads**
    
    
    def get_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `get_control` via a request object, either of type [GetControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetControlRequest "Google::Cloud::DiscoveryEngine::V1beta::GetControlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::GetControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetControlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_control(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `get_control` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the Control to get. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}/controls/{control_id}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::GetControlRequest.new
    
    # Call the get_control method.
    result = client.get_control request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::Control.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ControlService REST client object.

**Yields**

  * (config) — Configure the ControlService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ControlService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_controls
    
    
    def list_controls(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::Control>
    def list_controls(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::Control>

Lists all Controls by their parent [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DataStore "Google::Cloud::DiscoveryEngine::V1beta::DataStore \(class\)").

**Overloads**
    
    
    def list_controls(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::Control>

Pass arguments to `list_controls` via a request object, either of type [ListControlsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest "Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_controls(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::Control>

Pass arguments to `list_controls` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The data store resource name. Format: `projects/{project}/locations/{location}/collections/{collection_id}/dataStores/{data_store_id}` or `projects/{project}/locations/{location}/collections/{collection_id}/engines/{engine_id}`. 
  * **page_size** (::Integer) — Optional. Maximum number of results to return. If unspecified, defaults to 50. Max allowed value is 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListControls` call. Provide this to retrieve the subsequent page. 
  * **filter** (::String) — 

Optional. A filter to apply on the list results. Supported features:

    * List all the products under the parent branch if [filter](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListControlsRequest#Google__Cloud__DiscoveryEngine__V1beta__ListControlsRequest_filter_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest#filter \(method\)") is unset. Currently this field is unsupported.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::ListControlsRequest.new
    
    # Call the list_controls method.
    result = client.list_controls request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DiscoveryEngine::V1beta::Control.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_control
    
    
    def update_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control
    def update_control(control: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Updates a Control.

[Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control "Google::Cloud::DiscoveryEngine::V1beta::Control \(class\)") action type cannot be changed. If the [Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control "Google::Cloud::DiscoveryEngine::V1beta::Control \(class\)") to update does not exist, a NOT_FOUND error is returned.

**Overloads**
    
    
    def update_control(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `update_control` via a request object, either of type [UpdateControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateControlRequest "Google::Cloud::DiscoveryEngine::V1beta::UpdateControlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::UpdateControlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateControlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_control(control: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::Control

Pass arguments to `update_control` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **control** ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control), ::Hash) — Required. The Control to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Indicates which fields in the provided [Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control "Google::Cloud::DiscoveryEngine::V1beta::Control \(class\)") to update. The following are NOT supported:

    * [Control.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control#Google__Cloud__DiscoveryEngine__V1beta__Control_name_instance_ "Google::Cloud::DiscoveryEngine::V1beta::Control#name \(method\)")
    * [Control.solution_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control#Google__Cloud__DiscoveryEngine__V1beta__Control_solution_type_instance_ "Google::Cloud::DiscoveryEngine::V1beta::Control#solution_type \(method\)")

If not set or empty, all supported fields are updated. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::Control](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-Control)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::ControlService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::UpdateControlRequest.new
    
    # Call the update_control method.
    result = client.update_control request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::Control.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
