---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client/
title: Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:35:24.650885+00:00
---

# Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Database Migration Service V1 API - Class Google::Cloud::CloudDMS::V1::DataMigrationService::Client (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.1  1.2.2  1.1.0  1.0.1  0.8.0  0.7.2  0.6.0  0.5.0  0.4.0  0.3.0  0.2.0  0.1.5 

Reference documentation and code samples for the Cloud Database Migration Service V1 API class Google::Cloud::CloudDMS::V1::DataMigrationService::Client.

Client for the DataMigrationService service.

Database Migration service

## Inherits

  * Object 



## Includes

  * [Google::Cloud::CloudDMS::V1::DataMigrationService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DataMigrationService Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration "Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DataMigrationService clients
    ::Google::Cloud::CloudDMS::V1::DataMigrationService::Client.configure do |config|
      config.timeout = 10.0
    end

### #apply_conversion_workspace
    
    
    def apply_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def apply_conversion_workspace(name: nil, filter: nil, dry_run: nil, auto_commit: nil, connection_profile: nil) -> ::Gapic::Operation

Applies draft tree onto a specific destination database.

**Overloads**
    
    
    def apply_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `apply_conversion_workspace` via a request object, either of type [ApplyConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ApplyConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::ApplyConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ApplyConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ApplyConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def apply_conversion_workspace(name: nil, filter: nil, dry_run: nil, auto_commit: nil, connection_profile: nil) -> ::Gapic::Operation

Pass arguments to `apply_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the conversion workspace resource for which to apply the draft tree. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **filter** (::String) — Filter which entities to apply. Leaving this field empty will apply all of the entities. Supports Google AIP 160 based filtering. 
  * **dry_run** (::Boolean) — Optional. Only validates the apply process, but doesn't change the destination database. Only works for PostgreSQL destination connection profile. 
  * **auto_commit** (::Boolean) — Optional. Specifies whether the conversion workspace is to be committed automatically after the apply. 
  * **connection_profile** (::String) — Optional. Fully qualified (Uri) name of the destination connection profile. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ApplyConversionWorkspaceRequest.new
    
    # Call the apply_conversion_workspace method.
    result = client.apply_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #commit_conversion_workspace
    
    
    def commit_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def commit_conversion_workspace(name: nil, commit_name: nil) -> ::Gapic::Operation

Marks all the data in the conversion workspace as committed.

**Overloads**
    
    
    def commit_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `commit_conversion_workspace` via a request object, either of type [CommitConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CommitConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::CommitConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CommitConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CommitConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def commit_conversion_workspace(name: nil, commit_name: nil) -> ::Gapic::Operation

Pass arguments to `commit_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the conversion workspace resource to commit. 
  * **commit_name** (::String) — Optional. Optional name of the commit. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CommitConversionWorkspaceRequest.new
    
    # Call the commit_conversion_workspace method.
    result = client.commit_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DataMigrationService Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client#Google__Cloud__CloudDMS__V1__DataMigrationService__Client_configure_class_ "Google::Cloud::CloudDMS::V1::DataMigrationService::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration "Google::Cloud::CloudDMS::V1::DataMigrationService::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration)) 



### #convert_conversion_workspace
    
    
    def convert_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def convert_conversion_workspace(name: nil, auto_commit: nil, filter: nil, convert_full_path: nil) -> ::Gapic::Operation

Creates a draft tree schema for the destination database.

**Overloads**
    
    
    def convert_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `convert_conversion_workspace` via a request object, either of type [ConvertConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConvertConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::ConvertConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ConvertConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConvertConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def convert_conversion_workspace(name: nil, auto_commit: nil, filter: nil, convert_full_path: nil) -> ::Gapic::Operation

Pass arguments to `convert_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the conversion workspace resource to convert in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **auto_commit** (::Boolean) — Optional. Specifies whether the conversion workspace is to be committed automatically after the conversion. 
  * **filter** (::String) — Optional. Filter the entities to convert. Leaving this field empty will convert all of the entities. Supports Google AIP-160 style filtering. 
  * **convert_full_path** (::Boolean) — Optional. Automatically convert the full entity path for each entity specified by the filter. For example, if the filter specifies a table, that table schema (and database if there is one) will also be converted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ConvertConversionWorkspaceRequest.new
    
    # Call the convert_conversion_workspace method.
    result = client.convert_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_connection_profile
    
    
    def create_connection_profile(request, options = nil) -> ::Gapic::Operation
    def create_connection_profile(parent: nil, connection_profile_id: nil, connection_profile: nil, request_id: nil, validate_only: nil, skip_validation: nil) -> ::Gapic::Operation

Creates a new connection profile in a given project and location.

**Overloads**
    
    
    def create_connection_profile(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_connection_profile` via a request object, either of type [CreateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConnectionProfileRequest "Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConnectionProfileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_connection_profile(parent: nil, connection_profile_id: nil, connection_profile: nil, request_id: nil, validate_only: nil, skip_validation: nil) -> ::Gapic::Operation

Pass arguments to `create_connection_profile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of connection profiles. 
  * **connection_profile_id** (::String) — Required. The connection profile identifier. 
  * **connection_profile** ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile), ::Hash) — Required. The create request body including the connection profile data 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **validate_only** (::Boolean) — Optional. Only validate the connection profile, but don't create any resources. The default is false. Only supported for Oracle connection profiles. 
  * **skip_validation** (::Boolean) — Optional. Create the connection profile without validating it. The default is false. Only supported for Oracle connection profiles. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CreateConnectionProfileRequest.new
    
    # Call the create_connection_profile method.
    result = client.create_connection_profile request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_conversion_workspace
    
    
    def create_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def create_conversion_workspace(parent: nil, conversion_workspace_id: nil, conversion_workspace: nil, request_id: nil) -> ::Gapic::Operation

Creates a new conversion workspace in a given project and location.

**Overloads**
    
    
    def create_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_conversion_workspace` via a request object, either of type [CreateConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::CreateConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CreateConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_conversion_workspace(parent: nil, conversion_workspace_id: nil, conversion_workspace: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of conversion workspaces. 
  * **conversion_workspace_id** (::String) — Required. The ID of the conversion workspace to create. 
  * **conversion_workspace** ([::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace), ::Hash) — Required. Represents a conversion workspace object. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CreateConversionWorkspaceRequest.new
    
    # Call the create_conversion_workspace method.
    result = client.create_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_mapping_rule
    
    
    def create_mapping_rule(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule
    def create_mapping_rule(parent: nil, mapping_rule_id: nil, mapping_rule: nil, request_id: nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Creates a new mapping rule for a given conversion workspace.

**Overloads**
    
    
    def create_mapping_rule(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Pass arguments to `create_mapping_rule` via a request object, either of type [CreateMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMappingRuleRequest "Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMappingRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_mapping_rule(parent: nil, mapping_rule_id: nil, mapping_rule: nil, request_id: nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Pass arguments to `create_mapping_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of mapping rules. 
  * **mapping_rule_id** (::String) — Required. The ID of the rule to create. 
  * **mapping_rule** ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule), ::Hash) — Required. Represents a [mapping rule](https://cloud.google.com/database-migration/reference/rest/v1/projects.locations.mappingRules) object. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CreateMappingRuleRequest.new
    
    # Call the create_mapping_rule method.
    result = client.create_mapping_rule request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::MappingRule.
    p result

### #create_migration_job
    
    
    def create_migration_job(request, options = nil) -> ::Gapic::Operation
    def create_migration_job(parent: nil, migration_job_id: nil, migration_job: nil, request_id: nil) -> ::Gapic::Operation

Creates a new migration job in a given project and location.

**Overloads**
    
    
    def create_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_migration_job` via a request object, either of type [CreateMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMigrationJobRequest "Google::Cloud::CloudDMS::V1::CreateMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CreateMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreateMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_migration_job(parent: nil, migration_job_id: nil, migration_job: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of migration jobs. 
  * **migration_job_id** (::String) — Required. The ID of the instance to create. 
  * **migration_job** ([::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob), ::Hash) — Required. Represents a [migration job](https://cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs) object. 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CreateMigrationJobRequest.new
    
    # Call the create_migration_job method.
    result = client.create_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_private_connection
    
    
    def create_private_connection(request, options = nil) -> ::Gapic::Operation
    def create_private_connection(parent: nil, private_connection_id: nil, private_connection: nil, request_id: nil, skip_validation: nil) -> ::Gapic::Operation

Creates a new private connection in a given project and location.

**Overloads**
    
    
    def create_private_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_private_connection` via a request object, either of type [CreatePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreatePrivateConnectionRequest "Google::Cloud::CloudDMS::V1::CreatePrivateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::CreatePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-CreatePrivateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def create_private_connection(parent: nil, private_connection_id: nil, private_connection: nil, request_id: nil, skip_validation: nil) -> ::Gapic::Operation

Pass arguments to `create_private_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent that owns the collection of PrivateConnections. 
  * **private_connection_id** (::String) — Required. The private connection identifier. 
  * **private_connection** ([::Google::Cloud::CloudDMS::V1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PrivateConnection), ::Hash) — Required. The private connection resource to create. 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **skip_validation** (::Boolean) — Optional. If set to true, will skip validations. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::CreatePrivateConnectionRequest.new
    
    # Call the create_private_connection method.
    result = client.create_private_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_connection_profile
    
    
    def delete_connection_profile(request, options = nil) -> ::Gapic::Operation
    def delete_connection_profile(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Deletes a single Database Migration Service connection profile. A connection profile can only be deleted if it is not in use by any active migration jobs.

**Overloads**
    
    
    def delete_connection_profile(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_connection_profile` via a request object, either of type [Google::Cloud::CloudDMS::V1::DeleteConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteConnectionProfileRequest "Google::Cloud::CloudDMS::V1::DeleteConnectionProfileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DeleteConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteConnectionProfileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_connection_profile(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_connection_profile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the connection profile resource to delete. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **force** (::Boolean) — In case of force delete, the CloudSQL replica database is also deleted (only for CloudSQL connection profile). 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DeleteConnectionProfileRequest.new
    
    # Call the delete_connection_profile method.
    result = client.delete_connection_profile request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_conversion_workspace
    
    
    def delete_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def delete_conversion_workspace(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Deletes a single conversion workspace.

**Overloads**
    
    
    def delete_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_conversion_workspace` via a request object, either of type [Google::Cloud::CloudDMS::V1::DeleteConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::DeleteConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DeleteConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_conversion_workspace(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the conversion workspace resource to delete. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **force** (::Boolean) — Force delete the conversion workspace, even if there's a running migration that is using the workspace. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DeleteConversionWorkspaceRequest.new
    
    # Call the delete_conversion_workspace method.
    result = client.delete_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_mapping_rule
    
    
    def delete_mapping_rule(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_mapping_rule(name: nil, request_id: nil) -> ::Google::Protobuf::Empty

Deletes a single mapping rule.

**Overloads**
    
    
    def delete_mapping_rule(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_mapping_rule` via a request object, either of type [Google::Cloud::CloudDMS::V1::DeleteMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteMappingRuleRequest "Google::Cloud::CloudDMS::V1::DeleteMappingRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DeleteMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteMappingRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_mapping_rule(name: nil, request_id: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_mapping_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the mapping rule resource to delete. 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DeleteMappingRuleRequest.new
    
    # Call the delete_mapping_rule method.
    result = client.delete_mapping_rule request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_migration_job
    
    
    def delete_migration_job(request, options = nil) -> ::Gapic::Operation
    def delete_migration_job(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Deletes a single migration job.

**Overloads**
    
    
    def delete_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_migration_job` via a request object, either of type [Google::Cloud::CloudDMS::V1::DeleteMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteMigrationJobRequest "Google::Cloud::CloudDMS::V1::DeleteMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DeleteMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeleteMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_migration_job(name: nil, request_id: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the migration job resource to delete. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **force** (::Boolean) — The destination CloudSQL connection profile is always deleted with the migration job. In case of force delete, the destination CloudSQL replica database is also deleted. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DeleteMigrationJobRequest.new
    
    # Call the delete_migration_job method.
    result = client.delete_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_private_connection
    
    
    def delete_private_connection(request, options = nil) -> ::Gapic::Operation
    def delete_private_connection(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single Database Migration Service private connection.

**Overloads**
    
    
    def delete_private_connection(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_private_connection` via a request object, either of type [Google::Cloud::CloudDMS::V1::DeletePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeletePrivateConnectionRequest "Google::Cloud::CloudDMS::V1::DeletePrivateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DeletePrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DeletePrivateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def delete_private_connection(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_private_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The name of the private connection to delete. 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DeletePrivateConnectionRequest.new
    
    # Call the delete_private_connection method.
    result = client.delete_private_connection request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #describe_conversion_workspace_revisions
    
    
    def describe_conversion_workspace_revisions(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse
    def describe_conversion_workspace_revisions(conversion_workspace: nil, commit_id: nil) -> ::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse

Retrieves a list of committed revisions of a specific conversion workspace.

**Overloads**
    
    
    def describe_conversion_workspace_revisions(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse

Pass arguments to `describe_conversion_workspace_revisions` via a request object, either of type [Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeConversionWorkspaceRevisionsRequest "Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeConversionWorkspaceRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def describe_conversion_workspace_revisions(conversion_workspace: nil, commit_id: nil) -> ::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse

Pass arguments to `describe_conversion_workspace_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **conversion_workspace** (::String) — Required. Name of the conversion workspace resource whose revisions are listed. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **commit_id** (::String) — Optional. Optional filter to request a specific commit ID. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeConversionWorkspaceRevisionsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeConversionWorkspaceRevisionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsRequest.new
    
    # Call the describe_conversion_workspace_revisions method.
    result = client.describe_conversion_workspace_revisions request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::DescribeConversionWorkspaceRevisionsResponse.
    p result

### #describe_database_entities
    
    
    def describe_database_entities(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::DatabaseEntity>
    def describe_database_entities(conversion_workspace: nil, page_size: nil, page_token: nil, tree: nil, uncommitted: nil, commit_id: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::DatabaseEntity>

Describes the database entities tree for a specific conversion workspace and a specific tree type.

Database entities are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are simple data objects describing the structure of the client database.

**Overloads**
    
    
    def describe_database_entities(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::DatabaseEntity>

Pass arguments to `describe_database_entities` via a request object, either of type [Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest "Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def describe_database_entities(conversion_workspace: nil, page_size: nil, page_token: nil, tree: nil, uncommitted: nil, commit_id: nil, filter: nil, view: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::DatabaseEntity>

Pass arguments to `describe_database_entities` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **conversion_workspace** (::String) — Required. Name of the conversion workspace resource whose database entities are described. Must be in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **page_size** (::Integer) — Optional. The maximum number of entities to return. The service may return fewer entities than the value specifies. 
  * **page_token** (::String) — Optional. The nextPageToken value received in the previous call to conversionWorkspace.describeDatabaseEntities, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspace.describeDatabaseEntities must match the call that provided the page token. 
  * **tree** ([::Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest::DBTreeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DescribeDatabaseEntitiesRequest-DBTreeType)) — Required. The tree to fetch. 
  * **uncommitted** (::Boolean) — Optional. Whether to retrieve the latest committed version of the entities or the latest version. This field is ignored if a specific commit_id is specified. 
  * **commit_id** (::String) — Optional. Request a specific commit ID. If not specified, the entities from the latest commit are returned. 
  * **filter** (::String) — Optional. Filter the returned entities based on AIP-160 standard. 
  * **view** ([::Google::Cloud::CloudDMS::V1::DatabaseEntityView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntityView)) — Optional. Results view based on AIP-157 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::DatabaseEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::DatabaseEntity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DatabaseEntity)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::DescribeDatabaseEntitiesRequest.new
    
    # Call the describe_database_entities method.
    result = client.describe_database_entities request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::DatabaseEntity.
      p item
    end

### #fetch_static_ips
    
    
    def fetch_static_ips(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse
    def fetch_static_ips(name: nil, page_size: nil, page_token: nil) -> ::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse

Fetches a set of static IP addresses that need to be allowlisted by the customer when using the static-IP connectivity method.

**Overloads**
    
    
    def fetch_static_ips(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse

Pass arguments to `fetch_static_ips` via a request object, either of type [FetchStaticIpsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FetchStaticIpsRequest "Google::Cloud::CloudDMS::V1::FetchStaticIpsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::FetchStaticIpsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FetchStaticIpsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def fetch_static_ips(name: nil, page_size: nil, page_token: nil) -> ::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse

Pass arguments to `fetch_static_ips` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name for the location for which static IPs should be returned. Must be in the format `projects/*/locations/*`. 
  * **page_size** (::Integer) — Maximum number of IPs to return. 
  * **page_token** (::String) — A page token, received from a previous `FetchStaticIps` call. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FetchStaticIpsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-FetchStaticIpsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::FetchStaticIpsRequest.new
    
    # Call the fetch_static_ips method.
    result = client.fetch_static_ips request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::FetchStaticIpsResponse.
    p result

### #generate_ssh_script
    
    
    def generate_ssh_script(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::SshScript
    def generate_ssh_script(migration_job: nil, vm: nil, vm_creation_config: nil, vm_selection_config: nil, vm_port: nil) -> ::Google::Cloud::CloudDMS::V1::SshScript

Generate a SSH configuration script to configure the reverse SSH connectivity.

**Overloads**
    
    
    def generate_ssh_script(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::SshScript

Pass arguments to `generate_ssh_script` via a request object, either of type [GenerateSshScriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateSshScriptRequest "Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateSshScriptRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def generate_ssh_script(migration_job: nil, vm: nil, vm_creation_config: nil, vm_selection_config: nil, vm_port: nil) -> ::Google::Cloud::CloudDMS::V1::SshScript

Pass arguments to `generate_ssh_script` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **migration_job** (::String) — Name of the migration job resource to generate the SSH script. 
  * **vm** (::String) — Required. Bastion VM Instance name to use or to create. 
  * **vm_creation_config** ([::Google::Cloud::CloudDMS::V1::VmCreationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmCreationConfig), ::Hash) — The VM creation configuration

Note: The following parameters are mutually exclusive: `vm_creation_config`, `vm_selection_config`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **vm_selection_config** ([::Google::Cloud::CloudDMS::V1::VmSelectionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VmSelectionConfig), ::Hash) — The VM selection configuration

Note: The following parameters are mutually exclusive: `vm_selection_config`, `vm_creation_config`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **vm_port** (::Integer) — The port that will be open on the bastion host. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::SshScript](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SshScript)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SshScript](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SshScript)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GenerateSshScriptRequest.new
    
    # Call the generate_ssh_script method.
    result = client.generate_ssh_script request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::SshScript.
    p result

### #generate_tcp_proxy_script
    
    
    def generate_tcp_proxy_script(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::TcpProxyScript
    def generate_tcp_proxy_script(migration_job: nil, vm_name: nil, vm_machine_type: nil, vm_zone: nil, vm_subnet: nil) -> ::Google::Cloud::CloudDMS::V1::TcpProxyScript

Generate a TCP Proxy configuration script to configure a cloud-hosted VM running a TCP Proxy.

**Overloads**
    
    
    def generate_tcp_proxy_script(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::TcpProxyScript

Pass arguments to `generate_tcp_proxy_script` via a request object, either of type [GenerateTcpProxyScriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateTcpProxyScriptRequest "Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GenerateTcpProxyScriptRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def generate_tcp_proxy_script(migration_job: nil, vm_name: nil, vm_machine_type: nil, vm_zone: nil, vm_subnet: nil) -> ::Google::Cloud::CloudDMS::V1::TcpProxyScript

Pass arguments to `generate_tcp_proxy_script` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **migration_job** (::String) — Name of the migration job resource to generate the TCP Proxy script. 
  * **vm_name** (::String) — Required. The name of the Compute instance that will host the proxy. 
  * **vm_machine_type** (::String) — Required. The type of the Compute instance that will host the proxy. 
  * **vm_zone** (::String) — Optional. The Google Cloud Platform zone to create the VM in. The fully qualified name of the zone must be specified, including the region name, for example "us-central1-b". If not specified, uses the "-b" zone of the destination Connection Profile's region. 
  * **vm_subnet** (::String) — Required. The name of the subnet the Compute instance will use for private connectivity. Must be supplied in the form of projects/{project}/regions/{region}/subnetworks/{subnetwork}. Note: the region for the subnet must match the Compute instance region. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::TcpProxyScript](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-TcpProxyScript)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::TcpProxyScript](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-TcpProxyScript)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GenerateTcpProxyScriptRequest.new
    
    # Call the generate_tcp_proxy_script method.
    result = client.generate_tcp_proxy_script request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::TcpProxyScript.
    p result

### #get_connection_profile
    
    
    def get_connection_profile(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile
    def get_connection_profile(name: nil) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile

Gets details of a single connection profile.

**Overloads**
    
    
    def get_connection_profile(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile

Pass arguments to `get_connection_profile` via a request object, either of type [GetConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetConnectionProfileRequest "Google::Cloud::CloudDMS::V1::GetConnectionProfileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GetConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetConnectionProfileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_connection_profile(name: nil) -> ::Google::Cloud::CloudDMS::V1::ConnectionProfile

Pass arguments to `get_connection_profile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the connection profile resource to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GetConnectionProfileRequest.new
    
    # Call the get_connection_profile method.
    result = client.get_connection_profile request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::ConnectionProfile.
    p result

### #get_conversion_workspace
    
    
    def get_conversion_workspace(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::ConversionWorkspace
    def get_conversion_workspace(name: nil) -> ::Google::Cloud::CloudDMS::V1::ConversionWorkspace

Gets details of a single conversion workspace.

**Overloads**
    
    
    def get_conversion_workspace(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::ConversionWorkspace

Pass arguments to `get_conversion_workspace` via a request object, either of type [GetConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::GetConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GetConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_conversion_workspace(name: nil) -> ::Google::Cloud::CloudDMS::V1::ConversionWorkspace

Pass arguments to `get_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the conversion workspace resource to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GetConversionWorkspaceRequest.new
    
    # Call the get_conversion_workspace method.
    result = client.get_conversion_workspace request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::ConversionWorkspace.
    p result

### #get_mapping_rule
    
    
    def get_mapping_rule(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule
    def get_mapping_rule(name: nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Gets the details of a mapping rule.

**Overloads**
    
    
    def get_mapping_rule(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Pass arguments to `get_mapping_rule` via a request object, either of type [GetMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetMappingRuleRequest "Google::Cloud::CloudDMS::V1::GetMappingRuleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GetMappingRuleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetMappingRuleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_mapping_rule(name: nil) -> ::Google::Cloud::CloudDMS::V1::MappingRule

Pass arguments to `get_mapping_rule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the mapping rule resource to get. Example: conversionWorkspaces/123/mappingRules/rule123

In order to retrieve a previous revision of the mapping rule, also provide the revision ID. Example: conversionWorkspace/123/mappingRules/rule123@c7cfa2a8c7cfa2a8c7cfa2a8c7cfa2a8 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GetMappingRuleRequest.new
    
    # Call the get_mapping_rule method.
    result = client.get_mapping_rule request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::MappingRule.
    p result

### #get_migration_job
    
    
    def get_migration_job(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MigrationJob
    def get_migration_job(name: nil) -> ::Google::Cloud::CloudDMS::V1::MigrationJob

Gets details of a single migration job.

**Overloads**
    
    
    def get_migration_job(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::MigrationJob

Pass arguments to `get_migration_job` via a request object, either of type [GetMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetMigrationJobRequest "Google::Cloud::CloudDMS::V1::GetMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GetMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_migration_job(name: nil) -> ::Google::Cloud::CloudDMS::V1::MigrationJob

Pass arguments to `get_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the migration job resource to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GetMigrationJobRequest.new
    
    # Call the get_migration_job method.
    result = client.get_migration_job request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::MigrationJob.
    p result

### #get_private_connection
    
    
    def get_private_connection(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::PrivateConnection
    def get_private_connection(name: nil) -> ::Google::Cloud::CloudDMS::V1::PrivateConnection

Gets details of a single private connection.

**Overloads**
    
    
    def get_private_connection(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::PrivateConnection

Pass arguments to `get_private_connection` via a request object, either of type [GetPrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetPrivateConnectionRequest "Google::Cloud::CloudDMS::V1::GetPrivateConnectionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::GetPrivateConnectionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-GetPrivateConnectionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def get_private_connection(name: nil) -> ::Google::Cloud::CloudDMS::V1::PrivateConnection

Pass arguments to `get_private_connection` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the private connection to get. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PrivateConnection)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PrivateConnection)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::GetPrivateConnectionRequest.new
    
    # Call the get_private_connection method.
    result = client.get_private_connection request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::PrivateConnection.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Client) 



### #import_mapping_rules
    
    
    def import_mapping_rules(request, options = nil) -> ::Gapic::Operation
    def import_mapping_rules(parent: nil, rules_format: nil, rules_files: nil, auto_commit: nil) -> ::Gapic::Operation

Imports the mapping rules for a given conversion workspace. Supports various formats of external rules files.

**Overloads**
    
    
    def import_mapping_rules(request, options = nil) -> ::Gapic::Operation

Pass arguments to `import_mapping_rules` via a request object, either of type [ImportMappingRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ImportMappingRulesRequest "Google::Cloud::CloudDMS::V1::ImportMappingRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ImportMappingRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ImportMappingRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def import_mapping_rules(parent: nil, rules_format: nil, rules_files: nil, auto_commit: nil) -> ::Gapic::Operation

Pass arguments to `import_mapping_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Name of the conversion workspace resource to import the rules to in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **rules_format** ([::Google::Cloud::CloudDMS::V1::ImportRulesFileFormat](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ImportRulesFileFormat)) — Required. The format of the rules content file. 
  * **rules_files** (::Array<[::Google::Cloud::CloudDMS::V1::ImportMappingRulesRequest::RulesFile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ImportMappingRulesRequest-RulesFile), ::Hash>) — Required. One or more rules files. 
  * **auto_commit** (::Boolean) — Required. Should the conversion workspace be committed automatically after the import operation. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ImportMappingRulesRequest.new
    
    # Call the import_mapping_rules method.
    result = client.import_mapping_rules request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DataMigrationService client object.

**Yields**

  * (config) — Configure the DataMigrationService client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new do |config|
      config.timeout = 10.0
    end

### #list_connection_profiles
    
    
    def list_connection_profiles(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConnectionProfile>
    def list_connection_profiles(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConnectionProfile>

Retrieves a list of all connection profiles in a given project and location.

**Overloads**
    
    
    def list_connection_profiles(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConnectionProfile>

Pass arguments to `list_connection_profiles` via a request object, either of type [ListConnectionProfilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListConnectionProfilesRequest "Google::Cloud::CloudDMS::V1::ListConnectionProfilesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ListConnectionProfilesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListConnectionProfilesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_connection_profiles(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConnectionProfile>

Pass arguments to `list_connection_profiles` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of connection profiles. 
  * **page_size** (::Integer) — The maximum number of connection profiles to return. The service may return fewer than this value. If unspecified, at most 50 connection profiles will be returned. The maximum value is 1000; values above 1000 are coerced to 1000. 
  * **page_token** (::String) — A page token, received from a previous `ListConnectionProfiles` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListConnectionProfiles` must match the call that provided the page token. 

  * **filter** (::String) — A filter expression that filters connection profiles listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be either =, !=, >, or <. For example, list connection profiles created this year by specifying **createTime %gt; 2020-01-01T00:00:00.000000000Z**. You can also filter nested fields. For example, you could specify **mySql.username = %lt;my_username%gt;** to list all connection profiles configured to connect with a specific username. 
  * **order_by** (::String) — A comma-separated list of fields to order results according to. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ListConnectionProfilesRequest.new
    
    # Call the list_connection_profiles method.
    result = client.list_connection_profiles request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::ConnectionProfile.
      p item
    end

### #list_conversion_workspaces
    
    
    def list_conversion_workspaces(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConversionWorkspace>
    def list_conversion_workspaces(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConversionWorkspace>

Lists conversion workspaces in a given project and location.

**Overloads**
    
    
    def list_conversion_workspaces(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConversionWorkspace>

Pass arguments to `list_conversion_workspaces` via a request object, either of type [ListConversionWorkspacesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListConversionWorkspacesRequest "Google::Cloud::CloudDMS::V1::ListConversionWorkspacesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ListConversionWorkspacesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListConversionWorkspacesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_conversion_workspaces(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::ConversionWorkspace>

Pass arguments to `list_conversion_workspaces` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of conversion workspaces. 
  * **page_size** (::Integer) — The maximum number of conversion workspaces to return. The service may return fewer than this value. If unspecified, at most 50 sets are returned. 
  * **page_token** (::String) — The nextPageToken value received in the previous call to conversionWorkspaces.list, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to conversionWorkspaces.list must match the call that provided the page token. 
  * **filter** (::String) — A filter expression that filters conversion workspaces listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be either =, !=, >, or <. For example, list conversion workspaces created this year by specifying **createTime %gt; 2020-01-01T00:00:00.000000000Z.** You can also filter nested fields. For example, you could specify **source.version = "12.c.1"** to select all conversion workspaces with source database version equal to 12.c.1. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ListConversionWorkspacesRequest.new
    
    # Call the list_conversion_workspaces method.
    result = client.list_conversion_workspaces request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::ConversionWorkspace.
      p item
    end

### #list_mapping_rules
    
    
    def list_mapping_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MappingRule>
    def list_mapping_rules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MappingRule>

Lists the mapping rules for a specific conversion workspace.

**Overloads**
    
    
    def list_mapping_rules(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MappingRule>

Pass arguments to `list_mapping_rules` via a request object, either of type [ListMappingRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListMappingRulesRequest "Google::Cloud::CloudDMS::V1::ListMappingRulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ListMappingRulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListMappingRulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_mapping_rules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MappingRule>

Pass arguments to `list_mapping_rules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Name of the conversion workspace resource whose mapping rules are listed in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **page_size** (::Integer) — The maximum number of rules to return. The service may return fewer than this value. 
  * **page_token** (::String) — The nextPageToken value received in the previous call to mappingRules.list, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to mappingRules.list must match the call that provided the page token. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::MappingRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MappingRule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ListMappingRulesRequest.new
    
    # Call the list_mapping_rules method.
    result = client.list_mapping_rules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::MappingRule.
      p item
    end

### #list_migration_jobs
    
    
    def list_migration_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MigrationJob>
    def list_migration_jobs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MigrationJob>

Lists migration jobs in a given project and location.

**Overloads**
    
    
    def list_migration_jobs(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MigrationJob>

Pass arguments to `list_migration_jobs` via a request object, either of type [ListMigrationJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListMigrationJobsRequest "Google::Cloud::CloudDMS::V1::ListMigrationJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ListMigrationJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListMigrationJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_migration_jobs(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::MigrationJob>

Pass arguments to `list_migration_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent which owns this collection of migrationJobs. 
  * **page_size** (::Integer) — The maximum number of migration jobs to return. The service may return fewer than this value. If unspecified, at most 50 migration jobs will be returned. The maximum value is 1000; values above 1000 are coerced to 1000\. 
  * **page_token** (::String) — The nextPageToken value received in the previous call to migrationJobs.list, used in the subsequent request to retrieve the next page of results. On first call this should be left blank. When paginating, all other parameters provided to migrationJobs.list must match the call that provided the page token. 
  * **filter** (::String) — A filter expression that filters migration jobs listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be either =, !=, >, or <. For example, list migration jobs created this year by specifying **createTime %gt; 2020-01-01T00:00:00.000000000Z.** You can also filter nested fields. For example, you could specify **reverseSshConnectivity.vmIp = "1.2.3.4"** to select all migration jobs connecting through the specific SSH tunnel bastion. 
  * **order_by** (::String) — Sort the results based on the migration job name. Valid values are: "name", "name asc", and "name desc". 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ListMigrationJobsRequest.new
    
    # Call the list_migration_jobs method.
    result = client.list_migration_jobs request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::MigrationJob.
      p item
    end

### #list_private_connections
    
    
    def list_private_connections(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::PrivateConnection>
    def list_private_connections(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::PrivateConnection>

Retrieves a list of private connections in a given project and location.

**Overloads**
    
    
    def list_private_connections(request, options = nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::PrivateConnection>

Pass arguments to `list_private_connections` via a request object, either of type [ListPrivateConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListPrivateConnectionsRequest "Google::Cloud::CloudDMS::V1::ListPrivateConnectionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ListPrivateConnectionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ListPrivateConnectionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def list_private_connections(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::PagedEnumerable<::Google::Cloud::CloudDMS::V1::PrivateConnection>

Pass arguments to `list_private_connections` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent that owns the collection of private connections. 
  * **page_size** (::Integer) — Maximum number of private connections to return. If unspecified, at most 50 private connections that are returned. The maximum value is 1000; values above 1000 are coerced to 1000. 
  * **page_token** (::String) — Page token received from a previous `ListPrivateConnections` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListPrivateConnections` must match the call that provided the page token. 

  * **filter** (::String) — A filter expression that filters private connections listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be either =, !=, >, or <. For example, list private connections created this year by specifying **createTime %gt; 2021-01-01T00:00:00.000000000Z**. 
  * **order_by** (::String) — Order by fields for the result. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PrivateConnection)>) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::PagedEnumerable<[::Google::Cloud::CloudDMS::V1::PrivateConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PrivateConnection)>) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ListPrivateConnectionsRequest.new
    
    # Call the list_private_connections method.
    result = client.list_private_connections request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::CloudDMS::V1::PrivateConnection.
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



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::CloudDMS::V1::DataMigrationService::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::CloudDMS::V1::DataMigrationService::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-DataMigrationService-Operations)) 



### #promote_migration_job
    
    
    def promote_migration_job(request, options = nil) -> ::Gapic::Operation
    def promote_migration_job(name: nil) -> ::Gapic::Operation

Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.

**Overloads**
    
    
    def promote_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `promote_migration_job` via a request object, either of type [PromoteMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PromoteMigrationJobRequest "Google::Cloud::CloudDMS::V1::PromoteMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::PromoteMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-PromoteMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def promote_migration_job(name: nil) -> ::Gapic::Operation

Pass arguments to `promote_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the migration job resource to promote. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::PromoteMigrationJobRequest.new
    
    # Call the promote_migration_job method.
    result = client.promote_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #restart_migration_job
    
    
    def restart_migration_job(request, options = nil) -> ::Gapic::Operation
    def restart_migration_job(name: nil, skip_validation: nil) -> ::Gapic::Operation

Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.

**Overloads**
    
    
    def restart_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restart_migration_job` via a request object, either of type [RestartMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-RestartMigrationJobRequest "Google::Cloud::CloudDMS::V1::RestartMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::RestartMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-RestartMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def restart_migration_job(name: nil, skip_validation: nil) -> ::Gapic::Operation

Pass arguments to `restart_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the migration job resource to restart. 
  * **skip_validation** (::Boolean) — Optional. Restart the migration job without running prior configuration verification. Defaults to `false`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::RestartMigrationJobRequest.new
    
    # Call the restart_migration_job method.
    result = client.restart_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #resume_migration_job
    
    
    def resume_migration_job(request, options = nil) -> ::Gapic::Operation
    def resume_migration_job(name: nil) -> ::Gapic::Operation

Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).

**Overloads**
    
    
    def resume_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `resume_migration_job` via a request object, either of type [ResumeMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ResumeMigrationJobRequest "Google::Cloud::CloudDMS::V1::ResumeMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::ResumeMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ResumeMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def resume_migration_job(name: nil) -> ::Gapic::Operation

Pass arguments to `resume_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the migration job resource to resume. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::ResumeMigrationJobRequest.new
    
    # Call the resume_migration_job method.
    result = client.resume_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #rollback_conversion_workspace
    
    
    def rollback_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def rollback_conversion_workspace(name: nil) -> ::Gapic::Operation

Rolls back a conversion workspace to the last committed snapshot.

**Overloads**
    
    
    def rollback_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `rollback_conversion_workspace` via a request object, either of type [RollbackConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-RollbackConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::RollbackConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::RollbackConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-RollbackConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def rollback_conversion_workspace(name: nil) -> ::Gapic::Operation

Pass arguments to `rollback_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the conversion workspace resource to roll back to. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::RollbackConversionWorkspaceRequest.new
    
    # Call the rollback_conversion_workspace method.
    result = client.rollback_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #search_background_jobs
    
    
    def search_background_jobs(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse
    def search_background_jobs(conversion_workspace: nil, return_most_recent_per_job_type: nil, max_size: nil, completed_until_time: nil) -> ::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse

Searches/lists the background jobs for a specific conversion workspace.

The background jobs are not resources like conversion workspaces or mapping rules, and they can't be created, updated or deleted. Instead, they are a way to expose the data plane jobs log.

**Overloads**
    
    
    def search_background_jobs(request, options = nil) -> ::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse

Pass arguments to `search_background_jobs` via a request object, either of type [SearchBackgroundJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SearchBackgroundJobsRequest "Google::Cloud::CloudDMS::V1::SearchBackgroundJobsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SearchBackgroundJobsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def search_background_jobs(conversion_workspace: nil, return_most_recent_per_job_type: nil, max_size: nil, completed_until_time: nil) -> ::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse

Pass arguments to `search_background_jobs` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **conversion_workspace** (::String) — Required. Name of the conversion workspace resource whose jobs are listed, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **return_most_recent_per_job_type** (::Boolean) — Optional. Whether or not to return just the most recent job per job type, 
  * **max_size** (::Integer) — Optional. The maximum number of jobs to return. The service may return fewer than this value. If unspecified, at most 100 jobs are returned. The maximum value is 100; values above 100 are coerced to 100\. 
  * **completed_until_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Optional. If provided, only returns jobs that completed until (not including) the given timestamp. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** ([::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SearchBackgroundJobsResponse)) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * ([::Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SearchBackgroundJobsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::SearchBackgroundJobsRequest.new
    
    # Call the search_background_jobs method.
    result = client.search_background_jobs request
    
    # The returned object is of type Google::Cloud::CloudDMS::V1::SearchBackgroundJobsResponse.
    p result

### #seed_conversion_workspace
    
    
    def seed_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def seed_conversion_workspace(name: nil, auto_commit: nil, source_connection_profile: nil, destination_connection_profile: nil) -> ::Gapic::Operation

Imports a snapshot of the source database into the conversion workspace.

**Overloads**
    
    
    def seed_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `seed_conversion_workspace` via a request object, either of type [SeedConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SeedConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::SeedConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::SeedConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-SeedConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def seed_conversion_workspace(name: nil, auto_commit: nil, source_connection_profile: nil, destination_connection_profile: nil) -> ::Gapic::Operation

Pass arguments to `seed_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the conversion workspace resource to seed with new database structure, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversion_workspace}. 
  * **auto_commit** (::Boolean) — Should the conversion workspace be committed automatically after the seed operation. 
  * **source_connection_profile** (::String) — Optional. Fully qualified (Uri) name of the source connection profile.

Note: The following parameters are mutually exclusive: `source_connection_profile`, `destination_connection_profile`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **destination_connection_profile** (::String) — Optional. Fully qualified (Uri) name of the destination connection profile.

Note: The following parameters are mutually exclusive: `destination_connection_profile`, `source_connection_profile`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::SeedConversionWorkspaceRequest.new
    
    # Call the seed_conversion_workspace method.
    result = client.seed_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #start_migration_job
    
    
    def start_migration_job(request, options = nil) -> ::Gapic::Operation
    def start_migration_job(name: nil, skip_validation: nil) -> ::Gapic::Operation

Start an already created migration job.

**Overloads**
    
    
    def start_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `start_migration_job` via a request object, either of type [StartMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StartMigrationJobRequest "Google::Cloud::CloudDMS::V1::StartMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::StartMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StartMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def start_migration_job(name: nil, skip_validation: nil) -> ::Gapic::Operation

Pass arguments to `start_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the migration job resource to start. 
  * **skip_validation** (::Boolean) — Optional. Start the migration job without running prior configuration verification. Defaults to `false`. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::StartMigrationJobRequest.new
    
    # Call the start_migration_job method.
    result = client.start_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #stop_migration_job
    
    
    def stop_migration_job(request, options = nil) -> ::Gapic::Operation
    def stop_migration_job(name: nil) -> ::Gapic::Operation

Stops a running migration job.

**Overloads**
    
    
    def stop_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `stop_migration_job` via a request object, either of type [StopMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StopMigrationJobRequest "Google::Cloud::CloudDMS::V1::StopMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::StopMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-StopMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def stop_migration_job(name: nil) -> ::Gapic::Operation

Pass arguments to `stop_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Name of the migration job resource to stop. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::StopMigrationJobRequest.new
    
    # Call the stop_migration_job method.
    result = client.stop_migration_job request
    
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



### #update_connection_profile
    
    
    def update_connection_profile(request, options = nil) -> ::Gapic::Operation
    def update_connection_profile(update_mask: nil, connection_profile: nil, request_id: nil, validate_only: nil, skip_validation: nil) -> ::Gapic::Operation

Update the configuration of a single connection profile.

**Overloads**
    
    
    def update_connection_profile(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_connection_profile` via a request object, either of type [UpdateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateConnectionProfileRequest "Google::Cloud::CloudDMS::V1::UpdateConnectionProfileRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::UpdateConnectionProfileRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateConnectionProfileRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_connection_profile(update_mask: nil, connection_profile: nil, request_id: nil, validate_only: nil, skip_validation: nil) -> ::Gapic::Operation

Pass arguments to `update_connection_profile` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource. 
  * **connection_profile** ([::Google::Cloud::CloudDMS::V1::ConnectionProfile](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConnectionProfile), ::Hash) — Required. The connection profile parameters to update. 
  * **request_id** (::String) — Optional. A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 

  * **validate_only** (::Boolean) — Optional. Only validate the connection profile, but don't update any resources. The default is false. Only supported for Oracle connection profiles. 
  * **skip_validation** (::Boolean) — Optional. Update the connection profile without validating it. The default is false. Only supported for Oracle connection profiles. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::UpdateConnectionProfileRequest.new
    
    # Call the update_connection_profile method.
    result = client.update_connection_profile request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_conversion_workspace
    
    
    def update_conversion_workspace(request, options = nil) -> ::Gapic::Operation
    def update_conversion_workspace(update_mask: nil, conversion_workspace: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single conversion workspace.

**Overloads**
    
    
    def update_conversion_workspace(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_conversion_workspace` via a request object, either of type [UpdateConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateConversionWorkspaceRequest "Google::Cloud::CloudDMS::V1::UpdateConversionWorkspaceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::UpdateConversionWorkspaceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateConversionWorkspaceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_conversion_workspace(update_mask: nil, conversion_workspace: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_conversion_workspace` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource. 
  * **conversion_workspace** ([::Google::Cloud::CloudDMS::V1::ConversionWorkspace](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-ConversionWorkspace), ::Hash) — Required. The conversion workspace parameters to update. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::UpdateConversionWorkspaceRequest.new
    
    # Call the update_conversion_workspace method.
    result = client.update_conversion_workspace request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_migration_job
    
    
    def update_migration_job(request, options = nil) -> ::Gapic::Operation
    def update_migration_job(update_mask: nil, migration_job: nil, request_id: nil) -> ::Gapic::Operation

Updates the parameters of a single migration job.

**Overloads**
    
    
    def update_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_migration_job` via a request object, either of type [UpdateMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateMigrationJobRequest "Google::Cloud::CloudDMS::V1::UpdateMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::UpdateMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-UpdateMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def update_migration_job(update_mask: nil, migration_job: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten by the update in the conversion workspace resource. 
  * **migration_job** ([::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob), ::Hash) — Required. The migration job parameters to update. 
  * **request_id** (::String) — A unique ID used to identify the request. If the server receives two requests with the same ID, then the second request is ignored.

It is recommended to always set this value to a UUID.

The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), and hyphens (-). The maximum length is 40 characters. 




**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::UpdateMigrationJobRequest.new
    
    # Call the update_migration_job method.
    result = client.update_migration_job request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #verify_migration_job
    
    
    def verify_migration_job(request, options = nil) -> ::Gapic::Operation
    def verify_migration_job(name: nil, update_mask: nil, migration_job: nil) -> ::Gapic::Operation

Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.

**Overloads**
    
    
    def verify_migration_job(request, options = nil) -> ::Gapic::Operation

Pass arguments to `verify_migration_job` via a request object, either of type [VerifyMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VerifyMigrationJobRequest "Google::Cloud::CloudDMS::V1::VerifyMigrationJobRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::CloudDMS::V1::VerifyMigrationJobRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-VerifyMigrationJobRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries, etc. Optional. 


    
    
    def verify_migration_job(name: nil, update_mask: nil, migration_job: nil) -> ::Gapic::Operation

Pass arguments to `verify_migration_job` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Name of the migration job resource to verify. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. Field mask is used to specify the changed fields to be verified. It will not update the migration job. 
  * **migration_job** ([::Google::Cloud::CloudDMS::V1::MigrationJob](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_dms-v1/latest/Google-Cloud-CloudDMS-V1-MigrationJob), ::Hash) — Optional. The changed migration job parameters to verify. It will not update the migration job. 



**Yields**

  * (response, operation) — Access the result along with the RPC operation 



**Yield Parameters**

  * **response** (::Gapic::Operation) 
  * **operation** (::GRPC::ActiveCall::Operation) 



**Returns**

  * (::Gapic::Operation) 



**Raises**

  * (::Google::Cloud::Error) — if the RPC is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/cloud_dms/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::CloudDMS::V1::DataMigrationService::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::CloudDMS::V1::VerifyMigrationJobRequest.new
    
    # Call the verify_migration_job method.
    result = client.verify_migration_job request
    
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

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
