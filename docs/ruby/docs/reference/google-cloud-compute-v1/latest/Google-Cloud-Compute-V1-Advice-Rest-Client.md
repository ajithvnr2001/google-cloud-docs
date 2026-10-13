---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Advice::Rest::Client (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:24:28.408047+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Advice::Rest::Client (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::Advice::Rest::Client (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::Advice::Rest::Client.

REST client for the Advice service.

The Advice API.

This client uses Advice version 2026-09-01.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the Advice Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration "Google::Cloud::Compute::V1::Advice::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all Advice clients
    ::Google::Cloud::Compute::V1::Advice::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #calendar_mode
    
    
    def calendar_mode(request, options = nil) -> ::Google::Cloud::Compute::V1::CalendarModeAdviceResponse
    def calendar_mode(calendar_mode_advice_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CalendarModeAdviceResponse

Advise how, where and when to create the requested amount of instances with specified accelerators, within the specified time and location limits. The method recommends creating future reservations for the requested resources.

**Overloads**
    
    
    def calendar_mode(request, options = nil) -> ::Google::Cloud::Compute::V1::CalendarModeAdviceResponse

Pass arguments to `calendar_mode` via a request object, either of type [CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CalendarModeAdviceRpcRequest "Google::Cloud::Compute::V1::CalendarModeAdviceRpcRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::CalendarModeAdviceRpcRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CalendarModeAdviceRpcRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def calendar_mode(calendar_mode_advice_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CalendarModeAdviceResponse

Pass arguments to `calendar_mode` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **calendar_mode_advice_request_resource** ([::Google::Cloud::Compute::V1::CalendarModeAdviceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CalendarModeAdviceRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::CalendarModeAdviceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CalendarModeAdviceResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::CalendarModeAdviceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CalendarModeAdviceResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Advice::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::CalendarModeAdviceRpcRequest.new
    
    # Call the calendar_mode method.
    result = client.calendar_mode request
    
    # The returned object is of type Google::Cloud::Compute::V1::CalendarModeAdviceResponse.
    p result

### #capacity
    
    
    def capacity(request, options = nil) -> ::Google::Cloud::Compute::V1::CapacityAdviceResponse
    def capacity(capacity_advice_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CapacityAdviceResponse

Advice on making real-time decisions (such as choosing zone or machine types) during deployment to maximize your chances of obtaining capacity.

**Overloads**
    
    
    def capacity(request, options = nil) -> ::Google::Cloud::Compute::V1::CapacityAdviceResponse

Pass arguments to `capacity` via a request object, either of type [CapacityAdviceRpcRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityAdviceRpcRequest "Google::Cloud::Compute::V1::CapacityAdviceRpcRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::CapacityAdviceRpcRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityAdviceRpcRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def capacity(capacity_advice_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CapacityAdviceResponse

Pass arguments to `capacity` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **capacity_advice_request_resource** ([::Google::Cloud::Compute::V1::CapacityAdviceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityAdviceRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::CapacityAdviceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityAdviceResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::CapacityAdviceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityAdviceResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Advice::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::CapacityAdviceRpcRequest.new
    
    # Call the capacity method.
    result = client.capacity request
    
    # The returned object is of type Google::Cloud::Compute::V1::CapacityAdviceResponse.
    p result

### #capacity_history
    
    
    def capacity_history(request, options = nil) -> ::Google::Cloud::Compute::V1::CapacityHistoryResponse
    def capacity_history(capacity_history_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CapacityHistoryResponse

Gets the capacity history.

**Overloads**
    
    
    def capacity_history(request, options = nil) -> ::Google::Cloud::Compute::V1::CapacityHistoryResponse

Pass arguments to `capacity_history` via a request object, either of type [CapacityHistoryAdviceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityHistoryAdviceRequest "Google::Cloud::Compute::V1::CapacityHistoryAdviceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Compute::V1::CapacityHistoryAdviceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityHistoryAdviceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def capacity_history(capacity_history_request_resource: nil, project: nil, region: nil) -> ::Google::Cloud::Compute::V1::CapacityHistoryResponse

Pass arguments to `capacity_history` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **capacity_history_request_resource** ([::Google::Cloud::Compute::V1::CapacityHistoryRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityHistoryRequest), ::Hash) — The body resource for this request 
  * **project** (::String) — Project ID for this request. 
  * **region** (::String) — Name of the region for this request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Compute::V1::CapacityHistoryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityHistoryResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Compute::V1::CapacityHistoryResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-CapacityHistoryResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/compute/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Compute::V1::Advice::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Compute::V1::CapacityHistoryAdviceRequest.new
    
    # Call the capacity_history method.
    result = client.capacity_history request
    
    # The returned object is of type Google::Cloud::Compute::V1::CapacityHistoryResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the Advice Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client#Google__Cloud__Compute__V1__Advice__Rest__Client_configure_class_ "Google::Cloud::Compute::V1::Advice::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration "Google::Cloud::Compute::V1::Advice::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new Advice REST client object.

**Yields**

  * (config) — Configure the Advice client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-Advice-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Compute::V1::Advice::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Compute::V1::Advice::Rest::Client.new do |config|
      config.timeout = 10.0
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
