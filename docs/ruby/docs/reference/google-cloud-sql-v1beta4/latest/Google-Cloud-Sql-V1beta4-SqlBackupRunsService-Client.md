---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client/
title: Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client (v0.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:03.512110+00:00
---

# Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client (v0.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud SQL Admin V1BETA4 API - Class Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client (v0.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.2.0 (latest)  0.1.1 

Reference documentation and code samples for the Cloud SQL Admin V1BETA4 API class Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.

Client for the SqlBackupRunsService service.

## Inherits

  * Object 



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the SqlBackupRunsService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration "Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all SqlBackupRunsService clients
    ::Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the SqlBackupRunsService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client#Google__Cloud__Sql__V1beta4__SqlBackupRunsService__Client_configure_class_ "Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration "Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration)) 



### #delete
    
    
    def delete(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::Operation
    def delete(id: nil, instance: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Deletes the backup taken by a backup run.

**Overloads**
    
    
    def delete(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Pass arguments to `delete` via a request object, either of type [Google::Cloud::Sql::V1beta4::SqlBackupRunsDeleteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsDeleteRequest "Google::Cloud::Sql::V1beta4::SqlBackupRunsDeleteRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1beta4::SqlBackupRunsDeleteRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsDeleteRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete(id: nil, instance: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Pass arguments to `delete` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **id** (::Integer) — The ID of the backup run to delete. To find a backup run ID, use the [list](https://cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/backupRuns/list) method. 
  * **instance** (::String) — Cloud SQL instance ID. This does not include the project ID. 
  * **project** (::String) — Project ID of the project that contains the instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1beta4"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1beta4::SqlBackupRunsDeleteRequest.new
    
    # Call the delete method.
    result = client.delete request
    
    # The returned object is of type Google::Cloud::Sql::V1beta4::Operation.
    p result

### #get
    
    
    def get(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::BackupRun
    def get(id: nil, instance: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::BackupRun

Retrieves a resource containing information about a backup run.

**Overloads**
    
    
    def get(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::BackupRun

Pass arguments to `get` via a request object, either of type [Google::Cloud::Sql::V1beta4::SqlBackupRunsGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsGetRequest "Google::Cloud::Sql::V1beta4::SqlBackupRunsGetRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1beta4::SqlBackupRunsGetRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsGetRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get(id: nil, instance: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::BackupRun

Pass arguments to `get` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **id** (::Integer) — The ID of this backup run. 
  * **instance** (::String) — Cloud SQL instance ID. This does not include the project ID. 
  * **project** (::String) — Project ID of the project that contains the instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1beta4::BackupRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-BackupRun)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::BackupRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-BackupRun)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1beta4"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1beta4::SqlBackupRunsGetRequest.new
    
    # Call the get method.
    result = client.get request
    
    # The returned object is of type Google::Cloud::Sql::V1beta4::BackupRun.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new SqlBackupRunsService client object.

**Yields**

  * (config) — Configure the SqlBackupRunsService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new do |config|
      config.timeout = 10.0
    end

### #insert
    
    
    def insert(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::Operation
    def insert(instance: nil, project: nil, body: nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Creates a new backup run on demand.

**Overloads**
    
    
    def insert(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Pass arguments to `insert` via a request object, either of type [Google::Cloud::Sql::V1beta4::SqlBackupRunsInsertRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsInsertRequest "Google::Cloud::Sql::V1beta4::SqlBackupRunsInsertRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1beta4::SqlBackupRunsInsertRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsInsertRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def insert(instance: nil, project: nil, body: nil) -> ::Google::Cloud::Sql::V1beta4::Operation

Pass arguments to `insert` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance** (::String) — Cloud SQL instance ID. This does not include the project ID. 
  * **project** (::String) — Project ID of the project that contains the instance. 
  * **body** ([::Google::Cloud::Sql::V1beta4::BackupRun](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-BackupRun), ::Hash) 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-Operation)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1beta4"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1beta4::SqlBackupRunsInsertRequest.new
    
    # Call the insert method.
    result = client.insert request
    
    # The returned object is of type Google::Cloud::Sql::V1beta4::Operation.
    p result

### #list
    
    
    def list(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::BackupRunsListResponse
    def list(instance: nil, max_results: nil, page_token: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::BackupRunsListResponse

Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.

**Overloads**
    
    
    def list(request, options = nil) -> ::Google::Cloud::Sql::V1beta4::BackupRunsListResponse

Pass arguments to `list` via a request object, either of type [Google::Cloud::Sql::V1beta4::SqlBackupRunsListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsListRequest "Google::Cloud::Sql::V1beta4::SqlBackupRunsListRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Sql::V1beta4::SqlBackupRunsListRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-SqlBackupRunsListRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list(instance: nil, max_results: nil, page_token: nil, project: nil) -> ::Google::Cloud::Sql::V1beta4::BackupRunsListResponse

Pass arguments to `list` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **instance** (::String) — Cloud SQL instance ID, or "-" for all instances. This does not include the project ID. 
  * **max_results** (::Integer) — Maximum number of backup runs per response. 
  * **page_token** (::String) — A previously-returned page token representing part of the larger set of results to view. 
  * **project** (::String) — Project ID of the project that contains the instance. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::Sql::V1beta4::BackupRunsListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-BackupRunsListResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::Sql::V1beta4::BackupRunsListResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-sql-v1beta4/latest/Google-Cloud-Sql-V1beta4-BackupRunsListResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/sql/v1beta4"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Sql::V1beta4::SqlBackupRunsService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Sql::V1beta4::SqlBackupRunsListRequest.new
    
    # Call the list method.
    result = client.list request
    
    # The returned object is of type Google::Cloud::Sql::V1beta4::BackupRunsListResponse.
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
