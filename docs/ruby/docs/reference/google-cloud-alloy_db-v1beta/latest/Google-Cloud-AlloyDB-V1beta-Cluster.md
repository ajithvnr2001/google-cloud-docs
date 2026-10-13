---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster/
title: AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Cluster (v0.25.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:27:00.270157+00:00
---

# AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Cluster (v0.25.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  AlloyDB V1BETA API - Class Google::Cloud::AlloyDB::V1beta::Cluster (v0.25.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.25.0 (latest)  0.24.1  0.23.1  0.22.0  0.21.0  0.20.1  0.19.0  0.18.0  0.17.1  0.16.0  0.15.0  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 

Reference documentation and code samples for the AlloyDB V1BETA API class Google::Cloud::AlloyDB::V1beta::Cluster.

A cluster is a collection of regional AlloyDB resources. It can include a primary instance and one or more read pool instances. All cluster resources share a storage layer, which scales as needed.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #annotations
    
    
    def annotations() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 



### #annotations=
    
    
    def annotations=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128 



### #automated_backup_policy
    
    
    def automated_backup_policy() -> ::Google::Cloud::AlloyDB::V1beta::AutomatedBackupPolicy

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::AutomatedBackupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-AutomatedBackupPolicy)) — The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type. 




### #automated_backup_policy=
    
    
    def automated_backup_policy=(value) -> ::Google::Cloud::AlloyDB::V1beta::AutomatedBackupPolicy

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::AutomatedBackupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-AutomatedBackupPolicy)) — The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type. 




**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::AutomatedBackupPolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-AutomatedBackupPolicy)) — The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type. 




### #backup_source
    
    
    def backup_source() -> ::Google::Cloud::AlloyDB::V1beta::BackupSource

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::BackupSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-BackupSource)) — Output only. Cluster created from backup.

Note: The following fields are mutually exclusive: `backup_source`, `migration_source`, `cloudsql_backup_run_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cloudsql_backup_run_source
    
    
    def cloudsql_backup_run_source() -> ::Google::Cloud::AlloyDB::V1beta::CloudSQLBackupRunSource

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::CloudSQLBackupRunSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-CloudSQLBackupRunSource)) — Output only. Cluster created from CloudSQL snapshot.

Note: The following fields are mutually exclusive: `cloudsql_backup_run_source`, `backup_source`, `migration_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #cluster_type
    
    
    def cluster_type() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::ClusterType

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::ClusterType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-ClusterType)) — Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`



### #continuous_backup_config
    
    
    def continuous_backup_config() -> ::Google::Cloud::AlloyDB::V1beta::ContinuousBackupConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::ContinuousBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-ContinuousBackupConfig)) — Optional. Continuous backup configuration for this cluster. 



### #continuous_backup_config=
    
    
    def continuous_backup_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::ContinuousBackupConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::ContinuousBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-ContinuousBackupConfig)) — Optional. Continuous backup configuration for this cluster. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::ContinuousBackupConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-ContinuousBackupConfig)) — Optional. Continuous backup configuration for this cluster. 



### #continuous_backup_info
    
    
    def continuous_backup_info() -> ::Google::Cloud::AlloyDB::V1beta::ContinuousBackupInfo

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::ContinuousBackupInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-ContinuousBackupInfo)) — Output only. Continuous backup properties for this cluster. 



### #create_time
    
    
    def create_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. Create time stamp 



### #database_version
    
    
    def database_version() -> ::Google::Cloud::AlloyDB::V1beta::DatabaseVersion

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::DatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-DatabaseVersion)) — Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. 



### #database_version=
    
    
    def database_version=(value) -> ::Google::Cloud::AlloyDB::V1beta::DatabaseVersion

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::DatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-DatabaseVersion)) — Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::DatabaseVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-DatabaseVersion)) — Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used. 



### #dataplex_config
    
    
    def dataplex_config() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::DataplexConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::DataplexConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-DataplexConfig)) — Optional. Configuration for Dataplex integration. 



### #dataplex_config=
    
    
    def dataplex_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::Cluster::DataplexConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::Cluster::DataplexConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-DataplexConfig)) — Optional. Configuration for Dataplex integration. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::DataplexConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-DataplexConfig)) — Optional. Configuration for Dataplex integration. 



### #delete_time
    
    
    def delete_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. Delete time stamp 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — User-settable and human-readable display name for the Cluster. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — User-settable and human-readable display name for the Cluster. 



**Returns**

  * (::String) — User-settable and human-readable display name for the Cluster. 



### #encryption_config
    
    
    def encryption_config() -> ::Google::Cloud::AlloyDB::V1beta::EncryptionConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



### #encryption_config=
    
    
    def encryption_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::EncryptionConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::EncryptionConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-EncryptionConfig)) — Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data. 



### #encryption_info
    
    
    def encryption_info() -> ::Google::Cloud::AlloyDB::V1beta::EncryptionInfo

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::EncryptionInfo](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-EncryptionInfo)) — Output only. The encryption information for the cluster. 



### #etag
    
    
    def etag() -> ::String

**Returns**

  * (::String) — For Resource freshness validation (https://google.aip.dev/154) 



### #etag=
    
    
    def etag=(value) -> ::String

**Parameter**

  * **value** (::String) — For Resource freshness validation (https://google.aip.dev/154) 



**Returns**

  * (::String) — For Resource freshness validation (https://google.aip.dev/154) 



### #gemini_config
    
    
    def gemini_config() -> ::Google::Cloud::AlloyDB::V1beta::GeminiClusterConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::GeminiClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-GeminiClusterConfig)) — Optional. Deprecated and unused. This field will be removed in the near future. 



### #gemini_config=
    
    
    def gemini_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::GeminiClusterConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::GeminiClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-GeminiClusterConfig)) — Optional. Deprecated and unused. This field will be removed in the near future. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::GeminiClusterConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-GeminiClusterConfig)) — Optional. Deprecated and unused. This field will be removed in the near future. 



### #initial_user
    
    
    def initial_user() -> ::Google::Cloud::AlloyDB::V1beta::UserPassword

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-UserPassword)) — Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored. 



### #initial_user=
    
    
    def initial_user=(value) -> ::Google::Cloud::AlloyDB::V1beta::UserPassword

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-UserPassword)) — Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::UserPassword](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-UserPassword)) — Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored. 



### #labels
    
    
    def labels() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels as key value pairs 



### #labels=
    
    
    def labels=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Labels as key value pairs 



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Labels as key value pairs 



### #maintenance_schedule
    
    
    def maintenance_schedule() -> ::Google::Cloud::AlloyDB::V1beta::MaintenanceSchedule

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::MaintenanceSchedule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-MaintenanceSchedule)) — Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set. 



### #maintenance_update_policy
    
    
    def maintenance_update_policy() -> ::Google::Cloud::AlloyDB::V1beta::MaintenanceUpdatePolicy

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::MaintenanceUpdatePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-MaintenanceUpdatePolicy)) — Optional. The maintenance update policy determines when to allow or deny updates. 



### #maintenance_update_policy=
    
    
    def maintenance_update_policy=(value) -> ::Google::Cloud::AlloyDB::V1beta::MaintenanceUpdatePolicy

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::MaintenanceUpdatePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-MaintenanceUpdatePolicy)) — Optional. The maintenance update policy determines when to allow or deny updates. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::MaintenanceUpdatePolicy](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-MaintenanceUpdatePolicy)) — Optional. The maintenance update policy determines when to allow or deny updates. 



### #migration_source
    
    
    def migration_source() -> ::Google::Cloud::AlloyDB::V1beta::MigrationSource

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::MigrationSource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-MigrationSource)) — Output only. Cluster created via DMS migration.

Note: The following fields are mutually exclusive: `migration_source`, `backup_source`, `cloudsql_backup_run_source`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #name
    
    
    def name() -> ::String

**Returns**

  * (::String) — 

Output only. The name of the cluster resource with the format:

    * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see https://google.aip.dev/122. The prefix of the cluster resource name is the name of the parent resource:
    * projects/{project}/locations/{region}



### #network
    
    
    def network() -> ::String

**Returns**

  * (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead. 



### #network=
    
    
    def network=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead. 



**Returns**

  * (::String) — Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead. 



### #network_config
    
    
    def network_config() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::NetworkConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-NetworkConfig)) 



### #network_config=
    
    
    def network_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::Cluster::NetworkConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::Cluster::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-NetworkConfig)) 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::NetworkConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-NetworkConfig)) 



### #primary_config
    
    
    def primary_config() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::PrimaryConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::PrimaryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-PrimaryConfig)) — Output only. Cross Region replication config specific to PRIMARY cluster. 



### #psc_config
    
    
    def psc_config() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::PscConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::PscConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-PscConfig)) — Optional. The configuration for Private Service Connect (PSC) for the cluster. 



### #psc_config=
    
    
    def psc_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::Cluster::PscConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::Cluster::PscConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-PscConfig)) — Optional. The configuration for Private Service Connect (PSC) for the cluster. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::PscConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-PscConfig)) — Optional. The configuration for Private Service Connect (PSC) for the cluster. 



### #reconciling
    
    
    def reconciling() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance. 



### #satisfies_pzs
    
    
    def satisfies_pzs() -> ::Boolean

**Returns**

  * (::Boolean) — Output only. Reserved for future use. 



### #secondary_config
    
    
    def secondary_config() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::SecondaryConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::SecondaryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-SecondaryConfig)) — Cross Region replication config specific to SECONDARY cluster. 



### #secondary_config=
    
    
    def secondary_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::Cluster::SecondaryConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::Cluster::SecondaryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-SecondaryConfig)) — Cross Region replication config specific to SECONDARY cluster. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::SecondaryConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-SecondaryConfig)) — Cross Region replication config specific to SECONDARY cluster. 



### #service_account_email
    
    
    def service_account_email() -> ::String

**Returns**

  * (::String) — Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change. 



### #ssl_config
    
    
    def ssl_config() -> ::Google::Cloud::AlloyDB::V1beta::SslConfig

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — SSL configuration for this AlloyDB cluster. 



### #ssl_config=
    
    
    def ssl_config=(value) -> ::Google::Cloud::AlloyDB::V1beta::SslConfig

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — SSL configuration for this AlloyDB cluster. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SslConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SslConfig)) — SSL configuration for this AlloyDB cluster. 



### #state
    
    
    def state() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::State

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::State](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-State)) — Output only. The current serving state of the cluster. 



### #subscription_type
    
    
    def subscription_type() -> ::Google::Cloud::AlloyDB::V1beta::SubscriptionType

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SubscriptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SubscriptionType)) — Optional. Subscription type of the cluster. 



### #subscription_type=
    
    
    def subscription_type=(value) -> ::Google::Cloud::AlloyDB::V1beta::SubscriptionType

**Parameter**

  * **value** ([::Google::Cloud::AlloyDB::V1beta::SubscriptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SubscriptionType)) — Optional. Subscription type of the cluster. 



**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::SubscriptionType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-SubscriptionType)) — Optional. Subscription type of the cluster. 



### #tags
    
    
    def tags() -> ::Google::Protobuf::Map{::String => ::String}

**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: ` "123/environment": "production", "123/costCenter": "marketing" `



### #tags=
    
    
    def tags=(value) -> ::Google::Protobuf::Map{::String => ::String}

**Parameter**

  * **value** (::Google::Protobuf::Map{::String => ::String}) — Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: ` "123/environment": "production", "123/costCenter": "marketing" `



**Returns**

  * (::Google::Protobuf::Map{::String => ::String}) — Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: ` "123/environment": "production", "123/costCenter": "marketing" `



### #trial_metadata
    
    
    def trial_metadata() -> ::Google::Cloud::AlloyDB::V1beta::Cluster::TrialMetadata

**Returns**

  * ([::Google::Cloud::AlloyDB::V1beta::Cluster::TrialMetadata](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Cloud-AlloyDB-V1beta-Cluster-TrialMetadata)) — Output only. Metadata for free trial clusters 



### #uid
    
    
    def uid() -> ::String

**Returns**

  * (::String) — Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted. 



### #update_time
    
    
    def update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-alloy_db-v1beta/latest/Google-Protobuf-Timestamp)) — Output only. Update time stamp 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
