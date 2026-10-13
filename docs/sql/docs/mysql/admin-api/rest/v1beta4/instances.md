---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/
title: REST Resource: instances \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:05.973683+00:00
---

# REST Resource: instances  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  REST Resource: instances Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DatabaseInstance
    * JSON representation
    * SqlInstanceState
    * Settings
      * JSON representation
    * SqlAvailabilityType
    * SqlPricingPlan
    * SqlReplicationType
    * SqlActivationPolicy
    * IpConfiguration
      * JSON representation
    * AclEntry
      * JSON representation
    * SslMode
    * PscConfig
      * JSON representation
    * PscAutoConnectionConfig
      * JSON representation
    * AutoDnsStatus
    * CaMode
    * ServerCertificateRotationMode
    * LocationPreference
      * JSON representation
    * DatabaseFlags
      * JSON representation
    * SqlDataDiskType
    * MaintenanceWindow
      * JSON representation
    * SqlUpdateTrack
    * BackupConfiguration
      * JSON representation
    * BackupRetentionSettings
      * JSON representation
    * RetentionUnit
    * TransactionalLogStorageState
    * BackupTier
    * SqlActiveDirectoryConfig
      * JSON representation
    * ActiveDirectoryMode
    * DenyMaintenancePeriod
      * JSON representation
    * InsightsConfig
      * JSON representation
    * PasswordValidationPolicy
      * JSON representation
    * Complexity
    * SqlServerAuditConfig
      * JSON representation
    * Edition
    * ConnectorEnforcement
    * AdvancedMachineFeatures
      * JSON representation
    * DataCacheConfig
      * JSON representation
    * ConnectionPoolConfig
      * JSON representation
    * ConnectionPoolFlags
      * JSON representation
    * FinalBackupConfig
      * JSON representation
    * ReadPoolAutoScaleConfig
      * JSON representation
    * TargetMetric
      * JSON representation
    * DataApiAccess
    * IpMapping
      * JSON representation
    * SqlIpAddressType
    * SqlInstanceType
    * OnPremisesConfiguration
      * JSON representation
    * InstanceReference
      * JSON representation
    * SelectedObjects
      * JSON representation
    * SslOption
    * ReplicaConfiguration
      * JSON representation
    * MySqlReplicaConfiguration
      * JSON representation
    * SqlBackendType
    * SqlSuspensionReason
    * SqlScheduledMaintenance
      * JSON representation
    * SqlOutOfDiskReport
      * JSON representation
    * SqlOutOfDiskState
    * AvailableDatabaseVersion
      * JSON representation
    * SqlNetworkArchitecture
    * ReplicationCluster
      * JSON representation
    * GeminiInstanceConfig
      * JSON representation
    * PoolNodeConfig
      * JSON representation
    * DnsNameMapping
      * JSON representation
    * ConnectionType
    * DnsScope
    * RecordManager
    * BlueGreenDeploymentInfo
      * JSON representation
    * SourceRole
      * JSON representation
    * TargetRole
      * JSON representation
    * State
  * Methods



## Resource: DatabaseInstance

A Cloud SQL instance resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "state": enum ([SqlInstanceState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceState)),
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion)),
      "settings": {
        object ([Settings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Settings))
      },
      "etag": string,
      "failoverReplica": {
        "name": string,
        "available": boolean
      },
      "masterInstanceName": string,
      "replicaNames": [
        string
      ],
      "maxDiskSize": string,
      "currentDiskSize": string,
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpMapping))
        }
      ],
      "serverCaCert": {
        object ([SslCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts#SslCert))
      },
      "instanceType": enum ([SqlInstanceType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceType)),
      "project": string,
      "ipv6Address": string,
      "serviceAccountEmailAddress": string,
      "onPremisesConfiguration": {
        object ([OnPremisesConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.OnPremisesConfiguration))
      },
      "replicaConfiguration": {
        object ([ReplicaConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReplicaConfiguration))
      },
      "backendType": enum ([SqlBackendType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlBackendType)),
      "selfLink": string,
      "suspensionReason": [
        enum ([SqlSuspensionReason](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlSuspensionReason))
      ],
      "connectionName": string,
      "name": string,
      "region": string,
      "gceZone": string,
      "secondaryGceZone": string,
      "diskEncryptionConfiguration": {
        object ([DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/DiskEncryptionConfiguration))
      },
      "diskEncryptionStatus": {
        object ([DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/DiskEncryptionStatus))
      },
      "rootPassword": string,
      "scheduledMaintenance": {
        object ([SqlScheduledMaintenance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlScheduledMaintenance))
      },
      "satisfiesPzs": boolean,
      "databaseInstalledVersion": string,
      "createTime": string,
      "availableMaintenanceVersions": [
        string
      ],
      "maintenanceVersion": string,
      "upgradableDatabaseVersions": [
        {
          object ([AvailableDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AvailableDatabaseVersion))
        }
      ],
      "satisfiesPzi": boolean,
      "tags": {
        string: string,
        ...
      },
      "nodes": [
        {
          object ([PoolNodeConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PoolNodeConfig))
        }
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsNameMapping))
        }
      ],
      "outOfDiskReport": {
        object ([SqlOutOfDiskReport](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlOutOfDiskReport))
      },
      "sqlNetworkArchitecture": enum ([SqlNetworkArchitecture](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlNetworkArchitecture)),
      "pscServiceAttachmentLink": string,
      "dnsName": string,
      "primaryDnsName": string,
      "writeEndpoint": string,
      "replicationCluster": {
        object ([ReplicationCluster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReplicationCluster))
      },
      "geminiConfig": {
        object ([GeminiInstanceConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.GeminiInstanceConfig))
      },
      "switchTransactionLogsToCloudStorageEnabled": boolean,
      "includeReplicasForMajorVersionUpgrade": boolean,
      "nodeCount": integer,
      "deploymentInfo": {
        object ([BlueGreenDeploymentInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BlueGreenDeploymentInfo))
      }
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#instance`.  
`state` |  `enum (`[SqlInstanceState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceState)`)` The current serving state of the Cloud SQL instance.  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/SqlDatabaseVersion)`)` The database engine type and version. The `databaseVersion` field cannot be changed after instance creation.  
`settings` |  `object (`[Settings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Settings)`)` The user settings.  
`etag` |  `string` This field is deprecated and will be removed from a future version of the API. Use the `settings.settingsVersion` field instead.  
`failoverReplica` |  `object` The name and status of the failover replica.  
`failoverReplica.name` |  `string` The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID.  
`failoverReplica.available` |  `boolean` The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only failover to the failover replica when the status is true.  
`masterInstanceName` |  `string` The name of the instance which will act as primary in the replication setup.  
`replicaNames[]` |  `string` The replicas of the instance.  
`maxDiskSize  
**(deprecated)**` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The maximum disk size of the instance in bytes.  
`currentDiskSize  
**(deprecated)**` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details.  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpMapping)`)` The assigned IP addresses for the instance.  
`serverCaCert` |  `object (`[SslCert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/sslCerts#SslCert)`)` SSL configuration.  
`instanceType` |  `enum (`[SqlInstanceType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceType)`)` The instance type.  
`project` |  `string` The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable.  
`ipv6Address  
**(deprecated)**` |  `string` This item is deprecated!The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances.  
`serviceAccountEmailAddress` |  `string` The service account email address assigned to the instance. \This property is read-only.  
`onPremisesConfiguration` |  `object (`[OnPremisesConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.OnPremisesConfiguration)`)` Configuration specific to on-premises instances.  
`replicaConfiguration` |  `object (`[ReplicaConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReplicaConfiguration)`)` Configuration specific to failover replicas and read replicas.  
`backendType` |  `enum (`[SqlBackendType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlBackendType)`)` The backend type. `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google.This property is read-only; use the `tier` property in the `settings` object to determine the database type.  
`selfLink` |  `string` The URI of this resource.  
`suspensionReason[]` |  `enum (`[SqlSuspensionReason](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlSuspensionReason)`)` If the instance state is SUSPENDED, the reason for the suspension.  
`connectionName` |  `string` Connection name of the Cloud SQL instance used in connection strings.  
`name` |  `string` Name of the Cloud SQL instance. This does not include the project ID.  
`region` |  `string` The geographical region of the Cloud SQL instance.It can be one of the [regions](https://cloud.google.com/sql/docs/mysql/locations#location-r) where Cloud SQL operates:For example, `asia-east1`, `europe-west1`, and `us-central1`. The default value is `us-central1`.  
`gceZone` |  `string` The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance.  
`secondaryGceZone` |  `string` The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone.  
`diskEncryptionConfiguration` |  `object (`[DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/DiskEncryptionConfiguration)`)` Disk encryption configuration specific to an instance.  
`diskEncryptionStatus` |  `object (`[DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/DiskEncryptionStatus)`)` Disk encryption status specific to an instance.  
`rootPassword` |  `string` Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances.  
`scheduledMaintenance` |  `object (`[SqlScheduledMaintenance](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlScheduledMaintenance)`)` The start time of any upcoming scheduled maintenance for this instance.  
`satisfiesPzs` |  `boolean` This status indicates whether the instance satisfies PZS.The status is reserved for future use.  
`databaseInstalledVersion` |  `string` Output only. Stores the current database version running on the instance including minor version such as `MYSQL_8_0_18`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`availableMaintenanceVersions[]` |  `string` Output only. instances.list all maintenance versions applicable on the instance  
`maintenanceVersion` |  `string` The current software version on the instance.  
`upgradableDatabaseVersions[]` |  `object (`[AvailableDatabaseVersion](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AvailableDatabaseVersion)`)` Output only. All database versions that are available for upgrade.  
`satisfiesPzi` |  `boolean` Output only. This status indicates whether the instance satisfies PZI.The status is reserved for future use.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys and tag values that are bound to this instance. You must represent each item in the map as: `"<tag-key-namespaced-name>" : "<tag-value-short-name>"`.For example, a single resource can have the following tags:
    
    
      "123/environment": "production",
      "123/costCenter": "marketing",
    

For more information on tag creation and management, see <https://cloud.google.com/resource-manager/docs/tags/tags-overview>.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodes[]` |  `object (`[PoolNodeConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PoolNodeConfig)`)` Output only. Entries containing information about each read pool node of the read pool.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsNameMapping)`)` Output only. The list of DNS names used by this instance.  
`outOfDiskReport` |  `object (`[SqlOutOfDiskReport](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlOutOfDiskReport)`)` This field represents the report generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job  
`sqlNetworkArchitecture` |  `enum (`[SqlNetworkArchitecture](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlNetworkArchitecture)`)` The SQL network architecture for the instance.  
`pscServiceAttachmentLink` |  `string` Output only. The link to service attachment of PSC instance.  
`dnsName` |  `string` Output only. The dns name of the instance.  
`primaryDnsName  
**(deprecated)**` |  `string` This item is deprecated!Output only. DEPRECATED: please use writeEndpoint instead.  
`writeEndpoint` |  `string` Output only. The dns name of the primary instance in a replication group.  
`replicationCluster` |  `object (`[ReplicationCluster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReplicationCluster)`)` A primary instance and disaster recovery (DR) replica pair. A DR replica is a cross-region replica that you designate for failover in the event that the primary instance experiences regional failure. Applicable to MySQL and PostgreSQL.  
`geminiConfig` |  `object (`[GeminiInstanceConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.GeminiInstanceConfig)`)` Gemini instance configuration.  
`switchTransactionLogsToCloudStorageEnabled` |  `boolean` Input only. Whether Cloud SQL is enabled to switch storing point-in-time recovery log files from a data disk to Cloud Storage.  
`includeReplicasForMajorVersionUpgrade` |  `boolean` Input only. Determines whether an in-place major version upgrade of replicas happens when an in-place major version upgrade of a primary instance is initiated.  
`nodeCount` |  `integer` The number of read pool nodes in a read pool.  
`deploymentInfo` |  `object (`[BlueGreenDeploymentInfo](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BlueGreenDeploymentInfo)`)` Output only. Deployment info for the instance. This is set if the instance is currently part of any blue-green setup.  
  
### SqlInstanceState

The current serving state of the database instance.

Enums  
---  
`SQL_INSTANCE_STATE_UNSPECIFIED` | The state of the instance is unknown.  
`RUNNABLE` | The instance is running, or has been stopped by owner.  
`SUSPENDED` | The instance is not available, for example due to problems with billing.  
`PENDING_DELETE` | The instance is being deleted.  
`PENDING_CREATE` | The instance is being created.  
`MAINTENANCE` | The instance is down for maintenance.  
`FAILED` | The creation of the instance failed or a fatal error occurred during maintenance.  
`ONLINE_MAINTENANCE` | DeprecatedThis item is deprecated!  
`REPAIRING` | (Applicable to read pool nodes only.) The read pool node needs to be repaired. The database might be unavailable.  
  
### Settings

Database instance settings.

JSON representation  
---  
      
    
    {
      "settingsVersion": string,
      "authorizedGaeApplications": [
        string
      ],
      "tier": string,
      "kind": string,
      "userLabels": {
        string: string,
        ...
      },
      "availabilityType": enum ([SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlAvailabilityType)),
      "pricingPlan": enum ([SqlPricingPlan](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlPricingPlan)),
      "replicationType": enum ([SqlReplicationType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlReplicationType)),
      "storageAutoResizeLimit": string,
      "activationPolicy": enum ([SqlActivationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlActivationPolicy)),
      "ipConfiguration": {
        object ([IpConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpConfiguration))
      },
      "storageAutoResize": boolean,
      "locationPreference": {
        object ([LocationPreference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.LocationPreference))
      },
      "databaseFlags": [
        {
          object ([DatabaseFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DatabaseFlags))
        }
      ],
      "dataDiskType": enum ([SqlDataDiskType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlDataDiskType)),
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.MaintenanceWindow))
      },
      "backupConfiguration": {
        object ([BackupConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupConfiguration))
      },
      "databaseReplicationEnabled": boolean,
      "crashSafeReplicationEnabled": boolean,
      "dataDiskSizeGb": string,
      "activeDirectoryConfig": {
        object ([SqlActiveDirectoryConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlActiveDirectoryConfig))
      },
      "collation": string,
      "denyMaintenancePeriods": [
        {
          object ([DenyMaintenancePeriod](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DenyMaintenancePeriod))
        }
      ],
      "insightsConfig": {
        object ([InsightsConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InsightsConfig))
      },
      "passwordValidationPolicy": {
        object ([PasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PasswordValidationPolicy))
      },
      "sqlServerAuditConfig": {
        object ([SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlServerAuditConfig))
      },
      "edition": enum ([Edition](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Edition)),
      "connectorEnforcement": enum ([ConnectorEnforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectorEnforcement)),
      "deletionProtectionEnabled": boolean,
      "timeZone": string,
      "advancedMachineFeatures": {
        object ([AdvancedMachineFeatures](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AdvancedMachineFeatures))
      },
      "dataCacheConfig": {
        object ([DataCacheConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DataCacheConfig))
      },
      "replicationLagMaxSeconds": integer,
      "enableGoogleMlIntegration": boolean,
      "enableDataplexIntegration": boolean,
      "retainBackupsOnDelete": boolean,
      "dataDiskProvisionedIops": string,
      "dataDiskProvisionedThroughput": string,
      "connectionPoolConfig": {
        object ([ConnectionPoolConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionPoolConfig))
      },
      "finalBackupConfig": {
        object ([FinalBackupConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.FinalBackupConfig))
      },
      "readPoolAutoScaleConfig": {
        object ([ReadPoolAutoScaleConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReadPoolAutoScaleConfig))
      },
      "autoUpgradeEnabled": boolean,
      "dataApiAccess": enum ([DataApiAccess](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DataApiAccess))
    }  
  
Fields  
---  
`settingsVersion` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The version of instance settings. This is a required field for update method to make sure concurrent updates are handled properly. During update, use the most recent settingsVersion value for this instance and do not try to update this value.  
`authorizedGaeApplications[]  
**(deprecated)**` |  `string` This item is deprecated!The App Engine app IDs that can access this instance. (Deprecated) Applied to First Generation instances only.  
`tier` |  `string` The tier (or machine type) for this instance, for example `db-custom-1-3840`. WARNING: Changing this restarts the instance.  
`kind` |  `string` This is always `sql#settings`.  
`userLabels` |  `map (key: string, value: string)` User-provided labels, represented as a dictionary where each label is a single key value pair.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`availabilityType` |  `enum (`[SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlAvailabilityType)`)` Availability type. Potential values: * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data accessibility. * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available)./For more information, see [Overview of the High Availability Configuration](https://cloud.google.com/sql/docs/mysql/high-availability).  
`pricingPlan` |  `enum (`[SqlPricingPlan](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlPricingPlan)`)` The pricing plan for this instance. This can be either `PER_USE` or `PACKAGE`. Only `PER_USE` is supported for Second Generation instances.  
`replicationType  
**(deprecated)**` |  `enum (`[SqlReplicationType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlReplicationType)`)` This item is deprecated!The type of replication this instance uses. This can be either `ASYNCHRONOUS` or `SYNCHRONOUS`. (Deprecated) This property was only applicable to First Generation instances.  
`storageAutoResizeLimit` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit.  
`activationPolicy` |  `enum (`[SqlActivationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlActivationPolicy)`)` The activation policy specifies when the instance is activated; it is applicable only when the instance state is RUNNABLE. Valid values: * `ALWAYS`: The instance is on, and remains so even in the absence of connection requests. * `NEVER`: The instance is off; it is not activated, even if a connection request arrives.  
`ipConfiguration` |  `object (`[IpConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpConfiguration)`)` The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled for Second Generation instances.  
`storageAutoResize` |  `boolean` Configuration to increase storage size automatically. The default value is true.  
`locationPreference` |  `object (`[LocationPreference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.LocationPreference)`)` The location preference settings. This allows the instance to be located as near as possible to either an App Engine app or Compute Engine zone for better performance. App Engine co-location was only applicable to First Generation instances.  
`databaseFlags[]` |  `object (`[DatabaseFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DatabaseFlags)`)` The database flags passed to the instance at startup.  
`dataDiskType` |  `enum (`[SqlDataDiskType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlDataDiskType)`)` The type of data disk: `PD_SSD` (default) or `PD_HDD`. Not used for First Generation instances.  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.MaintenanceWindow)`)` The maintenance window for this instance. This specifies when the instance can be restarted for maintenance purposes.  
`backupConfiguration` |  `object (`[BackupConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupConfiguration)`)` The daily backup configuration for the instance.  
`databaseReplicationEnabled` |  `boolean` Configuration specific to read replica instances. Indicates whether replication is enabled or not. WARNING: Changing this restarts the instance.  
`crashSafeReplicationEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Configuration specific to read replica instances. Indicates whether database flags for crash-safe replication are enabled. This property was only applicable to First Generation instances.  
`dataDiskSizeGb` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The size of data disk, in GB. The data disk size minimum is 10GB.  
`activeDirectoryConfig` |  `object (`[SqlActiveDirectoryConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlActiveDirectoryConfig)`)` Active Directory configuration, relevant only for Cloud SQL for SQL Server.  
`collation` |  `string` The name of server Instance collation.  
`denyMaintenancePeriods[]` |  `object (`[DenyMaintenancePeriod](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DenyMaintenancePeriod)`)` Deny maintenance periods  
`insightsConfig` |  `object (`[InsightsConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InsightsConfig)`)` Insights configuration, for now relevant only for Postgres.  
`passwordValidationPolicy` |  `object (`[PasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PasswordValidationPolicy)`)` The local user password validation policy of the instance.  
`sqlServerAuditConfig` |  `object (`[SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlServerAuditConfig)`)` SQL Server specific audit configuration.  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Edition)`)` Optional. The edition type of the Cloud SQL instance.  
`connectorEnforcement` |  `enum (`[ConnectorEnforcement](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectorEnforcement)`)` Specifies if connections must use Cloud SQL connectors. Option values include the following: `NOT_REQUIRED` (Cloud SQL instances can be connected without Cloud SQL Connectors) and `REQUIRED` (Only allow connections that use Cloud SQL Connectors)Note that using REQUIRED disables all existing authorized networks. If this field is not specified when creating a new instance, NOT_REQUIRED is used. If this field is not specified when patching or updating an existing instance, it is left unchanged in the instance.  
`deletionProtectionEnabled` |  `boolean` Configuration to protect against accidental instance deletion.  
`timeZone` |  `string` Server timezone, relevant only for Cloud SQL for SQL Server.  
`advancedMachineFeatures` |  `object (`[AdvancedMachineFeatures](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AdvancedMachineFeatures)`)` Specifies advanced machine configuration for the instances relevant only for SQL Server.  
`dataCacheConfig` |  `object (`[DataCacheConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DataCacheConfig)`)` Configuration for data cache.  
`replicationLagMaxSeconds` |  `integer` Optional. Configuration value for recreation of replica after certain replication lag.  
`enableGoogleMlIntegration` |  `boolean` Optional. When this parameter is set to true, Cloud SQL instances can connect to Vertex AI to pass requests for real-time predictions and insights to the AI. The default value is false. This applies only to Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances.  
`enableDataplexIntegration` |  `boolean` Optional. By default, Cloud SQL instances have schema extraction disabled for Dataplex. When this parameter is set to true, schema extraction for Dataplex on Cloud SQL instances is activated.  
`retainBackupsOnDelete` |  `boolean` Optional. When this parameter is set to true, Cloud SQL retains backups of the instance even after the instance is deleted. The ON_DEMAND backup will be retained until customer deletes the backup or the project. The AUTOMATED backup will be retained based on the backups retention setting.  
`dataDiskProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned number of I/O operations per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
`dataDiskProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned throughput measured in MiB per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
`connectionPoolConfig` |  `object (`[ConnectionPoolConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionPoolConfig)`)` Optional. The managed connection pooling configuration for the instance.  
`finalBackupConfig` |  `object (`[FinalBackupConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.FinalBackupConfig)`)` Optional. The final backup configuration for the instance.  
`readPoolAutoScaleConfig` |  `object (`[ReadPoolAutoScaleConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ReadPoolAutoScaleConfig)`)` Optional. The read pool auto-scale configuration for the instance.  
`autoUpgradeEnabled` |  `boolean` Optional. Cloud SQL for MySQL auto-upgrade configuration. When this parameter is set to true, auto-upgrade is enabled for MySQL 8.0 minor versions. The MySQL version must be 8.0.35 or higher.  
`dataApiAccess` |  `enum (`[DataApiAccess](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DataApiAccess)`)` This parameter controls whether to allow using instances.executeSql API to connect to the instance. Not allowed by default.  
  
### SqlAvailabilityType

The availability type of the given Cloud SQL instance.

Enums  
---  
`SQL_AVAILABILITY_TYPE_UNSPECIFIED` | This is an unknown Availability type.  
`ZONAL` | Zonal available instance.  
`REGIONAL` | Regional available instance.  
  
### SqlPricingPlan

The pricing plan for this instance.

Enums  
---  
`SQL_PRICING_PLAN_UNSPECIFIED` | This is an unknown pricing plan for this instance.  
`PACKAGE` | The instance is billed at a monthly flat rate.  
`PER_USE` | The instance is billed per usage.  
  
### SqlReplicationType

Enums  
---  
`SQL_REPLICATION_TYPE_UNSPECIFIED` | This is an unknown replication type for a Cloud SQL instance.  
`SYNCHRONOUS` | The synchronous replication mode for First Generation instances. It is the default value.  
`ASYNCHRONOUS` | The asynchronous replication mode for First Generation instances. It provides a slight performance gain, but if an outage occurs while this option is set to asynchronous, you can lose up to a few seconds of updates to your data.  
  
### SqlActivationPolicy

Specifies when the instance is activated.

Enums  
---  
`SQL_ACTIVATION_POLICY_UNSPECIFIED` | Unknown activation plan.  
`ALWAYS` | The instance is always up and running.  
`NEVER` | The instance never starts.  
`ON_DEMAND` | The instance starts upon receiving requests.This item is deprecated!  
  
### IpConfiguration

IP Management configuration.

JSON representation  
---  
      
    
    {
      "ipv4Enabled": boolean,
      "privateNetwork": string,
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object ([AclEntry](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AclEntry))
        }
      ],
      "allocatedIpRange": string,
      "enablePrivatePathForGoogleCloudServices": boolean,
      "sslMode": enum ([SslMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SslMode)),
      "customSubjectAlternativeNames": [
        string
      ],
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscConfig))
      },
      "serverCaMode": enum ([CaMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.CaMode)),
      "serverCaPool": string,
      "serverCertificateRotationMode": enum ([ServerCertificateRotationMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ServerCertificateRotationMode))
    }  
  
Fields  
---  
`ipv4Enabled` |  `boolean` Whether the instance is assigned a public IP address or not.  
`privateNetwork` |  `string` The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `/projects/myProject/global/networks/default`. This setting can be updated, but it cannot be removed after it is set.  
`requireSsl` |  `boolean` Use `sslMode` instead.Whether SSL/TLS connections over IP are enforced. If set to false, then allow both non-SSL/non-TLS and SSL/TLS connections. For SSL/TLS connections, the client certificate won't be verified. If set to true, then only allow connections encrypted with SSL/TLS and with valid client certificates. If you want to enforce SSL/TLS without enforcing the requirement for valid client certificates, then use the `sslMode` flag instead of the legacy `requireSsl` flag.  
`authorizedNetworks[]` |  `object (`[AclEntry](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AclEntry)`)` The list of external networks that are allowed to connect to the instance using the IP. In 'CIDR' notation, also known as 'slash' notation (for example: `157.197.200.0/24`).  
`allocatedIpRange` |  `string` The name of the allocated ip range for the private ip Cloud SQL instance. For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with [RFC 1035](https://tools.ietf.org/html/rfc1035). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?.`  
`enablePrivatePathForGoogleCloudServices` |  `boolean` Controls connectivity to private IP instances from Google services, such as BigQuery.  
`sslMode` |  `enum (`[SslMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SslMode)`)` Specify how SSL/TLS is enforced in database connections. If you must use the `requireSsl` flag for backward compatibility, then only the following value pairs are valid:For PostgreSQL and MySQL:

  * `sslMode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `requireSsl=false`
  * `sslMode=ENCRYPTED_ONLY` and `requireSsl=false`
  * `sslMode=TRUSTED_CLIENT_CERTIFICATE_REQUIRED` and `requireSsl=true`

For SQL Server:

  * `sslMode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `requireSsl=false`
  * `sslMode=ENCRYPTED_ONLY` and `requireSsl=true`

The value of `sslMode` has priority over the value of `requireSsl`.For example, for the pair `sslMode=ENCRYPTED_ONLY` and `requireSsl=false`, `sslMode=ENCRYPTED_ONLY` means accept only SSL connections, while `requireSsl=false` means accept both non-SSL and SSL connections. In this case, MySQL and PostgreSQL databases respect `sslMode` and accepts only SSL connections.  
`customSubjectAlternativeNames[]` |  `string` Optional. Custom Subject Alternative Name(SAN)s for a Cloud SQL instance.  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscConfig)`)` PSC settings for this instance.  
`serverCaMode` |  `enum (`[CaMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.CaMode)`)` Specify what type of CA is used for the server certificate.  
`serverCaPool` |  `string` Optional. The resource name of the server CA pool for an instance with `CUSTOMER_MANAGED_CAS_CA` as the `serverCaMode`. Format: projects/{PROJECT}/locations/{REGION}/caPools/{CA_POOL_ID}  
`serverCertificateRotationMode` |  `enum (`[ServerCertificateRotationMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ServerCertificateRotationMode)`)` Optional. Controls the automatic server certificate rotation feature. This feature is disabled by default. When enabled, the server certificate will be automatically rotated during Cloud SQL scheduled maintenance or self-service maintenance updates up to six months before it expires. This setting can only be set if serverCaMode is either GOOGLE_MANAGED_CAS_CA or CUSTOMER_MANAGED_CAS_CA.  
  
### AclEntry

An entry for an Access Control list.

JSON representation  
---  
      
    
    {
      "value": string,
      "expirationTime": string,
      "name": string,
      "kind": string
    }  
  
Fields  
---  
`value` |  `string` The allowlisted value for the access control list.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when this access control entry expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`name` |  `string` Optional. A label to identify this entry.  
`kind` |  `string` This is always `sql#aclEntry`.  
  
### SslMode

The SSL options for database connections.

Enums  
---  
`SSL_MODE_UNSPECIFIED` | The SSL mode is unknown.  
`ALLOW_UNENCRYPTED_AND_ENCRYPTED` | Allow non-SSL/non-TLS and SSL/TLS connections. For SSL connections to MySQL and PostgreSQL, the client certificate isn't verified.When this value is used, the legacy `requireSsl` flag must be false or cleared to avoid a conflict between the values of the two flags.  
`ENCRYPTED_ONLY` | Only allow connections encrypted with SSL/TLS. For SSL connections to MySQL and PostgreSQL, the client certificate isn't verified.When this value is used, the legacy `requireSsl` flag must be false or cleared to avoid a conflict between the values of the two flags.  
`TRUSTED_CLIENT_CERTIFICATE_REQUIRED` | Only allow connections encrypted with SSL/TLS and with valid client certificates.When this value is used, the legacy `requireSsl` flag must be true or cleared to avoid the conflict between values of two flags. PostgreSQL clients or users that connect using IAM database authentication must use either the [Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/postgres/connect-auth-proxy) or [Cloud SQL Connectors](https://cloud.google.com/sql/docs/postgres/connect-connectors) to enforce client identity verification.Only applicable to MySQL and PostgreSQL. Not applicable to SQL Server.  
  
### PscConfig

PSC settings for a Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "allowedConsumerProjects": [
        string
      ],
      "pscAutoConnections": [
        {
          object ([PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscAutoConnectionConfig))
        }
      ],
      "networkAttachmentUri": string,
      "pscEnabled": boolean,
      "pscAutoDnsEnabled": boolean,
      "pscWriteEndpointDnsEnabled": boolean
    }  
  
Fields  
---  
`allowedConsumerProjects[]` |  `string` Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).  
`pscAutoConnections[]` |  `object (`[PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscAutoConnectionConfig)`)` Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.  
`networkAttachmentUri` |  `string` Optional. The network attachment of the consumer network that the Private Service Connect enabled Cloud SQL instance is authorized to connect via PSC interface. format: projects/PROJECT/regions/REGION/networkAttachments/ID  
`pscEnabled` |  `boolean` Whether PSC connectivity is enabled for this instance.  
`pscAutoDnsEnabled` |  `boolean` Optional. Indicates whether Private Service Connect DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections. This will default to true for new instances when Private Service Connect is enabled.  
`pscWriteEndpointDnsEnabled` |  `boolean` Optional. Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal global DNS record across all networks configured with Private Service Connect auto-connections that points to the cluster primary instance. This feature is only supported for Enterprise Plus edition. This will default to true for new enterprise plus instances when `pscAutoDnsEnabled` is enabled.  
  
### PscAutoConnectionConfig

Settings for an automatically-setup Private Service Connect consumer endpoint that is used to connect to a Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "consumerProject": string,
      "consumerNetwork": string,
      "ipAddress": string,
      "status": string,
      "consumerNetworkStatus": string,
      "serviceConnectionPolicy": string,
      "instanceAutoDnsStatus": enum ([AutoDnsStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AutoDnsStatus)),
      "writeEndpointAutoDnsStatus": enum ([AutoDnsStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AutoDnsStatus))
    }  
  
Fields  
---  
`consumerProject` |  `string` Optional. This is the project ID of consumer service project of this consumer endpoint.Optional. This is only applicable if consumerNetwork is a shared vpc network.  
`consumerNetwork` |  `string` Optional. The consumer network of this consumer endpoint. This must be a resource path that includes both the host project and the network name.For example, `projects/project1/global/networks/network1`.The consumer host project of this network might be different from the consumer service project.  
`ipAddress` |  `string` The IP address of the consumer endpoint.  
`status` |  `string` The connection status of the consumer endpoint.  
`consumerNetworkStatus` |  `string` The connection policy status of the consumer network.  
`serviceConnectionPolicy` |  `string` Output only. The service connection policy created automatically for the consumer network when `pscAutoConnectionPolicyEnabled` is true. It is in the format of: `projects/{project}/regions/{region}/serviceConnectionPolicies/{policyId}` The `policyId` is in format of `$NETWORK-$RANDOM`.  
`instanceAutoDnsStatus` |  `enum (`[AutoDnsStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AutoDnsStatus)`)` Output only. The status of automated DNS provisioning.  
`writeEndpointAutoDnsStatus` |  `enum (`[AutoDnsStatus](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.AutoDnsStatus)`)` Output only. The status of automated DNS provisioning for the write endpoint.  
  
### AutoDnsStatus

The status of automated DNS provisioning.

Enums  
---  
`AUTO_DNS_STATUS_UNSPECIFIED` | Unspecified status. This means status is missing from dependency service.  
`AUTO_DNS_OK` | DNS provisioning is OK.  
`AUTO_DNS_FAILED` | DNS provisioning failed.  
`AUTO_DNS_UNKNOWN` | DNS provisioning status is not recognized by Cloud SQL.  
  
### CaMode

Various Certificate Authority (CA) modes for certificate signing.

Enums  
---  
`CA_MODE_UNSPECIFIED` | CA mode is unspecified. It is effectively the same as `GOOGLE_MANAGED_INTERNAL_CA`.  
`GOOGLE_MANAGED_INTERNAL_CA` | Google-managed self-signed internal CA.  
`GOOGLE_MANAGED_CAS_CA` | Google-managed regional CA part of root CA hierarchy hosted on Google Cloud's Certificate Authority Service (CAS).  
`CUSTOMER_MANAGED_CAS_CA` | Customer-managed CA hosted on Google Cloud's Certificate Authority Service (CAS).  
  
### ServerCertificateRotationMode

Settings for automatic server certificate rotation.

Enums  
---  
`SERVER_CERTIFICATE_ROTATION_MODE_UNSPECIFIED` | Unspecified: no automatic server certificate rotation.  
`NO_AUTOMATIC_ROTATION` | No automatic server certificate rotation. The user must [manage server certificate rotation](https://docs.cloud.google.com/sql/docs/mysql/manage-ssl-instance#rotate-server-certificate-cas) on their side.  
`AUTOMATIC_ROTATION_DURING_MAINTENANCE` | Automatic server certificate rotation during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `serverCaMode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`.  
  
### LocationPreference

Preferred location. This specifies where a Cloud SQL instance is located. Note that if the preferred location is not available, the instance will be located as close as possible within the region. Only one location may be specified.

JSON representation  
---  
      
    
    {
      "followGaeApplication": string,
      "zone": string,
      "secondaryZone": string,
      "kind": string
    }  
  
Fields  
---  
`followGaeApplication  
**(deprecated)**` |  `string` This item is deprecated!The App Engine application to follow, it must be in the same region as the Cloud SQL instance. WARNING: Changing this might restart the instance.  
`zone` |  `string` The preferred Compute Engine zone (for example: us-central1-a, us-central1-b, etc.). WARNING: Changing this might restart the instance.  
`secondaryZone` |  `string` The preferred Compute Engine zone for the secondary/failover (for example: us-central1-a, us-central1-b, etc.). To disable this field, set it to 'no_secondary_zone'.  
`kind` |  `string` This is always `sql#locationPreference`.  
  
### DatabaseFlags

Database flags for Cloud SQL instances.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` The name of the flag. These flags are passed at instance startup, so include both server options and system variables. Flags are specified with underscores, not hyphens. For more information, see [Configuring Database Flags](https://cloud.google.com/sql/docs/mysql/flags) in the Cloud SQL documentation.  
`value` |  `string` The value of the flag. Boolean flags are set to `on` for true and `off` for false. This field must be omitted if the flag doesn't take a value.  
  
### SqlDataDiskType

The type of disk that is used for a v2 instance to use.

Enums  
---  
`SQL_DATA_DISK_TYPE_UNSPECIFIED` | This is an unknown data disk type.  
`PD_SSD` | An SSD data disk.  
`PD_HDD` | An HDD data disk.  
`OBSOLETE_LOCAL_SSD` | This field is deprecated and will be removed from a future version of the API.This item is deprecated!  
`HYPERDISK_BALANCED` | A Hyperdisk Balanced data disk.  
  
### MaintenanceWindow

Maintenance window. This specifies when a Cloud SQL instance is restarted for system maintenance purposes.

JSON representation  
---  
      
    
    {
      "hour": integer,
      "day": integer,
      "updateTrack": enum ([SqlUpdateTrack](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlUpdateTrack)),
      "kind": string
    }  
  
Fields  
---  
`hour` |  `integer` Hour of day - 0 to 23. Specify in the UTC time zone.  
`day` |  `integer` Day of week - `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, or `SUNDAY`. Specify in the UTC time zone. Returned in output as an integer, 1 to 7, where `1` equals Monday.  
`updateTrack` |  `enum (`[SqlUpdateTrack](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlUpdateTrack)`)` Maintenance timing settings: `canary`, `stable`, or `week5`. For more information, see [About maintenance on Cloud SQL instances](https://cloud.google.com/sql/docs/mysql/maintenance).  
`kind` |  `string` This is always `sql#maintenanceWindow`.  
  
### SqlUpdateTrack

Enums  
---  
`SQL_UPDATE_TRACK_UNSPECIFIED` | This is an unknown maintenance timing preference.  
`canary` | For an instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 7 to 14 days after the notification is sent out. Also referred to as `Week 1` (Console) and `preview` (gcloud CLI).  
`stable` | For an instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 15 to 21 days after the notification is sent out. Also referred to as `Week 2` (Console) and `production` (gcloud CLI).  
`week5` | For instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 35 to 42 days after the notification is sent out.  
  
### BackupConfiguration

Database instance backup configuration.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "enabled": boolean,
      "kind": string,
      "binaryLogEnabled": boolean,
      "replicationLogArchivingEnabled": boolean,
      "location": string,
      "pointInTimeRecoveryEnabled": boolean,
      "transactionLogRetentionDays": integer,
      "backupRetentionSettings": {
        object ([BackupRetentionSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupRetentionSettings))
      },
      "transactionalLogStorageState": enum ([TransactionalLogStorageState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TransactionalLogStorageState)),
      "backupTier": enum ([BackupTier](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupTier))
    }  
  
Fields  
---  
`startTime` |  `string` Start time for the daily backup configuration in UTC timezone in the 24 hour format - `HH:MM`.  
`enabled` |  `boolean` Whether this configuration is enabled.  
`kind` |  `string` This is always `sql#backupConfiguration`.  
`binaryLogEnabled` |  `boolean` (MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well.  
`replicationLogArchivingEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: replicationLogArchivingEnabled is deprecated and will be removed from a future version of the API. Use `[pointInTimeRecoveryEnabled](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupConfiguration.FIELDS.point_in_time_recovery_enabled)` instead.  
`location` |  `string` Location of the backup  
`pointInTimeRecoveryEnabled` |  `boolean` Whether point in time recovery is enabled.  
`transactionLogRetentionDays` |  `integer` The number of days of transaction logs we retain for point in time restore, from 1-7.  
`backupRetentionSettings` |  `object (`[BackupRetentionSettings](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupRetentionSettings)`)` Backup retention settings.  
`transactionalLogStorageState` |  `enum (`[TransactionalLogStorageState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TransactionalLogStorageState)`)` Output only. This value contains the storage location of transactional logs for the database for point-in-time recovery.  
`backupTier` |  `enum (`[BackupTier](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.BackupTier)`)` Output only. Backup tier that manages the backups for the instance.  
  
### BackupRetentionSettings

We currently only support backup retention by specifying the number of backups we will retain.

JSON representation  
---  
      
    
    {
      "retentionUnit": enum ([RetentionUnit](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.RetentionUnit)),
      "retainedBackups": integer
    }  
  
Fields  
---  
`retentionUnit` |  `enum (`[RetentionUnit](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.RetentionUnit)`)` The unit that 'retainedBackups' represents.  
`retainedBackups` |  `integer` Depending on the value of retentionUnit, this is used to determine if a backup needs to be deleted. If retentionUnit is 'COUNT', we will retain this many backups.  
  
### RetentionUnit

The units that retainedBackups specifies, we only support COUNT.

Enums  
---  
`RETENTION_UNIT_UNSPECIFIED` | Backup retention unit is unspecified, will be treated as COUNT.  
`COUNT` | Retention will be by count, eg. "retain the most recent 7 backups".  
  
### TransactionalLogStorageState

This value contains the storage location of the transactional logs used to perform point-in-time recovery (PITR) for the database.

Enums  
---  
`TRANSACTIONAL_LOG_STORAGE_STATE_UNSPECIFIED` | Unspecified.  
`DISK` | The transaction logs used for PITR for the instance are stored on a data disk.  
`SWITCHING_TO_CLOUD_STORAGE` | The transaction logs used for PITR for the instance are switching from being stored on a data disk to being stored in Cloud Storage. Only applicable to MySQL.  
`SWITCHED_TO_CLOUD_STORAGE` | The transaction logs used for PITR for the instance are now stored in Cloud Storage. Previously, they were stored on a data disk. Only applicable to MySQL.  
`CLOUD_STORAGE` | The transaction logs used for PITR for the instance are stored in Cloud Storage. Only applicable to MySQL and PostgreSQL.  
  
### BackupTier

Backup tier that manages the backups for the instance.

Enums  
---  
`BACKUP_TIER_UNSPECIFIED` | Unspecified.  
`STANDARD` | Instance is managed by Cloud SQL.  
`ADVANCED` | Deprecated: ADVANCED is deprecated. Please use ENHANCED instead.This item is deprecated!  
`ENHANCED` | Instance is managed by Google Cloud Backup and DR Service.  
  
### SqlActiveDirectoryConfig

Active Directory configuration, relevant only for Cloud SQL for SQL Server.

JSON representation  
---  
      
    
    {
      "kind": string,
      "domain": string,
      "mode": enum ([ActiveDirectoryMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ActiveDirectoryMode)),
      "dnsServers": [
        string
      ],
      "adminCredentialSecretName": string,
      "organizationalUnit": string
    }  
  
Fields  
---  
`kind` |  `string` This is always sql#activeDirectoryConfig.  
`domain` |  `string` The name of the domain (e.g., mydomain.com).  
`mode` |  `enum (`[ActiveDirectoryMode](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ActiveDirectoryMode)`)` Optional. The mode of the Active Directory configuration.  
`dnsServers[]` |  `string` Optional. Domain controller IPv4 addresses used to bootstrap Active Directory.  
`adminCredentialSecretName` |  `string` Optional. The secret manager key storing the administrator credential. (e.g., projects/{project}/secrets/{secret}).  
`organizationalUnit` |  `string` Optional. The organizational unit distinguished name. This is the full hierarchical path to the organizational unit.  
  
### ActiveDirectoryMode

The modes of Active Directory configuration.

Enums  
---  
`ACTIVE_DIRECTORY_MODE_UNSPECIFIED` | Unspecified mode.  
`MANAGED_ACTIVE_DIRECTORY` | Managed Active Directory mode. This is the fallback option to maintain backward compatibility.  
`SELF_MANAGED_ACTIVE_DIRECTORY` | Deprecated: Use CUSTOMER_MANAGED_ACTIVE_DIRECTORY instead.This item is deprecated!  
`CUSTOMER_MANAGED_ACTIVE_DIRECTORY` | Customer-managed Active Directory mode.  
  
### DenyMaintenancePeriod

Deny Maintenance Periods. This specifies a date range during when all CSA rollout will be denied.

JSON representation  
---  
      
    
    {
      "startDate": string,
      "endDate": string,
      "time": string
    }  
  
Fields  
---  
`startDate` |  `string` "deny maintenance period" start date. If the year of the start date is empty, the year of the end date also must be empty. In this case, it means the deny maintenance period recurs every year. The date is in format yyyy-mm-dd i.e., 2020-11-01, or mm-dd, i.e., 11-01  
`endDate` |  `string` "deny maintenance period" end date. If the year of the end date is empty, the year of the start date also must be empty. In this case, it means the deny maintenance period recurs every year. The date is in format yyyy-mm-dd i.e., 2020-11-01, or mm-dd, i.e., 11-01  
`time` |  `string` Time in UTC when the "deny maintenance period" starts on startDate and ends on endDate. The time is in format: HH:mm:SS, i.e., 00:00:00  
  
### InsightsConfig

Insights configuration. This specifies when Cloud SQL Insights feature is enabled and optional configuration.

JSON representation  
---  
      
    
    {
      "queryInsightsEnabled": boolean,
      "recordClientAddress": boolean,
      "recordApplicationTags": boolean,
      "queryStringLength": integer,
      "queryPlansPerMinute": integer,
      "enhancedQueryInsightsEnabled": boolean
    }  
  
Fields  
---  
`queryInsightsEnabled` |  `boolean` Whether Query Insights feature is enabled.  
`recordClientAddress` |  `boolean` Whether Query Insights will record client address when enabled.  
`recordApplicationTags` |  `boolean` Whether Query Insights will record application tags from query when enabled.  
`queryStringLength` |  `integer` Maximum query length stored in bytes. Default value: 1024 bytes. Range: 256-4500 bytes. Query lengths greater than this field value will be truncated to this value. When unset, query length will be the default value. Changing query length will restart the database.  
`queryPlansPerMinute` |  `integer` Number of query execution plans captured by Insights per minute for all queries combined. Default is 5.  
`enhancedQueryInsightsEnabled` |  `boolean` Optional. Whether enhanced query insights feature is enabled.  
  
### PasswordValidationPolicy

Database instance local user password validation policy. This message defines the password policy for local database users. When enabled, it enforces constraints on password complexity, length, and reuse. Keep this policy enabled to help prevent unauthorized access.

JSON representation  
---  
      
    
    {
      "minLength": integer,
      "complexity": enum ([Complexity](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Complexity)),
      "reuseInterval": integer,
      "disallowUsernameSubstring": boolean,
      "passwordChangeInterval": string,
      "enablePasswordPolicy": boolean,
      "disallowCompromisedCredentials": boolean
    }  
  
Fields  
---  
`minLength` |  `integer` Minimum number of characters allowed.  
`complexity` |  `enum (`[Complexity](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.Complexity)`)` The complexity of the password.  
`reuseInterval` |  `integer` Number of previous passwords that cannot be reused.  
`disallowUsernameSubstring` |  `boolean` Disallow username as a part of the password.  
`passwordChangeInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`enablePasswordPolicy` |  `boolean` Whether to enable the password policy or not. When enabled, passwords must meet complexity requirements. Keep this policy enabled to help prevent unauthorized access. Disabling this policy allows weak passwords.  
`disallowCompromisedCredentials  
**(deprecated)**` |  `boolean` This item is deprecated!This field is deprecated and will be removed in a future version of the API.  
  
### Complexity

The complexity choices of the password.

Enums  
---  
`COMPLEXITY_UNSPECIFIED` | Complexity check is not specified.  
`COMPLEXITY_DEFAULT` | A combination of lowercase, uppercase, numeric, and non-alphanumeric characters.  
  
### SqlServerAuditConfig

SQL Server specific audit configuration.

JSON representation  
---  
      
    
    {
      "kind": string,
      "bucket": string,
      "retentionInterval": string,
      "uploadInterval": string
    }  
  
Fields  
---  
`kind` |  `string` This is always sql#sqlServerAuditConfig  
`bucket` |  `string` The name of the destination bucket (e.g., gs://mybucket).  
`retentionInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` How long to keep generated audit files.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`uploadInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` How often to upload generated audit files.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### Edition

The list of Cloud SQL editions available to users.

Enums  
---  
`EDITION_UNSPECIFIED` | The instance did not specify the edition.  
`ENTERPRISE` | The instance is an enterprise edition.  
`ENTERPRISE_PLUS` | The instance is an Enterprise Plus edition.  
`DEVELOPER` | This instance is a Cloud SQL developer edition instance.  
  
### ConnectorEnforcement

The options for enforcing Cloud SQL connectors in the instance.

Enums  
---  
`CONNECTOR_ENFORCEMENT_UNSPECIFIED` | The requirement for Cloud SQL connectors is unknown.  
`NOT_REQUIRED` | Do not require Cloud SQL connectors.  
`REQUIRED` | Require all connections to use Cloud SQL connectors, including the Cloud SQL Auth Proxy and Cloud SQL Java, Python, and Go connectors. Note: This disables all existing authorized networks.  
  
### AdvancedMachineFeatures

Specifies options for controlling advanced machine features.

JSON representation  
---  
      
    
    {
      "threadsPerCore": integer
    }  
  
Fields  
---  
`threadsPerCore` |  `integer` The number of threads per physical core.  
  
### DataCacheConfig

Data cache configurations.

JSON representation  
---  
      
    
    {
      "dataCacheEnabled": boolean
    }  
  
Fields  
---  
`dataCacheEnabled` |  `boolean` Whether data cache is enabled for the instance.  
  
### ConnectionPoolConfig

The managed connection pooling configuration.

JSON representation  
---  
      
    
    {
      "flags": [
        {
          object ([ConnectionPoolFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionPoolFlags))
        }
      ],
      "connectionPoolingEnabled": boolean
    }  
  
Fields  
---  
`flags[]` |  `object (`[ConnectionPoolFlags](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionPoolFlags)`)` Optional. instances.list of connection pool configuration flags.  
`connectionPoolingEnabled` |  `boolean` Whether managed connection pooling is enabled.  
  
### ConnectionPoolFlags

Connection pool flags for Cloud SQL instances managed connection pool configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "value": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the flag.  
`value` |  `string` Required. The value of the flag. Boolean flags are set to `on` for true and `off` for false. This field must be omitted if the flag doesn't take a value.  
  
### FinalBackupConfig

Config used to determine the final backup settings for the instance.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "retentionDays": integer
    }  
  
Fields  
---  
`enabled` |  `boolean` Whether the final backup is enabled for the instance.  
`retentionDays` |  `integer` The number of days to retain the final backup after the instance deletion. The final backup will be purged at (time_of_instance_deletion + retentionDays).  
  
### ReadPoolAutoScaleConfig

The read pool auto-scale configuration.

JSON representation  
---  
      
    
    {
      "targetMetrics": [
        {
          object ([TargetMetric](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TargetMetric))
        }
      ],
      "enabled": boolean,
      "minNodeCount": integer,
      "maxNodeCount": integer,
      "disableScaleIn": boolean,
      "scaleInCooldownSeconds": integer,
      "scaleOutCooldownSeconds": integer
    }  
  
Fields  
---  
`targetMetrics[]` |  `object (`[TargetMetric](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TargetMetric)`)` Optional. Target metrics for read pool auto scaling.  
`enabled` |  `boolean` Indicates whether read pool auto scaling is enabled.  
`minNodeCount` |  `integer` Minimum number of read pool nodes to be maintained.  
`maxNodeCount` |  `integer` Maximum number of read pool nodes to be maintained.  
`disableScaleIn` |  `boolean` Indicates whether read pool auto scaling supports scale in operations (removing nodes).  
`scaleInCooldownSeconds` |  `integer` The cooldown period for scale in operations.  
`scaleOutCooldownSeconds` |  `integer` The cooldown period for scale out operations.  
  
### TargetMetric

Target metric for read pool auto scaling.

JSON representation  
---  
      
    
    {
      "metric": string,
      "targetValue": number
    }  
  
Fields  
---  
`metric` |  `string` The metric name to be used for auto scaling.  
`targetValue` |  `number` The target value for the metric.  
  
### DataApiAccess

instances.executeSql API's access to the instance.

Enums  
---  
`DATA_API_ACCESS_UNSPECIFIED` | Unspecified, effectively the same as `DISALLOW_DATA_API`.  
`DISALLOW_DATA_API` | Disallow using instances.executeSql API to connect to the instance.  
`ALLOW_DATA_API` | Allow using instances.executeSql API to connect to the instance. For private IP instances, this allows authorized users to access the instance from the public internet using instances.executeSql API.  
  
### IpMapping

Database instance IP mapping

JSON representation  
---  
      
    
    {
      "type": enum ([SqlIpAddressType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlIpAddressType)),
      "ipAddress": string,
      "timeToRetire": string
    }  
  
Fields  
---  
`type` |  `enum (`[SqlIpAddressType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlIpAddressType)`)` The type of this IP address. A `PRIMARY` address is a public address that can accept incoming connections. A `PRIVATE` address is a private address that can accept incoming connections. An `OUTGOING` address is the source address of connections originating from the instance, if supported.  
`ipAddress` |  `string` The IP address assigned.  
`timeToRetire` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The due time for this IP to be retired in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. This field is only available when the IP is scheduled to be retired.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SqlIpAddressType

Enums  
---  
`SQL_IP_ADDRESS_TYPE_UNSPECIFIED` | This is an unknown IP address type.  
`PRIMARY` | IP address the customer is supposed to connect to. Usually this is the load balancer's IP address  
`OUTGOING` | Source IP address of the connection a read replica establishes to its external primary instance. This IP address can be allowlisted by the customer in case it has a firewall that filters incoming connection to its on premises primary instance.  
`PRIVATE` | Private IP used when using private IPs and network peering.  
`MIGRATED_1ST_GEN` | V1 IP of a migrated instance. We want the user to decommission this IP as soon as the migration is complete. Note: V1 instances with V1 ip addresses will be counted as PRIMARY.  
  
### SqlInstanceType

Enums  
---  
`SQL_INSTANCE_TYPE_UNSPECIFIED` | This is an unknown Cloud SQL instance type.  
`CLOUD_SQL_INSTANCE` | A regular Cloud SQL instance that is not replicating from a primary instance.  
`ON_PREMISES_INSTANCE` | An instance running on the customer's premises that is not managed by Cloud SQL.  
`READ_REPLICA_INSTANCE` | A Cloud SQL instance acting as a read-replica.  
`READ_POOL_INSTANCE` | A Cloud SQL read pool.  
`GREEN_INSTANCE` | A Cloud SQL instance acting as a Blue-Green deployment target primary. (MySQL only)  
  
### OnPremisesConfiguration

On-premises instance configuration.

JSON representation  
---  
      
    
    {
      "hostPort": string,
      "kind": string,
      "username": string,
      "password": string,
      "caCertificate": string,
      "clientCertificate": string,
      "clientKey": string,
      "dumpFilePath": string,
      "sourceInstance": {
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference))
      },
      "selectedObjects": [
        {
          object ([SelectedObjects](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SelectedObjects))
        }
      ],
      "sslOption": enum ([SslOption](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SslOption)),
      "dmsManaged": boolean
    }  
  
Fields  
---  
`hostPort` |  `string` The host and port of the on-premises instance in host:port format  
`kind` |  `string` This is always `sql#onPremisesConfiguration`.  
`username` |  `string` The username for connecting to on-premises instance.  
`password` |  `string` The password for connecting to on-premises instance.  
`caCertificate` |  `string` PEM representation of the trusted CA's x509 certificate.  
`clientCertificate` |  `string` PEM representation of the replica's x509 certificate.  
`clientKey` |  `string` PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate.  
`dumpFilePath` |  `string` The dump file to create the Cloud SQL replica.  
`sourceInstance` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference)`)` The reference to Cloud SQL instance if the source is Cloud SQL.  
`selectedObjects[]` |  `object (`[SelectedObjects](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SelectedObjects)`)` Optional. A list of objects that the user selects for replication from an external source instance.  
`sslOption` |  `enum (`[SslOption](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SslOption)`)` Optional. SslOption for replica connection to the on-premises source.  
`dmsManaged` |  `boolean` Output only. Indicates whether the resource is managed by Database Migration Service.  
  
### InstanceReference

Reference to another Cloud SQL instance.

JSON representation  
---  
      
    
    {
      "name": string,
      "region": string,
      "project": string
    }  
  
Fields  
---  
`name` |  `string` The name of the Cloud SQL instance being referenced. This does not include the project ID.  
`region` |  `string` The region of the Cloud SQL instance being referenced.  
`project` |  `string` The project ID of the Cloud SQL instance being referenced. The default is the same project ID as the instance references it.  
  
### SelectedObjects

A list of objects that the user selects for replication from an external source instance.

JSON representation  
---  
      
    
    {
      "database": string
    }  
  
Fields  
---  
`database` |  `string` Required. The name of the database to migrate.  
  
### SslOption

SslOption defines the SSL mode to be used for replica connection to the on-premises source.

Enums  
---  
`SSL_OPTION_UNSPECIFIED` | Unknown SSL option i.e. SSL option not specified by user.  
`DISABLE` | SSL is disabled for replica connection to the on-premises source.  
`REQUIRE` | SSL is required for replica connection to the on-premises source.  
`VERIFY_CA` | Verify CA is required for replica connection to the on-premises source.  
  
### ReplicaConfiguration

Read-replica configuration for connecting to the primary instance.

JSON representation  
---  
      
    
    {
      "kind": string,
      "mysqlReplicaConfiguration": {
        object ([MySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.MySqlReplicaConfiguration))
      },
      "failoverTarget": boolean,
      "cascadableReplica": boolean
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#replicaConfiguration`.  
`mysqlReplicaConfiguration` |  `object (`[MySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.MySqlReplicaConfiguration)`)` MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory.  
`failoverTarget` |  `boolean` Specifies if the replica is the failover target. If the field is set to `true` the replica will be designated as a failover replica. In case the primary instance fails, the replica instance will be promoted as the new primary instance. Only one replica can be specified as failover target, and the replica has to be in different zone with the primary instance.  
`cascadableReplica` |  `boolean` Optional. Specifies if a SQL Server replica is a cascadable replica. A cascadable replica is a SQL Server cross region replica that supports replica(s) under it.  
  
### MySqlReplicaConfiguration

Read-replica configuration specific to MySQL databases.

JSON representation  
---  
      
    
    {
      "dumpFilePath": string,
      "username": string,
      "password": string,
      "connectRetryInterval": integer,
      "masterHeartbeatPeriod": string,
      "caCertificate": string,
      "clientCertificate": string,
      "clientKey": string,
      "sslCipher": string,
      "verifyServerCertificate": boolean,
      "kind": string
    }  
  
Fields  
---  
`dumpFilePath` |  `string` Path to a SQL dump file in Google Cloud Storage from which the replica instance is to be created. The URI is in the form gs://bucketName/fileName. Compressed gzip files (.gz) are also supported. Dumps have the binlog co-ordinates from which replication begins. This can be accomplished by setting --master-data to 1 when using mysqldump.  
`username` |  `string` The username for the replication connection.  
`password` |  `string` The password for the replication connection.  
`connectRetryInterval` |  `integer` Seconds to wait between connect retries. MySQL's default is 60 seconds.  
`masterHeartbeatPeriod` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` Interval in milliseconds between replication heartbeats.  
`caCertificate` |  `string` PEM representation of the trusted CA's x509 certificate.  
`clientCertificate` |  `string` PEM representation of the replica's x509 certificate.  
`clientKey` |  `string` PEM representation of the replica's private key. The corresponding public key is encoded in the client's certificate.  
`sslCipher` |  `string` A list of permissible ciphers to use for SSL encryption.  
`verifyServerCertificate` |  `boolean` Whether or not to check the primary instance's Common Name value in the certificate that it sends during the SSL handshake.  
`kind` |  `string` This is always `sql#mysqlReplicaConfiguration`.  
  
### SqlBackendType

Enums  
---  
`SQL_BACKEND_TYPE_UNSPECIFIED` | This is an unknown backend type for instance.  
`FIRST_GEN` | V1 speckle instance.This item is deprecated!  
`SECOND_GEN` | V2 speckle instance.  
`EXTERNAL` | On premises instance.  
  
### SqlSuspensionReason

The suspension reason of the database instance if the state is SUSPENDED.

Enums  
---  
`SQL_SUSPENSION_REASON_UNSPECIFIED` | This is an unknown suspension reason.  
`BILLING_ISSUE` | The instance is suspended due to billing issues (for example:, account issue)  
`LEGAL_ISSUE` | The instance is suspended due to illegal content (for example:, child pornography, copyrighted material, etc.).  
`OPERATIONAL_ISSUE` | The instance is causing operational issues (for example:, causing the database to crash).  
`KMS_KEY_ISSUE` | The KMS key used by the instance is either revoked or denied access to  
  
### SqlScheduledMaintenance

Any scheduled maintenance for this instance.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "canDefer": boolean,
      "canReschedule": boolean,
      "scheduleDeadlineTime": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`canDefer  
**(deprecated)**` |  `boolean` This item is deprecated!  
`canReschedule` |  `boolean` If the scheduled maintenance can be rescheduled.  
`scheduleDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Maintenance cannot be rescheduled to start beyond this deadline.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SqlOutOfDiskReport

This message wraps up the information written by out-of-disk detection job.

JSON representation  
---  
      
    
    {
      "sqlOutOfDiskState": enum ([SqlOutOfDiskState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlOutOfDiskState)),
      "sqlMinRecommendedIncreaseSizeGb": integer
    }  
  
Fields  
---  
`sqlOutOfDiskState` |  `enum (`[SqlOutOfDiskState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlOutOfDiskState)`)` This field represents the state generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job  
`sqlMinRecommendedIncreaseSizeGb` |  `integer` The minimum recommended increase size in GigaBytes This field is consumed by the frontend * Writers: * the proactive database wellness job for OOD. * Readers:  
  
### SqlOutOfDiskState

This enum lists all possible states regarding out-of-disk issues.

Enums  
---  
`SQL_OUT_OF_DISK_STATE_UNSPECIFIED` | Unspecified state  
`NORMAL` | The instance has plenty space on data disk  
`SOFT_SHUTDOWN` | Data disk is almost used up. It is shutdown to prevent data corruption.  
  
### AvailableDatabaseVersion

An available database version. It can be a major or a minor version.

JSON representation  
---  
      
    
    {
      "majorVersion": string,
      "name": string,
      "displayName": string
    }  
  
Fields  
---  
`majorVersion` |  `string` The version's major version name.  
`name` |  `string` The database version name. For MySQL 8.0, this string provides the database major and minor version.  
`displayName` |  `string` The database version's display name.  
  
### SqlNetworkArchitecture

The SQL network architecture for the instance.

Enums  
---  
`SQL_NETWORK_ARCHITECTURE_UNSPECIFIED` |   
`NEW_NETWORK_ARCHITECTURE` | The instance uses the new network architecture.  
`OLD_NETWORK_ARCHITECTURE` | The instance uses the old network architecture.  
  
### ReplicationCluster

A primary instance and disaster recovery (DR) replica pair. A DR replica is a cross-region replica that you designate for failover in the event that the primary instance has regional failure. Applicable to MySQL and PostgreSQL.

JSON representation  
---  
      
    
    {
      "psaWriteEndpoint": string,
      "failoverDrReplicaName": string,
      "drReplica": boolean
    }  
  
Fields  
---  
`psaWriteEndpoint` |  `string` Output only. If set, this field indicates this instance has a private service access (PSA) DNS endpoint that is pointing to the primary instance of the cluster. If this instance is the primary, then the DNS endpoint points to this instance. After a switchover or replica failover operation, this DNS endpoint points to the promoted instance. This is a read-only field, returned to the user as information. This field can exist even if a standalone instance doesn't have a DR replica yet or the DR replica is deleted.  
`failoverDrReplicaName` |  `string` Optional. If the instance is a primary instance, then this field identifies the disaster recovery (DR) replica. A DR replica is an optional configuration for Enterprise Plus edition instances. If the instance is a read replica, then the field is not set. Set this field to a replica name to designate a DR replica for a primary instance. Remove the replica name to remove the DR replica designation.  
`drReplica` |  `boolean` Output only. Read-only field that indicates whether the replica is a DR replica. This field is not set if the instance is a primary instance.  
  
### GeminiInstanceConfig

Gemini instance configuration.

JSON representation  
---  
      
    
    {
      "entitled": boolean,
      "googleVacuumMgmtEnabled": boolean,
      "oomSessionCancelEnabled": boolean,
      "activeQueryEnabled": boolean,
      "indexAdvisorEnabled": boolean,
      "flagRecommenderEnabled": boolean
    }  
  
Fields  
---  
`entitled` |  `boolean` Output only. Whether Gemini is enabled.  
`googleVacuumMgmtEnabled` |  `boolean` Output only. Whether the vacuum management is enabled.  
`oomSessionCancelEnabled` |  `boolean` Output only. Whether canceling the out-of-memory (OOM) session is enabled.  
`activeQueryEnabled` |  `boolean` Output only. Whether the active query is enabled.  
`indexAdvisorEnabled` |  `boolean` Output only. Whether the index advisor is enabled.  
`flagRecommenderEnabled` |  `boolean` Output only. Whether the flag recommender is enabled.  
  
### PoolNodeConfig

Details of a single read pool node of a read pool.

JSON representation  
---  
      
    
    {
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpMapping))
        }
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsNameMapping))
        }
      ],
      "pscAutoConnections": [
        {
          object ([PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscAutoConnectionConfig))
        }
      ],
      "name": string,
      "gceZone": string,
      "dnsName": string,
      "state": enum ([SqlInstanceState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceState)),
      "pscServiceAttachmentLink": string
    }  
  
Fields  
---  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.IpMapping)`)` Output only. Mappings containing IP addresses that can be used to connect to the read pool node.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsNameMapping)`)` Output only. The list of DNS names used by this read pool node.  
`pscAutoConnections[]` |  `object (`[PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.PscAutoConnectionConfig)`)` Output only. The list of settings for requested automatically-setup Private Service Connect (PSC) consumer endpoints that can be used to connect to this read pool node.  
`name` |  `string` Output only. The name of the read pool node, to be used for retrieving metrics and logs.  
`gceZone` |  `string` Output only. The zone of the read pool node.  
`dnsName` |  `string` Output only. The DNS name of the read pool node.  
`state` |  `enum (`[SqlInstanceState](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SqlInstanceState)`)` Output only. The current state of the read pool node.  
`pscServiceAttachmentLink` |  `string` Output only. The Private Service Connect (PSC) service attachment of the read pool node.  
  
### DnsNameMapping

DNS metadata.

JSON representation  
---  
      
    
    {
      "name": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionType)),
      "dnsScope": enum ([DnsScope](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsScope)),
      "recordManager": enum ([RecordManager](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.RecordManager))
    }  
  
Fields  
---  
`name` |  `string` Output only. The DNS name.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.ConnectionType)`)` Output only. The connection type of the DNS name.  
`dnsScope` |  `enum (`[DnsScope](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.DnsScope)`)` Output only. The scope that the DNS name applies to.  
`recordManager` |  `enum (`[RecordManager](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.RecordManager)`)` Output only. The manager for this DNS record.  
  
### ConnectionType

The connection type of the DNS name.

Enums  
---  
`CONNECTION_TYPE_UNSPECIFIED` | Unknown connection type.  
`PUBLIC` | Public IP.  
`PRIVATE_SERVICES_ACCESS` | Private services access (private IP).  
`PRIVATE_SERVICE_CONNECT` | Private Service Connect.  
  
### DnsScope

The scope that the DNS name applies to.

Enums  
---  
`DNS_SCOPE_UNSPECIFIED` | DNS scope not set. This value should not be used.  
`INSTANCE` | Indicates an instance-level DNS name.  
`CLUSTER` | Indicates a cluster-level DNS name.  
  
### RecordManager

The system responsible for managing the DNS record.

Enums  
---  
`RECORD_MANAGER_UNSPECIFIED` | Record manager not set. This value should not be used.  
`CUSTOMER` | The record may be managed by the customer. It is not automatically managed by Cloud SQL automation.  
`CLOUD_SQL_AUTOMATION` | The record is managed by Cloud SQL, which will create, update, and delete the DNS records for the zone automatically when the Cloud SQL database instance is created or updated.  
  
### BlueGreenDeploymentInfo

Blue-green deployment metadata for a database instance. In a blue-green deployment, we maintain two environments, one of which is live. This message contains details about the blue-green deployment.

JSON representation  
---  
      
    
    {
      "deploymentId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "source": {
        object ([SourceRole](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SourceRole))
      },
      "target": {
        object ([TargetRole](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TargetRole))
      }
      // End of mutually exclusive fields.
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.State))
    }  
  
Fields  
---  
`deploymentId` |  `string` Output only. The resource ID of the blue-green deployment.  
The role of the instance in the blue-green deployment. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`source` |  `object (`[SourceRole](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.SourceRole)`)` Output only. The source instance for the Blue-Green deployment.  
`target` |  `object (`[TargetRole](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.TargetRole)`)` Output only. The target instance for the Blue-Green deployment.  
End of mutually exclusive fields.  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.State)`)` Output only. The current state of blue-green-deployment for UI tags  
  
### SourceRole

The source instance for the Blue-Green deployment.

JSON representation  
---  
      
    
    {
      "targetId": {
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference))
      }
    }  
  
Fields  
---  
`targetId` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference)`)` Output only. The target instance paired with this source instance in a blue-green deployment.  
  
### TargetRole

The target instance for the Blue-Green deployment.

JSON representation  
---  
      
    
    {
      "sourceId": {
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference))
      }
    }  
  
Fields  
---  
`sourceId` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances#DatabaseInstance.InstanceReference)`)` Output only. The source instance paired with this target instance in a blue-green deployment.  
  
### State

The state of blue-green-deployment for UI tags

Enums  
---  
`STATE_UNSPECIFIED` | The state of the deployment is unknown.  
`PRE_SWITCHOVER` | The deployment is pre-switchover.  
`POST_SWITCHOVER` | The deployment is post-switchover.  
  
## Methods  
  
---  
  
### `[ListServerCertificates](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/ListServerCertificates)`

|  Lists all versions of server certificates and certificate authorities (CAs) for the specified instance.  
  
### `[RotateServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/RotateServerCertificate)`

|  Rotates the server certificate version to one previously added with the addServerCertificate method.  
  
### `[addServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/addServerCa)`

|  Add a new trusted Certificate Authority (CA) version for the specified instance.  
  
### `[addServerCertificate](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/addServerCertificate)`

|  Add a new trusted server certificate version for the specified instance using Certificate Authority Service (CAS) server CA.  
  
### `[clone](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/clone)`

|  Creates a Cloud SQL instance as a clone of the source instance.  
  
### `[delete](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/delete)`

|  Deletes a Cloud SQL instance.  
  
### `[demote](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demote)`

|  Demotes an existing standalone instance to be a Cloud SQL read replica for an external database server.  
  
### `[demoteMaster](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/demoteMaster)`

|  Demotes the stand-alone instance to be a Cloud SQL read replica for an external database server.  
  
### `[executeSql](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/executeSql)`

|  Execute SQL statements.  
  
### `[export](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/export)`

|  Exports data from a Cloud SQL instance to a Cloud Storage bucket as a SQL dump or CSV file.  
  
### `[failover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/failover)`

|  Initiates a manual failover of a high availability (HA) primary instance to a standby instance, which becomes the primary instance.  
  
### `[get](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/get)`

|  Retrieves a resource containing information about a Cloud SQL instance.  
  
### `[import](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/import)`

|  Imports data into a Cloud SQL instance from a SQL dump or CSV file in Cloud Storage.  
  
### `[insert](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/insert)`

|  Creates a new Cloud SQL instance.  
  
### `[list](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/list)`

|  Lists instances under a given project.  
  
### `[listServerCas](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/listServerCas)`

|  Lists all of the trusted Certificate Authorities (CAs) for the specified instance.  
  
### `[patch](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/patch)`

|  Partially updates settings of a Cloud SQL instance by merging the request with the current configuration.  
  
### `[pointInTimeRestore](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/pointInTimeRestore)`

|  Point in time restore for an instance managed by Google Cloud Backup and Disaster Recovery.  
  
### `[preCheckMajorVersionUpgrade](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/preCheckMajorVersionUpgrade)`

|  Execute MVU Pre-checks  
  
### `[promoteReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/promoteReplica)`

|  Promotes the read replica instance to be an independent Cloud SQL primary instance.  
  
### `[reencrypt](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/reencrypt)`

|  Reencrypt CMEK instance with latest key version.  
  
### `[resetSslConfig](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/resetSslConfig)`

|  Deletes all client certificates and generates a new server SSL certificate for the instance.  
  
### `[restart](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/restart)`

|  Restarts a Cloud SQL instance.  
  
### `[restoreBackup](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/restoreBackup)`

|  Restores a backup of a Cloud SQL instance.  
  
### `[rotateServerCa](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/rotateServerCa)`

|  Rotates the server certificate to one signed by the Certificate Authority (CA) version previously added with the addServerCA method.  
  
### `[startReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/startReplica)`

|  Starts the replication in the read replica instance.  
  
### `[stopReplica](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/stopReplica)`

|  Stops the replication in the read replica instance.  
  
### `[switchover](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/switchover)`

|  Switches over from the primary instance to the DR replica instance.  
  
### `[truncateLog](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/truncateLog)`

|  Truncate MySQL general and slow query log tables MySQL only.  
  
### `[update](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/instances/update)`

|  Updates settings of a Cloud SQL instance.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
