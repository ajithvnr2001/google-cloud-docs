---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client/
title: Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplateController::Client (v1.17.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:20.011148+00:00
---

# Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplateController::Client (v1.17.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Dataproc V1 API - Class Google::Cloud::Dataproc::V1::SessionTemplateController::Client (v1.17.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.17.1 (latest)  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.1  1.2.0  1.1.0  1.0.2  0.26.0  0.25.0  0.24.1  0.23.1  0.22.0  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Dataproc V1 API class Google::Cloud::Dataproc::V1::SessionTemplateController::Client.

Client for the SessionTemplateController service.

The SessionTemplateController provides methods to manage session templates.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Dataproc::V1::SessionTemplateController::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SessionTemplateController Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration "Google::Cloud::Dataproc::V1::SessionTemplateController::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SessionTemplateController clients
    ::Google::Cloud::Dataproc::V1::SessionTemplateController::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SessionTemplateController Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client#Google__Cloud__Dataproc__V1__SessionTemplateController__Client_configure_class_ "Google::Cloud::Dataproc::V1::SessionTemplateController::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration "Google::Cloud::Dataproc::V1::SessionTemplateController::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration)) 



### #create_session_template
    
    
    def create_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate
    def create_session_template(parent: nil, session_template: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Create a session template synchronously.

**Overloads**
    
    
    def create_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `create_session_template` via a request object, either of type [CreateSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-CreateSessionTemplateRequest "Google::Cloud::Dataproc::V1::CreateSessionTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::CreateSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-CreateSessionTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_session_template(parent: nil, session_template: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `create_session_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this session template will be created. 
  * **session_template** ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate), ::Hash) — Required. The session template to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::CreateSessionTemplateRequest.new
    
    # Call the create_session_template method.
    result = client.create_session_template request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::SessionTemplate.
    p result

### #delete_session_template
    
    
    def delete_session_template(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_session_template(name: nil) -> ::Google::Protobuf::Empty

Deletes a session template.

**Overloads**
    
    
    def delete_session_template(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_session_template` via a request object, either of type [DeleteSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DeleteSessionTemplateRequest "Google::Cloud::Dataproc::V1::DeleteSessionTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::DeleteSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-DeleteSessionTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_session_template(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_session_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the session template resource to delete. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::DeleteSessionTemplateRequest.new
    
    # Call the delete_session_template method.
    result = client.delete_session_template request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_session_template
    
    
    def get_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate
    def get_session_template(name: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Gets the resource representation for a session template.

**Overloads**
    
    
    def get_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `get_session_template` via a request object, either of type [GetSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-GetSessionTemplateRequest "Google::Cloud::Dataproc::V1::GetSessionTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::GetSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-GetSessionTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_session_template(name: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `get_session_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the session template to retrieve. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::GetSessionTemplateRequest.new
    
    # Call the get_session_template method.
    result = client.get_session_template request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::SessionTemplate.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SessionTemplateController client object.

**Yields**

  * (config) — Configure the SessionTemplateController client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplateController-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new do |config|
      config.timeout = 10.0
    end

### #list_session_templates
    
    
    def list_session_templates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::SessionTemplate>
    def list_session_templates(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::SessionTemplate>

Lists session templates.

**Overloads**
    
    
    def list_session_templates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::SessionTemplate>

Pass arguments to `list_session_templates` via a request object, either of type [ListSessionTemplatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionTemplatesRequest "Google::Cloud::Dataproc::V1::ListSessionTemplatesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::ListSessionTemplatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-ListSessionTemplatesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_session_templates(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Dataproc::V1::SessionTemplate>

Pass arguments to `list_session_templates` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent that owns this collection of session templates. 
  * **page_size** (::Integer) — Optional. The maximum number of sessions to return in each response. The service may return fewer than this value. 
  * **page_token** (::String) — Optional. A page token received from a previous `ListSessions` call. Provide this token to retrieve the subsequent page. 
  * **filter** (::String) — Optional. A filter for the session templates to return in the response. Filters are case sensitive and have the following syntax:

[field = value] AND [field [= value]] ... 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::ListSessionTemplatesRequest.new
    
    # Call the list_session_templates method.
    result = client.list_session_templates request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Dataproc::V1::SessionTemplate.
      p item
    end

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



### #update_session_template
    
    
    def update_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate
    def update_session_template(session_template: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Updates the session template synchronously.

**Overloads**
    
    
    def update_session_template(request, options = nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `update_session_template` via a request object, either of type [UpdateSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UpdateSessionTemplateRequest "Google::Cloud::Dataproc::V1::UpdateSessionTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Dataproc::V1::UpdateSessionTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-UpdateSessionTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_session_template(session_template: nil) -> ::Google::Cloud::Dataproc::V1::SessionTemplate

Pass arguments to `update_session_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **session_template** ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate), ::Hash) — Required. The updated session template. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Dataproc::V1::SessionTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dataproc-v1/latest/Google-Cloud-Dataproc-V1-SessionTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/dataproc/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Dataproc::V1::SessionTemplateController::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Dataproc::V1::UpdateSessionTemplateRequest.new
    
    # Call the update_session_template method.
    result = client.update_session_template request
    
    # The returned object is of type Google::Cloud::Dataproc::V1::SessionTemplate.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
