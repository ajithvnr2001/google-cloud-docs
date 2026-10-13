---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client/
title: Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ServiceHealth::Client (v2.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:08:58.584081+00:00
---

# Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ServiceHealth::Client (v2.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Service Health V1 API - Class Google::Cloud::ServiceHealth::V1::ServiceHealth::Client (v2.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.5.1 (latest)  2.5.0  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.0  1.2.1  1.1.0  1.0.2  0.2.0  0.1.2 

Reference documentation and code samples for the Service Health V1 API class Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.

Client for the ServiceHealth service.

Request service health events relevant to your Google Cloud project.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ServiceHealth::V1::ServiceHealth::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ServiceHealth Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration "Google::Cloud::ServiceHealth::V1::ServiceHealth::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ServiceHealth clients
    ::Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ServiceHealth Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client#Google__Cloud__ServiceHealth__V1__ServiceHealth__Client_configure_class_ "Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration "Google::Cloud::ServiceHealth::V1::ServiceHealth::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration)) 



### #get_event
    
    
    def get_event(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::Event
    def get_event(name: nil) -> ::Google::Cloud::ServiceHealth::V1::Event

Retrieves a resource containing information about an event.

**Overloads**
    
    
    def get_event(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::Event

Pass arguments to `get_event` via a request object, either of type [GetEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetEventRequest "Google::Cloud::ServiceHealth::V1::GetEventRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::GetEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetEventRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_event(name: nil) -> ::Google::Cloud::ServiceHealth::V1::Event

Pass arguments to `get_event` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Unique name of the event in this scope including project and location using the form `projects/{project_id}/locations/{location}/events/{event_id}`.

`project_id` \- Project ID of the project that contains the event.   
`location` \- The location to get the service health events from.   
`event_id` \- Event ID to retrieve. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ServiceHealth::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ServiceHealth::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::GetEventRequest.new
    
    # Call the get_event method.
    result = client.get_event request
    
    # The returned object is of type Google::Cloud::ServiceHealth::V1::Event.
    p result

### #get_organization_event
    
    
    def get_organization_event(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationEvent
    def get_organization_event(name: nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationEvent

Retrieves a resource containing information about an event affecting an organization .

**Overloads**
    
    
    def get_organization_event(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationEvent

Pass arguments to `get_organization_event` via a request object, either of type [GetOrganizationEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetOrganizationEventRequest "Google::Cloud::ServiceHealth::V1::GetOrganizationEventRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::GetOrganizationEventRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetOrganizationEventRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_organization_event(name: nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationEvent

Pass arguments to `get_organization_event` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Unique name of the event in this scope including organization and event ID using the form `organizations/{organization_id}/locations/locations/global/organizationEvents/{event_id}`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).  
`event_id` \- Organization event ID to retrieve. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ServiceHealth::V1::OrganizationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationEvent)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ServiceHealth::V1::OrganizationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationEvent)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::GetOrganizationEventRequest.new
    
    # Call the get_organization_event method.
    result = client.get_organization_event request
    
    # The returned object is of type Google::Cloud::ServiceHealth::V1::OrganizationEvent.
    p result

### #get_organization_impact
    
    
    def get_organization_impact(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationImpact
    def get_organization_impact(name: nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationImpact

Retrieves a resource containing information about impact to an asset under an organization affected by a service health event.

**Overloads**
    
    
    def get_organization_impact(request, options = nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationImpact

Pass arguments to `get_organization_impact` via a request object, either of type [GetOrganizationImpactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetOrganizationImpactRequest "Google::Cloud::ServiceHealth::V1::GetOrganizationImpactRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::GetOrganizationImpactRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-GetOrganizationImpactRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_organization_impact(name: nil) -> ::Google::Cloud::ServiceHealth::V1::OrganizationImpact

Pass arguments to `get_organization_impact` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the resource using the form `organizations/{organization_id}/locations/global/organizationImpacts/{organization_impact_id}`.

`organization_id` \- ID (number) of the organization that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).  
`organization_impact_id` \- ID of the [OrganizationImpact resource](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact). 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::ServiceHealth::V1::OrganizationImpact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationImpact)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::ServiceHealth::V1::OrganizationImpact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationImpact)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::GetOrganizationImpactRequest.new
    
    # Call the get_organization_impact method.
    result = client.get_organization_impact request
    
    # The returned object is of type Google::Cloud::ServiceHealth::V1::OrganizationImpact.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ServiceHealth client object.

**Yields**

  * (config) — Configure the ServiceHealth client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ServiceHealth-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new do |config|
      config.timeout = 10.0
    end

### #list_events
    
    
    def list_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::Event>
    def list_events(parent: nil, page_size: nil, page_token: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::Event>

Lists events under a given project and location.

**Overloads**
    
    
    def list_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::Event>

Pass arguments to `list_events` via a request object, either of type [ListEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListEventsRequest "Google::Cloud::ServiceHealth::V1::ListEventsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::ListEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListEventsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_events(parent: nil, page_size: nil, page_token: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::Event>

Pass arguments to `list_events` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value using the form `projects/{project_id}/locations/{location}/events`.

`project_id` \- ID of the project for which to list service health events. `location` \- The location to get the service health events from. To retrieve service health events of category = INCIDENT, use `location` = `global`. 

  * **page_size** (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are 1 to 100, inclusive. (The default value is 10.) If more results are available, the service returns a next_page_token that you can use to get the next page of results in subsequent list requests. The service may return fewer events than the requested page_size. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. Provide Page token returned by a previous `ListEvents` call to retrieve the next page of results. When paginating, all other parameters provided to `ListEvents` must match the call that provided the page token. 
  * **filter** (::String) — Optional. A filter expression that filters resources listed in the response. The expression takes the following forms:   


    * field=value for `category` and `state`  

    * field <, >, <=, or >= value for `update_time`   
Examples: `category=INCIDENT`, `update_time>="2000-01-01T11:30:00-04:00"`, `event_impacts.product.product_name:"Eventarc"`   


Multiple filter queries are separated by spaces. Example: `category=INCIDENT state=ACTIVE`.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.

Filter is supported for the following fields: `category`, `state`, `update_time`, `event_impacts.product.product_name`

  * **view** ([::Google::Cloud::ServiceHealth::V1::EventView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-EventView)) — Optional. Event fields to include in response. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::Event](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-Event)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::ListEventsRequest.new
    
    # Call the list_events method.
    result = client.list_events request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ServiceHealth::V1::Event.
      p item
    end

### #list_organization_events
    
    
    def list_organization_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationEvent>
    def list_organization_events(parent: nil, page_size: nil, page_token: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationEvent>

Lists organization events under a given organization and location.

**Overloads**
    
    
    def list_organization_events(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationEvent>

Pass arguments to `list_organization_events` via a request object, either of type [ListOrganizationEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationEventsRequest "Google::Cloud::ServiceHealth::V1::ListOrganizationEventsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::ListOrganizationEventsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationEventsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_organization_events(parent: nil, page_size: nil, page_token: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationEvent>

Pass arguments to `list_organization_events` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value using the form `organizations/{organization_id}/locations/{location}/organizationEvents`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).  
`location` \- The location to get the service health events from. To retrieve service health events of category = INCIDENT, use `location` = `global`. 

  * **page_size** (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are `1` to `100`, inclusive. (The default value is `10`.) If more results are available, the service returns a `next_page_token` that you can use to get the next page of results in subsequent list requests. The service may return fewer events than the requested `page_size`. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return.

Provide Page token returned by a previous `ListOrganizationEvents` call to retrieve the next page of results.

When paginating, all other parameters provided to `ListOrganizationEvents` must match the call that provided the page token. 

  * **filter** (::String) — Optional. A filter expression that filters resources listed in the response. The expression takes the following forms:

    * field=value for `category` and `state`
    * field <, >, <=, or >= value for `update_time`

Examples: `category=INCIDENT`, `update_time>="2000-01-01T11:30:00-04:00"`

Multiple filter queries are space-separated. Example: `category=INCIDENT state=ACTIVE`.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly.

Filter is supported for the following fields: `category`, `state`, `update_time`

  * **view** ([::Google::Cloud::ServiceHealth::V1::OrganizationEventView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationEventView)) — Optional. OrganizationEvent fields to include in response. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::OrganizationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationEvent)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::OrganizationEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationEvent)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::ListOrganizationEventsRequest.new
    
    # Call the list_organization_events method.
    result = client.list_organization_events request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ServiceHealth::V1::OrganizationEvent.
      p item
    end

### #list_organization_impacts
    
    
    def list_organization_impacts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationImpact>
    def list_organization_impacts(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationImpact>

Lists assets impacted by organization events under a given organization and location.

**Overloads**
    
    
    def list_organization_impacts(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationImpact>

Pass arguments to `list_organization_impacts` via a request object, either of type [ListOrganizationImpactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationImpactsRequest "Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-ListOrganizationImpactsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_organization_impacts(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::ServiceHealth::V1::OrganizationImpact>

Pass arguments to `list_organization_impacts` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent value using the form `organizations/{organization_id}/locations/{location}/organizationImpacts`.

`organization_id` \- ID (number) of the project that contains the event. To get your `organization_id`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). 

  * **page_size** (::Integer) — Optional. The maximum number of events that should be returned. Acceptable values are `1` to `100`, inclusive. The default value is `10`.

If more results are available, the service returns a `next_page_token` that can be used to get the next page of results in subsequent list requests. The service may return fewer [impacts](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/organizations.locations.organizationImpacts#OrganizationImpact) than the requested `page_size`. 

  * **page_token** (::String) — Optional. A token identifying a page of results the server should return.

Provide `page_token` returned by a previous `ListOrganizationImpacts` call to retrieve the next page of results.

When paginating, all other parameters provided to `ListOrganizationImpacts` must match the call that provided the page token. 

  * **filter** (::String) — Optional. A filter expression that filters resources listed in the response. The expression is in the form of `field:value` for checking if a repeated field contains a value.

Example: `events:organizations%2F{organization_id}%2Flocations%2Fglobal%2ForganizationEvents%2Fevent-id`

To get your `{organization_id}`, see [Getting your organization resource ID](https://cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id).

Multiple filter queries are separated by spaces.

By default, each expression is an AND expression. However, you can include AND and OR expressions explicitly. Filter is supported for the following fields: `events`. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::OrganizationImpact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationImpact)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::ServiceHealth::V1::OrganizationImpact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-service_health-v1/latest/Google-Cloud-ServiceHealth-V1-OrganizationImpact)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/service_health/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ServiceHealth::V1::ServiceHealth::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ServiceHealth::V1::ListOrganizationImpactsRequest.new
    
    # Call the list_organization_impacts method.
    result = client.list_organization_impacts request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ServiceHealth::V1::OrganizationImpact.
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
