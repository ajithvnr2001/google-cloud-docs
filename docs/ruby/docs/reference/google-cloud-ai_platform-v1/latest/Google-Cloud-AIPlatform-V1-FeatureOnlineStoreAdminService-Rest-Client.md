---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client/
title: Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client (v1.49.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:33.038446+00:00
---

# Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client (v1.49.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Vertex AI V1 API - Class Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client (v1.49.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.49.0 (latest)  1.48.0  1.47.1  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.38.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.1  1.29.0  1.28.0  1.27.0  1.26.0  1.25.0  1.24.0  1.23.1  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.64.0  0.63.0  0.62.0  0.61.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.49.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.37.0  0.36.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Vertex AI V1 API class Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.

REST client for the FeatureOnlineStoreAdminService service.

The service that handles CRUD and List for resources for FeatureOnlineStore.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the FeatureOnlineStoreAdminService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all FeatureOnlineStoreAdminService clients
    ::Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the FeatureOnlineStoreAdminService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_configure_class_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration)) 



### #create_feature_online_store
    
    
    def create_feature_online_store(request, options = nil) -> ::Gapic::Operation
    def create_feature_online_store(parent: nil, feature_online_store: nil, feature_online_store_id: nil) -> ::Gapic::Operation

Creates a new FeatureOnlineStore in a given project and location.

**Overloads**
    
    
    def create_feature_online_store(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_feature_online_store` via a request object, either of type [CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureOnlineStoreRequest "Google::Cloud::AIPlatform::V1::CreateFeatureOnlineStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureOnlineStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_feature_online_store(parent: nil, feature_online_store: nil, feature_online_store_id: nil) -> ::Gapic::Operation

Pass arguments to `create_feature_online_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to create FeatureOnlineStores. Format: `projects/{project}/locations/{location}`
  * **feature_online_store** ([::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore), ::Hash) — Required. The FeatureOnlineStore to create. 
  * **feature_online_store_id** (::String) — Required. The ID to use for this FeatureOnlineStore, which will become the final component of the FeatureOnlineStore's resource name.

This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number.

The value must be unique within the project and location. 




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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateFeatureOnlineStoreRequest.new
    
    # Call the create_feature_online_store method.
    result = client.create_feature_online_store request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_feature_view
    
    
    def create_feature_view(request, options = nil) -> ::Gapic::Operation
    def create_feature_view(parent: nil, feature_view: nil, feature_view_id: nil, run_sync_immediately: nil) -> ::Gapic::Operation

Creates a new FeatureView in a given FeatureOnlineStore.

**Overloads**
    
    
    def create_feature_view(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_feature_view` via a request object, either of type [CreateFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureViewRequest "Google::Cloud::AIPlatform::V1::CreateFeatureViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::CreateFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-CreateFeatureViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_feature_view(parent: nil, feature_view: nil, feature_view_id: nil, run_sync_immediately: nil) -> ::Gapic::Operation

Pass arguments to `create_feature_view` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the FeatureOnlineStore to create FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
  * **feature_view** ([::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView), ::Hash) — Required. The FeatureView to create. 
  * **feature_view_id** (::String) — Required. The ID to use for the FeatureView, which will become the final component of the FeatureView's resource name.

This value may be up to 60 characters, and valid characters are `[a-z0-9_]`. The first character cannot be a number.

The value must be unique within a FeatureOnlineStore. 

  * **run_sync_immediately** (::Boolean) — Immutable. If set to true, one on demand sync will be run immediately, regardless whether the [FeatureView.sync_config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView#Google__Cloud__AIPlatform__V1__FeatureView_sync_config_instance_ "Google::Cloud::AIPlatform::V1::FeatureView#sync_config \(method\)") is configured or not. 



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::CreateFeatureViewRequest.new
    
    # Call the create_feature_view method.
    result = client.create_feature_view request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_feature_online_store
    
    
    def delete_feature_online_store(request, options = nil) -> ::Gapic::Operation
    def delete_feature_online_store(name: nil, force: nil) -> ::Gapic::Operation

Deletes a single FeatureOnlineStore. The FeatureOnlineStore must not contain any FeatureViews.

**Overloads**
    
    
    def delete_feature_online_store(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_online_store` via a request object, either of type [DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureOnlineStoreRequest "Google::Cloud::AIPlatform::V1::DeleteFeatureOnlineStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureOnlineStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_feature_online_store(name: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_online_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the FeatureOnlineStore to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
  * **force** (::Boolean) — If set to true, any FeatureViews and Features for this FeatureOnlineStore will also be deleted. (Otherwise, the request will only work if the FeatureOnlineStore has no FeatureViews.) 



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteFeatureOnlineStoreRequest.new
    
    # Call the delete_feature_online_store method.
    result = client.delete_feature_online_store request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_feature_view
    
    
    def delete_feature_view(request, options = nil) -> ::Gapic::Operation
    def delete_feature_view(name: nil) -> ::Gapic::Operation

Deletes a single FeatureView.

**Overloads**
    
    
    def delete_feature_view(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_view` via a request object, either of type [DeleteFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureViewRequest "Google::Cloud::AIPlatform::V1::DeleteFeatureViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::DeleteFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-DeleteFeatureViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_feature_view(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_feature_view` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the FeatureView to be deleted. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::DeleteFeatureViewRequest.new
    
    # Call the delete_feature_view method.
    result = client.delete_feature_view request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_feature_online_store
    
    
    def get_feature_online_store(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::FeatureOnlineStore
    def get_feature_online_store(name: nil) -> ::Google::Cloud::AIPlatform::V1::FeatureOnlineStore

Gets details of a single FeatureOnlineStore.

**Overloads**
    
    
    def get_feature_online_store(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::FeatureOnlineStore

Pass arguments to `get_feature_online_store` via a request object, either of type [GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureOnlineStoreRequest "Google::Cloud::AIPlatform::V1::GetFeatureOnlineStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureOnlineStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feature_online_store(name: nil) -> ::Google::Cloud::AIPlatform::V1::FeatureOnlineStore

Pass arguments to `get_feature_online_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the FeatureOnlineStore resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetFeatureOnlineStoreRequest.new
    
    # Call the get_feature_online_store method.
    result = client.get_feature_online_store request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::FeatureOnlineStore.
    p result

### #get_feature_view
    
    
    def get_feature_view(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::FeatureView
    def get_feature_view(name: nil) -> ::Google::Cloud::AIPlatform::V1::FeatureView

Gets details of a single FeatureView.

**Overloads**
    
    
    def get_feature_view(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::FeatureView

Pass arguments to `get_feature_view` via a request object, either of type [GetFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureViewRequest "Google::Cloud::AIPlatform::V1::GetFeatureViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feature_view(name: nil) -> ::Google::Cloud::AIPlatform::V1::FeatureView

Pass arguments to `get_feature_view` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the FeatureView resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetFeatureViewRequest.new
    
    # Call the get_feature_view method.
    result = client.get_feature_view request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::FeatureView.
    p result

### #get_feature_view_sync
    
    
    def get_feature_view_sync(request, options = nil) -> ::Google::Cloud::Aiplatform::V1::FeatureViewSync
    def get_feature_view_sync(name: nil) -> ::Google::Cloud::Aiplatform::V1::FeatureViewSync

Gets details of a single FeatureViewSync.

**Overloads**
    
    
    def get_feature_view_sync(request, options = nil) -> ::Google::Cloud::Aiplatform::V1::FeatureViewSync

Pass arguments to `get_feature_view_sync` via a request object, either of type [GetFeatureViewSyncRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureViewSyncRequest "Google::Cloud::AIPlatform::V1::GetFeatureViewSyncRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::GetFeatureViewSyncRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-GetFeatureViewSyncRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feature_view_sync(name: nil) -> ::Google::Cloud::Aiplatform::V1::FeatureViewSync

Pass arguments to `get_feature_view_sync` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the FeatureViewSync resource. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}/featureViewSyncs/{feature_view_sync}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Aiplatform::V1::FeatureViewSync](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-Aiplatform-V1-FeatureViewSync)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Aiplatform::V1::FeatureViewSync](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-Aiplatform-V1-FeatureViewSync)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::GetFeatureViewSyncRequest.new
    
    # Call the get_feature_view_sync method.
    result = client.get_feature_view_sync request
    
    # The returned object is of type Google::Cloud::Aiplatform::V1::FeatureViewSync.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new FeatureOnlineStoreAdminService REST client object.

**Yields**

  * (config) — Configure the FeatureOnlineStoreAdminService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_feature_online_stores
    
    
    def list_feature_online_stores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureOnlineStore>
    def list_feature_online_stores(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureOnlineStore>

Lists FeatureOnlineStores in a given project and location.

**Overloads**
    
    
    def list_feature_online_stores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureOnlineStore>

Pass arguments to `list_feature_online_stores` via a request object, either of type [ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureOnlineStoresRequest "Google::Cloud::AIPlatform::V1::ListFeatureOnlineStoresRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListFeatureOnlineStoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureOnlineStoresRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feature_online_stores(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureOnlineStore>

Pass arguments to `list_feature_online_stores` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the Location to list FeatureOnlineStores. Format: `projects/{project}/locations/{location}`
  * **filter** (::String) — 

Lists the FeatureOnlineStores that match the filter expression. The following fields are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality and key presence.

Examples:

    * `create_time > "2020-01-01" OR update_time > "2020-01-01"` FeatureOnlineStores created or updated after 2020-01-01.
    * `labels.env = "prod"` FeatureOnlineStores with label "env" set to "prod".
  * **page_size** (::Integer) — The maximum number of FeatureOnlineStores to return. The service may return fewer than this value. If unspecified, at most 100 FeatureOnlineStores will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. 
  * **page_token** (::String) — A page token, received from a previous [FeatureOnlineStoreAdminService.ListFeatureOnlineStores](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_online_stores_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_online_stores \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeatureOnlineStoreAdminService.ListFeatureOnlineStores](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_online_stores_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_online_stores \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported Fields:

    * `create_time`
    * `update_time`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListFeatureOnlineStoresRequest.new
    
    # Call the list_feature_online_stores method.
    result = client.list_feature_online_stores request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::FeatureOnlineStore.
      p item
    end

### #list_feature_view_syncs
    
    
    def list_feature_view_syncs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Aiplatform::V1::FeatureViewSync>
    def list_feature_view_syncs(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Aiplatform::V1::FeatureViewSync>

Lists FeatureViewSyncs in a given FeatureView.

**Overloads**
    
    
    def list_feature_view_syncs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Aiplatform::V1::FeatureViewSync>

Pass arguments to `list_feature_view_syncs` via a request object, either of type [ListFeatureViewSyncsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureViewSyncsRequest "Google::Cloud::AIPlatform::V1::ListFeatureViewSyncsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListFeatureViewSyncsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureViewSyncsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feature_view_syncs(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Aiplatform::V1::FeatureViewSync>

Pass arguments to `list_feature_view_syncs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`
  * **filter** (::String) — 

Lists the FeatureViewSyncs that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\"` \--> FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z.
  * **page_size** (::Integer) — The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous [FeatureOnlineStoreAdminService.ListFeatureViewSyncs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_view_syncs_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_view_syncs \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeatureOnlineStoreAdminService.ListFeatureViewSyncs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_view_syncs_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_view_syncs \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `create_time`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Aiplatform::V1::FeatureViewSync](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-Aiplatform-V1-FeatureViewSync)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Aiplatform::V1::FeatureViewSync](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-Aiplatform-V1-FeatureViewSync)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListFeatureViewSyncsRequest.new
    
    # Call the list_feature_view_syncs method.
    result = client.list_feature_view_syncs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Aiplatform::V1::FeatureViewSync.
      p item
    end

### #list_feature_views
    
    
    def list_feature_views(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureView>
    def list_feature_views(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureView>

Lists FeatureViews in a given FeatureOnlineStore.

**Overloads**
    
    
    def list_feature_views(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureView>

Pass arguments to `list_feature_views` via a request object, either of type [ListFeatureViewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureViewsRequest "Google::Cloud::AIPlatform::V1::ListFeatureViewsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::ListFeatureViewsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-ListFeatureViewsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feature_views(parent: nil, filter: nil, page_size: nil, page_token: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::AIPlatform::V1::FeatureView>

Pass arguments to `list_feature_views` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The resource name of the FeatureOnlineStore to list FeatureViews. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
  * **filter** (::String) — 

Lists the FeatureViews that match the filter expression. The following filters are supported:

    * `create_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `update_time`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.
    * `labels`: Supports key-value equality as well as key presence.

Examples:

    * `create_time > \"2020-01-31T15:30:00.000000Z\" OR update_time > \"2020-01-31T15:30:00.000000Z\"` \--> FeatureViews created or updated after 2020-01-31T15:30:00.000000Z.
    * `labels.active = yes AND labels.env = prod` \--> FeatureViews having both (active: yes) and (env: prod) labels.
    * `labels.env: *` \--> Any FeatureView which has a label with 'env' as the key.
  * **page_size** (::Integer) — The maximum number of FeatureViews to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViews will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous [FeatureOnlineStoreAdminService.ListFeatureViews](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_views_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_views \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [FeatureOnlineStoreAdminService.ListFeatureViews](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Client#Google__Cloud__AIPlatform__V1__FeatureOnlineStoreAdminService__Rest__Client_list_feature_views_instance_ "Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client#list_feature_views \(method\)") must match the call that provided the page token. 

  * **order_by** (::String) — 

A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * `feature_view_id`
    * `create_time`
    * `update_time`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::ListFeatureViewsRequest.new
    
    # Call the list_feature_views method.
    result = client.list_feature_views request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::AIPlatform::V1::FeatureView.
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



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStoreAdminService-Rest-Operations)) 



### #sync_feature_view
    
    
    def sync_feature_view(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse
    def sync_feature_view(feature_view: nil) -> ::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse

Triggers on-demand sync for the FeatureView.

**Overloads**
    
    
    def sync_feature_view(request, options = nil) -> ::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse

Pass arguments to `sync_feature_view` via a request object, either of type [SyncFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SyncFeatureViewRequest "Google::Cloud::AIPlatform::V1::SyncFeatureViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::SyncFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SyncFeatureViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def sync_feature_view(feature_view: nil) -> ::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse

Pass arguments to `sync_feature_view` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **feature_view** (::String) — Required. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SyncFeatureViewResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-SyncFeatureViewResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::SyncFeatureViewRequest.new
    
    # Call the sync_feature_view method.
    result = client.sync_feature_view request
    
    # The returned object is of type Google::Cloud::AIPlatform::V1::SyncFeatureViewResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_feature_online_store
    
    
    def update_feature_online_store(request, options = nil) -> ::Gapic::Operation
    def update_feature_online_store(feature_online_store: nil, update_mask: nil) -> ::Gapic::Operation

Updates the parameters of a single FeatureOnlineStore.

**Overloads**
    
    
    def update_feature_online_store(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_feature_online_store` via a request object, either of type [UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureOnlineStoreRequest "Google::Cloud::AIPlatform::V1::UpdateFeatureOnlineStoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateFeatureOnlineStoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureOnlineStoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_feature_online_store(feature_online_store: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_feature_online_store` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **feature_online_store** ([::Google::Cloud::AIPlatform::V1::FeatureOnlineStore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureOnlineStore), ::Hash) — Required. The FeatureOnlineStore's `name` field is used to identify the FeatureOnlineStore to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Field mask is used to specify the fields to be overwritten in the FeatureOnlineStore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields.

Updatable fields:

    * `labels`
    * `description`
    * `bigtable`
    * `bigtable.auto_scaling`
    * `bigtable.enable_multi_region_replica`



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateFeatureOnlineStoreRequest.new
    
    # Call the update_feature_online_store method.
    result = client.update_feature_online_store request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_feature_view
    
    
    def update_feature_view(request, options = nil) -> ::Gapic::Operation
    def update_feature_view(feature_view: nil, update_mask: nil) -> ::Gapic::Operation

Updates the parameters of a single FeatureView.

**Overloads**
    
    
    def update_feature_view(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_feature_view` via a request object, either of type [UpdateFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureViewRequest "Google::Cloud::AIPlatform::V1::UpdateFeatureViewRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::AIPlatform::V1::UpdateFeatureViewRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-UpdateFeatureViewRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_feature_view(feature_view: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_feature_view` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **feature_view** ([::Google::Cloud::AIPlatform::V1::FeatureView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Cloud-AIPlatform-V1-FeatureView), ::Hash) — Required. The FeatureView's `name` field is used to identify the FeatureView to be updated. Format: `projects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}`
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-ai_platform-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Field mask is used to specify the fields to be overwritten in the FeatureView resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields.

Updatable fields:

    * `labels`
    * `service_agent_type`
    * `big_query_source`
    * `big_query_source.uri`
    * `big_query_source.entity_id_columns`
    * `feature_registry_source`
    * `feature_registry_source.feature_groups`
    * `sync_config`
    * `sync_config.cron`
    * `optimized_config.automatic_resources`



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
    
    
    require "google/cloud/ai_platform/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::AIPlatform::V1::FeatureOnlineStoreAdminService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::AIPlatform::V1::UpdateFeatureViewRequest.new
    
    # Call the update_feature_view method.
    result = client.update_feature_view request
    
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
