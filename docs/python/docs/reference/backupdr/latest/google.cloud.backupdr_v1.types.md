---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types
title: Package types (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:43.633742+00:00
---

# Package types (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 

API documentation for `backupdr_v1.types` package.

## Classes 

### [AcceleratorConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AcceleratorConfig)

A specification of the type and number of accelerator cards attached to the instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AccessConfig)

An access configuration attached to an instance's network interface. Only one access config per instance is supported.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AdvancedMachineFeatures](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AdvancedMachineFeatures)

Specifies options for controlling advanced machine features.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AliasIpRange](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AliasIpRange)

An alias IP range attached to an instance's network interface.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AllocationAffinity](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AllocationAffinity)

Specifies the reservations that this instance can consume from.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AlloyDBClusterBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterBackupPlanAssociationProperties)

Properties for an AlloyDB cluster backup plan association.

### [AlloyDBClusterDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDBClusterDataSourceProperties)

AlloyDBClusterDataSourceProperties represents the properties of a AlloyDB cluster resource that are stored in the DataSource. .

### [AlloyDbClusterBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AlloyDbClusterBackupProperties)

AlloyDbClusterBackupProperties represents AlloyDB cluster backup properties. .

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AttachedDisk](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.AttachedDisk)

An instance-attached disk resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Backup](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Backup)

Message describing a Backup object.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupApplianceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupConfig)

BackupApplianceBackupConfig captures the backup configuration for applications that are protected by Backup Appliances.

### [BackupApplianceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupProperties)

BackupApplianceBackupProperties represents BackupDR backup appliance's properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupApplianceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceLockInfo)

BackupApplianceLockInfo contains metadata about the backupappliance that created the lock.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfigDetails](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails)

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo)

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupConfigState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigState)

Backup configuration state. Is the resource configured for backup?

### [BackupDrPlanConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrPlanConfig)

BackupDrPlanConfig has additional information about Google Cloud Backup and DR's Plan backup configuration.

### [BackupDrPlanRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrPlanRule)

BackupDrPlanRule has rule specific information of the backup plan resource.

### [BackupDrTemplateConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrTemplateConfig)

Provides additional information about Google Cloud Backup and DR's Template backup configuration.

### [BackupGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupGcpResource)

Minimum details to identify a Google Cloud resource for a backup.

### [BackupLocation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLocation)

BackupLocation represents a cloud location where a backup can be stored.

### [BackupLock](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLock)

BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupPlan](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlan)

A `BackupPlan` specifies some common fields, such as `description` as well as one or more `BackupRule` messages. Each `BackupRule` has a retention policy and defines a schedule by which the system is to perform backup workloads.

### [BackupPlanAssociation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanAssociation)

A BackupPlanAssociation represents a single BackupPlanAssociation which contains details like workload, backup plan etc

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupPlanRevision](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupPlanRevision)

`BackupPlanRevision` represents a snapshot of a `BackupPlan` at a point in time.

### [BackupRule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupRule)

`BackupRule` binds the backup schedule to a retention policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupVault](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault)

Message describing a BackupVault object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupVaultView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVaultView)

BackupVaultView contains enum options for Partial and Full view.

### [BackupView](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupView)

BackupView contains enum options for Partial and Full view.

### [BackupWindow](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupWindow)

`BackupWindow` defines a window of the day during which backup jobs will run.

### [CloudSqlInstanceBackupPlanAssociationProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupPlanAssociationProperties)

Cloud SQL instance's BPA properties.

### [CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceBackupProperties)

CloudSqlInstanceBackupProperties represents Cloud SQL Instance Backup properties.

### [CloudSqlInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceProperties)

CloudSqlInstanceDataSourceProperties represents the properties of a Cloud SQL resource that are stored in the DataSource.

### [CloudSqlInstanceDataSourceReferenceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceDataSourceReferenceProperties)

CloudSqlInstanceDataSourceReferenceProperties represents the properties of a Cloud SQL resource that are stored in the DataSourceReference.

### [CloudSqlInstanceInitializationConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CloudSqlInstanceInitializationConfig)

CloudSqlInstanceInitializationConfig contains the configuration for initializing a Cloud SQL instance.

### [ComputeInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceBackupProperties)

ComputeInstanceBackupProperties represents Compute Engine instance backup properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ComputeInstanceDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceDataSourceProperties)

ComputeInstanceDataSourceProperties represents the properties of a ComputeEngine resource that are stored in the DataSource.

### [ComputeInstanceRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceRestoreProperties)

ComputeInstanceRestoreProperties represents Compute Engine instance properties to be overridden during restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ComputeInstanceTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ComputeInstanceTargetEnvironment)

ComputeInstanceTargetEnvironment represents Compute Engine target environment to be used during restore.

### [ConfidentialInstanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ConfidentialInstanceConfig)

A set of Confidential Instance options.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CreateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanAssociationRequest)

Request message for creating a backup plan.

### [CreateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupPlanRequest)

The request message for creating a `BackupPlan`.

### [CreateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateBackupVaultRequest)

Message for creating a BackupVault.

### [CreateManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CreateManagementServerRequest)

Request message for creating a management server instance.

### [CustomerEncryptionKey](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.CustomerEncryptionKey)

A customer-supplied encryption key.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource)

Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceBackupApplianceApplication](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceBackupApplianceApplication)

BackupApplianceApplication describes a Source Resource when it is an application backed up by a BackupAppliance.

### [DataSourceBackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceBackupConfigInfo)

Information of backup configuration on the DataSource.

### [DataSourceGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResource)

DataSourceGcpResource is used for protected resources that are Google Cloud Resources. This name is easeier to understand than GcpResourceDataSource or GcpDataSourceResource

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceGcpResourceInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResourceInfo)

The GCP resource that the DataSource is associated with.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataSourceReference](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceReference)

DataSourceReference is a reference to a DataSource resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DeleteBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanAssociationRequest)

Request message for deleting a backup plan association.

### [DeleteBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupPlanRequest)

The request message for deleting a `BackupPlan`.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupRequest)

Message for deleting a Backup.

### [DeleteBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteBackupVaultRequest)

Message for deleting a BackupVault.

### [DeleteManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DeleteManagementServerRequest)

Request message for deleting a management server instance.

### [DiskBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskBackupProperties)

DiskBackupProperties represents the properties of a Disk backup.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DiskDataSourceProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskDataSourceProperties)

DiskDataSourceProperties represents the properties of a Disk resource that are stored in the DataSource. .

### [DiskRestoreProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskRestoreProperties)

DiskRestoreProperties represents the properties of a Disk restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DiskTargetEnvironment)

DiskTargetEnvironment represents the target environment for the disk.

### [DisplayDevice](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DisplayDevice)

A set of Display Device options

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Entry](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Entry)

A key/value pair to be used for storing metadata.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [FetchBackupPlanAssociationsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeRequest)

Request for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupPlanAssociationsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupPlanAssociationsForResourceTypeResponse)

Response for the FetchBackupPlanAssociationsForResourceType method.

### [FetchBackupsForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeRequest)

Request for the FetchBackupsForResourceType method.

### [FetchBackupsForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchBackupsForResourceTypeResponse)

Response for the FetchBackupsForResourceType method.

### [FetchDataSourceReferencesForResourceTypeRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeRequest)

Request for the FetchDataSourceReferencesForResourceType method.

### [FetchDataSourceReferencesForResourceTypeResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchDataSourceReferencesForResourceTypeResponse)

Response for the FetchDataSourceReferencesForResourceType method.

### [FetchUsableBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsRequest)

Request message for fetching usable BackupVaults.

### [FetchUsableBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.FetchUsableBackupVaultsResponse)

Response message for fetching usable BackupVaults.

### [GcpBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GcpBackupConfig)

GcpBackupConfig captures the Backup configuration details for Google Cloud resources. All Google Cloud resources regardless of type are protected with backup plan associations.

### [GcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GcpResource)

Minimum details to identify a Google Cloud resource

### [GetBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanAssociationRequest)

Request message for getting a BackupPlanAssociation resource.

### [GetBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRequest)

The request message for getting a `BackupPlan`.

### [GetBackupPlanRevisionRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupPlanRevisionRequest)

The request message for getting a `BackupPlanRevision`.

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupRequest)

Request message for getting a Backup.

### [GetBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetBackupVaultRequest)

Request message for getting a BackupVault.

### [GetDataSourceReferenceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceReferenceRequest)

Request for the GetDataSourceReference method.

### [GetDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetDataSourceRequest)

Request message for getting a DataSource instance.

### [GetManagementServerRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GetManagementServerRequest)

Request message for getting a management server instance.

### [GuestOsFeature](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GuestOsFeature)

Feature type of the Guest OS.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InitializeServiceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceRequest)

Request message for initializing the service.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [InitializeServiceResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InitializeServiceResponse)

Response message for initializing the service.

### [InstanceParams](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.InstanceParams)

Additional instance params.

### [KeyRevocationActionType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.KeyRevocationActionType)

Specifies whether the virtual machine instance will be shut down on key revocation. It is currently used in instance, instance properties and GMI protos

### [ListBackupPlanAssociationsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsRequest)

Request message for List BackupPlanAssociation

### [ListBackupPlanAssociationsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanAssociationsResponse)

Response message for List BackupPlanAssociation

### [ListBackupPlanRevisionsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsRequest)

The request message for getting a list of `BackupPlanRevision`.

### [ListBackupPlanRevisionsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlanRevisionsResponse)

The response message for getting a list of `BackupPlanRevision`.

### [ListBackupPlansRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansRequest)

The request message for getting a list `BackupPlan`.

### [ListBackupPlansResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupPlansResponse)

The response message for getting a list of `BackupPlan`.

### [ListBackupVaultsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsRequest)

Request message for listing backupvault stores.

### [ListBackupVaultsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupVaultsResponse)

Response message for listing BackupVaults.

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsRequest)

Request message for listing Backups.

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListBackupsResponse)

Response message for listing Backups.

### [ListDataSourceReferencesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesRequest)

Request for the ListDataSourceReferences method.

### [ListDataSourceReferencesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourceReferencesResponse)

Response for the ListDataSourceReferences method.

### [ListDataSourcesRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesRequest)

Request message for listing DataSources.

### [ListDataSourcesResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListDataSourcesResponse)

Response message for listing DataSources.

### [ListManagementServersRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersRequest)

Request message for listing management servers.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ListManagementServersResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListManagementServersResponse)

Response message for listing management servers.

### [ListResourceBackupConfigsRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsRequest)

Request for ListResourceBackupConfigs.

### [ListResourceBackupConfigsResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ListResourceBackupConfigsResponse)

Response for ListResourceBackupConfigs.

### [ManagementServer](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementServer)

ManagementServer describes a single BackupDR ManagementServer instance.

### [ManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ManagementURI)

ManagementURI for the Management Server resource.

### [Metadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Metadata)

A metadata key/value entry.

### [NetworkConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkConfig)

Network configuration for ManagementServer instance.

### [NetworkInterface](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkInterface)

A network interface resource attached to an instance. s

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NetworkPerformanceConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.NetworkPerformanceConfig)

Network performance configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PitrSettings](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.PitrSettings)

Point in time recovery settings of the backup configuration resource.

### [RegionDiskTargetEnvironment](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RegionDiskTargetEnvironment)

RegionDiskTargetEnvironment represents the target environment for the disk.

### [ResourceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ResourceBackupConfig)

ResourceBackupConfig represents a resource along with its backup configurations.

### [RestoreBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupRequest)

Request message for restoring from a Backup.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreBackupResponse](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RestoreBackupResponse)

Response message for restoring from a Backup.

### [RuleConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.RuleConfigInfo)

Message for rules config info.

### [Scheduling](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Scheduling)

Sets the scheduling options for an Instance.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SchedulingDuration](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.SchedulingDuration)

A SchedulingDuration represents a fixed-length span of time represented as a count of seconds and fractions of seconds at nanosecond resolution. It is independent of any calendar and concepts like "day" or "month". Range is approximately 10,000 years.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ServiceAccount)

A service account.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ServiceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.ServiceLockInfo)

ServiceLockInfo represents the details of a lock taken by the service on a Backup resource.

### [StandardSchedule](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.StandardSchedule)

`StandardSchedule` defines a schedule that run within the confines of a defined window of days. We can define recurrence type for schedule as HOURLY, DAILY, WEEKLY, MONTHLY or YEARLY.

### [Tags](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.Tags)

A set of instance tags.

### [TargetResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TargetResource)

Details of the target resource created/modified as part of restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TriggerBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.TriggerBackupRequest)

Request message for triggering a backup.

### [UpdateBackupPlanAssociationRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanAssociationRequest)

Request message for updating a backup plan association.

### [UpdateBackupPlanRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupPlanRequest)

Request message for updating a backup plan.

### [UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupRequest)

Request message for updating a Backup.

### [UpdateBackupVaultRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateBackupVaultRequest)

Request message for updating a BackupVault.

### [UpdateDataSourceRequest](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.UpdateDataSourceRequest)

Request message for updating a data source instance.

### [WeekDayOfMonth](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WeekDayOfMonth)

`WeekDayOfMonth` defines the week day of the month on which the backups will run. The message combines a `WeekOfMonth` and `DayOfWeek` to produce values like `FIRST`/`MONDAY` or `LAST`/`FRIDAY`.

### [WorkforceIdentityBasedManagementURI](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedManagementURI)

ManagementURI depending on the Workforce Identity i.e. either 1p or 3p.

### [WorkforceIdentityBasedOAuth2ClientID](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.WorkforceIdentityBasedOAuth2ClientID)

OAuth Client ID depending on the Workforce Identity i.e. either 1p or 3p,

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
