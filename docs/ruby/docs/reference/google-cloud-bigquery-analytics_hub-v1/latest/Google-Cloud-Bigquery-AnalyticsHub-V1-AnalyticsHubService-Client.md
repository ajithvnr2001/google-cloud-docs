---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client/
title: Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client (v0.20.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:00:14.273199+00:00
---

# Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client (v0.20.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Analytics Hub V1 API - Class Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client (v0.20.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.20.1 (latest)  0.20.0  0.19.0  0.18.0  0.17.0  0.16.1  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.0  0.5.2  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Analytics Hub V1 API class Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.

Client for the AnalyticsHubService service.

The `AnalyticsHubService` API facilitates data sharing within and across organizations. It allows data providers to publish listings that reference shared datasets. With Analytics Hub, users can discover and search for listings that they have access to. Subscribers can view and subscribe to listings. When you subscribe to a listing, Analytics Hub creates a linked dataset in your project.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the AnalyticsHubService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration "Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all AnalyticsHubService clients
    ::Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.configure do |config|
      config.timeout = 10.0
    end

### #approve_query_template
    
    
    def approve_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate
    def approve_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Approves a query template.

**Overloads**
    
    
    def approve_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `approve_query_template` via a request object, either of type [Google::Cloud::Bigquery::AnalyticsHub::V1::ApproveQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ApproveQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ApproveQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ApproveQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ApproveQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def approve_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `approve_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ApproveQueryTemplateRequest.new
    
    # Call the approve_query_template method.
    result = client.approve_query_template request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the AnalyticsHubService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client#Google__Cloud__Bigquery__AnalyticsHub__V1__AnalyticsHubService__Client_configure_class_ "Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration "Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration)) 



### #create_data_exchange
    
    
    def create_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange
    def create_data_exchange(parent: nil, data_exchange_id: nil, data_exchange: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Creates a new data exchange.

**Overloads**
    
    
    def create_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `create_data_exchange` via a request object, either of type [CreateDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateDataExchangeRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::CreateDataExchangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::CreateDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateDataExchangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_data_exchange(parent: nil, data_exchange_id: nil, data_exchange: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `create_data_exchange` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the data exchange. e.g. `projects/myproject/locations/us`. 
  * **data_exchange_id** (::String) — Required. The ID of the data exchange. Must contain only Unicode letters, numbers (0-9), underscores (_). Max length: 100 bytes. 
  * **data_exchange** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange), ::Hash) — Required. The data exchange to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::CreateDataExchangeRequest.new
    
    # Call the create_data_exchange method.
    result = client.create_data_exchange request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.
    p result

### #create_listing
    
    
    def create_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing
    def create_listing(parent: nil, listing_id: nil, listing: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Creates a new listing.

**Overloads**
    
    
    def create_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `create_listing` via a request object, either of type [CreateListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateListingRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::CreateListingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::CreateListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateListingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_listing(parent: nil, listing_id: nil, listing: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `create_listing` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`. 
  * **listing_id** (::String) — Required. The ID of the listing to create. Must contain only Unicode letters, numbers (0-9), underscores (_). Max length: 100 bytes. 
  * **listing** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing), ::Hash) — Required. The listing to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::CreateListingRequest.new
    
    # Call the create_listing method.
    result = client.create_listing request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::Listing.
    p result

### #create_query_template
    
    
    def create_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate
    def create_query_template(parent: nil, query_template_id: nil, query_template: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Creates a new QueryTemplate

**Overloads**
    
    
    def create_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `create_query_template` via a request object, either of type [CreateQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::CreateQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::CreateQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-CreateQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_query_template(parent: nil, query_template_id: nil, query_template: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `create_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myQueryTemplate`. 
  * **query_template_id** (::String) — Required. The ID of the QueryTemplate to create. Must contain only Unicode letters, numbers (0-9), underscores (_). Max length: 100 bytes. 
  * **query_template** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate), ::Hash) — Required. The QueryTemplate to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::CreateQueryTemplateRequest.new
    
    # Call the create_query_template method.
    result = client.create_query_template request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
    p result

### #delete_data_exchange
    
    
    def delete_data_exchange(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_data_exchange(name: nil) -> ::Google::Protobuf::Empty

Deletes an existing data exchange.

**Overloads**
    
    
    def delete_data_exchange(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_data_exchange` via a request object, either of type [DeleteDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteDataExchangeRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteDataExchangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteDataExchangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_data_exchange(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_data_exchange` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The full name of the data exchange resource that you want to delete. For example, `projects/myproject/locations/us/dataExchanges/123`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteDataExchangeRequest.new
    
    # Call the delete_data_exchange method.
    result = client.delete_data_exchange request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_listing
    
    
    def delete_listing(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_listing(name: nil, delete_commercial: nil) -> ::Google::Protobuf::Empty

Deletes a listing.

**Overloads**
    
    
    def delete_listing(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_listing` via a request object, either of type [DeleteListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteListingRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteListingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteListingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_listing(name: nil, delete_commercial: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_listing` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the listing to delete. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`. 
  * **delete_commercial** (::Boolean) — Optional. If the listing is commercial then this field must be set to true, otherwise a failure is thrown. This acts as a safety guard to avoid deleting commercial listings accidentally. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteListingRequest.new
    
    # Call the delete_listing method.
    result = client.delete_listing request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_query_template
    
    
    def delete_query_template(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_query_template(name: nil) -> ::Google::Protobuf::Empty

Deletes a query template.

**Overloads**
    
    
    def delete_query_template(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_query_template` via a request object, either of type [DeleteQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_query_template(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteQueryTemplateRequest.new
    
    # Call the delete_query_template method.
    result = client.delete_query_template request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_subscription
    
    
    def delete_subscription(request, options = nil) -> ::Gapic::Operation
    def delete_subscription(name: nil) -> ::Gapic::Operation

Deletes a subscription.

**Overloads**
    
    
    def delete_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_subscription` via a request object, either of type [DeleteSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteSubscriptionRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DeleteSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_subscription(name: nil) -> ::Gapic::Operation

Pass arguments to `delete_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the subscription to delete. e.g. projects/123/locations/us/subscriptions/456 



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
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::DeleteSubscriptionRequest.new
    
    # Call the delete_subscription method.
    result = client.delete_subscription request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_data_exchange
    
    
    def get_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange
    def get_data_exchange(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Gets the details of a data exchange.

**Overloads**
    
    
    def get_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `get_data_exchange` via a request object, either of type [GetDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetDataExchangeRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::GetDataExchangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::GetDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetDataExchangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_data_exchange(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `get_data_exchange` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the data exchange. e.g. `projects/myproject/locations/us/dataExchanges/123`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::GetDataExchangeRequest.new
    
    # Call the get_data_exchange method.
    result = client.get_data_exchange request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the IAM policy.

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #get_listing
    
    
    def get_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing
    def get_listing(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Gets the details of a listing.

**Overloads**
    
    
    def get_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `get_listing` via a request object, either of type [GetListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetListingRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::GetListingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::GetListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetListingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_listing(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `get_listing` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::GetListingRequest.new
    
    # Call the get_listing method.
    result = client.get_listing request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::Listing.
    p result

### #get_query_template
    
    
    def get_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate
    def get_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Gets a QueryTemplate

**Overloads**
    
    
    def get_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `get_query_template` via a request object, either of type [GetQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::GetQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::GetQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `get_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The parent resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::GetQueryTemplateRequest.new
    
    # Call the get_query_template method.
    result = client.get_query_template request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
    p result

### #get_subscription
    
    
    def get_subscription(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription
    def get_subscription(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription

Gets the details of a Subscription.

**Overloads**
    
    
    def get_subscription(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription

Pass arguments to `get_subscription` via a request object, either of type [GetSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetSubscriptionRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::GetSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::GetSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-GetSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_subscription(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription

Pass arguments to `get_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the subscription. e.g. projects/123/locations/us/subscriptions/456 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::GetSubscriptionRequest.new
    
    # Call the get_subscription method.
    result = client.get_subscription request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new AnalyticsHubService client object.

**Yields**

  * (config) — Configure the AnalyticsHubService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_data_exchanges
    
    
    def list_data_exchanges(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>
    def list_data_exchanges(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Lists all data exchanges in a given project and location.

**Overloads**
    
    
    def list_data_exchanges(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Pass arguments to `list_data_exchanges` via a request object, either of type [ListDataExchangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListDataExchangesRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListDataExchangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListDataExchangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListDataExchangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_data_exchanges(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Pass arguments to `list_data_exchanges` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the data exchanges. e.g. `projects/myproject/locations/us`. 
  * **page_size** (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 
  * **page_token** (::String) — Page token, returned by a previous call, to request the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListDataExchangesRequest.new
    
    # Call the list_data_exchanges method.
    result = client.list_data_exchanges request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.
      p item
    end

### #list_listings
    
    
    def list_listings(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing>
    def list_listings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing>

Lists all listings in a given project and location.

**Overloads**
    
    
    def list_listings(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing>

Pass arguments to `list_listings` via a request object, either of type [ListListingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListListingsRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListListingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListListingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListListingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_listings(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing>

Pass arguments to `list_listings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the listing. e.g. `projects/myproject/locations/us/dataExchanges/123`. 
  * **page_size** (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 
  * **page_token** (::String) — Page token, returned by a previous call, to request the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListListingsRequest.new
    
    # Call the list_listings method.
    result = client.list_listings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing.
      p item
    end

### #list_org_data_exchanges
    
    
    def list_org_data_exchanges(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>
    def list_org_data_exchanges(organization: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Lists all data exchanges from projects in a given organization and location.

**Overloads**
    
    
    def list_org_data_exchanges(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Pass arguments to `list_org_data_exchanges` via a request object, either of type [ListOrgDataExchangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListOrgDataExchangesRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListOrgDataExchangesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListOrgDataExchangesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListOrgDataExchangesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_org_data_exchanges(organization: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange>

Pass arguments to `list_org_data_exchanges` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **organization** (::String) — Required. The organization resource path of the projects containing DataExchanges. e.g. `organizations/myorg/locations/us`. 
  * **page_size** (::Integer) — The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 
  * **page_token** (::String) — Page token, returned by a previous call, to request the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListOrgDataExchangesRequest.new
    
    # Call the list_org_data_exchanges method.
    result = client.list_org_data_exchanges request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.
      p item
    end

### #list_query_templates
    
    
    def list_query_templates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate>
    def list_query_templates(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate>

Lists all QueryTemplates in a given project and location.

**Overloads**
    
    
    def list_query_templates(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate>

Pass arguments to `list_query_templates` via a request object, either of type [ListQueryTemplatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListQueryTemplatesRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListQueryTemplatesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListQueryTemplatesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListQueryTemplatesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_query_templates(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate>

Pass arguments to `list_query_templates` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the QueryTemplates. e.g. `projects/myproject/locations/us/dataExchanges/123`. 
  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response page. Leverage the page tokens to iterate through the entire collection. 
  * **page_token** (::String) — Optional. Page token, returned by a previous call, to request the next page of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListQueryTemplatesRequest.new
    
    # Call the list_query_templates method.
    result = client.list_query_templates request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
      p item
    end

### #list_shared_resource_subscriptions
    
    
    def list_shared_resource_subscriptions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>
    def list_shared_resource_subscriptions(resource: nil, include_deleted_subscriptions: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Lists all subscriptions on a given Data Exchange or Listing.

**Overloads**
    
    
    def list_shared_resource_subscriptions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Pass arguments to `list_shared_resource_subscriptions` via a request object, either of type [ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListSharedResourceSubscriptionsRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListSharedResourceSubscriptionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListSharedResourceSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListSharedResourceSubscriptionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_shared_resource_subscriptions(resource: nil, include_deleted_subscriptions: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Pass arguments to `list_shared_resource_subscriptions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — Required. Resource name of the requested target. This resource may be either a Listing or a DataExchange. e.g. projects/123/locations/us/dataExchanges/456 OR e.g. projects/123/locations/us/dataExchanges/456/listings/789 
  * **include_deleted_subscriptions** (::Boolean) — If selected, includes deleted subscriptions in the response (up to 63 days after deletion). 
  * **page_size** (::Integer) — The maximum number of results to return in a single response page. 
  * **page_token** (::String) — Page token, returned by a previous call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListSharedResourceSubscriptionsRequest.new
    
    # Call the list_shared_resource_subscriptions method.
    result = client.list_shared_resource_subscriptions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription.
      p item
    end

### #list_subscriptions
    
    
    def list_subscriptions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>
    def list_subscriptions(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Lists all subscriptions in a given project and location.

**Overloads**
    
    
    def list_subscriptions(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Pass arguments to `list_subscriptions` via a request object, either of type [ListSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListSubscriptionsRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::ListSubscriptionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::ListSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-ListSubscriptionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_subscriptions(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription>

Pass arguments to `list_subscriptions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource path of the subscription. e.g. projects/myproject/locations/us 
  * **filter** (::String) — 

An expression for filtering the results of the request. Eligible fields for filtering are:

    * `listing`
    * `data_exchange`

Alternatively, a literal wrapped in double quotes may be provided. This will be checked for an exact match against both fields above.

In all cases, the full Data Exchange or Listing resource name must be provided. Some example of using filters:

    * data_exchange="projects/myproject/locations/us/dataExchanges/123"
    * listing="projects/123/locations/us/dataExchanges/456/listings/789"
    * "projects/myproject/locations/us/dataExchanges/123"
  * **page_size** (::Integer) — The maximum number of results to return in a single response page. 
  * **page_token** (::String) — Page token, returned by a previous call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Subscription)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::ListSubscriptionsRequest.new
    
    # Call the list_subscriptions method.
    result = client.list_subscriptions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::AnalyticsHub::V1::Subscription.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-AnalyticsHubService-Operations)) 



### #refresh_subscription
    
    
    def refresh_subscription(request, options = nil) -> ::Gapic::Operation
    def refresh_subscription(name: nil) -> ::Gapic::Operation

Refreshes a Subscription to a Data Exchange. A Data Exchange can become stale when a publisher adds or removes data. This is a long-running operation as it may create many linked datasets.

**Overloads**
    
    
    def refresh_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `refresh_subscription` via a request object, either of type [RefreshSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RefreshSubscriptionRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::RefreshSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::RefreshSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RefreshSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def refresh_subscription(name: nil) -> ::Gapic::Operation

Pass arguments to `refresh_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the Subscription to refresh. e.g. `projects/subscriberproject/locations/us/subscriptions/123`



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
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::RefreshSubscriptionRequest.new
    
    # Call the refresh_subscription method.
    result = client.refresh_subscription request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #revoke_subscription
    
    
    def revoke_subscription(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse
    def revoke_subscription(name: nil, revoke_commercial: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse

Revokes a given subscription.

**Overloads**
    
    
    def revoke_subscription(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse

Pass arguments to `revoke_subscription` via a request object, either of type [RevokeSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RevokeSubscriptionRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RevokeSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def revoke_subscription(name: nil, revoke_commercial: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse

Pass arguments to `revoke_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the subscription to revoke. e.g. projects/123/locations/us/subscriptions/456 
  * **revoke_commercial** (::Boolean) — Optional. If the subscription is commercial then this field must be set to true, otherwise a failure is thrown. This acts as a safety guard to avoid revoking commercial subscriptions accidentally. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RevokeSubscriptionResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-RevokeSubscriptionResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionRequest.new
    
    # Call the revoke_subscription method.
    result = client.revoke_subscription request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::RevokeSubscriptionResponse.
    p result

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the IAM policy.

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #submit_query_template
    
    
    def submit_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate
    def submit_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Submits a query template for approval.

**Overloads**
    
    
    def submit_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `submit_query_template` via a request object, either of type [SubmitQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubmitQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::SubmitQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SubmitQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubmitQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def submit_query_template(name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `submit_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource path of the QueryTemplate. e.g. `projects/myproject/locations/us/dataExchanges/123/queryTemplates/myqueryTemplate`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::SubmitQueryTemplateRequest.new
    
    # Call the submit_query_template method.
    result = client.submit_query_template request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
    p result

### #subscribe_data_exchange
    
    
    def subscribe_data_exchange(request, options = nil) -> ::Gapic::Operation
    def subscribe_data_exchange(name: nil, destination: nil, destination_dataset: nil, subscription: nil, subscriber_contact: nil) -> ::Gapic::Operation

Creates a Subscription to a Data Clean Room. This is a long-running operation as it will create one or more linked datasets. Throws a Bad Request error if the Data Exchange does not contain any listings.

**Overloads**
    
    
    def subscribe_data_exchange(request, options = nil) -> ::Gapic::Operation

Pass arguments to `subscribe_data_exchange` via a request object, either of type [SubscribeDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeDataExchangeRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeDataExchangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeDataExchangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def subscribe_data_exchange(name: nil, destination: nil, destination_dataset: nil, subscription: nil, subscriber_contact: nil) -> ::Gapic::Operation

Pass arguments to `subscribe_data_exchange` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the Data Exchange. e.g. `projects/publisherproject/locations/us/dataExchanges/123`
  * **destination** (::String) — Required. The parent resource path of the Subscription. e.g. `projects/subscriberproject/locations/us`
  * **destination_dataset** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationDataset), ::Hash) — Optional. BigQuery destination dataset to create for the subscriber. 
  * **subscription** (::String) — Required. Name of the subscription to create. e.g. `subscription1`
  * **subscriber_contact** (::String) — Email of the subscriber. 



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
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeDataExchangeRequest.new
    
    # Call the subscribe_data_exchange method.
    result = client.subscribe_data_exchange request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #subscribe_listing
    
    
    def subscribe_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse
    def subscribe_listing(destination_dataset: nil, destination_pubsub_subscription: nil, name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse

Subscribes to a listing.

Currently, with Analytics Hub, you can create listings that reference only BigQuery datasets. Upon subscription to a listing for a BigQuery dataset, Analytics Hub creates a linked dataset in the subscriber's project.

**Overloads**
    
    
    def subscribe_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse

Pass arguments to `subscribe_listing` via a request object, either of type [SubscribeListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeListingRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeListingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def subscribe_listing(destination_dataset: nil, destination_pubsub_subscription: nil, name: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse

Pass arguments to `subscribe_listing` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **destination_dataset** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationDataset](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationDataset), ::Hash) — Input only. BigQuery destination dataset to create for the subscriber.

Note: The following parameters are mutually exclusive: `destination_dataset`, `destination_pubsub_subscription`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **destination_pubsub_subscription** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DestinationPubSubSubscription](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DestinationPubSubSubscription), ::Hash) — Input only. Destination Pub/Sub subscription to create for the subscriber.

Note: The following parameters are mutually exclusive: `destination_pubsub_subscription`, `destination_dataset`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **name** (::String) — Required. Resource name of the listing that you want to subscribe to. e.g. `projects/myproject/locations/us/dataExchanges/123/listings/456`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeListingResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-SubscribeListingResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingRequest.new
    
    # Call the subscribe_listing method.
    result = client.subscribe_listing request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::SubscribeListingResponse.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Returns the permissions that a caller has.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_data_exchange
    
    
    def update_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange
    def update_data_exchange(update_mask: nil, data_exchange: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Updates an existing data exchange.

**Overloads**
    
    
    def update_data_exchange(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `update_data_exchange` via a request object, either of type [UpdateDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateDataExchangeRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateDataExchangeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateDataExchangeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateDataExchangeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_data_exchange(update_mask: nil, data_exchange: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange

Pass arguments to `update_data_exchange` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask specifies the fields to update in the data exchange resource. The fields specified in the `updateMask` are relative to the resource and are not a full request. 
  * **data_exchange** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange), ::Hash) — Required. The data exchange to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-DataExchange)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateDataExchangeRequest.new
    
    # Call the update_data_exchange method.
    result = client.update_data_exchange request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::DataExchange.
    p result

### #update_listing
    
    
    def update_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing
    def update_listing(update_mask: nil, listing: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Updates an existing listing.

**Overloads**
    
    
    def update_listing(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `update_listing` via a request object, either of type [UpdateListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateListingRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateListingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateListingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateListingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_listing(update_mask: nil, listing: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing

Pass arguments to `update_listing` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask specifies the fields to update in the listing resource. The fields specified in the `updateMask` are relative to the resource and are not a full request. 
  * **listing** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing), ::Hash) — Required. The listing to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::Listing](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-Listing)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateListingRequest.new
    
    # Call the update_listing method.
    result = client.update_listing request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::Listing.
    p result

### #update_query_template
    
    
    def update_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate
    def update_query_template(update_mask: nil, query_template: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Updates an existing QueryTemplate

**Overloads**
    
    
    def update_query_template(request, options = nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `update_query_template` via a request object, either of type [UpdateQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateQueryTemplateRequest "Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateQueryTemplateRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateQueryTemplateRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-UpdateQueryTemplateRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_query_template(update_mask: nil, query_template: nil) -> ::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate

Pass arguments to `update_query_template` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask specifies the fields to update in the query template resource. The fields specified in the `updateMask` are relative to the resource and are not a full request. 
  * **query_template** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate), ::Hash) — Required. The QueryTemplate to update. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-analytics_hub-v1/latest/Google-Cloud-Bigquery-AnalyticsHub-V1-QueryTemplate)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/analytics_hub/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::AnalyticsHub::V1::AnalyticsHubService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::AnalyticsHub::V1::UpdateQueryTemplateRequest.new
    
    # Call the update_query_template method.
    result = client.update_query_template request
    
    # The returned object is of type Google::Cloud::Bigquery::AnalyticsHub::V1::QueryTemplate.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
