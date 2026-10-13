---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Addresses::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:20.933459+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Addresses::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Addresses::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::Addresses::Rest::Client.

REST client for the Addresses service.

The Addresses API.

This client uses Addresses version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Addresses Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration "Google::Cloud::Compute::V1::Addresses::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Addresses clients
    ::Google::Cloud::Compute::V1::Addresses::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #aggregated_list
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>

Retrieves an aggregated list of addresses.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Overloads**
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>

Pass arguments to `aggregated_list` via a request object, either of type [Google::Cloud::Compute::V1::AggregatedListAddressesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListAddressesRequest "Google::Cloud::Compute::V1::AggregatedListAddressesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::AggregatedListAddressesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListAddressesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>

Pass arguments to `aggregated_list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

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

  * **include_all_scopes** (::Boolean) — Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included. 
  * **max_results** (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 
  * **order_by** (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 

  * **page_token** (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 
  * **project** (::String) — Project ID for this request. 
  * **service_project_number** (::Integer) — The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AddressesScopedList>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::AggregatedListAddressesRequest.new
    
    # Call the aggregated_list method.
    result = client.aggregated_list request
    
    # The returned object is of type Google::Cloud::Compute::V1::AddressAggregatedList.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Addresses Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client#Google__Cloud__Compute__V1__Addresses__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::Addresses::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration "Google::Cloud::Compute::V1::Addresses::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration)) 



### #delete
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def delete(address: nil, project: nil, region: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Deletes the specified address resource.

**Overloads**
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via a request object, either of type [DeleteAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteAddressRequest "Google::Cloud::Compute::V1::DeleteAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::DeleteAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete(address: nil, project: nil, region: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **address** (::String) — Name of the address resource to delete. 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 
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
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::DeleteAddressRequest.new
    
    # Call the delete method.
    result = client.delete request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::Address
    def get(address: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::Address

Returns the specified address resource.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::Address

Pass arguments to `get` via a request object, either of type [GetAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetAddressRequest "Google::Cloud::Compute::V1::GetAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(address: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::Address

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **address** (::String) — Name of the address resource to return. 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetAddressRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::Address.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Addresses REST client object.

**Yields**

  * (config) — Configure the Addresses client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Addresses-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::Addresses::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #insert
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def insert(address_resource: nil, project: nil, region: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Creates an address resource in the specified project by using the data included in the request.

**Overloads**
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via a request object, either of type [InsertAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertAddressRequest "Google::Cloud::Compute::V1::InsertAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::InsertAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def insert(address_resource: nil, project: nil, region: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **address_resource** ([::Google::Cloud::Compute::V1::Address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 
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
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::InsertAddressRequest.new
    
    # Call the insert method.
    result = client.insert request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #list
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::Address>
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, region: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::Address>

Retrieves a list of addresses contained within the specified region.

**Overloads**
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::Address>

Pass arguments to `list` via a request object, either of type [ListAddressesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListAddressesRequest "Google::Cloud::Compute::V1::ListAddressesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListAddressesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListAddressesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, region: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::Address>

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
  * **region** (::String) — Name of the region for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::Address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::Address](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Address)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListAddressesRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Compute::V1::AddressList.
    p result

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #move
    
    
    def move(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def move(address: nil, project: nil, region: nil, region_addresses_move_request_resource: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Moves the specified address resource.

**Overloads**
    
    
    def move(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `move` via a request object, either of type [MoveAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MoveAddressRequest "Google::Cloud::Compute::V1::MoveAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::MoveAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-MoveAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def move(address: nil, project: nil, region: nil, region_addresses_move_request_resource: nil, request_id: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `move` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **address** (::String) — Name of the address resource to move. 
  * **project** (::String) — Source project ID which the Address is moved from. 
  * **region** (::String) — Name of the region for this request. 
  * **region_addresses_move_request_resource** ([::Google::Cloud::Compute::V1::RegionAddressesMoveRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionAddressesMoveRequest), ::Hash) — The body resource for this request 
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
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::MoveAddressRequest.new
    
    # Call the move method.
    result = client.move request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #region_operations
    
    
    def region_operations() -> ::Google::Cloud::Compute::V1::RegionOperations::Rest::Client

Get the associated client for long-running operations via RegionOperations.

**Returns**

  * ([::Google::Cloud::Compute::V1::RegionOperations::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionOperations-Rest-Client)) 



### #set_labels
    
    
    def set_labels(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def set_labels(project: nil, region: nil, region_set_labels_request_resource: nil, request_id: nil, resource: nil) -> ::Gapic::GenericLRO::Operation

Sets the labels on an Address. To learn more about labels, read theLabeling Resources documentation.

**Overloads**
    
    
    def set_labels(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `set_labels` via a request object, either of type [SetLabelsAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetLabelsAddressRequest "Google::Cloud::Compute::V1::SetLabelsAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::SetLabelsAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetLabelsAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def set_labels(project: nil, region: nil, region_set_labels_request_resource: nil, request_id: nil, resource: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `set_labels` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — The region for this request. 
  * **region_set_labels_request_resource** ([::Google::Cloud::Compute::V1::RegionSetLabelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RegionSetLabelsRequest), ::Hash) — The body resource for this request 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **resource** (::String) — Name or id of the resource for this request. 



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
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::SetLabelsAddressRequest.new
    
    # Call the set_labels method.
    result = client.set_labels request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse
    def test_iam_permissions(project: nil, region: nil, resource: nil, test_permissions_request_resource: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Returns permissions that a caller has on the specified resource.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [TestIamPermissionsAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsAddressRequest "Google::Cloud::Compute::V1::TestIamPermissionsAddressRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::TestIamPermissionsAddressRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsAddressRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def test_iam_permissions(project: nil, region: nil, resource: nil, test_permissions_request_resource: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — The name of the region for this request. 
  * **resource** (::String) — Name or id of the resource for this request. 
  * **test_permissions_request_resource** ([::Google::Cloud::Compute::V1::TestPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsRequest), ::Hash) — The body resource for this request 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::TestPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::TestPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Addresses::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::TestIamPermissionsAddressRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Cloud::Compute::V1::TestPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
