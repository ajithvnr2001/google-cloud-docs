---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client/
title: Cloud Functions V2 API - Class Google::Cloud::Functions::V2::FunctionService::Rest::Client (v1.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:21.276406+00:00
---

# Cloud Functions V2 API - Class Google::Cloud::Functions::V2::FunctionService::Rest::Client (v1.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Functions V2 API - Class Google::Cloud::Functions::V2::FunctionService::Rest::Client (v1.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.6.1 (latest)  1.6.0  1.5.1  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.0  0.4.1  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Functions V2 API class Google::Cloud::Functions::V2::FunctionService::Rest::Client.

REST client for the FunctionService service.

Google Cloud Functions is used to deploy functions that are executed by Google in response to various events. Data connected with that event is passed to a function as the input data.

A **function** is a resource which describes a function that should be executed and how it is triggered.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Functions::V2::FunctionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the FunctionService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration "Google::Cloud::Functions::V2::FunctionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all FunctionService clients
    ::Google::Cloud::Functions::V2::FunctionService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the FunctionService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client#Google__Cloud__Functions__V2__FunctionService__Rest__Client_configure_class_ "Google::Cloud::Functions::V2::FunctionService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration "Google::Cloud::Functions::V2::FunctionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration)) 



### #create_function
    
    
    def create_function(request, options = nil) -> ::Gapic::Operation
    def create_function(parent: nil, function: nil, function_id: nil) -> ::Gapic::Operation

Creates a new function. If a function with the given name already exists in the specified project, the long running operation will return `ALREADY_EXISTS` error.

**Overloads**
    
    
    def create_function(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_function` via a request object, either of type [CreateFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-CreateFunctionRequest "Google::Cloud::Functions::V2::CreateFunctionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::CreateFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-CreateFunctionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_function(parent: nil, function: nil, function_id: nil) -> ::Gapic::Operation

Pass arguments to `create_function` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location in which the function should be created, specified in the format `projects/*/locations/*`
  * **function** ([::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function), ::Hash) — Required. Function to be created. 
  * **function_id** (::String) — The ID to use for the function, which will become the final component of the function's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. 




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
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::CreateFunctionRequest.new
    
    # Call the create_function method.
    result = client.create_function request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_function
    
    
    def delete_function(request, options = nil) -> ::Gapic::Operation
    def delete_function(name: nil) -> ::Gapic::Operation

Deletes a function with the given name from the specified project. If the given function is used by some trigger, the trigger will be updated to remove this function.

**Overloads**
    
    
    def delete_function(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_function` via a request object, either of type [DeleteFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-DeleteFunctionRequest "Google::Cloud::Functions::V2::DeleteFunctionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::DeleteFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-DeleteFunctionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_function(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_function` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the function which should be deleted. 



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
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::DeleteFunctionRequest.new
    
    # Call the delete_function method.
    result = client.delete_function request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #generate_download_url
    
    
    def generate_download_url(request, options = nil) -> ::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse
    def generate_download_url(name: nil) -> ::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse

Returns a signed URL for downloading deployed function source code. The URL is only valid for a limited period and should be used within 30 minutes of generation. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>

**Overloads**
    
    
    def generate_download_url(request, options = nil) -> ::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse

Pass arguments to `generate_download_url` via a request object, either of type [GenerateDownloadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateDownloadUrlRequest "Google::Cloud::Functions::V2::GenerateDownloadUrlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::GenerateDownloadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateDownloadUrlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def generate_download_url(name: nil) -> ::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse

Pass arguments to `generate_download_url` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of function for which source code Google Cloud Storage signed URL should be generated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateDownloadUrlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Functions::V2::GenerateDownloadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateDownloadUrlResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::GenerateDownloadUrlRequest.new
    
    # Call the generate_download_url method.
    result = client.generate_download_url request
    
    # The returned object is of type Google::Cloud::Functions::V2::GenerateDownloadUrlResponse.
    p result

### #generate_upload_url
    
    
    def generate_upload_url(request, options = nil) -> ::Google::Cloud::Functions::V2::GenerateUploadUrlResponse
    def generate_upload_url(parent: nil, kms_key_name: nil, environment: nil) -> ::Google::Cloud::Functions::V2::GenerateUploadUrlResponse

Returns a signed URL for uploading a function source code. For more information about the signed URL usage see: <https://cloud.google.com/storage/docs/access-control/signed-urls>. Once the function source code upload is complete, the used signed URL should be provided in CreateFunction or UpdateFunction request as a reference to the function source code.

When uploading source code to the generated signed URL, please follow these restrictions:

  * Source file type should be a zip file.
  * No credentials should be attached - the signed URLs provide access to the target bucket using internal service identity; if credentials were attached, the identity from the credentials would be used, but that identity does not have permissions to upload files to the URL.



When making a HTTP PUT request, specify this header:

  * `content-type: application/zip`



Do not specify this header:

  * `Authorization: Bearer YOUR_TOKEN`



**Overloads**
    
    
    def generate_upload_url(request, options = nil) -> ::Google::Cloud::Functions::V2::GenerateUploadUrlResponse

Pass arguments to `generate_upload_url` via a request object, either of type [GenerateUploadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateUploadUrlRequest "Google::Cloud::Functions::V2::GenerateUploadUrlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::GenerateUploadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateUploadUrlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def generate_upload_url(parent: nil, kms_key_name: nil, environment: nil) -> ::Google::Cloud::Functions::V2::GenerateUploadUrlResponse

Pass arguments to `generate_upload_url` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location in which the Google Cloud Storage signed URL should be generated, specified in the format `projects/*/locations/*`. 
  * **kms_key_name** (::String) — Resource name of a KMS crypto key (managed by the user) used to encrypt/decrypt function source code objects in intermediate Cloud Storage buckets. When you generate an upload url and upload your source code, it gets copied to an intermediate Cloud Storage bucket. The source code is then copied to a versioned directory in the sources bucket in the consumer project during the function deployment.

It must match the pattern `projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`.

The Google Cloud Functions service account (service-{project_number}@gcf-admin-robot.iam.gserviceaccount.com) must be granted the role 'Cloud KMS CryptoKey Encrypter/Decrypter (roles/cloudkms.cryptoKeyEncrypterDecrypter)' on the Key/KeyRing/Project/Organization (least access preferred). 

  * **environment** ([::Google::Cloud::Functions::V2::Environment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Environment)) — The function environment the generated upload url will be used for. The upload url for 2nd Gen functions can also be used for 1st gen functions, but not vice versa. If not specified, 2nd generation-style upload URLs are generated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Functions::V2::GenerateUploadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateUploadUrlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Functions::V2::GenerateUploadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GenerateUploadUrlResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::GenerateUploadUrlRequest.new
    
    # Call the generate_upload_url method.
    result = client.generate_upload_url request
    
    # The returned object is of type Google::Cloud::Functions::V2::GenerateUploadUrlResponse.
    p result

### #get_function
    
    
    def get_function(request, options = nil) -> ::Google::Cloud::Functions::V2::Function
    def get_function(name: nil, revision: nil) -> ::Google::Cloud::Functions::V2::Function

Returns a function with the given name from the requested project.

**Overloads**
    
    
    def get_function(request, options = nil) -> ::Google::Cloud::Functions::V2::Function

Pass arguments to `get_function` via a request object, either of type [GetFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GetFunctionRequest "Google::Cloud::Functions::V2::GetFunctionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::GetFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-GetFunctionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_function(name: nil, revision: nil) -> ::Google::Cloud::Functions::V2::Function

Pass arguments to `get_function` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the function which details should be obtained. 
  * **revision** (::String) — Optional. The optional version of the 1st gen function whose details should be obtained. The version of a 1st gen function is an integer that starts from 1 and gets incremented on redeployments. GCF may keep historical configs for old versions of 1st gen function. This field can be specified to fetch the historical configs. This field is valid only for GCF 1st gen function. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::GetFunctionRequest.new
    
    # Call the get_function method.
    result = client.get_function request
    
    # The returned object is of type Google::Cloud::Functions::V2::Function.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new FunctionService REST client object.

**Yields**

  * (config) — Configure the FunctionService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Functions::V2::FunctionService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_functions
    
    
    def list_functions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Functions::V2::Function>
    def list_functions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Functions::V2::Function>

Returns a list of functions that belong to the requested project.

**Overloads**
    
    
    def list_functions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Functions::V2::Function>

Pass arguments to `list_functions` via a request object, either of type [ListFunctionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListFunctionsRequest "Google::Cloud::Functions::V2::ListFunctionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::ListFunctionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListFunctionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_functions(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Functions::V2::Function>

Pass arguments to `list_functions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the function should be listed, specified in the format `projects/*/locations/*` If you want to list functions in all locations, use "-" in place of a location. When listing functions in all locations, if one or more location(s) are unreachable, the response will contain functions from all reachable locations along with the names of any unreachable locations. 
  * **page_size** (::Integer) — Maximum number of functions to return per call. The largest allowed page_size is 1,000, if the page_size is omitted or specified as greater than 1,000 then it will be replaced as 1,000. The size of the list response can be less than specified when used with filters. 
  * **page_token** (::String) — The value returned by the last `ListFunctionsResponse`; indicates that this is a continuation of a prior `ListFunctions` call, and that the system should return the next page of data. 
  * **filter** (::String) — The filter for Functions that match the filter expression, following the syntax outlined in https://google.aip.dev/160. 
  * **order_by** (::String) — The sorting order of the resources returned. Value should be a comma separated list of fields. The default sorting order is ascending. See https://google.aip.dev/132#ordering. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::ListFunctionsRequest.new
    
    # Call the list_functions method.
    result = client.list_functions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Functions::V2::Function.
      p item
    end

### #list_runtimes
    
    
    def list_runtimes(request, options = nil) -> ::Google::Cloud::Functions::V2::ListRuntimesResponse
    def list_runtimes(parent: nil, filter: nil) -> ::Google::Cloud::Functions::V2::ListRuntimesResponse

Returns a list of runtimes that are supported for the requested project.

**Overloads**
    
    
    def list_runtimes(request, options = nil) -> ::Google::Cloud::Functions::V2::ListRuntimesResponse

Pass arguments to `list_runtimes` via a request object, either of type [ListRuntimesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListRuntimesRequest "Google::Cloud::Functions::V2::ListRuntimesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::ListRuntimesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListRuntimesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_runtimes(parent: nil, filter: nil) -> ::Google::Cloud::Functions::V2::ListRuntimesResponse

Pass arguments to `list_runtimes` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location from which the runtimes should be listed, specified in the format `projects/*/locations/*`
  * **filter** (::String) — The filter for Runtimes that match the filter expression, following the syntax outlined in https://google.aip.dev/160. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Functions::V2::ListRuntimesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListRuntimesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Functions::V2::ListRuntimesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-ListRuntimesResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::ListRuntimesRequest.new
    
    # Call the list_runtimes method.
    result = client.list_runtimes request
    
    # The returned object is of type Google::Cloud::Functions::V2::ListRuntimesResponse.
    p result

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
    
    
    def operations_client() -> ::Google::Cloud::Functions::V2::FunctionService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Functions::V2::FunctionService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-FunctionService-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_function
    
    
    def update_function(request, options = nil) -> ::Gapic::Operation
    def update_function(function: nil, update_mask: nil) -> ::Gapic::Operation

Updates existing function.

**Overloads**
    
    
    def update_function(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_function` via a request object, either of type [UpdateFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-UpdateFunctionRequest "Google::Cloud::Functions::V2::UpdateFunctionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Functions::V2::UpdateFunctionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-UpdateFunctionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_function(function: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_function` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **function** ([::Google::Cloud::Functions::V2::Function](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Cloud-Functions-V2-Function), ::Hash) — Required. New version of the function. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-functions-v2/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be updated. If no field mask is provided, all fields will be updated. 



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
    
    
    require "google/cloud/functions/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Functions::V2::FunctionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Functions::V2::UpdateFunctionRequest.new
    
    # Call the update_function method.
    result = client.update_function request
    
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
