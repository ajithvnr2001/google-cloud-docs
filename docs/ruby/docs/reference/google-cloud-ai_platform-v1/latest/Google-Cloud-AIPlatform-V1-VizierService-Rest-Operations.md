---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::VizierService::Rest::Operations (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:41:42.055975+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::VizierService::Rest::Operations (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::VizierService::Rest::Operations (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::VizierService::Rest::Operations.

Service that implements Longrunning Operations API.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Operations::Configuration

Configuration for the VizierService Operations API.

**Yields**

  * (config) — Configure the Operations client. 



**Yield Parameter**

  * **config** ([Operations::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations-Configuration)) 



**Returns**

  * ([Operations::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations-Configuration)) 



### #cancel_operation
    
    
    def cancel_operation(request, options = nil) -> ::Google::Protobuf::Empty
    def cancel_operation(name: nil) -> ::Google::Protobuf::Empty

Starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an [Operation.error](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_error_instance_ "Google::Longrunning::Operation#error \(method\)") value with a [google.rpc.Status.code](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Rpc-Status#Google__Rpc__Status_code_instance_ "Google::Rpc::Status#code \(method\)") of `1`, corresponding to `Code.CANCELLED`.

**Overloads**
    
    
    def cancel_operation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel_operation` via a request object, either of type [Longrunning::CancelOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-CancelOperationRequest "Google::Longrunning::CancelOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Longrunning::CancelOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-CancelOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def cancel_operation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — The name of the operation resource to be cancelled. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/longrunning"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Longrunning::Operations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Longrunning::CancelOperationRequest.new
    
    # Call the cancel_operation method.
    result = client.cancel_operation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Operations::Configuration

Configure the VizierService Operations instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Operations.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations#Google__Cloud__AIPlatform__V1__VizierService__Rest__Operations_configure_class_ "Google::Cloud::AIPlatform::V1::VizierService::Rest::Operations.configure \(method\)").

**Yields**

  * (config) — Configure the Operations client. 



**Yield Parameter**

  * **config** ([Operations::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations-Configuration)) 



**Returns**

  * ([Operations::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations-Configuration)) 



### #delete_operation
    
    
    def delete_operation(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_operation(name: nil) -> ::Google::Protobuf::Empty

Deletes a long-running operation. This method indicates that the client is no longer interested in the operation result. It does not cancel the operation. If the server doesn't support this method, it returns `google.rpc.Code.UNIMPLEMENTED`.

**Overloads**
    
    
    def delete_operation(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_operation` via a request object, either of type [Longrunning::DeleteOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-DeleteOperationRequest "Google::Longrunning::DeleteOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Longrunning::DeleteOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-DeleteOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_operation(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — The name of the operation resource to be deleted. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/longrunning"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Longrunning::Operations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Longrunning::DeleteOperationRequest.new
    
    # Call the delete_operation method.
    result = client.delete_operation request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_operation
    
    
    def get_operation(request, options = nil) -> ::Gapic::Operation
    def get_operation(name: nil) -> ::Gapic::Operation

Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

**Overloads**
    
    
    def get_operation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `get_operation` via a request object, either of type [Longrunning::GetOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-GetOperationRequest "Google::Longrunning::GetOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Longrunning::GetOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-GetOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_operation(name: nil) -> ::Gapic::Operation

Pass arguments to `get_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — The name of the operation resource. 



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
    
    
    require "google/longrunning"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Longrunning::Operations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Longrunning::GetOperationRequest.new
    
    # Call the get_operation method.
    result = client.get_operation request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Operations

Create a new Operations client object.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Operations::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations-Configuration)) 



**Returns**

  * ([Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-VizierService-Rest-Operations)) — a new instance of Operations 



### #list_operations
    
    
    def list_operations(request, options = nil) -> ::Gapic::Operation
    def list_operations(name: nil, filter: nil, page_size: nil, page_token: nil, return_partial_success: nil) -> ::Gapic::Operation

Lists operations that match the specified filter in the request. If the server doesn't support this method, it returns `UNIMPLEMENTED`.

**Overloads**
    
    
    def list_operations(request, options = nil) -> ::Gapic::Operation

Pass arguments to `list_operations` via a request object, either of type [Longrunning::ListOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-ListOperationsRequest "Google::Longrunning::ListOperationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Longrunning::ListOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-ListOperationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_operations(name: nil, filter: nil, page_size: nil, page_token: nil, return_partial_success: nil) -> ::Gapic::Operation

Pass arguments to `list_operations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the operation's parent resource. 
  * **filter** (::String) — The standard list filter. 
  * **page_size** (::Integer) — The standard list page size. 
  * **page_token** (::String) — The standard list page token. 
  * **return_partial_success** (::Boolean) — When set to `true`, operations that are reachable are returned as normal, and those that are unreachable are returned in the [ListOperationsResponse.unreachable] field.

This can only be `true` when reading across collections e.g. when `parent` is set to `"projects/example/locations/-"`.

This field is not by default supported and will result in an `UNIMPLEMENTED` error if set unless explicitly documented otherwise in service or product specific documentation. 




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
    
    
    require "google/longrunning"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Longrunning::Operations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Longrunning::ListOperationsRequest.new
    
    # Call the list_operations method.
    result = client.list_operations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Longrunning::Operation.
      p item
    end

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #wait_operation
    
    
    def wait_operation(request, options = nil) -> ::Gapic::Operation
    def wait_operation(name: nil, timeout: nil) -> ::Gapic::Operation

Waits until the specified long-running operation is done or reaches at most a specified timeout, returning the latest state. If the operation is already done, the latest state is immediately returned. If the timeout specified is greater than the default HTTP/RPC timeout, the HTTP/RPC timeout is used. If the server does not support this method, it returns `google.rpc.Code.UNIMPLEMENTED`. Note that this method is on a best-effort basis. It may return the latest state before the specified timeout (including immediately), meaning even an immediate response is no guarantee that the operation is done.

**Overloads**
    
    
    def wait_operation(request, options = nil) -> ::Gapic::Operation

Pass arguments to `wait_operation` via a request object, either of type [Longrunning::WaitOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-WaitOperationRequest "Google::Longrunning::WaitOperationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Longrunning::WaitOperationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Longrunning-WaitOperationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def wait_operation(name: nil, timeout: nil) -> ::Gapic::Operation

Pass arguments to `wait_operation` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — The name of the operation resource to wait on. 
  * **timeout** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-Duration), ::Hash) — The maximum duration to wait before timing out. If left blank, the wait will be at most the time permitted by the underlying HTTP/RPC protocol. If RPC context deadline is also specified, the shorter one will be used. 



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
    
    
    require "google/longrunning"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Longrunning::Operations::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Longrunning::WaitOperationRequest.new
    
    # Call the wait_operation method.
    result = client.wait_operation request
    
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
