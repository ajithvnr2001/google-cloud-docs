---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Rest::Client (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:25.312273+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Rest::Client (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::FeedsService::Rest::Client (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.

REST client for the FeedsService service.

FeedsService contains procedures for managing Chronicle third-party feeds.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Chronicle::V1::FeedsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the FeedsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration "Google::Cloud::Chronicle::V1::FeedsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all FeedsService clients
    ::Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the FeedsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client#Google__Cloud__Chronicle__V1__FeedsService__Rest__Client_configure_class_ "Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration "Google::Cloud::Chronicle::V1::FeedsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration)) 



### #create_feed
    
    
    def create_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed
    def create_feed(parent: nil, feed: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Creates a feed.

**Overloads**
    
    
    def create_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `create_feed` via a request object, either of type [CreateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CreateFeedRequest "Google::Cloud::Chronicle::V1::CreateFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::CreateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CreateFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_feed(parent: nil, feed: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `create_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this Feed will be created. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **feed** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed), ::Hash) — Required. Feed to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::CreateFeedRequest.new
    
    # Call the create_feed method.
    result = client.create_feed request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Feed.
    p result

### #delete_feed
    
    
    def delete_feed(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_feed(name: nil, delete_backlog: nil) -> ::Google::Protobuf::Empty

Deletes a feed.

**Overloads**
    
    
    def delete_feed(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_feed` via a request object, either of type [DeleteFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DeleteFeedRequest "Google::Cloud::Chronicle::V1::DeleteFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::DeleteFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DeleteFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_feed(name: nil, delete_backlog: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The ID of the feed to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 
  * **delete_backlog** (::Boolean) — Optional. If true, delete the uningested backlog in OOB retry queue for the feed. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::DeleteFeedRequest.new
    
    # Call the delete_feed method.
    result = client.delete_feed request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #disable_feed
    
    
    def disable_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed
    def disable_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Disable feed for ingestion. Make FeedState ARCHIVED.

**Overloads**
    
    
    def disable_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `disable_feed` via a request object, either of type [DisableFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DisableFeedRequest "Google::Cloud::Chronicle::V1::DisableFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::DisableFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DisableFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def disable_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `disable_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the feed to disable. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::DisableFeedRequest.new
    
    # Call the disable_feed method.
    result = client.disable_feed request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Feed.
    p result

### #enable_feed
    
    
    def enable_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed
    def enable_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Enable feed for ingestion.

**Overloads**
    
    
    def enable_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `enable_feed` via a request object, either of type [EnableFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EnableFeedRequest "Google::Cloud::Chronicle::V1::EnableFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::EnableFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EnableFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def enable_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `enable_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the feed to enable. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::EnableFeedRequest.new
    
    # Call the enable_feed method.
    result = client.enable_feed request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Feed.
    p result

### #fetch_service_account_for_customer
    
    
    def fetch_service_account_for_customer(request, options = nil) -> ::Google::Cloud::Chronicle::V1::FeedServiceAccount
    def fetch_service_account_for_customer(parent: nil) -> ::Google::Cloud::Chronicle::V1::FeedServiceAccount

Fetch Chronicle's service account used for ingesting data from Cloud Storage buckets.

**Overloads**
    
    
    def fetch_service_account_for_customer(request, options = nil) -> ::Google::Cloud::Chronicle::V1::FeedServiceAccount

Pass arguments to `fetch_service_account_for_customer` via a request object, either of type [Google::Cloud::Chronicle::V1::FetchServiceAccountForCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FetchServiceAccountForCustomerRequest "Google::Cloud::Chronicle::V1::FetchServiceAccountForCustomerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::FetchServiceAccountForCustomerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FetchServiceAccountForCustomerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_service_account_for_customer(parent: nil) -> ::Google::Cloud::Chronicle::V1::FeedServiceAccount

Pass arguments to `fetch_service_account_for_customer` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **parent** (::String) — Required. The parent resource where this FeedServiceAccount will be created. Format: projects/{project}/locations/{location}/instances/{instance} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::FeedServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedServiceAccount)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedServiceAccount](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedServiceAccount)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::FetchServiceAccountForCustomerRequest.new
    
    # Call the fetch_service_account_for_customer method.
    result = client.fetch_service_account_for_customer request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::FeedServiceAccount.
    p result

### #generate_secret
    
    
    def generate_secret(request, options = nil) -> ::Google::Cloud::Chronicle::V1::GenerateSecretResponse
    def generate_secret(name: nil) -> ::Google::Cloud::Chronicle::V1::GenerateSecretResponse

Generates a new secret for https push feeds which do not support jwt tokens. Secrets once generated should be copied and stored in safe place to be used while configuring https push feeds.Please note that you can always generate a new secret again for a feed using this API but it will invalidate the previously generated secret for the feed.

**Overloads**
    
    
    def generate_secret(request, options = nil) -> ::Google::Cloud::Chronicle::V1::GenerateSecretResponse

Pass arguments to `generate_secret` via a request object, either of type [GenerateSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GenerateSecretRequest "Google::Cloud::Chronicle::V1::GenerateSecretRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::GenerateSecretRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GenerateSecretRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def generate_secret(name: nil) -> ::Google::Cloud::Chronicle::V1::GenerateSecretResponse

Pass arguments to `generate_secret` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the feed to for which to generate secret. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::GenerateSecretResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GenerateSecretResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::GenerateSecretResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GenerateSecretResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::GenerateSecretRequest.new
    
    # Call the generate_secret method.
    result = client.generate_secret request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::GenerateSecretResponse.
    p result

### #get_feed
    
    
    def get_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed
    def get_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Gets a feed.

**Overloads**
    
    
    def get_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `get_feed` via a request object, either of type [GetFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetFeedRequest "Google::Cloud::Chronicle::V1::GetFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::GetFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feed(name: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `get_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The ID of the feed to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::GetFeedRequest.new
    
    # Call the get_feed method.
    result = client.get_feed request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Feed.
    p result

### #get_feed_pack
    
    
    def get_feed_pack(request, options = nil) -> ::Google::Cloud::Chronicle::V1::FeedPack
    def get_feed_pack(name: nil) -> ::Google::Cloud::Chronicle::V1::FeedPack

Gets a feed pack.

**Overloads**
    
    
    def get_feed_pack(request, options = nil) -> ::Google::Cloud::Chronicle::V1::FeedPack

Pass arguments to `get_feed_pack` via a request object, either of type [GetFeedPackRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetFeedPackRequest "Google::Cloud::Chronicle::V1::GetFeedPackRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::GetFeedPackRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetFeedPackRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_feed_pack(name: nil) -> ::Google::Cloud::Chronicle::V1::FeedPack

Pass arguments to `get_feed_pack` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The ID of the feed pack to retrieve. Format: projects/{project}/locations/{location}/instances/{instance}/feedPacks/{feedPack} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::FeedPack](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedPack)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::FeedPack](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedPack)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::GetFeedPackRequest.new
    
    # Call the get_feed_pack method.
    result = client.get_feed_pack request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::FeedPack.
    p result

### #import_push_logs
    
    
    def import_push_logs(request, options = nil) -> ::Google::Api::HttpBody
    def import_push_logs(parent: nil, http_body: nil, secret: nil) -> ::Google::Api::HttpBody

Import logs coming from https push feeds. All log entries must be valid UTF-8. A single invalid event will cause the entire request to be rejected.

**Overloads**
    
    
    def import_push_logs(request, options = nil) -> ::Google::Api::HttpBody

Pass arguments to `import_push_logs` via a request object, either of type [ImportPushLogsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ImportPushLogsRequest "Google::Cloud::Chronicle::V1::ImportPushLogsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ImportPushLogsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ImportPushLogsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def import_push_logs(parent: nil, http_body: nil, secret: nil) -> ::Google::Api::HttpBody

Pass arguments to `import_push_logs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of logs. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed} 
  * **http_body** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Api-HttpBody), ::Hash) — Required. The raw HTTP body is bound to this field. All log entries must be valid UTF-8. A single invalid event will cause the entire request to be rejected. 
  * **secret** (::String) — Immutable. The secret for the feed. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Api-HttpBody)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Api::HttpBody](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Api-HttpBody)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ImportPushLogsRequest.new
    
    # Call the import_push_logs method.
    result = client.import_push_logs request
    
    # The returned object is of type Google::Api::HttpBody.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new FeedsService REST client object.

**Yields**

  * (config) — Configure the FeedsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedsService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_feed_packs
    
    
    def list_feed_packs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedPack>
    def list_feed_packs(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedPack>

Lists Packs for which feeds can be configured.

**Overloads**
    
    
    def list_feed_packs(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedPack>

Pass arguments to `list_feed_packs` via a request object, either of type [ListFeedPacksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedPacksRequest "Google::Cloud::Chronicle::V1::ListFeedPacksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListFeedPacksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedPacksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feed_packs(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedPack>

Pass arguments to `list_feed_packs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this content pack will be created. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **page_size** (::Integer) — Optional. The maximum number of feed content packs to return. The service may return fewer than this value. If unspecified, at most 50 feed content packs will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListFeedPacks` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListFeedPacks` must match the call that provided the page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::FeedPack](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedPack)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::FeedPack](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedPack)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListFeedPacksRequest.new
    
    # Call the list_feed_packs method.
    result = client.list_feed_packs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::FeedPack.
      p item
    end

### #list_feed_source_type_schemas
    
    
    def list_feed_source_type_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema>
    def list_feed_source_type_schemas(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema>

List all FeedSourceTypeSchemas.

**Overloads**
    
    
    def list_feed_source_type_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema>

Pass arguments to `list_feed_source_type_schemas` via a request object, either of type [ListFeedSourceTypeSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedSourceTypeSchemasRequest "Google::Cloud::Chronicle::V1::ListFeedSourceTypeSchemasRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListFeedSourceTypeSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedSourceTypeSchemasRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feed_source_type_schemas(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema>

Pass arguments to `list_feed_source_type_schemas` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of FeedSourceTypeSchemas. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **page_size** (::Integer) — The maximum number of FeedSourceTypeSchemas to return. The service may return fewer than this value. If unspecified all FeedSourceTypeSchemas will be returned, meaning one FeedSourceTypeSchema for each FeedDetails.FeedSourceType. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — A page token, received from a previous `ListFeedSourceTypeSchemas` call. Provide this to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedSourceTypeSchema)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-FeedSourceTypeSchema)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListFeedSourceTypeSchemasRequest.new
    
    # Call the list_feed_source_type_schemas method.
    result = client.list_feed_source_type_schemas request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::FeedSourceTypeSchema.
      p item
    end

### #list_feeds
    
    
    def list_feeds(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Feed>
    def list_feeds(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Feed>

Lists all feeds for the customer.

**Overloads**
    
    
    def list_feeds(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Feed>

Pass arguments to `list_feeds` via a request object, either of type [ListFeedsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedsRequest "Google::Cloud::Chronicle::V1::ListFeedsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListFeedsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListFeedsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_feeds(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Feed>

Pass arguments to `list_feeds` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this Feed will be created. Format: projects/{project}/locations/{location}/instances/{instance} 
  * **page_size** (::Integer) — The maximum number of feeds to return. The service may return fewer than this value. If unspecified, at most 100 feeds will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListFeeds` call. Provide this to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListFeedsRequest.new
    
    # Call the list_feeds method.
    result = client.list_feeds request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::Feed.
      p item
    end

### #list_log_type_schemas
    
    
    def list_log_type_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::LogTypeSchema>
    def list_log_type_schemas(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::LogTypeSchema>

List all LogTypeSchemas compatible with a given FeedSourceType.

**Overloads**
    
    
    def list_log_type_schemas(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::LogTypeSchema>

Pass arguments to `list_log_type_schemas` via a request object, either of type [ListLogTypeSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListLogTypeSchemasRequest "Google::Cloud::Chronicle::V1::ListLogTypeSchemasRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListLogTypeSchemasRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListLogTypeSchemasRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_log_type_schemas(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::LogTypeSchema>

Pass arguments to `list_log_type_schemas` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of LogTypeSchemas. Format: Format: projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{feed_source_type} 
  * **page_size** (::Integer) — The maximum number of LogTypeSchemas to return. The service may return fewer than this value. If unspecified, at most 5000 LogTypeSchemas will be returned. The maximum value is 10000; values above 10000 will be coerced to 10000. 
  * **page_token** (::String) — A page token, received from a previous `ListLogTypeSchemas` call. Provide this to retrieve the subsequent page. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::LogTypeSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-LogTypeSchema)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::LogTypeSchema](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-LogTypeSchema)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListLogTypeSchemasRequest.new
    
    # Call the list_log_type_schemas method.
    result = client.list_log_type_schemas request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::LogTypeSchema.
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



### #update_feed
    
    
    def update_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed
    def update_feed(feed: nil, update_mask: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Updates the full feed.

**Overloads**
    
    
    def update_feed(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `update_feed` via a request object, either of type [UpdateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-UpdateFeedRequest "Google::Cloud::Chronicle::V1::UpdateFeedRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::UpdateFeedRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-UpdateFeedRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_feed(feed: nil, update_mask: nil) -> ::Google::Cloud::Chronicle::V1::Feed

Pass arguments to `update_feed` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **feed** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed), ::Hash) — Required. Feed to update. Updates full feed object. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Specifies which fields to update. If empty, update the full feed. To update the display name, pass only `displayName` and no other fields. To update other fields, pass a comma-separated list of fields to update and omit `displayName`. The update fails if an existing `displayName` is sent in the update request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Feed](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Feed)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::FeedsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::UpdateFeedRequest.new
    
    # Call the update_feed method.
    result = client.update_feed request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Feed.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
