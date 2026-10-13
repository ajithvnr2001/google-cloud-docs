---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:23:53.636106+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.

REST client for the AcceleratorTypes service.

Services

The AcceleratorTypes API.

This client uses AcceleratorTypes version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AcceleratorTypes Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration "Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AcceleratorTypes clients
    ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #aggregated_list
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>

Retrieves an aggregated list of accelerator types.

To prevent failure, it is recommended that you set the `returnPartialSuccess` parameter to `true`.

**Overloads**
    
    
    def aggregated_list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>

Pass arguments to `aggregated_list` via a request object, either of type [Google::Cloud::Compute::V1::AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListAcceleratorTypesRequest "Google::Cloud::Compute::V1::AggregatedListAcceleratorTypesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::AggregatedListAcceleratorTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AggregatedListAcceleratorTypesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def aggregated_list(filter: nil, include_all_scopes: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, service_project_number: nil) -> ::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>

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

  * **result** (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<::String, ::Google::Cloud::Compute::V1::AcceleratorTypesScopedList>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::AggregatedListAcceleratorTypesRequest.new
    
    # Call the aggregated_list method.
    result = client.aggregated_list request
    
    # The returned object is of type Google::Cloud::Compute::V1::AcceleratorTypeAggregatedList.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AcceleratorTypes Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client#Google__Cloud__Compute__V1__AcceleratorTypes__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration "Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration)) 



### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::AcceleratorType
    def get(accelerator_type: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::AcceleratorType

Returns the specified accelerator type.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Compute::V1::AcceleratorType

Pass arguments to `get` via a request object, either of type [GetAcceleratorTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetAcceleratorTypeRequest "Google::Cloud::Compute::V1::GetAcceleratorTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::GetAcceleratorTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-GetAcceleratorTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get(accelerator_type: nil, project: nil, zone: nil) -> ::Google::Cloud::Compute::V1::AcceleratorType

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **accelerator_type** (::String) — Name of the accelerator type to return. 
  * **project** (::String) — Project ID for this request. 
  * **zone** (::String) — The name of the zone for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::AcceleratorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::AcceleratorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::GetAcceleratorTypeRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Compute::V1::AcceleratorType.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AcceleratorTypes REST client object.

**Yields**

  * (config) — Configure the AcceleratorTypes client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorTypes-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::AcceleratorType>
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::AcceleratorType>

Retrieves a list of accelerator types that are available to the specified project.

**Overloads**
    
    
    def list(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::AcceleratorType>

Pass arguments to `list` via a request object, either of type [ListAcceleratorTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListAcceleratorTypesRequest "Google::Cloud::Compute::V1::ListAcceleratorTypesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::ListAcceleratorTypesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-ListAcceleratorTypesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list(filter: nil, max_results: nil, order_by: nil, page_token: nil, project: nil, zone: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Compute::V1::AcceleratorType>

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
  * **zone** (::String) — The name of the zone for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::AcceleratorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Compute::V1::AcceleratorType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-AcceleratorType)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::AcceleratorTypes::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::ListAcceleratorTypesRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Compute::V1::AcceleratorTypeList.
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
