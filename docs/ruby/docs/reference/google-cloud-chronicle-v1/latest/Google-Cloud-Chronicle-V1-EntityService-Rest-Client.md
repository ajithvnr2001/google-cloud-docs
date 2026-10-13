---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client/
title: Chronicle V1 API - Class Google::Cloud::Chronicle::V1::EntityService::Rest::Client (v1.1.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:49:03.484196+00:00
---

# Chronicle V1 API - Class Google::Cloud::Chronicle::V1::EntityService::Rest::Client (v1.1.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Chronicle V1 API - Class Google::Cloud::Chronicle::V1::EntityService::Rest::Client (v1.1.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.1.0 (latest)  1.0.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Chronicle V1 API class Google::Cloud::Chronicle::V1::EntityService::Rest::Client.

REST client for the EntityService service.

EntityService contains apis for finding entities.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Chronicle::V1::EntityService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the EntityService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration "Google::Cloud::Chronicle::V1::EntityService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all EntityService clients
    ::Google::Cloud::Chronicle::V1::EntityService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the EntityService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client#Google__Cloud__Chronicle__V1__EntityService__Rest__Client_configure_class_ "Google::Cloud::Chronicle::V1::EntityService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration "Google::Cloud::Chronicle::V1::EntityService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration)) 



### #create_watchlist
    
    
    def create_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist
    def create_watchlist(parent: nil, watchlist_id: nil, watchlist: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Creates a watchlist for the given instance. Note that there can be at most 200 watchlists per instance.

**Overloads**
    
    
    def create_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `create_watchlist` via a request object, either of type [CreateWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CreateWatchlistRequest "Google::Cloud::Chronicle::V1::CreateWatchlistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::CreateWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-CreateWatchlistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_watchlist(parent: nil, watchlist_id: nil, watchlist: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `create_watchlist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource where this watchlist will be created. Format: `projects/{project}/locations/{location}/instances/{instance}`
  * **watchlist_id** (::String) — Optional. The ID to use for the watchlist, which will become the final component of the watchlist's resource name.

This value should be 4-63 characters, and valid characters are /[a-z][0-9]-/. 

  * **watchlist** ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist), ::Hash) — Required. The watchlist to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::CreateWatchlistRequest.new
    
    # Call the create_watchlist method.
    result = client.create_watchlist request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Watchlist.
    p result

### #delete_watchlist
    
    
    def delete_watchlist(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_watchlist(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes the watchlist for the given instance.

**Overloads**
    
    
    def delete_watchlist(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_watchlist` via a request object, either of type [DeleteWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DeleteWatchlistRequest "Google::Cloud::Chronicle::V1::DeleteWatchlistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::DeleteWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-DeleteWatchlistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_watchlist(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_watchlist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the watchlist to delete. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`
  * **force** (::Boolean) — Optional. If set to true, any entities under this watchlist will also be deleted. (Otherwise, the request will only work if the watchlist has no entities.) 



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
    client = Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::DeleteWatchlistRequest.new
    
    # Call the delete_watchlist method.
    result = client.delete_watchlist request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_watchlist
    
    
    def get_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist
    def get_watchlist(name: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Gets watchlist details for the given watchlist ID.

**Overloads**
    
    
    def get_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `get_watchlist` via a request object, either of type [GetWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetWatchlistRequest "Google::Cloud::Chronicle::V1::GetWatchlistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::GetWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-GetWatchlistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_watchlist(name: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `get_watchlist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The parent, which owns this collection of watchlists. The name of the watchlist to retrieve. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::GetWatchlistRequest.new
    
    # Call the get_watchlist method.
    result = client.get_watchlist request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Watchlist.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new EntityService REST client object.

**Yields**

  * (config) — Configure the EntityService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-EntityService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_watchlists
    
    
    def list_watchlists(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Watchlist>
    def list_watchlists(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Watchlist>

Lists all watchlists for the given instance.

**Overloads**
    
    
    def list_watchlists(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Watchlist>

Pass arguments to `list_watchlists` via a request object, either of type [ListWatchlistsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListWatchlistsRequest "Google::Cloud::Chronicle::V1::ListWatchlistsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::ListWatchlistsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-ListWatchlistsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_watchlists(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Chronicle::V1::Watchlist>

Pass arguments to `list_watchlists` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent, which owns this collection of watchlists. Format: `projects/{project}/locations/{location}/instances/{instance}`
  * **page_size** (::Integer) — Optional. The maximum number of watchlists to return. The service may return fewer than this value. If unspecified, at most 200 watchlists will be returned. The maximum value is 200; values above 200 will be coerced to 200. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListWatchlists` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListWatchlists` must match the call that provided the page token. 

  * **filter** (::String) — 

Optional. Which watchlist to return in aip.dev/160 form. Currently, only the following filters are supported:

    * `watchlist_user_preferences.pinned=true`
    * `has_entity([ENTITY_INDICATOR],[ENTITY_TYPE])`
    * `has_entity([ENTITY_INDICATOR],[ENTITY_TYPE],[NAMESPACE])`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::ListWatchlistsRequest.new
    
    # Call the list_watchlists method.
    result = client.list_watchlists request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Chronicle::V1::Watchlist.
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



### #update_watchlist
    
    
    def update_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist
    def update_watchlist(watchlist: nil, update_mask: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Updates the watchlist for the given instance.

**Overloads**
    
    
    def update_watchlist(request, options = nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `update_watchlist` via a request object, either of type [UpdateWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-UpdateWatchlistRequest "Google::Cloud::Chronicle::V1::UpdateWatchlistRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Chronicle::V1::UpdateWatchlistRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-UpdateWatchlistRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_watchlist(watchlist: nil, update_mask: nil) -> ::Google::Cloud::Chronicle::V1::Watchlist

Pass arguments to `update_watchlist` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **watchlist** ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist), ::Hash) — Required. The watchlist to update.

The watchlist's `name` field is used to identify the watchlist to update. Format: `projects/{project}/locations/{location}/instances/{instance}/watchlists/{watchlist}`

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The list of fields to update. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Chronicle::V1::Watchlist](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-chronicle-v1/latest/Google-Cloud-Chronicle-V1-Watchlist)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/chronicle/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Chronicle::V1::EntityService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Chronicle::V1::UpdateWatchlistRequest.new
    
    # Call the update_watchlist method.
    result = client.update_watchlist request
    
    # The returned object is of type Google::Cloud::Chronicle::V1::Watchlist.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
