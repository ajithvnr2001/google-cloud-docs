---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client/
title: AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client (v1.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:09.799563+00:00
---

# AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client (v1.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AI Platform Notebooks V1 API - Class Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client (v1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.0 (latest)  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.1  0.11.0  0.10.0  0.9.1  0.8.2  0.7.0  0.6.1  0.5.0  0.4.2  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the AI Platform Notebooks V1 API class Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.

REST client for the ManagedNotebookService service.

API v1 service for Managed Notebooks.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Notebooks::V1::ManagedNotebookService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ManagedNotebookService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration "Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ManagedNotebookService clients
    ::Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ManagedNotebookService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client#Google__Cloud__Notebooks__V1__ManagedNotebookService__Rest__Client_configure_class_ "Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration "Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration)) 



### #create_runtime
    
    
    def create_runtime(request, options = nil) -> ::Gapic::Operation
    def create_runtime(parent: nil, runtime_id: nil, runtime: nil, request_id: nil) -> ::Gapic::Operation

Creates a new Runtime in a given project and location.

**Overloads**
    
    
    def create_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_runtime` via a request object, either of type [CreateRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-CreateRuntimeRequest "Google::Cloud::Notebooks::V1::CreateRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::CreateRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-CreateRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_runtime(parent: nil, runtime_id: nil, runtime: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `parent=projects/{project_id}/locations/{location}`
  * **runtime_id** (::String) — Required. User-defined unique ID of this Runtime. 
  * **runtime** ([::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime), ::Hash) — Required. The Runtime to be created. 
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::CreateRuntimeRequest.new
    
    # Call the create_runtime method.
    result = client.create_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_runtime
    
    
    def delete_runtime(request, options = nil) -> ::Gapic::Operation
    def delete_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Runtime.

**Overloads**
    
    
    def delete_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_runtime` via a request object, either of type [DeleteRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-DeleteRuntimeRequest "Google::Cloud::Notebooks::V1::DeleteRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::DeleteRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-DeleteRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::DeleteRuntimeRequest.new
    
    # Call the delete_runtime method.
    result = client.delete_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #diagnose_runtime
    
    
    def diagnose_runtime(request, options = nil) -> ::Gapic::Operation
    def diagnose_runtime(name: nil, diagnostic_config: nil) -> ::Gapic::Operation

Creates a Diagnostic File and runs Diagnostic Tool given a Runtime.

**Overloads**
    
    
    def diagnose_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `diagnose_runtime` via a request object, either of type [DiagnoseRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-DiagnoseRuntimeRequest "Google::Cloud::Notebooks::V1::DiagnoseRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::DiagnoseRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-DiagnoseRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def diagnose_runtime(name: nil, diagnostic_config: nil) -> ::Gapic::Operation

Pass arguments to `diagnose_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtimes_id}`
  * **diagnostic_config** ([::Google::Cloud::Notebooks::V1::DiagnosticConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-DiagnosticConfig), ::Hash) — Required. Defines flags that are used to run the diagnostic tool 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::DiagnoseRuntimeRequest.new
    
    # Call the diagnose_runtime method.
    result = client.diagnose_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_runtime
    
    
    def get_runtime(request, options = nil) -> ::Google::Cloud::Notebooks::V1::Runtime
    def get_runtime(name: nil) -> ::Google::Cloud::Notebooks::V1::Runtime

Gets details of a single Runtime. The location must be a regional endpoint rather than zonal.

**Overloads**
    
    
    def get_runtime(request, options = nil) -> ::Google::Cloud::Notebooks::V1::Runtime

Pass arguments to `get_runtime` via a request object, either of type [GetRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-GetRuntimeRequest "Google::Cloud::Notebooks::V1::GetRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::GetRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-GetRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_runtime(name: nil) -> ::Google::Cloud::Notebooks::V1::Runtime

Pass arguments to `get_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::GetRuntimeRequest.new
    
    # Call the get_runtime method.
    result = client.get_runtime request
    
    # The returned object is of type Google::Cloud::Notebooks::V1::Runtime.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ManagedNotebookService REST client object.

**Yields**

  * (config) — Configure the ManagedNotebookService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_runtimes
    
    
    def list_runtimes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Notebooks::V1::Runtime>
    def list_runtimes(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Notebooks::V1::Runtime>

Lists Runtimes in a given project and location.

**Overloads**
    
    
    def list_runtimes(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Notebooks::V1::Runtime>

Pass arguments to `list_runtimes` via a request object, either of type [ListRuntimesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ListRuntimesRequest "Google::Cloud::Notebooks::V1::ListRuntimesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::ListRuntimesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ListRuntimesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_runtimes(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Notebooks::V1::Runtime>

Pass arguments to `list_runtimes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: `parent=projects/{project_id}/locations/{location}`
  * **page_size** (::Integer) — Maximum return size of the list call. 
  * **page_token** (::String) — A previous returned page token that can be used to continue listing from the last result. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::ListRuntimesRequest.new
    
    # Call the list_runtimes method.
    result = client.list_runtimes request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Notebooks::V1::Runtime.
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
    
    
    def operations_client() -> ::Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ManagedNotebookService-Rest-Operations)) 



### #refresh_runtime_token_internal
    
    
    def refresh_runtime_token_internal(request, options = nil) -> ::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse
    def refresh_runtime_token_internal(name: nil, vm_id: nil) -> ::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse

Gets an access token for the consumer service account that the customer attached to the runtime. Only accessible from the tenant instance.

**Overloads**
    
    
    def refresh_runtime_token_internal(request, options = nil) -> ::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse

Pass arguments to `refresh_runtime_token_internal` via a request object, either of type [RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RefreshRuntimeTokenInternalRequest "Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RefreshRuntimeTokenInternalRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def refresh_runtime_token_internal(name: nil, vm_id: nil) -> ::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse

Pass arguments to `refresh_runtime_token_internal` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **vm_id** (::String) — Required. The VM hardware token for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RefreshRuntimeTokenInternalResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RefreshRuntimeTokenInternalResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalRequest.new
    
    # Call the refresh_runtime_token_internal method.
    result = client.refresh_runtime_token_internal request
    
    # The returned object is of type Google::Cloud::Notebooks::V1::RefreshRuntimeTokenInternalResponse.
    p result

### #report_runtime_event
    
    
    def report_runtime_event(request, options = nil) -> ::Gapic::Operation
    def report_runtime_event(name: nil, vm_id: nil, event: nil) -> ::Gapic::Operation

Report and process a runtime event.

**Overloads**
    
    
    def report_runtime_event(request, options = nil) -> ::Gapic::Operation

Pass arguments to `report_runtime_event` via a request object, either of type [ReportRuntimeEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ReportRuntimeEventRequest "Google::Cloud::Notebooks::V1::ReportRuntimeEventRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::ReportRuntimeEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ReportRuntimeEventRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def report_runtime_event(name: nil, vm_id: nil, event: nil) -> ::Gapic::Operation

Pass arguments to `report_runtime_event` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **vm_id** (::String) — Required. The VM hardware token for authenticating the VM. https://cloud.google.com/compute/docs/instances/verifying-instance-identity 
  * **event** ([::Google::Cloud::Notebooks::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Event), ::Hash) — Required. The Event to be reported. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::ReportRuntimeEventRequest.new
    
    # Call the report_runtime_event method.
    result = client.report_runtime_event request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #reset_runtime
    
    
    def reset_runtime(request, options = nil) -> ::Gapic::Operation
    def reset_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Resets a Managed Notebook Runtime.

**Overloads**
    
    
    def reset_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reset_runtime` via a request object, either of type [ResetRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ResetRuntimeRequest "Google::Cloud::Notebooks::V1::ResetRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::ResetRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-ResetRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def reset_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `reset_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::ResetRuntimeRequest.new
    
    # Call the reset_runtime method.
    result = client.reset_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #start_runtime
    
    
    def start_runtime(request, options = nil) -> ::Gapic::Operation
    def start_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Starts a Managed Notebook Runtime. Perform "Start" on GPU instances; "Resume" on CPU instances See: <https://cloud.google.com/compute/docs/instances/stop-start-instance> <https://cloud.google.com/compute/docs/instances/suspend-resume-instance>

**Overloads**
    
    
    def start_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `start_runtime` via a request object, either of type [StartRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-StartRuntimeRequest "Google::Cloud::Notebooks::V1::StartRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::StartRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-StartRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def start_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `start_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::StartRuntimeRequest.new
    
    # Call the start_runtime method.
    result = client.start_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #stop_runtime
    
    
    def stop_runtime(request, options = nil) -> ::Gapic::Operation
    def stop_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Stops a Managed Notebook Runtime. Perform "Stop" on GPU instances; "Suspend" on CPU instances See: <https://cloud.google.com/compute/docs/instances/stop-start-instance> <https://cloud.google.com/compute/docs/instances/suspend-resume-instance>

**Overloads**
    
    
    def stop_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `stop_runtime` via a request object, either of type [StopRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-StopRuntimeRequest "Google::Cloud::Notebooks::V1::StopRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::StopRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-StopRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def stop_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `stop_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::StopRuntimeRequest.new
    
    # Call the stop_runtime method.
    result = client.stop_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #switch_runtime
    
    
    def switch_runtime(request, options = nil) -> ::Gapic::Operation
    def switch_runtime(name: nil, machine_type: nil, accelerator_config: nil, request_id: nil) -> ::Gapic::Operation

Switch a Managed Notebook Runtime.

**Overloads**
    
    
    def switch_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `switch_runtime` via a request object, either of type [SwitchRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-SwitchRuntimeRequest "Google::Cloud::Notebooks::V1::SwitchRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::SwitchRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-SwitchRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def switch_runtime(name: nil, machine_type: nil, accelerator_config: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `switch_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **machine_type** (::String) — machine type. 
  * **accelerator_config** ([::Google::Cloud::Notebooks::V1::RuntimeAcceleratorConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-RuntimeAcceleratorConfig), ::Hash) — accelerator config. 
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::SwitchRuntimeRequest.new
    
    # Call the switch_runtime method.
    result = client.switch_runtime request
    
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



### #update_runtime
    
    
    def update_runtime(request, options = nil) -> ::Gapic::Operation
    def update_runtime(runtime: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Update Notebook Runtime configuration.

**Overloads**
    
    
    def update_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_runtime` via a request object, either of type [UpdateRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-UpdateRuntimeRequest "Google::Cloud::Notebooks::V1::UpdateRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::UpdateRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-UpdateRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_runtime(runtime: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **runtime** ([::Google::Cloud::Notebooks::V1::Runtime](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-Runtime), ::Hash) — Required. The Runtime to be updated. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Required. Specifies the path, relative to `Runtime`, of the field to update. For example, to change the software configuration kernels, the `update_mask` parameter would be specified as `software_config.kernels`, and the `PATCH` request body would specify the new value, as follows:
        
        {
          "software_config":{
            "kernels": [{
               'repository':
               'gcr.io/deeplearning-platform-release/pytorch-gpu', 'tag':
               'latest' }],
            }
        }
        

Currently, only the following fields can be updated:

    * `software_config.kernels`
    * `software_config.post_startup_script`
    * `software_config.custom_gpu_driver_path`
    * `software_config.idle_shutdown`
    * `software_config.idle_shutdown_timeout`
    * `software_config.disable_terminal`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::UpdateRuntimeRequest.new
    
    # Call the update_runtime method.
    result = client.update_runtime request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #upgrade_runtime
    
    
    def upgrade_runtime(request, options = nil) -> ::Gapic::Operation
    def upgrade_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Upgrades a Managed Notebook Runtime to the latest version.

**Overloads**
    
    
    def upgrade_runtime(request, options = nil) -> ::Gapic::Operation

Pass arguments to `upgrade_runtime` via a request object, either of type [UpgradeRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-UpgradeRuntimeRequest "Google::Cloud::Notebooks::V1::UpgradeRuntimeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Notebooks::V1::UpgradeRuntimeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-notebooks-v1/latest/Google-Cloud-Notebooks-V1-UpgradeRuntimeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def upgrade_runtime(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `upgrade_runtime` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: `projects/{project_id}/locations/{location}/runtimes/{runtime_id}`
  * **request_id** (::String) — Idempotent request UUID. 



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
    
    
    require "google/cloud/notebooks/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Notebooks::V1::ManagedNotebookService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Notebooks::V1::UpgradeRuntimeRequest.new
    
    # Call the upgrade_runtime method.
    result = client.upgrade_runtime request
    
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
