---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:12:43.872318+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.

Client for the ServingConfigService service.

Service for operations related to [ServingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig "Google::Cloud::DiscoveryEngine::V1::ServingConfig \(class\)").

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ServingConfigService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ServingConfigService clients
    ::Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ServingConfigService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client#Google__Cloud__DiscoveryEngine__V1__ServingConfigService__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ServingConfigService client object.

**Yields**

  * (config) — Configure the ServingConfigService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfigService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.new do |config|
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_serving_config
    
    
    def update_serving_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::ServingConfig
    def update_serving_config(serving_config: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1::ServingConfig

Updates a ServingConfig.

Returns a NOT_FOUND error if the ServingConfig does not exist.

**Overloads**
    
    
    def update_serving_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::ServingConfig

Pass arguments to `update_serving_config` via a request object, either of type [UpdateServingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-UpdateServingConfigRequest "Google::Cloud::DiscoveryEngine::V1::UpdateServingConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::UpdateServingConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-UpdateServingConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_serving_config(serving_config: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1::ServingConfig

Pass arguments to `update_serving_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **serving_config** ([::Google::Cloud::DiscoveryEngine::V1::ServingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig), ::Hash) — Required. The ServingConfig to update. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Indicates which fields in the provided [ServingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig "Google::Cloud::DiscoveryEngine::V1::ServingConfig \(class\)") to update. The following are NOT supported:

    * [ServingConfig.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig#Google__Cloud__DiscoveryEngine__V1__ServingConfig_name_instance_ "Google::Cloud::DiscoveryEngine::V1::ServingConfig#name \(method\)")

If not set, all supported fields are updated. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1::ServingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::ServingConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ServingConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::ServingConfigService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::UpdateServingConfigRequest.new
    
    # Call the update_serving_config method.
    result = client.update_serving_config request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1::ServingConfig.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
