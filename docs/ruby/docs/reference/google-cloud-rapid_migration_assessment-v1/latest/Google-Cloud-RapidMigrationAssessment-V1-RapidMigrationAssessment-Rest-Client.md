---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client/
title: Rapid Migration Assessment V1 API - Class Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client (v2.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:31.770795+00:00
---

# Rapid Migration Assessment V1 API - Class Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client (v2.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Rapid Migration Assessment V1 API - Class Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client (v2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.0 (latest)  2.5.1  2.4.0  2.3.1  2.2.0  2.1.0  2.0.2  1.2.0  1.1.0  1.0.1  0.4.0  0.3.2  0.2.1  0.1.0 

Reference documentation and code samples for the Rapid Migration Assessment V1 API class Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.

REST client for the RapidMigrationAssessment service.

Service describing handlers for resources.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the RapidMigrationAssessment Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration "Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all RapidMigrationAssessment clients
    ::Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the RapidMigrationAssessment Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client#Google__Cloud__RapidMigrationAssessment__V1__RapidMigrationAssessment__Rest__Client_configure_class_ "Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration "Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration)) 



### #create_annotation
    
    
    def create_annotation(request, options = nil) -> ::Gapic::Operation
    def create_annotation(parent: nil, annotation: nil, request_id: nil) -> ::Gapic::Operation

Creates an Annotation

**Overloads**
    
    
    def create_annotation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_annotation` via a request object, either of type [CreateAnnotationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-CreateAnnotationRequest "Google::Cloud::RapidMigrationAssessment::V1::CreateAnnotationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::CreateAnnotationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-CreateAnnotationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_annotation(parent: nil, annotation: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_annotation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Name of the parent (project+location). 
  * **annotation** ([::Google::Cloud::RapidMigrationAssessment::V1::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Annotation), ::Hash) — Required. The resource being created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. 



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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::CreateAnnotationRequest.new
    
    # Call the create_annotation method.
    result = client.create_annotation request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_collector
    
    
    def create_collector(request, options = nil) -> ::Gapic::Operation
    def create_collector(parent: nil, collector_id: nil, collector: nil, request_id: nil) -> ::Gapic::Operation

Create a Collector to manage the on-prem appliance which collects information about Customer assets.

**Overloads**
    
    
    def create_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_collector` via a request object, either of type [CreateCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-CreateCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::CreateCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::CreateCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-CreateCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_collector(parent: nil, collector_id: nil, collector: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Name of the parent (project+location). 
  * **collector_id** (::String) — Required. Id of the requesting object. 
  * **collector** ([::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector), ::Hash) — Required. The resource being created. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. 



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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::CreateCollectorRequest.new
    
    # Call the create_collector method.
    result = client.create_collector request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_collector
    
    
    def delete_collector(request, options = nil) -> ::Gapic::Operation
    def delete_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Collector - changes state of collector to "Deleting". Background jobs does final deletion through producer API.

**Overloads**
    
    
    def delete_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_collector` via a request object, either of type [DeleteCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-DeleteCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::DeleteCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::DeleteCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-DeleteCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::DeleteCollectorRequest.new
    
    # Call the delete_collector method.
    result = client.delete_collector request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_annotation
    
    
    def get_annotation(request, options = nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Annotation
    def get_annotation(name: nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Annotation

Gets details of a single Annotation.

**Overloads**
    
    
    def get_annotation(request, options = nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Annotation

Pass arguments to `get_annotation` via a request object, either of type [GetAnnotationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-GetAnnotationRequest "Google::Cloud::RapidMigrationAssessment::V1::GetAnnotationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::GetAnnotationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-GetAnnotationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_annotation(name: nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Annotation

Pass arguments to `get_annotation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::RapidMigrationAssessment::V1::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Annotation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::RapidMigrationAssessment::V1::Annotation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Annotation)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::GetAnnotationRequest.new
    
    # Call the get_annotation method.
    result = client.get_annotation request
    
    # The returned object is of type Google::Cloud::RapidMigrationAssessment::V1::Annotation.
    p result

### #get_collector
    
    
    def get_collector(request, options = nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Collector
    def get_collector(name: nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Collector

Gets details of a single Collector.

**Overloads**
    
    
    def get_collector(request, options = nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Collector

Pass arguments to `get_collector` via a request object, either of type [GetCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-GetCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::GetCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::GetCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-GetCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_collector(name: nil) -> ::Google::Cloud::RapidMigrationAssessment::V1::Collector

Pass arguments to `get_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::GetCollectorRequest.new
    
    # Call the get_collector method.
    result = client.get_collector request
    
    # The returned object is of type Google::Cloud::RapidMigrationAssessment::V1::Collector.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new RapidMigrationAssessment REST client object.

**Yields**

  * (config) — Configure the RapidMigrationAssessment client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_collectors
    
    
    def list_collectors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::RapidMigrationAssessment::V1::Collector>
    def list_collectors(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::RapidMigrationAssessment::V1::Collector>

Lists Collectors in a given project and location.

**Overloads**
    
    
    def list_collectors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::RapidMigrationAssessment::V1::Collector>

Pass arguments to `list_collectors` via a request object, either of type [ListCollectorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-ListCollectorsRequest "Google::Cloud::RapidMigrationAssessment::V1::ListCollectorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::ListCollectorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-ListCollectorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_collectors(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::RapidMigrationAssessment::V1::Collector>

Pass arguments to `list_collectors` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value for ListCollectorsRequest. 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — A token identifying a page of results the server should return. 
  * **filter** (::String) — Filtering results. 
  * **order_by** (::String) — Hint for how to order the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::ListCollectorsRequest.new
    
    # Call the list_collectors method.
    result = client.list_collectors request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::RapidMigrationAssessment::V1::Collector.
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
    
    
    def operations_client() -> ::Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RapidMigrationAssessment-Rest-Operations)) 



### #pause_collector
    
    
    def pause_collector(request, options = nil) -> ::Gapic::Operation
    def pause_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Pauses the given collector.

**Overloads**
    
    
    def pause_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `pause_collector` via a request object, either of type [PauseCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-PauseCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::PauseCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::PauseCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-PauseCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def pause_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `pause_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::PauseCollectorRequest.new
    
    # Call the pause_collector method.
    result = client.pause_collector request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #register_collector
    
    
    def register_collector(request, options = nil) -> ::Gapic::Operation
    def register_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Registers the given collector.

**Overloads**
    
    
    def register_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `register_collector` via a request object, either of type [Google::Cloud::RapidMigrationAssessment::V1::RegisterCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RegisterCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::RegisterCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::RegisterCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-RegisterCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def register_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `register_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::RegisterCollectorRequest.new
    
    # Call the register_collector method.
    result = client.register_collector request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #resume_collector
    
    
    def resume_collector(request, options = nil) -> ::Gapic::Operation
    def resume_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Resumes the given collector.

**Overloads**
    
    
    def resume_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `resume_collector` via a request object, either of type [Google::Cloud::RapidMigrationAssessment::V1::ResumeCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-ResumeCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::ResumeCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::ResumeCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-ResumeCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def resume_collector(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `resume_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::ResumeCollectorRequest.new
    
    # Call the resume_collector method.
    result = client.resume_collector request
    
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



### #update_collector
    
    
    def update_collector(request, options = nil) -> ::Gapic::Operation
    def update_collector(update_mask: nil, collector: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single Collector.

**Overloads**
    
    
    def update_collector(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_collector` via a request object, either of type [UpdateCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-UpdateCollectorRequest "Google::Cloud::RapidMigrationAssessment::V1::UpdateCollectorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::RapidMigrationAssessment::V1::UpdateCollectorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-UpdateCollectorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_collector(update_mask: nil, collector: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_collector` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the Collector resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then all fields will be overwritten. 
  * **collector** ([::Google::Cloud::RapidMigrationAssessment::V1::Collector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-rapid_migration_assessment-v1/latest/Google-Cloud-RapidMigrationAssessment-V1-Collector), ::Hash) — Required. The resource being updated. 
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
    
    
    require "google/cloud/rapid_migration_assessment/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::RapidMigrationAssessment::V1::RapidMigrationAssessment::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::RapidMigrationAssessment::V1::UpdateCollectorRequest.new
    
    # Call the update_collector method.
    result = client.update_collector request
    
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

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
