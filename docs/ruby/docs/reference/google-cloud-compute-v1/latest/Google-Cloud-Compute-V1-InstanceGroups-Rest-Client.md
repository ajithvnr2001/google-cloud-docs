---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InstanceGroups::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:35:58.888806+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InstanceGroups::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::InstanceGroups::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.

REST client for the InstanceGroups service.

The InstanceGroups API.

This client uses InstanceGroups version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the InstanceGroups Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration "Google::Cloud::Compute::V1::InstanceGroups::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all InstanceGroups clients
    ::Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #add_instances
    
    
    def add_instances(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def add_instances(instance_group: nil, instance_groups_add_instances_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Adds a list of instances to the specified instance group. All of the instances in the instance group must be in the same network/subnetwork. Read Adding instances for more information.

**Overloads**
    
    
    def add_instances(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `add_instances` via a request object, either of type [AddInstancesInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AddInstancesInstanceGroupRequest "Google::Cloud::Compute::V1::AddInstancesInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::AddInstancesInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AddInstancesInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def add_instances(instance_group: nil, instance_groups_add_instances_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `add_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group** (::String) — The name of the instance group where you are adding instances. 
  * **instance_groups_add_instances_request_resource** ([::Google::Cloud::Compute::V1::InstanceGroupsAddInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupsAddInstancesRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **zone** (::String) — The name of the zone where the instance group is located. 



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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::AddInstancesInstanceGroupRequest.new
    
    # Call the add_instances method.
    result = client.add_instances request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #aggregated_list
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>

Retrieves the list of instance groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

**Overloads**
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>

Pass arguments to `aggregated_list` via a request object, either of type [AggregatedListInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListInstanceGroupsRequest "Google::Cloud::Compute::V1::AggregatedListInstanceGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::AggregatedListInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListInstanceGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>

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

  * **result** (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::InstanceGroupsScopedList>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::AggregatedListInstanceGroupsRequest.new
    
    # Call the aggregated_list method.
    result = client.aggregated_list request
    
    # The returned object is of type Google::Cloud::Compute::V1::InstanceGroupAggregatedList.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the InstanceGroups Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client#Google__Cloud__Compute__V1__InstanceGroups__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration "Google::Cloud::Compute::V1::InstanceGroups::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration)) 



### #delete
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def delete(instance_group: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Deletes the specified instance group. The instances in the group are not deleted. Note that instance group must not belong to a backend service. Read Deleting an instance group for more information.

**Overloads**
    
    
    def delete(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via a request object, either of type [DeleteInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteInstanceGroupRequest "Google::Cloud::Compute::V1::DeleteInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::DeleteInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-DeleteInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete(instance_group: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `delete` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group** (::String) — The name of the instance group to delete. 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **zone** (::String) — The name of the zone where the instance group is located. 



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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::DeleteInstanceGroupRequest.new
    
    # Call the delete method.
    result = client.delete request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::InstanceGroup
    def get(instance_group: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::InstanceGroup

Returns the specified zonal instance group. Get a list of available zonal instance groups by making a list() request.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::InstanceGroup

Pass arguments to `get` via a request object, either of type [GetInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetInstanceGroupRequest "Google::Cloud::Compute::V1::GetInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(instance_group: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::InstanceGroup

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group** (::String) — The name of the instance group. 
  * **project** (::String) — Project ID for this request. 
  * **zone** (::String) — The name of the zone where the instance group is located. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::InstanceGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::InstanceGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetInstanceGroupRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::InstanceGroup.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new InstanceGroups REST client object.

**Yields**

  * (config) — Configure the InstanceGroups client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroups-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #insert
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def insert(instance_group_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Creates an instance group in the specified project using the parameters that are included in the request.

**Overloads**
    
    
    def insert(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via a request object, either of type [Google::Cloud::Compute::V1::InsertInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertInstanceGroupRequest "Google::Cloud::Compute::V1::InsertInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::InsertInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InsertInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def insert(instance_group_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `insert` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group_resource** ([::Google::Cloud::Compute::V1::InstanceGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroup), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **zone** (::String) — The name of the zone where you want to create the instance group. 



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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::InsertInstanceGroupRequest.new
    
    # Call the insert method.
    result = client.insert request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #list
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceGroup>
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceGroup>

Retrieves the list of zonal instance group resources contained within the specified zone.

For managed instance groups, use theinstanceGroupManagers or regionInstanceGroupManagers methods instead.

**Overloads**
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceGroup>

Pass arguments to `list` via a request object, either of type [ListInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListInstanceGroupsRequest "Google::Cloud::Compute::V1::ListInstanceGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListInstanceGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceGroup>

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
  * **zone** (::String) — The name of thezone where the instance group is located. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::InstanceGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::InstanceGroup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListInstanceGroupsRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Compute::V1::InstanceGroupList.
    p result

### #list_instances
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceWithNamedPorts>
    def list_instances(filter: nil, instance_group: nil, instance_groups_list_instances_request_resource: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceWithNamedPorts>

Lists the instances in the specified instance group. The orderBy query parameter is not supported. The filter query parameter is supported, but only for expressions that use `eq` (equal) or `ne` (not equal) operators.

**Overloads**
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceWithNamedPorts>

Pass arguments to `list_instances` via a request object, either of type [ListInstancesInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListInstancesInstanceGroupsRequest "Google::Cloud::Compute::V1::ListInstancesInstanceGroupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListInstancesInstanceGroupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListInstancesInstanceGroupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_instances(filter: nil, instance_group: nil, instance_groups_list_instances_request_resource: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::InstanceWithNamedPorts>

Pass arguments to `list_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

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

  * **instance_group** (::String) — The name of the instance group from which you want to generate a list of included instances. 
  * **instance_groups_list_instances_request_resource** ([::Google::Cloud::Compute::V1::InstanceGroupsListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupsListInstancesRequest), ::Hash) — The body resource for this request 
  * **max_results** (::Integer) — The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`) 
  * **order_by** (::String) — Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.

You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.

Currently, only sorting by `name` or `creationTimestamp desc` is supported. 

  * **page_token** (::String) — Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results. 
  * **project** (::String) — Project ID for this request. 
  * **zone** (::String) — The name of the zone where the instance group is located. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::InstanceWithNamedPorts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceWithNamedPorts)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::InstanceWithNamedPorts](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceWithNamedPorts)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListInstancesInstanceGroupsRequest.new
    
    # Call the list_instances method.
    result = client.list_instances request
    
    # The returned object is of type Google::Cloud::Compute::V1::InstanceGroupsListInstances.
    p result

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #remove_instances
    
    
    def remove_instances(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def remove_instances(instance_group: nil, instance_groups_remove_instances_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Removes one or more instances from the specified instance group, but does not delete those instances.

If the group is part of a backend service that has enabled connection draining, it can take up to 60 seconds after the connection draining duration before the VM instance is removed or deleted.

**Overloads**
    
    
    def remove_instances(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `remove_instances` via a request object, either of type [RemoveInstancesInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RemoveInstancesInstanceGroupRequest "Google::Cloud::Compute::V1::RemoveInstancesInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::RemoveInstancesInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-RemoveInstancesInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def remove_instances(instance_group: nil, instance_groups_remove_instances_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `remove_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group** (::String) — The name of the instance group where the specified instances will be removed. 
  * **instance_groups_remove_instances_request_resource** ([::Google::Cloud::Compute::V1::InstanceGroupsRemoveInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupsRemoveInstancesRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **zone** (::String) — The name of the zone where the instance group is located. 



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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::RemoveInstancesInstanceGroupRequest.new
    
    # Call the remove_instances method.
    result = client.remove_instances request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #set_named_ports
    
    
    def set_named_ports(request, options = nil) -> ::Gapic::GenericLRO::Operation
    def set_named_ports(instance_group: nil, instance_groups_set_named_ports_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Sets the named ports for the specified instance group.

**Overloads**
    
    
    def set_named_ports(request, options = nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `set_named_ports` via a request object, either of type [SetNamedPortsInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetNamedPortsInstanceGroupRequest "Google::Cloud::Compute::V1::SetNamedPortsInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::SetNamedPortsInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-SetNamedPortsInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def set_named_ports(instance_group: nil, instance_groups_set_named_ports_request_resource: nil, project: nil, request_id: nil, zone: nil) -> ::Gapic::GenericLRO::Operation

Pass arguments to `set_named_ports` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance_group** (::String) — The name of the instance group where the named ports are updated. 
  * **instance_groups_set_named_ports_request_resource** ([::Google::Cloud::Compute::V1::InstanceGroupsSetNamedPortsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceGroupsSetNamedPortsRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **request_id** (::String) — An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **zone** (::String) — The name of the zone where the instance group is located. 



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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::SetNamedPortsInstanceGroupRequest.new
    
    # Call the set_named_ports method.
    result = client.set_named_ports request
    
    # The returned object is of type Google::Cloud::Compute::V1::Operation.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse
    def test_iam_permissions(project: nil, resource: nil, test_permissions_request_resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Returns permissions that a caller has on the specified resource.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [TestIamPermissionsInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsInstanceGroupRequest "Google::Cloud::Compute::V1::TestIamPermissionsInstanceGroupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::TestIamPermissionsInstanceGroupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-TestIamPermissionsInstanceGroupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def test_iam_permissions(project: nil, resource: nil, test_permissions_request_resource: nil, zone: nil) -> ::Google::Cloud::Compute::V1::TestPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

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
    client = Google::Cloud::Compute::V1::InstanceGroups::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::TestIamPermissionsInstanceGroupRequest.new
    
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
