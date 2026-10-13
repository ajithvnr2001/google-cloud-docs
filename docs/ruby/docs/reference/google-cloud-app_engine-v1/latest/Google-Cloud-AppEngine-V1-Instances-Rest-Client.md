---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instances::Rest::Client (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:57.648428+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instances::Rest::Client (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Instances::Rest::Client (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Instances::Rest::Client.

REST client for the Instances service.

Manages instances of a version.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Instances Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration "Google::Cloud::AppEngine::V1::Instances::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Instances clients
    ::Google::Cloud::AppEngine::V1::Instances::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Instances Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client#Google__Cloud__AppEngine__V1__Instances__Rest__Client_configure_class_ "Google::Cloud::AppEngine::V1::Instances::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration "Google::Cloud::AppEngine::V1::Instances::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration)) 



### #debug_instance
    
    
    def debug_instance(request, options = nil) -> ::Gapic::Operation
    def debug_instance(name: nil, ssh_key: nil) -> ::Gapic::Operation

Enables debugging on a VM instance. This allows you to use the SSH command to connect to the virtual machine where the instance lives. While in "debug mode", the instance continues to serve live traffic. You should delete the instance when you are done debugging and then allow the system to take over and determine if another instance should be started.

Only applicable for instances in App Engine flexible environment.

**Overloads**
    
    
    def debug_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `debug_instance` via a request object, either of type [DebugInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DebugInstanceRequest "Google::Cloud::AppEngine::V1::DebugInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::DebugInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DebugInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def debug_instance(name: nil, ssh_key: nil) -> ::Gapic::Operation

Pass arguments to `debug_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. 
  * **ssh_key** (::String) — Public SSH key to add to the instance. Examples:

    * `[USERNAME]:ssh-rsa [KEY_VALUE] [USERNAME]`
    * `[USERNAME]:ssh-rsa [KEY_VALUE] google-ssh {"userName":"[USERNAME]","expireOn":"[EXPIRE_TIME]"}`

For more information, see [Adding and Removing SSH Keys](https://cloud.google.com/compute/docs/instances/adding-removing-ssh-keys). 




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
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Instances::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::DebugInstanceRequest.new
    
    # Call the debug_instance method.
    result = client.debug_instance request
    
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
    def delete_instance(name: nil) -> ::Gapic::Operation

Stops a running instance.

The instance might be automatically recreated based on the scaling settings of the version. For more information, see "How Instances are Managed" ([standard environment](https://cloud.google.com/appengine/docs/standard/python/how-instances-are-managed) | [flexible environment](https://cloud.google.com/appengine/docs/flexible/python/how-instances-are-managed)).

To ensure that instances are not re-created and avoid getting billed, you can stop all instances within the target version by changing the serving status of the version to `STOPPED` with the [`apps.services.versions.patch`](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions/patch) method.

**Overloads**
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via a request object, either of type [DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteInstanceRequest "Google::Cloud::AppEngine::V1::DeleteInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-DeleteInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_instance(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. 



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
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Instances::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::DeleteInstanceRequest.new
    
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

### #get_instance
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::AppEngine::V1::Instance
    def get_instance(name: nil) -> ::Google::Cloud::AppEngine::V1::Instance

Gets instance information.

**Overloads**
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::AppEngine::V1::Instance

Pass arguments to `get_instance` via a request object, either of type [GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetInstanceRequest "Google::Cloud::AppEngine::V1::GetInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_instance(name: nil) -> ::Google::Cloud::AppEngine::V1::Instance

Pass arguments to `get_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the resource requested. Example: `apps/myapp/services/default/versions/v1/instances/instance-1`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AppEngine::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Instances::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::GetInstanceRequest.new
    
    # Call the get_instance method.
    result = client.get_instance request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::Instance.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Instances REST client object.

**Yields**

  * (config) — Configure the Instances client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AppEngine::V1::Instances::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AppEngine::V1::Instances::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_instances
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AppEngine::V1::Instance>
    def list_instances(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AppEngine::V1::Instance>

Lists the instances of a version.

Tip: To aggregate details about instances over time, see the [Stackdriver Monitoring API](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list).

**Overloads**
    
    
    def list_instances(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AppEngine::V1::Instance>

Pass arguments to `list_instances` via a request object, either of type [ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListInstancesRequest "Google::Cloud::AppEngine::V1::ListInstancesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::ListInstancesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-ListInstancesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_instances(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AppEngine::V1::Instance>

Pass arguments to `list_instances` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Name of the parent Version resource. Example: `apps/myapp/services/default/versions/v1`. 
  * **page_size** (::Integer) — Maximum results to return per page. 
  * **page_token** (::String) — Continuation token for fetching the next page of results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AppEngine::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AppEngine::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instance)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Instances::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::ListInstancesRequest.new
    
    # Call the list_instances method.
    result = client.list_instances request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AppEngine::V1::Instance.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AppEngine::V1::Instances::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Instances::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Instances-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
