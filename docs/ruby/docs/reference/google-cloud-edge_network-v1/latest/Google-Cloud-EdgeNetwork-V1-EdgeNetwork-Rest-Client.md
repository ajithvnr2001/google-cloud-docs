---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client/
title: Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:49:54.561413+00:00
---

# Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Distributed Cloud Edge Network V1 API - Class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.3  0.5.0  0.4.1  0.3.1  0.2.1  0.1.0 

Reference documentation and code samples for the Distributed Cloud Edge Network V1 API class Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.

REST client for the EdgeNetwork service.

EdgeNetwork API provides managed, highly available cloud dynamic network configuration service to the GEC customer to enable edge application and network function solutions. This allows the customers to easily define and configure the network setup and property to meet the workload requirement.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the EdgeNetwork Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration "Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all EdgeNetwork clients
    ::Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the EdgeNetwork Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client#Google__Cloud__EdgeNetwork__V1__EdgeNetwork__Rest__Client_configure_class_ "Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration "Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration)) 



### #create_interconnect_attachment
    
    
    def create_interconnect_attachment(request, options = nil) -> ::Gapic::Operation
    def create_interconnect_attachment(parent: nil, interconnect_attachment_id: nil, interconnect_attachment: nil, request_id: nil) -> ::Gapic::Operation

Creates a new InterconnectAttachment in a given project and location.

**Overloads**
    
    
    def create_interconnect_attachment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_interconnect_attachment` via a request object, either of type [CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateInterconnectAttachmentRequest "Google::Cloud::EdgeNetwork::V1::CreateInterconnectAttachmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::CreateInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateInterconnectAttachmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_interconnect_attachment(parent: nil, interconnect_attachment_id: nil, interconnect_attachment: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_interconnect_attachment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **interconnect_attachment_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and interconnect_attachment_id from the method_signature of Create RPC 
  * **interconnect_attachment** ([::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectAttachment), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::CreateInterconnectAttachmentRequest.new
    
    # Call the create_interconnect_attachment method.
    result = client.create_interconnect_attachment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_network
    
    
    def create_network(request, options = nil) -> ::Gapic::Operation
    def create_network(parent: nil, network_id: nil, network: nil, request_id: nil) -> ::Gapic::Operation

Creates a new Network in a given project and location.

**Overloads**
    
    
    def create_network(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_network` via a request object, either of type [CreateNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateNetworkRequest "Google::Cloud::EdgeNetwork::V1::CreateNetworkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::CreateNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateNetworkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_network(parent: nil, network_id: nil, network: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_network` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **network_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and network_id from the method_signature of Create RPC 
  * **network** ([::Google::Cloud::EdgeNetwork::V1::Network](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Network), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::CreateNetworkRequest.new
    
    # Call the create_network method.
    result = client.create_network request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_router
    
    
    def create_router(request, options = nil) -> ::Gapic::Operation
    def create_router(parent: nil, router_id: nil, router: nil, request_id: nil) -> ::Gapic::Operation

Creates a new Router in a given project and location.

**Overloads**
    
    
    def create_router(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_router` via a request object, either of type [CreateRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateRouterRequest "Google::Cloud::EdgeNetwork::V1::CreateRouterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::CreateRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateRouterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_router(parent: nil, router_id: nil, router: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_router` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **router_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and router_id from the method_signature of Create RPC 
  * **router** ([::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::CreateRouterRequest.new
    
    # Call the create_router method.
    result = client.create_router request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_subnet
    
    
    def create_subnet(request, options = nil) -> ::Gapic::Operation
    def create_subnet(parent: nil, subnet_id: nil, subnet: nil, request_id: nil) -> ::Gapic::Operation

Creates a new Subnet in a given project and location.

**Overloads**
    
    
    def create_subnet(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_subnet` via a request object, either of type [CreateSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateSubnetRequest "Google::Cloud::EdgeNetwork::V1::CreateSubnetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::CreateSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-CreateSubnetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_subnet(parent: nil, subnet_id: nil, subnet: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_subnet` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **subnet_id** (::String) — Required. Id of the requesting object If auto-generating Id server-side, remove this field and subnet_id from the method_signature of Create RPC 
  * **subnet** ([::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::CreateSubnetRequest.new
    
    # Call the create_subnet method.
    result = client.create_subnet request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_interconnect_attachment
    
    
    def delete_interconnect_attachment(request, options = nil) -> ::Gapic::Operation
    def delete_interconnect_attachment(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single InterconnectAttachment.

**Overloads**
    
    
    def delete_interconnect_attachment(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_interconnect_attachment` via a request object, either of type [DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteInterconnectAttachmentRequest "Google::Cloud::EdgeNetwork::V1::DeleteInterconnectAttachmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DeleteInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteInterconnectAttachmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_interconnect_attachment(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_interconnect_attachment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DeleteInterconnectAttachmentRequest.new
    
    # Call the delete_interconnect_attachment method.
    result = client.delete_interconnect_attachment request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_network
    
    
    def delete_network(request, options = nil) -> ::Gapic::Operation
    def delete_network(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Network.

**Overloads**
    
    
    def delete_network(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_network` via a request object, either of type [DeleteNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteNetworkRequest "Google::Cloud::EdgeNetwork::V1::DeleteNetworkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DeleteNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteNetworkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_network(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_network` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DeleteNetworkRequest.new
    
    # Call the delete_network method.
    result = client.delete_network request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_router
    
    
    def delete_router(request, options = nil) -> ::Gapic::Operation
    def delete_router(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Router.

**Overloads**
    
    
    def delete_router(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_router` via a request object, either of type [DeleteRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteRouterRequest "Google::Cloud::EdgeNetwork::V1::DeleteRouterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DeleteRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteRouterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_router(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_router` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DeleteRouterRequest.new
    
    # Call the delete_router method.
    result = client.delete_router request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_subnet
    
    
    def delete_subnet(request, options = nil) -> ::Gapic::Operation
    def delete_subnet(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Subnet.

**Overloads**
    
    
    def delete_subnet(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_subnet` via a request object, either of type [DeleteSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteSubnetRequest "Google::Cloud::EdgeNetwork::V1::DeleteSubnetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DeleteSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DeleteSubnetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_subnet(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_subnet` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DeleteSubnetRequest.new
    
    # Call the delete_subnet method.
    result = client.delete_subnet request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #diagnose_interconnect
    
    
    def diagnose_interconnect(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse
    def diagnose_interconnect(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse

Get the diagnostics of a single interconnect resource.

**Overloads**
    
    
    def diagnose_interconnect(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse

Pass arguments to `diagnose_interconnect` via a request object, either of type [DiagnoseInterconnectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseInterconnectRequest "Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseInterconnectRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def diagnose_interconnect(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse

Pass arguments to `diagnose_interconnect` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the interconnect resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseInterconnectResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseInterconnectResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectRequest.new
    
    # Call the diagnose_interconnect method.
    result = client.diagnose_interconnect request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::DiagnoseInterconnectResponse.
    p result

### #diagnose_network
    
    
    def diagnose_network(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse
    def diagnose_network(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse

Get the diagnostics of a single network resource.

**Overloads**
    
    
    def diagnose_network(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse

Pass arguments to `diagnose_network` via a request object, either of type [DiagnoseNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseNetworkRequest "Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseNetworkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def diagnose_network(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse

Pass arguments to `diagnose_network` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the network resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseNetworkResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseNetworkResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkRequest.new
    
    # Call the diagnose_network method.
    result = client.diagnose_network request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::DiagnoseNetworkResponse.
    p result

### #diagnose_router
    
    
    def diagnose_router(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse
    def diagnose_router(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse

Get the diagnostics of a single router resource.

**Overloads**
    
    
    def diagnose_router(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse

Pass arguments to `diagnose_router` via a request object, either of type [DiagnoseRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseRouterRequest "Google::Cloud::EdgeNetwork::V1::DiagnoseRouterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseRouterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def diagnose_router(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse

Pass arguments to `diagnose_router` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the router resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseRouterResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-DiagnoseRouterResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::DiagnoseRouterRequest.new
    
    # Call the diagnose_router method.
    result = client.diagnose_router request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::DiagnoseRouterResponse.
    p result

### #get_interconnect
    
    
    def get_interconnect(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Interconnect
    def get_interconnect(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Interconnect

Gets details of a single Interconnect.

**Overloads**
    
    
    def get_interconnect(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Interconnect

Pass arguments to `get_interconnect` via a request object, either of type [GetInterconnectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetInterconnectRequest "Google::Cloud::EdgeNetwork::V1::GetInterconnectRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetInterconnectRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetInterconnectRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_interconnect(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Interconnect

Pass arguments to `get_interconnect` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::Interconnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Interconnect)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::Interconnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Interconnect)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetInterconnectRequest.new
    
    # Call the get_interconnect method.
    result = client.get_interconnect request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::Interconnect.
    p result

### #get_interconnect_attachment
    
    
    def get_interconnect_attachment(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment
    def get_interconnect_attachment(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment

Gets details of a single InterconnectAttachment.

**Overloads**
    
    
    def get_interconnect_attachment(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment

Pass arguments to `get_interconnect_attachment` via a request object, either of type [GetInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetInterconnectAttachmentRequest "Google::Cloud::EdgeNetwork::V1::GetInterconnectAttachmentRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetInterconnectAttachmentRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetInterconnectAttachmentRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_interconnect_attachment(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment

Pass arguments to `get_interconnect_attachment` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectAttachment)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectAttachment)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetInterconnectAttachmentRequest.new
    
    # Call the get_interconnect_attachment method.
    result = client.get_interconnect_attachment request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::InterconnectAttachment.
    p result

### #get_network
    
    
    def get_network(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Network
    def get_network(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Network

Gets details of a single Network.

**Overloads**
    
    
    def get_network(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Network

Pass arguments to `get_network` via a request object, either of type [GetNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetNetworkRequest "Google::Cloud::EdgeNetwork::V1::GetNetworkRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetNetworkRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetNetworkRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_network(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Network

Pass arguments to `get_network` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::Network](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Network)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::Network](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Network)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetNetworkRequest.new
    
    # Call the get_network method.
    result = client.get_network request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::Network.
    p result

### #get_router
    
    
    def get_router(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Router
    def get_router(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Router

Gets details of a single Router.

**Overloads**
    
    
    def get_router(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Router

Pass arguments to `get_router` via a request object, either of type [GetRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetRouterRequest "Google::Cloud::EdgeNetwork::V1::GetRouterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetRouterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_router(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Router

Pass arguments to `get_router` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetRouterRequest.new
    
    # Call the get_router method.
    result = client.get_router request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::Router.
    p result

### #get_subnet
    
    
    def get_subnet(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Subnet
    def get_subnet(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Subnet

Gets details of a single Subnet.

**Overloads**
    
    
    def get_subnet(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Subnet

Pass arguments to `get_subnet` via a request object, either of type [GetSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetSubnetRequest "Google::Cloud::EdgeNetwork::V1::GetSubnetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetSubnetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_subnet(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Subnet

Pass arguments to `get_subnet` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetSubnetRequest.new
    
    # Call the get_subnet method.
    result = client.get_subnet request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::Subnet.
    p result

### #get_zone
    
    
    def get_zone(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Zone
    def get_zone(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Zone

Deprecated: not implemented. Gets details of a single Zone.

**Overloads**
    
    
    def get_zone(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::Zone

Pass arguments to `get_zone` via a request object, either of type [GetZoneRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetZoneRequest "Google::Cloud::EdgeNetwork::V1::GetZoneRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::GetZoneRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-GetZoneRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_zone(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::Zone

Pass arguments to `get_zone` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::Zone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Zone)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::Zone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Zone)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::GetZoneRequest.new
    
    # Call the get_zone method.
    result = client.get_zone request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::Zone.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new EdgeNetwork REST client object.

**Yields**

  * (config) — Configure the EdgeNetwork client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #initialize_zone
    
    
    def initialize_zone(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse
    def initialize_zone(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse

InitializeZone will initialize resources for a zone in a project.

**Overloads**
    
    
    def initialize_zone(request, options = nil) -> ::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse

Pass arguments to `initialize_zone` via a request object, either of type [InitializeZoneRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InitializeZoneRequest "Google::Cloud::EdgeNetwork::V1::InitializeZoneRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::InitializeZoneRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InitializeZoneRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def initialize_zone(name: nil) -> ::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse

Pass arguments to `initialize_zone` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the zone resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InitializeZoneResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InitializeZoneResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::InitializeZoneRequest.new
    
    # Call the initialize_zone method.
    result = client.initialize_zone request
    
    # The returned object is of type Google::Cloud::EdgeNetwork::V1::InitializeZoneResponse.
    p result

### #list_interconnect_attachments
    
    
    def list_interconnect_attachments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment>
    def list_interconnect_attachments(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment>

Lists InterconnectAttachments in a given project and location.

**Overloads**
    
    
    def list_interconnect_attachments(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment>

Pass arguments to `list_interconnect_attachments` via a request object, either of type [ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListInterconnectAttachmentsRequest "Google::Cloud::EdgeNetwork::V1::ListInterconnectAttachmentsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListInterconnectAttachmentsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListInterconnectAttachmentsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_interconnect_attachments(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment>

Pass arguments to `list_interconnect_attachments` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListInterconnectAttachmentsRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectAttachment)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-InterconnectAttachment)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListInterconnectAttachmentsRequest.new
    
    # Call the list_interconnect_attachments method.
    result = client.list_interconnect_attachments request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::InterconnectAttachment.
      p item
    end

### #list_interconnects
    
    
    def list_interconnects(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Interconnect>
    def list_interconnects(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Interconnect>

Lists Interconnects in a given project and location.

**Overloads**
    
    
    def list_interconnects(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Interconnect>

Pass arguments to `list_interconnects` via a request object, either of type [ListInterconnectsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListInterconnectsRequest "Google::Cloud::EdgeNetwork::V1::ListInterconnectsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListInterconnectsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListInterconnectsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_interconnects(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Interconnect>

Pass arguments to `list_interconnects` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListInterconnectsRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Interconnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Interconnect)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Interconnect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Interconnect)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListInterconnectsRequest.new
    
    # Call the list_interconnects method.
    result = client.list_interconnects request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::Interconnect.
      p item
    end

### #list_networks
    
    
    def list_networks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Network>
    def list_networks(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Network>

Lists Networks in a given project and location.

**Overloads**
    
    
    def list_networks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Network>

Pass arguments to `list_networks` via a request object, either of type [ListNetworksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListNetworksRequest "Google::Cloud::EdgeNetwork::V1::ListNetworksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListNetworksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListNetworksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_networks(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Network>

Pass arguments to `list_networks` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListNetworksRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Network](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Network)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Network](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Network)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListNetworksRequest.new
    
    # Call the list_networks method.
    result = client.list_networks request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::Network.
      p item
    end

### #list_routers
    
    
    def list_routers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Router>
    def list_routers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Router>

Lists Routers in a given project and location.

**Overloads**
    
    
    def list_routers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Router>

Pass arguments to `list_routers` via a request object, either of type [ListRoutersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListRoutersRequest "Google::Cloud::EdgeNetwork::V1::ListRoutersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListRoutersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListRoutersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_routers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Router>

Pass arguments to `list_routers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListRoutersRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListRoutersRequest.new
    
    # Call the list_routers method.
    result = client.list_routers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::Router.
      p item
    end

### #list_subnets
    
    
    def list_subnets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Subnet>
    def list_subnets(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Subnet>

Lists Subnets in a given project and location.

**Overloads**
    
    
    def list_subnets(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Subnet>

Pass arguments to `list_subnets` via a request object, either of type [ListSubnetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListSubnetsRequest "Google::Cloud::EdgeNetwork::V1::ListSubnetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListSubnetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListSubnetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_subnets(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Subnet>

Pass arguments to `list_subnets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListSubnetsRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListSubnetsRequest.new
    
    # Call the list_subnets method.
    result = client.list_subnets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::Subnet.
      p item
    end

### #list_zones
    
    
    def list_zones(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Zone>
    def list_zones(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Zone>

Deprecated: not implemented. Lists Zones in a given project and location.

**Overloads**
    
    
    def list_zones(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Zone>

Pass arguments to `list_zones` via a request object, either of type [ListZonesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListZonesRequest "Google::Cloud::EdgeNetwork::V1::ListZonesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::ListZonesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-ListZonesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_zones(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::EdgeNetwork::V1::Zone>

Pass arguments to `list_zones` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListZonesRequest 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results 
  * **order_by** (::String) — Hint for how to order the results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Zone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Zone)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::EdgeNetwork::V1::Zone](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Zone)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::ListZonesRequest.new
    
    # Call the list_zones method.
    result = client.list_zones request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::EdgeNetwork::V1::Zone.
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
    
    
    def operations_client() -> ::Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-EdgeNetwork-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_router
    
    
    def update_router(request, options = nil) -> ::Gapic::Operation
    def update_router(update_mask: nil, router: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Router.

**Overloads**
    
    
    def update_router(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_router` via a request object, either of type [UpdateRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-UpdateRouterRequest "Google::Cloud::EdgeNetwork::V1::UpdateRouterRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::UpdateRouterRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-UpdateRouterRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_router(update_mask: nil, router: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_router` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the Router resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **router** ([::Google::Cloud::EdgeNetwork::V1::Router](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Router), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::UpdateRouterRequest.new
    
    # Call the update_router method.
    result = client.update_router request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_subnet
    
    
    def update_subnet(request, options = nil) -> ::Gapic::Operation
    def update_subnet(update_mask: nil, subnet: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Subnet.

**Overloads**
    
    
    def update_subnet(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_subnet` via a request object, either of type [UpdateSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-UpdateSubnetRequest "Google::Cloud::EdgeNetwork::V1::UpdateSubnetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::EdgeNetwork::V1::UpdateSubnetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-UpdateSubnetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_subnet(update_mask: nil, subnet: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_subnet` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the Subnet resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **subnet** ([::Google::Cloud::EdgeNetwork::V1::Subnet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-edge_network-v1/latest/Google-Cloud-EdgeNetwork-V1-Subnet), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/edge_network/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::EdgeNetwork::V1::EdgeNetwork::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::EdgeNetwork::V1::UpdateSubnetRequest.new
    
    # Call the update_subnet method.
    result = client.update_subnet request
    
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
