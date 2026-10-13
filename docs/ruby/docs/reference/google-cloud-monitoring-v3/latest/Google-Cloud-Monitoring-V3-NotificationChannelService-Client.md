---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client/
title: Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::NotificationChannelService::Client (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:32.629092+00:00
---

# Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::NotificationChannelService::Client (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::NotificationChannelService::Client (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Monitoring V3 API class Google::Cloud::Monitoring::V3::NotificationChannelService::Client.

Client for the NotificationChannelService service.

The Notification Channel API provides access to configuration that controls how messages related to incidents are sent.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Monitoring::V3::NotificationChannelService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the NotificationChannelService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration "Google::Cloud::Monitoring::V3::NotificationChannelService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all NotificationChannelService clients
    ::Google::Cloud::Monitoring::V3::NotificationChannelService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the NotificationChannelService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client#Google__Cloud__Monitoring__V3__NotificationChannelService__Client_configure_class_ "Google::Cloud::Monitoring::V3::NotificationChannelService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration "Google::Cloud::Monitoring::V3::NotificationChannelService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration)) 



### #create_notification_channel
    
    
    def create_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel
    def create_notification_channel(name: nil, notification_channel: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Creates a new notification channel, representing a single notification endpoint such as an email address, SMS number, or PagerDuty service.

Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

**Overloads**
    
    
    def create_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `create_notification_channel` via a request object, either of type [CreateNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-CreateNotificationChannelRequest "Google::Cloud::Monitoring::V3::CreateNotificationChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::CreateNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-CreateNotificationChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_notification_channel(name: nil, notification_channel: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `create_notification_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]
        

This names the container into which the channel will be written, this does not name the newly created channel. The resulting channel's name will have a normalized version of this field as a prefix, but will add `/notificationChannels/[CHANNEL_ID]` to identify the channel. 

  * **notification_channel** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel), ::Hash) — Required. The definition of the `NotificationChannel` to create. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::CreateNotificationChannelRequest.new
    
    # Call the create_notification_channel method.
    result = client.create_notification_channel request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::NotificationChannel.
    p result

### #delete_notification_channel
    
    
    def delete_notification_channel(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_notification_channel(name: nil, force: nil) -> ::Google::Protobuf::Empty

Deletes a notification channel.

Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

**Overloads**
    
    
    def delete_notification_channel(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_notification_channel` via a request object, either of type [DeleteNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-DeleteNotificationChannelRequest "Google::Cloud::Monitoring::V3::DeleteNotificationChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::DeleteNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-DeleteNotificationChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_notification_channel(name: nil, force: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_notification_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — 

Required. The channel for which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
        

  * **force** (::Boolean) — If true, the notification channel will be deleted regardless of its use in alert policies (the policies will be updated to remove the channel). If false, this operation will fail if the notification channel is referenced by existing alerting policies. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::DeleteNotificationChannelRequest.new
    
    # Call the delete_notification_channel method.
    result = client.delete_notification_channel request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_notification_channel
    
    
    def get_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel
    def get_notification_channel(name: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Gets a single notification channel. The channel includes the relevant configuration details with which the channel was created. However, the response may truncate or omit passwords, API keys, or other private key matter and thus the response may not be 100% identical to the information that was supplied in the call to the create method.

**Overloads**
    
    
    def get_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `get_notification_channel` via a request object, either of type [GetNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelRequest "Google::Cloud::Monitoring::V3::GetNotificationChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::GetNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_notification_channel(name: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `get_notification_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The channel for which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]/notificationChannels/[CHANNEL_ID]
        




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::GetNotificationChannelRequest.new
    
    # Call the get_notification_channel method.
    result = client.get_notification_channel request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::NotificationChannel.
    p result

### #get_notification_channel_descriptor
    
    
    def get_notification_channel_descriptor(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor
    def get_notification_channel_descriptor(name: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor

Gets a single channel descriptor. The descriptor indicates which fields are expected / permitted for a notification channel of the given type.

**Overloads**
    
    
    def get_notification_channel_descriptor(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor

Pass arguments to `get_notification_channel_descriptor` via a request object, either of type [GetNotificationChannelDescriptorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelDescriptorRequest "Google::Cloud::Monitoring::V3::GetNotificationChannelDescriptorRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::GetNotificationChannelDescriptorRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelDescriptorRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_notification_channel_descriptor(name: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor

Pass arguments to `get_notification_channel_descriptor` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — 

Required. The channel type for which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]/notificationChannelDescriptors/[CHANNEL_TYPE]
        




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelDescriptor)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelDescriptor)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::GetNotificationChannelDescriptorRequest.new
    
    # Call the get_notification_channel_descriptor method.
    result = client.get_notification_channel_descriptor request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::NotificationChannelDescriptor.
    p result

### #get_notification_channel_verification_code
    
    
    def get_notification_channel_verification_code(request, options = nil) -> ::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse
    def get_notification_channel_verification_code(name: nil, expire_time: nil) -> ::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse

Requests a verification code for an already verified channel that can then be used in a call to VerifyNotificationChannel() on a different channel with an equivalent identity in the same or in a different project. This makes it possible to copy a channel between projects without requiring manual reverification of the channel. If the channel is not in the verified state, this method will fail (in other words, this may only be used if the SendNotificationChannelVerificationCode and VerifyNotificationChannel paths have already been used to put the given channel into the verified state).

There is no guarantee that the verification codes returned by this method will be of a similar structure or form as the ones that are delivered to the channel via SendNotificationChannelVerificationCode; while VerifyNotificationChannel() will recognize both the codes delivered via SendNotificationChannelVerificationCode() and returned from GetNotificationChannelVerificationCode(), it is typically the case that the verification codes delivered via SendNotificationChannelVerificationCode() will be shorter and also have a shorter expiration (e.g. codes such as "G-123456") whereas GetVerificationCode() will typically return a much longer, websafe base 64 encoded string that has a longer expiration time.

**Overloads**
    
    
    def get_notification_channel_verification_code(request, options = nil) -> ::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse

Pass arguments to `get_notification_channel_verification_code` via a request object, either of type [GetNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelVerificationCodeRequest "Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelVerificationCodeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_notification_channel_verification_code(name: nil, expire_time: nil) -> ::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse

Pass arguments to `get_notification_channel_verification_code` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The notification channel for which a verification code is to be generated and retrieved. This must name a channel that is already verified; if the specified channel is not verified, the request will fail. 
  * **expire_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-Timestamp), ::Hash) — The desired expiration time. If specified, the API will guarantee that the returned code will not be valid after the specified timestamp; however, the API cannot guarantee that the returned code will be valid for at least as long as the requested time (the API puts an upper bound on the amount of time for which a code may be valid). If omitted, a default expiration will be used, which may be less than the max permissible expiration (so specifying an expiration may extend the code's lifetime over omitting an expiration, even though the API does impose an upper limit on the maximum expiration that is permitted). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelVerificationCodeResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-GetNotificationChannelVerificationCodeResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeRequest.new
    
    # Call the get_notification_channel_verification_code method.
    result = client.get_notification_channel_verification_code request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::GetNotificationChannelVerificationCodeResponse.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new NotificationChannelService client object.

**Yields**

  * (config) — Configure the NotificationChannelService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_notification_channel_descriptors
    
    
    def list_notification_channel_descriptors(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor>
    def list_notification_channel_descriptors(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor>

Lists the descriptors for supported channel types. The use of descriptors makes it possible for new channel types to be dynamically added.

**Overloads**
    
    
    def list_notification_channel_descriptors(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor>

Pass arguments to `list_notification_channel_descriptors` via a request object, either of type [ListNotificationChannelDescriptorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-ListNotificationChannelDescriptorsRequest "Google::Cloud::Monitoring::V3::ListNotificationChannelDescriptorsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::ListNotificationChannelDescriptorsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-ListNotificationChannelDescriptorsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_notification_channel_descriptors(name: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor>

Pass arguments to `list_notification_channel_descriptors` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The REST resource name of the parent from which to retrieve the notification channel descriptors. The expected syntax is:
        
        projects/[PROJECT_ID_OR_NUMBER]
        

Note that this [names](https://cloud.google.com/monitoring/api/v3#project_name) the parent container in which to look for the descriptors; to retrieve a single descriptor by name, use the [GetNotificationChannelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client#Google__Cloud__Monitoring__V3__NotificationChannelService__Client_get_notification_channel_descriptor_instance_ "Google::Cloud::Monitoring::V3::NotificationChannelService::Client#get_notification_channel_descriptor \(method\)") operation, instead. 

  * **page_size** (::Integer) — The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service. 
  * **page_token** (::String) — If non-empty, `page_token` must contain a value returned as the `next_page_token` in a previous response to request the next set of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelDescriptor)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelDescriptor)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::ListNotificationChannelDescriptorsRequest.new
    
    # Call the list_notification_channel_descriptors method.
    result = client.list_notification_channel_descriptors request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Monitoring::V3::NotificationChannelDescriptor.
      p item
    end

### #list_notification_channels
    
    
    def list_notification_channels(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannel>
    def list_notification_channels(name: nil, filter: nil, order_by: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannel>

Lists the notification channels that have been created for the project. To list the types of notification channels that are supported, use the `ListNotificationChannelDescriptors` method.

**Overloads**
    
    
    def list_notification_channels(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannel>

Pass arguments to `list_notification_channels` via a request object, either of type [ListNotificationChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-ListNotificationChannelsRequest "Google::Cloud::Monitoring::V3::ListNotificationChannelsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::ListNotificationChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-ListNotificationChannelsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_notification_channels(name: nil, filter: nil, order_by: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::Monitoring::V3::NotificationChannel>

Pass arguments to `list_notification_channels` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The [project](https://cloud.google.com/monitoring/api/v3#project_name) on which to execute the request. The format is:
        
        projects/[PROJECT_ID_OR_NUMBER]
        

This names the container in which to look for the notification channels; it does not name a specific channel. To query a specific channel by REST resource name, use the [`GetNotificationChannel`](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannelService-Client#Google__Cloud__Monitoring__V3__NotificationChannelService__Client_get_notification_channel_instance_ "Google::Cloud::Monitoring::V3::NotificationChannelService::Client#get_notification_channel \(method\)") operation. 

  * **filter** (::String) — Optional. If provided, this field specifies the criteria that must be met by notification channels to be included in the response.

For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering). 

  * **order_by** (::String) — Optional. A comma-separated list of fields by which to sort the result. Supports the same set of fields as in `filter`. Entries can be prefixed with a minus sign to sort in descending rather than ascending order.

For more details, see [sorting and filtering](https://cloud.google.com/monitoring/api/v3/sorting-and-filtering). 

  * **page_size** (::Integer) — Optional. The maximum number of results to return in a single response. If not set to a positive number, a reasonable value will be chosen by the service. 
  * **page_token** (::String) — Optional. If non-empty, `page_token` must contain a value returned as the `next_page_token` in a previous response to request the next set of results. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::ListNotificationChannelsRequest.new
    
    # Call the list_notification_channels method.
    result = client.list_notification_channels request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Monitoring::V3::NotificationChannel.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #send_notification_channel_verification_code
    
    
    def send_notification_channel_verification_code(request, options = nil) -> ::Google::Protobuf::Empty
    def send_notification_channel_verification_code(name: nil) -> ::Google::Protobuf::Empty

Causes a verification code to be delivered to the channel. The code can then be supplied in `VerifyNotificationChannel` to verify the channel.

**Overloads**
    
    
    def send_notification_channel_verification_code(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `send_notification_channel_verification_code` via a request object, either of type [SendNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-SendNotificationChannelVerificationCodeRequest "Google::Cloud::Monitoring::V3::SendNotificationChannelVerificationCodeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::SendNotificationChannelVerificationCodeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-SendNotificationChannelVerificationCodeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def send_notification_channel_verification_code(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `send_notification_channel_verification_code` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The notification channel to which to send a verification code. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::SendNotificationChannelVerificationCodeRequest.new
    
    # Call the send_notification_channel_verification_code method.
    result = client.send_notification_channel_verification_code request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_notification_channel
    
    
    def update_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel
    def update_notification_channel(update_mask: nil, notification_channel: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Updates a notification channel. Fields not specified in the field mask remain unchanged.

Design your application to single-thread API calls that modify the state of notification channels in a single project. This includes calls to CreateNotificationChannel, DeleteNotificationChannel and UpdateNotificationChannel.

**Overloads**
    
    
    def update_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `update_notification_channel` via a request object, either of type [UpdateNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UpdateNotificationChannelRequest "Google::Cloud::Monitoring::V3::UpdateNotificationChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::UpdateNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UpdateNotificationChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_notification_channel(update_mask: nil, notification_channel: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `update_notification_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The fields to update. 
  * **notification_channel** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel), ::Hash) — Required. A description of the changes to be applied to the specified notification channel. The description must provide a definition for fields to be updated; the names of these fields should also be included in the `update_mask`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::UpdateNotificationChannelRequest.new
    
    # Call the update_notification_channel method.
    result = client.update_notification_channel request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::NotificationChannel.
    p result

### #verify_notification_channel
    
    
    def verify_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel
    def verify_notification_channel(name: nil, code: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Verifies a `NotificationChannel` by proving receipt of the code delivered to the channel as a result of calling `SendNotificationChannelVerificationCode`.

**Overloads**
    
    
    def verify_notification_channel(request, options = nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `verify_notification_channel` via a request object, either of type [VerifyNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-VerifyNotificationChannelRequest "Google::Cloud::Monitoring::V3::VerifyNotificationChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Monitoring::V3::VerifyNotificationChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-VerifyNotificationChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def verify_notification_channel(name: nil, code: nil) -> ::Google::Cloud::Monitoring::V3::NotificationChannel

Pass arguments to `verify_notification_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The notification channel to verify. 
  * **code** (::String) — Required. The verification code that was delivered to the channel as a result of invoking the `SendNotificationChannelVerificationCode` API method or that was retrieved from a verified channel via `GetNotificationChannelVerificationCode`. For example, one might have "G-123456" or "TKNZGhhd2EyN3I1MnRnMjRv" (in general, one is only guaranteed that the code is valid UTF-8; one should not make any assumptions regarding the structure or format of the code). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::NotificationChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-NotificationChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/monitoring/v3"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Monitoring::V3::NotificationChannelService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Monitoring::V3::VerifyNotificationChannelRequest.new
    
    # Call the verify_notification_channel method.
    result = client.verify_notification_channel request
    
    # The returned object is of type Google::Cloud::Monitoring::V3::NotificationChannel.
    p result

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
