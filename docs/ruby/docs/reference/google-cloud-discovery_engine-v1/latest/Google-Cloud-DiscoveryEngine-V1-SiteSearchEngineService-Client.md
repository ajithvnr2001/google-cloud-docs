---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client/
title: Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client (v2.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:06:33.676602+00:00
---

# Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client (v2.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1 API - Class Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client (v2.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.12.0 (latest)  2.11.1  2.10.1  2.9.0  2.8.0  2.7.0  2.6.2  2.5.0  2.4.0  2.3.1  2.2.0  2.1.1  2.0.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.2  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Discovery Engine V1 API class Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.

Client for the SiteSearchEngineService service.

Service for managing site search related resources.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SiteSearchEngineService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SiteSearchEngineService clients
    ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_create_target_sites
    
    
    def batch_create_target_sites(request, options = nil) -> ::Gapic::Operation
    def batch_create_target_sites(parent: nil, requests: nil) -> ::Gapic::Operation

Creates [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") in a batch.

**Overloads**
    
    
    def batch_create_target_sites(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_create_target_sites` via a request object, either of type [BatchCreateTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BatchCreateTargetSitesRequest "Google::Cloud::DiscoveryEngine::V1::BatchCreateTargetSitesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::BatchCreateTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BatchCreateTargetSitesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_create_target_sites(parent: nil, requests: nil) -> ::Gapic::Operation

Pass arguments to `batch_create_target_sites` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource shared by all TargetSites being created. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. The parent field in the CreateBookRequest messages must either be empty or match this field. 
  * **requests** (::Array<[::Google::Cloud::DiscoveryEngine::V1::CreateTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateTargetSiteRequest), ::Hash>) — Required. The request message specifying the resources to create. A maximum of 20 TargetSites can be created in a batch. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::BatchCreateTargetSitesRequest.new
    
    # Call the batch_create_target_sites method.
    result = client.batch_create_target_sites request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #batch_verify_target_sites
    
    
    def batch_verify_target_sites(request, options = nil) -> ::Gapic::Operation
    def batch_verify_target_sites(parent: nil) -> ::Gapic::Operation

Verify target sites' ownership and validity. This API sends all the target sites under site search engine for verification.

**Overloads**
    
    
    def batch_verify_target_sites(request, options = nil) -> ::Gapic::Operation

Pass arguments to `batch_verify_target_sites` via a request object, either of type [BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BatchVerifyTargetSitesRequest "Google::Cloud::DiscoveryEngine::V1::BatchVerifyTargetSitesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::BatchVerifyTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-BatchVerifyTargetSitesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def batch_verify_target_sites(parent: nil) -> ::Gapic::Operation

Pass arguments to `batch_verify_target_sites` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent resource shared by all TargetSites being verified. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::BatchVerifyTargetSitesRequest.new
    
    # Call the batch_verify_target_sites method.
    result = client.batch_verify_target_sites request
    
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

Configure the SiteSearchEngineService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client#Google__Cloud__DiscoveryEngine__V1__SiteSearchEngineService__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration)) 



### #create_sitemap
    
    
    def create_sitemap(request, options = nil) -> ::Gapic::Operation
    def create_sitemap(parent: nil, sitemap: nil) -> ::Gapic::Operation

Creates a [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)").

**Overloads**
    
    
    def create_sitemap(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_sitemap` via a request object, either of type [CreateSitemapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateSitemapRequest "Google::Cloud::DiscoveryEngine::V1::CreateSitemapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::CreateSitemapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateSitemapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_sitemap(parent: nil, sitemap: nil) -> ::Gapic::Operation

Pass arguments to `create_sitemap` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource name of the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`. 
  * **sitemap** ([::Google::Cloud::DiscoveryEngine::V1::Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap), ::Hash) — Required. The [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)") to create. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::CreateSitemapRequest.new
    
    # Call the create_sitemap method.
    result = client.create_sitemap request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_target_site
    
    
    def create_target_site(request, options = nil) -> ::Gapic::Operation
    def create_target_site(parent: nil, target_site: nil) -> ::Gapic::Operation

Creates a [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)").

**Overloads**
    
    
    def create_target_site(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_target_site` via a request object, either of type [CreateTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateTargetSiteRequest "Google::Cloud::DiscoveryEngine::V1::CreateTargetSiteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::CreateTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-CreateTargetSiteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_target_site(parent: nil, target_site: nil) -> ::Gapic::Operation

Pass arguments to `create_target_site` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource name of [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. 
  * **target_site** ([::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite), ::Hash) — Required. The [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") to create. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::CreateTargetSiteRequest.new
    
    # Call the create_target_site method.
    result = client.create_target_site request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_sitemap
    
    
    def delete_sitemap(request, options = nil) -> ::Gapic::Operation
    def delete_sitemap(name: nil) -> ::Gapic::Operation

Deletes a [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)").

**Overloads**
    
    
    def delete_sitemap(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_sitemap` via a request object, either of type [DeleteSitemapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DeleteSitemapRequest "Google::Cloud::DiscoveryEngine::V1::DeleteSitemapRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::DeleteSitemapRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DeleteSitemapRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_sitemap(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_sitemap` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full resource name of [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)"), such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/sitemaps/{sitemap}`.

If the caller does not have permission to access the [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the requested [Sitemap](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-Sitemap "Google::Cloud::DiscoveryEngine::V1::Sitemap \(class\)") does not exist, a NOT_FOUND error is returned. 




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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::DeleteSitemapRequest.new
    
    # Call the delete_sitemap method.
    result = client.delete_sitemap request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_target_site
    
    
    def delete_target_site(request, options = nil) -> ::Gapic::Operation
    def delete_target_site(name: nil) -> ::Gapic::Operation

Deletes a [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)").

**Overloads**
    
    
    def delete_target_site(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_target_site` via a request object, either of type [DeleteTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DeleteTargetSiteRequest "Google::Cloud::DiscoveryEngine::V1::DeleteTargetSiteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::DeleteTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DeleteTargetSiteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_target_site(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_target_site` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full resource name of [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`.

If the caller does not have permission to access the [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the requested [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") does not exist, a NOT_FOUND error is returned. 




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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::DeleteTargetSiteRequest.new
    
    # Call the delete_target_site method.
    result = client.delete_target_site request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #disable_advanced_site_search
    
    
    def disable_advanced_site_search(request, options = nil) -> ::Gapic::Operation
    def disable_advanced_site_search(site_search_engine: nil) -> ::Gapic::Operation

Downgrade from advanced site search to basic site search.

**Overloads**
    
    
    def disable_advanced_site_search(request, options = nil) -> ::Gapic::Operation

Pass arguments to `disable_advanced_site_search` via a request object, either of type [DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DisableAdvancedSiteSearchRequest "Google::Cloud::DiscoveryEngine::V1::DisableAdvancedSiteSearchRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::DisableAdvancedSiteSearchRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DisableAdvancedSiteSearchRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def disable_advanced_site_search(site_search_engine: nil) -> ::Gapic::Operation

Pass arguments to `disable_advanced_site_search` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **site_search_engine** (::String) — Required. Full resource name of the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::DisableAdvancedSiteSearchRequest.new
    
    # Call the disable_advanced_site_search method.
    result = client.disable_advanced_site_search request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #enable_advanced_site_search
    
    
    def enable_advanced_site_search(request, options = nil) -> ::Gapic::Operation
    def enable_advanced_site_search(site_search_engine: nil) -> ::Gapic::Operation

Upgrade from basic site search to advanced site search.

**Overloads**
    
    
    def enable_advanced_site_search(request, options = nil) -> ::Gapic::Operation

Pass arguments to `enable_advanced_site_search` via a request object, either of type [EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-EnableAdvancedSiteSearchRequest "Google::Cloud::DiscoveryEngine::V1::EnableAdvancedSiteSearchRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::EnableAdvancedSiteSearchRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-EnableAdvancedSiteSearchRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def enable_advanced_site_search(site_search_engine: nil) -> ::Gapic::Operation

Pass arguments to `enable_advanced_site_search` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **site_search_engine** (::String) — Required. Full resource name of the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/{project}/locations/{location}/dataStores/{data_store_id}/siteSearchEngine`. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::EnableAdvancedSiteSearchRequest.new
    
    # Call the enable_advanced_site_search method.
    result = client.enable_advanced_site_search request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #fetch_domain_verification_status
    
    
    def fetch_domain_verification_status(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>
    def fetch_domain_verification_status(site_search_engine: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Returns list of target sites with its domain verification status. This method can only be called under data store with BASIC_SITE_SEARCH state at the moment.

**Overloads**
    
    
    def fetch_domain_verification_status(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Pass arguments to `fetch_domain_verification_status` via a request object, either of type [FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchDomainVerificationStatusRequest "Google::Cloud::DiscoveryEngine::V1::FetchDomainVerificationStatusRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::FetchDomainVerificationStatusRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchDomainVerificationStatusRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_domain_verification_status(site_search_engine: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Pass arguments to `fetch_domain_verification_status` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **site_search_engine** (::String) — Required. The site search engine resource under which we fetch all the domain verification status. `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`. 
  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000.

If this field is negative, an INVALID_ARGUMENT error is returned. 

  * **page_token** (::String) — A page token, received from a previous `FetchDomainVerificationStatus` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchDomainVerificationStatus` must match the call that provided the page token. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::FetchDomainVerificationStatusRequest.new
    
    # Call the fetch_domain_verification_status method.
    result = client.fetch_domain_verification_status request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DiscoveryEngine::V1::TargetSite.
      p item
    end

### #fetch_sitemaps
    
    
    def fetch_sitemaps(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse
    def fetch_sitemaps(parent: nil, matcher: nil) -> ::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse

Fetch {::Google::Cloud::DiscoveryEngine::V1::Sitemap Sitemap}s in a [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)").

**Overloads**
    
    
    def fetch_sitemaps(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse

Pass arguments to `fetch_sitemaps` via a request object, either of type [FetchSitemapsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchSitemapsRequest "Google::Cloud::DiscoveryEngine::V1::FetchSitemapsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchSitemapsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_sitemaps(parent: nil, matcher: nil) -> ::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse

Pass arguments to `fetch_sitemaps` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent resource name of the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`. 
  * **matcher** ([::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsRequest::Matcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchSitemapsRequest-Matcher), ::Hash) — Optional. If specified, fetches the matching {::Google::Cloud::DiscoveryEngine::V1::Sitemap Sitemap}s. If not specified, fetches all {::Google::Cloud::DiscoveryEngine::V1::Sitemap Sitemap}s in the [DataStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-DataStore "Google::Cloud::DiscoveryEngine::V1::DataStore \(class\)"). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchSitemapsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-FetchSitemapsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::FetchSitemapsRequest.new
    
    # Call the fetch_sitemaps method.
    result = client.fetch_sitemaps request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1::FetchSitemapsResponse.
    p result

### #get_site_search_engine
    
    
    def get_site_search_engine(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine
    def get_site_search_engine(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine

Gets the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)").

**Overloads**
    
    
    def get_site_search_engine(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine

Pass arguments to `get_site_search_engine` via a request object, either of type [GetSiteSearchEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-GetSiteSearchEngineRequest "Google::Cloud::DiscoveryEngine::V1::GetSiteSearchEngineRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::GetSiteSearchEngineRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-GetSiteSearchEngineRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_site_search_engine(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine

Pass arguments to `get_site_search_engine` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.

If the caller does not have permission to access the [SiteSearchEngine], regardless of whether or not it exists, a PERMISSION_DENIED error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::GetSiteSearchEngineRequest.new
    
    # Call the get_site_search_engine method.
    result = client.get_site_search_engine request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine.
    p result

### #get_target_site
    
    
    def get_target_site(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::TargetSite
    def get_target_site(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1::TargetSite

Gets a [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)").

**Overloads**
    
    
    def get_target_site(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1::TargetSite

Pass arguments to `get_target_site` via a request object, either of type [GetTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-GetTargetSiteRequest "Google::Cloud::DiscoveryEngine::V1::GetTargetSiteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::GetTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-GetTargetSiteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_target_site(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1::TargetSite

Pass arguments to `get_target_site` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full resource name of [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine/targetSites/{target_site}`.

If the caller does not have permission to access the [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the requested [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") does not exist, a NOT_FOUND error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::GetTargetSiteRequest.new
    
    # Call the get_target_site method.
    result = client.get_target_site request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1::TargetSite.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SiteSearchEngineService client object.

**Yields**

  * (config) — Configure the SiteSearchEngineService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_target_sites
    
    
    def list_target_sites(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>
    def list_target_sites(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Gets a list of {::Google::Cloud::DiscoveryEngine::V1::TargetSite TargetSite}s.

**Overloads**
    
    
    def list_target_sites(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Pass arguments to `list_target_sites` via a request object, either of type [ListTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListTargetSitesRequest "Google::Cloud::DiscoveryEngine::V1::ListTargetSitesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::ListTargetSitesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-ListTargetSitesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_target_sites(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1::TargetSite>

Pass arguments to `list_target_sites` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent site search engine resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/siteSearchEngine`.

If the caller does not have permission to list {::Google::Cloud::DiscoveryEngine::V1::TargetSite TargetSite}s under this site search engine, regardless of whether or not this branch exists, a PERMISSION_DENIED error is returned. 

  * **page_size** (::Integer) — Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum value is 1000; values above 1000 will be coerced to 1000.

If this field is negative, an INVALID_ARGUMENT error is returned. 

  * **page_token** (::String) — A page token, received from a previous `ListTargetSites` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListTargetSites` must match the call that provided the page token. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::ListTargetSitesRequest.new
    
    # Call the list_target_sites method.
    result = client.list_target_sites request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DiscoveryEngine::V1::TargetSite.
      p item
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
    
    
    def operations_client() -> ::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngineService-Operations)) 



### #recrawl_uris
    
    
    def recrawl_uris(request, options = nil) -> ::Gapic::Operation
    def recrawl_uris(site_search_engine: nil, uris: nil, site_credential: nil) -> ::Gapic::Operation

Request on-demand recrawl for a list of URIs.

**Overloads**
    
    
    def recrawl_uris(request, options = nil) -> ::Gapic::Operation

Pass arguments to `recrawl_uris` via a request object, either of type [RecrawlUrisRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-RecrawlUrisRequest "Google::Cloud::DiscoveryEngine::V1::RecrawlUrisRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::RecrawlUrisRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-RecrawlUrisRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def recrawl_uris(site_search_engine: nil, uris: nil, site_credential: nil) -> ::Gapic::Operation

Pass arguments to `recrawl_uris` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **site_search_engine** (::String) — Required. Full resource name of the [SiteSearchEngine](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-SiteSearchEngine "Google::Cloud::DiscoveryEngine::V1::SiteSearchEngine \(class\)"), such as `projects/*/locations/*/collections/*/dataStores/*/siteSearchEngine`. 
  * **uris** (::Array<::String>) — Required. List of URIs to crawl. At most 10K URIs are supported, otherwise an INVALID_ARGUMENT error is thrown. Each URI should match at least one [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") in `site_search_engine`. 
  * **site_credential** (::String) — Optional. Credential id to use for crawling. 



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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::RecrawlUrisRequest.new
    
    # Call the recrawl_uris method.
    result = client.recrawl_uris request
    
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



### #update_target_site
    
    
    def update_target_site(request, options = nil) -> ::Gapic::Operation
    def update_target_site(target_site: nil) -> ::Gapic::Operation

Updates a [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)").

**Overloads**
    
    
    def update_target_site(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_target_site` via a request object, either of type [UpdateTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-UpdateTargetSiteRequest "Google::Cloud::DiscoveryEngine::V1::UpdateTargetSiteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1::UpdateTargetSiteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-UpdateTargetSiteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_target_site(target_site: nil) -> ::Gapic::Operation

Pass arguments to `update_target_site` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **target_site** ([::Google::Cloud::DiscoveryEngine::V1::TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite), ::Hash) — Required. The target site to update. If the caller does not have permission to update the [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the [TargetSite](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1/latest/Google-Cloud-DiscoveryEngine-V1-TargetSite "Google::Cloud::DiscoveryEngine::V1::TargetSite \(class\)") to update does not exist, a NOT_FOUND error is returned. 




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
    
    
    require "google/cloud/discovery_engine/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1::SiteSearchEngineService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1::UpdateTargetSiteRequest.new
    
    # Call the update_target_site method.
    result = client.update_target_site request
    
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
