---
url: https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance/
title: MCP Tools Reference: cloud-sql \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:57:59.502615+00:00
---

# MCP Tools Reference: cloud-sql  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  MCP Tools Reference: cloud-sql Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_instance`

Get the details of a Cloud SQL instance.

The following code sample shows how to use `curl` to call the `get_instance` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://sqladmin.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_instance",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Instance get request.

### SqlInstancesGetRequest

JSON representation  
---  
      
    
    {
      "instance": string,
      "project": string,
      "location": string
    }  
  
Fields  
---  
`instance` |  `string` Required. Database instance ID. This does not include the project ID.  
`project` |  `string` Required. Project ID of the project that contains the instance.  
`location` |  `string` Optional. Region of the Cloud SQL instance.  
  
## Output Schema

A Cloud SQL instance resource.

### DatabaseInstance

JSON representation  
---  
      
    
    {
      "kind": string,
      "state": enum ([SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState)),
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlDatabaseVersion)),
      "settings": {
        object ([Settings](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Settings))
      },
      "etag": string,
      "failoverReplica": {
        object ([SqlFailoverReplica](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlFailoverReplica))
      },
      "masterInstanceName": string,
      "replicaNames": [
        string
      ],
      "maxDiskSize": string,
      "currentDiskSize": string,
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpMapping))
        }
      ],
      "serverCaCert": {
        object ([SslCert](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslCert))
      },
      "instanceType": enum ([SqlInstanceType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlInstanceType)),
      "project": string,
      "ipv6Address": string,
      "serviceAccountEmailAddress": string,
      "onPremisesConfiguration": {
        object ([OnPremisesConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.OnPremisesConfiguration))
      },
      "replicaConfiguration": {
        object ([ReplicaConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReplicaConfiguration))
      },
      "backendType": enum ([SqlBackendType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlBackendType)),
      "selfLink": string,
      "suspensionReason": [
        enum ([SqlSuspensionReason](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlSuspensionReason))
      ],
      "connectionName": string,
      "name": string,
      "region": string,
      "gceZone": string,
      "secondaryGceZone": string,
      "diskEncryptionConfiguration": {
        object ([DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DiskEncryptionConfiguration))
      },
      "diskEncryptionStatus": {
        object ([DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DiskEncryptionStatus))
      },
      "rootPassword": string,
      "scheduledMaintenance": {
        object ([SqlScheduledMaintenance](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlScheduledMaintenance))
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
          object ([AvailableDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AvailableDatabaseVersion))
        }
      ],
      "replicationCluster": {
        object ([ReplicationCluster](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReplicationCluster))
      },
      "satisfiesPzi": boolean,
      "tags": {
        string: string,
        ...
      },
      "nodes": [
        {
          object ([PoolNodeConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PoolNodeConfig))
        }
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsNameMapping))
        }
      ],
      "databaseCenterIntegrationEnabled": boolean,
    
      // Union field _out_of_disk_report can be only one of the following:
      "outOfDiskReport": {
        object ([SqlOutOfDiskReport](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlOutOfDiskReport))
      }
      // End of list of possible types for union field _out_of_disk_report.
    
      // Union field _sql_network_architecture can be only one of the following:
      "sqlNetworkArchitecture": enum ([SqlNetworkArchitecture](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlNetworkArchitecture))
      // End of list of possible types for union field _sql_network_architecture.
    
      // Union field _psc_service_attachment_link can be only one of the following:
      "pscServiceAttachmentLink": string
      // End of list of possible types for union field _psc_service_attachment_link.
    
      // Union field _dns_name can be only one of the following:
      "dnsName": string
      // End of list of possible types for union field _dns_name.
    
      // Union field _primary_dns_name can be only one of the following:
      "primaryDnsName": string
      // End of list of possible types for union field _primary_dns_name.
    
      // Union field _write_endpoint can be only one of the following:
      "writeEndpoint": string
      // End of list of possible types for union field _write_endpoint.
    
      // Union field _gemini_config can be only one of the following:
      "geminiConfig": {
        object ([GeminiInstanceConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.GeminiInstanceConfig))
      }
      // End of list of possible types for union field _gemini_config.
    
      // Union field _switch_transaction_logs_to_cloud_storage_enabled can be only
      // one of the following:
      "switchTransactionLogsToCloudStorageEnabled": boolean
      // End of list of possible types for union field
      // _switch_transaction_logs_to_cloud_storage_enabled.
    
      // Union field _include_replicas_for_major_version_upgrade can be only one of
      // the following:
      "includeReplicasForMajorVersionUpgrade": boolean
      // End of list of possible types for union field
      // _include_replicas_for_major_version_upgrade.
    
      // Union field _skip_precheck can be only one of the following:
      "skipPrecheck": boolean
      // End of list of possible types for union field _skip_precheck.
    
      // Union field _node_count can be only one of the following:
      "nodeCount": integer
      // End of list of possible types for union field _node_count.
    
      // Union field _deployment_info can be only one of the following:
      "deploymentInfo": {
        object ([BlueGreenDeploymentInfo](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BlueGreenDeploymentInfo))
      }
      // End of list of possible types for union field _deployment_info.
    
      // Union field _database_center_integration can be only one of the following:
      "databaseCenterIntegration": enum ([DatabaseCenterIntegration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DatabaseCenterIntegration))
      // End of list of possible types for union field _database_center_integration.
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#instance`.  
`state` |  `enum (`[SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState)`)` The current serving state of the Cloud SQL instance.  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlDatabaseVersion)`)` The database engine type and version. The `databaseVersion` field cannot be changed after instance creation.  
`settings` |  `object (`[Settings](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Settings)`)` The user settings.  
`etag` |  `string` This field is deprecated and will be removed from a future version of the API. Use the `settings.settingsVersion` field instead.  
`failoverReplica` |  `object (`[SqlFailoverReplica](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlFailoverReplica)`)` The name and status of the failover replica.  
`masterInstanceName` |  `string` The name of the instance which will act as primary in the replication setup.  
`replicaNames[]` |  `string` The replicas of the instance.  
`maxDiskSize  
**(deprecated)**` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The maximum disk size of the instance in bytes.  
`currentDiskSize  
**(deprecated)**` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` This item is deprecated!The current disk usage of the instance in bytes. This property has been deprecated. Use the "cloudsql.googleapis.com/database/disk/bytes_used" metric in Cloud Monitoring API instead. Please see [this announcement](https://groups.google.com/d/msg/google-cloud-sql-announce/I_7-F9EBhT0/BtvFtdFeAgAJ) for details.  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpMapping)`)` The assigned IP addresses for the instance.  
`serverCaCert` |  `object (`[SslCert](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslCert)`)` SSL configuration.  
`instanceType` |  `enum (`[SqlInstanceType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlInstanceType)`)` The instance type.  
`project` |  `string` The project ID of the project containing the Cloud SQL instance. The Google apps domain is prefixed if applicable.  
`ipv6Address  
**(deprecated)**` |  `string` This item is deprecated!The IPv6 address assigned to the instance. (Deprecated) This property was applicable only to First Generation instances.  
`serviceAccountEmailAddress` |  `string` The service account email address assigned to the instance.\This property is read-only.  
`onPremisesConfiguration` |  `object (`[OnPremisesConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.OnPremisesConfiguration)`)` Configuration specific to on-premises instances.  
`replicaConfiguration` |  `object (`[ReplicaConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReplicaConfiguration)`)` Configuration specific to failover replicas and read replicas.  
`backendType` |  `enum (`[SqlBackendType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlBackendType)`)` The backend type. `SECOND_GEN`: Cloud SQL database instance. `EXTERNAL`: A database server that is not managed by Google.This property is read-only; use the `tier` property in the `settings` object to determine the database type.  
`selfLink` |  `string` The URI of this resource.  
`suspensionReason[]` |  `enum (`[SqlSuspensionReason](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlSuspensionReason)`)` If the instance state is SUSPENDED, the reason for the suspension.  
`connectionName` |  `string` Connection name of the Cloud SQL instance used in connection strings.  
`name` |  `string` Name of the Cloud SQL instance. This does not include the project ID.  
`region` |  `string` The geographical region of the Cloud SQL instance.It can be one of the [regions](https://cloud.google.com/sql/docs/mysql/locations#location-r) where Cloud SQL operates:For example, `asia-east1`, `europe-west1`, and `us-central1`. The default value is `us-central1`.  
`gceZone` |  `string` The Compute Engine zone that the instance is currently serving from. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary zone. WARNING: Changing this might restart the instance.  
`secondaryGceZone` |  `string` The Compute Engine zone that the failover instance is currently serving from for a regional instance. This value could be different from the zone that was specified when the instance was created if the instance has failed over to its secondary/failover zone.  
`diskEncryptionConfiguration` |  `object (`[DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DiskEncryptionConfiguration)`)` Disk encryption configuration specific to an instance.  
`diskEncryptionStatus` |  `object (`[DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DiskEncryptionStatus)`)` Disk encryption status specific to an instance.  
`rootPassword` |  `string` Initial root password. Use only on creation. You must set root passwords before you can connect to PostgreSQL instances.  
`scheduledMaintenance` |  `object (`[SqlScheduledMaintenance](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlScheduledMaintenance)`)` The start time of any upcoming scheduled maintenance for this instance.  
`satisfiesPzs` |  `boolean` This status indicates whether the instance satisfies PZS.The status is reserved for future use.  
`databaseInstalledVersion` |  `string` Output only. Stores the current database version running on the instance including minor version such as `MYSQL_8_0_18`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the instance was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`availableMaintenanceVersions[]` |  `string` Output only. List all maintenance versions applicable on the instance  
`maintenanceVersion` |  `string` The current software version on the instance.  
`upgradableDatabaseVersions[]` |  `object (`[AvailableDatabaseVersion](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AvailableDatabaseVersion)`)` Output only. All database versions that are available for upgrade.  
`replicationCluster` |  `object (`[ReplicationCluster](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReplicationCluster)`)` Optional. A primary instance and disaster recovery (DR) replica pair. A DR replica is a cross-region replica that you designate for failover in the event that the primary instance experiences regional failure. Applicable to MySQL and PostgreSQL.  
`satisfiesPzi` |  `boolean` Output only. This status indicates whether the instance satisfies PZI.The status is reserved for future use.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys and tag values that are bound to this instance. You must represent each item in the map as: `"<tag-key-namespaced-name>" : "<tag-value-short-name>"`.For example, a single resource can have the following tags:
    
    
      "123/environment": "production",
      "123/costCenter": "marketing",
    

For more information on tag creation and management, see <https://cloud.google.com/resource-manager/docs/tags/tags-overview>.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`nodes[]` |  `object (`[PoolNodeConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PoolNodeConfig)`)` Output only. Entries containing information about each read pool node of the read pool.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsNameMapping)`)` Output only. The list of DNS names used by this instance.  
`databaseCenterIntegrationEnabled` |  `boolean` Optional. If true, instance metadata is sent to the Database Center. If false, instance metadata is not sent to the Database Center.  
Union field `_out_of_disk_report`.`_out_of_disk_report` can be only one of the following:  
`outOfDiskReport` |  `object (`[SqlOutOfDiskReport](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlOutOfDiskReport)`)` This field represents the report generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job  
Union field `_sql_network_architecture`.`_sql_network_architecture` can be only one of the following:  
`sqlNetworkArchitecture` |  `enum (`[SqlNetworkArchitecture](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlNetworkArchitecture)`)`  
Union field `_psc_service_attachment_link`.`_psc_service_attachment_link` can be only one of the following:  
`pscServiceAttachmentLink` |  `string` Output only. The link to service attachment of PSC instance.  
Union field `_dns_name`.`_dns_name` can be only one of the following:  
`dnsName` |  `string` Output only. The dns name of the instance.  
Union field `_primary_dns_name`.`_primary_dns_name` can be only one of the following:  
`primaryDnsName  
**(deprecated)**` |  `string` This item is deprecated!Output only. DEPRECATED: please use write_endpoint instead.  
Union field `_write_endpoint`.`_write_endpoint` can be only one of the following:  
`writeEndpoint` |  `string` Output only. The dns name of the primary instance in a replication group.  
Union field `_gemini_config`.`_gemini_config` can be only one of the following:  
`geminiConfig` |  `object (`[GeminiInstanceConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.GeminiInstanceConfig)`)` Gemini instance configuration.  
Union field `_switch_transaction_logs_to_cloud_storage_enabled`.`_switch_transaction_logs_to_cloud_storage_enabled` can be only one of the following:  
`switchTransactionLogsToCloudStorageEnabled` |  `boolean` Input only. Whether Cloud SQL is enabled to switch storing point-in-time recovery log files from a data disk to Cloud Storage.  
Union field `_include_replicas_for_major_version_upgrade`.`_include_replicas_for_major_version_upgrade` can be only one of the following:  
`includeReplicasForMajorVersionUpgrade` |  `boolean` Input only. Determines whether an in-place major version upgrade of replicas happens when an in-place major version upgrade of a primary instance is initiated.  
Union field `_skip_precheck`.`_skip_precheck` can be only one of the following:  
`skipPrecheck` |  `boolean` Optional. Input only. Determines whether the precheck step is skipped during a major version upgrade.  
Union field `_node_count`.`_node_count` can be only one of the following:  
`nodeCount` |  `integer` The number of read pool nodes in a read pool.  
Union field `_deployment_info`.`_deployment_info` can be only one of the following:  
`deploymentInfo` |  `object (`[BlueGreenDeploymentInfo](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BlueGreenDeploymentInfo)`)` Output only. Deployment info for the instance. This is set if the instance is currently part of any blue-green setup.  
Union field `_database_center_integration`.`_database_center_integration` can be only one of the following:  
`databaseCenterIntegration` |  `enum (`[DatabaseCenterIntegration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DatabaseCenterIntegration)`)` Optional. State of the Database Center integration for this instance. When unspecified, Database Center integration is enabled by default.  
  
### Settings

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
      "availabilityType": enum ([SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlAvailabilityType)),
      "pricingPlan": enum ([SqlPricingPlan](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlPricingPlan)),
      "replicationType": enum ([SqlReplicationType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlReplicationType)),
      "storageAutoResizeLimit": string,
      "activationPolicy": enum ([SqlActivationPolicy](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlActivationPolicy)),
      "ipConfiguration": {
        object ([IpConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpConfiguration))
      },
      "storageAutoResize": boolean,
      "locationPreference": {
        object ([LocationPreference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.LocationPreference))
      },
      "databaseFlags": [
        {
          object ([DatabaseFlags](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DatabaseFlags))
        }
      ],
      "dataDiskType": enum ([SqlDataDiskType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlDataDiskType)),
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.MaintenanceWindow))
      },
      "backupConfiguration": {
        object ([BackupConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupConfiguration))
      },
      "databaseReplicationEnabled": boolean,
      "crashSafeReplicationEnabled": boolean,
      "dataDiskSizeGb": string,
      "activeDirectoryConfig": {
        object ([SqlActiveDirectoryConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlActiveDirectoryConfig))
      },
      "collation": string,
      "denyMaintenancePeriods": [
        {
          object ([DenyMaintenancePeriod](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DenyMaintenancePeriod))
        }
      ],
      "insightsConfig": {
        object ([InsightsConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InsightsConfig))
      },
      "passwordValidationPolicy": {
        object ([PasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PasswordValidationPolicy))
      },
      "sqlServerAuditConfig": {
        object ([SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlServerAuditConfig))
      },
      "edition": enum ([Edition](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Edition)),
      "connectorEnforcement": enum ([ConnectorEnforcement](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectorEnforcement)),
      "deletionProtectionEnabled": boolean,
      "timeZone": string,
      "advancedMachineFeatures": {
        object ([AdvancedMachineFeatures](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AdvancedMachineFeatures))
      },
      "dataCacheConfig": {
        object ([DataCacheConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DataCacheConfig))
      },
      "replicationLagMaxSeconds": integer,
      "enableGoogleMlIntegration": boolean,
      "enableDataplexIntegration": boolean,
      "retainBackupsOnDelete": boolean,
      "acceleratedReplicaMode": boolean,
      "entraidConfig": {
        object ([SqlServerEntraIdConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlServerEntraIdConfig))
      },
      "performanceCaptureConfig": {
        object ([PerformanceCaptureConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PerformanceCaptureConfig))
      },
    
      // Union field _data_disk_provisioned_iops can be only one of the following:
      "dataDiskProvisionedIops": string
      // End of list of possible types for union field _data_disk_provisioned_iops.
    
      // Union field _data_disk_provisioned_throughput can be only one of the
      // following:
      "dataDiskProvisionedThroughput": string
      // End of list of possible types for union field
      // _data_disk_provisioned_throughput.
    
      // Union field _connection_pool_config can be only one of the following:
      "connectionPoolConfig": {
        object ([ConnectionPoolConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionPoolConfig))
      }
      // End of list of possible types for union field _connection_pool_config.
    
      // Union field _final_backup_config can be only one of the following:
      "finalBackupConfig": {
        object ([FinalBackupConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.FinalBackupConfig))
      }
      // End of list of possible types for union field _final_backup_config.
    
      // Union field _read_pool_auto_scale_config can be only one of the following:
      "readPoolAutoScaleConfig": {
        object ([ReadPoolAutoScaleConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReadPoolAutoScaleConfig))
      }
      // End of list of possible types for union field _read_pool_auto_scale_config.
    
      // Union field _auto_upgrade_enabled can be only one of the following:
      "autoUpgradeEnabled": boolean
      // End of list of possible types for union field _auto_upgrade_enabled.
    
      // Union field _data_api_access can be only one of the following:
      "dataApiAccess": enum ([DataApiAccess](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DataApiAccess))
      // End of list of possible types for union field _data_api_access.
    }  
  
Fields  
---  
`settingsVersion` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The version of instance settings. This is a required field for update method to make sure concurrent updates are handled properly. During update, use the most recent settingsVersion value for this instance and do not try to update this value.  
`authorizedGaeApplications[]  
**(deprecated)**` |  `string` This item is deprecated!The App Engine app IDs that can access this instance. (Deprecated) Applied to First Generation instances only.  
`tier` |  `string` The tier (or machine type) for this instance, for example `db-custom-1-3840`. WARNING: Changing this restarts the instance.  
`kind` |  `string` This is always `sql#settings`.  
`userLabels` |  `map (key: string, value: string)` User-provided labels, represented as a dictionary where each label is a single key value pair.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`availabilityType` |  `enum (`[SqlAvailabilityType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlAvailabilityType)`)` Availability type. Potential values: * `ZONAL`: The instance serves data from only one zone. Outages in that zone affect data accessibility. * `REGIONAL`: The instance can serve data from more than one zone in a region (it is highly available)./For more information, see [Overview of the High Availability Configuration](https://cloud.google.com/sql/docs/mysql/high-availability).  
`pricingPlan` |  `enum (`[SqlPricingPlan](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlPricingPlan)`)` The pricing plan for this instance. This can be either `PER_USE` or `PACKAGE`. Only `PER_USE` is supported for Second Generation instances.  
`replicationType  
**(deprecated)**` |  `enum (`[SqlReplicationType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlReplicationType)`)` This item is deprecated!The type of replication this instance uses. This can be either `ASYNCHRONOUS` or `SYNCHRONOUS`. (Deprecated) This property was only applicable to First Generation instances.  
`storageAutoResizeLimit` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The maximum size to which storage capacity can be automatically increased. The default value is 0, which specifies that there is no limit.  
`activationPolicy` |  `enum (`[SqlActivationPolicy](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlActivationPolicy)`)` The activation policy specifies when the instance is activated; it is applicable only when the instance state is RUNNABLE. Valid values: * `ALWAYS`: The instance is on, and remains so even in the absence of connection requests. * `NEVER`: The instance is off; it is not activated, even if a connection request arrives.  
`ipConfiguration` |  `object (`[IpConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpConfiguration)`)` The settings for IP Management. This allows to enable or disable the instance IP and manage which external networks can connect to the instance. The IPv4 address cannot be disabled for Second Generation instances.  
`storageAutoResize` |  `boolean` Configuration to increase storage size automatically. The default value is true.  
`locationPreference` |  `object (`[LocationPreference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.LocationPreference)`)` The location preference settings. This allows the instance to be located as near as possible to either an App Engine app or Compute Engine zone for better performance. App Engine co-location was only applicable to First Generation instances.  
`databaseFlags[]` |  `object (`[DatabaseFlags](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DatabaseFlags)`)` The database flags passed to the instance at startup.  
`dataDiskType` |  `enum (`[SqlDataDiskType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlDataDiskType)`)` The type of data disk: `PD_SSD` (default) or `PD_HDD`. Not used for First Generation instances.  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.MaintenanceWindow)`)` The maintenance window for this instance. This specifies when the instance can be restarted for maintenance purposes.  
`backupConfiguration` |  `object (`[BackupConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupConfiguration)`)` The daily backup configuration for the instance.  
`databaseReplicationEnabled` |  `boolean` Configuration specific to read replica instances. Indicates whether replication is enabled or not. WARNING: Changing this restarts the instance.  
`crashSafeReplicationEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Configuration specific to read replica instances. Indicates whether database flags for crash-safe replication are enabled. This property was only applicable to First Generation instances.  
`dataDiskSizeGb` |  `string ([Int64Value](https://developers.google.com/discovery/v1/type-format) format)` The size of data disk, in GB. The data disk size minimum is 10GB.  
`activeDirectoryConfig` |  `object (`[SqlActiveDirectoryConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlActiveDirectoryConfig)`)` Active Directory configuration, relevant only for Cloud SQL for SQL Server.  
`collation` |  `string` The name of server Instance collation.  
`denyMaintenancePeriods[]` |  `object (`[DenyMaintenancePeriod](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DenyMaintenancePeriod)`)` Deny maintenance periods  
`insightsConfig` |  `object (`[InsightsConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InsightsConfig)`)` Insights configuration, for now relevant only for Postgres.  
`passwordValidationPolicy` |  `object (`[PasswordValidationPolicy](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PasswordValidationPolicy)`)` The local user password validation policy of the instance for PostgreSQL and MySQL.  
`sqlServerAuditConfig` |  `object (`[SqlServerAuditConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlServerAuditConfig)`)` SQL Server specific audit configuration.  
`edition` |  `enum (`[Edition](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Edition)`)` Optional. The edition type of the Cloud SQL instance.  
`connectorEnforcement` |  `enum (`[ConnectorEnforcement](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectorEnforcement)`)` Specifies if connections must use Cloud SQL connectors. Option values include the following: `NOT_REQUIRED` (Cloud SQL instances can be connected without Cloud SQL Connectors) and `REQUIRED` (Only allow connections that use Cloud SQL Connectors).Note that using REQUIRED disables all existing authorized networks. If this field is not specified when creating a new instance, NOT_REQUIRED is used. If this field is not specified when patching or updating an existing instance, it is left unchanged in the instance.  
`deletionProtectionEnabled` |  `boolean` Configuration to protect against accidental instance deletion.  
`timeZone` |  `string` Server timezone, relevant only for Cloud SQL for SQL Server.  
`advancedMachineFeatures` |  `object (`[AdvancedMachineFeatures](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AdvancedMachineFeatures)`)` Specifies advanced machine configuration for the instances relevant only for SQL Server.  
`dataCacheConfig` |  `object (`[DataCacheConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DataCacheConfig)`)` Configuration for data cache.  
`replicationLagMaxSeconds` |  `integer` Optional. Configuration value for recreation of replica after certain replication lag  
`enableGoogleMlIntegration` |  `boolean` Optional. When this parameter is set to true, Cloud SQL instances can connect to Vertex AI to pass requests for real-time predictions and insights to the AI. The default value is false. This applies only to Cloud SQL for MySQL and Cloud SQL for PostgreSQL instances.  
`enableDataplexIntegration` |  `boolean` Optional. By default, Cloud SQL instances have schema extraction disabled for Dataplex. When this parameter is set to true, schema extraction for Dataplex on Cloud SQL instances is activated.  
`retainBackupsOnDelete` |  `boolean` Optional. When this parameter is set to true, Cloud SQL retains backups of the instance even after the instance is deleted. The ON_DEMAND backup will be retained until customer deletes the backup or the project. The AUTOMATED backup will be retained based on the backups retention setting.  
`acceleratedReplicaMode` |  `boolean` Optional. Whether the replica is in accelerated mode. This feature is in private preview and requires allowlisting to take effect.  
`entraidConfig` |  `object (`[SqlServerEntraIdConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlServerEntraIdConfig)`)` Optional. The Microsoft Entra ID configuration for the SQL Server instance.  
`performanceCaptureConfig` |  `object (`[PerformanceCaptureConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PerformanceCaptureConfig)`)` Optional. Configuration for Performance Capture, provides diagnostic metrics during high load situations.  
Union field `_data_disk_provisioned_iops`.`_data_disk_provisioned_iops` can be only one of the following:  
`dataDiskProvisionedIops` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned number of I/O operations per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
Union field `_data_disk_provisioned_throughput`.`_data_disk_provisioned_throughput` can be only one of the following:  
`dataDiskProvisionedThroughput` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Provisioned throughput measured in MiB per second for the data disk. This field is only used for hyperdisk-balanced disk types.  
Union field `_connection_pool_config`.`_connection_pool_config` can be only one of the following:  
`connectionPoolConfig` |  `object (`[ConnectionPoolConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionPoolConfig)`)` Optional. The managed connection pooling configuration for the instance.  
Union field `_final_backup_config`.`_final_backup_config` can be only one of the following:  
`finalBackupConfig` |  `object (`[FinalBackupConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.FinalBackupConfig)`)` Optional. The final backup configuration for the instance.  
Union field `_read_pool_auto_scale_config`.`_read_pool_auto_scale_config` can be only one of the following:  
`readPoolAutoScaleConfig` |  `object (`[ReadPoolAutoScaleConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ReadPoolAutoScaleConfig)`)` Optional. The read pool auto-scale configuration for the instance.  
Union field `_auto_upgrade_enabled`.`_auto_upgrade_enabled` can be only one of the following:  
`autoUpgradeEnabled` |  `boolean` Optional. Cloud SQL for MySQL auto-upgrade configuration. When this parameter is set to true, auto-upgrade is enabled for MySQL 8.0 minor versions. The MySQL version must be 8.0.35 or higher.  
Union field `_data_api_access`.`_data_api_access` can be only one of the following:  
`dataApiAccess` |  `enum (`[DataApiAccess](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DataApiAccess)`)` This parameter controls whether to allow using ExecuteSql API to connect to the instance. Not allowed by default.  
  
### Int64Value

JSON representation  
---  
      
    
    {
      "value": string
    }  
  
Fields  
---  
`value` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The int64 value.  
  
### UserLabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### IpConfiguration

JSON representation  
---  
      
    
    {
      "ipv4Enabled": boolean,
      "privateNetwork": string,
      "requireSsl": boolean,
      "authorizedNetworks": [
        {
          object ([AclEntry](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AclEntry))
        }
      ],
      "allocatedIpRange": string,
      "enablePrivatePathForGoogleCloudServices": boolean,
      "sslMode": enum ([SslMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslMode)),
      "customSubjectAlternativeNames": [
        string
      ],
    
      // Union field _psc_config can be only one of the following:
      "pscConfig": {
        object ([PscConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscConfig))
      }
      // End of list of possible types for union field _psc_config.
    
      // Union field _server_ca_mode can be only one of the following:
      "serverCaMode": enum ([CaMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.CaMode))
      // End of list of possible types for union field _server_ca_mode.
    
      // Union field _server_ca_pool can be only one of the following:
      "serverCaPool": string
      // End of list of possible types for union field _server_ca_pool.
    
      // Union field _server_certificate_rotation_mode can be only one of the
      // following:
      "serverCertificateRotationMode": enum ([ServerCertificateRotationMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ServerCertificateRotationMode))
      // End of list of possible types for union field
      // _server_certificate_rotation_mode.
    }  
  
Fields  
---  
`ipv4Enabled` |  `boolean` Whether the instance is assigned a public IP address or not.  
`privateNetwork` |  `string` The resource link for the VPC network from which the Cloud SQL instance is accessible for private IP. For example, `/projects/myProject/global/networks/default`. This setting can be updated, but it cannot be removed after it is set.  
`requireSsl` |  `boolean` Use `ssl_mode` instead.Whether SSL/TLS connections over IP are enforced. If set to false, then allow both non-SSL/non-TLS and SSL/TLS connections. For SSL/TLS connections, the client certificate won't be verified. If set to true, then only allow connections encrypted with SSL/TLS and with valid client certificates. If you want to enforce SSL/TLS without enforcing the requirement for valid client certificates, then use the `ssl_mode` flag instead of the `require_ssl` flag.  
`authorizedNetworks[]` |  `object (`[AclEntry](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AclEntry)`)` The list of external networks that are allowed to connect to the instance using the IP. In 'CIDR' notation, also known as 'slash' notation (for example: `157.197.200.0/24`).  
`allocatedIpRange` |  `string` The name of the allocated ip range for the private ip Cloud SQL instance. For example: "google-managed-services-default". If set, the instance ip will be created in the allocated range. The range name must comply with [RFC 1035](https://tools.ietf.org/html/rfc1035). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?.`  
`enablePrivatePathForGoogleCloudServices` |  `boolean` Controls connectivity to private IP instances from Google services, such as BigQuery.  
`sslMode` |  `enum (`[SslMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslMode)`)` Specify how SSL/TLS is enforced in database connections. If you must use the `require_ssl` flag for backward compatibility, then only the following value pairs are valid:For PostgreSQL and MySQL:

  * `ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `require_ssl=false`
  * `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=false`
  * `ssl_mode=TRUSTED_CLIENT_CERTIFICATE_REQUIRED` and `require_ssl=true`

For SQL Server:

  * `ssl_mode=ALLOW_UNENCRYPTED_AND_ENCRYPTED` and `require_ssl=false`
  * `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=true`

The value of `ssl_mode` has priority over the value of `require_ssl`.For example, for the pair `ssl_mode=ENCRYPTED_ONLY` and `require_ssl=false`, `ssl_mode=ENCRYPTED_ONLY` means accept only SSL connections, while `require_ssl=false` means accept both non-SSL and SSL connections. In this case, MySQL and PostgreSQL databases respect `ssl_mode` and accepts only SSL connections.  
`customSubjectAlternativeNames[]` |  `string` Optional. Custom Subject Alternative Name(SAN)s for a Cloud SQL instance.  
Union field `_psc_config`.`_psc_config` can be only one of the following:  
`pscConfig` |  `object (`[PscConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscConfig)`)` PSC settings for this instance.  
Union field `_server_ca_mode`.`_server_ca_mode` can be only one of the following:  
`serverCaMode` |  `enum (`[CaMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.CaMode)`)` Specify what type of CA is used for the server certificate.  
Union field `_server_ca_pool`.`_server_ca_pool` can be only one of the following:  
`serverCaPool` |  `string` Optional. The resource name of the server CA pool for an instance with `CUSTOMER_MANAGED_CAS_CA` as the `server_ca_mode`. Format: projects/{PROJECT}/locations/{REGION}/caPools/{CA_POOL_ID}  
Union field `_server_certificate_rotation_mode`.`_server_certificate_rotation_mode` can be only one of the following:  
`serverCertificateRotationMode` |  `enum (`[ServerCertificateRotationMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ServerCertificateRotationMode)`)` Optional. Controls the automatic server certificate rotation feature. This feature is disabled by default. When enabled, the server certificate will be automatically rotated during Cloud SQL scheduled maintenance or self-service maintenance updates up to six months before it expires. This setting can only be set if server_ca_mode is either GOOGLE_MANAGED_CAS_CA or CUSTOMER_MANAGED_CAS_CA.  
  
### BoolValue

JSON representation  
---  
      
    
    {
      "value": boolean
    }  
  
Fields  
---  
`value` |  `boolean` The bool value.  
  
### AclEntry

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
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### PscConfig

JSON representation  
---  
      
    
    {
      "allowedConsumerProjects": [
        string
      ],
      "pscAutoConnections": [
        {
          object ([PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscAutoConnectionConfig))
        }
      ],
      "networkAttachmentUri": string,
    
      // Union field _psc_enabled can be only one of the following:
      "pscEnabled": boolean
      // End of list of possible types for union field _psc_enabled.
    
      // Union field _psc_auto_dns_enabled can be only one of the following:
      "pscAutoDnsEnabled": boolean
      // End of list of possible types for union field _psc_auto_dns_enabled.
    
      // Union field _psc_write_endpoint_dns_enabled can be only one of the
      // following:
      "pscWriteEndpointDnsEnabled": boolean
      // End of list of possible types for union field
      // _psc_write_endpoint_dns_enabled.
    
      // Union field _psc_auto_connection_policy_enabled can be only one of the
      // following:
      "pscAutoConnectionPolicyEnabled": boolean
      // End of list of possible types for union field
      // _psc_auto_connection_policy_enabled.
    }  
  
Fields  
---  
`allowedConsumerProjects[]` |  `string` Optional. The list of consumer projects that are allow-listed for PSC connections to this instance. This instance can be connected to with PSC from any network in these projects.Each consumer project in this list may be represented by a project number (numeric) or by a project id (alphanumeric).  
`pscAutoConnections[]` |  `object (`[PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscAutoConnectionConfig)`)` Optional. The list of settings for requested Private Service Connect consumer endpoints that can be used to connect to this Cloud SQL instance.  
`networkAttachmentUri` |  `string` Optional. The network attachment of the consumer network that the Private Service Connect enabled Cloud SQL instance is authorized to connect using the PSC interface. format: projects/PROJECT/regions/REGION/networkAttachments/ID  
Union field `_psc_enabled`.`_psc_enabled` can be only one of the following:  
`pscEnabled` |  `boolean` Whether PSC connectivity is enabled for this instance.  
Union field `_psc_auto_dns_enabled`.`_psc_auto_dns_enabled` can be only one of the following:  
`pscAutoDnsEnabled` |  `boolean` Optional. Indicates whether Private Service Connect DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal DNS record across all networks configured with Private Service Connect auto-connections. This will default to true for new instances when Private Service Connect is enabled.  
Union field `_psc_write_endpoint_dns_enabled`.`_psc_write_endpoint_dns_enabled` can be only one of the following:  
`pscWriteEndpointDnsEnabled` |  `boolean` Optional. Indicates whether Private Service Connect write endpoint DNS automation is enabled for this instance. When enabled, Cloud SQL provisions a universal global DNS record across all networks configured with Private Service Connect auto-connections that points to the cluster primary instance. This feature is only supported for Enterprise Plus edition. This will default to true for new Enterprise Plus instances when `psc_auto_dns_enabled` is enabled.  
Union field `_psc_auto_connection_policy_enabled`.`_psc_auto_connection_policy_enabled` can be only one of the following:  
`pscAutoConnectionPolicyEnabled` |  `boolean` Optional. Whether to set up the PSC service connection policy automatically.  
  
### PscAutoConnectionConfig

JSON representation  
---  
      
    
    {
      "consumerProject": string,
      "consumerNetwork": string,
    
      // Union field _ip_address can be only one of the following:
      "ipAddress": string
      // End of list of possible types for union field _ip_address.
    
      // Union field _status can be only one of the following:
      "status": string
      // End of list of possible types for union field _status.
    
      // Union field _consumer_network_status can be only one of the following:
      "consumerNetworkStatus": string
      // End of list of possible types for union field _consumer_network_status.
    
      // Union field _service_connection_policy can be only one of the following:
      "serviceConnectionPolicy": string
      // End of list of possible types for union field _service_connection_policy.
    
      // Union field _service_connection_policy_creation_result can be only one of
      // the following:
      "serviceConnectionPolicyCreationResult": string
      // End of list of possible types for union field
      // _service_connection_policy_creation_result.
    
      // Union field _instance_auto_dns_status can be only one of the following:
      "instanceAutoDnsStatus": enum ([AutoDnsStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AutoDnsStatus))
      // End of list of possible types for union field _instance_auto_dns_status.
    
      // Union field _write_endpoint_auto_dns_status can be only one of the
      // following:
      "writeEndpointAutoDnsStatus": enum ([AutoDnsStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AutoDnsStatus))
      // End of list of possible types for union field
      // _write_endpoint_auto_dns_status.
    }  
  
Fields  
---  
`consumerProject` |  `string` Optional. This is the project ID of consumer service project of this consumer endpoint.This is only applicable if `consumer_network` is a shared VPC network.  
`consumerNetwork` |  `string` Optional. The consumer network of this consumer endpoint. This must be a resource path that includes both the host project and the network name.For example, `projects/project1/global/networks/network1`.The consumer host project of this network might be different from the consumer service project.  
Union field `_ip_address`.`_ip_address` can be only one of the following:  
`ipAddress` |  `string` The IP address of the consumer endpoint.  
Union field `_status`.`_status` can be only one of the following:  
`status` |  `string` The connection status of the consumer endpoint.  
Union field `_consumer_network_status`.`_consumer_network_status` can be only one of the following:  
`consumerNetworkStatus` |  `string` The connection policy status of the consumer network.  
Union field `_service_connection_policy`.`_service_connection_policy` can be only one of the following:  
`serviceConnectionPolicy` |  `string` Output only. The service connection policy created automatically for the consumer network when `psc_auto_connection_policy_enabled` is true. It is in the format of: `projects/{project}/regions/{region}/serviceConnectionPolicies/{policy_id}` The `policy_id` is in format of `$NETWORK-$RANDOM`.  
Union field `_service_connection_policy_creation_result`.`_service_connection_policy_creation_result` can be only one of the following:  
`serviceConnectionPolicyCreationResult` |  `string` Output only. The status of service connection policy creation.  
Union field `_instance_auto_dns_status`.`_instance_auto_dns_status` can be only one of the following:  
`instanceAutoDnsStatus` |  `enum (`[AutoDnsStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AutoDnsStatus)`)` Output only. The status of automated DNS provisioning.  
Union field `_write_endpoint_auto_dns_status`.`_write_endpoint_auto_dns_status` can be only one of the following:  
`writeEndpointAutoDnsStatus` |  `enum (`[AutoDnsStatus](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.AutoDnsStatus)`)` Output only. The status of automated DNS provisioning for the write endpoint.  
  
### LocationPreference

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
  
### MaintenanceWindow

JSON representation  
---  
      
    
    {
      "hour": integer,
      "day": integer,
      "updateTrack": enum ([SqlUpdateTrack](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlUpdateTrack)),
      "kind": string
    }  
  
Fields  
---  
`hour` |  `integer` Hour of day - 0 to 23. Specify in the UTC time zone.  
`day` |  `integer` Day of week - `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, or `SUNDAY`. Specify in the UTC time zone. Returned in output as an integer, 1 to 7, where `1` equals Monday.  
`updateTrack` |  `enum (`[SqlUpdateTrack](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlUpdateTrack)`)` Maintenance timing settings: `canary`, `stable`, or `week5`. For more information, see [About maintenance on Cloud SQL instances](https://cloud.google.com/sql/docs/mysql/maintenance).  
`kind` |  `string` This is always `sql#maintenanceWindow`.  
  
### Int32Value

JSON representation  
---  
      
    
    {
      "value": integer
    }  
  
Fields  
---  
`value` |  `integer` The int32 value.  
  
### BackupConfiguration

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
      "backupRetentionSettings": {
        object ([BackupRetentionSettings](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupRetentionSettings))
      },
      "transactionLogRetentionDays": integer,
    
      // Union field _transactional_log_storage_state can be only one of the
      // following:
      "transactionalLogStorageState": enum ([TransactionalLogStorageState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TransactionalLogStorageState))
      // End of list of possible types for union field
      // _transactional_log_storage_state.
    
      // Union field _backup_tier can be only one of the following:
      "backupTier": enum ([BackupTier](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupTier))
      // End of list of possible types for union field _backup_tier.
    }  
  
Fields  
---  
`startTime` |  `string` Start time for the daily backup configuration in UTC timezone in the 24 hour format - `HH:MM`.  
`enabled` |  `boolean` Whether this configuration is enabled.  
`kind` |  `string` This is always `sql#backupConfiguration`.  
`binaryLogEnabled` |  `boolean` (MySQL only) Whether binary log is enabled. If backup configuration is disabled, binarylog must be disabled as well.  
`replicationLogArchivingEnabled  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: replication_log_archiving_enabled is deprecated and will be removed from a future version of the API. Use `point_in_time_recovery_enabled` instead.  
`location` |  `string` Location of the backup  
`pointInTimeRecoveryEnabled` |  `boolean` Whether point in time recovery is enabled.  
`backupRetentionSettings` |  `object (`[BackupRetentionSettings](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupRetentionSettings)`)` Backup retention settings.  
`transactionLogRetentionDays` |  `integer` The number of days of transaction logs we retain for point in time restore, from 1-7.  
Union field `_transactional_log_storage_state`.`_transactional_log_storage_state` can be only one of the following:  
`transactionalLogStorageState` |  `enum (`[TransactionalLogStorageState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TransactionalLogStorageState)`)` Output only. This value contains the storage location of transactional logs used to perform point-in-time recovery (PITR) for the database.  
Union field `_backup_tier`.`_backup_tier` can be only one of the following:  
`backupTier` |  `enum (`[BackupTier](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.BackupTier)`)` Output only. Backup tier that manages the backups for the instance.  
  
### BackupRetentionSettings

JSON representation  
---  
      
    
    {
      "retentionUnit": enum ([RetentionUnit](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.RetentionUnit)),
      "retainedBackups": integer
    }  
  
Fields  
---  
`retentionUnit` |  `enum (`[RetentionUnit](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.RetentionUnit)`)` The unit that 'retained_backups' represents.  
`retainedBackups` |  `integer` Depending on the value of retention_unit, this is used to determine if a backup needs to be deleted. If retention_unit is 'COUNT', we will retain this many backups.  
  
### SqlActiveDirectoryConfig

JSON representation  
---  
      
    
    {
      "kind": string,
      "domain": string,
      "mode": enum ([ActiveDirectoryMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ActiveDirectoryMode)),
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
`mode` |  `enum (`[ActiveDirectoryMode](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ActiveDirectoryMode)`)` Optional. The mode of the Active Directory configuration.  
`dnsServers[]` |  `string` Optional. Domain controller IPv4 addresses used to bootstrap Active Directory.  
`adminCredentialSecretName` |  `string` Optional. The secret manager key storing the administrator credential. (e.g., projects/{project}/secrets/{secret}).  
`organizationalUnit` |  `string` Optional. The organizational unit distinguished name. This is the full hierarchical path to the organizational unit.  
  
### DenyMaintenancePeriod

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
`endDate` |  `string` "deny maintenance period" end date. If the year of the end date is empty, the year of the start date also must be empty. In this case, it means the no maintenance interval recurs every year. The date is in format yyyy-mm-dd i.e., 2020-11-01, or mm-dd, i.e., 11-01  
`time` |  `string` Time in UTC when the "deny maintenance period" starts on start_date and ends on end_date. The time is in format: HH:mm:SS, i.e., 00:00:00  
  
### InsightsConfig

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

JSON representation  
---  
      
    
    {
      "minLength": integer,
      "complexity": enum ([Complexity](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Complexity)),
      "reuseInterval": integer,
      "disallowUsernameSubstring": boolean,
      "passwordChangeInterval": string,
      "enablePasswordPolicy": boolean,
      "disallowCompromisedCredentials": boolean
    }  
  
Fields  
---  
`minLength` |  `integer` Minimum number of characters allowed.  
`complexity` |  `enum (`[Complexity](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.Complexity)`)` The complexity of the password.  
`reuseInterval` |  `integer` Number of previous passwords that cannot be reused.  
`disallowUsernameSubstring` |  `boolean` Disallow username as a part of the password.  
`passwordChangeInterval` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Minimum interval after which the password can be changed. This flag is only supported for PostgreSQL.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`enablePasswordPolicy` |  `boolean` Whether to enable the password policy or not. When enabled, passwords must meet complexity requirements. Keep this policy enabled to help prevent unauthorized access. Disabling this policy allows weak passwords.  
`disallowCompromisedCredentials  
**(deprecated)**` |  `boolean` This item is deprecated!This field is deprecated and will be removed in a future version of the API.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### SqlServerAuditConfig

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
  
### AdvancedMachineFeatures

JSON representation  
---  
      
    
    {
      "threadsPerCore": integer
    }  
  
Fields  
---  
`threadsPerCore` |  `integer` The number of threads per physical core.  
  
### DataCacheConfig

JSON representation  
---  
      
    
    {
      "dataCacheEnabled": boolean
    }  
  
Fields  
---  
`dataCacheEnabled` |  `boolean` Whether data cache is enabled for the instance.  
  
### ConnectionPoolConfig

JSON representation  
---  
      
    
    {
      "flags": [
        {
          object ([ConnectionPoolFlags](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionPoolFlags))
        }
      ],
    
      // Union field _connection_pooling_enabled can be only one of the following:
      "connectionPoolingEnabled": boolean
      // End of list of possible types for union field _connection_pooling_enabled.
    
      // Union field _pooler_count can be only one of the following:
      "poolerCount": integer
      // End of list of possible types for union field _pooler_count.
    }  
  
Fields  
---  
`flags[]` |  `object (`[ConnectionPoolFlags](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionPoolFlags)`)` Optional. List of connection pool configuration flags.  
Union field `_connection_pooling_enabled`.`_connection_pooling_enabled` can be only one of the following:  
`connectionPoolingEnabled` |  `boolean` Whether managed connection pooling is enabled.  
Union field `_pooler_count`.`_pooler_count` can be only one of the following:  
`poolerCount` |  `integer` Output only. Number of connection poolers.  
  
### ConnectionPoolFlags

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

JSON representation  
---  
      
    
    {
    
      // Union field _enabled can be only one of the following:
      "enabled": boolean
      // End of list of possible types for union field _enabled.
    
      // Union field _retention_days can be only one of the following:
      "retentionDays": integer
      // End of list of possible types for union field _retention_days.
    }  
  
Fields  
---  
Union field `_enabled`.`_enabled` can be only one of the following:  
`enabled` |  `boolean` Whether the final backup is enabled for the instance.  
Union field `_retention_days`.`_retention_days` can be only one of the following:  
`retentionDays` |  `integer` The number of days to retain the final backup after the instance deletion. The final backup will be purged at (time_of_instance_deletion + retention_days).  
  
### ReadPoolAutoScaleConfig

JSON representation  
---  
      
    
    {
      "targetMetrics": [
        {
          object ([TargetMetric](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TargetMetric))
        }
      ],
    
      // Union field _enabled can be only one of the following:
      "enabled": boolean
      // End of list of possible types for union field _enabled.
    
      // Union field _min_node_count can be only one of the following:
      "minNodeCount": integer
      // End of list of possible types for union field _min_node_count.
    
      // Union field _max_node_count can be only one of the following:
      "maxNodeCount": integer
      // End of list of possible types for union field _max_node_count.
    
      // Union field _disable_scale_in can be only one of the following:
      "disableScaleIn": boolean
      // End of list of possible types for union field _disable_scale_in.
    
      // Union field _scale_in_cooldown_seconds can be only one of the following:
      "scaleInCooldownSeconds": integer
      // End of list of possible types for union field _scale_in_cooldown_seconds.
    
      // Union field _scale_out_cooldown_seconds can be only one of the following:
      "scaleOutCooldownSeconds": integer
      // End of list of possible types for union field _scale_out_cooldown_seconds.
    }  
  
Fields  
---  
`targetMetrics[]` |  `object (`[TargetMetric](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TargetMetric)`)` Optional. Target metrics for read pool auto scaling.  
Union field `_enabled`.`_enabled` can be only one of the following:  
`enabled` |  `boolean` Indicates whether read pool auto scaling is enabled.  
Union field `_min_node_count`.`_min_node_count` can be only one of the following:  
`minNodeCount` |  `integer` Minimum number of read pool nodes to be maintained.  
Union field `_max_node_count`.`_max_node_count` can be only one of the following:  
`maxNodeCount` |  `integer` Maximum number of read pool nodes to be maintained.  
Union field `_disable_scale_in`.`_disable_scale_in` can be only one of the following:  
`disableScaleIn` |  `boolean` Indicates whether read pool auto scaling supports scale in operations (removing nodes).  
Union field `_scale_in_cooldown_seconds`.`_scale_in_cooldown_seconds` can be only one of the following:  
`scaleInCooldownSeconds` |  `integer` The cooldown period for scale-in operations.  
Union field `_scale_out_cooldown_seconds`.`_scale_out_cooldown_seconds` can be only one of the following:  
`scaleOutCooldownSeconds` |  `integer` The cooldown period for scale-out operations.  
  
### TargetMetric

JSON representation  
---  
      
    
    {
    
      // Union field _metric can be only one of the following:
      "metric": string
      // End of list of possible types for union field _metric.
    
      // Union field _target_value can be only one of the following:
      "targetValue": number
      // End of list of possible types for union field _target_value.
    }  
  
Fields  
---  
Union field `_metric`.`_metric` can be only one of the following:  
`metric` |  `string` The metric name to be used for auto scaling.  
Union field `_target_value`.`_target_value` can be only one of the following:  
`targetValue` |  `number` The target value for the metric.  
  
### SqlServerEntraIdConfig

JSON representation  
---  
      
    
    {
      "kind": string,
      "tenantId": string,
      "applicationId": string
    }  
  
Fields  
---  
`kind` |  `string` Output only. This is always sql#sqlServerEntraIdConfig  
`tenantId` |  `string` Optional. The tenant ID for the Entra ID configuration.  
`applicationId` |  `string` Optional. The application ID for the Entra ID configuration.  
  
### PerformanceCaptureConfig

JSON representation  
---  
      
    
    {
      "transactionKillExcludedUserHosts": [
        string
      ],
    
      // Union field _enabled can be only one of the following:
      "enabled": boolean
      // End of list of possible types for union field _enabled.
    
      // Union field _probing_interval_seconds can be only one of the following:
      "probingIntervalSeconds": integer
      // End of list of possible types for union field _probing_interval_seconds.
    
      // Union field _probe_threshold can be only one of the following:
      "probeThreshold": integer
      // End of list of possible types for union field _probe_threshold.
    
      // Union field _running_threads_threshold can be only one of the following:
      "runningThreadsThreshold": integer
      // End of list of possible types for union field _running_threads_threshold.
    
      // Union field _seconds_behind_source_threshold can be only one of the
      // following:
      "secondsBehindSourceThreshold": integer
      // End of list of possible types for union field
      // _seconds_behind_source_threshold.
    
      // Union field _transaction_duration_threshold can be only one of the
      // following:
      "transactionDurationThreshold": integer
      // End of list of possible types for union field
      // _transaction_duration_threshold.
    
      // Union field _cpu_utilization_threshold_percent can be only one of the
      // following:
      "cpuUtilizationThresholdPercent": integer
      // End of list of possible types for union field
      // _cpu_utilization_threshold_percent.
    
      // Union field _memory_usage_threshold_percent can be only one of the
      // following:
      "memoryUsageThresholdPercent": integer
      // End of list of possible types for union field
      // _memory_usage_threshold_percent.
    
      // Union field _transaction_lock_wait_threshold_count can be only one of the
      // following:
      "transactionLockWaitThresholdCount": integer
      // End of list of possible types for union field
      // _transaction_lock_wait_threshold_count.
    
      // Union field _semaphore_wait_threshold_count can be only one of the
      // following:
      "semaphoreWaitThresholdCount": integer
      // End of list of possible types for union field
      // _semaphore_wait_threshold_count.
    
      // Union field _history_list_length_threshold_count can be only one of the
      // following:
      "historyListLengthThresholdCount": integer
      // End of list of possible types for union field
      // _history_list_length_threshold_count.
    
      // Union field _transaction_kill_threshold_seconds can be only one of the
      // following:
      "transactionKillThresholdSeconds": integer
      // End of list of possible types for union field
      // _transaction_kill_threshold_seconds.
    
      // Union field _transaction_kill_type can be only one of the following:
      "transactionKillType": enum ([TransactionKillType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TransactionKillType))
      // End of list of possible types for union field _transaction_kill_type.
    }  
  
Fields  
---  
`transactionKillExcludedUserHosts[]` |  `string` Optional. Specifies a customer-defined list of users to exclude from transaction termination. Entries can be in the format 'user@host' or just 'user'. A standalone 'user' implies 'user@%', excluding the user from any host. Wildcard '%' is allowed in the host part of the 'user@host' format. Example: `["app_user", "db_admin@10.1.2.3", "report_user@%"]`  
Union field `_enabled`.`_enabled` can be only one of the following:  
`enabled` |  `boolean` Optional. Enables or disables the performance capture feature.  
Union field `_probing_interval_seconds`.`_probing_interval_seconds` can be only one of the following:  
`probingIntervalSeconds` |  `integer` Optional. Specifies the interval in seconds between consecutive probes that check if any trigger condition thresholds have been reached.  
Union field `_probe_threshold`.`_probe_threshold` can be only one of the following:  
`probeThreshold` |  `integer` Optional. Specifies the minimum number of consecutive probe threshold that triggers performance capture.  
Union field `_running_threads_threshold`.`_running_threads_threshold` can be only one of the following:  
`runningThreadsThreshold` |  `integer` Optional. Specifies the minimum number of MySQL `Threads_running` to trigger the performance capture on the primary instance.  
Union field `_seconds_behind_source_threshold`.`_seconds_behind_source_threshold` can be only one of the following:  
`secondsBehindSourceThreshold` |  `integer` Optional. Specifies the minimum number of seconds replica must be lagging behind primary instance to trigger the performance capture on replica.  
Union field `_transaction_duration_threshold`.`_transaction_duration_threshold` can be only one of the following:  
`transactionDurationThreshold` |  `integer` Optional. Specifies the amount of time in seconds that a transaction needs to have been open before the watcher starts recording it.  
Union field `_cpu_utilization_threshold_percent`.`_cpu_utilization_threshold_percent` can be only one of the following:  
`cpuUtilizationThresholdPercent` |  `integer` Optional. Specifies the minimum percentage of CPU utilization to trigger the performance capture. Valid integers range from `10` to `99`. Enter `0` to disable the check.  
Union field `_memory_usage_threshold_percent`.`_memory_usage_threshold_percent` can be only one of the following:  
`memoryUsageThresholdPercent` |  `integer` Optional. Specifies the minimum percentage of memory usage to trigger the performance capture. Valid integers range from `10` to `99`. Enter `0` to disable the check.  
Union field `_transaction_lock_wait_threshold_count`.`_transaction_lock_wait_threshold_count` can be only one of the following:  
`transactionLockWaitThresholdCount` |  `integer` Optional. Specifies the minimum allowed number of transactions in lock wait state to trigger the performance capture. Valid integers range from `10` to `10000`. Enter `0` to disable the check.  
Union field `_semaphore_wait_threshold_count`.`_semaphore_wait_threshold_count` can be only one of the following:  
`semaphoreWaitThresholdCount` |  `integer` Optional. Specifies the minimum allowed number of semaphore waits to trigger the performance capture. Valid integers range from `10` to `10000`. Enter `0` to disable the check.  
Union field `_history_list_length_threshold_count`.`_history_list_length_threshold_count` can be only one of the following:  
`historyListLengthThresholdCount` |  `integer` Optional. Specifies the minimum number of undo log entries in the history list length to trigger the performance capture. Valid integers range from `10000` to `10000000`. Enter `0` to disable the check.  
Union field `_transaction_kill_threshold_seconds`.`_transaction_kill_threshold_seconds` can be only one of the following:  
`transactionKillThresholdSeconds` |  `integer` Optional. Specifies the amount of time in seconds that a transaction needs to have been open before the watcher starts terminating it. Valid integers range from `60` to `604800` (7 days). Enter `0` to disable. If enabled (i.e., > 0), this value must be greater than or equal to `transaction_duration_threshold`. Configurations where `0 < transaction_kill_threshold_seconds < transaction_duration_threshold` will be rejected.  
Union field `_transaction_kill_type`.`_transaction_kill_type` can be only one of the following:  
`transactionKillType` |  `enum (`[TransactionKillType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TransactionKillType)`)` Optional. Determines which transactions are allowed to be terminated when they exceed `transaction_kill_threshold_seconds`. This allows protecting write-heavy transactions from auto-termination if desired. Defaults to `READ_ONLY_TRANSACTIONS` if unspecified.  
  
### SqlFailoverReplica

JSON representation  
---  
      
    
    {
      "name": string,
      "available": boolean
    }  
  
Fields  
---  
`name` |  `string` The name of the failover replica. If specified at instance creation, a failover replica is created for the instance. The name doesn't include the project ID.  
`available` |  `boolean` The availability status of the failover replica. A false status indicates that the failover replica is out of sync. The primary instance can only failover to the failover replica when the status is true.  
  
### IpMapping

JSON representation  
---  
      
    
    {
      "type": enum ([SqlIpAddressType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlIpAddressType)),
      "ipAddress": string,
      "timeToRetire": string
    }  
  
Fields  
---  
`type` |  `enum (`[SqlIpAddressType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlIpAddressType)`)` The type of this IP address. A `PRIMARY` address is a public address that can accept incoming connections. A `PRIVATE` address is a private address that can accept incoming connections. An `OUTGOING` address is the source address of connections originating from the instance, if supported.  
`ipAddress` |  `string` The IP address assigned.  
`timeToRetire` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The due time for this IP to be retired in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`. This field is only available when the IP is scheduled to be retired.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SslCert

JSON representation  
---  
      
    
    {
      "kind": string,
      "certSerialNumber": string,
      "cert": string,
      "createTime": string,
      "commonName": string,
      "expirationTime": string,
      "sha1Fingerprint": string,
      "instance": string,
      "selfLink": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#sslCert`.  
`certSerialNumber` |  `string` Serial number, as extracted from the certificate.  
`cert` |  `string` PEM representation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the certificate was created in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commonName` |  `string` User supplied name. Constrained to [a-zA-Z.-_ ]+.  
`expirationTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time when the certificate expires in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sha1Fingerprint` |  `string` Sha1 Fingerprint.  
`instance` |  `string` Name of the database instance.  
`selfLink` |  `string` The URI of this resource.  
  
### OnPremisesConfiguration

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
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference))
      },
      "selectedObjects": [
        {
          object ([SelectedObjects](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SelectedObjects))
        }
      ],
      "sslOption": enum ([SslOption](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslOption)),
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
`sourceInstance` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference)`)` The reference to Cloud SQL instance if the source is Cloud SQL.  
`selectedObjects[]` |  `object (`[SelectedObjects](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SelectedObjects)`)` Optional. A list of objects that the user selects for replication from an external source instance.  
`sslOption` |  `enum (`[SslOption](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SslOption)`)` Optional. SSL option for replica connection to the on-premises source.  
`dmsManaged` |  `boolean` Output only. Indicates whether the resource is managed by Database Migration Service.  
  
### InstanceReference

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

JSON representation  
---  
      
    
    {
      "database": string
    }  
  
Fields  
---  
`database` |  `string` Required. The name of the database to migrate.  
  
### ReplicaConfiguration

JSON representation  
---  
      
    
    {
      "kind": string,
      "mysqlReplicaConfiguration": {
        object ([MySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.MySqlReplicaConfiguration))
      },
      "failoverTarget": boolean,
      "cascadableReplica": boolean
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#replicaConfiguration`.  
`mysqlReplicaConfiguration` |  `object (`[MySqlReplicaConfiguration](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.MySqlReplicaConfiguration)`)` MySQL specific configuration when replicating from a MySQL on-premises primary instance. Replication configuration information such as the username, password, certificates, and keys are not stored in the instance metadata. The configuration information is used only to set up the replication connection and is stored by MySQL in a file named `master.info` in the data directory.  
`failoverTarget` |  `boolean` Specifies if the replica is the failover target. If the field is set to `true`, the replica will be designated as a failover replica. In case the primary instance fails, the replica instance will be promoted as the new primary instance. Only one replica can be specified as failover target, and the replica has to be in different zone with the primary instance.  
`cascadableReplica` |  `boolean` Optional. Specifies if a SQL Server replica is a cascadable replica. A cascadable replica is a SQL Server cross region replica that supports replica(s) under it.  
  
### MySqlReplicaConfiguration

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
  
### DiskEncryptionConfiguration

JSON representation  
---  
      
    
    {
      "kmsKeyName": string,
      "kind": string,
    
      // Union field _confidential_mode can be only one of the following:
      "confidentialMode": boolean
      // End of list of possible types for union field _confidential_mode.
    
      // Union field _cmek_source_log_encryption_enforced can be only one of the
      // following:
      "cmekSourceLogEncryptionEnforced": boolean
      // End of list of possible types for union field
      // _cmek_source_log_encryption_enforced.
    }  
  
Fields  
---  
`kmsKeyName` |  `string` Resource name of KMS key for disk encryption.  
`kind` |  `string` This is always `sql#diskEncryptionConfiguration`.  
Union field `_confidential_mode`.`_confidential_mode` can be only one of the following:  
`confidentialMode` |  `boolean` Optional. If true, enables Confidential Mode for the instance's Hyperdisk Balanced volumes. Only supported for zonal C4A instances currently.  
Union field `_cmek_source_log_encryption_enforced`.`_cmek_source_log_encryption_enforced` can be only one of the following:  
`cmekSourceLogEncryptionEnforced` |  `boolean` Optional. Whether to enforce CMEK log encryption at source. When enforced, transaction logs are encrypted prior to being uploaded to Cloud Storage. If not enforced, then CMEK logs are encrypted by the Cloud Storage service.  
  
### DiskEncryptionStatus

JSON representation  
---  
      
    
    {
      "kmsKeyVersionName": string,
      "kind": string
    }  
  
Fields  
---  
`kmsKeyVersionName` |  `string` KMS key version used to encrypt the Cloud SQL instance resource  
`kind` |  `string` This is always `sql#diskEncryptionStatus`.  
  
### SqlScheduledMaintenance

JSON representation  
---  
      
    
    {
      "startTime": string,
      "canDefer": boolean,
      "canReschedule": boolean,
    
      // Union field _schedule_deadline_time can be only one of the following:
      "scheduleDeadlineTime": string
      // End of list of possible types for union field _schedule_deadline_time.
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of any upcoming scheduled maintenance for this instance.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`canDefer  
**(deprecated)**` |  `boolean` This item is deprecated!  
`canReschedule` |  `boolean` If the scheduled maintenance can be rescheduled.  
Union field `_schedule_deadline_time`.`_schedule_deadline_time` can be only one of the following:  
`scheduleDeadlineTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Maintenance cannot be rescheduled to start beyond this deadline.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### SqlOutOfDiskReport

JSON representation  
---  
      
    
    {
    
      // Union field _sql_out_of_disk_state can be only one of the following:
      "sqlOutOfDiskState": enum ([SqlOutOfDiskState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlOutOfDiskState))
      // End of list of possible types for union field _sql_out_of_disk_state.
    
      // Union field _sql_min_recommended_increase_size_gb can be only one of the
      // following:
      "sqlMinRecommendedIncreaseSizeGb": integer
      // End of list of possible types for union field
      // _sql_min_recommended_increase_size_gb.
    }  
  
Fields  
---  
Union field `_sql_out_of_disk_state`.`_sql_out_of_disk_state` can be only one of the following:  
`sqlOutOfDiskState` |  `enum (`[SqlOutOfDiskState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SqlOutOfDiskState)`)` This field represents the state generated by the proactive database wellness job for OutOfDisk issues. * Writers: * the proactive database wellness job for OOD. * Readers: * the proactive database wellness job  
Union field `_sql_min_recommended_increase_size_gb`.`_sql_min_recommended_increase_size_gb` can be only one of the following:  
`sqlMinRecommendedIncreaseSizeGb` |  `integer` The minimum recommended increase size in GigaBytes This field is consumed by the frontend * Writers: * the proactive database wellness job for OOD. * Readers:  
  
### AvailableDatabaseVersion

JSON representation  
---  
      
    
    {
    
      // Union field _major_version can be only one of the following:
      "majorVersion": string
      // End of list of possible types for union field _major_version.
    
      // Union field _name can be only one of the following:
      "name": string
      // End of list of possible types for union field _name.
    
      // Union field _display_name can be only one of the following:
      "displayName": string
      // End of list of possible types for union field _display_name.
    }  
  
Fields  
---  
Union field `_major_version`.`_major_version` can be only one of the following:  
`majorVersion` |  `string` The version's major version name.  
Union field `_name`.`_name` can be only one of the following:  
`name` |  `string` The database version name. For MySQL 8.0, this string provides the database major and minor version.  
Union field `_display_name`.`_display_name` can be only one of the following:  
`displayName` |  `string` The database version's display name.  
  
### ReplicationCluster

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

JSON representation  
---  
      
    
    {
    
      // Union field _entitled can be only one of the following:
      "entitled": boolean
      // End of list of possible types for union field _entitled.
    
      // Union field _google_vacuum_mgmt_enabled can be only one of the following:
      "googleVacuumMgmtEnabled": boolean
      // End of list of possible types for union field _google_vacuum_mgmt_enabled.
    
      // Union field _oom_session_cancel_enabled can be only one of the following:
      "oomSessionCancelEnabled": boolean
      // End of list of possible types for union field _oom_session_cancel_enabled.
    
      // Union field _active_query_enabled can be only one of the following:
      "activeQueryEnabled": boolean
      // End of list of possible types for union field _active_query_enabled.
    
      // Union field _index_advisor_enabled can be only one of the following:
      "indexAdvisorEnabled": boolean
      // End of list of possible types for union field _index_advisor_enabled.
    
      // Union field _flag_recommender_enabled can be only one of the following:
      "flagRecommenderEnabled": boolean
      // End of list of possible types for union field _flag_recommender_enabled.
    }  
  
Fields  
---  
Union field `_entitled`.`_entitled` can be only one of the following:  
`entitled` |  `boolean` Output only. Whether Gemini is enabled.  
Union field `_google_vacuum_mgmt_enabled`.`_google_vacuum_mgmt_enabled` can be only one of the following:  
`googleVacuumMgmtEnabled` |  `boolean` Output only. Whether the vacuum management is enabled.  
Union field `_oom_session_cancel_enabled`.`_oom_session_cancel_enabled` can be only one of the following:  
`oomSessionCancelEnabled` |  `boolean` Output only. Whether canceling the out-of-memory (OOM) session is enabled.  
Union field `_active_query_enabled`.`_active_query_enabled` can be only one of the following:  
`activeQueryEnabled` |  `boolean` Output only. Whether the active query is enabled.  
Union field `_index_advisor_enabled`.`_index_advisor_enabled` can be only one of the following:  
`indexAdvisorEnabled` |  `boolean` Output only. Whether the index advisor is enabled.  
Union field `_flag_recommender_enabled`.`_flag_recommender_enabled` can be only one of the following:  
`flagRecommenderEnabled` |  `boolean` Output only. Whether the flag recommender is enabled.  
  
### TagsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### PoolNodeConfig

JSON representation  
---  
      
    
    {
      "ipAddresses": [
        {
          object ([IpMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpMapping))
        }
      ],
      "dnsNames": [
        {
          object ([DnsNameMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsNameMapping))
        }
      ],
      "pscAutoConnections": [
        {
          object ([PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscAutoConnectionConfig))
        }
      ],
    
      // Union field _name can be only one of the following:
      "name": string
      // End of list of possible types for union field _name.
    
      // Union field _gce_zone can be only one of the following:
      "gceZone": string
      // End of list of possible types for union field _gce_zone.
    
      // Union field _dns_name can be only one of the following:
      "dnsName": string
      // End of list of possible types for union field _dns_name.
    
      // Union field _state can be only one of the following:
      "state": enum ([SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState))
      // End of list of possible types for union field _state.
    
      // Union field _psc_service_attachment_link can be only one of the following:
      "pscServiceAttachmentLink": string
      // End of list of possible types for union field _psc_service_attachment_link.
    }  
  
Fields  
---  
`ipAddresses[]` |  `object (`[IpMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.IpMapping)`)` Output only. Mappings containing IP addresses that can be used to connect to the read pool node.  
`dnsNames[]` |  `object (`[DnsNameMapping](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsNameMapping)`)` Output only. The list of DNS names used by this read pool node.  
`pscAutoConnections[]` |  `object (`[PscAutoConnectionConfig](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.PscAutoConnectionConfig)`)` Output only. The list of settings for requested automatically-setup Private Service Connect (PSC) consumer endpoints that can be used to connect to this read pool node.  
Union field `_name`.`_name` can be only one of the following:  
`name` |  `string` Output only. The name of the read pool node, to be used for retrieving metrics and logs.  
Union field `_gce_zone`.`_gce_zone` can be only one of the following:  
`gceZone` |  `string` Output only. The zone of the read pool node.  
Union field `_dns_name`.`_dns_name` can be only one of the following:  
`dnsName` |  `string` Output only. The DNS name of the read pool node.  
Union field `_state`.`_state` can be only one of the following:  
`state` |  `enum (`[SqlInstanceState](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/list_instances#Output.Schema.SqlInstanceState)`)` Output only. The current state of the read pool node.  
Union field `_psc_service_attachment_link`.`_psc_service_attachment_link` can be only one of the following:  
`pscServiceAttachmentLink` |  `string` Output only. The Private Service Connect (PSC) service attachment of the read pool node.  
  
### DnsNameMapping

JSON representation  
---  
      
    
    {
      "name": string,
      "connectionType": enum ([ConnectionType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionType)),
      "dnsScope": enum ([DnsScope](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsScope)),
      "recordManager": enum ([RecordManager](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.RecordManager))
    }  
  
Fields  
---  
`name` |  `string` Output only. The DNS name.  
`connectionType` |  `enum (`[ConnectionType](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.ConnectionType)`)` Output only. The connection type of the DNS name.  
`dnsScope` |  `enum (`[DnsScope](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.DnsScope)`)` Output only. The scope that the DNS name applies to.  
`recordManager` |  `enum (`[RecordManager](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.RecordManager)`)` Output only. The manager for this DNS record.  
  
### BlueGreenDeploymentInfo

JSON representation  
---  
      
    
    {
    
      // Union field _deployment_id can be only one of the following:
      "deploymentId": string
      // End of list of possible types for union field _deployment_id.
    
      // Union field role_details can be only one of the following:
      "source": {
        object ([SourceRole](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SourceRole))
      },
      "target": {
        object ([TargetRole](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TargetRole))
      }
      // End of list of possible types for union field role_details.
    
      // Union field _state can be only one of the following:
      "state": enum ([State](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.State))
      // End of list of possible types for union field _state.
    }  
  
Fields  
---  
Union field `_deployment_id`.`_deployment_id` can be only one of the following:  
`deploymentId` |  `string` Output only. The resource ID of the blue-green deployment.  
Union field `role_details`. The role of the instance in the blue-green deployment. `role_details` can be only one of the following:  
`source` |  `object (`[SourceRole](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.SourceRole)`)` Output only. The source instance for the Blue-Green deployment.  
`target` |  `object (`[TargetRole](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.TargetRole)`)` Output only. The target instance for the Blue-Green deployment.  
Union field `_state`.`_state` can be only one of the following:  
`state` |  `enum (`[State](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.State)`)` Output only. The current state of blue-green-deployment for UI tags  
  
### SourceRole

JSON representation  
---  
      
    
    {
    
      // Union field _target_id can be only one of the following:
      "targetId": {
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference))
      }
      // End of list of possible types for union field _target_id.
    }  
  
Fields  
---  
Union field `_target_id`.`_target_id` can be only one of the following:  
`targetId` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference)`)` Output only. The target instance paired with this source instance in a blue-green deployment.  
  
### TargetRole

JSON representation  
---  
      
    
    {
    
      // Union field _source_id can be only one of the following:
      "sourceId": {
        object ([InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference))
      }
      // End of list of possible types for union field _source_id.
    }  
  
Fields  
---  
Union field `_source_id`.`_source_id` can be only one of the following:  
`sourceId` |  `object (`[InstanceReference](https://docs.cloud.google.com/sql/docs/sqlserver/reference/mcp/sqlserver/mcp/tools_list/get_instance#Output.Schema.InstanceReference)`)` Output only. The source instance paired with this target instance in a blue-green deployment.  
  
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
`ONLINE_MAINTENANCE` | Deprecated  
`REPAIRING` | (Applicable to read pool nodes only.) The read pool node needs to be repaired. The database might be unavailable.  
  
### SqlDatabaseVersion

The database engine type and version.

Enums  
---  
`SQL_DATABASE_VERSION_UNSPECIFIED` | This is an unknown database version.  
`MYSQL_5_1` | The database version is MySQL 5.1.  
`MYSQL_5_5` | The database version is MySQL 5.5.  
`MYSQL_5_6` | The database version is MySQL 5.6.  
`MYSQL_5_7` | The database version is MySQL 5.7.  
`MYSQL_8_0` | The database version is MySQL 8.  
`MYSQL_8_0_18` | The database major version is MySQL 8.0 and the minor version is 18.  
`MYSQL_8_0_26` | The database major version is MySQL 8.0 and the minor version is 26.  
`MYSQL_8_0_27` | The database major version is MySQL 8.0 and the minor version is 27.  
`MYSQL_8_0_28` | The database major version is MySQL 8.0 and the minor version is 28.  
`MYSQL_8_0_29` | The database major version is MySQL 8.0 and the minor version is 29.  
`MYSQL_8_0_30` | The database major version is MySQL 8.0 and the minor version is 30.  
`MYSQL_8_0_31` | The database major version is MySQL 8.0 and the minor version is 31.  
`MYSQL_8_0_32` | The database major version is MySQL 8.0 and the minor version is 32.  
`MYSQL_8_0_33` | The database major version is MySQL 8.0 and the minor version is 33.  
`MYSQL_8_0_34` | The database major version is MySQL 8.0 and the minor version is 34.  
`MYSQL_8_0_35` | The database major version is MySQL 8.0 and the minor version is 35.  
`MYSQL_8_0_36` | The database major version is MySQL 8.0 and the minor version is 36.  
`MYSQL_8_0_37` | The database major version is MySQL 8.0 and the minor version is 37.  
`MYSQL_8_0_39` | The database major version is MySQL 8.0 and the minor version is 39.  
`MYSQL_8_0_40` | The database major version is MySQL 8.0 and the minor version is 40.  
`MYSQL_8_0_41` | The database major version is MySQL 8.0 and the minor version is 41.  
`MYSQL_8_0_42` | The database major version is MySQL 8.0 and the minor version is 42.  
`MYSQL_8_0_43` | The database major version is MySQL 8.0 and the minor version is 43.  
`MYSQL_8_0_44` | The database major version is MySQL 8.0 and the minor version is 44.  
`MYSQL_8_0_45` | The database major version is MySQL 8.0 and the minor version is 45.  
`MYSQL_8_0_46` | The database major version is MySQL 8.0 and the minor version is 46.  
`MYSQL_8_4` | The database version is MySQL 8.4.  
`MYSQL_9_7` | The database version is MySQL 9.7.  
`SQLSERVER_2017_STANDARD` | The database version is SQL Server 2017 Standard.  
`SQLSERVER_2017_ENTERPRISE` | The database version is SQL Server 2017 Enterprise.  
`SQLSERVER_2017_EXPRESS` | The database version is SQL Server 2017 Express.  
`SQLSERVER_2017_WEB` | The database version is SQL Server 2017 Web.  
`POSTGRES_9_6` | The database version is PostgreSQL 9.6.  
`POSTGRES_10` | The database version is PostgreSQL 10.  
`POSTGRES_11` | The database version is PostgreSQL 11.  
`POSTGRES_12` | The database version is PostgreSQL 12.  
`POSTGRES_13` | The database version is PostgreSQL 13.  
`POSTGRES_14` | The database version is PostgreSQL 14.  
`POSTGRES_15` | The database version is PostgreSQL 15.  
`POSTGRES_16` | The database version is PostgreSQL 16.  
`POSTGRES_17` | The database version is PostgreSQL 17.  
`POSTGRES_18` | The database version is PostgreSQL 18.  
`POSTGRES_19` | The database version is PostgreSQL 19.  
`POSTGRES_20` | The database version is PostgreSQL 20.  
`SQLSERVER_2019_STANDARD` | The database version is SQL Server 2019 Standard.  
`SQLSERVER_2019_ENTERPRISE` | The database version is SQL Server 2019 Enterprise.  
`SQLSERVER_2019_EXPRESS` | The database version is SQL Server 2019 Express.  
`SQLSERVER_2019_WEB` | The database version is SQL Server 2019 Web.  
`SQLSERVER_2022_STANDARD` | The database version is SQL Server 2022 Standard.  
`SQLSERVER_2022_ENTERPRISE` | The database version is SQL Server 2022 Enterprise.  
`SQLSERVER_2022_EXPRESS` | The database version is SQL Server 2022 Express.  
`SQLSERVER_2022_WEB` | The database version is SQL Server 2022 Web.  
`SQLSERVER_2025_STANDARD` | The database version is SQL Server 2025 Standard.  
`SQLSERVER_2025_ENTERPRISE` | The database version is SQL Server 2025 Enterprise.  
`SQLSERVER_2025_EXPRESS` | The database version is SQL Server 2025 Express.  
  
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
`ON_DEMAND` | The instance starts upon receiving requests.  
  
### SslMode

The SSL options for database connections.

Enums  
---  
`SSL_MODE_UNSPECIFIED` | The SSL mode is unknown.  
`ALLOW_UNENCRYPTED_AND_ENCRYPTED` | Allow non-SSL/non-TLS and SSL/TLS connections. For SSL connections to MySQL and PostgreSQL, the client certificate isn't verified.When this value is used, the legacy `require_ssl` flag must be false or cleared to avoid a conflict between the values of the two flags.  
`ENCRYPTED_ONLY` | Only allow connections encrypted with SSL/TLS. For SSL connections to MySQL and PostgreSQL, the client certificate isn't verified.When this value is used, the legacy `require_ssl` flag must be false or cleared to avoid a conflict between the values of the two flags.  
`TRUSTED_CLIENT_CERTIFICATE_REQUIRED` | Only allow connections encrypted with SSL/TLS and with valid client certificates.When this value is used, the legacy `require_ssl` flag must be true or cleared to avoid the conflict between values of two flags. PostgreSQL clients or users that connect using IAM database authentication must use either the [Cloud SQL Auth Proxy](https://cloud.google.com/sql/docs/postgres/connect-auth-proxy) or [Cloud SQL Connectors](https://cloud.google.com/sql/docs/postgres/connect-connectors) to enforce client identity verification.Only applicable to MySQL and PostgreSQL. Not applicable to SQL Server.  
  
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
`AUTOMATIC_ROTATION_DURING_MAINTENANCE` | Automatic server certificate rotation during Cloud SQL scheduled maintenance or self-service maintenance updates. Requires `server_ca_mode` to be `GOOGLE_MANAGED_CAS_CA` or `CUSTOMER_MANAGED_CAS_CA`.  
  
### SqlDataDiskType

The type of disk that is used for a v2 instance to use.

Enums  
---  
`SQL_DATA_DISK_TYPE_UNSPECIFIED` | This is an unknown data disk type.  
`PD_SSD` | An SSD data disk.  
`PD_HDD` | An HDD data disk.  
`OBSOLETE_LOCAL_SSD` | This field is deprecated and will be removed from a future version of the API.  
`HYPERDISK_BALANCED` | A Hyperdisk Balanced data disk.  
  
### SqlUpdateTrack

Enums  
---  
`SQL_UPDATE_TRACK_UNSPECIFIED` | This is an unknown maintenance timing preference.  
`canary` | For an instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 7 to 14 days after the notification is sent out. Also referred to as `Week 1` (Console) and `preview` (gcloud CLI).  
`stable` | For an instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 15 to 21 days after the notification is sent out. Also referred to as `Week 2` (Console) and `production` (gcloud CLI).  
`week5` | For instance with a scheduled maintenance window, this maintenance timing indicates that the maintenance update is scheduled 35 to 42 days after the notification is sent out.  
  
### RetentionUnit

The units that retained_backups specifies, we only support COUNT.

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
`ADVANCED` | Deprecated: ADVANCED is deprecated. Please use ENHANCED instead.  
`ENHANCED` | Instance is managed by Google Cloud Backup and DR Service.  
  
### ActiveDirectoryMode

The modes of Active Directory configuration.

Enums  
---  
`ACTIVE_DIRECTORY_MODE_UNSPECIFIED` | Unspecified mode. Will default to MANAGED_ACTIVE_DIRECTORY if the mode is not specified to maintain backward compatibility.  
`MANAGED_ACTIVE_DIRECTORY` | Managed Active Directory mode.  
`SELF_MANAGED_ACTIVE_DIRECTORY` | Deprecated: Use CUSTOMER_MANAGED_ACTIVE_DIRECTORY instead.  
`CUSTOMER_MANAGED_ACTIVE_DIRECTORY` | Customer-managed Active Directory mode.  
  
### Complexity

The complexity choices of the password.

Enums  
---  
`COMPLEXITY_UNSPECIFIED` | Complexity check is not specified.  
`COMPLEXITY_DEFAULT` | A combination of lowercase, uppercase, numeric, and non-alphanumeric characters.  
  
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
  
### DataApiAccess

ExecuteSql API's access to the instance.

Enums  
---  
`DATA_API_ACCESS_UNSPECIFIED` | Unspecified, effectively the same as `DISALLOW_DATA_API`.  
`DISALLOW_DATA_API` | Disallow using ExecuteSql API to connect to the instance.  
`ALLOW_DATA_API` | Allow using ExecuteSql API to connect to the instance. For private IP instances, this allows authorized users to access the instance from the public internet using ExecuteSql API.  
  
### TransactionKillType

Defines the categories of long-running transactions eligible for automatic termination by the Performance Capture.

Enums  
---  
`TRANSACTION_KILL_TYPE_UNSPECIFIED` | Unspecified.  
`READ_ONLY_TRANSACTIONS` | Only read-only transactions are eligible for termination.  
`ALL_TRANSACTIONS` | All transactions are eligible for termination, including those with write operations (such as INSERT, UPDATE, DELETE, or DDL).  
  
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
  
### SslOption

SslOption defines the SSL mode to be used for replica connection to the on-premises source.

Enums  
---  
`SSL_OPTION_UNSPECIFIED` | Unknown SSL option i.e. SSL option not specified by user.  
`DISABLE` | SSL is not used for replica connection to the on-premises source.  
`REQUIRE` | SSL is required for replica connection to the on-premises source.  
`VERIFY_CA` | Verify CA is required for replica connection to the on-premises source.  
  
### SqlBackendType

Enums  
---  
`SQL_BACKEND_TYPE_UNSPECIFIED` | This is an unknown backend type for instance.  
`FIRST_GEN` | V1 speckle instance.  
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
`PROJECT_ABUSE` | The project is suspended due to abuse detected by Ares.  
  
### SqlOutOfDiskState

This enum lists all possible states regarding out-of-disk issues.

Enums  
---  
`SQL_OUT_OF_DISK_STATE_UNSPECIFIED` | Unspecified state  
`NORMAL` | The instance has plenty space on data disk  
`SOFT_SHUTDOWN` | Data disk is almost used up. It is shutdown to prevent data corruption.  
  
### SqlNetworkArchitecture

The SQL network architecture for the instance.

Enums  
---  
`SQL_NETWORK_ARCHITECTURE_UNSPECIFIED` |   
`NEW_NETWORK_ARCHITECTURE` | The instance uses the new network architecture.  
`OLD_NETWORK_ARCHITECTURE` | The instance uses the old network architecture.  
  
### ConnectionType

The connection type of the DNS name. This enum is not frozen, and new values may be added in the future.

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
  
### State

The state of blue-green-deployment for UI tags

Enums  
---  
`STATE_UNSPECIFIED` | The state of the deployment is unknown.  
`PRE_SWITCHOVER` | The deployment is pre-switchover.  
`POST_SWITCHOVER` | The deployment is post-switchover.  
  
### DatabaseCenterIntegration

State of the integration with Database Center.

Enums  
---  
`DATABASE_CENTER_INTEGRATION_UNSPECIFIED` | Default value. The integration state is unspecified. When unspecified, Database Center integration is enabled by default.  
`ENABLED` | Database Center integration is enabled.  
`DISABLED` | Database Center integration is disabled.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ❌ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
