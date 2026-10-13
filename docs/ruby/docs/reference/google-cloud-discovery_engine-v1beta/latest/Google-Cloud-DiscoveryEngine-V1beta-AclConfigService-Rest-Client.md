---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:59:05.561736+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.

REST client for the AclConfigService service.

Service for managing Acl Configuration.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AclConfigService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AclConfigService clients
    ::Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AclConfigService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client#Google__Cloud__DiscoveryEngine__V1beta__AclConfigService__Rest__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration)) 



### #get_acl_config
    
    
    def get_acl_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig
    def get_acl_config(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Gets the [AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig "Google::Cloud::DiscoveryEngine::V1beta::AclConfig \(class\)").

**Overloads**
    
    
    def get_acl_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Pass arguments to `get_acl_config` via a request object, either of type [GetAclConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetAclConfigRequest "Google::Cloud::DiscoveryEngine::V1beta::GetAclConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::GetAclConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetAclConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_acl_config(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Pass arguments to `get_acl_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of [AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig "Google::Cloud::DiscoveryEngine::V1beta::AclConfig \(class\)"), such as `projects/*/locations/*/aclConfig`.

If the caller does not have permission to access the [AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig "Google::Cloud::DiscoveryEngine::V1beta::AclConfig \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::GetAclConfigRequest.new
    
    # Call the get_acl_config method.
    result = client.get_acl_config request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::AclConfig.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AclConfigService REST client object.

**Yields**

  * (config) — Configure the AclConfigService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfigService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.new do |config|
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_acl_config
    
    
    def update_acl_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig
    def update_acl_config(acl_config: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Default ACL configuration for use in a location of a customer's project. Updates will only reflect to new data stores. Existing data stores will still use the old value.

**Overloads**
    
    
    def update_acl_config(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Pass arguments to `update_acl_config` via a request object, either of type [UpdateAclConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateAclConfigRequest "Google::Cloud::DiscoveryEngine::V1beta::UpdateAclConfigRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::UpdateAclConfigRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateAclConfigRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_acl_config(acl_config: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::AclConfig

Pass arguments to `update_acl_config` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **acl_config** ([::Google::Cloud::DiscoveryEngine::V1beta::AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig), ::Hash) 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::DiscoveryEngine::V1beta::AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::AclConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-AclConfig)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::AclConfigService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::UpdateAclConfigRequest.new
    
    # Call the update_acl_config method.
    result = client.update_acl_config request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::AclConfig.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
