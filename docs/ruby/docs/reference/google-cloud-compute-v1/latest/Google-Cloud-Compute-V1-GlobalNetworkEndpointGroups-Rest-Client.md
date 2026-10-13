---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:50.058158+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.

REST client for the GlobalNetworkEndpointGroups service.

The GlobalNetworkEndpointGroups API.

This client uses GlobalNetworkEndpointGroups version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the GlobalNetworkEndpointGroups Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration "Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all GlobalNetworkEndpointGroups clients
    ::Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #attach_network_endpoints
    
    
    def attach_network_endpoints(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def attach_network_endpoints(global_network_endpoint_groups_attach_endpoints_request_resource: nil, network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Attach a network endpoint to the specified network endpoint group.

**Overloads**
    
    
    def attach_network_endpoints(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `attach_network_endpoints` via a request object, either of type [AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest "Google::Cloud::Compute::V1::AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def attach_network_endpoints(global_network_endpoint_groups_attach_endpoints_request_resource: nil, network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `attach_network_endpoints` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **global_network_endpoint_groups_attach_endpoints_request_resource** ([::Google::Cloud::Compute::V1::GlobalNetworkEndpointGroupsAttachEndpointsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroupsAttachEndpointsRequest), ::Hash) — The body resource for this request 
  * **network_endpoint_group** (::String) — The name of the network endpoint group where you are attaching network endpoints to. It should comply with RFC1035. 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::GenericLRO::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::GenericLRO::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::AttachNetworkEndpointsGlobalNetworkEndpointGroupRequest.new
    
    # Call the attach_network_endpoints method.
    result = client.attach_network_endpoints request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the GlobalNetworkEndpointGroups Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client#Google__Cloud__Compute__V1__GlobalNetworkEndpointGroups__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration "Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration)) 



### #delete
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def delete(network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Deletes the specified network endpoint group.Note that the NEG cannot be deleted if there are backend services referencing it.

**Overloads**
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via a request object, either of type [DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteGlobalNetworkEndpointGroupRequest "Google::Cloud::Compute::V1::DeleteGlobalNetworkEndpointGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::DeleteGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteGlobalNetworkEndpointGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete(network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **network_endpoint_group** (::String) — The name of the network endpoint group to delete. It should comply with RFC1035. 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::GenericLRO::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::GenericLRO::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::DeleteGlobalNetworkEndpointGroupRequest.new
    
    # Call the delete method.
    result = client.delete request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #detach_network_endpoints
    
    
    def detach_network_endpoints(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def detach_network_endpoints(global_network_endpoint_groups_detach_endpoints_request_resource: nil, network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Detach the network endpoint from the specified network endpoint group.

**Overloads**
    
    
    def detach_network_endpoints(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `detach_network_endpoints` via a request object, either of type [DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest "Google::Cloud::Compute::V1::DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def detach_network_endpoints(global_network_endpoint_groups_detach_endpoints_request_resource: nil, network_endpoint_group: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `detach_network_endpoints` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **global_network_endpoint_groups_detach_endpoints_request_resource** ([::Google::Cloud::Compute::V1::GlobalNetworkEndpointGroupsDetachEndpointsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroupsDetachEndpointsRequest), ::Hash) — The body resource for this request 
  * **network_endpoint_group** (::String) — The name of the network endpoint group where you are removing network endpoints. It should comply with RFC1035. 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::GenericLRO::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::GenericLRO::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::DetachNetworkEndpointsGlobalNetworkEndpointGroupRequest.new
    
    # Call the detach_network_endpoints method.
    result = client.detach_network_endpoints request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroup
    def get(network_endpoint_group: nil, project: nil) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroup

Returns the specified network endpoint group.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroup

Pass arguments to `get` via a request object, either of type [Google::Cloud::Compute::V1::GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetGlobalNetworkEndpointGroupRequest "Google::Cloud::Compute::V1::GetGlobalNetworkEndpointGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetGlobalNetworkEndpointGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(network_endpoint_group: nil, project: nil) -> ::Google::Cloud::Compute::V1::NetworkEndpointGroup

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **network_endpoint_group** (::String) — The name of the network endpoint group. It should comply with RFC1035. 
  * **project** (::String) — Project ID for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::NetworkEndpointGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::NetworkEndpointGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetGlobalNetworkEndpointGroupRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::NetworkEndpointGroup.
    p result

### #global_operations
    
    
    def global_operations() -> ::Google::Cloud::Compute::V1::GlobalOperations::Rest::Client

Get the associated client for long-running operations via GlobalOperations.

**Returns**

  * ([::Google::Cloud::Compute::V1::GlobalOperations::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalOperations-Rest-Client)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new GlobalNetworkEndpointGroups REST client object.

**Yields**

  * (config) — Configure the GlobalNetworkEndpointGroups client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GlobalNetworkEndpointGroups-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #insert
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def insert(network_endpoint_group_resource: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Creates a network endpoint group in the specified project using the parameters that are included in the request.

Note: Use the following APIs to manage network endpoint groups:

\- To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): zonal API \- To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): regional API \- To manage NEGs with global scope (such as global internet NEGs):global API

**Overloads**
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via a request object, either of type [InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertGlobalNetworkEndpointGroupRequest "Google::Cloud::Compute::V1::InsertGlobalNetworkEndpointGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::InsertGlobalNetworkEndpointGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertGlobalNetworkEndpointGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def insert(network_endpoint_group_resource: nil, project: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **network_endpoint_group_resource** ([::Google::Cloud::Compute::V1::NetworkEndpointGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::GenericLRO::Operation) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::GenericLRO::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::InsertGlobalNetworkEndpointGroupRequest.new
    
    # Call the insert method.
    result = client.insert request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #list
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointGroup>
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointGroup>

Retrieves the list of network endpoint groups that are located in the specified project.

**Overloads**
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointGroup>

Pass arguments to `list` via a request object, either of type [ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListGlobalNetworkEndpointGroupsRequest "Google::Cloud::Compute::V1::ListGlobalNetworkEndpointGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListGlobalNetworkEndpointGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointGroup>

Pass arguments to `list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **filter** (::String) — A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160. These two types of filter expressions cannot be mixed in one request.

If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.

For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.

The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use: ` labels.owner:* `

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based onresource labels.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake") ` By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true) `

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:

`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`

The literal value is interpreted as a regular expression using GoogleRE2 library syntax. The literal value must match the entire field.

For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.

You cannot combine constraints on multiple fields using regular expressions. 

  * **max_results** (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 
  * **order_by** (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 

  * **page_token** (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 
  * **project** (::String) — Project ID for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::NetworkEndpointGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::NetworkEndpointGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointGroup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListGlobalNetworkEndpointGroupsRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Compute::V1::NetworkEndpointGroupList.
    p result

### #list_network_endpoints
    
    
    def list_network_endpoints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus>
    def list_network_endpoints(filter: nil, max_results: nil, network_endpoint_group: nil, order_by: nil, page_token: nil, project: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus>

Lists the network endpoints in the specified network endpoint group.

**Overloads**
    
    
    def list_network_endpoints(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus>

Pass arguments to `list_network_endpoints` via a request object, either of type [ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest "Google::Cloud::Compute::V1::ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_network_endpoints(filter: nil, max_results: nil, network_endpoint_group: nil, order_by: nil, page_token: nil, project: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus>

Pass arguments to `list_network_endpoints` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **filter** (::String) — A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal AIP-160. These two types of filter expressions cannot be mixed in one request.

If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.

For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.

The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use: ` labels.owner:* `

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based onresource labels.

To filter on multiple expressions, provide each separate expression within parentheses. For example: ` (scheduling.automaticRestart = true) (cpuPlatform = "Intel Skylake") ` By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example: ` (cpuPlatform = "Intel Skylake") OR (cpuPlatform = "Intel Broadwell") AND (scheduling.automaticRestart = true) `

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:

`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`

The literal value is interpreted as a regular expression using GoogleRE2 library syntax. The literal value must match the entire field.

For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.

You cannot combine constraints on multiple fields using regular expressions. 

  * **max_results** (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 
  * **network_endpoint_group** (::String) — The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035. 
  * **order_by** (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 

  * **page_token** (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 
  * **project** (::String) — Project ID for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointWithHealthStatus)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::NetworkEndpointWithHealthStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-NetworkEndpointWithHealthStatus)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::GlobalNetworkEndpointGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListNetworkEndpointsGlobalNetworkEndpointGroupsRequest.new
    
    # Call the list_network_endpoints method.
    result = client.list_network_endpoints request
    
    # The returned object is of type Google::Cloud::Compute::V1::NetworkEndpointGroupsListNetworkEndpoints.
    p result

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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
