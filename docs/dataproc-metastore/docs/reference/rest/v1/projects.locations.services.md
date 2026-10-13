---
url: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services
title: REST Resource: projects.locations.services \u00a0|\u00a0 Dataproc Metastore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:51.968519+00:00
---

# REST Resource: projects.locations.services  |  Dataproc Metastore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataproc Metastore ](https://docs.cloud.google.com/dataproc-metastore/docs)
  * [ Reference ](https://docs.cloud.google.com/dataproc-metastore/docs/reference)



Send feedback 

#  REST Resource: projects.locations.services Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Service
    * JSON representation
    * HiveMetastoreConfig
      * JSON representation
    * KerberosConfig
      * JSON representation
    * Secret
      * JSON representation
    * EndpointProtocol
    * AuxiliaryVersionConfig
      * JSON representation
    * NetworkConfig
      * JSON representation
    * Consumer
      * JSON representation
    * State
    * Tier
    * MetadataIntegration
      * JSON representation
    * DataCatalogConfig
      * JSON representation
    * MaintenanceWindow
      * JSON representation
    * MetadataManagementActivity
      * JSON representation
    * MetadataExport
      * JSON representation
    * State
    * Restore
      * JSON representation
    * State
    * RestoreType
    * ReleaseChannel
    * EncryptionConfig
      * JSON representation
    * DatabaseType
    * TelemetryConfig
      * JSON representation
    * LogFormat
    * ScalingConfig
      * JSON representation
    * InstanceSize
    * AutoscalingConfig
      * JSON representation
    * LimitConfig
      * JSON representation
    * ScheduledBackup
      * JSON representation
    * LatestBackup
      * JSON representation
    * State
  * Methods



## Resource: Service

A managed metastore service that serves metadata queries.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "network": string,
      "endpointUri": string,
      "port": integer,
      "state": enum ([State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State)),
      "stateMessage": string,
      "artifactGcsUri": string,
      "tier": enum ([Tier](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Tier)),
      "metadataIntegration": {
        object ([MetadataIntegration](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataIntegration))
      },
      "maintenanceWindow": {
        object ([MaintenanceWindow](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MaintenanceWindow))
      },
      "uid": string,
      "metadataManagementActivity": {
        object ([MetadataManagementActivity](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataManagementActivity))
      },
      "releaseChannel": enum ([ReleaseChannel](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ReleaseChannel)),
      "encryptionConfig": {
        object ([EncryptionConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.EncryptionConfig))
      },
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.NetworkConfig))
      },
      "databaseType": enum ([DatabaseType](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.DatabaseType)),
      "telemetryConfig": {
        object ([TelemetryConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.TelemetryConfig))
      },
      "scalingConfig": {
        object ([ScalingConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ScalingConfig))
      },
      "scheduledBackup": {
        object ([ScheduledBackup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ScheduledBackup))
      },
      "deletionProtection": boolean,
      "tags": {
        string: string,
        ...
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "hiveMetastoreConfig": {
        object ([HiveMetastoreConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.HiveMetastoreConfig))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Immutable. Identifier. The relative resource name of the metastore service, in the following format:`projects/{projectNumber}/locations/{locationId}/services/{serviceId}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the metastore service was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the metastore service was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` User-defined labels for the metastore service.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`network` |  `string` Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form:`projects/{projectNumber}/global/networks/{network_id}`.  
`endpointUri` |  `string` Output only. The URI of the endpoint used to access the metastore service.  
`port` |  `integer` Optional. The TCP port at which the metastore service is reached. Default: 9083.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State)`)` Output only. The current state of the metastore service.  
`stateMessage` |  `string` Output only. Additional information about the current state of the metastore service, if available.  
`artifactGcsUri` |  `string` Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.  
`tier` |  `enum (`[Tier](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Tier)`)` Optional. The tier of the service.  
`metadataIntegration` |  `object (`[MetadataIntegration](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataIntegration)`)` Optional. The setting that defines how metastore metadata should be integrated with external services and systems.  
`maintenanceWindow` |  `object (`[MaintenanceWindow](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MaintenanceWindow)`)` Optional. The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.  
`uid` |  `string` Output only. The globally unique resource identifier of the metastore service.  
`metadataManagementActivity` |  `object (`[MetadataManagementActivity](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataManagementActivity)`)` Output only. The metadata management activities of the metastore service.  
`releaseChannel` |  `enum (`[ReleaseChannel](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ReleaseChannel)`)` Immutable. The release channel of the service. If unspecified, defaults to `STABLE`.  
`encryptionConfig` |  `object (`[EncryptionConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.EncryptionConfig)`)` Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.NetworkConfig)`)` Optional. The configuration specifying the network settings for the Dataproc Metastore service.  
`databaseType` |  `enum (`[DatabaseType](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.DatabaseType)`)` Immutable. The database type that the Metastore service stores its data.  
`telemetryConfig` |  `object (`[TelemetryConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.TelemetryConfig)`)` Optional. The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.  
`scalingConfig` |  `object (`[ScalingConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ScalingConfig)`)` Optional. Scaling configuration of the metastore service.  
`scheduledBackup` |  `object (`[ScheduledBackup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.ScheduledBackup)`)` Optional. The configuration of scheduled backup for the metastore service.  
`deletionProtection` |  `boolean` Optional. Indicates if the dataproc metastore should be protected against accidental deletions.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: "123/environment": "production", "123/costCenter": "marketing"An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Configuration properties specific to the underlying metastore service technology (the software that serves metastore queries). The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`hiveMetastoreConfig` |  `object (`[HiveMetastoreConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.HiveMetastoreConfig)`)` Configuration information specific to running Hive metastore software as the metastore service.  
End of mutually exclusive fields.  
  
### HiveMetastoreConfig

Specifies configuration information specific to running Hive metastore software as the metastore service.

JSON representation  
---  
      
    
    {
      "version": string,
      "configOverrides": {
        string: string,
        ...
      },
      "kerberosConfig": {
        object ([KerberosConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.KerberosConfig))
      },
      "endpointProtocol": enum ([EndpointProtocol](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.EndpointProtocol)),
      "auxiliaryVersions": {
        string: {
          object ([AuxiliaryVersionConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.AuxiliaryVersionConfig))
        },
        ...
      }
    }  
  
Fields  
---  
`version` |  `string` Immutable. The Hive metastore schema version.  
`configOverrides` |  `map (key: string, value: string)` Optional. A mapping of Hive metastore configuration key-value pairs to apply to the Hive metastore (configured in `hive-site.xml`). The mappings override system defaults (some keys cannot be overridden). These overrides are also applied to auxiliary versions and can be further customized in the auxiliary version's `AuxiliaryVersionConfig`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`kerberosConfig` |  `object (`[KerberosConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.KerberosConfig)`)` Optional. Information used to configure the Hive metastore service as a service principal in a Kerberos realm. To disable Kerberos, use the `services.patch` method and specify this field's path (`hiveMetastoreConfig.kerberos_config`) in the request's `updateMask` while omitting this field from the request's `service`.  
`endpointProtocol` |  `enum (`[EndpointProtocol](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.EndpointProtocol)`)` Optional. The protocol to use for the metastore service endpoint. If unspecified, defaults to `THRIFT`.  
`auxiliaryVersions` |  `map (key: string, value: object (`[AuxiliaryVersionConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.AuxiliaryVersionConfig)`))` Optional. A mapping of Hive metastore version to the auxiliary version configuration. When specified, a secondary Hive metastore service is created along with the primary service. All auxiliary versions must be less than the service's primary version. The key is the auxiliary service name and it must match the regular expression [a-z](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/\[-a-z0-9\]*\[a-z0-9\])?. This means that the first character must be a lowercase letter, and all the following characters must be hyphens, lowercase letters, or digits, except the last character, which cannot be a hyphen.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### KerberosConfig

Configuration information for a Kerberos principal.

JSON representation  
---  
      
    
    {
      "keytab": {
        object ([Secret](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Secret))
      },
      "principal": string,
      "krb5ConfigGcsUri": string
    }  
  
Fields  
---  
`keytab` |  `object (`[Secret](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Secret)`)` Optional. A Kerberos keytab file that can be used to authenticate a service principal with a Kerberos Key Distribution Center (KDC).  
`principal` |  `string` Optional. A Kerberos principal that exists in the both the keytab the KDC to authenticate as. A typical principal is of the form `primary/instance@REALM`, but there is no exact format.  
`krb5ConfigGcsUri` |  `string` Optional. A Cloud Storage URI that specifies the path to a krb5.conf file. It is of the form `gs://{bucket_name}/path/to/krb5.conf`, although the file does not need to be named krb5.conf explicitly.  
  
### Secret

A securely stored value.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "cloudSecret": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`cloudSecret` |  `string` Optional. The relative resource name of a Secret Manager secret version, in the following form:`projects/{projectNumber}/secrets/{secret_id}/versions/{version_id}`.  
End of mutually exclusive fields.  
  
### EndpointProtocol

Protocols available for serving the metastore service endpoint.

Enums  
---  
`ENDPOINT_PROTOCOL_UNSPECIFIED` | The protocol is not set.  
`THRIFT` | Use the legacy Apache Thrift protocol for the metastore service endpoint.  
`GRPC` | Use the modernized gRPC protocol for the metastore service endpoint.  
  
### AuxiliaryVersionConfig

Configuration information for the auxiliary service versions.

JSON representation  
---  
      
    
    {
      "version": string,
      "configOverrides": {
        string: string,
        ...
      },
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.NetworkConfig))
      }
    }  
  
Fields  
---  
`version` |  `string` Optional. The Hive metastore version of the auxiliary service. It must be less than the primary Hive metastore service's version.  
`configOverrides` |  `map (key: string, value: string)` Optional. A mapping of Hive metastore configuration key-value pairs to apply to the auxiliary Hive metastore (configured in `hive-site.xml`) in addition to the primary version's overrides. If keys are present in both the auxiliary version's overrides and the primary version's overrides, the value from the auxiliary version's overrides takes precedence.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.NetworkConfig)`)` Output only. The network configuration contains the endpoint URI(s) of the auxiliary Hive metastore service.  
  
### NetworkConfig

Network configuration for the Dataproc Metastore service.

JSON representation  
---  
      
    
    {
      "consumers": [
        {
          object ([Consumer](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Consumer))
        }
      ]
    }  
  
Fields  
---  
`consumers[]` |  `object (`[Consumer](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Consumer)`)` Immutable. The consumer-side network configuration for the Dataproc Metastore instance.  
  
### Consumer

Contains information of the customer's network configurations.

JSON representation  
---  
      
    
    {
      "endpointUri": string,
      "endpointLocation": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "subnetwork": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`endpointUri` |  `string` Output only. The URI of the endpoint used to access the metastore service.  
`endpointLocation` |  `string` Output only. The location of the endpoint URI. Format: `projects/{project}/locations/{location}`.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`subnetwork` |  `string` Immutable. The subnetwork of the customer project from which an IP address is reserved and used as the Dataproc Metastore service's endpoint. It is accessible to hosts in the subnet and to all hosts in a subnet in the same region and same network. There must be at least one IP address available in the subnet's primary range. The subnet is specified in the following form:`projects/{projectNumber}/regions/{region_id}/subnetworks/{subnetwork_id}`  
End of mutually exclusive fields.  
  
### State

The current state of the metastore service.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the metastore service is unknown.  
`CREATING` | The metastore service is in the process of being created.  
`ACTIVE` | The metastore service is running and ready to serve queries.  
`SUSPENDING` | The metastore service is entering suspension. Its query-serving availability may cease unexpectedly.  
`SUSPENDED` | The metastore service is suspended and unable to serve queries.  
`UPDATING` | The metastore service is being updated. It remains usable but cannot accept additional update requests or be deleted at this time.  
`DELETING` | The metastore service is undergoing deletion. It cannot be used.  
`ERROR` | The metastore service has encountered an error and cannot be used. The metastore service should be deleted.  
`AUTOSCALING` | The Dataproc Metastore service 2 is being scaled up or down.  
`MIGRATING` | The metastore service is processing a managed migration.  
`PROXY` | The metastore service has completed managed migration and is now proxying requests to the Lakehouse runtime catalog.  
  
### Tier

Available service tiers.

Enums  
---  
`TIER_UNSPECIFIED` | The tier is not set.  
`DEVELOPER` | The developer tier provides limited scalability and no fault tolerance. Good for low-cost proof-of-concept.  
`ENTERPRISE` | The enterprise tier provides multi-zone high availability, and sufficient scalability for enterprise-level Dataproc Metastore workloads.  
  
### MetadataIntegration

Specifies how metastore metadata should be integrated with external services.

JSON representation  
---  
      
    
    {
      "dataCatalogConfig": {
        object ([DataCatalogConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.DataCatalogConfig))
      }
    }  
  
Fields  
---  
`dataCatalogConfig` |  `object (`[DataCatalogConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.DataCatalogConfig)`)` Optional. The integration config for the Data Catalog service.  
  
### DataCatalogConfig

Specifies how metastore metadata should be integrated with the Data Catalog service.

JSON representation  
---  
      
    
    {
      "enabled": boolean
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Defines whether the metastore metadata should be synced to Data Catalog. The default value is to disable syncing metastore metadata to Data Catalog.  
  
### MaintenanceWindow

Maintenance window. This specifies when Dataproc Metastore may perform system maintenance operation to the service.

JSON representation  
---  
      
    
    {
      "hourOfDay": integer,
      "dayOfWeek": enum ([DayOfWeek](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/Shared.Types/DayOfWeek))
    }  
  
Fields  
---  
`hourOfDay` |  `integer` Optional. The hour of day (0-23) when the window starts.  
`dayOfWeek` |  `enum (`[DayOfWeek](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/Shared.Types/DayOfWeek)`)` Optional. The day of week, when the window starts.  
  
### MetadataManagementActivity

The metadata management activities of the metastore service.

JSON representation  
---  
      
    
    {
      "metadataExports": [
        {
          object ([MetadataExport](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataExport))
        }
      ],
      "restores": [
        {
          object ([Restore](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Restore))
        }
      ]
    }  
  
Fields  
---  
`metadataExports[]` |  `object (`[MetadataExport](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.MetadataExport)`)` Output only. The latest metadata exports of the metastore service.  
`restores[]` |  `object (`[Restore](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.Restore)`)` Output only. The latest restores of the metastore service.  
  
### MetadataExport

The details of a metadata export operation.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_1)),
      "databaseDumpType": enum ([Type](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/Type)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "destinationGcsUri": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the export started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the export ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_1)`)` Output only. The current state of the export.  
`databaseDumpType` |  `enum (`[Type](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/Type)`)` Output only. The type of the database dump.  
The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`destinationGcsUri` |  `string` Output only. A Cloud Storage URI of a folder that metadata are exported to, in the form of `gs://<bucket_name>/<path_inside_bucket>/<export_folder>`, where `<export_folder>` is automatically generated.  
End of mutually exclusive fields.  
  
### State

The current state of the metadata export.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the metadata export is unknown.  
`RUNNING` | The metadata export is running.  
`SUCCEEDED` | The metadata export completed successfully.  
`FAILED` | The metadata export failed.  
`CANCELLED` | The metadata export is cancelled.  
  
### Restore

The details of a metadata restore operation.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_2)),
      "backup": string,
      "type": enum ([RestoreType](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.RestoreType)),
      "details": string,
      "backupLocation": string
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the restore started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the restore ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_2)`)` Output only. The current state of the restore.  
`backup` |  `string` Output only. The relative resource name of the metastore service backup to restore from, in the following form:`projects/{projectId}/locations/{locationId}/services/{serviceId}/backups/{backupId}`.  
`type` |  `enum (`[RestoreType](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.RestoreType)`)` Output only. The type of restore.  
`details` |  `string` Output only. The restore details containing the revision of the service to be restored to, in format of JSON.  
`backupLocation` |  `string` Optional. A Cloud Storage URI specifying where the backup artifacts are stored, in the format `gs://<bucket_name>/<path_inside_bucket>`.  
  
### State

The current state of the restore.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the metadata restore is unknown.  
`RUNNING` | The metadata restore is running.  
`SUCCEEDED` | The metadata restore completed successfully.  
`FAILED` | The metadata restore failed.  
`CANCELLED` | The metadata restore is cancelled.  
  
### RestoreType

The type of restore. If unspecified, defaults to `METADATA_ONLY`.

Enums  
---  
`RESTORE_TYPE_UNSPECIFIED` | The restore type is unknown.  
`FULL` | The service's metadata and configuration are restored.  
`METADATA_ONLY` | Only the service's metadata is restored.  
  
### ReleaseChannel

Release channels bundle features of varying levels of stability. Newer features may be introduced initially into less stable release channels and can be automatically promoted into more stable release channels.

Enums  
---  
`RELEASE_CHANNEL_UNSPECIFIED` | Release channel is not specified.  
`CANARY` | The `CANARY` release channel contains the newest features, which may be unstable and subject to unresolved issues with no known workarounds. Services using the `CANARY` release channel are not subject to any SLAs.  
`STABLE` | The `STABLE` release channel contains features that are considered stable and have been validated for production use.  
  
### EncryptionConfig

Encryption settings for the service.

JSON representation  
---  
      
    
    {
      "kmsKey": string
    }  
  
Fields  
---  
`kmsKey` |  `string` Optional. The fully qualified customer provided Cloud KMS key name to use for customer data encryption, in the following format:`projects/{projectNumber}/locations/{locationId}/keyRings/{key_ring_id}/cryptoKeys/{crypto_key_id}`.  
  
### DatabaseType

The backend database type for the metastore service.

Enums  
---  
`DATABASE_TYPE_UNSPECIFIED` | The DATABASE_TYPE is not set.  
`MYSQL` | MySQL is used to persist the metastore data.  
`SPANNER` | Spanner is used to persist the metastore data.  
  
### TelemetryConfig

Telemetry Configuration for the Dataproc Metastore service.

JSON representation  
---  
      
    
    {
      "logFormat": enum ([LogFormat](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LogFormat))
    }  
  
Fields  
---  
`logFormat` |  `enum (`[LogFormat](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LogFormat)`)` Optional. The output format of the Dataproc Metastore service's logs.  
  
### LogFormat

Enums  
---  
`LOG_FORMAT_UNSPECIFIED` | The LOG_FORMAT is not set.  
`LEGACY` | Logging output uses the legacy `textPayload` format.  
`JSON` | Logging output uses the `jsonPayload` format.  
  
### ScalingConfig

Represents the scaling configuration of a metastore service.

JSON representation  
---  
      
    
    {
      "autoscalingConfig": {
        object ([AutoscalingConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.AutoscalingConfig))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "instanceSize": enum ([InstanceSize](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.InstanceSize)),
      "scalingFactor": number
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`autoscalingConfig` |  `object (`[AutoscalingConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.AutoscalingConfig)`)` Optional. The autoscaling configuration.  
Represents either a predetermined instance size or a numeric scaling factor. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`instanceSize` |  `enum (`[InstanceSize](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.InstanceSize)`)` An enum of readable instance sizes, with each instance size mapping to a float value (e.g. InstanceSize.EXTRA_SMALL = scalingFactor(0.1))  
`scalingFactor` |  `number` Scaling factor, increments of 0.1 for values less than 1.0, and increments of 1.0 for values greater than 1.0.  
End of mutually exclusive fields.  
  
### InstanceSize

Metastore instance sizes.

Enums  
---  
`INSTANCE_SIZE_UNSPECIFIED` | Unspecified instance size  
`EXTRA_SMALL` | Extra small instance size, maps to a scaling factor of 0.1.  
`SMALL` | Small instance size, maps to a scaling factor of 0.5.  
`MEDIUM` | Medium instance size, maps to a scaling factor of 1.0.  
`LARGE` | Large instance size, maps to a scaling factor of 3.0.  
`EXTRA_LARGE` | Extra large instance size, maps to a scaling factor of 6.0.  
  
### AutoscalingConfig

Represents the autoscaling configuration of a metastore service.

JSON representation  
---  
      
    
    {
      "autoscalingFactor": number,
      "autoscalingEnabled": boolean,
      "limitConfig": {
        object ([LimitConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LimitConfig))
      }
    }  
  
Fields  
---  
`autoscalingFactor` |  `number` Output only. The scaling factor of a service with autoscaling enabled.  
`autoscalingEnabled` |  `boolean` Optional. Whether or not autoscaling is enabled for this service.  
`limitConfig` |  `object (`[LimitConfig](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LimitConfig)`)` Optional. The LimitConfig of the service.  
  
### LimitConfig

Represents the autoscaling limit configuration of a metastore service.

JSON representation  
---  
      
    
    {
      "maxScalingFactor": number,
      "minScalingFactor": number
    }  
  
Fields  
---  
`maxScalingFactor` |  `number` Optional. The highest scaling factor that the service should be autoscaled to.  
`minScalingFactor` |  `number` Optional. The lowest scaling factor that the service should be autoscaled to.  
  
### ScheduledBackup

This specifies the configuration of scheduled backup.

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "cronSchedule": string,
      "timeZone": string,
      "nextScheduledTime": string,
      "backupLocation": string,
      "latestBackup": {
        object ([LatestBackup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LatestBackup))
      }
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Defines whether the scheduled backup is enabled. The default value is false.  
`cronSchedule` |  `string` Optional. The scheduled interval in Cron format, see <https://en.wikipedia.org/wiki/Cron> The default is empty: scheduled backup is not enabled. Must be specified to enable scheduled backups.  
`timeZone` |  `string` Optional. Specifies the time zone to be used when interpreting cronSchedule. Must be a time zone name from the time zone database (<https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)>, e.g. America/Los_Angeles or Africa/Abidjan. If left unspecified, the default is UTC.  
`nextScheduledTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the next backups execution is scheduled to start.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`backupLocation` |  `string` Optional. A Cloud Storage URI of a folder, in the format `gs://<bucket_name>/<path_inside_bucket>`. A sub-folder `<backup_folder>` containing backup files will be stored below it.  
`latestBackup` |  `object (`[LatestBackup](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.LatestBackup)`)` Output only. The details of the latest scheduled backup.  
  
### LatestBackup

The details of the latest scheduled backup.

JSON representation  
---  
      
    
    {
      "backupId": string,
      "startTime": string,
      "state": enum ([State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_3)),
      "duration": string
    }  
  
Fields  
---  
`backupId` |  `string` Output only. The ID of an in-progress scheduled backup. Empty if no backup is in progress.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the backup was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services#Service.State_3)`)` Output only. The current state of the backup.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the backup completion.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### State

The current state of the backup.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the backup is unknown.  
`IN_PROGRESS` | The backup is in progress.  
`SUCCEEDED` | The backup completed.  
`FAILED` | The backup failed.  
  
## Methods  
  
---  
  
### `[alterLocation](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/alterLocation)`

|  Alter metadata resource location.  
  
### `[alterTableProperties](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/alterTableProperties)`

|  Alter metadata table properties.  
  
### `[cancelMigration](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/cancelMigration)`

|  Cancels the ongoing Managed Migration process.  
  
### `[completeMigration](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/completeMigration)`

|  Completes the managed migration process.  
  
### `[create](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/create)`

|  Creates a metastore service in a project and location.  
  
### `[delete](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/delete)`

|  Deletes a single service.  
  
### `[exportMetadata](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/exportMetadata)`

|  Exports metadata from a service.  
  
### `[get](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/get)`

|  Gets the details of a single service.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/list)`

|  Lists services in a project and location.  
  
### `[moveTableToDatabase](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/moveTableToDatabase)`

|  Move a table to another database.  
  
### `[patch](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/patch)`

|  Updates the parameters of a single service.  
  
### `[queryMetadata](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/queryMetadata)`

|  Query Dataproc Metastore metadata.  
  
### `[restore](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/restore)`

|  Restores a service from a backup.  
  
### `[setIamPolicy](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[startMigration](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/startMigration)`

|  Starts the Managed Migration process.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dataproc-metastore/docs/reference/rest/v1/projects.locations.services/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
