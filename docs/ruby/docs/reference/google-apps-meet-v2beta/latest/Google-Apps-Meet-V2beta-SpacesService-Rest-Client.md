---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client/
title: Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::SpacesService::Rest::Client (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:58:15.866307+00:00
---

# Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::SpacesService::Rest::Client (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Meet V2BETA API - Class Google::Apps::Meet::V2beta::SpacesService::Rest::Client (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.0  0.8.1  0.7.0  0.6.1  0.5.0  0.4.0  0.3.2  0.2.2  0.1.0 

Reference documentation and code samples for the Google Meet V2BETA API class Google::Apps::Meet::V2beta::SpacesService::Rest::Client.

REST client for the SpacesService service.

REST API for services dealing with spaces.

## Inherits

  * Object 



## Includes

  * [Google::Apps::Meet::V2beta::SpacesService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SpacesService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration "Google::Apps::Meet::V2beta::SpacesService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SpacesService clients
    ::Google::Apps::Meet::V2beta::SpacesService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #batch_update_members
    
    
    def batch_update_members(request, options = nil) -> ::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse
    def batch_update_members(parent: nil, requests: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse

Updates members of one space within a batch.

**Overloads**
    
    
    def batch_update_members(request, options = nil) -> ::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse

Pass arguments to `batch_update_members` via a request object, either of type [BatchUpdateMembersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-BatchUpdateMembersRequest "Google::Apps::Meet::V2beta::BatchUpdateMembersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::BatchUpdateMembersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-BatchUpdateMembersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def batch_update_members(parent: nil, requests: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse

Pass arguments to `batch_update_members` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource shared by all Members being updated. Format: spaces/{space} 
  * **requests** (::Array<[::Google::Apps::Meet::V2beta::UpdateMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateMemberRequest), ::Hash>) — Required. The request message specifying the resources to update. A maximum of 500 members can be modified in a batch. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask), ::Hash) — 

Optional. Top-level field mask used to specify the fields to be updated in the member for all UpdateMemberRequests. There are 4 possible scenarios for top-level and child field mask:

    1. top-level and child field mask is absent: All fields provided in the requests are updated, including deleting fields not set in the requests.
    2. top-level field mask is present but child field mask is absent: The fields specified in the top-level field mask are updated.
    3. top-level and child field mask is present: The child field mask must be the same as the top-level field mask.
    4. top-level field mask is absent but child field mask is present: It isn't supported and will return an error.



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-BatchUpdateMembersResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::BatchUpdateMembersResponse](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-BatchUpdateMembersResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::BatchUpdateMembersRequest.new
    
    # Call the batch_update_members method.
    result = client.batch_update_members request
    
    # The returned object is of type Google::Apps::Meet::V2beta::BatchUpdateMembersResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SpacesService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client#Google__Apps__Meet__V2beta__SpacesService__Rest__Client_configure_class_ "Google::Apps::Meet::V2beta::SpacesService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration "Google::Apps::Meet::V2beta::SpacesService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration)) 



### #connect_active_conference
    
    
    def connect_active_conference(request, options = nil) -> ::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse
    def connect_active_conference(name: nil, offer: nil, config: nil) -> ::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse

[Developer Preview](https://developers.google.com/workspace/preview): Broker a WebRTC connection to the active conference of a space.

On success, clients must use the resulting SDP (Session Description Protocol) answer to establish a WebRTC connection. Once connected, additional functionality is available across WebRTC data channels.

See [Meet Media API overview](https://developers.google.com/workspace/meet/media-api/guides/overview) for more details about this connection.

**Overloads**
    
    
    def connect_active_conference(request, options = nil) -> ::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse

Pass arguments to `connect_active_conference` via a request object, either of type [ConnectActiveConferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConnectActiveConferenceRequest "Google::Apps::Meet::V2beta::ConnectActiveConferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ConnectActiveConferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConnectActiveConferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def connect_active_conference(name: nil, offer: nil, config: nil) -> ::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse

Pass arguments to `connect_active_conference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the space. Format: spaces/{spaceId} 
  * **offer** (::String) — Required. WebRTC SDP (Session Description Protocol) offer from the client.

The format is defined by [RFC 8866](https://www.rfc-editor.org/rfc/rfc8866) with mandatory keys defined by [RFC 8829](https://www.rfc-editor.org/rfc/rfc8829). This is the standard SDP format generated by a peer connection's createOffer() and createAnswer() methods. 

  * **config** ([::Google::Apps::Meet::V2beta::ConnectActiveConferenceRequest::ConnectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConnectActiveConferenceRequest-ConnectionConfig), ::Hash) — Optional. Additional configuration options for a Media API session. If unset, default values will be provided for the session. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConnectActiveConferenceResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ConnectActiveConferenceResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ConnectActiveConferenceRequest.new
    
    # Call the connect_active_conference method.
    result = client.connect_active_conference request
    
    # The returned object is of type Google::Apps::Meet::V2beta::ConnectActiveConferenceResponse.
    p result

### #create_member
    
    
    def create_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member
    def create_member(parent: nil, member: nil) -> ::Google::Apps::Meet::V2beta::Member

Creates a member.

This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted, this API response will default to "name,email,role,user".

**Overloads**
    
    
    def create_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `create_member` via a request object, either of type [CreateMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-CreateMemberRequest "Google::Apps::Meet::V2beta::CreateMemberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::CreateMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-CreateMemberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_member(parent: nil, member: nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `create_member` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: spaces/{space} 
  * **member** ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member), ::Hash) — Required. The member to be created. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::CreateMemberRequest.new
    
    # Call the create_member method.
    result = client.create_member request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Member.
    p result

### #create_space
    
    
    def create_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space
    def create_space(space: nil) -> ::Google::Apps::Meet::V2beta::Space

Creates a space.

**Overloads**
    
    
    def create_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `create_space` via a request object, either of type [CreateSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-CreateSpaceRequest "Google::Apps::Meet::V2beta::CreateSpaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::CreateSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-CreateSpaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_space(space: nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `create_space` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **space** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space), ::Hash) — Space to be created. As of May 2023, the input space can be empty. Later on the input space can be non-empty when space configuration is introduced. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::CreateSpaceRequest.new
    
    # Call the create_space method.
    result = client.create_space request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Space.
    p result

### #delete_member
    
    
    def delete_member(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_member(name: nil) -> ::Google::Protobuf::Empty

Deletes the member who was previously assigned roles in the space.

**Overloads**
    
    
    def delete_member(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_member` via a request object, either of type [DeleteMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-DeleteMemberRequest "Google::Apps::Meet::V2beta::DeleteMemberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::DeleteMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-DeleteMemberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_member(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_member` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: “spaces/{space}/members/{member}” 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::DeleteMemberRequest.new
    
    # Call the delete_member method.
    result = client.delete_member request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #end_active_conference
    
    
    def end_active_conference(request, options = nil) -> ::Google::Protobuf::Empty
    def end_active_conference(name: nil) -> ::Google::Protobuf::Empty

Ends an active conference (if there's one).

For an example, see [End active conference](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#end-active-conference).

**Overloads**
    
    
    def end_active_conference(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `end_active_conference` via a request object, either of type [EndActiveConferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-EndActiveConferenceRequest "Google::Apps::Meet::V2beta::EndActiveConferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::EndActiveConferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-EndActiveConferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def end_active_conference(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `end_active_conference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the space.

Format: `spaces/{space}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::EndActiveConferenceRequest.new
    
    # Call the end_active_conference method.
    result = client.end_active_conference request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_member
    
    
    def get_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member
    def get_member(name: nil) -> ::Google::Apps::Meet::V2beta::Member

Gets a member.

This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted, this API response will default to "name,email,role,user".

**Overloads**
    
    
    def get_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `get_member` via a request object, either of type [GetMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetMemberRequest "Google::Apps::Meet::V2beta::GetMemberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetMemberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_member(name: nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `get_member` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Format: “spaces/{space}/members/{member}” 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetMemberRequest.new
    
    # Call the get_member method.
    result = client.get_member request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Member.
    p result

### #get_space
    
    
    def get_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space
    def get_space(name: nil) -> ::Google::Apps::Meet::V2beta::Space

Gets details about a meeting space.

For an example, see [Get a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#get-meeting-space).

**Overloads**
    
    
    def get_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `get_space` via a request object, either of type [GetSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetSpaceRequest "Google::Apps::Meet::V2beta::GetSpaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::GetSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-GetSpaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_space(name: nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `get_space` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the space.

Format: `spaces/{space}` or `spaces/{meetingCode}`.

`{space}` is the resource identifier for the space. It's a unique, server-generated ID and is case sensitive. For example, `jQCFfuBOdN5z`.

`{meetingCode}` is an alias for the space. It's a typeable, unique character string and is non-case sensitive. For example, `abc-mnop-xyz`. The maximum length is 128 characters.

A `meetingCode` shouldn't be stored long term as it can become dissociated from a meeting space and can be reused for different meeting spaces in the future. Generally, a `meetingCode` expires 365 days after last use. For more information, see [Learn about meeting codes in Google Meet](https://support.google.com/meet/answer/10710509).

For more information, see [How Meet identifies a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#identify-meeting-space). 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::GetSpaceRequest.new
    
    # Call the get_space method.
    result = client.get_space request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Space.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SpacesService REST client object.

**Yields**

  * (config) — Configure the SpacesService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-SpacesService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_members
    
    
    def list_members(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Member>
    def list_members(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Member>

Lists members.

This API supports the `fields` parameter in [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters). When the `fields` parameter is omitted this API response will default to "name,email,role,user".

**Overloads**
    
    
    def list_members(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Member>

Pass arguments to `list_members` via a request object, either of type [ListMembersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListMembersRequest "Google::Apps::Meet::V2beta::ListMembersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::ListMembersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-ListMembersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_members(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Meet::V2beta::Member>

Pass arguments to `list_members` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Format: spaces/{space} 
  * **page_size** (::Integer) — Optional. Maximum number of members to return. The service might return fewer than this value. If unspecified or set to 0, at most 250 members are returned. The maximum value is 500; values above 500 are coerced to 500. Maximum might change in the future. 
  * **page_token** (::String) — Optional. Page token returned from previous List Call. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::ListMembersRequest.new
    
    # Call the list_members method.
    result = client.list_members request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Meet::V2beta::Member.
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



### #update_member
    
    
    def update_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member
    def update_member(member: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::Member

Updates a member.

**Overloads**
    
    
    def update_member(request, options = nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `update_member` via a request object, either of type [UpdateMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateMemberRequest "Google::Apps::Meet::V2beta::UpdateMemberRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::UpdateMemberRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateMemberRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_member(member: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::Member

Pass arguments to `update_member` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **member** ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member), ::Hash) — Required. The Member to update. Format: spaces/{space}/members/{member} 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask used to specify the fields to be updated in the member. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. In case of BatchUpdate, it must be absent or the same as the update_mask in BatchUpdateMembersRequest when UpdateMemberRequest is built as a child request of BatchUpdateMembersRequest. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Member](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Member)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::UpdateMemberRequest.new
    
    # Call the update_member method.
    result = client.update_member request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Member.
    p result

### #update_space
    
    
    def update_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space
    def update_space(space: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::Space

Updates details about a meeting space.

For an example, see [Update a meeting space](https://developers.google.com/workspace/meet/api/guides/meeting-spaces#update-meeting-space).

**Overloads**
    
    
    def update_space(request, options = nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `update_space` via a request object, either of type [UpdateSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateSpaceRequest "Google::Apps::Meet::V2beta::UpdateSpaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Meet::V2beta::UpdateSpaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-UpdateSpaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_space(space: nil, update_mask: nil) -> ::Google::Apps::Meet::V2beta::Space

Pass arguments to `update_space` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **space** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space), ::Hash) — Required. Space to be updated. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask used to specify the fields to be updated in the space. If update_mask isn't provided(not set, set with empty paths, or only has "" as paths), it defaults to update all fields provided with values in the request. Using "*" as update_mask will update all fields, including deleting fields not set in the request. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Meet::V2beta::Space](https://docs.cloud.google.com/ruby/docs/reference/google-apps-meet-v2beta/latest/Google-Apps-Meet-V2beta-Space)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/meet/v2beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Meet::V2beta::SpacesService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Meet::V2beta::UpdateSpaceRequest.new
    
    # Call the update_space method.
    result = client.update_space request
    
    # The returned object is of type Google::Apps::Meet::V2beta::Space.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
