---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client/
title: Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::HubService::Client (v1.15.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:56:05.846057+00:00
---

# Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::HubService::Client (v1.15.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Network Connectivity V1 API - Class Google::Cloud::NetworkConnectivity::V1::HubService::Client (v1.15.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.15.0 (latest)  1.14.0  1.13.0  1.12.0  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Network Connectivity V1 API class Google::Cloud::NetworkConnectivity::V1::HubService::Client.

Client for the HubService service.

Network Connectivity Center is a hub-and-spoke abstraction for network connectivity management in Google Cloud. It reduces operational complexity through a simple, centralized connectivity management model.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::NetworkConnectivity::V1::HubService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the HubService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration "Google::Cloud::NetworkConnectivity::V1::HubService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all HubService clients
    ::Google::Cloud::NetworkConnectivity::V1::HubService::Client.configure do |config|
      config.timeout = 10.0
    end

### #accept_hub_spoke
    
    
    def accept_hub_spoke(request, options = nil) -> ::Gapic::Operation
    def accept_hub_spoke(name: nil, spoke_uri: nil, request_id: nil) -> ::Gapic::Operation

Accepts a proposal to attach a Network Connectivity Center spoke to a hub.

**Overloads**
    
    
    def accept_hub_spoke(request, options = nil) -> ::Gapic::Operation

Pass arguments to `accept_hub_spoke` via a request object, either of type [AcceptHubSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-AcceptHubSpokeRequest "Google::Cloud::NetworkConnectivity::V1::AcceptHubSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::AcceptHubSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-AcceptHubSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def accept_hub_spoke(name: nil, spoke_uri: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `accept_hub_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub into which to accept the spoke. 
  * **spoke_uri** (::String) — Required. The URI of the spoke to accept into the hub. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::AcceptHubSpokeRequest.new
    
    # Call the accept_hub_spoke method.
    result = client.accept_hub_spoke request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #accept_spoke_update
    
    
    def accept_spoke_update(request, options = nil) -> ::Gapic::Operation
    def accept_spoke_update(name: nil, spoke_uri: nil, spoke_etag: nil, request_id: nil) -> ::Gapic::Operation

Accepts a proposal to update a Network Connectivity Center spoke in a hub.

**Overloads**
    
    
    def accept_spoke_update(request, options = nil) -> ::Gapic::Operation

Pass arguments to `accept_spoke_update` via a request object, either of type [AcceptSpokeUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-AcceptSpokeUpdateRequest "Google::Cloud::NetworkConnectivity::V1::AcceptSpokeUpdateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::AcceptSpokeUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-AcceptSpokeUpdateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def accept_spoke_update(name: nil, spoke_uri: nil, spoke_etag: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `accept_spoke_update` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub to accept spoke update. 
  * **spoke_uri** (::String) — Required. The URI of the spoke to accept update. 
  * **spoke_etag** (::String) — Required. The etag of the spoke to accept update. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::AcceptSpokeUpdateRequest.new
    
    # Call the accept_spoke_update method.
    result = client.accept_spoke_update request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the HubService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client#Google__Cloud__NetworkConnectivity__V1__HubService__Client_configure_class_ "Google::Cloud::NetworkConnectivity::V1::HubService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration "Google::Cloud::NetworkConnectivity::V1::HubService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration)) 



### #create_hub
    
    
    def create_hub(request, options = nil) -> ::Gapic::Operation
    def create_hub(parent: nil, hub_id: nil, hub: nil, request_id: nil) -> ::Gapic::Operation

Creates a new Network Connectivity Center hub in the specified project.

**Overloads**
    
    
    def create_hub(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_hub` via a request object, either of type [CreateHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CreateHubRequest "Google::Cloud::NetworkConnectivity::V1::CreateHubRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::CreateHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CreateHubRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_hub(parent: nil, hub_id: nil, hub: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_hub` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource. 
  * **hub_id** (::String) — Required. A unique identifier for the hub. 
  * **hub** ([::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub), ::Hash) — Required. The initial values for a new hub. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::CreateHubRequest.new
    
    # Call the create_hub method.
    result = client.create_hub request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_spoke
    
    
    def create_spoke(request, options = nil) -> ::Gapic::Operation
    def create_spoke(parent: nil, spoke_id: nil, spoke: nil, request_id: nil) -> ::Gapic::Operation

Creates a Network Connectivity Center spoke.

**Overloads**
    
    
    def create_spoke(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_spoke` via a request object, either of type [CreateSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CreateSpokeRequest "Google::Cloud::NetworkConnectivity::V1::CreateSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::CreateSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-CreateSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_spoke(parent: nil, spoke_id: nil, spoke: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource. 
  * **spoke_id** (::String) — Required. Unique id for the spoke to create. 
  * **spoke** ([::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke), ::Hash) — Required. The initial values for a new spoke. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::CreateSpokeRequest.new
    
    # Call the create_spoke method.
    result = client.create_spoke request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_hub
    
    
    def delete_hub(request, options = nil) -> ::Gapic::Operation
    def delete_hub(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a Network Connectivity Center hub.

**Overloads**
    
    
    def delete_hub(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_hub` via a request object, either of type [DeleteHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-DeleteHubRequest "Google::Cloud::NetworkConnectivity::V1::DeleteHubRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::DeleteHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-DeleteHubRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_hub(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_hub` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub to delete. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::DeleteHubRequest.new
    
    # Call the delete_hub method.
    result = client.delete_hub request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_spoke
    
    
    def delete_spoke(request, options = nil) -> ::Gapic::Operation
    def delete_spoke(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a Network Connectivity Center spoke.

**Overloads**
    
    
    def delete_spoke(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_spoke` via a request object, either of type [DeleteSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-DeleteSpokeRequest "Google::Cloud::NetworkConnectivity::V1::DeleteSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::DeleteSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-DeleteSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_spoke(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the spoke to delete. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::DeleteSpokeRequest.new
    
    # Call the delete_spoke method.
    result = client.delete_spoke request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_group
    
    
    def get_group(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Group
    def get_group(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Group

Gets details about a Network Connectivity Center group.

**Overloads**
    
    
    def get_group(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Group

Pass arguments to `get_group` via a request object, either of type [GetGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetGroupRequest "Google::Cloud::NetworkConnectivity::V1::GetGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::GetGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_group(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Group

Pass arguments to `get_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the route table resource. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::GetGroupRequest.new
    
    # Call the get_group method.
    result = client.get_group request
    
    # The returned object is of type Google::Cloud::NetworkConnectivity::V1::Group.
    p result

### #get_hub
    
    
    def get_hub(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Hub
    def get_hub(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Hub

Gets details about a Network Connectivity Center hub.

**Overloads**
    
    
    def get_hub(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Hub

Pass arguments to `get_hub` via a request object, either of type [GetHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetHubRequest "Google::Cloud::NetworkConnectivity::V1::GetHubRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::GetHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetHubRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_hub(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Hub

Pass arguments to `get_hub` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the hub resource to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::GetHubRequest.new
    
    # Call the get_hub method.
    result = client.get_hub request
    
    # The returned object is of type Google::Cloud::NetworkConnectivity::V1::Hub.
    p result

### #get_route
    
    
    def get_route(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Route
    def get_route(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Route

Gets details about the specified route.

**Overloads**
    
    
    def get_route(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Route

Pass arguments to `get_route` via a request object, either of type [GetRouteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetRouteRequest "Google::Cloud::NetworkConnectivity::V1::GetRouteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::GetRouteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetRouteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_route(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Route

Pass arguments to `get_route` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the route resource. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkConnectivity::V1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Route)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Route)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::GetRouteRequest.new
    
    # Call the get_route method.
    result = client.get_route request
    
    # The returned object is of type Google::Cloud::NetworkConnectivity::V1::Route.
    p result

### #get_route_table
    
    
    def get_route_table(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::RouteTable
    def get_route_table(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::RouteTable

Gets details about a Network Connectivity Center route table.

**Overloads**
    
    
    def get_route_table(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::RouteTable

Pass arguments to `get_route_table` via a request object, either of type [GetRouteTableRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetRouteTableRequest "Google::Cloud::NetworkConnectivity::V1::GetRouteTableRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::GetRouteTableRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetRouteTableRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_route_table(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::RouteTable

Pass arguments to `get_route_table` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the route table resource. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkConnectivity::V1::RouteTable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RouteTable)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::RouteTable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RouteTable)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::GetRouteTableRequest.new
    
    # Call the get_route_table method.
    result = client.get_route_table request
    
    # The returned object is of type Google::Cloud::NetworkConnectivity::V1::RouteTable.
    p result

### #get_spoke
    
    
    def get_spoke(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Spoke
    def get_spoke(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Spoke

Gets details about a Network Connectivity Center spoke.

**Overloads**
    
    
    def get_spoke(request, options = nil) -> ::Google::Cloud::NetworkConnectivity::V1::Spoke

Pass arguments to `get_spoke` via a request object, either of type [GetSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetSpokeRequest "Google::Cloud::NetworkConnectivity::V1::GetSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::GetSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-GetSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_spoke(name: nil) -> ::Google::Cloud::NetworkConnectivity::V1::Spoke

Pass arguments to `get_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the spoke resource. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::GetSpokeRequest.new
    
    # Call the get_spoke method.
    result = client.get_spoke request
    
    # The returned object is of type Google::Cloud::NetworkConnectivity::V1::Spoke.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new HubService client object.

**Yields**

  * (config) — Configure the HubService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::NetworkConnectivity::V1::HubService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_groups
    
    
    def list_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Group>
    def list_groups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Group>

Lists groups in a given hub.

**Overloads**
    
    
    def list_groups(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Group>

Pass arguments to `list_groups` via a request object, either of type [ListGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListGroupsRequest "Google::Cloud::NetworkConnectivity::V1::ListGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_groups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Group>

Pass arguments to `list_groups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource's name. 
  * **page_size** (::Integer) — The maximum number of results to return per page. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by a certain order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListGroupsRequest.new
    
    # Call the list_groups method.
    result = client.list_groups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::Group.
      p item
    end

### #list_hub_spokes
    
    
    def list_hub_spokes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>
    def list_hub_spokes(name: nil, spoke_locations: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Lists the Network Connectivity Center spokes associated with a specified hub and location. The list includes both spokes that are attached to the hub and spokes that have been proposed but not yet accepted.

**Overloads**
    
    
    def list_hub_spokes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Pass arguments to `list_hub_spokes` via a request object, either of type [ListHubSpokesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest "Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_hub_spokes(name: nil, spoke_locations: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Pass arguments to `list_hub_spokes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub. 
  * **spoke_locations** (::Array<::String>) — A list of locations. Specify one of the following: `[global]`, a single region (for example, `[us-central1]`), or a combination of values (for example, `[global, us-central1, us-west1]`). If the spoke_locations field is populated, the list of results includes only spokes in the specified location. If the spoke_locations field is not populated, the list of results includes spokes in all locations. 
  * **page_size** (::Integer) — The maximum number of results to return per page. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by name or create_time. 
  * **view** ([::Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest::SpokeView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubSpokesRequest-SpokeView)) — The view of the spoke to return. The view that you use determines which spoke fields are included in the response. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListHubSpokesRequest.new
    
    # Call the list_hub_spokes method.
    result = client.list_hub_spokes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::Spoke.
      p item
    end

### #list_hubs
    
    
    def list_hubs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Hub>
    def list_hubs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Hub>

Lists the Network Connectivity Center hubs associated with a given project.

**Overloads**
    
    
    def list_hubs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Hub>

Pass arguments to `list_hubs` via a request object, either of type [ListHubsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubsRequest "Google::Cloud::NetworkConnectivity::V1::ListHubsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListHubsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListHubsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_hubs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Hub>

Pass arguments to `list_hubs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource's name. 
  * **page_size** (::Integer) — The maximum number of results per page to return. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by a certain order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListHubsRequest.new
    
    # Call the list_hubs method.
    result = client.list_hubs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::Hub.
      p item
    end

### #list_route_tables
    
    
    def list_route_tables(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::RouteTable>
    def list_route_tables(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::RouteTable>

Lists route tables in a given hub.

**Overloads**
    
    
    def list_route_tables(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::RouteTable>

Pass arguments to `list_route_tables` via a request object, either of type [ListRouteTablesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListRouteTablesRequest "Google::Cloud::NetworkConnectivity::V1::ListRouteTablesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListRouteTablesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListRouteTablesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_route_tables(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::RouteTable>

Pass arguments to `list_route_tables` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource's name. 
  * **page_size** (::Integer) — The maximum number of results to return per page. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by a certain order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::RouteTable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RouteTable)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::RouteTable](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RouteTable)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListRouteTablesRequest.new
    
    # Call the list_route_tables method.
    result = client.list_route_tables request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::RouteTable.
      p item
    end

### #list_routes
    
    
    def list_routes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Route>
    def list_routes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Route>

Lists routes in a given route table.

**Overloads**
    
    
    def list_routes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Route>

Pass arguments to `list_routes` via a request object, either of type [ListRoutesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListRoutesRequest "Google::Cloud::NetworkConnectivity::V1::ListRoutesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListRoutesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListRoutesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_routes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Route>

Pass arguments to `list_routes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource's name. 
  * **page_size** (::Integer) — The maximum number of results to return per page. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by a certain order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Route)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Route)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListRoutesRequest.new
    
    # Call the list_routes method.
    result = client.list_routes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::Route.
      p item
    end

### #list_spokes
    
    
    def list_spokes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>
    def list_spokes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Lists the Network Connectivity Center spokes in a specified project and location.

**Overloads**
    
    
    def list_spokes(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Pass arguments to `list_spokes` via a request object, either of type [ListSpokesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListSpokesRequest "Google::Cloud::NetworkConnectivity::V1::ListSpokesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::ListSpokesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-ListSpokesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_spokes(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::Spoke>

Pass arguments to `list_spokes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource. 
  * **page_size** (::Integer) — The maximum number of results to return per page. 
  * **page_token** (::String) — The page token. 
  * **filter** (::String) — An expression that filters the list of results. 
  * **order_by** (::String) — Sort the results by a certain order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::ListSpokesRequest.new
    
    # Call the list_spokes method.
    result = client.list_spokes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::Spoke.
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
    
    
    def operations_client() -> ::Google::Cloud::NetworkConnectivity::V1::HubService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::NetworkConnectivity::V1::HubService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubService-Operations)) 



### #query_hub_status
    
    
    def query_hub_status(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry>
    def query_hub_status(name: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, group_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry>

Query the Private Service Connect propagation status of a Network Connectivity Center hub.

**Overloads**
    
    
    def query_hub_status(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry>

Pass arguments to `query_hub_status` via a request object, either of type [QueryHubStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-QueryHubStatusRequest "Google::Cloud::NetworkConnectivity::V1::QueryHubStatusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::QueryHubStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-QueryHubStatusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def query_hub_status(name: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, group_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry>

Pass arguments to `query_hub_status` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub. 
  * **page_size** (::Integer) — Optional. The maximum number of results to return per page. 
  * **page_token** (::String) — Optional. The page token. 
  * **filter** (::String) — 

Optional. An expression that filters the list of results. The filter can be used to filter the results by the following fields:

    * `psc_propagation_status.source_spoke`
    * `psc_propagation_status.source_group`
    * `psc_propagation_status.source_forwarding_rule`
    * `psc_propagation_status.target_spoke`
    * `psc_propagation_status.target_group`
    * `psc_propagation_status.code`
    * `psc_propagation_status.message`
  * **order_by** (::String) — 

Optional. Sort the results in ascending order by the specified fields. A comma-separated list of any of these fields:

    * `psc_propagation_status.source_spoke`
    * `psc_propagation_status.source_group`
    * `psc_propagation_status.source_forwarding_rule`
    * `psc_propagation_status.target_spoke`
    * `psc_propagation_status.target_group`
    * `psc_propagation_status.code` If `group_by` is set, the value of the `order_by` field must be the same as or a subset of the `group_by` field.
  * **group_by** (::String) — 

Optional. Aggregate the results by the specified fields. A comma-separated list of any of these fields:

    * `psc_propagation_status.source_spoke`
    * `psc_propagation_status.source_group`
    * `psc_propagation_status.source_forwarding_rule`
    * `psc_propagation_status.target_spoke`
    * `psc_propagation_status.target_group`
    * `psc_propagation_status.code`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubStatusEntry)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-HubStatusEntry)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::QueryHubStatusRequest.new
    
    # Call the query_hub_status method.
    result = client.query_hub_status request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::NetworkConnectivity::V1::HubStatusEntry.
      p item
    end

### #reject_hub_spoke
    
    
    def reject_hub_spoke(request, options = nil) -> ::Gapic::Operation
    def reject_hub_spoke(name: nil, spoke_uri: nil, request_id: nil, details: nil) -> ::Gapic::Operation

Rejects a Network Connectivity Center spoke from being attached to a hub. If the spoke was previously in the `ACTIVE` state, it transitions to the `INACTIVE` state and is no longer able to connect to other spokes that are attached to the hub.

**Overloads**
    
    
    def reject_hub_spoke(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reject_hub_spoke` via a request object, either of type [RejectHubSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RejectHubSpokeRequest "Google::Cloud::NetworkConnectivity::V1::RejectHubSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::RejectHubSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RejectHubSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def reject_hub_spoke(name: nil, spoke_uri: nil, request_id: nil, details: nil) -> ::Gapic::Operation

Pass arguments to `reject_hub_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub from which to reject the spoke. 
  * **spoke_uri** (::String) — Required. The URI of the spoke to reject from the hub. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **details** (::String) — Optional. Additional information provided by the hub administrator. 



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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::RejectHubSpokeRequest.new
    
    # Call the reject_hub_spoke method.
    result = client.reject_hub_spoke request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #reject_spoke_update
    
    
    def reject_spoke_update(request, options = nil) -> ::Gapic::Operation
    def reject_spoke_update(name: nil, spoke_uri: nil, spoke_etag: nil, details: nil, request_id: nil) -> ::Gapic::Operation

Rejects a proposal to update a Network Connectivity Center spoke in a hub.

**Overloads**
    
    
    def reject_spoke_update(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reject_spoke_update` via a request object, either of type [RejectSpokeUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RejectSpokeUpdateRequest "Google::Cloud::NetworkConnectivity::V1::RejectSpokeUpdateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::RejectSpokeUpdateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-RejectSpokeUpdateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def reject_spoke_update(name: nil, spoke_uri: nil, spoke_etag: nil, details: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `reject_spoke_update` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the hub to reject spoke update. 
  * **spoke_uri** (::String) — Required. The URI of the spoke to reject update. 
  * **spoke_etag** (::String) — Required. The etag of the spoke to reject update. 
  * **details** (::String) — Optional. Additional information provided by the hub administrator. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::RejectSpokeUpdateRequest.new
    
    # Call the reject_spoke_update method.
    result = client.reject_spoke_update request
    
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



### #update_group
    
    
    def update_group(request, options = nil) -> ::Gapic::Operation
    def update_group(update_mask: nil, group: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a Network Connectivity Center group.

**Overloads**
    
    
    def update_group(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_group` via a request object, either of type [UpdateGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateGroupRequest "Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_group(update_mask: nil, group: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_group` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. In the case of an update to an existing group, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 
  * **group** ([::Google::Cloud::NetworkConnectivity::V1::Group](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Group), ::Hash) — Required. The state that the group should be in after the update. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::UpdateGroupRequest.new
    
    # Call the update_group method.
    result = client.update_group request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_hub
    
    
    def update_hub(request, options = nil) -> ::Gapic::Operation
    def update_hub(update_mask: nil, hub: nil, request_id: nil) -> ::Gapic::Operation

Updates the description and/or labels of a Network Connectivity Center hub.

**Overloads**
    
    
    def update_hub(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_hub` via a request object, either of type [UpdateHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateHubRequest "Google::Cloud::NetworkConnectivity::V1::UpdateHubRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::UpdateHubRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateHubRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_hub(update_mask: nil, hub: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_hub` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. In the case of an update to an existing hub, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 
  * **hub** ([::Google::Cloud::NetworkConnectivity::V1::Hub](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Hub), ::Hash) — Required. The state that the hub should be in after the update. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::UpdateHubRequest.new
    
    # Call the update_hub method.
    result = client.update_hub request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_spoke
    
    
    def update_spoke(request, options = nil) -> ::Gapic::Operation
    def update_spoke(update_mask: nil, spoke: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a Network Connectivity Center spoke.

**Overloads**
    
    
    def update_spoke(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_spoke` via a request object, either of type [UpdateSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateSpokeRequest "Google::Cloud::NetworkConnectivity::V1::UpdateSpokeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::NetworkConnectivity::V1::UpdateSpokeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-UpdateSpokeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_spoke(update_mask: nil, spoke: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_spoke` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. In the case of an update to an existing spoke, field mask is used to specify the fields to be overwritten. The fields specified in the update_mask are relative to the resource, not the full request. A field is overwritten if it is in the mask. If the user does not provide a mask, then all fields are overwritten. 
  * **spoke** ([::Google::Cloud::NetworkConnectivity::V1::Spoke](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-network_connectivity-v1/latest/Google-Cloud-NetworkConnectivity-V1-Spoke), ::Hash) — Required. The state that the spoke should be in after the update. 
  * **request_id** (::String) — Optional. A request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server knows to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate commitments for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check to see whether the original operation was received. If it was, the server ignores the second request. This behavior prevents clients from mistakenly creating duplicate commitments.

The request ID must be a valid UUID, with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/network_connectivity/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::NetworkConnectivity::V1::HubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::NetworkConnectivity::V1::UpdateSpokeRequest.new
    
    # Call the update_spoke method.
    result = client.update_spoke request
    
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

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
