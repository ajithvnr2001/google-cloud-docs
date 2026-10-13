---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client/
title: Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::Lustre::Rest::Client (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:14.437591+00:00
---

# Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::Lustre::Rest::Client (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Managed Lustre V1 API - Class Google::Cloud::Lustre::V1::Lustre::Rest::Client (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the Google Cloud Managed Lustre V1 API class Google::Cloud::Lustre::V1::Lustre::Rest::Client.

REST client for the Lustre service.

Service describing handlers for resources

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Lustre::V1::Lustre::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Lustre Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration "Google::Cloud::Lustre::V1::Lustre::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Lustre clients
    ::Google::Cloud::Lustre::V1::Lustre::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Lustre Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client#Google__Cloud__Lustre__V1__Lustre__Rest__Client_configure_class_ "Google::Cloud::Lustre::V1::Lustre::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration "Google::Cloud::Lustre::V1::Lustre::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration)) 



### #create_directory_policy
    
    
    def create_directory_policy(request, options = nil) -> ::Gapic::Operation
    def create_directory_policy(parent: nil, directory_policy_id: nil, directory_policy: nil) -> ::Gapic::Operation

Creates a directory policy resource.

**Overloads**
    
    
    def create_directory_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_directory_policy` via a request object, either of type [CreateDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateDirectoryPolicyRequest "Google::Cloud::Lustre::V1::CreateDirectoryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::CreateDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateDirectoryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_directory_policy(parent: nil, directory_policy_id: nil, directory_policy: nil) -> ::Gapic::Operation

Pass arguments to `create_directory_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`. 
  * **directory_policy_id** (::String) — Required. The ID for the DirectoryPolicy to create. 
  * **directory_policy** ([::Google::Cloud::Lustre::V1::DirectoryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DirectoryPolicy), ::Hash) — Required. The directory policy to create. 



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::CreateDirectoryPolicyRequest.new
    
    # Call the create_directory_policy method.
    result = client.create_directory_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_instance
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Creates a new instance in a given project and location.

**Overloads**
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via a request object, either of type [CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateInstanceRequest "Google::Cloud::Lustre::V1::CreateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_instance(parent: nil, instance_id: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance's project and location, in the format `projects/{project}/locations/{location}`. Locations map to Google Cloud zones; for example, `us-west1-b`. 
  * **instance_id** (::String) — 

Required. The name of the Managed Lustre instance.

    * Must contain only lowercase letters, numbers, and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.
  * **instance** ([::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance), ::Hash) — Required. The resource being created 
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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::CreateInstanceRequest.new
    
    # Call the create_instance method.
    result = client.create_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_mirror
    
    
    def create_mirror(request, options = nil) -> ::Gapic::Operation
    def create_mirror(parent: nil, mirror_id: nil, mirror: nil, request_id: nil) -> ::Gapic::Operation

Creates a new mirror in a given instance.

**Overloads**
    
    
    def create_mirror(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_mirror` via a request object, either of type [CreateMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateMirrorRequest "Google::Cloud::Lustre::V1::CreateMirrorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::CreateMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-CreateMirrorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_mirror(parent: nil, mirror_id: nil, mirror: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_mirror` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent instance resource where the mirror will be created, in the format: `projects/{project}/locations/{location}/instances/{instance}`
  * **mirror_id** (::String) — Required. The ID to use for the mirror.

    * Must contain only lowercase letters, numbers, and hyphens.
    * Must start with a letter.
    * Must be between 1-63 characters.
    * Must end with a number or a letter.

The ID cannot be changed after the mirror is created. 

  * **mirror** ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror), ::Hash) — Required. The mirror to create. 
  * **request_id** (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in creation of duplicate mirrors for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate mirrors.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::CreateMirrorRequest.new
    
    # Call the create_mirror method.
    result = client.create_mirror request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_directory_policy
    
    
    def delete_directory_policy(request, options = nil) -> ::Gapic::Operation
    def delete_directory_policy(name: nil) -> ::Gapic::Operation

Deletes a directory policy resource.

**Overloads**
    
    
    def delete_directory_policy(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_directory_policy` via a request object, either of type [DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteDirectoryPolicyRequest "Google::Cloud::Lustre::V1::DeleteDirectoryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::DeleteDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteDirectoryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_directory_policy(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_directory_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`. 



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::DeleteDirectoryPolicyRequest.new
    
    # Call the delete_directory_policy method.
    result = client.delete_directory_policy request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_instance
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation
    def delete_instance(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Deletes a single instance.

**Overloads**
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via a request object, either of type [DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteInstanceRequest "Google::Cloud::Lustre::V1::DeleteInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_instance(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the instance to delete, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **force** (::Boolean) — Optional. If set to true, any sub-resources from this instance will also be deleted. Otherwise, the request will only work if the instance has no sub-resources. 



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::DeleteInstanceRequest.new
    
    # Call the delete_instance method.
    result = client.delete_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_mirror
    
    
    def delete_mirror(request, options = nil) -> ::Gapic::Operation
    def delete_mirror(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single mirror.

**Overloads**
    
    
    def delete_mirror(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_mirror` via a request object, either of type [DeleteMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteMirrorRequest "Google::Cloud::Lustre::V1::DeleteMirrorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::DeleteMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DeleteMirrorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_mirror(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_mirror` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the mirror to delete, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`
  * **request_id** (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in the same delete request being executed for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::DeleteMirrorRequest.new
    
    # Call the delete_mirror method.
    result = client.delete_mirror request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #export_data
    
    
    def export_data(request, options = nil) -> ::Gapic::Operation
    def export_data(lustre_path: nil, gcs_path: nil, name: nil, request_id: nil, service_account: nil) -> ::Gapic::Operation

Exports data from a Managed Lustre instance to Cloud Storage.

**Overloads**
    
    
    def export_data(request, options = nil) -> ::Gapic::Operation

Pass arguments to `export_data` via a request object, either of type [ExportDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ExportDataRequest "Google::Cloud::Lustre::V1::ExportDataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::ExportDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ExportDataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def export_data(lustre_path: nil, gcs_path: nil, name: nil, request_id: nil, service_account: nil) -> ::Gapic::Operation

Pass arguments to `export_data` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **lustre_path** ([::Google::Cloud::Lustre::V1::LustrePath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-LustrePath), ::Hash) — The root directory path to the Managed Lustre file system. Must start with `/`. Default is `/`. 
  * **gcs_path** ([::Google::Cloud::Lustre::V1::GcsPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GcsPath), ::Hash) — The URI to a Cloud Storage bucket, or a path within a bucket, using the format `gs://<bucket_name>/<optional_path_inside_bucket>/`. If a path inside the bucket is specified, it must end with a forward slash (`/`). 
  * **name** (::String) — Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`. 
  * **request_id** (::String) — Optional. UUID to identify requests. 
  * **service_account** (::String) — 

Optional. User-specified service account used to perform the transfer. If unspecified, the Managed Lustre service agent is used.

Use one of the following formats:

    * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
    * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
    * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::ExportDataRequest.new
    
    # Call the export_data method.
    result = client.export_data request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_directory_policy
    
    
    def get_directory_policy(request, options = nil) -> ::Google::Cloud::Lustre::V1::DirectoryPolicy
    def get_directory_policy(name: nil) -> ::Google::Cloud::Lustre::V1::DirectoryPolicy

Gets details of a single directory policy.

**Overloads**
    
    
    def get_directory_policy(request, options = nil) -> ::Google::Cloud::Lustre::V1::DirectoryPolicy

Pass arguments to `get_directory_policy` via a request object, either of type [GetDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetDirectoryPolicyRequest "Google::Cloud::Lustre::V1::GetDirectoryPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::GetDirectoryPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetDirectoryPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_directory_policy(name: nil) -> ::Google::Cloud::Lustre::V1::DirectoryPolicy

Pass arguments to `get_directory_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the directory policy. DirectoryPolicy names have the form `projects/{project}/locations/{location}/instances/{instance}/directoryPolicies/{id}`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Lustre::V1::DirectoryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DirectoryPolicy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Lustre::V1::DirectoryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DirectoryPolicy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::GetDirectoryPolicyRequest.new
    
    # Call the get_directory_policy method.
    result = client.get_directory_policy request
    
    # The returned object is of type Google::Cloud::Lustre::V1::DirectoryPolicy.
    p result

### #get_instance
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::Lustre::V1::Instance
    def get_instance(name: nil) -> ::Google::Cloud::Lustre::V1::Instance

Gets details of a single instance.

**Overloads**
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::Lustre::V1::Instance

Pass arguments to `get_instance` via a request object, either of type [GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetInstanceRequest "Google::Cloud::Lustre::V1::GetInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_instance(name: nil) -> ::Google::Cloud::Lustre::V1::Instance

Pass arguments to `get_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The instance resource name, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::GetInstanceRequest.new
    
    # Call the get_instance method.
    result = client.get_instance request
    
    # The returned object is of type Google::Cloud::Lustre::V1::Instance.
    p result

### #get_mirror
    
    
    def get_mirror(request, options = nil) -> ::Google::Cloud::Lustre::V1::Mirror
    def get_mirror(name: nil) -> ::Google::Cloud::Lustre::V1::Mirror

Gets details of a single mirror.

**Overloads**
    
    
    def get_mirror(request, options = nil) -> ::Google::Cloud::Lustre::V1::Mirror

Pass arguments to `get_mirror` via a request object, either of type [GetMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetMirrorRequest "Google::Cloud::Lustre::V1::GetMirrorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::GetMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GetMirrorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_mirror(name: nil) -> ::Google::Cloud::Lustre::V1::Mirror

Pass arguments to `get_mirror` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the mirror to retrieve, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::GetMirrorRequest.new
    
    # Call the get_mirror method.
    result = client.get_mirror request
    
    # The returned object is of type Google::Cloud::Lustre::V1::Mirror.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #import_data
    
    
    def import_data(request, options = nil) -> ::Gapic::Operation
    def import_data(gcs_path: nil, lustre_path: nil, name: nil, request_id: nil, service_account: nil) -> ::Gapic::Operation

Imports data from Cloud Storage to a Managed Lustre instance.

**Overloads**
    
    
    def import_data(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_data` via a request object, either of type [ImportDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ImportDataRequest "Google::Cloud::Lustre::V1::ImportDataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::ImportDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ImportDataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_data(gcs_path: nil, lustre_path: nil, name: nil, request_id: nil, service_account: nil) -> ::Gapic::Operation

Pass arguments to `import_data` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **gcs_path** ([::Google::Cloud::Lustre::V1::GcsPath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-GcsPath), ::Hash) — The Cloud Storage source bucket and, optionally, path inside the bucket. If a path inside the bucket is specified, it must end with a forward slash (`/`). 
  * **lustre_path** ([::Google::Cloud::Lustre::V1::LustrePath](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-LustrePath), ::Hash) — Lustre path destination. 
  * **name** (::String) — Required. The name of the Managed Lustre instance in the format `projects/{project}/locations/{location}/instances/{instance}`. 
  * **request_id** (::String) — Optional. UUID to identify requests. 
  * **service_account** (::String) — 

Optional. User-specified service account used to perform the transfer. If unspecified, the default Managed Lustre service agent will be used.

Use one of the following formats:

    * `{EMAIL_ADDRESS_OR_UNIQUE_ID}`
    * `projects/{PROJECT_ID}/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`
    * `projects/-/serviceAccounts/{EMAIL_ADDRESS_OR_UNIQUE_ID}`



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::ImportDataRequest.new
    
    # Call the import_data method.
    result = client.import_data request
    
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
    
    
    def initialize() { |config| ... } -> Client

Create a new Lustre REST client object.

**Yields**

  * (config) — Configure the Lustre client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Lustre::V1::Lustre::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_directory_policies
    
    
    def list_directory_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::DirectoryPolicy>
    def list_directory_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::DirectoryPolicy>

Gets details of multiple directory policies under a given instance.

**Overloads**
    
    
    def list_directory_policies(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::DirectoryPolicy>

Pass arguments to `list_directory_policies` via a request object, either of type [Google::Cloud::Lustre::V1::ListDirectoryPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListDirectoryPoliciesRequest "Google::Cloud::Lustre::V1::ListDirectoryPoliciesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::ListDirectoryPoliciesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListDirectoryPoliciesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_directory_policies(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::DirectoryPolicy>

Pass arguments to `list_directory_policies` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent instance. It must be in the format of `projects/{project}/locations/{location}/instances/{instance}`. 
  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer items than requested. If unspecified, the server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListDirectoryPolicies` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListDirectoryPolicies` must match the call that provided the page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::DirectoryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DirectoryPolicy)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::DirectoryPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-DirectoryPolicy)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::ListDirectoryPoliciesRequest.new
    
    # Call the list_directory_policies method.
    result = client.list_directory_policies request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Lustre::V1::DirectoryPolicy.
      p item
    end

### #list_instances
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Instance>
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Instance>

Lists instances in a given project and location.

**Overloads**
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Instance>

Pass arguments to `list_instances` via a request object, either of type [Google::Cloud::Lustre::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListInstancesRequest "Google::Cloud::Lustre::V1::ListInstancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListInstancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_instances(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Instance>

Pass arguments to `list_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve a list of instances, in the format `projects/{projectId}/locations/{location}`.

To retrieve instance information for all locations, use "-" as the value of `{location}`. 

  * **page_size** (::Integer) — Optional. Requested page size. Server might return fewer items than requested. If unspecified, the server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Desired order of results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::ListInstancesRequest.new
    
    # Call the list_instances method.
    result = client.list_instances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Lustre::V1::Instance.
      p item
    end

### #list_mirrors
    
    
    def list_mirrors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Mirror>
    def list_mirrors(parent: nil, page_size: nil, page_token: nil, order_by: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Mirror>

Gets details of multiple mirrors under a given instance.

**Overloads**
    
    
    def list_mirrors(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Mirror>

Pass arguments to `list_mirrors` via a request object, either of type [Google::Cloud::Lustre::V1::ListMirrorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListMirrorsRequest "Google::Cloud::Lustre::V1::ListMirrorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::ListMirrorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-ListMirrorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_mirrors(parent: nil, page_size: nil, page_token: nil, order_by: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Lustre::V1::Mirror>

Pass arguments to `list_mirrors` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent instance resource where the mirrors will be listed, in the format: `projects/{project}/locations/{location}/instances/{instance}`
  * **page_size** (::Integer) — Optional. Requested page size. The server might return fewer items than requested. If unspecified, the default page size is 10. The maximum value is 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListMirrors` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListMirrors` must match the call that provided the page token. 
  * **order_by** (::String) — Optional. Desired order of results. 
  * **filter** (::String) — Optional. Filtering results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::ListMirrorsRequest.new
    
    # Call the list_mirrors method.
    result = client.list_mirrors request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Lustre::V1::Mirror.
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
    
    
    def operations_client() -> ::Google::Cloud::Lustre::V1::Lustre::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Lustre::V1::Lustre::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Lustre-Rest-Operations)) 



### #reschedule_maintenance
    
    
    def reschedule_maintenance(request, options = nil) -> ::Gapic::Operation
    def reschedule_maintenance(name: nil, reschedule: nil, request_id: nil) -> ::Gapic::Operation

Reschedules a planned maintenance event for a specific instance.

**Overloads**
    
    
    def reschedule_maintenance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reschedule_maintenance` via a request object, either of type [RescheduleMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-RescheduleMaintenanceRequest "Google::Cloud::Lustre::V1::RescheduleMaintenanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::RescheduleMaintenanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-RescheduleMaintenanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def reschedule_maintenance(name: nil, reschedule: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `reschedule_maintenance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **reschedule** ([::Google::Cloud::Lustre::V1::RescheduleMaintenanceRequest::Reschedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-RescheduleMaintenanceRequest-Reschedule), ::Hash) — Required. The desired reschedule settings. 
  * **request_id** (::String) — Optional. A unique identifier for this request. A random UUID is recommended. This request is only idempotent if a `request_id` is provided. 



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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::RescheduleMaintenanceRequest.new
    
    # Call the reschedule_maintenance method.
    result = client.reschedule_maintenance request
    
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



### #update_instance
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation
    def update_instance(update_mask: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single instance.

**Overloads**
    
    
    def update_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via a request object, either of type [UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateInstanceRequest "Google::Cloud::Lustre::V1::UpdateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::UpdateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_instance(update_mask: nil, instance: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Specifies the fields to be overwritten in the instance resource by the update.

The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten. 

  * **instance** ([::Google::Cloud::Lustre::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Instance), ::Hash) — Required. The resource name of the instance to update, in the format `projects/{projectId}/locations/{location}/instances/{instanceId}`. 
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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::UpdateInstanceRequest.new
    
    # Call the update_instance method.
    result = client.update_instance request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_mirror
    
    
    def update_mirror(request, options = nil) -> ::Gapic::Operation
    def update_mirror(mirror: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single mirror.

**Overloads**
    
    
    def update_mirror(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_mirror` via a request object, either of type [UpdateMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateMirrorRequest "Google::Cloud::Lustre::V1::UpdateMirrorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Lustre::V1::UpdateMirrorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-UpdateMirrorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_mirror(mirror: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_mirror` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **mirror** ([::Google::Cloud::Lustre::V1::Mirror](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Cloud-Lustre-V1-Mirror), ::Hash) — Required. Mirror to update. The mirror's `name` field is used to identify the mirror to update, in the format: `projects/{project}/locations/{location}/instances/{instance}/mirrors/{mirror}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-lustre-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If no mask is provided then all fields present in the request are overwritten. 
  * **request_id** (::String) — Optional. The unique ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server guarantees that a request doesn't result in the same update request being executed for at least 60 minutes.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request.

The request ID must be a valid UUID version 4 with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`). This request is only idempotent if a `request_id` is provided. 




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
    
    
    require "google/cloud/lustre/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Lustre::V1::Lustre::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Lustre::V1::UpdateMirrorRequest.new
    
    # Call the update_mirror method.
    result = client.update_mirror request
    
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
