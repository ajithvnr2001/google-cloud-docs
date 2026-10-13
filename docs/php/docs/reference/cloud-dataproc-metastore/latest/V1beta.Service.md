---
url: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service
title: Google Cloud Dataproc Metastore V1beta Client - Class Service (1.3.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:41.704822+00:00
---

# Google Cloud Dataproc Metastore V1beta Client - Class Service (1.3.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Dataproc Metastore V1beta Client - Class Service (1.3.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.3.3 (latest)  1.2.4  1.1.1  1.0.4  0.11.5  0.10.2  0.9.0  0.8.1  0.7.0  0.6.1  0.5.1  0.4.1 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Dataproc Metastore V1beta Client class Service.

A managed metastore service that serves metadata queries.

Generated from protobuf message `google.cloud.metastore.v1beta.Service`

## Namespace

Google \ Cloud \ Metastore \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ hive_metastore_config` |  `[HiveMetastoreConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.HiveMetastoreConfig)`   
Configuration information specific to running Hive metastore software as the metastore service.  
`↳ name` |  `string`   
Immutable. The relative resource name of the metastore service, in the following format: `projects/{project_number}/locations/{location_id}/services/{service_id}`.  
`↳ create_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the metastore service was created.  
`↳ update_time` |  `Google\Protobuf\Timestamp`   
Output only. The time when the metastore service was last updated.  
`↳ labels` |  `array|Google\Protobuf\Internal\MapField`   
User-defined labels for the metastore service.  
`↳ network` |  `string`   
Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form: `projects/{project_number}/global/networks/{network_id}`.  
`↳ endpoint_uri` |  `string`   
Output only. The URI of the endpoint used to access the metastore service.  
`↳ port` |  `int`   
The TCP port at which the metastore service is reached. Default: 9083.  
`↳ state` |  `int`   
Output only. The current state of the metastore service.  
`↳ state_message` |  `string`   
Output only. Additional information about the current state of the metastore service, if available.  
`↳ artifact_gcs_uri` |  `string`   
Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.  
`↳ tier` |  `int`   
The tier of the service.  
`↳ metadata_integration` |  `[MetadataIntegration](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataIntegration)`   
The setting that defines how metastore metadata should be integrated with external services and systems.  
`↳ maintenance_window` |  `[MaintenanceWindow](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MaintenanceWindow)`   
The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time. Maintenance window is not needed for services with the SPANNER database type.  
`↳ uid` |  `string`   
Output only. The globally unique resource identifier of the metastore service.  
`↳ metadata_management_activity` |  `[MetadataManagementActivity](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataManagementActivity)`   
Output only. The metadata management activities of the metastore service.  
`↳ release_channel` |  `int`   
Immutable. The release channel of the service. If unspecified, defaults to `STABLE`.  
`↳ encryption_config` |  `[EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.EncryptionConfig)`   
Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.  
`↳ network_config` |  `[NetworkConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.NetworkConfig)`   
The configuration specifying the network settings for the Dataproc Metastore service.  
`↳ database_type` |  `int`   
Immutable. The database type that the Metastore service stores its data.  
`↳ telemetry_config` |  `[TelemetryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.TelemetryConfig)`   
The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.  
`↳ scaling_config` |  `[ScalingConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ScalingConfig)`   
Scaling configuration of the metastore service.  
  
### getHiveMetastoreConfig

Configuration information specific to running Hive metastore software as the metastore service.

**Returns**  
---  
**Type** | **Description**  
`[HiveMetastoreConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.HiveMetastoreConfig)|null` |   
  
### hasHiveMetastoreConfig

### setHiveMetastoreConfig

Configuration information specific to running Hive metastore software as the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[HiveMetastoreConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.HiveMetastoreConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getName

Immutable. The relative resource name of the metastore service, in the following format: `projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

Immutable. The relative resource name of the metastore service, in the following format: `projects/{project_number}/locations/{location_id}/services/{service_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCreateTime

Output only. The time when the metastore service was created.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasCreateTime

### clearCreateTime

### setCreateTime

Output only. The time when the metastore service was created.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateTime

Output only. The time when the metastore service was last updated.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasUpdateTime

### clearUpdateTime

### setUpdateTime

Output only. The time when the metastore service was last updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getLabels

User-defined labels for the metastore service.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Internal\MapField` |   
  
### setLabels

User-defined labels for the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|Google\Protobuf\Internal\MapField`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNetwork

Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form: `projects/{project_number}/global/networks/{network_id}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNetwork

Immutable. The relative resource name of the VPC network on which the instance can be accessed. It is specified in the following form: `projects/{project_number}/global/networks/{network_id}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndpointUri

Output only. The URI of the endpoint used to access the metastore service.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEndpointUri

Output only. The URI of the endpoint used to access the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPort

The TCP port at which the metastore service is reached. Default: 9083.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPort

The TCP port at which the metastore service is reached. Default: 9083.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getState

Output only. The current state of the metastore service.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.State).  
  
### setState

Output only. The current state of the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [State](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.State).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStateMessage

Output only. Additional information about the current state of the metastore service, if available.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setStateMessage

Output only. Additional information about the current state of the metastore service, if available.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getArtifactGcsUri

Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setArtifactGcsUri

Output only. A Cloud Storage URI (starting with `gs://`) that specifies where artifacts related to the metastore service are stored.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTier

The tier of the service.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [Tier](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.Tier).  
  
### setTier

The tier of the service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [Tier](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.Tier).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadataIntegration

The setting that defines how metastore metadata should be integrated with external services and systems.

**Returns**  
---  
**Type** | **Description**  
`[MetadataIntegration](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataIntegration)|null` |   
  
### hasMetadataIntegration

### clearMetadataIntegration

### setMetadataIntegration

The setting that defines how metastore metadata should be integrated with external services and systems.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MetadataIntegration](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataIntegration)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMaintenanceWindow

The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time.

Maintenance window is not needed for services with the SPANNER database type.

**Returns**  
---  
**Type** | **Description**  
`[MaintenanceWindow](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MaintenanceWindow)|null` |   
  
### hasMaintenanceWindow

### clearMaintenanceWindow

### setMaintenanceWindow

The one hour maintenance window of the metastore service. This specifies when the service can be restarted for maintenance purposes in UTC time.

Maintenance window is not needed for services with the SPANNER database type.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MaintenanceWindow](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MaintenanceWindow)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUid

Output only. The globally unique resource identifier of the metastore service.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setUid

Output only. The globally unique resource identifier of the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetadataManagementActivity

Output only. The metadata management activities of the metastore service.

**Returns**  
---  
**Type** | **Description**  
`[MetadataManagementActivity](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataManagementActivity)|null` |   
  
### hasMetadataManagementActivity

### clearMetadataManagementActivity

### setMetadataManagementActivity

Output only. The metadata management activities of the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MetadataManagementActivity](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.MetadataManagementActivity)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getReleaseChannel

Immutable. The release channel of the service.

If unspecified, defaults to `STABLE`.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ReleaseChannel](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.ReleaseChannel).  
  
### setReleaseChannel

Immutable. The release channel of the service.

If unspecified, defaults to `STABLE`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ReleaseChannel](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.ReleaseChannel).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEncryptionConfig

Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.

**Returns**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.EncryptionConfig)|null` |   
  
### hasEncryptionConfig

### clearEncryptionConfig

### setEncryptionConfig

Immutable. Information used to configure the Dataproc Metastore service to encrypt customer data at rest. Cannot be updated.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EncryptionConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.EncryptionConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNetworkConfig

The configuration specifying the network settings for the Dataproc Metastore service.

**Returns**  
---  
**Type** | **Description**  
`[NetworkConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.NetworkConfig)|null` |   
  
### hasNetworkConfig

### clearNetworkConfig

### setNetworkConfig

The configuration specifying the network settings for the Dataproc Metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[NetworkConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.NetworkConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDatabaseType

Immutable. The database type that the Metastore service stores its data.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [DatabaseType](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.DatabaseType).  
  
### setDatabaseType

Immutable. The database type that the Metastore service stores its data.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [DatabaseType](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.Service.DatabaseType).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTelemetryConfig

The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.

**Returns**  
---  
**Type** | **Description**  
`[TelemetryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.TelemetryConfig)|null` |   
  
### hasTelemetryConfig

### clearTelemetryConfig

### setTelemetryConfig

The configuration specifying telemetry settings for the Dataproc Metastore service. If unspecified defaults to `JSON`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[TelemetryConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.TelemetryConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getScalingConfig

Scaling configuration of the metastore service.

**Returns**  
---  
**Type** | **Description**  
`[ScalingConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ScalingConfig)|null` |   
  
### hasScalingConfig

### clearScalingConfig

### setScalingConfig

Scaling configuration of the metastore service.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ScalingConfig](https://docs.cloud.google.com/php/docs/reference/cloud-dataproc-metastore/latest/V1beta.ScalingConfig)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getMetastoreConfig

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
