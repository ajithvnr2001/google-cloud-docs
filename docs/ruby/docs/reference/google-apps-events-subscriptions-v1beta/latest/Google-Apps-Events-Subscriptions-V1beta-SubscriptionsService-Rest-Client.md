---
url: https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client/
title: Google Workspace Events V1BETA API - Class Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client (v0.6.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:34.534807+00:00
---

# Google Workspace Events V1BETA API - Class Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client (v0.6.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Workspace Events V1BETA API - Class Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client (v0.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.0 (latest)  0.5.0  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Google Workspace Events V1BETA API class Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.

REST client for the SubscriptionsService service.

A service that manages subscriptions to Google Workspace events.

## Inherits

  * Object 



## Includes

  * [Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SubscriptionsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration "Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SubscriptionsService clients
    ::Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SubscriptionsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client#Google__Apps__Events__Subscriptions__V1beta__SubscriptionsService__Rest__Client_configure_class_ "Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration "Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration)) 



### #create_subscription
    
    
    def create_subscription(request, options = nil) -> ::Gapic::Operation
    def create_subscription(subscription: nil, validate_only: nil) -> ::Gapic::Operation

Creates a Google Workspace subscription. To learn how to use this method, see [Create a Google Workspace subscription](https://developers.google.com/workspace/events/guides/create-subscription).

**Overloads**
    
    
    def create_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_subscription` via a request object, either of type [CreateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-CreateSubscriptionRequest "Google::Apps::Events::Subscriptions::V1beta::CreateSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::CreateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-CreateSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_subscription(subscription: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **subscription** ([::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription), ::Hash) — Required. The subscription resource to create. 
  * **validate_only** (::Boolean) — Optional. If set to `true`, validates and previews the request, but doesn't create the subscription. 



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
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::CreateSubscriptionRequest.new
    
    # Call the create_subscription method.
    result = client.create_subscription request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_subscription
    
    
    def delete_subscription(request, options = nil) -> ::Gapic::Operation
    def delete_subscription(name: nil, validate_only: nil, allow_missing: nil, etag: nil) -> ::Gapic::Operation

Deletes a Google Workspace subscription. To learn how to use this method, see [Delete a Google Workspace subscription](https://developers.google.com/workspace/events/guides/delete-subscription).

**Overloads**
    
    
    def delete_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_subscription` via a request object, either of type [DeleteSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-DeleteSubscriptionRequest "Google::Apps::Events::Subscriptions::V1beta::DeleteSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::DeleteSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-DeleteSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_subscription(name: nil, validate_only: nil, allow_missing: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Resource name of the subscription to delete.

Format: `subscriptions/{subscription}`

  * **validate_only** (::Boolean) — Optional. If set to `true`, validates and previews the request, but doesn't delete the subscription. 
  * **allow_missing** (::Boolean) — Optional. If set to `true` and the subscription isn't found, the request succeeds but doesn't delete the subscription. 
  * **etag** (::String) — Optional. Etag of the subscription.

If present, it must match with the server's etag. Otherwise, request fails with the status `ABORTED`. 




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
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::DeleteSubscriptionRequest.new
    
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

### #get_subscription
    
    
    def get_subscription(request, options = nil) -> ::Google::Apps::Events::Subscriptions::V1beta::Subscription
    def get_subscription(name: nil) -> ::Google::Apps::Events::Subscriptions::V1beta::Subscription

Gets details about a Google Workspace subscription. To learn how to use this method, see [Get details about a Google Workspace subscription](https://developers.google.com/workspace/events/guides/get-subscription).

**Overloads**
    
    
    def get_subscription(request, options = nil) -> ::Google::Apps::Events::Subscriptions::V1beta::Subscription

Pass arguments to `get_subscription` via a request object, either of type [GetSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-GetSubscriptionRequest "Google::Apps::Events::Subscriptions::V1beta::GetSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::GetSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-GetSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_subscription(name: nil) -> ::Google::Apps::Events::Subscriptions::V1beta::Subscription

Pass arguments to `get_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the subscription.

Format: `subscriptions/{subscription}`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::GetSubscriptionRequest.new
    
    # Call the get_subscription method.
    result = client.get_subscription request
    
    # The returned object is of type Google::Apps::Events::Subscriptions::V1beta::Subscription.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SubscriptionsService REST client object.

**Yields**

  * (config) — Configure the SubscriptionsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_subscriptions
    
    
    def list_subscriptions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Events::Subscriptions::V1beta::Subscription>
    def list_subscriptions(page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Events::Subscriptions::V1beta::Subscription>

Lists Google Workspace subscriptions. To learn how to use this method, see [List Google Workspace subscriptions](https://developers.google.com/workspace/events/guides/list-subscriptions).

**Overloads**
    
    
    def list_subscriptions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Events::Subscriptions::V1beta::Subscription>

Pass arguments to `list_subscriptions` via a request object, either of type [ListSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-ListSubscriptionsRequest "Google::Apps::Events::Subscriptions::V1beta::ListSubscriptionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::ListSubscriptionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-ListSubscriptionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_subscriptions(page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Apps::Events::Subscriptions::V1beta::Subscription>

Pass arguments to `list_subscriptions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **page_size** (::Integer) — Optional. The maximum number of subscriptions to return. The service might return fewer than this value.

If unspecified or set to `0`, up to 50 subscriptions are returned.

The maximum value is 100. If you specify a value more than 100, the system only returns 100 subscriptions. 

  * **page_token** (::String) — Optional. A page token, received from a previous list subscriptions call. Provide this parameter to retrieve the subsequent page.

When paginating, the filter value should match the call that provided the page token. Passing a different value might lead to unexpected results. 

  * **filter** (::String) — Required. A query filter.

You can filter subscriptions by event type (`event_types`) and target resource (`target_resource`).

You must specify at least one event type in your query. To filter for multiple event types, use the `OR` operator.

To filter by both event type and target resource, use the `AND` operator and specify the full resource name, such as `//chat.googleapis.com/spaces/{space}`.

For example, the following queries are valid:

``` event_types:"google.workspace.chat.membership.v1.updated" OR event_types:"google.workspace.chat.message.v1.created"

event_types:"google.workspace.chat.message.v1.created" AND target_resource="//chat.googleapis.com/spaces/{space}"

( event_types:"google.workspace.chat.membership.v1.updated" OR event_types:"google.workspace.chat.message.v1.created" ) AND target_resource="//chat.googleapis.com/spaces/{space}" ```

The server rejects invalid queries with an `INVALID_ARGUMENT` error. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::ListSubscriptionsRequest.new
    
    # Call the list_subscriptions method.
    result = client.list_subscriptions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Apps::Events::Subscriptions::V1beta::Subscription.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-SubscriptionsService-Rest-Operations)) 



### #reactivate_subscription
    
    
    def reactivate_subscription(request, options = nil) -> ::Gapic::Operation
    def reactivate_subscription(name: nil) -> ::Gapic::Operation

Reactivates a suspended Google Workspace subscription.

This method resets your subscription's `State` field to `ACTIVE`. Before you use this method, you must fix the error that suspended the subscription. This method will ignore or reject any subscription that isn't currently in a suspended state. To learn how to use this method, see [Reactivate a Google Workspace subscription](https://developers.google.com/workspace/events/guides/reactivate-subscription).

**Overloads**
    
    
    def reactivate_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `reactivate_subscription` via a request object, either of type [ReactivateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-ReactivateSubscriptionRequest "Google::Apps::Events::Subscriptions::V1beta::ReactivateSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::ReactivateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-ReactivateSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def reactivate_subscription(name: nil) -> ::Gapic::Operation

Pass arguments to `reactivate_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Resource name of the subscription.

Format: `subscriptions/{subscription}`




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
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::ReactivateSubscriptionRequest.new
    
    # Call the reactivate_subscription method.
    result = client.reactivate_subscription request
    
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



### #update_subscription
    
    
    def update_subscription(request, options = nil) -> ::Gapic::Operation
    def update_subscription(subscription: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Updates or renews a Google Workspace subscription. To learn how to use this method, see [Update or renew a Google Workspace subscription](https://developers.google.com/workspace/events/guides/update-subscription).

**Overloads**
    
    
    def update_subscription(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_subscription` via a request object, either of type [UpdateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-UpdateSubscriptionRequest "Google::Apps::Events::Subscriptions::V1beta::UpdateSubscriptionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Apps::Events::Subscriptions::V1beta::UpdateSubscriptionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-UpdateSubscriptionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_subscription(subscription: nil, update_mask: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `update_subscription` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **subscription** ([::Google::Apps::Events::Subscriptions::V1beta::Subscription](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription), ::Hash) — Required. The subscription to update.

The subscription's `name` field is used to identify the subscription to update. 

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The field to update. If omitted, updates any fields included in the request.

You can update one of the following fields in a subscription:

    * [`expire_time`](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription#Google__Apps__Events__Subscriptions__V1beta__Subscription_expire_time_instance_ "Google::Apps::Events::Subscriptions::V1beta::Subscription#expire_time \(method\)"): The timestamp when the subscription expires.
    * [`ttl`](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription#Google__Apps__Events__Subscriptions__V1beta__Subscription_ttl_instance_ "Google::Apps::Events::Subscriptions::V1beta::Subscription#ttl \(method\)"): The time-to-live (TTL) or duration of the subscription.
    * [`event_types`](https://docs.cloud.google.com/ruby/docs/reference/google-apps-events-subscriptions-v1beta/latest/Google-Apps-Events-Subscriptions-V1beta-Subscription#Google__Apps__Events__Subscriptions__V1beta__Subscription_event_types_instance_ "Google::Apps::Events::Subscriptions::V1beta::Subscription#event_types \(method\)"): The list of event types to receive about the target resource.

To fully replace the subscription (the equivalent of `PUT`), use `*`. Any omitted fields are updated with empty values. 

  * **validate_only** (::Boolean) — Optional. If set to `true`, validates and previews the request, but doesn't update the subscription. 



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
    
    
    require "google/apps/events/subscriptions/v1beta"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Apps::Events::Subscriptions::V1beta::SubscriptionsService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Apps::Events::Subscriptions::V1beta::UpdateSubscriptionRequest.new
    
    # Call the update_subscription method.
    result = client.update_subscription request
    
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

Last updated 2026-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-26 UTC."],[],[]] 
