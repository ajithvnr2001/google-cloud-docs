---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client/
title: Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlOperationsService::Client (v0.4.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:23.921836+00:00
---

# Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlOperationsService::Client (v0.4.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1 API - Class Google::Cloud::Sql::V1::SqlOperationsService::Client (v0.4.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.4.0 (latest)  0.2.0  0.1.0 

Reference documentation and code samples for the Cloud SQL Admin V1 API class Google::Cloud::Sql::V1::SqlOperationsService::Client.

Client for the SqlOperationsService service.

Service to fetch operations for database instances.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SqlOperationsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration "Google::Cloud::Sql::V1::SqlOperationsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SqlOperationsService clients
    ::Google::Cloud::Sql::V1::SqlOperationsService::Client.configure do |config|
      config.timeout = 10.0
    end

### #cancel
    
    
    def cancel(request, options = nil) -> ::Google::Protobuf::Empty
    def cancel(operation: nil, project: nil, location: nil) -> ::Google::Protobuf::Empty

Cancels an instance operation that has been performed on an instance.

**Overloads**
    
    
    def cancel(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel` via a request object, either of type [Google::Cloud::Sql::V1::SqlOperationsCancelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsCancelRequest "Google::Cloud::Sql::V1::SqlOperationsCancelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1::SqlOperationsCancelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsCancelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def cancel(operation: nil, project: nil, location: nil) -> ::Google::Protobuf::Empty

Pass arguments to `cancel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **operation** (::String) — Instance operation ID. 
  * **project** (::String) — Project ID of the project that contains the instance. 
  * **location** (::String) — Optional. Region of the Cloud SQL instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1::SqlOperationsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1::SqlOperationsCancelRequest.new
    
    # Call the cancel method.
    result = client.cancel request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SqlOperationsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client#Google__Cloud__Sql__V1__SqlOperationsService__Client_configure_class_ "Google::Cloud::Sql::V1::SqlOperationsService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration "Google::Cloud::Sql::V1::SqlOperationsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration)) 



### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Sql::V1::Operation
    def get(operation: nil, project: nil, location: nil) -> ::Google::Cloud::Sql::V1::Operation

Retrieves an instance operation that has been performed on an instance.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Sql::V1::Operation

Pass arguments to `get` via a request object, either of type [Google::Cloud::Sql::V1::SqlOperationsGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsGetRequest "Google::Cloud::Sql::V1::SqlOperationsGetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1::SqlOperationsGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsGetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get(operation: nil, project: nil, location: nil) -> ::Google::Cloud::Sql::V1::Operation

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **operation** (::String) — Required. Instance operation ID. 
  * **project** (::String) — Required. Project ID of the project that contains the instance. 
  * **location** (::String) — Optional. Region of the Cloud SQL instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-Operation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-Operation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1::SqlOperationsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1::SqlOperationsGetRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Sql::V1::Operation.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SqlOperationsService client object.

**Yields**

  * (config) — Configure the SqlOperationsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Sql::V1::SqlOperationsService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Sql::V1::SqlOperationsService::Client.new do |config|
      config.timeout = 10.0
    end

### #list
    
    
    def list(request, options = nil) -> ::Google::Cloud::Sql::V1::OperationsListResponse
    def list(instance: nil, max_results: nil, page_token: nil, project: nil, location: nil) -> ::Google::Cloud::Sql::V1::OperationsListResponse

Lists all instance operations that have been performed on the given Cloud SQL instance in the reverse chronological order of the start time.

**Overloads**
    
    
    def list(request, options = nil) -> ::Google::Cloud::Sql::V1::OperationsListResponse

Pass arguments to `list` via a request object, either of type [Google::Cloud::Sql::V1::SqlOperationsListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsListRequest "Google::Cloud::Sql::V1::SqlOperationsListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1::SqlOperationsListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-SqlOperationsListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list(instance: nil, max_results: nil, page_token: nil, project: nil, location: nil) -> ::Google::Cloud::Sql::V1::OperationsListResponse

Pass arguments to `list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance** (::String) — Cloud SQL instance ID. This does not include the project ID. 
  * **max_results** (::Integer) — Maximum number of operations per response. 
  * **page_token** (::String) — A previously-returned page token representing part of the larger set of results to view. 
  * **project** (::String) — Project ID of the project that contains the instance. 
  * **location** (::String) — Optional. Region of the Cloud SQL instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1::OperationsListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-OperationsListResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1::OperationsListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1/latest/Google-Cloud-Sql-V1-OperationsListResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1::SqlOperationsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1::SqlOperationsListRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Sql::V1::OperationsListResponse.
    p result

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
