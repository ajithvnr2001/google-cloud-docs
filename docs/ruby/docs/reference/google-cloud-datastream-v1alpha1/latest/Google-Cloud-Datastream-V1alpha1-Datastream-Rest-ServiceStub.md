---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Datastream-Rest-ServiceStub/
title: Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Datastream::Rest::ServiceStub (v0.15.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:19.696212+00:00
---

# Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Datastream::Rest::ServiceStub (v0.15.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Datastream-Rest-ServiceStub/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Datastream V1alpha1 API - Class Google::Cloud::Datastream::V1alpha1::Datastream::Rest::ServiceStub (v0.15.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.15.1 (latest)  0.15.0  0.14.0  0.13.1  0.12.0  0.11.1  0.10.1  0.9.0  0.8.0  0.7.1  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Datastream V1alpha1 API class Google::Cloud::Datastream::V1alpha1::Datastream::Rest::ServiceStub.

REST service stub for the Datastream service. Service stub contains baseline method implementations including transcoding, making the REST call, and deserialing the response.

## Inherits

  * Object 



## Methods 

### #create_connection_profile
    
    
    def create_connection_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_connection_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::CreateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreateConnectionProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_private_connection
    
    
    def create_private_connection(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_private_connection REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::CreatePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreatePrivateConnectionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_route
    
    
    def create_route(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_route REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::CreateRouteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreateRouteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #create_stream
    
    
    def create_stream(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the create_stream REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::CreateStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-CreateStreamRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_connection_profile
    
    
    def delete_connection_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_connection_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::DeleteConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DeleteConnectionProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_private_connection
    
    
    def delete_private_connection(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_private_connection REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::DeletePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DeletePrivateConnectionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_route
    
    
    def delete_route(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_route REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::DeleteRouteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DeleteRouteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #delete_stream
    
    
    def delete_stream(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the delete_stream REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::DeleteStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DeleteStreamRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #discover_connection_profile
    
    
    def discover_connection_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::DiscoverConnectionProfileResponse

Baseline implementation for the discover_connection_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::DiscoverConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DiscoverConnectionProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::DiscoverConnectionProfileResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DiscoverConnectionProfileResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::DiscoverConnectionProfileResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-DiscoverConnectionProfileResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #endpoint
    
    
    def endpoint() -> String

The effective endpoint

**Returns**

  * (String) 



### #fetch_errors
    
    
    def fetch_errors(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the fetch_errors REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::FetchErrorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchErrorsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #fetch_static_ips
    
    
    def fetch_static_ips(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse

Baseline implementation for the fetch_static_ips REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::FetchStaticIpsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchStaticIpsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchStaticIpsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::FetchStaticIpsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-FetchStaticIpsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_connection_profile
    
    
    def get_connection_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::ConnectionProfile

Baseline implementation for the get_connection_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::GetConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-GetConnectionProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ConnectionProfile)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ConnectionProfile)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_private_connection
    
    
    def get_private_connection(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::PrivateConnection

Baseline implementation for the get_private_connection REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::GetPrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-GetPrivateConnectionRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-PrivateConnection)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-PrivateConnection)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_route
    
    
    def get_route(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::Route

Baseline implementation for the get_route REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::GetRouteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-GetRouteRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Route)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Route](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Route)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #get_stream
    
    
    def get_stream(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::Stream

Baseline implementation for the get_stream REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::GetStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-GetStreamRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::Stream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::Stream](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-Stream)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_connection_profiles
    
    
    def list_connection_profiles(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::ListConnectionProfilesResponse

Baseline implementation for the list_connection_profiles REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::ListConnectionProfilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListConnectionProfilesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::ListConnectionProfilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListConnectionProfilesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::ListConnectionProfilesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListConnectionProfilesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_private_connections
    
    
    def list_private_connections(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::ListPrivateConnectionsResponse

Baseline implementation for the list_private_connections REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::ListPrivateConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListPrivateConnectionsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::ListPrivateConnectionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListPrivateConnectionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::ListPrivateConnectionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListPrivateConnectionsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_routes
    
    
    def list_routes(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::ListRoutesResponse

Baseline implementation for the list_routes REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::ListRoutesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListRoutesRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::ListRoutesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListRoutesResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::ListRoutesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListRoutesResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #list_streams
    
    
    def list_streams(request_pb, options = nil) { |result, operation| ... } -> ::Google::Cloud::Datastream::V1alpha1::ListStreamsResponse

Baseline implementation for the list_streams REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::ListStreamsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListStreamsRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Datastream::V1alpha1::ListStreamsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListStreamsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Datastream::V1alpha1::ListStreamsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-ListStreamsResponse)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #logger
    
    
    def logger(stub: false) -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_connection_profile
    
    
    def update_connection_profile(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_connection_profile REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::UpdateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-UpdateConnectionProfileRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



### #update_stream
    
    
    def update_stream(request_pb, options = nil) { |result, operation| ... } -> ::Google::Longrunning::Operation

Baseline implementation for the update_stream REST call

**Parameters**

  * **request_pb** ([::Google::Cloud::Datastream::V1alpha1::UpdateStreamRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Cloud-Datastream-V1alpha1-UpdateStreamRequest)) — A request object representing the call parameters. Required. 
  * **options** (::Gapic::CallOptions) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Longrunning::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-datastream-v1alpha1/latest/Google-Longrunning-Operation)) — A result object deserialized from the server's reply 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
