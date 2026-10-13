---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client/
title: Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client (v1.7.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:32:07.412318+00:00
---

# Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client (v1.7.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Apigee Connect V1 API - Class Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client (v1.7.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.2 (latest)  1.7.1  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.4 

Reference documentation and code samples for the Apigee Connect V1 API class Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.

REST client for the ConnectionService service.

Service Interface for the Apigee Connect connection management APIs.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::ApigeeConnect::V1::ConnectionService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the ConnectionService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration "Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all ConnectionService clients
    ::Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the ConnectionService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client#Google__Cloud__ApigeeConnect__V1__ConnectionService__Rest__Client_configure_class_ "Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration "Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration)) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new ConnectionService REST client object.

**Yields**

  * (config) — Configure the ConnectionService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ConnectionService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_connections
    
    
    def list_connections(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApigeeConnect::V1::Connection>
    def list_connections(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApigeeConnect::V1::Connection>

Lists connections that are currently active for the given Apigee Connect endpoint.

**Overloads**
    
    
    def list_connections(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApigeeConnect::V1::Connection>

Pass arguments to `list_connections` via a request object, either of type [ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ListConnectionsRequest "Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-ListConnectionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_connections(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::ApigeeConnect::V1::Connection>

Pass arguments to `list_connections` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Parent name of the form: `projects/{project_number or project_id}/endpoints/{endpoint}`. 
  * **page_size** (::Integer) — The maximum number of connections to return. The service may return fewer than this value. If unspecified, at most 100 connections will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListConnections` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListConnections` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApigeeConnect::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Connection)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::ApigeeConnect::V1::Connection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-apigee_connect-v1/latest/Google-Cloud-ApigeeConnect-V1-Connection)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/apigee_connect/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::ApigeeConnect::V1::ConnectionService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::ApigeeConnect::V1::ListConnectionsRequest.new
    
    # Call the list_connections method.
    result = client.list_connections request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::ApigeeConnect::V1::Connection.
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



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
