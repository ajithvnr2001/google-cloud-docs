---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client/
title: API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client (v1.0.3) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:23:33.475940+00:00
---

# API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client (v1.0.3)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  API hub V1 API - Class Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client (v1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.2  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0  0.2.0  0.1.1 

Reference documentation and code samples for the API hub V1 API class Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.

REST client for the ApiHubCollect service.

This service exposes methods used for collecting various types of data from different first party and third party sources and push it to Hub's collect layer.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApiHub::V1::ApiHubCollect::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ApiHubCollect Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration "Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ApiHubCollect clients
    ::Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #collect_api_data
    
    
    def collect_api_data(request, options = nil) -> ::Gapic::Operation
    def collect_api_data(location: nil, collection_type: nil, plugin_instance: nil, action_id: nil, api_data: nil) -> ::Gapic::Operation

Collect API data from a source and push it to Hub's collect layer.

**Overloads**
    
    
    def collect_api_data(request, options = nil) -> ::Gapic::Operation

Pass arguments to `collect_api_data` via a request object, either of type [CollectApiDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CollectApiDataRequest "Google::Cloud::ApiHub::V1::CollectApiDataRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApiHub::V1::CollectApiDataRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CollectApiDataRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def collect_api_data(location: nil, collection_type: nil, plugin_instance: nil, action_id: nil, api_data: nil) -> ::Gapic::Operation

Pass arguments to `collect_api_data` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **location** (::String) — Required. The regional location of the API hub instance and its resources. Format: `projects/{project}/locations/{location}`
  * **collection_type** ([::Google::Cloud::ApiHub::V1::CollectionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CollectionType)) — Required. The type of collection. Applies to all entries in [api_data](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-CollectApiDataRequest#Google__Cloud__ApiHub__V1__CollectApiDataRequest_api_data_instance_ "Google::Cloud::ApiHub::V1::CollectApiDataRequest#api_data \(method\)"). 
  * **plugin_instance** (::String) — Required. The plugin instance collecting the API data. Format: `projects/{project}/locations/{location}/plugins/{plugin}/instances/{instance}`. 
  * **action_id** (::String) — Required. The action ID to be used for collecting the API data. This should map to one of the action IDs specified in action configs in the plugin. 
  * **api_data** ([::Google::Cloud::ApiHub::V1::ApiData](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiData), ::Hash) — Required. The API data to be collected. 



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
    
    
    require "google/cloud/api_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApiHub::V1::CollectApiDataRequest.new
    
    # Call the collect_api_data method.
    result = client.collect_api_data request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ApiHubCollect Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client#Google__Cloud__ApiHub__V1__ApiHubCollect__Rest__Client_configure_class_ "Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration "Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ApiHubCollect REST client object.

**Yields**

  * (config) — Configure the ApiHubCollect client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Client.new do |config|
      config.timeout = 10.0
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
    
    
    def operations_client() -> ::Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::ApiHub::V1::ApiHubCollect::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-api_hub-v1/latest/Google-Cloud-ApiHub-V1-ApiHubCollect-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
