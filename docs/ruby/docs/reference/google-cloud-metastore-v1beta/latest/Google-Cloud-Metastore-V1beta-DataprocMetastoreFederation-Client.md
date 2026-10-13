---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client/
title: Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client (v0.22.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:27.018261+00:00
---

# Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client (v0.22.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dataproc Metastore V1beta API - Class Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client (v0.22.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.22.1 (latest)  0.22.0  0.21.0  0.20.0  0.19.1  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.2  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Dataproc Metastore V1beta API class Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.

Client for the DataprocMetastoreFederation service.

Configures and manages metastore federation services. Dataproc Metastore Federation Service allows federating a collection of backend metastores like BigQuery, Dataplex Lakes, and other Dataproc Metastores. The Federation Service exposes a gRPC URL through which metadata from the backend metastores are served at query time.

The Dataproc Metastore Federation API defines the following resource model:

  * The service works with a collection of Google Cloud projects.
  * Each project has a collection of available locations.
  * Each location has a collection of federations.
  * Dataproc Metastore Federations are resources with names of the form: `projects/{project_number}/locations/{location_id}/federations/{federation_id}`.



## Inherits

  * Object 



## Includes

  * [Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DataprocMetastoreFederation Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration "Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DataprocMetastoreFederation clients
    ::Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DataprocMetastoreFederation Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client#Google__Cloud__Metastore__V1beta__DataprocMetastoreFederation__Client_configure_class_ "Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration "Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration)) 



### #create_federation
    
    
    def create_federation(request, options = nil) -> ::Gapic::Operation
    def create_federation(parent: nil, federation_id: nil, federation: nil, request_id: nil) -> ::Gapic::Operation

Creates a metastore federation in a project and location.

**Overloads**
    
    
    def create_federation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_federation` via a request object, either of type [CreateFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-CreateFederationRequest "Google::Cloud::Metastore::V1beta::CreateFederationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Metastore::V1beta::CreateFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-CreateFederationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_federation(parent: nil, federation_id: nil, federation: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_federation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative resource name of the location in which to create a federation service, in the following form:

`projects/{project_number}/locations/{location_id}`. 

  * **federation_id** (::String) — Required. The ID of the metastore federation, which is used as the final component of the metastore federation's name.

This value must be between 2 and 63 characters long inclusive, begin with a letter, end with a letter or number, and consist of alpha-numeric ASCII characters or hyphens. 

  * **federation** ([::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation), ::Hash) — Required. The Metastore Federation to create. The `name` field is ignored. The ID of the created metastore federation must be provided in the request's `federation_id` field. 
  * **request_id** (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




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
    
    
    require "google/cloud/metastore/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Metastore::V1beta::CreateFederationRequest.new
    
    # Call the create_federation method.
    result = client.create_federation request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_federation
    
    
    def delete_federation(request, options = nil) -> ::Gapic::Operation
    def delete_federation(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single federation.

**Overloads**
    
    
    def delete_federation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_federation` via a request object, either of type [Google::Cloud::Metastore::V1beta::DeleteFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DeleteFederationRequest "Google::Cloud::Metastore::V1beta::DeleteFederationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Metastore::V1beta::DeleteFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DeleteFederationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_federation(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_federation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The relative resource name of the metastore federation to delete, in the following form:

`projects/{project_number}/locations/{location_id}/federations/{federation_id}`. 

  * **request_id** (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




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
    
    
    require "google/cloud/metastore/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Metastore::V1beta::DeleteFederationRequest.new
    
    # Call the delete_federation method.
    result = client.delete_federation request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_federation
    
    
    def get_federation(request, options = nil) -> ::Google::Cloud::Metastore::V1beta::Federation
    def get_federation(name: nil) -> ::Google::Cloud::Metastore::V1beta::Federation

Gets the details of a single federation.

**Overloads**
    
    
    def get_federation(request, options = nil) -> ::Google::Cloud::Metastore::V1beta::Federation

Pass arguments to `get_federation` via a request object, either of type [GetFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-GetFederationRequest "Google::Cloud::Metastore::V1beta::GetFederationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Metastore::V1beta::GetFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-GetFederationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_federation(name: nil) -> ::Google::Cloud::Metastore::V1beta::Federation

Pass arguments to `get_federation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The relative resource name of the metastore federation to retrieve, in the following form:

`projects/{project_number}/locations/{location_id}/federations/{federation_id}`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/metastore/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Metastore::V1beta::GetFederationRequest.new
    
    # Call the get_federation method.
    result = client.get_federation request
    
    # The returned object is of type Google::Cloud::Metastore::V1beta::Federation.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DataprocMetastoreFederation client object.

**Yields**

  * (config) — Configure the DataprocMetastoreFederation client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new do |config|
      config.timeout = 10.0
    end

### #list_federations
    
    
    def list_federations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Metastore::V1beta::Federation>
    def list_federations(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Metastore::V1beta::Federation>

Lists federations in a project and location.

**Overloads**
    
    
    def list_federations(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Metastore::V1beta::Federation>

Pass arguments to `list_federations` via a request object, either of type [ListFederationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListFederationsRequest "Google::Cloud::Metastore::V1beta::ListFederationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Metastore::V1beta::ListFederationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-ListFederationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_federations(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Metastore::V1beta::Federation>

Pass arguments to `list_federations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The relative resource name of the location of metastore federations to list, in the following form: `projects/{project_number}/locations/{location_id}`. 
  * **page_size** (::Integer) — Optional. The maximum number of federations to return. The response may contain less than the maximum number. If unspecified, no more than 500 services are returned. The maximum value is 1000; values above 1000 are changed to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous ListFederationServices call. Provide this token to retrieve the subsequent page.

To retrieve the first page, supply an empty page token.

When paginating, other parameters provided to ListFederationServices must match the call that provided the page token. 

  * **filter** (::String) — Optional. The filter to apply to list results. 
  * **order_by** (::String) — Optional. Specify the ordering of results as described in [Sorting Order](https://cloud.google.com/apis/design/design_patterns#sorting_order). If not specified, the results will be sorted in the default order. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/metastore/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Metastore::V1beta::ListFederationsRequest.new
    
    # Call the list_federations method.
    result = client.list_federations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Metastore::V1beta::Federation.
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
    
    
    def operations_client() -> ::Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-DataprocMetastoreFederation-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_federation
    
    
    def update_federation(request, options = nil) -> ::Gapic::Operation
    def update_federation(update_mask: nil, federation: nil, request_id: nil) -> ::Gapic::Operation

Updates the fields of a federation.

**Overloads**
    
    
    def update_federation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_federation` via a request object, either of type [UpdateFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-UpdateFederationRequest "Google::Cloud::Metastore::V1beta::UpdateFederationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Metastore::V1beta::UpdateFederationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-UpdateFederationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_federation(update_mask: nil, federation: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_federation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A field mask used to specify the fields to be overwritten in the metastore federation resource by the update. Fields specified in the `update_mask` are relative to the resource (not to the full request). A field is overwritten if it is in the mask. 
  * **federation** ([::Google::Cloud::Metastore::V1beta::Federation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-metastore-v1beta/latest/Google-Cloud-Metastore-V1beta-Federation), ::Hash) — Required. The metastore federation to update. The server only merges fields in the service if they are specified in `update_mask`.

The metastore federation's `name` field is used to identify the metastore service to be updated. 

  * **request_id** (::String) — Optional. A request ID. Specify a unique request ID to allow the server to ignore the request if it has completed. The server will ignore subsequent requests that provide a duplicate request ID for at least 60 minutes after the first request.

For example, if an initial request times out, followed by another request with the same request ID, the server ignores the second request to prevent the creation of duplicate commitments.

The request ID must be a valid [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier#Format) A zero UUID (00000000-0000-0000-0000-000000000000) is not supported. 




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
    
    
    require "google/cloud/metastore/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Metastore::V1beta::DataprocMetastoreFederation::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Metastore::V1beta::UpdateFederationRequest.new
    
    # Call the update_federation method.
    result = client.update_federation request
    
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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
