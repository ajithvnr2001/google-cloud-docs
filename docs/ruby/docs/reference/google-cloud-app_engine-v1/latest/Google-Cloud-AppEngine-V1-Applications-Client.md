---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Applications::Client (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:11.360627+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Applications::Client (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::Applications::Client (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::Applications::Client.

Client for the Applications service.

Manages App Engine applications.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Applications Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration "Google::Cloud::AppEngine::V1::Applications::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Applications clients
    ::Google::Cloud::AppEngine::V1::Applications::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Applications Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client#Google__Cloud__AppEngine__V1__Applications__Client_configure_class_ "Google::Cloud::AppEngine::V1::Applications::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration "Google::Cloud::AppEngine::V1::Applications::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration)) 



### #create_application
    
    
    def create_application(request, options = nil) -> ::Gapic::Operation
    def create_application(application: nil) -> ::Gapic::Operation

Creates an App Engine application for a Google Cloud Platform project. Required fields:

  * `id` \- The ID of the target Cloud Platform project.
  * _location_ \- The [region](https://cloud.google.com/appengine/docs/locations) where you want the App Engine application located.



For more information about App Engine applications, see [Managing Projects, Applications, and Billing](https://cloud.google.com/appengine/docs/standard/python/console/).

**Overloads**
    
    
    def create_application(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_application` via a request object, either of type [CreateApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateApplicationRequest "Google::Cloud::AppEngine::V1::CreateApplicationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::CreateApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateApplicationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_application(application: nil) -> ::Gapic::Operation

Pass arguments to `create_application` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **application** ([::Google::Cloud::AppEngine::V1::Application](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application), ::Hash) — Application configuration. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Applications::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::CreateApplicationRequest.new
    
    # Call the create_application method.
    result = client.create_application request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_application
    
    
    def get_application(request, options = nil) -> ::Google::Cloud::AppEngine::V1::Application
    def get_application(name: nil) -> ::Google::Cloud::AppEngine::V1::Application

Gets information about an application.

**Overloads**
    
    
    def get_application(request, options = nil) -> ::Google::Cloud::AppEngine::V1::Application

Pass arguments to `get_application` via a request object, either of type [GetApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetApplicationRequest "Google::Cloud::AppEngine::V1::GetApplicationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::GetApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-GetApplicationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_application(name: nil) -> ::Google::Cloud::AppEngine::V1::Application

Pass arguments to `get_application` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the Application resource to get. Example: `apps/myapp`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::AppEngine::V1::Application](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::Application](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Applications::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::GetApplicationRequest.new
    
    # Call the get_application method.
    result = client.get_application request
    
    # The returned object is of type Google::Cloud::AppEngine::V1::Application.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Applications client object.

**Yields**

  * (config) — Configure the Applications client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AppEngine::V1::Applications::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AppEngine::V1::Applications::Client.new do |config|
      config.timeout = 10.0
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AppEngine::V1::Applications::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AppEngine::V1::Applications::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Applications-Operations)) 



### #repair_application
    
    
    def repair_application(request, options = nil) -> ::Gapic::Operation
    def repair_application(name: nil) -> ::Gapic::Operation

Recreates the required App Engine features for the specified App Engine application, for example a Cloud Storage bucket or App Engine service account. Use this method if you receive an error message about a missing feature, for example, _Error retrieving the App Engine service account_. If you have deleted your App Engine service account, this will not be able to recreate it. Instead, you should attempt to use the IAM undelete API if possible at <https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts/undelete?apix_params=%7B"name"%3A"projects%2F-%2FserviceAccounts%2Funique_id"%2C"resource"%3A%7B%7D%7D> . If the deletion was recent, the numeric ID can be found in the Cloud Console Activity Log.

**Overloads**
    
    
    def repair_application(request, options = nil) -> ::Gapic::Operation

Pass arguments to `repair_application` via a request object, either of type [RepairApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-RepairApplicationRequest "Google::Cloud::AppEngine::V1::RepairApplicationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::RepairApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-RepairApplicationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def repair_application(name: nil) -> ::Gapic::Operation

Pass arguments to `repair_application` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the application to repair. Example: `apps/myapp`



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Applications::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::RepairApplicationRequest.new
    
    # Call the repair_application method.
    result = client.repair_application request
    
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



### #update_application
    
    
    def update_application(request, options = nil) -> ::Gapic::Operation
    def update_application(name: nil, application: nil, update_mask: nil) -> ::Gapic::Operation

Updates the specified Application resource. You can update the following fields:

  * `auth_domain` \- Google authentication domain for controlling user access to the application.
  * `default_cookie_expiration` \- Cookie expiration policy for the application.
  * `iap` \- Identity-Aware Proxy properties for the application.



**Overloads**
    
    
    def update_application(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_application` via a request object, either of type [UpdateApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateApplicationRequest "Google::Cloud::AppEngine::V1::UpdateApplicationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AppEngine::V1::UpdateApplicationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-UpdateApplicationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_application(name: nil, application: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_application` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the Application resource to update. Example: `apps/myapp`. 
  * **application** ([::Google::Cloud::AppEngine::V1::Application](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-Application), ::Hash) — An Application containing the updated resource. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Standard field mask for the set of fields to be updated. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/app_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AppEngine::V1::Applications::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AppEngine::V1::UpdateApplicationRequest.new
    
    # Call the update_application method.
    result = client.update_application request
    
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
