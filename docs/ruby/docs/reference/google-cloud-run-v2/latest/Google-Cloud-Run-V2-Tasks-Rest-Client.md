---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client/
title: Cloud Run V2 API - Class Google::Cloud::Run::V2::Tasks::Rest::Client (v0.29.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:50:54.002497+00:00
---

# Cloud Run V2 API - Class Google::Cloud::Run::V2::Tasks::Rest::Client (v0.29.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Run V2 API - Class Google::Cloud::Run::V2::Tasks::Rest::Client (v0.29.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.29.1 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.1  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.2  0.12.0  0.11.0  0.10.1  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud Run V2 API class Google::Cloud::Run::V2::Tasks::Rest::Client.

REST client for the Tasks service.

Cloud Run Task Control Plane API.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Run::V2::Tasks::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Tasks Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration "Google::Cloud::Run::V2::Tasks::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Tasks clients
    ::Google::Cloud::Run::V2::Tasks::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Tasks Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client#Google__Cloud__Run__V2__Tasks__Rest__Client_configure_class_ "Google::Cloud::Run::V2::Tasks::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration "Google::Cloud::Run::V2::Tasks::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration)) 



### #get_task
    
    
    def get_task(request, options = nil) -> ::Google::Cloud::Run::V2::Task
    def get_task(name: nil) -> ::Google::Cloud::Run::V2::Task

Gets information about a Task.

**Overloads**
    
    
    def get_task(request, options = nil) -> ::Google::Cloud::Run::V2::Task

Pass arguments to `get_task` via a request object, either of type [GetTaskRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-GetTaskRequest "Google::Cloud::Run::V2::GetTaskRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::GetTaskRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-GetTaskRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_task(name: nil) -> ::Google::Cloud::Run::V2::Task

Pass arguments to `get_task` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The full name of the Task. Format: projects/{project}/locations/{location}/jobs/{job}/executions/{execution}/tasks/{task} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Run::V2::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Task)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Run::V2::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Task)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Tasks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::GetTaskRequest.new
    
    # Call the get_task method.
    result = client.get_task request
    
    # The returned object is of type Google::Cloud::Run::V2::Task.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Tasks REST client object.

**Yields**

  * (config) — Configure the Tasks client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Tasks-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Run::V2::Tasks::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Run::V2::Tasks::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_tasks
    
    
    def list_tasks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Run::V2::Task>
    def list_tasks(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Run::V2::Task>

Lists Tasks from an Execution of a Job.

**Overloads**
    
    
    def list_tasks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Run::V2::Task>

Pass arguments to `list_tasks` via a request object, either of type [ListTasksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ListTasksRequest "Google::Cloud::Run::V2::ListTasksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Run::V2::ListTasksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-ListTasksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_tasks(parent: nil, page_size: nil, page_token: nil, show_deleted: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Run::V2::Task>

Pass arguments to `list_tasks` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The Execution from which the Tasks should be listed. To list all Tasks across Executions of a Job, use "-" instead of Execution name. To list all Tasks across Jobs, use "-" instead of Job name. Format: projects/{project}/locations/{location}/jobs/{job}/executions/{execution} 
  * **page_size** (::Integer) — Maximum number of Tasks to return in this call. 
  * **page_token** (::String) — A page token received from a previous call to ListTasks. All other parameters must match. 
  * **show_deleted** (::Boolean) — If true, returns deleted (but unexpired) resources along with active ones. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Run::V2::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Task)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Run::V2::Task](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-run-v2/latest/Google-Cloud-Run-V2-Task)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/run/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Run::V2::Tasks::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Run::V2::ListTasksRequest.new
    
    # Call the list_tasks method.
    result = client.list_tasks request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Run::V2::Task.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
