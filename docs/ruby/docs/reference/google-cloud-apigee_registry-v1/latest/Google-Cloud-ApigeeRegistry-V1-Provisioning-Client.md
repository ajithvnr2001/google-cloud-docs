---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client/
title: Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Provisioning::Client (v0.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:22.249069+00:00
---

# Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Provisioning::Client (v0.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Registry V1 API - Class Google::Cloud::ApigeeRegistry::V1::Provisioning::Client (v0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.0  0.15.0  0.14.0  0.13.1  0.12.0  0.11.0  0.10.1  0.9.0  0.8.1  0.7.2  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Apigee Registry V1 API class Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.

Client for the Provisioning service.

The service that is used for managing the data plane provisioning of the Registry.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApigeeRegistry::V1::Provisioning::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Provisioning Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration "Google::Cloud::ApigeeRegistry::V1::Provisioning::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Provisioning clients
    ::Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Provisioning Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client#Google__Cloud__ApigeeRegistry__V1__Provisioning__Client_configure_class_ "Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration "Google::Cloud::ApigeeRegistry::V1::Provisioning::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration)) 



### #create_instance
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation
    def create_instance(parent: nil, instance_id: nil, instance: nil) -> ::Gapic::Operation

Provisions instance resources for the Registry.

**Overloads**
    
    
    def create_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via a request object, either of type [CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateInstanceRequest "Google::Cloud::ApigeeRegistry::V1::CreateInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::CreateInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-CreateInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_instance(parent: nil, instance_id: nil, instance: nil) -> ::Gapic::Operation

Pass arguments to `create_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource of the Instance, of the form: `projects/*/locations/*`
  * **instance_id** (::String) — Required. Identifier to assign to the Instance. Must be unique within scope of the parent resource. 
  * **instance** ([::Google::Cloud::ApigeeRegistry::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance), ::Hash) — Required. The Instance. 



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
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::CreateInstanceRequest.new
    
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

### #delete_instance
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation
    def delete_instance(name: nil) -> ::Gapic::Operation

Deletes the Registry instance.

**Overloads**
    
    
    def delete_instance(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via a request object, either of type [DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteInstanceRequest "Google::Cloud::ApigeeRegistry::V1::DeleteInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::DeleteInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-DeleteInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_instance(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Instance to delete. Format: `projects/*/locations/*/instances/*`. 



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
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::DeleteInstanceRequest.new
    
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
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Instance
    def get_instance(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Instance

Gets details of a single Instance.

**Overloads**
    
    
    def get_instance(request, options = nil) -> ::Google::Cloud::ApigeeRegistry::V1::Instance

Pass arguments to `get_instance` via a request object, either of type [GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetInstanceRequest "Google::Cloud::ApigeeRegistry::V1::GetInstanceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeRegistry::V1::GetInstanceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-GetInstanceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_instance(name: nil) -> ::Google::Cloud::ApigeeRegistry::V1::Instance

Pass arguments to `get_instance` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the Instance to retrieve. Format: `projects/*/locations/*/instances/*`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ApigeeRegistry::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Instance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Instance)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_registry/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeRegistry::V1::GetInstanceRequest.new
    
    # Call the get_instance method.
    result = client.get_instance request
    
    # The returned object is of type Google::Cloud::ApigeeRegistry::V1::Instance.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Provisioning client object.

**Yields**

  * (config) — Configure the Provisioning client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApigeeRegistry::V1::Provisioning::Client.new do |config|
      config.timeout = 10.0
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::ApigeeRegistry::V1::Provisioning::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::ApigeeRegistry::V1::Provisioning::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_registry-v1/latest/Google-Cloud-ApigeeRegistry-V1-Provisioning-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
