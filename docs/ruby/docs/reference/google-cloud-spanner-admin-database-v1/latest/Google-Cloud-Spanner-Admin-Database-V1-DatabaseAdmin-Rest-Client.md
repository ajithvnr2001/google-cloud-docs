---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client/
title: Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:39.917167+00:00
---

# Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner Database Admin V1 API - Class Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.1  1.1.1  1.0.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.1  0.15.0  0.14.2  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.0  0.7.6 

Reference documentation and code samples for the Cloud Spanner Database Admin V1 API class Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.

REST client for the DatabaseAdmin service.

Cloud Spanner Database Admin API

The Cloud Spanner Database Admin API can be used to:

  * create, drop, and list databases
  * update the schema of pre-existing databases
  * create, delete, copy and list backups for a database
  * restore a database from an existing backup



## Inherits

  * Object 



## Includes

  * [Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Paths)



## Methods 

### .configure
    
    
    def self.configure() { |config| ... } -> Client::Configuration

Configure the DatabaseAdmin Client class.

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration)) 



**Example**
    
    
    # Modify the configuration for all DatabaseAdmin clients
    ::Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.configure do |config|
      config.timeout = 10.0
    end

### #add_split_points
    
    
    def add_split_points(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse
    def add_split_points(database: nil, split_points: nil, initiator: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse

Adds split points to specified tables, indexes of a database.

**Overloads**
    
    
    def add_split_points(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse

Pass arguments to `add_split_points` via a request object, either of type [AddSplitPointsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-AddSplitPointsRequest "Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-AddSplitPointsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def add_split_points(database: nil, split_points: nil, initiator: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse

Pass arguments to `add_split_points` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **database** (::String) — Required. The database on whose tables/indexes split points are to be added. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. 
  * **split_points** (::Array<[::Google::Cloud::Spanner::Admin::Database::V1::SplitPoints](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-SplitPoints), ::Hash>) — Required. The split points to add. 
  * **initiator** (::String) — Optional. A user-supplied tag associated with the split points. For example, "intital_data_load", "special_event_1". Defaults to "CloudAddSplitPointsAPI" if not specified. The length of the tag must not exceed 50 characters,else will be trimmed. Only valid UTF8 characters are allowed. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-AddSplitPointsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-AddSplitPointsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsRequest.new
    
    # Call the add_split_points method.
    result = client.add_split_points request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::AddSplitPointsResponse.
    p result

### #configure
    
    
    def configure() { |config| ... } -> Client::Configuration

Configure the DatabaseAdmin Client instance.

The configuration is set to the derived mode, meaning that values can be changed, but structural changes (adding new fields, etc.) are not allowed. Structural changes should be made on [Client.configure](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client#Google__Cloud__Spanner__Admin__Database__V1__DatabaseAdmin__Rest__Client_configure_class_ "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.configure \(method\)").

See [Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client::Configuration \(class\)") for a description of the configuration fields.

**Yields**

  * (config) — Configure the Client client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration)) 



### #copy_backup
    
    
    def copy_backup(request, options = nil) -> ::Gapic::Operation
    def copy_backup(parent: nil, backup_id: nil, source_backup: nil, expire_time: nil, encryption_config: nil) -> ::Gapic::Operation

Starts copying a Cloud Spanner Backup. The returned backup [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track copying of the backup. The operation is associated with the destination backup. The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [CopyBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CopyBackupMetadata \(class\)"). The [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") field type is [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)"), if successful. Cancelling the returned operation will stop the copying and delete the destination backup. Concurrent CopyBackup requests can run on the same source backup.

**Overloads**
    
    
    def copy_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `copy_backup` via a request object, either of type [CopyBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupRequest "Google::Cloud::Spanner::Admin::Database::V1::CopyBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::CopyBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def copy_backup(parent: nil, backup_id: nil, source_backup: nil, expire_time: nil, encryption_config: nil) -> ::Gapic::Operation

Pass arguments to `copy_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the destination instance that will contain the backup copy. Values are of the form: `projects/<project>/instances/<instance>`. 
  * **backup_id** (::String) — Required. The id of the backup copy. The `backup_id` appended to `parent` forms the full backup_uri of the form `projects/<project>/instances/<instance>/backups/<backup>`. 
  * **source_backup** (::String) — Required. The source backup to be copied. The source backup needs to be in READY state for it to be copied. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/backups/<backup>`. 
  * **expire_time** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Timestamp), ::Hash) — Required. The expiration time of the backup in microsecond granularity. The expiration time must be at least 6 hours and at most 366 days from the `create_time` of the source backup. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup. 
  * **encryption_config** ([::Google::Cloud::Spanner::Admin::Database::V1::CopyBackupEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupEncryptionConfig), ::Hash) — Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the source backup by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CopyBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CopyBackupEncryptionConfig#encryption_type \(method\)") = `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::CopyBackupRequest.new
    
    # Call the copy_backup method.
    result = client.copy_backup request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #create_backup
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation
    def create_backup(parent: nil, backup_id: nil, backup: nil, encryption_config: nil) -> ::Gapic::Operation

Starts creating a new Cloud Spanner Backup. The returned backup [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track creation of the backup. The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [CreateBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupMetadata \(class\)"). The [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") field type is [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)"), if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.

**Overloads**
    
    
    def create_backup(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via a request object, either of type [CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupRequest "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup(parent: nil, backup_id: nil, backup: nil, encryption_config: nil) -> ::Gapic::Operation

Pass arguments to `create_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the instance in which the backup will be created. This must be the same instance that contains the database the backup will be created from. The backup will be stored in the location(s) specified in the instance configuration of this instance. Values are of the form `projects/<project>/instances/<instance>`. 
  * **backup_id** (::String) — Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/<project>/instances/<instance>/backups/<backup_id>`. 
  * **backup** ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup), ::Hash) — Required. The backup to create. 
  * **encryption_config** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig), ::Hash) — Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the database by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__CreateBackupEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupEncryptionConfig#encryption_type \(method\)") = `USE_DATABASE_ENCRYPTION`. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::CreateBackupRequest.new
    
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

### #create_backup_schedule
    
    
    def create_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule
    def create_backup_schedule(parent: nil, backup_schedule_id: nil, backup_schedule: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Creates a new backup schedule.

**Overloads**
    
    
    def create_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `create_backup_schedule` via a request object, either of type [CreateBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupScheduleRequest "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_backup_schedule(parent: nil, backup_schedule_id: nil, backup_schedule: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `create_backup_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the database that this backup schedule applies to. 
  * **backup_schedule_id** (::String) — Required. The Id to use for the backup schedule. The `backup_schedule_id` appended to `parent` forms the full backup schedule name of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`. 
  * **backup_schedule** ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule), ::Hash) — Required. The backup schedule to create. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::CreateBackupScheduleRequest.new
    
    # Call the create_backup_schedule method.
    result = client.create_backup_schedule request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule.
    p result

### #create_database
    
    
    def create_database(request, options = nil) -> ::Gapic::Operation
    def create_database(parent: nil, create_statement: nil, extra_statements: nil, encryption_config: nil, database_dialect: nil, proto_descriptors: nil) -> ::Gapic::Operation

Creates a new Cloud Spanner database and starts to prepare it for serving. The returned [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track preparation of the database. The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [CreateDatabaseMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateDatabaseMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateDatabaseMetadata \(class\)"). The [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") field type is [Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database "Google::Cloud::Spanner::Admin::Database::V1::Database \(class\)"), if successful.

**Overloads**
    
    
    def create_database(request, options = nil) -> ::Gapic::Operation

Pass arguments to `create_database` via a request object, either of type [CreateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateDatabaseRequest "Google::Cloud::Spanner::Admin::Database::V1::CreateDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::CreateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def create_database(parent: nil, create_statement: nil, extra_statements: nil, encryption_config: nil, database_dialect: nil, proto_descriptors: nil) -> ::Gapic::Operation

Pass arguments to `create_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the instance that will serve the new database. Values are of the form `projects/<project>/instances/<instance>`. 
  * **create_statement** (::String) — Required. A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `[a-z][a-z0-9_\-]*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (```). 
  * **extra_statements** (::Array<::String>) — Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created. 
  * **encryption_config** ([::Google::Cloud::Spanner::Admin::Database::V1::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-EncryptionConfig), ::Hash) — Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption. 
  * **database_dialect** ([::Google::Cloud::Spanner::Admin::Database::V1::DatabaseDialect](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseDialect)) — Optional. The dialect of the Cloud Spanner Database. 
  * **proto_descriptors** (::String) — Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements in 'extra_statements' above. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run ` $protoc --proto_path=/app_path --proto_path=/lib_path \ --include_imports \ --descriptor_set_out=descriptors.data \ moon/shot/app.proto ` For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::CreateDatabaseRequest.new
    
    # Call the create_database method.
    result = client.create_database request
    
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
    
    
    def delete_backup(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_backup(name: nil) -> ::Google::Protobuf::Empty

Deletes a pending or completed [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)").

**Overloads**
    
    
    def delete_backup(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_backup` via a request object, either of type [Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DeleteBackupRequest "Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DeleteBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the backup to delete. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupRequest.new
    
    # Call the delete_backup method.
    result = client.delete_backup request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #delete_backup_schedule
    
    
    def delete_backup_schedule(request, options = nil) -> ::Google::Protobuf::Empty
    def delete_backup_schedule(name: nil) -> ::Google::Protobuf::Empty

Deletes a backup schedule.

**Overloads**
    
    
    def delete_backup_schedule(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_backup_schedule` via a request object, either of type [Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DeleteBackupScheduleRequest "Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DeleteBackupScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def delete_backup_schedule(name: nil) -> ::Google::Protobuf::Empty

Pass arguments to `delete_backup_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the schedule to delete. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::DeleteBackupScheduleRequest.new
    
    # Call the delete_backup_schedule method.
    result = client.delete_backup_schedule request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #drop_database
    
    
    def drop_database(request, options = nil) -> ::Google::Protobuf::Empty
    def drop_database(database: nil) -> ::Google::Protobuf::Empty

Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their `expire_time`. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted.

**Overloads**
    
    
    def drop_database(request, options = nil) -> ::Google::Protobuf::Empty

Pass arguments to `drop_database` via a request object, either of type [Google::Cloud::Spanner::Admin::Database::V1::DropDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DropDatabaseRequest "Google::Cloud::Spanner::Admin::Database::V1::DropDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::DropDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DropDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def drop_database(database: nil) -> ::Google::Protobuf::Empty

Pass arguments to `drop_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **database** (::String) — Required. The database to be dropped. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Protobuf::Empty](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-Empty)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::DropDatabaseRequest.new
    
    # Call the drop_database method.
    result = client.drop_database request
    
    # The returned object is of type Google::Protobuf::Empty.
    p result

### #get_backup
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup
    def get_backup(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Gets metadata on a pending or completed [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)").

**Overloads**
    
    
    def get_backup(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Pass arguments to `get_backup` via a request object, either of type [GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetBackupRequest "Google::Cloud::Spanner::Admin::Database::V1::GetBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::GetBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Pass arguments to `get_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. Name of the backup. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::GetBackupRequest.new
    
    # Call the get_backup method.
    result = client.get_backup request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::Backup.
    p result

### #get_backup_schedule
    
    
    def get_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule
    def get_backup_schedule(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Gets backup schedule for the input schedule name.

**Overloads**
    
    
    def get_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `get_backup_schedule` via a request object, either of type [GetBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetBackupScheduleRequest "Google::Cloud::Spanner::Admin::Database::V1::GetBackupScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::GetBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetBackupScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_backup_schedule(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `get_backup_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the schedule to retrieve. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::GetBackupScheduleRequest.new
    
    # Call the get_backup_schedule method.
    result = client.get_backup_schedule request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule.
    p result

### #get_database
    
    
    def get_database(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Database
    def get_database(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Database

Gets the state of a Cloud Spanner database.

**Overloads**
    
    
    def get_database(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Database

Pass arguments to `get_database` via a request object, either of type [GetDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseRequest "Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_database(name: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Database

Pass arguments to `get_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **name** (::String) — Required. The name of the requested database. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseRequest.new
    
    # Call the get_database method.
    result = client.get_database request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::Database.
    p result

### #get_database_ddl
    
    
    def get_database_ddl(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse
    def get_database_ddl(database: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse

Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the Operations API.

**Overloads**
    
    
    def get_database_ddl(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse

Pass arguments to `get_database_ddl` via a request object, either of type [GetDatabaseDdlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseDdlRequest "Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseDdlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_database_ddl(database: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse

Pass arguments to `get_database_ddl` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameter**

  * **database** (::String) — Required. The database whose schema we wish to get. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseDdlResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-GetDatabaseDdlResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlRequest.new
    
    # Call the get_database_ddl method.
    result = client.get_database_ddl request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::GetDatabaseDdlResponse.
    p result

### #get_iam_policy
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Gets the access control policy for a database or backup resource. Returns an empty policy if a database or backup exists but does not have a policy set.

Authorization requires `spanner.databases.getIamPolicy` permission on [resource][google.iam.v1.GetIamPolicyRequest.resource]. For backups, authorization requires `spanner.backups.getIamPolicy` permission on [resource][google.iam.v1.GetIamPolicyRequest.resource].

**Overloads**
    
    
    def get_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via a request object, either of type [Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-GetIamPolicyRequest "Google::Iam::V1::GetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::GetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-GetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def get_iam_policy(resource: nil, options: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `get_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being requested. See the operation documentation for the appropriate value for this field. 
  * **options** ([::Google::Iam::V1::GetPolicyOptions](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-GetPolicyOptions), ::Hash) — OPTIONAL: A `GetPolicyOptions` object for specifying options to `GetIamPolicy`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::GetIamPolicyRequest.new
    
    # Call the get_iam_policy method.
    result = client.get_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #initialize
    
    
    def initialize() { |config| ... } -> Client

Create a new DatabaseAdmin REST client object.

**Yields**

  * (config) — Configure the DatabaseAdmin client. 



**Yield Parameter**

  * **config** ([Client::Configuration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client-Configuration)) 



**Returns**

  * ([Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client)) — a new instance of Client 



**Example**
    
    
    # Create a client using the default configuration
    client = ::Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a client using a custom configuration
    client = ::Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new do |config|
      config.timeout = 10.0
    end

### #list_backup_operations
    
    
    def list_backup_operations(request, options = nil) -> ::Gapic::Operation
    def list_backup_operations(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Operation

Lists the backup [long-running operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") in the given instance. A backup operation has a name of the form `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation>`. The long-running operation [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.

**Overloads**
    
    
    def list_backup_operations(request, options = nil) -> ::Gapic::Operation

Pass arguments to `list_backup_operations` via a request object, either of type [ListBackupOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupOperationsRequest "Google::Cloud::Spanner::Admin::Database::V1::ListBackupOperationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListBackupOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupOperationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_operations(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Operation

Pass arguments to `list_backup_operations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`. 
  * **filter** (::String) — 

An expression that filters the list of returned backup operations.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.

The following fields in the [operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") are eligible for filtering:

    * `name` \- The name of the long-running operation
    * `done` \- False if the operation is in progress, else true.
    * `metadata.@type` \- the type of metadata. For example, the type string for [CreateBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupMetadata \(class\)") is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`.
    * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first if filtering on metadata fields.
    * `error` \- Error associated with the long-running operation.
    * `response.@type` \- the type of response.
    * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.

Here are a few examples:

    * `done:true` \- The operation is complete.
    * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where: 
      * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupMetadata \(class\)").
      * The source database name of backup contains the string "prod".
    * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
      * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupMetadata \(class\)").
      * The backup name contains the string "howl".
      * The operation started before 2018-03-28T14:50:00Z.
      * The operation resulted in an error.
    * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
      * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CopyBackupMetadata \(class\)").
      * The source backup name contains the string "test".
      * The operation started before 2022-01-18T14:50:00Z.
      * The operation resulted in an error.
    * `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where: 
      * The operation's metadata matches either of criteria: 
        * The operation's metadata type is [CreateBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CreateBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CreateBackupMetadata \(class\)") AND the source database name of the backup contains the string "test_db"
        * The operation's metadata type is [CopyBackupMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-CopyBackupMetadata "Google::Cloud::Spanner::Admin::Database::V1::CopyBackupMetadata \(class\)") AND the source backup name contains the string "test_bkp"
      * The operation resulted in an error.
  * **page_size** (::Integer) — Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupOperationsResponse#Google__Cloud__Spanner__Admin__Database__V1__ListBackupOperationsResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListBackupOperationsResponse#next_page_token \(method\)") from a previous [ListBackupOperationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupOperationsResponse "Google::Cloud::Spanner::Admin::Database::V1::ListBackupOperationsResponse \(class\)") to the same `parent` and with the same `filter`. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListBackupOperationsRequest.new
    
    # Call the list_backup_operations method.
    result = client.list_backup_operations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Longrunning::Operation.
      p item
    end

### #list_backup_schedules
    
    
    def list_backup_schedules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule>
    def list_backup_schedules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule>

Lists all the backup schedules for the database.

**Overloads**
    
    
    def list_backup_schedules(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule>

Pass arguments to `list_backup_schedules` via a request object, either of type [ListBackupSchedulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupSchedulesRequest "Google::Cloud::Spanner::Admin::Database::V1::ListBackupSchedulesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListBackupSchedulesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupSchedulesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backup_schedules(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule>

Pass arguments to `list_backup_schedules` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. Database is the parent resource whose backup schedules should be listed. Values are of the form projects/
  * **page_size** (::Integer) — Optional. Number of backup schedules to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — Optional. If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupSchedulesResponse#Google__Cloud__Spanner__Admin__Database__V1__ListBackupSchedulesResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListBackupSchedulesResponse#next_page_token \(method\)") from a previous [ListBackupSchedulesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupSchedulesResponse "Google::Cloud::Spanner::Admin::Database::V1::ListBackupSchedulesResponse \(class\)") to the same `parent`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListBackupSchedulesRequest.new
    
    # Call the list_backup_schedules method.
    result = client.list_backup_schedules request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule.
      p item
    end

### #list_backups
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Backup>
    def list_backups(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Backup>

Lists completed and pending backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`.

**Overloads**
    
    
    def list_backups(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Backup>

Pass arguments to `list_backups` via a request object, either of type [ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupsRequest "Google::Cloud::Spanner::Admin::Database::V1::ListBackupsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListBackupsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_backups(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Backup>

Pass arguments to `list_backups` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance to list backups from. Values are of the form `projects/<project>/instances/<instance>`. 
  * **filter** (::String) — 

An expression that filters the list of returned backups.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.

The following fields in the [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)") are eligible for filtering:

    * `name`
    * `database`
    * `state`
    * `create_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
    * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
    * `version_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
    * `size_bytes`
    * `backup_schedules`

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.

Here are a few examples:

    * `name:Howl` \- The backup's name contains the string "howl".
    * `database:prod` \- The database's name contains the string "prod".
    * `state:CREATING` \- The backup is pending creation.
    * `state:READY` \- The backup is fully created and ready for use.
    * `(name:howl) AND (create_time < \"2018-03-28T14:50:00Z\")` \- The backup name contains the string "howl" and `create_time` of the backup is before 2018-03-28T14:50:00Z.
    * `expire_time < \"2018-03-28T14:50:00Z\"` \- The backup `expire_time` is before 2018-03-28T14:50:00Z.
    * `size_bytes > 10000000000` \- The backup's size is greater than 10GB
    * `backup_schedules:daily` \- The backup is created from a schedule with "daily" in its name.
  * **page_size** (::Integer) — Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupsResponse#Google__Cloud__Spanner__Admin__Database__V1__ListBackupsResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListBackupsResponse#next_page_token \(method\)") from a previous [ListBackupsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListBackupsResponse "Google::Cloud::Spanner::Admin::Database::V1::ListBackupsResponse \(class\)") to the same `parent` and with the same `filter`. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListBackupsRequest.new
    
    # Call the list_backups method.
    result = client.list_backups request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Spanner::Admin::Database::V1::Backup.
      p item
    end

### #list_database_operations
    
    
    def list_database_operations(request, options = nil) -> ::Gapic::Operation
    def list_database_operations(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Operation

Lists database [longrunning-operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)"). A database operation has a name of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>`. The long-running operation [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations.

**Overloads**
    
    
    def list_database_operations(request, options = nil) -> ::Gapic::Operation

Pass arguments to `list_database_operations` via a request object, either of type [ListDatabaseOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseOperationsRequest "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseOperationsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseOperationsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseOperationsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_database_operations(parent: nil, filter: nil, page_size: nil, page_token: nil) -> ::Gapic::Operation

Pass arguments to `list_database_operations` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance of the database operations. Values are of the form `projects/<project>/instances/<instance>`. 
  * **filter** (::String) — 

An expression that filters the list of returned operations.

A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.

The following fields in the [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") are eligible for filtering:

    * `name` \- The name of the long-running operation
    * `done` \- False if the operation is in progress, else true.
    * `metadata.@type` \- the type of metadata. For example, the type string for [RestoreDatabaseMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseMetadata "Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseMetadata \(class\)") is `type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata`.
    * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first, if filtering on metadata fields.
    * `error` \- Error associated with the long-running operation.
    * `response.@type` \- the type of response.
    * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly.

Here are a few examples:

    * `done:true` \- The operation is complete.
    * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata) AND` \ `(metadata.source_type:BACKUP) AND` \ `(metadata.backup_info.backup:backup_howl) AND` \ `(metadata.name:restored_howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Return operations where: 
      * The operation's metadata type is [RestoreDatabaseMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseMetadata "Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseMetadata \(class\)").
      * The database is restored from a backup.
      * The backup name contains "backup_howl".
      * The restored database's name contains "restored_howl".
      * The operation started before 2018-03-28T14:50:00Z.
      * The operation resulted in an error.
  * **page_size** (::Integer) — Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseOperationsResponse#Google__Cloud__Spanner__Admin__Database__V1__ListDatabaseOperationsResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseOperationsResponse#next_page_token \(method\)") from a previous [ListDatabaseOperationsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseOperationsResponse "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseOperationsResponse \(class\)") to the same `parent` and with the same `filter`. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseOperationsRequest.new
    
    # Call the list_database_operations method.
    result = client.list_database_operations request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Longrunning::Operation.
      p item
    end

### #list_database_roles
    
    
    def list_database_roles(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole>
    def list_database_roles(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole>

Lists Cloud Spanner database roles.

**Overloads**
    
    
    def list_database_roles(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole>

Pass arguments to `list_database_roles` via a request object, either of type [ListDatabaseRolesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseRolesRequest "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseRolesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseRolesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseRolesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_database_roles(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole>

Pass arguments to `list_database_roles` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The database whose roles should be listed. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. 
  * **page_size** (::Integer) — Number of database roles to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseRolesResponse#Google__Cloud__Spanner__Admin__Database__V1__ListDatabaseRolesResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseRolesResponse#next_page_token \(method\)") from a previous [ListDatabaseRolesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabaseRolesResponse "Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseRolesResponse \(class\)"). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseRole)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseRole)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListDatabaseRolesRequest.new
    
    # Call the list_database_roles method.
    result = client.list_database_roles request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Spanner::Admin::Database::V1::DatabaseRole.
      p item
    end

### #list_databases
    
    
    def list_databases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Database>
    def list_databases(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Database>

Lists Cloud Spanner databases.

**Overloads**
    
    
    def list_databases(request, options = nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Database>

Pass arguments to `list_databases` via a request object, either of type [ListDatabasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabasesRequest "Google::Cloud::Spanner::Admin::Database::V1::ListDatabasesRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::ListDatabasesRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabasesRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def list_databases(parent: nil, page_size: nil, page_token: nil) -> ::Gapic::Rest::PagedEnumerable<::Google::Cloud::Spanner::Admin::Database::V1::Database>

Pass arguments to `list_databases` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The instance whose databases should be listed. Values are of the form `projects/<project>/instances/<instance>`. 
  * **page_size** (::Integer) — Number of databases to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size. 
  * **page_token** (::String) — If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabasesResponse#Google__Cloud__Spanner__Admin__Database__V1__ListDatabasesResponse_next_page_token_instance_ "Google::Cloud::Spanner::Admin::Database::V1::ListDatabasesResponse#next_page_token \(method\)") from a previous [ListDatabasesResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-ListDatabasesResponse "Google::Cloud::Spanner::Admin::Database::V1::ListDatabasesResponse \(class\)"). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database)>) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * (::Gapic::Rest::PagedEnumerable<[::Google::Cloud::Spanner::Admin::Database::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database)>) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::ListDatabasesRequest.new
    
    # Call the list_databases method.
    result = client.list_databases request
    
    # The returned object is of type Gapic::PagedEnumerable. You can iterate
    # over elements, and API calls will be issued to fetch pages as needed.
    result.each do |item|
      # Each element is of type ::Google::Cloud::Spanner::Admin::Database::V1::Database.
      p item
    end

### #logger
    
    
    def logger() -> Logger

The logger used for request/response debug logging.

**Returns**

  * (Logger) 



### #operations_client
    
    
    def operations_client() -> ::Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Operations

Get the associated client for long-running operations.

**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Operations](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Operations)) 



### #restore_database
    
    
    def restore_database(request, options = nil) -> ::Gapic::Operation
    def restore_database(parent: nil, database_id: nil, backup: nil, encryption_config: nil) -> ::Gapic::Operation

Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database [long-running operation][google.longrunning.Operation] has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>`, and can be used to track the progress of the operation, and to cancel it. The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [RestoreDatabaseMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseMetadata "Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseMetadata \(class\)"). The [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") type is [Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database "Google::Cloud::Spanner::Admin::Database::V1::Database \(class\)"), if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete.

**Overloads**
    
    
    def restore_database(request, options = nil) -> ::Gapic::Operation

Pass arguments to `restore_database` via a request object, either of type [RestoreDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseRequest "Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def restore_database(parent: nil, database_id: nil, backup: nil, encryption_config: nil) -> ::Gapic::Operation

Pass arguments to `restore_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **parent** (::String) — Required. The name of the instance in which to create the restored database. This instance must be in the same project and have the same instance configuration as the instance containing the source backup. Values are of the form `projects/<project>/instances/<instance>`. 
  * **database_id** (::String) — Required. The id of the database to create and restore to. This database must not already exist. The `database_id` appended to `parent` forms the full database name of the form `projects/<project>/instances/<instance>/databases/<database_id>`. 
  * **backup** (::String) — Name of the backup from which to restore. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. 
  * **encryption_config** ([::Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseEncryptionConfig), ::Hash) — Optional. An encryption configuration describing the encryption type and key resources in Cloud KMS used to encrypt/decrypt the database to restore to. If this field is not specified, the restored database will use the same encryption configuration as the backup by default, namely [encryption_type](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-RestoreDatabaseEncryptionConfig#Google__Cloud__Spanner__Admin__Database__V1__RestoreDatabaseEncryptionConfig_encryption_type_instance_ "Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseEncryptionConfig#encryption_type \(method\)") = `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::RestoreDatabaseRequest.new
    
    # Call the restore_database method.
    result = client.restore_database request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #set_iam_policy
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Sets the access control policy on a database or backup resource. Replaces any existing policy.

Authorization requires `spanner.databases.setIamPolicy` permission on [resource][google.iam.v1.SetIamPolicyRequest.resource]. For backups, authorization requires `spanner.backups.setIamPolicy` permission on [resource][google.iam.v1.SetIamPolicyRequest.resource].

**Overloads**
    
    
    def set_iam_policy(request, options = nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via a request object, either of type [Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-SetIamPolicyRequest "Google::Iam::V1::SetIamPolicyRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::SetIamPolicyRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-SetIamPolicyRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def set_iam_policy(resource: nil, policy: nil, update_mask: nil) -> ::Google::Iam::V1::Policy

Pass arguments to `set_iam_policy` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy is being specified. See the operation documentation for the appropriate value for this field. 
  * **policy** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-Policy), ::Hash) — REQUIRED: The complete policy to be applied to the `resource`. The size of the policy is limited to a few 10s of KB. An empty policy is a valid policy but certain Cloud Platform services (such as Projects) might reject them. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-FieldMask), ::Hash) — OPTIONAL: A FieldMask specifying which fields of the policy to modify. Only the fields in the mask will be modified. If no mask is provided, the following default mask is used:

`paths: "bindings, etag"`




**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-Policy)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::Policy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-Policy)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::SetIamPolicyRequest.new
    
    # Call the set_iam_policy method.
    result = client.set_iam_policy request
    
    # The returned object is of type Google::Iam::V1::Policy.
    p result

### #test_iam_permissions
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Returns permissions that the caller has on the specified database or backup resource.

Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has `spanner.databases.list` permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has `spanner.backups.list` permission on the containing instance.

**Overloads**
    
    
    def test_iam_permissions(request, options = nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via a request object, either of type [Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-TestIamPermissionsRequest "Google::Iam::V1::TestIamPermissionsRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Iam::V1::TestIamPermissionsRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-TestIamPermissionsRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def test_iam_permissions(resource: nil, permissions: nil) -> ::Google::Iam::V1::TestIamPermissionsResponse

Pass arguments to `test_iam_permissions` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **resource** (::String) — REQUIRED: The resource for which the policy detail is being requested. See the operation documentation for the appropriate value for this field. 
  * **permissions** (::Array<::String>) — The set of permissions to check for the `resource`. Permissions with wildcards (such as '_' or 'storage._ ') are not allowed. For more information see [IAM Overview](https://cloud.google.com/iam/docs/overview#permissions). 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Iam::V1::TestIamPermissionsResponse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Iam-V1-TestIamPermissionsResponse)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Iam::V1::TestIamPermissionsRequest.new
    
    # Call the test_iam_permissions method.
    result = client.test_iam_permissions request
    
    # The returned object is of type Google::Iam::V1::TestIamPermissionsResponse.
    p result

### #universe_domain
    
    
    def universe_domain() -> String

The effective universe domain

**Returns**

  * (String) 



### #update_backup
    
    
    def update_backup(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup
    def update_backup(backup: nil, update_mask: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Updates a pending or completed [Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup "Google::Cloud::Spanner::Admin::Database::V1::Backup \(class\)").

**Overloads**
    
    
    def update_backup(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Pass arguments to `update_backup` via a request object, either of type [UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateBackupRequest "Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateBackupRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup(backup: nil, update_mask: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::Backup

Pass arguments to `update_backup` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup** ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup), ::Hash) — 

Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Update is only supported for the following fields:

    * `backup.expire_time`.
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A mask specifying which fields (e.g. `expire_time`) in the Backup resource should be updated. This mask is relative to the Backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::Backup](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Backup)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupRequest.new
    
    # Call the update_backup method.
    result = client.update_backup request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::Backup.
    p result

### #update_backup_schedule
    
    
    def update_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule
    def update_backup_schedule(backup_schedule: nil, update_mask: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Updates a backup schedule.

**Overloads**
    
    
    def update_backup_schedule(request, options = nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `update_backup_schedule` via a request object, either of type [UpdateBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateBackupScheduleRequest "Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupScheduleRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupScheduleRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateBackupScheduleRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_backup_schedule(backup_schedule: nil, update_mask: nil) -> ::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule

Pass arguments to `update_backup_schedule` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **backup_schedule** ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule), ::Hash) — Required. The backup schedule to update. `backup_schedule.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. A mask specifying which fields in the BackupSchedule resource should be updated. This mask is relative to the BackupSchedule resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally. 



**Yields**

  * (result, operation) — Access the result along with the TransportOperation object 



**Yield Parameters**

  * **result** ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 
  * **operation** (::Gapic::Rest::TransportOperation) 



**Returns**

  * ([::Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-BackupSchedule)) 



**Raises**

  * (::Google::Cloud::Error) — if the REST call is aborted. 



**Example**

Basic example
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::UpdateBackupScheduleRequest.new
    
    # Call the update_backup_schedule method.
    result = client.update_backup_schedule request
    
    # The returned object is of type Google::Cloud::Spanner::Admin::Database::V1::BackupSchedule.
    p result

### #update_database
    
    
    def update_database(request, options = nil) -> ::Gapic::Operation
    def update_database(database: nil, update_mask: nil) -> ::Gapic::Operation

Updates a Cloud Spanner database. The returned [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") can be used to track the progress of updating the database. If the named database does not exist, returns `NOT_FOUND`.

While the operation is pending:

  * The database's [reconciling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database#Google__Cloud__Spanner__Admin__Database__V1__Database_reconciling_instance_ "Google::Cloud::Spanner::Admin::Database::V1::Database#reconciling \(method\)") field is set to true.
  * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata's [cancel_time](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseMetadata#Google__Cloud__Spanner__Admin__Database__V1__UpdateDatabaseMetadata_cancel_time_instance_ "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseMetadata#cancel_time \(method\)") is set, the updates are reverted, and the operation terminates with a `CANCELLED` status.
  * New UpdateDatabase requests will return a `FAILED_PRECONDITION` error until the pending operation is done (returns successfully or with error).
  * Reading the database via the API continues to give the pre-request values.



Upon completion of the returned operation:

  * The new values are in effect and readable via the API.
  * The database's [reconciling](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database#Google__Cloud__Spanner__Admin__Database__V1__Database_reconciling_instance_ "Google::Cloud::Spanner::Admin::Database::V1::Database#reconciling \(method\)") field becomes false.



The returned [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will have a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>` and can be used to track the database modification. The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [UpdateDatabaseMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseMetadata "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseMetadata \(class\)"). The [response](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_response_instance_ "Google::Longrunning::Operation#response \(method\)") field type is [Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database "Google::Cloud::Spanner::Admin::Database::V1::Database \(class\)"), if successful.

**Overloads**
    
    
    def update_database(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_database` via a request object, either of type [UpdateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseRequest "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_database(database: nil, update_mask: nil) -> ::Gapic::Operation

Pass arguments to `update_database` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **database** ([::Google::Cloud::Spanner::Admin::Database::V1::Database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-Database), ::Hash) — Required. The database to update. The `name` field of the database is of the form `projects/<project>/instances/<instance>/databases/<database>`. 
  * **update_mask** ([::Google::Protobuf::FieldMask](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Protobuf-FieldMask), ::Hash) — Required. The list of fields to update. Currently, only `enable_drop_protection` field can be updated. 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseRequest.new
    
    # Call the update_database method.
    result = client.update_database request
    
    # The returned object is of type Gapic::Operation. You can use it to
    # check the status of an operation, cancel it, or wait for results.
    # Here is how to wait for a response.
    result.wait_until_done! timeout: 60
    if result.response?
      p result.response
    else
      puts "No response received."
    end

### #update_database_ddl
    
    
    def update_database_ddl(request, options = nil) -> ::Gapic::Operation
    def update_database_ddl(database: nil, statements: nil, operation_id: nil, proto_descriptors: nil, throughput_mode: nil) -> ::Gapic::Operation

Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned [long-running operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)") will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track execution of the schema change(s). The [metadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_metadata_instance_ "Google::Longrunning::Operation#metadata \(method\)") field type is [UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseDdlMetadata "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseDdlMetadata \(class\)"). The operation has no response.

**Overloads**
    
    
    def update_database_ddl(request, options = nil) -> ::Gapic::Operation

Pass arguments to `update_database_ddl` via a request object, either of type [UpdateDatabaseDdlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseDdlRequest "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseDdlRequest \(class\)") or an equivalent Hash. 

**Parameters**

  * **request** ([::Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseDdlRequest](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseDdlRequest), ::Hash) — A request object representing the call parameters. Required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash. 
  * **options** (::Gapic::CallOptions, ::Hash) — Overrides the default settings for this call, e.g, timeout, retries etc. Optional. 


    
    
    def update_database_ddl(database: nil, statements: nil, operation_id: nil, proto_descriptors: nil, throughput_mode: nil) -> ::Gapic::Operation

Pass arguments to `update_database_ddl` via keyword arguments. Note that at least one keyword argument is required. To specify no parameters, or to keep all the default parameter values, pass an empty Hash as a request object (see above). 

**Parameters**

  * **database** (::String) — Required. The database to update. 
  * **statements** (::Array<::String>) — Required. DDL statements to be applied to the database. 
  * **operation_id** (::String) — If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operation_id` is used to construct the name of the resulting [Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)").

Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the [UpdateDatabaseDdl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client#Google__Cloud__Spanner__Admin__Database__V1__DatabaseAdmin__Rest__Client_update_database_ddl_instance_ "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client#update_database_ddl \(method\)") call is replayed, or the return value is otherwise lost: the [database](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-UpdateDatabaseDdlRequest#Google__Cloud__Spanner__Admin__Database__V1__UpdateDatabaseDdlRequest_database_instance_ "Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseDdlRequest#database \(method\)") and `operation_id` fields can be combined to form the [name](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation#Google__Longrunning__Operation_name_instance_ "Google::Longrunning::Operation#name \(method\)") of the resulting [longrunning.Operation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Longrunning-Operation "Google::Longrunning::Operation \(class\)"): `<database>/operations/<operation_id>`.

`operation_id` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, [UpdateDatabaseDdl](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-admin-database-v1/latest/Google-Cloud-Spanner-Admin-Database-V1-DatabaseAdmin-Rest-Client#Google__Cloud__Spanner__Admin__Database__V1__DatabaseAdmin__Rest__Client_update_database_ddl_instance_ "Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client#update_database_ddl \(method\)") returns `ALREADY_EXISTS`. 

  * **proto_descriptors** (::String) — Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run ` $protoc --proto_path=/app_path --proto_path=/lib_path \ --include_imports \ --descriptor_set_out=descriptors.data \ moon/shot/app.proto ` For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description). 
  * **throughput_mode** (::Boolean) — Optional. This field is exposed to be used by the Spanner Migration Tool. For more details, see [SMT](https://github.com/GoogleCloudPlatform/spanner-migration-tool). 



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
    
    
    require "google/cloud/spanner/admin/database/v1"
    
    # Create a client object. The client can be reused for multiple calls.
    client = Google::Cloud::Spanner::Admin::Database::V1::DatabaseAdmin::Rest::Client.new
    
    # Create a request. To set request fields, pass in keyword arguments.
    request = Google::Cloud::Spanner::Admin::Database::V1::UpdateDatabaseDdlRequest.new
    
    # Call the update_database_ddl method.
    result = client.update_database_ddl request
    
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
