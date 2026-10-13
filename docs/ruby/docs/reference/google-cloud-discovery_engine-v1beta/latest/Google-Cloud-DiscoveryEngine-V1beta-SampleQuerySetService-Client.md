---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client/
title: Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client (v0.30.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:17.217041+00:00
---

# Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client (v0.30.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Discovery Engine V1BETA API - Class Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client (v0.30.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.0 (latest)  0.29.0  0.28.1  0.27.0  0.26.0  0.25.0  0.24.0  0.23.1  0.22.0  0.21.0  0.20.1  0.19.1  0.18.0  0.17.0  0.16.0  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Discovery Engine V1BETA API class Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.

Client for the SampleQuerySetService service.

Service for managing {::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet SampleQuerySet}s,

## Inherits

  * Object 



## Includes

  * [Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SampleQuerySetService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SampleQuerySetService clients
    ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SampleQuerySetService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client#Google__Cloud__DiscoveryEngine__V1beta__SampleQuerySetService__Client_configure_class_ "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration)) 



### #create_sample_query_set
    
    
    def create_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet
    def create_sample_query_set(parent: nil, sample_query_set: nil, sample_query_set_id: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Creates a [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)")

**Overloads**
    
    
    def create_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `create_sample_query_set` via a request object, either of type [CreateSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CreateSampleQuerySetRequest "Google::Cloud::DiscoveryEngine::V1beta::CreateSampleQuerySetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::CreateSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CreateSampleQuerySetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_sample_query_set(parent: nil, sample_query_set: nil, sample_query_set_id: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `create_sample_query_set` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name, such as `projects/{project}/locations/{location}`. 
  * **sample_query_set** ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet), ::Hash) — Required. The [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)") to create. 
  * **sample_query_set_id** (::String) — Required. The ID to use for the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), which will become the final component of the [SampleQuerySet.name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet#Google__Cloud__DiscoveryEngine__V1beta__SampleQuerySet_name_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet#name \(method\)").

If the caller does not have permission to create the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

This field must be unique among all [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)")s with the same [parent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-CreateSampleQuerySetRequest#Google__Cloud__DiscoveryEngine__V1beta__CreateSampleQuerySetRequest_parent_instance_ "Google::Cloud::DiscoveryEngine::V1beta::CreateSampleQuerySetRequest#parent \(method\)"). Otherwise, an `ALREADY_EXISTS` error is returned.

This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 63 characters. Otherwise, an `INVALID_ARGUMENT` error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::CreateSampleQuerySetRequest.new
    
    # Call the create_sample_query_set method.
    result = client.create_sample_query_set request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet.
    p result

### #delete_sample_query_set
    
    
    def delete_sample_query_set(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_sample_query_set(name: nil) -> ::Google::Protobuf::Empty

Deletes a [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)").

**Overloads**
    
    
    def delete_sample_query_set(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_sample_query_set` via a request object, either of type [DeleteSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DeleteSampleQuerySetRequest "Google::Cloud::DiscoveryEngine::V1beta::DeleteSampleQuerySetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::DeleteSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-DeleteSampleQuerySetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_sample_query_set(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_sample_query_set` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full resource name of [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), such as `projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}`.

If the caller does not have permission to delete the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)") to delete does not exist, a `NOT_FOUND` error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::DeleteSampleQuerySetRequest.new
    
    # Call the delete_sample_query_set method.
    result = client.delete_sample_query_set request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_sample_query_set
    
    
    def get_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet
    def get_sample_query_set(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Gets a [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)").

**Overloads**
    
    
    def get_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `get_sample_query_set` via a request object, either of type [GetSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetSampleQuerySetRequest "Google::Cloud::DiscoveryEngine::V1beta::GetSampleQuerySetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::GetSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-GetSampleQuerySetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_sample_query_set(name: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `get_sample_query_set` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full resource name of [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), such as `projects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}`.

If the caller does not have permission to access the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), regardless of whether or not it exists, a PERMISSION_DENIED error is returned.

If the requested [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)") does not exist, a NOT_FOUND error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::GetSampleQuerySetRequest.new
    
    # Call the get_sample_query_set method.
    result = client.get_sample_query_set request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SampleQuerySetService client object.

**Yields**

  * (config) — Configure the SampleQuerySetService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_sample_query_sets
    
    
    def list_sample_query_sets(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet>
    def list_sample_query_sets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet>

Gets a list of {::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet SampleQuerySet}s.

**Overloads**
    
    
    def list_sample_query_sets(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet>

Pass arguments to `list_sample_query_sets` via a request object, either of type [ListSampleQuerySetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListSampleQuerySetsRequest "Google::Cloud::DiscoveryEngine::V1beta::ListSampleQuerySetsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::ListSampleQuerySetsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListSampleQuerySetsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_sample_query_sets(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet>

Pass arguments to `list_sample_query_sets` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent location resource name, such as `projects/{project}/locations/{location}`.

If the caller does not have permission to list [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)")s under this location, regardless of whether or not this location exists, a `PERMISSION_DENIED` error is returned. 

  * **page_size** (::Integer) — Maximum number of [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)")s to return. If unspecified, defaults to 100. The maximum allowed value is 1000. Values above 1000 will be coerced to 1000.

If this field is negative, an `INVALID_ARGUMENT` error is returned. 

  * **page_token** (::String) — A page token [ListSampleQuerySetsResponse.next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-ListSampleQuerySetsResponse#Google__Cloud__DiscoveryEngine__V1beta__ListSampleQuerySetsResponse_next_page_token_instance_ "Google::Cloud::DiscoveryEngine::V1beta::ListSampleQuerySetsResponse#next_page_token \(method\)"), received from a previous [SampleQuerySetService.ListSampleQuerySets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client#Google__Cloud__DiscoveryEngine__V1beta__SampleQuerySetService__Client_list_sample_query_sets_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client#list_sample_query_sets \(method\)") call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to [SampleQuerySetService.ListSampleQuerySets](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySetService-Client#Google__Cloud__DiscoveryEngine__V1beta__SampleQuerySetService__Client_list_sample_query_sets_instance_ "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client#list_sample_query_sets \(method\)") must match the call that provided the page token. Otherwise, an `INVALID_ARGUMENT` error is returned. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::ListSampleQuerySetsRequest.new
    
    # Call the list_sample_query_sets method.
    result = client.list_sample_query_sets request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet.
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



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_sample_query_set
    
    
    def update_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet
    def update_sample_query_set(sample_query_set: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Updates a [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)").

**Overloads**
    
    
    def update_sample_query_set(request, options = nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `update_sample_query_set` via a request object, either of type [UpdateSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateSampleQuerySetRequest "Google::Cloud::DiscoveryEngine::V1beta::UpdateSampleQuerySetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::DiscoveryEngine::V1beta::UpdateSampleQuerySetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-UpdateSampleQuerySetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_sample_query_set(sample_query_set: nil, update_mask: nil) -> ::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet

Pass arguments to `update_sample_query_set` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **sample_query_set** ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet), ::Hash) — Required. The sample query set to update.

If the caller does not have permission to update the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)"), regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned.

If the [SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet "Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet \(class\)") to update does not exist a `NOT_FOUND` error is returned. 

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Protobuf-FieldMask), ::Hash) — Indicates which fields in the provided imported 'sample query set' to update. If not set, will by default update all fields. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-discovery_engine-v1beta/latest/Google-Cloud-DiscoveryEngine-V1beta-SampleQuerySet)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/discovery_engine/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySetService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::DiscoveryEngine::V1beta::UpdateSampleQuerySetRequest.new
    
    # Call the update_sample_query_set method.
    result = client.update_sample_query_set request
    
    # The returned object is of type Google::Cloud::DiscoveryEngine::V1beta::SampleQuerySet.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
