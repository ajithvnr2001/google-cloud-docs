---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client/
title: Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:33.549831+00:00
---

# Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API class Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.

REST client for the BackupDR service.

The BackupDR Service

## Inherits

  * Object 



## Includes

  * [Google::Cloud::BackupDR::V1::BackupDR::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the BackupDR Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration "Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all BackupDR clients
    ::Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the BackupDR Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client#Google__Cloud__BackupDR__V1__BackupDR__Rest__Client_configure_class_ "Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration "Google::Cloud::BackupDR::V1::BackupDR::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration)) 



### #create_backup_plan
    
    
    def create_backup_plan(request, options = nil) -> ::Gapic::Operation
    def create_backup_plan(parent: nil, backup_plan_id: nil, backup_plan: nil, request_id: nil) -> ::Gapic::Operation

Create a BackupPlan

**Overloads**
    
    
    def create_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan` via a request object, either of type [CreateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanRequest "Google::Cloud::BackupDR::V1::CreateBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::CreateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_plan(parent: nil, backup_plan_id: nil, backup_plan: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The `BackupPlan` project and location in the format `projects/{project}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**. 
  * **backup_plan_id** (::String) — Required. The name of the `BackupPlan` to create. The name must be unique for the specified project and location.The name must start with a lowercase letter followed by up to 62 lowercase letters, numbers, or hyphens. Pattern, /[a-z][a-z0-9-]{,62}/. 
  * **backup_plan** ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan), ::Hash) — Required. The `BackupPlan` resource object to create. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::CreateBackupPlanRequest.new
    
    # Call the create_backup_plan method.
    result = client.create_backup_plan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backup_plan_association
    
    
    def create_backup_plan_association(request, options = nil) -> ::Gapic::Operation
    def create_backup_plan_association(parent: nil, backup_plan_association_id: nil, backup_plan_association: nil, request_id: nil) -> ::Gapic::Operation

Create a BackupPlanAssociation

**Overloads**
    
    
    def create_backup_plan_association(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan_association` via a request object, either of type [CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanAssociationRequest "Google::Cloud::BackupDR::V1::CreateBackupPlanAssociationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupPlanAssociationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_plan_association(parent: nil, backup_plan_association_id: nil, backup_plan_association: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan_association` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The backup plan association project and location in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR locations map to GCP regions, for example **us-central1**. 
  * **backup_plan_association_id** (::String) — Required. The name of the backup plan association to create. The name must be unique for the specified project and location. 
  * **backup_plan_association** ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::CreateBackupPlanAssociationRequest.new
    
    # Call the create_backup_plan_association method.
    result = client.create_backup_plan_association request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backup_vault
    
    
    def create_backup_vault(request, options = nil) -> ::Gapic::Operation
    def create_backup_vault(parent: nil, backup_vault_id: nil, backup_vault: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Creates a new BackupVault in a given project and location.

**Overloads**
    
    
    def create_backup_vault(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup_vault` via a request object, either of type [CreateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupVaultRequest "Google::Cloud::BackupDR::V1::CreateBackupVaultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::CreateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateBackupVaultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_vault(parent: nil, backup_vault_id: nil, backup_vault: nil, request_id: nil, validate_only: nil) -> ::Gapic::Operation

Pass arguments to `create_backup_vault` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Value for parent. 
  * **backup_vault_id** (::String) — Required. ID of the requesting object If auto-generating ID server-side, remove this field and backup_vault_id from the method_signature of Create RPC 
  * **backup_vault** ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault), ::Hash) — Required. The resource being created 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::CreateBackupVaultRequest.new
    
    # Call the create_backup_vault method.
    result = client.create_backup_vault request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_management_server
    
    
    def create_management_server(request, options = nil) -> ::Gapic::Operation
    def create_management_server(parent: nil, management_server_id: nil, management_server: nil, request_id: nil) -> ::Gapic::Operation

Creates a new ManagementServer in a given project and location.

**Overloads**
    
    
    def create_management_server(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_management_server` via a request object, either of type [CreateManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateManagementServerRequest "Google::Cloud::BackupDR::V1::CreateManagementServerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::CreateManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CreateManagementServerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_management_server(parent: nil, management_server_id: nil, management_server: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `create_management_server` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The management server project and location in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR locations map to Google Cloud regions, for example **us-central1**. 
  * **management_server_id** (::String) — Required. The name of the management server to create. The name must be unique for the specified project and location. 
  * **management_server** ([::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer), ::Hash) — Required. A [management server resource][google.cloud.backupdr.v1.ManagementServer] 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::CreateManagementServerRequest.new
    
    # Call the create_management_server method.
    result = client.create_management_server request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backup
    
    
    def delete_backup(request, options = nil) -> ::Gapic::Operation
    def delete_backup(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a Backup.

**Overloads**
    
    
    def delete_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via a request object, either of type [DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupRequest "Google::Cloud::BackupDR::V1::DeleteBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::DeleteBackupRequest.new
    
    # Call the delete_backup method.
    result = client.delete_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backup_plan
    
    
    def delete_backup_plan(request, options = nil) -> ::Gapic::Operation
    def delete_backup_plan(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single BackupPlan.

**Overloads**
    
    
    def delete_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan` via a request object, either of type [DeleteBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanRequest "Google::Cloud::BackupDR::V1::DeleteBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::DeleteBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_plan(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the `BackupPlan` to delete.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`

  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::DeleteBackupPlanRequest.new
    
    # Call the delete_backup_plan method.
    result = client.delete_backup_plan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backup_plan_association
    
    
    def delete_backup_plan_association(request, options = nil) -> ::Gapic::Operation
    def delete_backup_plan_association(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single BackupPlanAssociation.

**Overloads**
    
    
    def delete_backup_plan_association(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan_association` via a request object, either of type [DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanAssociationRequest "Google::Cloud::BackupDR::V1::DeleteBackupPlanAssociationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupPlanAssociationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_plan_association(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan_association` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::DeleteBackupPlanAssociationRequest.new
    
    # Call the delete_backup_plan_association method.
    result = client.delete_backup_plan_association request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_backup_vault
    
    
    def delete_backup_vault(request, options = nil) -> ::Gapic::Operation
    def delete_backup_vault(name: nil, request_id: nil, force: nil, etag: nil, validate_only: nil, allow_missing: nil, ignore_backup_plan_references: nil) -> ::Gapic::Operation

Deletes a BackupVault.

**Overloads**
    
    
    def delete_backup_vault(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_vault` via a request object, either of type [DeleteBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupVaultRequest "Google::Cloud::BackupDR::V1::DeleteBackupVaultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::DeleteBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteBackupVaultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_vault(name: nil, request_id: nil, force: nil, etag: nil, validate_only: nil, allow_missing: nil, ignore_backup_plan_references: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_vault` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **force** (::Boolean) — Optional. If set to true, any data source from this backup vault will also be deleted. 
  * **etag** (::String) — The current etag of the backup vault. If an etag is provided and does not match the current etag of the connection, deletion will be blocked. 
  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 
  * **allow_missing** (::Boolean) — Optional. If true and the BackupVault is not found, the request will succeed but no action will be taken. 
  * **ignore_backup_plan_references** (::Boolean) — Optional. If set to true, backupvault deletion will proceed even if there are backup plans referencing the backupvault. The default is 'false'. 



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::DeleteBackupVaultRequest.new
    
    # Call the delete_backup_vault method.
    result = client.delete_backup_vault request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_management_server
    
    
    def delete_management_server(request, options = nil) -> ::Gapic::Operation
    def delete_management_server(name: nil, request_id: nil) -> ::Gapic::Operation

Deletes a single ManagementServer.

**Overloads**
    
    
    def delete_management_server(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_management_server` via a request object, either of type [DeleteManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteManagementServerRequest "Google::Cloud::BackupDR::V1::DeleteManagementServerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::DeleteManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DeleteManagementServerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_management_server(name: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `delete_management_server` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the resource 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::DeleteManagementServerRequest.new
    
    # Call the delete_management_server method.
    result = client.delete_management_server request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #fetch_backup_plan_associations_for_resource_type
    
    
    def fetch_backup_plan_associations_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>
    def fetch_backup_plan_associations_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

List BackupPlanAssociations for a given resource type.

**Overloads**
    
    
    def fetch_backup_plan_associations_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

Pass arguments to `fetch_backup_plan_associations_for_resource_type` via a request object, either of type [FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeRequest "Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupPlanAssociationsForResourceTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_backup_plan_associations_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

Pass arguments to `fetch_backup_plan_associations_for_resource_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 
  * **resource_type** (::String) — Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance 
  * **page_size** (::Integer) — Optional. The maximum number of BackupPlanAssociations to return. The service may return fewer than this value. If unspecified, at most 50 BackupPlanAssociations will be returned. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call of `FetchBackupPlanAssociationsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupPlanAssociationsForResourceType` must match the call that provided the page token. 

  * **filter** (::String) — 

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

    * resource
    * backup_plan
    * state
    * data_source
    * cloud_sql_instance_backup_plan_association_properties.instance_create_time
  * **order_by** (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * name



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::FetchBackupPlanAssociationsForResourceTypeRequest.new
    
    # Call the fetch_backup_plan_associations_for_resource_type method.
    result = client.fetch_backup_plan_associations_for_resource_type request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupPlanAssociation.
      p item
    end

### #fetch_backups_for_resource_type
    
    
    def fetch_backups_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>
    def fetch_backups_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Fetch Backups for a given resource type.

**Overloads**
    
    
    def fetch_backups_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Pass arguments to `fetch_backups_for_resource_type` via a request object, either of type [FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupsForResourceTypeRequest "Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchBackupsForResourceTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_backups_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Pass arguments to `fetch_backups_for_resource_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Datasources are the parent resource for the backups. Format: projects/{project}/locations/{location}/backupVaults/{backupVaultId}/dataSources/{datasourceId} 
  * **resource_type** (::String) — Required. The type of the GCP resource. Ex: sqladmin.googleapis.com/Instance 
  * **page_size** (::Integer) — Optional. The maximum number of Backups to return. The service may return fewer than this value. If unspecified, at most 50 Backups will be returned. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call of `FetchBackupsForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchBackupsForResourceType` must match the call that provided the page token. 

  * **filter** (::String) — Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields: 
  * **order_by** (::String) — Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. 
  * **view** ([::Google::Cloud::BackupDR::V1::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupView)) — Optional. This parameter is used to specify the view of the backup. If not specified, the default view is BASIC. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::FetchBackupsForResourceTypeRequest.new
    
    # Call the fetch_backups_for_resource_type method.
    result = client.fetch_backups_for_resource_type request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::Backup.
      p item
    end

### #fetch_data_source_references_for_resource_type
    
    
    def fetch_data_source_references_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>
    def fetch_data_source_references_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Fetch DataSourceReferences for a given project, location and resource type.

**Overloads**
    
    
    def fetch_data_source_references_for_resource_type(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Pass arguments to `fetch_data_source_references_for_resource_type` via a request object, either of type [FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchDataSourceReferencesForResourceTypeRequest "Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchDataSourceReferencesForResourceTypeRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_data_source_references_for_resource_type(parent: nil, resource_type: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Pass arguments to `fetch_data_source_references_for_resource_type` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 
  * **resource_type** (::String) — Required. The type of the GCP resource. Ex: sql.googleapis.com/Instance 
  * **page_size** (::Integer) — Optional. The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous call of `FetchDataSourceReferencesForResourceType`. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `FetchDataSourceReferencesForResourceType` must match the call that provided the page token. 

  * **filter** (::String) — 

Optional. A filter expression that filters the results fetched in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. Supported fields:

    * data_source
    * data_source_gcp_resource_info.gcp_resourcename
    * data_source_backup_config_state
    * data_source_backup_count
    * data_source_backup_config_info.last_backup_state
    * data_source_gcp_resource_info.gcp_resourcename
    * data_source_gcp_resource_info.type
    * data_source_gcp_resource_info.location
    * data_source_gcp_resource_info.cloud_sql_instance_properties.instance_create_time
  * **order_by** (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * name



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::FetchDataSourceReferencesForResourceTypeRequest.new
    
    # Call the fetch_data_source_references_for_resource_type method.
    result = client.fetch_data_source_references_for_resource_type request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::DataSourceReference.
      p item
    end

### #fetch_usable_backup_vaults
    
    
    def fetch_usable_backup_vaults(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>
    def fetch_usable_backup_vaults(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

FetchUsableBackupVaults lists usable BackupVaults in a given project and location. Usable BackupVault are the ones that user has backupdr.backupVaults.get permission.

**Overloads**
    
    
    def fetch_usable_backup_vaults(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

Pass arguments to `fetch_usable_backup_vaults` via a request object, either of type [FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchUsableBackupVaultsRequest "Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-FetchUsableBackupVaultsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def fetch_usable_backup_vaults(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

Pass arguments to `fetch_usable_backup_vaults` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::FetchUsableBackupVaultsRequest.new
    
    # Call the fetch_usable_backup_vaults method.
    result = client.fetch_usable_backup_vaults request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupVault.
      p item
    end

### #get_backup
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::BackupDR::V1::Backup
    def get_backup(name: nil, view: nil) -> ::Google::Cloud::BackupDR::V1::Backup

Gets details of a Backup.

**Overloads**
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::BackupDR::V1::Backup

Pass arguments to `get_backup` via a request object, either of type [GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupRequest "Google::Cloud::BackupDR::V1::GetBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup(name: nil, view: nil) -> ::Google::Cloud::BackupDR::V1::Backup

Pass arguments to `get_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{backupVault}/dataSources/{datasource}/backups/{backup}' 
  * **view** ([::Google::Cloud::BackupDR::V1::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetBackupRequest.new
    
    # Call the get_backup method.
    result = client.get_backup request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::Backup.
    p result

### #get_backup_plan
    
    
    def get_backup_plan(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlan
    def get_backup_plan(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlan

Gets details of a single BackupPlan.

**Overloads**
    
    
    def get_backup_plan(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlan

Pass arguments to `get_backup_plan` via a request object, either of type [GetBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRequest "Google::Cloud::BackupDR::V1::GetBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_plan(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlan

Pass arguments to `get_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the `BackupPlan` to retrieve.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetBackupPlanRequest.new
    
    # Call the get_backup_plan method.
    result = client.get_backup_plan request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::BackupPlan.
    p result

### #get_backup_plan_association
    
    
    def get_backup_plan_association(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation
    def get_backup_plan_association(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation

Gets details of a single BackupPlanAssociation.

**Overloads**
    
    
    def get_backup_plan_association(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation

Pass arguments to `get_backup_plan_association` via a request object, either of type [GetBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanAssociationRequest "Google::Cloud::BackupDR::V1::GetBackupPlanAssociationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanAssociationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_plan_association(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanAssociation

Pass arguments to `get_backup_plan_association` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetBackupPlanAssociationRequest.new
    
    # Call the get_backup_plan_association method.
    result = client.get_backup_plan_association request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::BackupPlanAssociation.
    p result

### #get_backup_plan_revision
    
    
    def get_backup_plan_revision(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanRevision
    def get_backup_plan_revision(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanRevision

Gets details of a single BackupPlanRevision.

**Overloads**
    
    
    def get_backup_plan_revision(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanRevision

Pass arguments to `get_backup_plan_revision` via a request object, either of type [GetBackupPlanRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRevisionRequest "Google::Cloud::BackupDR::V1::GetBackupPlanRevisionRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetBackupPlanRevisionRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupPlanRevisionRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_plan_revision(name: nil) -> ::Google::Cloud::BackupDR::V1::BackupPlanRevision

Pass arguments to `get_backup_plan_revision` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The resource name of the `BackupPlanRevision` to retrieve.

Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}/revisions/{revision}`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetBackupPlanRevisionRequest.new
    
    # Call the get_backup_plan_revision method.
    result = client.get_backup_plan_revision request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::BackupPlanRevision.
    p result

### #get_backup_vault
    
    
    def get_backup_vault(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupVault
    def get_backup_vault(name: nil, view: nil) -> ::Google::Cloud::BackupDR::V1::BackupVault

Gets details of a BackupVault.

**Overloads**
    
    
    def get_backup_vault(request, options = nil) -> ::Google::Cloud::BackupDR::V1::BackupVault

Pass arguments to `get_backup_vault` via a request object, either of type [GetBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupVaultRequest "Google::Cloud::BackupDR::V1::GetBackupVaultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetBackupVaultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_vault(name: nil, view: nil) -> ::Google::Cloud::BackupDR::V1::BackupVault

Pass arguments to `get_backup_vault` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the backupvault store resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}' 
  * **view** ([::Google::Cloud::BackupDR::V1::BackupVaultView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVaultView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup Vault 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetBackupVaultRequest.new
    
    # Call the get_backup_vault method.
    result = client.get_backup_vault request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::BackupVault.
    p result

### #get_data_source
    
    
    def get_data_source(request, options = nil) -> ::Google::Cloud::BackupDR::V1::DataSource
    def get_data_source(name: nil) -> ::Google::Cloud::BackupDR::V1::DataSource

Gets details of a DataSource.

**Overloads**
    
    
    def get_data_source(request, options = nil) -> ::Google::Cloud::BackupDR::V1::DataSource

Pass arguments to `get_data_source` via a request object, either of type [GetDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceRequest "Google::Cloud::BackupDR::V1::GetDataSourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_source(name: nil) -> ::Google::Cloud::BackupDR::V1::DataSource

Pass arguments to `get_data_source` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the data source resource name, in the format 'projects/{project_id}/locations/{location}/backupVaults/{resource_name}/dataSource/{resource_name}' 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetDataSourceRequest.new
    
    # Call the get_data_source method.
    result = client.get_data_source request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::DataSource.
    p result

### #get_data_source_reference
    
    
    def get_data_source_reference(request, options = nil) -> ::Google::Cloud::BackupDR::V1::DataSourceReference
    def get_data_source_reference(name: nil) -> ::Google::Cloud::BackupDR::V1::DataSourceReference

Gets details of a single DataSourceReference.

**Overloads**
    
    
    def get_data_source_reference(request, options = nil) -> ::Google::Cloud::BackupDR::V1::DataSourceReference

Pass arguments to `get_data_source_reference` via a request object, either of type [GetDataSourceReferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceReferenceRequest "Google::Cloud::BackupDR::V1::GetDataSourceReferenceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetDataSourceReferenceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetDataSourceReferenceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_data_source_reference(name: nil) -> ::Google::Cloud::BackupDR::V1::DataSourceReference

Pass arguments to `get_data_source_reference` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the DataSourceReference to retrieve. Format: projects/{project}/locations/{location}/dataSourceReferences/{data_source_reference} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetDataSourceReferenceRequest.new
    
    # Call the get_data_source_reference method.
    result = client.get_data_source_reference request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::DataSourceReference.
    p result

### #get_management_server
    
    
    def get_management_server(request, options = nil) -> ::Google::Cloud::BackupDR::V1::ManagementServer
    def get_management_server(name: nil) -> ::Google::Cloud::BackupDR::V1::ManagementServer

Gets details of a single ManagementServer.

**Overloads**
    
    
    def get_management_server(request, options = nil) -> ::Google::Cloud::BackupDR::V1::ManagementServer

Pass arguments to `get_management_server` via a request object, either of type [GetManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetManagementServerRequest "Google::Cloud::BackupDR::V1::GetManagementServerRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::GetManagementServerRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-GetManagementServerRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_management_server(name: nil) -> ::Google::Cloud::BackupDR::V1::ManagementServer

Pass arguments to `get_management_server` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the management server resource name, in the format 'projects/{project_id}/locations/{location}/managementServers/{resource_name}' 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::GetManagementServerRequest.new
    
    # Call the get_management_server method.
    result = client.get_management_server request
    
    # The returned object is of type Google::Cloud::BackupDR::V1::ManagementServer.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new BackupDR REST client object.

**Yields**

  * (config) — Configure the BackupDR client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #initialize_service
    
    
    def initialize_service(request, options = nil) -> ::Gapic::Operation
    def initialize_service(name: nil, resource_type: nil, request_id: nil, cloud_sql_instance_initialization_config: nil) -> ::Gapic::Operation

Initializes the service related config for a project.

**Overloads**
    
    
    def initialize_service(request, options = nil) -> ::Gapic::Operation

Pass arguments to `initialize_service` via a request object, either of type [InitializeServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InitializeServiceRequest "Google::Cloud::BackupDR::V1::InitializeServiceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::InitializeServiceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-InitializeServiceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def initialize_service(name: nil, resource_type: nil, request_id: nil, cloud_sql_instance_initialization_config: nil) -> ::Gapic::Operation

Pass arguments to `initialize_service` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the serviceConfig used to initialize the service. Format: `projects/{project_id}/locations/{location}/serviceConfig`. 
  * **resource_type** (::String) — Required. The resource type to which the default service config will be applied. Examples include, "compute.googleapis.com/Instance" and "storage.googleapis.com/Bucket". 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **cloud_sql_instance_initialization_config** ([::Google::Cloud::BackupDR::V1::CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-CloudSqlInstanceInitializationConfig), ::Hash) — Optional. The configuration for initializing a Cloud SQL instance. 



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::InitializeServiceRequest.new
    
    # Call the initialize_service method.
    result = client.initialize_service request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #list_backup_plan_associations
    
    
    def list_backup_plan_associations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>
    def list_backup_plan_associations(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

Lists BackupPlanAssociations in a given project and location.

**Overloads**
    
    
    def list_backup_plan_associations(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

Pass arguments to `list_backup_plan_associations` via a request object, either of type [ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanAssociationsRequest "Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanAssociationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_plan_associations(parent: nil, page_size: nil, page_token: nil, filter: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanAssociation>

Pass arguments to `list_backup_plan_associations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve backup Plan Associations information, in the format `projects/{project_id}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for example **us-central1**. To retrieve backup plan associations for all locations, use "-" for the `{location}` value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListBackupPlanAssociationsRequest.new
    
    # Call the list_backup_plan_associations method.
    result = client.list_backup_plan_associations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupPlanAssociation.
      p item
    end

### #list_backup_plan_revisions
    
    
    def list_backup_plan_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanRevision>
    def list_backup_plan_revisions(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanRevision>

Lists BackupPlanRevisions in a given project and location.

**Overloads**
    
    
    def list_backup_plan_revisions(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanRevision>

Pass arguments to `list_backup_plan_revisions` via a request object, either of type [ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanRevisionsRequest "Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlanRevisionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_plan_revisions(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlanRevision>

Pass arguments to `list_backup_plan_revisions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve `BackupPlanRevisions` information. Format: `projects/{project}/locations/{location}/backupPlans/{backup_plan}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. 
  * **page_size** (::Integer) — Optional. The maximum number of `BackupPlans` to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse#Google__Cloud__BackupDR__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::BackupDR::V1::ListBackupPlansResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse#Google__Cloud__BackupDR__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::BackupDR::V1::ListBackupPlansResponse#next_page_token \(method\)") received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlanRevision](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanRevision)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListBackupPlanRevisionsRequest.new
    
    # Call the list_backup_plan_revisions method.
    result = client.list_backup_plan_revisions request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupPlanRevision.
      p item
    end

### #list_backup_plans
    
    
    def list_backup_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlan>
    def list_backup_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlan>

Lists BackupPlans in a given project and location.

**Overloads**
    
    
    def list_backup_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlan>

Pass arguments to `list_backup_plans` via a request object, either of type [ListBackupPlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansRequest "Google::Cloud::BackupDR::V1::ListBackupPlansRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListBackupPlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupPlan>

Pass arguments to `list_backup_plans` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve `BackupPlans` information. Format: `projects/{project}/locations/{location}`. In Cloud BackupDR, locations map to GCP regions, for e.g. **us-central1**. To retrieve backup plans for all locations, use "-" for the `{location}` value. 
  * **page_size** (::Integer) — Optional. The maximum number of `BackupPlans` to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse#Google__Cloud__BackupDR__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::BackupDR::V1::ListBackupPlansResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupPlansResponse#Google__Cloud__BackupDR__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::BackupDR::V1::ListBackupPlansResponse#next_page_token \(method\)") received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListBackupPlansRequest.new
    
    # Call the list_backup_plans method.
    result = client.list_backup_plans request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupPlan.
      p item
    end

### #list_backup_vaults
    
    
    def list_backup_vaults(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>
    def list_backup_vaults(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

Lists BackupVaults in a given project and location.

**Overloads**
    
    
    def list_backup_vaults(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

Pass arguments to `list_backup_vaults` via a request object, either of type [ListBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupVaultsRequest "Google::Cloud::BackupDR::V1::ListBackupVaultsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListBackupVaultsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupVaultsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_vaults(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::BackupVault>

Pass arguments to `list_backup_vaults` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve backupvault stores information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve backupvault stores for all locations, use "-" for the '{location}' value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 
  * **view** ([::Google::Cloud::BackupDR::V1::BackupVaultView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVaultView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup Vault. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListBackupVaultsRequest.new
    
    # Call the list_backup_vaults method.
    result = client.list_backup_vaults request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::BackupVault.
      p item
    end

### #list_backups
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Lists Backups in a given project and location.

**Overloads**
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Pass arguments to `list_backups` via a request object, either of type [ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupsRequest "Google::Cloud::BackupDR::V1::ListBackupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListBackupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, view: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::Backup>

Pass arguments to `list_backups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve backup information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 
  * **view** ([::Google::Cloud::BackupDR::V1::BackupView](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupView)) — Optional. Reserved for future use to provide a BASIC & FULL view of Backup resource. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListBackupsRequest.new
    
    # Call the list_backups method.
    result = client.list_backups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::Backup.
      p item
    end

### #list_data_source_references
    
    
    def list_data_source_references(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>
    def list_data_source_references(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Lists DataSourceReferences for a given project and location.

**Overloads**
    
    
    def list_data_source_references(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Pass arguments to `list_data_source_references` via a request object, either of type [ListDataSourceReferencesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourceReferencesRequest "Google::Cloud::BackupDR::V1::ListDataSourceReferencesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListDataSourceReferencesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourceReferencesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_source_references(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSourceReference>

Pass arguments to `list_data_source_references` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The parent resource name. Format: projects/{project}/locations/{location} 
  * **page_size** (::Integer) — Optional. The maximum number of DataSourceReferences to return. The service may return fewer than this value. If unspecified, at most 50 DataSourceReferences will be returned. The maximum value is 100; values above 100 will be coerced to 100. 
  * **page_token** (::String) — Optional. A page token, received from a previous `ListDataSourceReferences` call. Provide this to retrieve the subsequent page.

When paginating, all other parameters provided to `ListDataSourceReferences` must match the call that provided the page token. 

  * **filter** (::String) — 

Optional. A filter expression that filters the results listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering.

The following field and operator combinations are supported:

    * data_source_gcp_resource_info.gcp_resourcename with `=`, `!=`
    * data_source_gcp_resource_info.type with `=`, `!=`
  * **order_by** (::String) — 

Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.

Supported fields:

    * data_source
    * data_source_gcp_resource_info.gcp_resourcename



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSourceReference](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSourceReference)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListDataSourceReferencesRequest.new
    
    # Call the list_data_source_references method.
    result = client.list_data_source_references request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::DataSourceReference.
      p item
    end

### #list_data_sources
    
    
    def list_data_sources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSource>
    def list_data_sources(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSource>

Lists DataSources in a given project and location.

**Overloads**
    
    
    def list_data_sources(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSource>

Pass arguments to `list_data_sources` via a request object, either of type [ListDataSourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourcesRequest "Google::Cloud::BackupDR::V1::ListDataSourcesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListDataSourcesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListDataSourcesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_data_sources(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::DataSource>

Pass arguments to `list_data_sources` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve data sources information, in the format 'projects/{project_id}/locations/{location}'. In Cloud Backup and DR, locations map to Google Cloud regions, for example **us-central1**. To retrieve data sources for all locations, use "-" for the '{location}' value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListDataSourcesRequest.new
    
    # Call the list_data_sources method.
    result = client.list_data_sources request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::DataSource.
      p item
    end

### #list_management_servers
    
    
    def list_management_servers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::ManagementServer>
    def list_management_servers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::ManagementServer>

Lists ManagementServers in a given project and location.

**Overloads**
    
    
    def list_management_servers(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::ManagementServer>

Pass arguments to `list_management_servers` via a request object, either of type [ListManagementServersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListManagementServersRequest "Google::Cloud::BackupDR::V1::ListManagementServersRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::ListManagementServersRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ListManagementServersRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_management_servers(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::BackupDR::V1::ManagementServer>

Pass arguments to `list_management_servers` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The project and location for which to retrieve management servers information, in the format 'projects/{project_id}/locations/{location}'. In Cloud BackupDR, locations map to Google Cloud regions, for example **us-central1**. To retrieve management servers for all locations, use "-" for the '{location}' value. 
  * **page_size** (::Integer) — Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. 
  * **page_token** (::String) — Optional. A token identifying a page of results the server should return. 
  * **filter** (::String) — Optional. Filtering results. 
  * **order_by** (::String) — Optional. Hint for how to order the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::BackupDR::V1::ManagementServer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ManagementServer)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::ListManagementServersRequest.new
    
    # Call the list_management_servers method.
    result = client.list_management_servers request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::BackupDR::V1::ManagementServer.
      p item
    end

### #location_client
    
    
    def location_client() -> Google::Cloud::Location::Locations::Rest::Client

Get the associated client for mix-in of the Locations.

**Returns**

  * (Google::Cloud::Location::Locations::Rest::Client) 



### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::BackupDR::V1::BackupDR::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::BackupDR::V1::BackupDR::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupDR-Rest-Operations)) 



### #restore_backup
    
    
    def restore_backup(request, options = nil) -> ::Gapic::Operation
    def restore_backup(name: nil, request_id: nil, compute_instance_target_environment: nil, disk_target_environment: nil, region_disk_target_environment: nil, compute_instance_restore_properties: nil, disk_restore_properties: nil, clear_overrides_field_mask: nil) -> ::Gapic::Operation

Restore from a Backup

**Overloads**
    
    
    def restore_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restore_backup` via a request object, either of type [RestoreBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-RestoreBackupRequest "Google::Cloud::BackupDR::V1::RestoreBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::RestoreBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-RestoreBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def restore_backup(name: nil, request_id: nil, compute_instance_target_environment: nil, disk_target_environment: nil, region_disk_target_environment: nil, compute_instance_restore_properties: nil, disk_restore_properties: nil, clear_overrides_field_mask: nil) -> ::Gapic::Operation

Pass arguments to `restore_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. The resource name of the Backup instance, in the format 'projects/_/locations/_ /backupVaults/_/dataSources/_ /backups/'. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **compute_instance_target_environment** ([::Google::Cloud::BackupDR::V1::ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceTargetEnvironment), ::Hash) — Compute Engine target environment to be used during restore.

Note: The following parameters are mutually exclusive: `compute_instance_target_environment`, `disk_target_environment`, `region_disk_target_environment`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **disk_target_environment** ([::Google::Cloud::BackupDR::V1::DiskTargetEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskTargetEnvironment), ::Hash) — Disk target environment to be used during restore.

Note: The following parameters are mutually exclusive: `disk_target_environment`, `compute_instance_target_environment`, `region_disk_target_environment`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **region_disk_target_environment** ([::Google::Cloud::BackupDR::V1::RegionDiskTargetEnvironment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-RegionDiskTargetEnvironment), ::Hash) — Region disk target environment to be used during restore.

Note: The following parameters are mutually exclusive: `region_disk_target_environment`, `compute_instance_target_environment`, `disk_target_environment`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **compute_instance_restore_properties** ([::Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties), ::Hash) — Compute Engine instance properties to be overridden during restore.

Note: The following parameters are mutually exclusive: `compute_instance_restore_properties`, `disk_restore_properties`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **disk_restore_properties** ([::Google::Cloud::BackupDR::V1::DiskRestoreProperties](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DiskRestoreProperties), ::Hash) — Disk properties to be overridden during restore.

Note: The following parameters are mutually exclusive: `disk_restore_properties`, `compute_instance_restore_properties`. At most one of these parameters can be set. If more than one is set, only one will be used, and it is not defined which one. 

  * **clear_overrides_field_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — 

Optional. A field mask used to clear server-side default values for fields within the `instance_properties` oneof.

When a field in this mask is cleared, the server will not apply its default logic (like inheriting a value from the source) for that field.

The most common current use case is clearing default encryption keys.

Examples of field mask paths:

    * Compute Instance Disks: `compute_instance_restore_properties.disks.*.disk_encryption_key`
    * Single Disk: `disk_restore_properties.disk_encryption_key`



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::RestoreBackupRequest.new
    
    # Call the restore_backup method.
    result = client.restore_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #trigger_backup
    
    
    def trigger_backup(request, options = nil) -> ::Gapic::Operation
    def trigger_backup(name: nil, rule_id: nil, request_id: nil) -> ::Gapic::Operation

Triggers a new Backup.

**Overloads**
    
    
    def trigger_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `trigger_backup` via a request object, either of type [TriggerBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-TriggerBackupRequest "Google::Cloud::BackupDR::V1::TriggerBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::TriggerBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-TriggerBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def trigger_backup(name: nil, rule_id: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `trigger_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the backup plan association resource, in the format `projects/{project}/locations/{location}/backupPlanAssociations/{backupPlanAssociationId}`
  * **rule_id** (::String) — Required. backup rule_id for which a backup needs to be triggered. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes after the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::TriggerBackupRequest.new
    
    # Call the trigger_backup method.
    result = client.trigger_backup request
    
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



### #update_backup
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation
    def update_backup(update_mask: nil, backup: nil, request_id: nil) -> ::Gapic::Operation

Updates the settings of a Backup.

**Overloads**
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via a request object, either of type [UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupRequest "Google::Cloud::BackupDR::V1::UpdateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup(update_mask: nil, backup: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the Backup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. 
  * **backup** ([::Google::Cloud::BackupDR::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-Backup), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::UpdateBackupRequest.new
    
    # Call the update_backup method.
    result = client.update_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_backup_plan
    
    
    def update_backup_plan(request, options = nil) -> ::Gapic::Operation
    def update_backup_plan(backup_plan: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Update a BackupPlan.

**Overloads**
    
    
    def update_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan` via a request object, either of type [UpdateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanRequest "Google::Cloud::BackupDR::V1::UpdateBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::UpdateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_plan(backup_plan: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_plan** ([::Google::Cloud::BackupDR::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlan), ::Hash) — Required. The resource being updated 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlan resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently, these fields are supported in update: description, schedules, retention period, adding and removing Backup Rules. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::UpdateBackupPlanRequest.new
    
    # Call the update_backup_plan method.
    result = client.update_backup_plan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_backup_plan_association
    
    
    def update_backup_plan_association(request, options = nil) -> ::Gapic::Operation
    def update_backup_plan_association(backup_plan_association: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Update a BackupPlanAssociation.

**Overloads**
    
    
    def update_backup_plan_association(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan_association` via a request object, either of type [UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanAssociationRequest "Google::Cloud::BackupDR::V1::UpdateBackupPlanAssociationRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupPlanAssociationRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_plan_association(backup_plan_association: nil, update_mask: nil, request_id: nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan_association` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_plan_association** ([::Google::Cloud::BackupDR::V1::BackupPlanAssociation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupPlanAssociation), ::Hash) — Required. The resource being updated 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. Field mask is used to specify the fields to be overwritten in the BackupPlanAssociation resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. Currently backup_plan_association.backup_plan is the only supported field. 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and t he request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 




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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::UpdateBackupPlanAssociationRequest.new
    
    # Call the update_backup_plan_association method.
    result = client.update_backup_plan_association request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_backup_vault
    
    
    def update_backup_vault(request, options = nil) -> ::Gapic::Operation
    def update_backup_vault(update_mask: nil, backup_vault: nil, request_id: nil, validate_only: nil, force: nil, force_update_access_restriction: nil) -> ::Gapic::Operation

Updates the settings of a BackupVault.

**Overloads**
    
    
    def update_backup_vault(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup_vault` via a request object, either of type [UpdateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupVaultRequest "Google::Cloud::BackupDR::V1::UpdateBackupVaultRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::UpdateBackupVaultRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateBackupVaultRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_vault(update_mask: nil, backup_vault: nil, request_id: nil, validate_only: nil, force: nil, force_update_access_restriction: nil) -> ::Gapic::Operation

Pass arguments to `update_backup_vault` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the BackupVault resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. 
  * **backup_vault** ([::Google::Cloud::BackupDR::V1::BackupVault](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **validate_only** (::Boolean) — Optional. Only validate the request, but do not perform mutations. The default is 'false'. 
  * **force** (::Boolean) — Optional. If set to true, will not check plan duration against backup vault enforcement duration. 
  * **force_update_access_restriction** (::Boolean) — Optional. If set to true, we will force update access restriction even if some non compliant data sources are present. The default is 'false'. 



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::UpdateBackupVaultRequest.new
    
    # Call the update_backup_vault method.
    result = client.update_backup_vault request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_data_source
    
    
    def update_data_source(request, options = nil) -> ::Gapic::Operation
    def update_data_source(update_mask: nil, data_source: nil, request_id: nil, allow_missing: nil) -> ::Gapic::Operation

Updates the settings of a DataSource.

**Overloads**
    
    
    def update_data_source(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_data_source` via a request object, either of type [UpdateDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateDataSourceRequest "Google::Cloud::BackupDR::V1::UpdateDataSourceRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::BackupDR::V1::UpdateDataSourceRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-UpdateDataSourceRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_data_source(update_mask: nil, data_source: nil, request_id: nil, allow_missing: nil) -> ::Gapic::Operation

Pass arguments to `update_data_source` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. Field mask is used to specify the fields to be overwritten in the DataSource resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then the request will fail. 
  * **data_source** ([::Google::Cloud::BackupDR::V1::DataSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-DataSource), ::Hash) — Required. The resource being updated 
  * **request_id** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.

For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.

The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000). 

  * **allow_missing** (::Boolean) — Optional. Enable upsert. 



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
    
    
    require "google/cloud/backupdr/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::BackupDR::V1::BackupDR::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::BackupDR::V1::UpdateDataSourceRequest.new
    
    # Call the update_data_source method.
    result = client.update_data_source request
    
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

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
