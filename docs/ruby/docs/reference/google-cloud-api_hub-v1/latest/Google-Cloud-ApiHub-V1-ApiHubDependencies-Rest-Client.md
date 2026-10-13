---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:40.496053+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.

REST client for the ApiHubDependencies service.

This service provides methods for various operations related to a [Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency "Google::Cloud::ApiHub::V1::Dependency \(class\)") in the API hub.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApiHub::V1::ApiHubDependencies::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ApiHubDependencies Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration "Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ApiHubDependencies clients
    ::Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ApiHubDependencies Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client#Google__Cloud__ApiHub__V1__ApiHubDependencies__Rest__Client_configure_class_ "Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration "Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration)) 



### #create_dependency
    
    
    def create_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency
    def create_dependency(parent: nil, dependency_id: nil, dependency: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Create a dependency between two entities in the API hub.

**Overloads**
    
    
    def create_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `create_dependency` via a request object, either of type [CreateDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CreateDependencyRequest "Google::Cloud::ApiHub::V1::CreateDependencyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::CreateDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CreateDependencyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_dependency(parent: nil, dependency_id: nil, dependency: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `create_dependency` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource for the dependency resource. Format: `projects/{project}/locations/{location}`
  * **dependency_id** (::String) — Optional. The ID to use for the dependency resource, which will become the final component of the dependency's resource name. This field is optional.

    * If provided, the same will be used. The service will throw an error if duplicate id is provided by the client.
    * If not provided, a system generated id will be used.

This value should be 4-500 characters, and valid characters are `[a-z][A-Z][0-9]-_`. 

  * **dependency** ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency), ::Hash) — Required. The dependency resource to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::CreateDependencyRequest.new
    
    # Call the create_dependency method.
    result = client.create_dependency request
    
    # The returned object is of type Google::Cloud::ApiHub::V1::Dependency.
    p result

### #delete_dependency
    
    
    def delete_dependency(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_dependency(name: nil) -> ::Google::Protobuf::Empty

Delete the dependency resource.

**Overloads**
    
    
    def delete_dependency(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_dependency` via a request object, either of type [DeleteDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DeleteDependencyRequest "Google::Cloud::ApiHub::V1::DeleteDependencyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::DeleteDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-DeleteDependencyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_dependency(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_dependency` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the dependency resource to delete. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::DeleteDependencyRequest.new
    
    # Call the delete_dependency method.
    result = client.delete_dependency request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_dependency
    
    
    def get_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency
    def get_dependency(name: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Get details about a dependency resource in the API hub.

**Overloads**
    
    
    def get_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `get_dependency` via a request object, either of type [GetDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-GetDependencyRequest "Google::Cloud::ApiHub::V1::GetDependencyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::GetDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-GetDependencyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_dependency(name: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `get_dependency` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the dependency resource to retrieve. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::GetDependencyRequest.new
    
    # Call the get_dependency method.
    result = client.get_dependency request
    
    # The returned object is of type Google::Cloud::ApiHub::V1::Dependency.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ApiHubDependencies REST client object.

**Yields**

  * (config) — Configure the ApiHubDependencies client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubDependencies-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_dependencies
    
    
    def list_dependencies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiHub::V1::Dependency>
    def list_dependencies(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiHub::V1::Dependency>

List dependencies based on the provided filter and pagination parameters.

**Overloads**
    
    
    def list_dependencies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiHub::V1::Dependency>

Pass arguments to `list_dependencies` via a request object, either of type [ListDependenciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListDependenciesRequest "Google::Cloud::ApiHub::V1::ListDependenciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::ListDependenciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ListDependenciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_dependencies(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiHub::V1::Dependency>

Pass arguments to `list_dependencies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of dependency resources. Format: `projects/{project}/locations/{location}`
  * **filter** (::String) — Optional. An expression that filters the list of Dependencies.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string. Allowed comparison operator is `=`. Filters are not case sensitive.

The following fields in the `Dependency` are eligible for filtering:

    * `consumer.operation_resource_name` \- The operation resource name for the consumer entity involved in a dependency. Allowed comparison operators: `=`.
    * `consumer.external_api_resource_name` \- The external api resource name for the consumer entity involved in a dependency. Allowed comparison operators: `=`.
    * `supplier.operation_resource_name` \- The operation resource name for the supplier entity involved in a dependency. Allowed comparison operators: `=`.
    * `supplier.external_api_resource_name` \- The external api resource name for the supplier entity involved in a dependency. Allowed comparison operators: `=`.

Expressions are combined with either `AND` logic operator or `OR` logical operator but not both of them together i.e. only one of the `AND` or `OR` operator can be used throughout the filter string and both the operators cannot be used together. No other logical operators are supported. At most three filter fields are allowed in the filter string and if provided more than that then `INVALID_ARGUMENT` error is returned by the API.

For example, `consumer.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\" OR supplier.operation_resource_name = \"projects/p1/locations/global/apis/a1/versions/v1/operations/o1\"` \- The dependencies with either consumer or supplier operation resource name as _projects/p1/locations/global/apis/a1/versions/v1/operations/o1_. 

  * **page_size** (::Integer) — Optional. The maximum number of dependency resources to return. The service may return fewer than this value. If unspecified, at most 50 dependencies will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListDependencies` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListDependencies` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::ListDependenciesRequest.new
    
    # Call the list_dependencies method.
    result = client.list_dependencies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApiHub::V1::Dependency.
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



### #update_dependency
    
    
    def update_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency
    def update_dependency(dependency: nil, update_mask: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Update a dependency based on the [update_mask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-UpdateDependencyRequest#Google__Cloud__ApiHub__V1__UpdateDependencyRequest_update_mask_instance_ "Google::Cloud::ApiHub::V1::UpdateDependencyRequest#update_mask \(method\)") provided in the request.

The following fields in the [dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency "Google::Cloud::ApiHub::V1::Dependency \(class\)") can be updated:

  * [description](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency#Google__Cloud__ApiHub__V1__Dependency_description_instance_ "Google::Cloud::ApiHub::V1::Dependency#description \(method\)")



**Overloads**
    
    
    def update_dependency(request, options = nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `update_dependency` via a request object, either of type [UpdateDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-UpdateDependencyRequest "Google::Cloud::ApiHub::V1::UpdateDependencyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::UpdateDependencyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-UpdateDependencyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_dependency(dependency: nil, update_mask: nil) -> ::Google::Cloud::ApiHub::V1::Dependency

Pass arguments to `update_dependency` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **dependency** ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency), ::Hash) — Required. The dependency resource to update.

The dependency's `name` field is used to identify the dependency to update. Format: `projects/{project}/locations/{location}/dependencies/{dependency}`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiHub::V1::Dependency](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-Dependency)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubDependencies::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::UpdateDependencyRequest.new
    
    # Call the update_dependency method.
    result = client.update_dependency request
    
    # The returned object is of type Google::Cloud::ApiHub::V1::Dependency.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
