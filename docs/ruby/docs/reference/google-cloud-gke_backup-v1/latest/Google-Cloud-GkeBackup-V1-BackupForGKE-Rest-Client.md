---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client/
title: Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client (v1.8.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:30.906398+00:00
---

# Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client (v1.8.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup for GKE V1 API - Class Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client (v1.8.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.0 (latest)  1.7.1  1.6.0  1.5.1  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.12.0  0.11.0  0.10.1  0.9.0  0.8.0  0.7.2  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the Backup for GKE V1 API class Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.

REST client for the BackupForGKE service.

BackupForGKE allows Kubernetes administrators to configure, execute, and manage backup and restore operations for their GKE clusters.

## Inherits

  * Object 



## Includes

  * [Google::Cloud::GkeBackup::V1::BackupForGKE::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the BackupForGKE Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration "Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all BackupForGKE clients
    ::Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the BackupForGKE Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client#Google__Cloud__GkeBackup__V1__BackupForGKE__Rest__Client_configure_class_ "Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration "Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration)) 



### #create_backup
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation
    def create_backup(parent: nil, backup: nil, backup_id: nil) -> ::Gapic::Operation

Creates a Backup for the given BackupPlan.

**Overloads**
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via a request object, either of type [CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupRequest "Google::Cloud::GkeBackup::V1::CreateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup(parent: nil, backup: nil, backup_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The BackupPlan within which to create the Backup. Format: `projects/*/locations/*/backupPlans/*`
  * **backup** ([::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup), ::Hash) — Optional. The Backup resource to create. 
  * **backup_id** (::String) — 

Optional. The client-provided short name for the Backup resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of Backups in this BackupPlan



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateBackupRequest.new
    
    # Call the create_backup method.
    result = client.create_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backup_channel
    
    
    def create_backup_channel(request, options = nil) -> ::Gapic::Operation
    def create_backup_channel(parent: nil, backup_channel: nil, backup_channel_id: nil) -> ::Gapic::Operation

Creates a new BackupChannel in a given location.

**Overloads**
    
    
    def create_backup_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup_channel` via a request object, either of type [CreateBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupChannelRequest "Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_channel(parent: nil, backup_channel: nil, backup_channel_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backup_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location within which to create the BackupChannel. Format: `projects/*/locations/*`
  * **backup_channel** ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel), ::Hash) — Required. The BackupChannel resource object to create. 
  * **backup_channel_id** (::String) — 

Optional. The client-provided short name for the BackupChannel resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of BackupChannels in this location If the user does not provide a name, a uuid will be used as the name.



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateBackupChannelRequest.new
    
    # Call the create_backup_channel method.
    result = client.create_backup_channel request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backup_plan
    
    
    def create_backup_plan(request, options = nil) -> ::Gapic::Operation
    def create_backup_plan(parent: nil, backup_plan: nil, backup_plan_id: nil) -> ::Gapic::Operation

Creates a new BackupPlan in a given location.

**Overloads**
    
    
    def create_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan` via a request object, either of type [CreateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupPlanRequest "Google::Cloud::GkeBackup::V1::CreateBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_plan(parent: nil, backup_plan: nil, backup_plan_id: nil) -> ::Gapic::Operation

Pass arguments to `create_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location within which to create the BackupPlan. Format: `projects/*/locations/*`
  * **backup_plan** ([::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan), ::Hash) — Required. The BackupPlan resource object to create. 
  * **backup_plan_id** (::String) — 

Required. The client-provided short name for the BackupPlan resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of BackupPlans in this location



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateBackupPlanRequest.new
    
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

### #create_restore
    
    
    def create_restore(request, options = nil) -> ::Gapic::Operation
    def create_restore(parent: nil, restore: nil, restore_id: nil) -> ::Gapic::Operation

Creates a new Restore for the given RestorePlan.

**Overloads**
    
    
    def create_restore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_restore` via a request object, either of type [CreateRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestoreRequest "Google::Cloud::GkeBackup::V1::CreateRestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_restore(parent: nil, restore: nil, restore_id: nil) -> ::Gapic::Operation

Pass arguments to `create_restore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The RestorePlan within which to create the Restore. Format: `projects/*/locations/*/restorePlans/*`
  * **restore** ([::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore), ::Hash) — Required. The restore resource to create. 
  * **restore_id** (::String) — 

Required. The client-provided short name for the Restore resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of Restores in this RestorePlan.



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateRestoreRequest.new
    
    # Call the create_restore method.
    result = client.create_restore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_restore_channel
    
    
    def create_restore_channel(request, options = nil) -> ::Gapic::Operation
    def create_restore_channel(parent: nil, restore_channel: nil, restore_channel_id: nil) -> ::Gapic::Operation

Creates a new RestoreChannel in a given location.

**Overloads**
    
    
    def create_restore_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_restore_channel` via a request object, either of type [CreateRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestoreChannelRequest "Google::Cloud::GkeBackup::V1::CreateRestoreChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestoreChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_restore_channel(parent: nil, restore_channel: nil, restore_channel_id: nil) -> ::Gapic::Operation

Pass arguments to `create_restore_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location within which to create the RestoreChannel. Format: `projects/*/locations/*`
  * **restore_channel** ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel), ::Hash) — Required. The RestoreChannel resource object to create. 
  * **restore_channel_id** (::String) — 

Optional. The client-provided short name for the RestoreChannel resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of RestoreChannels in this location If the user does not provide a name, a uuid will be used as the name.



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateRestoreChannelRequest.new
    
    # Call the create_restore_channel method.
    result = client.create_restore_channel request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_restore_plan
    
    
    def create_restore_plan(request, options = nil) -> ::Gapic::Operation
    def create_restore_plan(parent: nil, restore_plan: nil, restore_plan_id: nil) -> ::Gapic::Operation

Creates a new RestorePlan in a given location.

**Overloads**
    
    
    def create_restore_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_restore_plan` via a request object, either of type [CreateRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestorePlanRequest "Google::Cloud::GkeBackup::V1::CreateRestorePlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::CreateRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-CreateRestorePlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_restore_plan(parent: nil, restore_plan: nil, restore_plan_id: nil) -> ::Gapic::Operation

Pass arguments to `create_restore_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location within which to create the RestorePlan. Format: `projects/*/locations/*`
  * **restore_plan** ([::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan), ::Hash) — Required. The RestorePlan resource object to create. 
  * **restore_plan_id** (::String) — 

Required. The client-provided short name for the RestorePlan resource. This name must:

    * be between 1 and 63 characters long (inclusive)
    * consist of only lower-case ASCII letters, numbers, and dashes
    * start with a lower-case letter
    * end with a lower-case letter or number
    * be unique within the set of RestorePlans in this location



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::CreateRestorePlanRequest.new
    
    # Call the create_restore_plan method.
    result = client.create_restore_plan request
    
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
    def delete_backup(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Deletes an existing Backup.

**Overloads**
    
    
    def delete_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via a request object, either of type [DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupRequest "Google::Cloud::GkeBackup::V1::DeleteBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Name of the Backup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target Backup's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup#Google__Cloud__GkeBackup__V1__Backup_etag_instance_ "Google::Cloud::GkeBackup::V1::Backup#etag \(method\)") field or the request is rejected. 
  * **force** (::Boolean) — Optional. If set to true, any VolumeBackups below this Backup will also be deleted. Otherwise, the request will only succeed if the Backup has no VolumeBackups. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteBackupRequest.new
    
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

### #delete_backup_channel
    
    
    def delete_backup_channel(request, options = nil) -> ::Gapic::Operation
    def delete_backup_channel(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Deletes an existing BackupChannel.

**Overloads**
    
    
    def delete_backup_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_channel` via a request object, either of type [DeleteBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupChannelRequest "Google::Cloud::GkeBackup::V1::DeleteBackupChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_channel(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Fully qualified BackupChannel name. Format: `projects/*/locations/*/backupChannels/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target BackupChannel's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel#Google__Cloud__GkeBackup__V1__BackupChannel_etag_instance_ "Google::Cloud::GkeBackup::V1::BackupChannel#etag \(method\)") field or the request is rejected. 
  * **force** (::Boolean) — Optional. If set to true, any BackupPlanAssociations below this BackupChannel will also be deleted. Otherwise, the request will only succeed if the BackupChannel has no BackupPlanAssociations. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteBackupChannelRequest.new
    
    # Call the delete_backup_channel method.
    result = client.delete_backup_channel request
    
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
    def delete_backup_plan(name: nil, etag: nil) -> ::Gapic::Operation

Deletes an existing BackupPlan.

**Overloads**
    
    
    def delete_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan` via a request object, either of type [DeleteBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupPlanRequest "Google::Cloud::GkeBackup::V1::DeleteBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_plan(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Fully qualified BackupPlan name. Format: `projects/*/locations/*/backupPlans/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target BackupPlan's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan#Google__Cloud__GkeBackup__V1__BackupPlan_etag_instance_ "Google::Cloud::GkeBackup::V1::BackupPlan#etag \(method\)") field or the request is rejected. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteBackupPlanRequest.new
    
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

### #delete_restore
    
    
    def delete_restore(request, options = nil) -> ::Gapic::Operation
    def delete_restore(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Deletes an existing Restore.

**Overloads**
    
    
    def delete_restore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_restore` via a request object, either of type [DeleteRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestoreRequest "Google::Cloud::GkeBackup::V1::DeleteRestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_restore(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_restore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Full name of the Restore Format: `projects/*/locations/*/restorePlans/*/restores/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target Restore's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore#Google__Cloud__GkeBackup__V1__Restore_etag_instance_ "Google::Cloud::GkeBackup::V1::Restore#etag \(method\)") field or the request is rejected. 
  * **force** (::Boolean) — Optional. If set to true, any VolumeRestores below this restore will also be deleted. Otherwise, the request will only succeed if the restore has no VolumeRestores. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteRestoreRequest.new
    
    # Call the delete_restore method.
    result = client.delete_restore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_restore_channel
    
    
    def delete_restore_channel(request, options = nil) -> ::Gapic::Operation
    def delete_restore_channel(name: nil, etag: nil) -> ::Gapic::Operation

Deletes an existing RestoreChannel.

**Overloads**
    
    
    def delete_restore_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_restore_channel` via a request object, either of type [DeleteRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestoreChannelRequest "Google::Cloud::GkeBackup::V1::DeleteRestoreChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestoreChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_restore_channel(name: nil, etag: nil) -> ::Gapic::Operation

Pass arguments to `delete_restore_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Fully qualified RestoreChannel name. Format: `projects/*/locations/*/restoreChannels/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target RestoreChannel's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel#Google__Cloud__GkeBackup__V1__RestoreChannel_etag_instance_ "Google::Cloud::GkeBackup::V1::RestoreChannel#etag \(method\)") field or the request is rejected. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteRestoreChannelRequest.new
    
    # Call the delete_restore_channel method.
    result = client.delete_restore_channel request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #delete_restore_plan
    
    
    def delete_restore_plan(request, options = nil) -> ::Gapic::Operation
    def delete_restore_plan(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Deletes an existing RestorePlan.

**Overloads**
    
    
    def delete_restore_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `delete_restore_plan` via a request object, either of type [DeleteRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestorePlanRequest "Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-DeleteRestorePlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_restore_plan(name: nil, etag: nil, force: nil) -> ::Gapic::Operation

Pass arguments to `delete_restore_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **name** (::String) — Required. Fully qualified RestorePlan name. Format: `projects/*/locations/*/restorePlans/*`
  * **etag** (::String) — Optional. If provided, this value must match the current value of the target RestorePlan's [etag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan#Google__Cloud__GkeBackup__V1__RestorePlan_etag_instance_ "Google::Cloud::GkeBackup::V1::RestorePlan#etag \(method\)") field or the request is rejected. 
  * **force** (::Boolean) — Optional. If set to true, any Restores below this RestorePlan will also be deleted. Otherwise, the request will only succeed if the RestorePlan has no Restores. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::DeleteRestorePlanRequest.new
    
    # Call the delete_restore_plan method.
    result = client.delete_restore_plan request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #get_backup
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::Backup
    def get_backup(name: nil) -> ::Google::Cloud::GkeBackup::V1::Backup

Retrieve the details of a single Backup.

**Overloads**
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::Backup

Pass arguments to `get_backup` via a request object, either of type [GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupRequest "Google::Cloud::GkeBackup::V1::GetBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup(name: nil) -> ::Google::Cloud::GkeBackup::V1::Backup

Pass arguments to `get_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full name of the Backup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetBackupRequest.new
    
    # Call the get_backup method.
    result = client.get_backup request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::Backup.
    p result

### #get_backup_channel
    
    
    def get_backup_channel(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupChannel
    def get_backup_channel(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupChannel

Retrieve the details of a single BackupChannel.

**Overloads**
    
    
    def get_backup_channel(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupChannel

Pass arguments to `get_backup_channel` via a request object, either of type [GetBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupChannelRequest "Google::Cloud::GkeBackup::V1::GetBackupChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_channel(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupChannel

Pass arguments to `get_backup_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified BackupChannel name. Format: `projects/*/locations/*/backupChannels/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetBackupChannelRequest.new
    
    # Call the get_backup_channel method.
    result = client.get_backup_channel request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::BackupChannel.
    p result

### #get_backup_index_download_url
    
    
    def get_backup_index_download_url(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse
    def get_backup_index_download_url(backup: nil) -> ::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse

Retrieve the link to the backupIndex.

**Overloads**
    
    
    def get_backup_index_download_url(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse

Pass arguments to `get_backup_index_download_url` via a request object, either of type [GetBackupIndexDownloadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupIndexDownloadUrlRequest "Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupIndexDownloadUrlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_index_download_url(backup: nil) -> ::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse

Pass arguments to `get_backup_index_download_url` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **backup** (::String) — Required. Full name of Backup resource. Format: projects/{project}/locations/{location}/backupPlans/{backup_plan}/backups/{backup} 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupIndexDownloadUrlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupIndexDownloadUrlResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlRequest.new
    
    # Call the get_backup_index_download_url method.
    result = client.get_backup_index_download_url request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::GetBackupIndexDownloadUrlResponse.
    p result

### #get_backup_plan
    
    
    def get_backup_plan(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlan
    def get_backup_plan(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlan

Retrieve the details of a single BackupPlan.

**Overloads**
    
    
    def get_backup_plan(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlan

Pass arguments to `get_backup_plan` via a request object, either of type [GetBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupPlanRequest "Google::Cloud::GkeBackup::V1::GetBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_plan(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlan

Pass arguments to `get_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified BackupPlan name. Format: `projects/*/locations/*/backupPlans/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetBackupPlanRequest.new
    
    # Call the get_backup_plan method.
    result = client.get_backup_plan request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::BackupPlan.
    p result

### #get_backup_plan_binding
    
    
    def get_backup_plan_binding(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlanBinding
    def get_backup_plan_binding(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlanBinding

Retrieve the details of a single BackupPlanBinding.

**Overloads**
    
    
    def get_backup_plan_binding(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlanBinding

Pass arguments to `get_backup_plan_binding` via a request object, either of type [GetBackupPlanBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupPlanBindingRequest "Google::Cloud::GkeBackup::V1::GetBackupPlanBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetBackupPlanBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetBackupPlanBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_plan_binding(name: nil) -> ::Google::Cloud::GkeBackup::V1::BackupPlanBinding

Pass arguments to `get_backup_plan_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified BackupPlanBinding name. Format: `projects/*/locations/*/backupChannels/*/backupPlanBindings/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::BackupPlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlanBinding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupPlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlanBinding)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetBackupPlanBindingRequest.new
    
    # Call the get_backup_plan_binding method.
    result = client.get_backup_plan_binding request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::BackupPlanBinding.
    p result

### #get_restore
    
    
    def get_restore(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::Restore
    def get_restore(name: nil) -> ::Google::Cloud::GkeBackup::V1::Restore

Retrieves the details of a single Restore.

**Overloads**
    
    
    def get_restore(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::Restore

Pass arguments to `get_restore` via a request object, either of type [GetRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestoreRequest "Google::Cloud::GkeBackup::V1::GetRestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_restore(name: nil) -> ::Google::Cloud::GkeBackup::V1::Restore

Pass arguments to `get_restore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the restore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetRestoreRequest.new
    
    # Call the get_restore method.
    result = client.get_restore request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::Restore.
    p result

### #get_restore_channel
    
    
    def get_restore_channel(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestoreChannel
    def get_restore_channel(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestoreChannel

Retrieve the details of a single RestoreChannel.

**Overloads**
    
    
    def get_restore_channel(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestoreChannel

Pass arguments to `get_restore_channel` via a request object, either of type [GetRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestoreChannelRequest "Google::Cloud::GkeBackup::V1::GetRestoreChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestoreChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_restore_channel(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestoreChannel

Pass arguments to `get_restore_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified RestoreChannel name. Format: `projects/*/locations/*/restoreChannels/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetRestoreChannelRequest.new
    
    # Call the get_restore_channel method.
    result = client.get_restore_channel request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::RestoreChannel.
    p result

### #get_restore_plan
    
    
    def get_restore_plan(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlan
    def get_restore_plan(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlan

Retrieve the details of a single RestorePlan.

**Overloads**
    
    
    def get_restore_plan(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlan

Pass arguments to `get_restore_plan` via a request object, either of type [GetRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestorePlanRequest "Google::Cloud::GkeBackup::V1::GetRestorePlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestorePlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_restore_plan(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlan

Pass arguments to `get_restore_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified RestorePlan name. Format: `projects/*/locations/*/restorePlans/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetRestorePlanRequest.new
    
    # Call the get_restore_plan method.
    result = client.get_restore_plan request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::RestorePlan.
    p result

### #get_restore_plan_binding
    
    
    def get_restore_plan_binding(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlanBinding
    def get_restore_plan_binding(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlanBinding

Retrieve the details of a single RestorePlanBinding.

**Overloads**
    
    
    def get_restore_plan_binding(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlanBinding

Pass arguments to `get_restore_plan_binding` via a request object, either of type [GetRestorePlanBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestorePlanBindingRequest "Google::Cloud::GkeBackup::V1::GetRestorePlanBindingRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetRestorePlanBindingRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetRestorePlanBindingRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_restore_plan_binding(name: nil) -> ::Google::Cloud::GkeBackup::V1::RestorePlanBinding

Pass arguments to `get_restore_plan_binding` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Fully qualified RestorePlanBinding name. Format: `projects/*/locations/*/restoreChannels/*/restorePlanBindings/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::RestorePlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlanBinding)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::RestorePlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlanBinding)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetRestorePlanBindingRequest.new
    
    # Call the get_restore_plan_binding method.
    result = client.get_restore_plan_binding request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::RestorePlanBinding.
    p result

### #get_volume_backup
    
    
    def get_volume_backup(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::VolumeBackup
    def get_volume_backup(name: nil) -> ::Google::Cloud::GkeBackup::V1::VolumeBackup

Retrieve the details of a single VolumeBackup.

**Overloads**
    
    
    def get_volume_backup(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::VolumeBackup

Pass arguments to `get_volume_backup` via a request object, either of type [GetVolumeBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetVolumeBackupRequest "Google::Cloud::GkeBackup::V1::GetVolumeBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetVolumeBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetVolumeBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_volume_backup(name: nil) -> ::Google::Cloud::GkeBackup::V1::VolumeBackup

Pass arguments to `get_volume_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full name of the VolumeBackup resource. Format: `projects/*/locations/*/backupPlans/*/backups/*/volumeBackups/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetVolumeBackupRequest.new
    
    # Call the get_volume_backup method.
    result = client.get_volume_backup request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::VolumeBackup.
    p result

### #get_volume_restore
    
    
    def get_volume_restore(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::VolumeRestore
    def get_volume_restore(name: nil) -> ::Google::Cloud::GkeBackup::V1::VolumeRestore

Retrieve the details of a single VolumeRestore.

**Overloads**
    
    
    def get_volume_restore(request, options = nil) -> ::Google::Cloud::GkeBackup::V1::VolumeRestore

Pass arguments to `get_volume_restore` via a request object, either of type [GetVolumeRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetVolumeRestoreRequest "Google::Cloud::GkeBackup::V1::GetVolumeRestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::GetVolumeRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-GetVolumeRestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_volume_restore(name: nil) -> ::Google::Cloud::GkeBackup::V1::VolumeRestore

Pass arguments to `get_volume_restore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Full name of the VolumeRestore resource. Format: `projects/*/locations/*/restorePlans/*/restores/*/volumeRestores/*`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::GkeBackup::V1::VolumeRestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeRestore)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::GkeBackup::V1::VolumeRestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeRestore)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::GetVolumeRestoreRequest.new
    
    # Call the get_volume_restore method.
    result = client.get_volume_restore request
    
    # The returned object is of type Google::Cloud::GkeBackup::V1::VolumeRestore.
    p result

### #iam_policy_client
    
    
    def iam_policy_client() -> Google::Iam::V1::IAMPolicy::Rest::Client

Get the associated client for mix-in of the IAMPolicy.

**Returns**

  * (Google::Iam::V1::IAMPolicy::Rest::Client) 



### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new BackupForGKE REST client object.

**Yields**

  * (config) — Configure the BackupForGKE client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_backup_channels
    
    
    def list_backup_channels(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupChannel>
    def list_backup_channels(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupChannel>

Lists BackupChannels in a given location.

**Overloads**
    
    
    def list_backup_channels(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupChannel>

Pass arguments to `list_backup_channels` via a request object, either of type [ListBackupChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupChannelsRequest "Google::Cloud::GkeBackup::V1::ListBackupChannelsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListBackupChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupChannelsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_channels(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupChannel>

Pass arguments to `list_backup_channels` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location that contains the BackupChannels to list. Format: `projects/*/locations/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupChannelsResponse#Google__Cloud__GkeBackup__V1__ListBackupChannelsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupChannelsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupChannelsResponse#Google__Cloud__GkeBackup__V1__ListBackupChannelsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupChannelsResponse#next_page_token \(method\)") received from a previous `ListBackupChannels` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupChannels` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListBackupChannelsRequest.new
    
    # Call the list_backup_channels method.
    result = client.list_backup_channels request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::BackupChannel.
      p item
    end

### #list_backup_plan_bindings
    
    
    def list_backup_plan_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlanBinding>
    def list_backup_plan_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlanBinding>

Lists BackupPlanBindings in a given location.

**Overloads**
    
    
    def list_backup_plan_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlanBinding>

Pass arguments to `list_backup_plan_bindings` via a request object, either of type [ListBackupPlanBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlanBindingsRequest "Google::Cloud::GkeBackup::V1::ListBackupPlanBindingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListBackupPlanBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlanBindingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_plan_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlanBinding>

Pass arguments to `list_backup_plan_bindings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The BackupChannel that contains the BackupPlanBindings to list. Format: `projects/*/locations/*/backupChannels/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlanBindingsResponse#Google__Cloud__GkeBackup__V1__ListBackupPlanBindingsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupPlanBindingsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlanBindingsResponse#Google__Cloud__GkeBackup__V1__ListBackupPlanBindingsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupPlanBindingsResponse#next_page_token \(method\)") received from a previous `ListBackupPlanBindings` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlanBindings` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupPlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlanBinding)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupPlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlanBinding)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListBackupPlanBindingsRequest.new
    
    # Call the list_backup_plan_bindings method.
    result = client.list_backup_plan_bindings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::BackupPlanBinding.
      p item
    end

### #list_backup_plans
    
    
    def list_backup_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlan>
    def list_backup_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlan>

Lists BackupPlans in a given location.

**Overloads**
    
    
    def list_backup_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlan>

Pass arguments to `list_backup_plans` via a request object, either of type [ListBackupPlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlansRequest "Google::Cloud::GkeBackup::V1::ListBackupPlansRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListBackupPlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlansRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::BackupPlan>

Pass arguments to `list_backup_plans` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location that contains the BackupPlans to list. Format: `projects/*/locations/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlansResponse#Google__Cloud__GkeBackup__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupPlansResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupPlansResponse#Google__Cloud__GkeBackup__V1__ListBackupPlansResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupPlansResponse#next_page_token \(method\)") received from a previous `ListBackupPlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackupPlans` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListBackupPlansRequest.new
    
    # Call the list_backup_plans method.
    result = client.list_backup_plans request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::BackupPlan.
      p item
    end

### #list_backups
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Backup>
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, return_partial_success: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Backup>

Lists the Backups for a given BackupPlan.

**Overloads**
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Backup>

Pass arguments to `list_backups` via a request object, either of type [ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupsRequest "Google::Cloud::GkeBackup::V1::ListBackupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil, return_partial_success: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Backup>

Pass arguments to `list_backups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The BackupPlan that contains the Backups to list. Format: `projects/*/locations/*/backupPlans/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupsResponse#Google__Cloud__GkeBackup__V1__ListBackupsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListBackupsResponse#Google__Cloud__GkeBackup__V1__ListBackupsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListBackupsResponse#next_page_token \(method\)") received from a previous `ListBackups` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListBackups` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 
  * **return_partial_success** (::Boolean) — Optional. If set to true, the response will return partial results when some regions are unreachable and the unreachable field will be populated. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListBackupsRequest.new
    
    # Call the list_backups method.
    result = client.list_backups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::Backup.
      p item
    end

### #list_restore_channels
    
    
    def list_restore_channels(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestoreChannel>
    def list_restore_channels(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestoreChannel>

Lists RestoreChannels in a given location.

**Overloads**
    
    
    def list_restore_channels(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestoreChannel>

Pass arguments to `list_restore_channels` via a request object, either of type [ListRestoreChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoreChannelsRequest "Google::Cloud::GkeBackup::V1::ListRestoreChannelsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListRestoreChannelsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoreChannelsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_restore_channels(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestoreChannel>

Pass arguments to `list_restore_channels` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location that contains the RestoreChannels to list. Format: `projects/*/locations/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoreChannelsResponse#Google__Cloud__GkeBackup__V1__ListRestoreChannelsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestoreChannelsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoreChannelsResponse#Google__Cloud__GkeBackup__V1__ListRestoreChannelsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestoreChannelsResponse#next_page_token \(method\)") received from a previous `ListRestoreChannels` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListRestoreChannels` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListRestoreChannelsRequest.new
    
    # Call the list_restore_channels method.
    result = client.list_restore_channels request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::RestoreChannel.
      p item
    end

### #list_restore_plan_bindings
    
    
    def list_restore_plan_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlanBinding>
    def list_restore_plan_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlanBinding>

Lists RestorePlanBindings in a given location.

**Overloads**
    
    
    def list_restore_plan_bindings(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlanBinding>

Pass arguments to `list_restore_plan_bindings` via a request object, either of type [ListRestorePlanBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlanBindingsRequest "Google::Cloud::GkeBackup::V1::ListRestorePlanBindingsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListRestorePlanBindingsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlanBindingsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_restore_plan_bindings(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlanBinding>

Pass arguments to `list_restore_plan_bindings` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The RestoreChannel that contains the ListRestorePlanBindings to list. Format: `projects/*/locations/*/restoreChannels/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlanBindingsResponse#Google__Cloud__GkeBackup__V1__ListRestorePlanBindingsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestorePlanBindingsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlanBindingsResponse#Google__Cloud__GkeBackup__V1__ListRestorePlanBindingsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestorePlanBindingsResponse#next_page_token \(method\)") received from a previous `ListRestorePlanBindings` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListRestorePlanBindings` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestorePlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlanBinding)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestorePlanBinding](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlanBinding)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListRestorePlanBindingsRequest.new
    
    # Call the list_restore_plan_bindings method.
    result = client.list_restore_plan_bindings request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::RestorePlanBinding.
      p item
    end

### #list_restore_plans
    
    
    def list_restore_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlan>
    def list_restore_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlan>

Lists RestorePlans in a given location.

**Overloads**
    
    
    def list_restore_plans(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlan>

Pass arguments to `list_restore_plans` via a request object, either of type [ListRestorePlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlansRequest "Google::Cloud::GkeBackup::V1::ListRestorePlansRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListRestorePlansRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlansRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_restore_plans(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::RestorePlan>

Pass arguments to `list_restore_plans` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The location that contains the RestorePlans to list. Format: `projects/*/locations/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlansResponse#Google__Cloud__GkeBackup__V1__ListRestorePlansResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestorePlansResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestorePlansResponse#Google__Cloud__GkeBackup__V1__ListRestorePlansResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestorePlansResponse#next_page_token \(method\)") received from a previous `ListRestorePlans` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListRestorePlans` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListRestorePlansRequest.new
    
    # Call the list_restore_plans method.
    result = client.list_restore_plans request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::RestorePlan.
      p item
    end

### #list_restores
    
    
    def list_restores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Restore>
    def list_restores(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Restore>

Lists the Restores for a given RestorePlan.

**Overloads**
    
    
    def list_restores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Restore>

Pass arguments to `list_restores` via a request object, either of type [ListRestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoresRequest "Google::Cloud::GkeBackup::V1::ListRestoresRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListRestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoresRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_restores(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::Restore>

Pass arguments to `list_restores` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The RestorePlan that contains the Restores to list. Format: `projects/*/locations/*/restorePlans/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoresResponse#Google__Cloud__GkeBackup__V1__ListRestoresResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestoresResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListRestoresResponse#Google__Cloud__GkeBackup__V1__ListRestoresResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListRestoresResponse#next_page_token \(method\)") received from a previous `ListRestores` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListRestores` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListRestoresRequest.new
    
    # Call the list_restores method.
    result = client.list_restores request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::Restore.
      p item
    end

### #list_volume_backups
    
    
    def list_volume_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeBackup>
    def list_volume_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeBackup>

Lists the VolumeBackups for a given Backup.

**Overloads**
    
    
    def list_volume_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeBackup>

Pass arguments to `list_volume_backups` via a request object, either of type [ListVolumeBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsRequest "Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_volume_backups(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeBackup>

Pass arguments to `list_volume_backups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The Backup that contains the VolumeBackups to list. Format: `projects/*/locations/*/backupPlans/*/backups/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsResponse#Google__Cloud__GkeBackup__V1__ListVolumeBackupsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeBackupsResponse#Google__Cloud__GkeBackup__V1__ListVolumeBackupsResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeBackupsResponse#next_page_token \(method\)") received from a previous `ListVolumeBackups` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListVolumeBackups` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::VolumeBackup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeBackup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListVolumeBackupsRequest.new
    
    # Call the list_volume_backups method.
    result = client.list_volume_backups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::VolumeBackup.
      p item
    end

### #list_volume_restores
    
    
    def list_volume_restores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeRestore>
    def list_volume_restores(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeRestore>

Lists the VolumeRestores for a given Restore.

**Overloads**
    
    
    def list_volume_restores(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeRestore>

Pass arguments to `list_volume_restores` via a request object, either of type [ListVolumeRestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeRestoresRequest "Google::Cloud::GkeBackup::V1::ListVolumeRestoresRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::ListVolumeRestoresRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeRestoresRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_volume_restores(parent: nil, page_size: nil, page_token: nil, filter: nil, order_by: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::GkeBackup::V1::VolumeRestore>

Pass arguments to `list_volume_restores` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The Restore that contains the VolumeRestores to list. Format: `projects/*/locations/*/restorePlans/*/restores/*`
  * **page_size** (::Integer) — Optional. The target number of results to return in a single response. If not specified, a default value will be chosen by the service. Note that the response may include a partial list and a caller should only rely on the response's [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeRestoresResponse#Google__Cloud__GkeBackup__V1__ListVolumeRestoresResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeRestoresResponse#next_page_token \(method\)") to determine if there are more instances left to be queried. 
  * **page_token** (::String) — Optional. The value of [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-ListVolumeRestoresResponse#Google__Cloud__GkeBackup__V1__ListVolumeRestoresResponse_next_page_token_instance_ "Google::Cloud::GkeBackup::V1::ListVolumeRestoresResponse#next_page_token \(method\)") received from a previous `ListVolumeRestores` call. Provide this to retrieve the subsequent page in a multi-page list of results. When paginating, all other parameters provided to `ListVolumeRestores` must match the call that provided the page token. 
  * **filter** (::String) — Optional. Field match expression used to filter the results. 
  * **order_by** (::String) — Optional. Field by which to sort the results. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::VolumeRestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeRestore)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::GkeBackup::V1::VolumeRestore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-VolumeRestore)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::ListVolumeRestoresRequest.new
    
    # Call the list_volume_restores method.
    result = client.list_volume_restores request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::GkeBackup::V1::VolumeRestore.
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
    
    
    def operations_client() -> ::Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupForGKE-Rest-Operations)) 



### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_backup
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation
    def update_backup(backup: nil, update_mask: nil) -> ::Gapic::Operation

Update a Backup.

**Overloads**
    
    
    def update_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via a request object, either of type [UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupRequest "Google::Cloud::GkeBackup::V1::UpdateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup(backup: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup** ([::Google::Cloud::GkeBackup::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Backup), ::Hash) — Required. A new version of the Backup resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the Backup targeted for update. The values for each of these updated fields will be taken from the `backup_plan` provided with this request. Field names are relative to the root of the resource. If no `update_mask` is provided, all fields in `backup` will be written to the target Backup resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `backup` are ignored and are not used to update the target Backup. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateBackupRequest.new
    
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

### #update_backup_channel
    
    
    def update_backup_channel(request, options = nil) -> ::Gapic::Operation
    def update_backup_channel(backup_channel: nil, update_mask: nil) -> ::Gapic::Operation

Update a BackupChannel.

**Overloads**
    
    
    def update_backup_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup_channel` via a request object, either of type [UpdateBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupChannelRequest "Google::Cloud::GkeBackup::V1::UpdateBackupChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateBackupChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_channel(backup_channel: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_backup_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_channel** ([::Google::Cloud::GkeBackup::V1::BackupChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupChannel), ::Hash) — Required. A new version of the BackupChannel resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the BackupChannel targeted for update. The values for each of these updated fields will be taken from the `backup_channel` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `labels`, etc.) If no `update_mask` is provided, all fields in `backup_channel` will be written to the target BackupChannel resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `backup_channel` are ignored and are not used to update the target BackupChannel. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateBackupChannelRequest.new
    
    # Call the update_backup_channel method.
    result = client.update_backup_channel request
    
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
    def update_backup_plan(backup_plan: nil, update_mask: nil) -> ::Gapic::Operation

Update a BackupPlan.

**Overloads**
    
    
    def update_backup_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan` via a request object, either of type [UpdateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupPlanRequest "Google::Cloud::GkeBackup::V1::UpdateBackupPlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateBackupPlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateBackupPlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_plan(backup_plan: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_backup_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_plan** ([::Google::Cloud::GkeBackup::V1::BackupPlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-BackupPlan), ::Hash) — Required. A new version of the BackupPlan resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the BackupPlan targeted for update. The values for each of these updated fields will be taken from the `backup_plan` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `backup_config.include_volume_data`, etc.) If no `update_mask` is provided, all fields in `backup_plan` will be written to the target BackupPlan resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `backup_plan` are ignored and are not used to update the target BackupPlan. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateBackupPlanRequest.new
    
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

### #update_restore
    
    
    def update_restore(request, options = nil) -> ::Gapic::Operation
    def update_restore(restore: nil, update_mask: nil) -> ::Gapic::Operation

Update a Restore.

**Overloads**
    
    
    def update_restore(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_restore` via a request object, either of type [UpdateRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreRequest "Google::Cloud::GkeBackup::V1::UpdateRestoreRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateRestoreRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_restore(restore: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_restore` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **restore** ([::Google::Cloud::GkeBackup::V1::Restore](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-Restore), ::Hash) — Required. A new version of the Restore resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the Restore targeted for update. The values for each of these updated fields will be taken from the `restore` provided with this request. Field names are relative to the root of the resource. If no `update_mask` is provided, all fields in `restore` will be written to the target Restore resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore` are ignored and are not used to update the target Restore. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateRestoreRequest.new
    
    # Call the update_restore method.
    result = client.update_restore request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_restore_channel
    
    
    def update_restore_channel(request, options = nil) -> ::Gapic::Operation
    def update_restore_channel(restore_channel: nil, update_mask: nil) -> ::Gapic::Operation

Update a RestoreChannel.

**Overloads**
    
    
    def update_restore_channel(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_restore_channel` via a request object, either of type [UpdateRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreChannelRequest "Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestoreChannelRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_restore_channel(restore_channel: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_restore_channel` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **restore_channel** ([::Google::Cloud::GkeBackup::V1::RestoreChannel](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestoreChannel), ::Hash) — Required. A new version of the RestoreChannel resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the RestoreChannel targeted for update. The values for each of these updated fields will be taken from the `restore_channel` provided with this request. Field names are relative to the root of the resource (e.g., `description`, `destination_project_id`, etc.) If no `update_mask` is provided, all fields in `restore_channel` will be written to the target RestoreChannel resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore_channel` are ignored and are not used to update the target RestoreChannel. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateRestoreChannelRequest.new
    
    # Call the update_restore_channel method.
    result = client.update_restore_channel request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_restore_plan
    
    
    def update_restore_plan(request, options = nil) -> ::Gapic::Operation
    def update_restore_plan(restore_plan: nil, update_mask: nil) -> ::Gapic::Operation

Update a RestorePlan.

**Overloads**
    
    
    def update_restore_plan(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_restore_plan` via a request object, either of type [UpdateRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestorePlanRequest "Google::Cloud::GkeBackup::V1::UpdateRestorePlanRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::GkeBackup::V1::UpdateRestorePlanRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-UpdateRestorePlanRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_restore_plan(restore_plan: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_restore_plan` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **restore_plan** ([::Google::Cloud::GkeBackup::V1::RestorePlan](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Cloud-GkeBackup-V1-RestorePlan), ::Hash) — Required. A new version of the RestorePlan resource that contains updated fields. This may be sparsely populated if an `update_mask` is provided. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gke_backup-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Optional. This is used to specify the fields to be overwritten in the RestorePlan targeted for update. The values for each of these updated fields will be taken from the `restore_plan` provided with this request. Field names are relative to the root of the resource. If no `update_mask` is provided, all fields in `restore_plan` will be written to the target RestorePlan resource. Note that OUTPUT_ONLY and IMMUTABLE fields in `restore_plan` are ignored and are not used to update the target RestorePlan. 



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
    
    
    require "google/cloud/gke_backup/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::GkeBackup::V1::BackupForGKE::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::GkeBackup::V1::UpdateRestorePlanRequest.new
    
    # Call the update_restore_plan method.
    result = client.update_restore_plan request
    
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

Last updated 2026-06-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-12 UTC."],[],[]] 
