---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client/
title: BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client (v0.23.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:28:06.848480+00:00
---

# BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client (v0.23.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  BigQuery Migration V2 API - Class Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client (v0.23.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.23.0 (latest)  0.22.1  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the BigQuery Migration V2 API class Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.

REST client for the MigrationService service.

Service to handle EDW migrations.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::Bigquery::Migration::V2::MigrationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the MigrationService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration "Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all MigrationService clients
    ::Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the MigrationService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client#Google__Cloud__Bigquery__Migration__V2__MigrationService__Rest__Client_configure_class_ "Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration "Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration)) 



### #create_migration_workflow
    
    
    def create_migration_workflow(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow
    def create_migration_workflow(parent: nil, migration_workflow: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Creates a migration workflow.

**Overloads**
    
    
    def create_migration_workflow(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Pass arguments to `create_migration_workflow` via a request object, either of type [CreateMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-CreateMigrationWorkflowRequest "Google::Cloud::Bigquery::Migration::V2::CreateMigrationWorkflowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::CreateMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-CreateMigrationWorkflowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_migration_workflow(parent: nil, migration_workflow: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Pass arguments to `create_migration_workflow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the project to which this migration workflow belongs. Example: `projects/foo/locations/bar`
  * **migration_workflow** ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow), ::Hash) — Required. The migration workflow to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::CreateMigrationWorkflowRequest.new
    
    # Call the create_migration_workflow method.
    result = client.create_migration_workflow request
    
    # The returned object is of type Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow.
    p result

### #delete_migration_workflow
    
    
    def delete_migration_workflow(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_migration_workflow(name: nil) -> ::Google::Protobuf::Empty

Deletes a migration workflow by name.

**Overloads**
    
    
    def delete_migration_workflow(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_migration_workflow` via a request object, either of type [DeleteMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-DeleteMigrationWorkflowRequest "Google::Cloud::Bigquery::Migration::V2::DeleteMigrationWorkflowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::DeleteMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-DeleteMigrationWorkflowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_migration_workflow(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_migration_workflow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The unique identifier for the migration workflow. Example: `projects/123/locations/us/workflows/1234`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::DeleteMigrationWorkflowRequest.new
    
    # Call the delete_migration_workflow method.
    result = client.delete_migration_workflow request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_migration_subtask
    
    
    def get_migration_subtask(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask
    def get_migration_subtask(name: nil, read_mask: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask

Gets a previously created migration subtask.

**Overloads**
    
    
    def get_migration_subtask(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask

Pass arguments to `get_migration_subtask` via a request object, either of type [GetMigrationSubtaskRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GetMigrationSubtaskRequest "Google::Cloud::Bigquery::Migration::V2::GetMigrationSubtaskRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::GetMigrationSubtaskRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GetMigrationSubtaskRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_migration_subtask(name: nil, read_mask: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask

Pass arguments to `get_migration_subtask` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The unique identifier for the migration subtask. Example: `projects/123/locations/us/workflows/1234/subtasks/543`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The list of fields to be retrieved. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::GetMigrationSubtaskRequest.new
    
    # Call the get_migration_subtask method.
    result = client.get_migration_subtask request
    
    # The returned object is of type Google::Cloud::Bigquery::Migration::V2::MigrationSubtask.
    p result

### #get_migration_workflow
    
    
    def get_migration_workflow(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow
    def get_migration_workflow(name: nil, read_mask: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Gets a previously created migration workflow.

**Overloads**
    
    
    def get_migration_workflow(request, options = nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Pass arguments to `get_migration_workflow` via a request object, either of type [GetMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GetMigrationWorkflowRequest "Google::Cloud::Bigquery::Migration::V2::GetMigrationWorkflowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::GetMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-GetMigrationWorkflowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_migration_workflow(name: nil, read_mask: nil) -> ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow

Pass arguments to `get_migration_workflow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The unique identifier for the migration workflow. Example: `projects/123/locations/us/workflows/1234`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be retrieved. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::GetMigrationWorkflowRequest.new
    
    # Call the get_migration_workflow method.
    result = client.get_migration_workflow request
    
    # The returned object is of type Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new MigrationService REST client object.

**Yields**

  * (config) — Configure the MigrationService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationService-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_migration_subtasks
    
    
    def list_migration_subtasks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask>
    def list_migration_subtasks(parent: nil, read_mask: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask>

Lists previously created migration subtasks.

**Overloads**
    
    
    def list_migration_subtasks(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask>

Pass arguments to `list_migration_subtasks` via a request object, either of type [ListMigrationSubtasksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationSubtasksRequest "Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationSubtasksRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_migration_subtasks(parent: nil, read_mask: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask>

Pass arguments to `list_migration_subtasks` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The migration task of the subtasks to list. Example: `projects/123/locations/us/workflows/1234`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. The list of fields to be retrieved. 
  * **page_size** (::Integer) — Optional. The maximum number of migration tasks to return. The service may return fewer than this number. 
  * **page_token** (::String) — Optional. A page token, received from previous `ListMigrationSubtasks` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListMigrationSubtasks` must match the call that provided the page token. 

  * **filter** (::String) — Optional. The filter to apply. This can be used to get the subtasks of a specific tasks in a workflow, e.g. `migration_task = "ab012"` where `"ab012"` is the task ID (not the name in the named map). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationSubtask)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::ListMigrationSubtasksRequest.new
    
    # Call the list_migration_subtasks method.
    result = client.list_migration_subtasks request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Migration::V2::MigrationSubtask.
      p item
    end

### #list_migration_workflows
    
    
    def list_migration_workflows(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow>
    def list_migration_workflows(parent: nil, read_mask: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow>

Lists previously created migration workflow.

**Overloads**
    
    
    def list_migration_workflows(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow>

Pass arguments to `list_migration_workflows` via a request object, either of type [ListMigrationWorkflowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationWorkflowsRequest "Google::Cloud::Bigquery::Migration::V2::ListMigrationWorkflowsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::ListMigrationWorkflowsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-ListMigrationWorkflowsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_migration_workflows(parent: nil, read_mask: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow>

Pass arguments to `list_migration_workflows` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location of the migration workflows to list. Example: `projects/123/locations/us`
  * **read_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-FieldMask), ::Hash) — The list of fields to be retrieved. 
  * **page_size** (::Integer) — The maximum number of migration workflows to return. The service may return fewer than this number. 
  * **page_token** (::String) — A page token, received from previous `ListMigrationWorkflows` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListMigrationWorkflows` must match the call that provided the page token. 




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-MigrationWorkflow)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::ListMigrationWorkflowsRequest.new
    
    # Call the list_migration_workflows method.
    result = client.list_migration_workflows request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Bigquery::Migration::V2::MigrationWorkflow.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #start_migration_workflow
    
    
    def start_migration_workflow(request, options = nil) -> ::Google::Protobuf::Empty
    def start_migration_workflow(name: nil) -> ::Google::Protobuf::Empty

Starts a previously created migration workflow. I.e., the state transitions from DRAFT to RUNNING. This is a no-op if the state is already RUNNING. An error will be signaled if the state is anything other than DRAFT or RUNNING.

**Overloads**
    
    
    def start_migration_workflow(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `start_migration_workflow` via a request object, either of type [StartMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-StartMigrationWorkflowRequest "Google::Cloud::Bigquery::Migration::V2::StartMigrationWorkflowRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Bigquery::Migration::V2::StartMigrationWorkflowRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Cloud-Bigquery-Migration-V2-StartMigrationWorkflowRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def start_migration_workflow(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `start_migration_workflow` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The unique identifier for the migration workflow. Example: `projects/123/locations/us/workflows/1234`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-bigquery-migration-v2/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/bigquery/migration/v2"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Bigquery::Migration::V2::MigrationService::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Bigquery::Migration::V2::StartMigrationWorkflowRequest.new
    
    # Call the start_migration_workflow method.
    result = client.start_migration_workflow request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
