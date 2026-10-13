---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:51:38.850966+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.

REST client for the ReservationSubBlocks service.

The ReservationSubBlocks API.

This client uses ReservationSubBlocks version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ReservationSubBlocks Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration "Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ReservationSubBlocks clients
    ::Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ReservationSubBlocks Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client#Google__Cloud__Compute__V1__ReservationSubBlocks__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration "Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration)) 



### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse
    def get(parent_name: nil, project: nil, reservation_sub_block: nil, view: nil, zone: nil) -> ::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse

Retrieves information about the specified reservation subBlock.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse

Pass arguments to `get` via a request object, either of type [GetReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetReservationSubBlockRequest "Google::Cloud::Compute::V1::GetReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(parent_name: nil, project: nil, reservation_sub_block: nil, view: nil, zone: nil) -> ::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_name** (::String) — The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name} 
  * **project** (::String) — Project ID for this request. 
  * **reservation_sub_block** (::String) — The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID. 
  * **view** (::String) — View of the subBlock. Check the View enum for the list of possible values. 
  * **zone** (::String) — Name of the zone for this request. Zone name should conform to RFC1035. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocksGetResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocksGetResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetReservationSubBlockRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::ReservationSubBlocksGetResponse.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Cloud::Compute::V1::Policy
    def get_iam_policy(options_requested_policy_version: nil, parent_resource: nil, project: nil, resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::Policy

Gets the access control policy for a resource. May be empty if no such policy or resource exists.

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Cloud::Compute::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [GetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetIamPolicyReservationSubBlockRequest "Google::Cloud::Compute::V1::GetIamPolicyReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetIamPolicyReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_iam_policy(options_requested_policy_version: nil, parent_resource: nil, project: nil, resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **options_requested_policy_version** (::Integer) — Requested IAM Policy version. 
  * **parent_resource** (::String) — Name or id of parent resource of the resource for this request. 
  * **project** (::String) — Project ID for this request. 
  * **resource** (::String) — Name or id of the resource for this request. 
  * **zone** (::String) — The name of the zone for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetIamPolicyReservationSubBlockRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Cloud::Compute::V1::Policy.
    p result

### #get_version
    
    
    def get_version(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def get_version(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, reservation_sub_blocks_get_version_request_resource: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Allows customers to get SBOM versions of a reservation subBlock.

**Overloads**
    
    
    def get_version(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `get_version` via a request object, either of type [GetVersionReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetVersionReservationSubBlockRequest "Google::Cloud::Compute::V1::GetVersionReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetVersionReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetVersionReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_version(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, reservation_sub_blocks_get_version_request_resource: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `get_version` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_name** (::String) — The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name} 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **reservation_sub_block** (::String) — The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID. 
  * **reservation_sub_blocks_get_version_request_resource** ([::Google::Cloud::Compute::V1::ReservationSubBlocksGetVersionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocksGetVersionRequest), ::Hash) — The body resource for this request 
  * **zone** (::String) — Name of the zone for this request. Zone name should conform to RFC1035. 



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
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetVersionReservationSubBlockRequest.new
    
    # Call the get_version method.
    result = client.get_version request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ReservationSubBlocks REST client object.

**Yields**

  * (config) — Configure the ReservationSubBlocks client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocks-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::ReservationSubBlock>
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, parent_name: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::ReservationSubBlock>

Retrieves a list of reservation subBlocks under a single reservation.

**Overloads**
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::ReservationSubBlock>

Pass arguments to `list` via a request object, either of type [ListReservationSubBlocksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListReservationSubBlocksRequest "Google::Cloud::Compute::V1::ListReservationSubBlocksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListReservationSubBlocksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListReservationSubBlocksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, parent_name: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::ReservationSubBlock>

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
  * **parent_name** (::String) — The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name} 
  * **project** (::String) — Project ID for this request. 
  * **zone** (::String) — Name of the zone for this request. Zone name should conform to RFC1035. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::ReservationSubBlock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::ReservationSubBlock](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlock)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListReservationSubBlocksRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Compute::V1::ReservationSubBlocksListResponse.
    p result

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #perform_maintenance
    
    
    def perform_maintenance(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def perform_maintenance(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Allows customers to perform maintenance on a reservation subBlock

**Overloads**
    
    
    def perform_maintenance(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `perform_maintenance` via a request object, either of type [PerformMaintenanceReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PerformMaintenanceReservationSubBlockRequest "Google::Cloud::Compute::V1::PerformMaintenanceReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::PerformMaintenanceReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-PerformMaintenanceReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def perform_maintenance(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `perform_maintenance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_name** (::String) — The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name} 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **reservation_sub_block** (::String) — The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID. 
  * **zone** (::String) — Name of the zone for this request. Zone name should conform to RFC1035. 



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
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::PerformMaintenanceReservationSubBlockRequest.new
    
    # Call the perform_maintenance method.
    result = client.perform_maintenance request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #report_faulty
    
    
    def report_faulty(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def report_faulty(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, reservation_sub_blocks_report_faulty_request_resource: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Allows customers to report a faulty subBlock.

**Overloads**
    
    
    def report_faulty(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `report_faulty` via a request object, either of type [Google::Cloud::Compute::V1::ReportFaultyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReportFaultyReservationSubBlockRequest "Google::Cloud::Compute::V1::ReportFaultyReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ReportFaultyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReportFaultyReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def report_faulty(parent_name: nil, project: nil, request_id: nil, reservation_sub_block: nil, reservation_sub_blocks_report_faulty_request_resource: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `report_faulty` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_name** (::String) — The name of the parent reservation and parent block. In the format of reservations/{reservation_name}/reservationBlocks/{reservation_block_name} 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **reservation_sub_block** (::String) — The name of the reservation subBlock. Name should conform to RFC1035 or be a resource ID. 
  * **reservation_sub_blocks_report_faulty_request_resource** ([::Google::Cloud::Compute::V1::ReservationSubBlocksReportFaultyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ReservationSubBlocksReportFaultyRequest), ::Hash) — The body resource for this request 
  * **zone** (::String) — Name of the zone for this request. Zone name should conform to RFC1035. 



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
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ReportFaultyReservationSubBlockRequest.new
    
    # Call the report_faulty method.
    result = client.report_faulty request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Cloud::Compute::V1::Policy
    def set_iam_policy(parent_resource: nil, project: nil, resource: nil, zone: nil, zone_set_nested_policy_request_resource: nil) -> ::Google::Cloud::Compute::V1::Policy

Sets the access control policy on the specified resource. Replaces any existing policy.

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Cloud::Compute::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [SetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetIamPolicyReservationSubBlockRequest "Google::Cloud::Compute::V1::SetIamPolicyReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::SetIamPolicyReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetIamPolicyReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def set_iam_policy(parent_resource: nil, project: nil, resource: nil, zone: nil, zone_set_nested_policy_request_resource: nil) -> ::Google::Cloud::Compute::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_resource** (::String) — Name or id of parent resource of the resource for this request. 
  * **project** (::String) — Project ID for this request. 
  * **resource** (::String) — Name or id of the resource for this request. 
  * **zone** (::String) — The name of the zone for this request. 
  * **zone_set_nested_policy_request_resource** ([::Google::Cloud::Compute::V1::ZoneSetNestedPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ZoneSetNestedPolicyRequest), ::Hash) — The body resource for this request 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::SetIamPolicyReservationSubBlockRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Cloud::Compute::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse
    def test_iam_permissions(parent_resource: nil, project: nil, resource: nil, test_permissions_request_resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Returns permissions that a caller has on the specified resource.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [TestIamPermissionsReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsReservationSubBlockRequest "Google::Cloud::Compute::V1::TestIamPermissionsReservationSubBlockRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::TestIamPermissionsReservationSubBlockRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsReservationSubBlockRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def test_iam_permissions(parent_resource: nil, project: nil, resource: nil, test_permissions_request_resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent_resource** (::String) — Name or id of parent resource of the resource for this request. 
  * **project** (::String) — Project ID for this request. 
  * **resource** (::String) — Name or id of the resource for this request. 
  * **test_permissions_request_resource** ([::Google::Cloud::Compute::V1::TestPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestPermissionsRequest), ::Hash) — The body resource for this request 
  * **zone** (::String) — The name of the zone for this request. 



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
    client = Google::Cloud::Compute::V1::ReservationSubBlocks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::TestIamPermissionsReservationSubBlockRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Cloud::Compute::V1::TestPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #zone_operations
    
    
    def zone_operations() -> ::Google::Cloud::Compute::V1::ZoneOperations::Rest::Client

Get the associated client for long-running operations via ZoneOperations.

**Returns**

  * ([::Google::Cloud::Compute::V1::ZoneOperations::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ZoneOperations-Rest-Client)) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
