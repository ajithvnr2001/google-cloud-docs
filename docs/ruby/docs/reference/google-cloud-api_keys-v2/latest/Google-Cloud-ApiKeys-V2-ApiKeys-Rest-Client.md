---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client/
title: API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client (v0.14.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:52:59.489850+00:00
---

# API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client (v0.14.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API Keys V2 API - Class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client (v0.14.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.14.2 (latest)  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.2  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the API Keys V2 API class Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.

REST client for the ApiKeys service.

Manages the API keys associated with projects.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApiKeys::V2::ApiKeys::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ApiKeys Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration "Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ApiKeys clients
    ::Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ApiKeys Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client#Google__Cloud__ApiKeys__V2__ApiKeys__Rest__Client_configure_class_ "Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration "Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration)) 



### #create_key
    
    
    def create_key(request, options = nil) -> ::Gapic::Operation
    def create_key(parent: nil, key: nil, key_id: nil) -> ::Gapic::Operation

Creates a new API key.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def create_key(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_key` via a request object, either of type [CreateKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-CreateKeyRequest "Google::Cloud::ApiKeys::V2::CreateKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::CreateKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-CreateKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_key(parent: nil, key: nil, key_id: nil) -> ::Gapic::Operation

Pass arguments to `create_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project in which the API key is created. 
  * **key** ([::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key), ::Hash) — Required. The API key fields to set at creation time. You can configure only the `display_name`, `restrictions`, and `annotations` fields. 
  * **key_id** (::String) — User specified key id (optional). If specified, it will become the final component of the key resource name.

The id must be unique within the project, must conform with RFC-1034, is restricted to lower-cased letters, and has a maximum length of 63 characters. In another word, the id must match the regular expression: `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`.

The id must NOT be a UUID-like string. 




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
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::CreateKeyRequest.new
    
    # Call the create_key method.
    result = client.create_key request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_key
    
    
    def delete_key(request, options = nil) -> ::Gapic::Operation
    def delete_key(name: nil, etag: nil) -> ::Gapic::Operation

Deletes an API key. Deleted key can be retrieved within 30 days of deletion. Afterward, key will be purged from the project.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def delete_key(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_key` via a request object, either of type [DeleteKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-DeleteKeyRequest "Google::Cloud::ApiKeys::V2::DeleteKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::DeleteKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-DeleteKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_key(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the API key to be deleted. 
  * **etag** (::String) — Optional. The etag known to the client for the expected state of the key. This is to be used for optimistic concurrency. 



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
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::DeleteKeyRequest.new
    
    # Call the delete_key method.
    result = client.delete_key request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_key
    
    
    def get_key(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::Key
    def get_key(name: nil) -> ::Google::Cloud::ApiKeys::V2::Key

Gets the metadata for an API key. The key string of the API key isn't included in the response.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def get_key(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::Key

Pass arguments to `get_key` via a request object, either of type [GetKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyRequest "Google::Cloud::ApiKeys::V2::GetKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::GetKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_key(name: nil) -> ::Google::Cloud::ApiKeys::V2::Key

Pass arguments to `get_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the API key to get. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::GetKeyRequest.new
    
    # Call the get_key method.
    result = client.get_key request
    
    # The returned object is of type Google::Cloud::ApiKeys::V2::Key.
    p result

### #get_key_string
    
    
    def get_key_string(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::GetKeyStringResponse
    def get_key_string(name: nil) -> ::Google::Cloud::ApiKeys::V2::GetKeyStringResponse

Get the key string for an API key.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def get_key_string(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::GetKeyStringResponse

Pass arguments to `get_key_string` via a request object, either of type [GetKeyStringRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyStringRequest "Google::Cloud::ApiKeys::V2::GetKeyStringRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::GetKeyStringRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyStringRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_key_string(name: nil) -> ::Google::Cloud::ApiKeys::V2::GetKeyStringResponse

Pass arguments to `get_key_string` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the API key to be retrieved. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiKeys::V2::GetKeyStringResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyStringResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiKeys::V2::GetKeyStringResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-GetKeyStringResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::GetKeyStringRequest.new
    
    # Call the get_key_string method.
    result = client.get_key_string request
    
    # The returned object is of type Google::Cloud::ApiKeys::V2::GetKeyStringResponse.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ApiKeys REST client object.

**Yields**

  * (config) — Configure the ApiKeys client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_keys
    
    
    def list_keys(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiKeys::V2::Key>
    def list_keys(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiKeys::V2::Key>

Lists the API keys owned by a project. The key string of the API key isn't included in the response.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def list_keys(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiKeys::V2::Key>

Pass arguments to `list_keys` via a request object, either of type [ListKeysRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ListKeysRequest "Google::Cloud::ApiKeys::V2::ListKeysRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::ListKeysRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ListKeysRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_keys(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApiKeys::V2::Key>

Pass arguments to `list_keys` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Lists all API keys associated with this project. 
  * **page_size** (::Integer) — Optional. Specifies the maximum number of results to be returned at a time. 
  * **page_token** (::String) — Optional. Requests a specific page of results. 
  * **show_deleted** (::Boolean) — Optional. Indicate that keys deleted in the past 30 days should also be returned. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::ListKeysRequest.new
    
    # Call the list_keys method.
    result = client.list_keys request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApiKeys::V2::Key.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #lookup_key
    
    
    def lookup_key(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::LookupKeyResponse
    def lookup_key(key_string: nil) -> ::Google::Cloud::ApiKeys::V2::LookupKeyResponse

Find the parent project and resource name of the API key that matches the key string in the request. If the API key has been purged, resource name will not be set. The service account must have the `apikeys.keys.lookup` permission on the parent project.

**Overloads**
    
    
    def lookup_key(request, options = nil) -> ::Google::Cloud::ApiKeys::V2::LookupKeyResponse

Pass arguments to `lookup_key` via a request object, either of type [LookupKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-LookupKeyRequest "Google::Cloud::ApiKeys::V2::LookupKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::LookupKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-LookupKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def lookup_key(key_string: nil) -> ::Google::Cloud::ApiKeys::V2::LookupKeyResponse

Pass arguments to `lookup_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **key_string** (::String) — Required. Finds the project that owns the key string value. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::ApiKeys::V2::LookupKeyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-LookupKeyResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::ApiKeys::V2::LookupKeyResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-LookupKeyResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::LookupKeyRequest.new
    
    # Call the lookup_key method.
    result = client.lookup_key request
    
    # The returned object is of type Google::Cloud::ApiKeys::V2::LookupKeyResponse.
    p result

### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-ApiKeys-Rest-Operations)) 



### #undelete_key
    
    
    def undelete_key(request, options = nil) -> ::Gapic::Operation
    def undelete_key(name: nil) -> ::Gapic::Operation

Undeletes an API key which was deleted within 30 days.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def undelete_key(request, options = nil) -> ::Gapic::Operation

Pass arguments to `undelete_key` via a request object, either of type [UndeleteKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-UndeleteKeyRequest "Google::Cloud::ApiKeys::V2::UndeleteKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::UndeleteKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-UndeleteKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def undelete_key(name: nil) -> ::Gapic::Operation

Pass arguments to `undelete_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the API key to be undeleted. 



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
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::UndeleteKeyRequest.new
    
    # Call the undelete_key method.
    result = client.undelete_key request
    
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



### #update_key
    
    
    def update_key(request, options = nil) -> ::Gapic::Operation
    def update_key(key: nil, update_mask: nil) -> ::Gapic::Operation

Patches the modifiable fields of an API key. The key string of the API key isn't included in the response.

NOTE: Key is a global resource; hence the only supported value for location is `global`.

**Overloads**
    
    
    def update_key(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_key` via a request object, either of type [UpdateKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-UpdateKeyRequest "Google::Cloud::ApiKeys::V2::UpdateKeyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiKeys::V2::UpdateKeyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-UpdateKeyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_key(key: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_key` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **key** ([::Google::Cloud::ApiKeys::V2::Key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Cloud-ApiKeys-V2-Key), ::Hash) — Required. Set the `name` field to the resource name of the API key to be updated. You can update only the `display_name`, `restrictions`, and `annotations` fields. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_keys-v2/latest/Google-Protobuf-FieldMask), ::Hash) — The field mask specifies which fields to be updated as part of this request. All other fields are ignored. Mutable fields are: `display_name`, `restrictions`, and `annotations`. If an update mask is not provided, the service treats it as an implied mask equivalent to all allowed fields that are set on the wire. If the field mask has a special value "*", the service treats it equivalent to replace all allowed mutable fields. 



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
    
    
    require "google/cloud/api_keys/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiKeys::V2::ApiKeys::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiKeys::V2::UpdateKeyRequest.new
    
    # Call the update_key method.
    result = client.update_key request
    
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
