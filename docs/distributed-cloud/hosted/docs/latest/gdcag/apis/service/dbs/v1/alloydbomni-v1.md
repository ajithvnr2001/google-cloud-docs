---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/v1/alloydbomni-v1/
title: KRM API alloydbomni.dbadmin.gdc.goog/v1 \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:41.496523+00:00
---

# KRM API alloydbomni.dbadmin.gdc.goog/v1  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/apis/service/dbs/v1/alloydbomni-v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/reference/reference-overview)



Send feedback 

#  KRM API alloydbomni.dbadmin.gdc.goog/v1 Stay organized with collections  Save and categorize content based on your preferences. 

## alloydbomni.dbadmin.gdc.goog/v1

### AlInstanceSpec

_Appears in:_ \- DBClusterSpec

Field | Description  
---|---  
`version` _string_ | Version of a database. nullon(samwise-fleet,samwise-local)  
`images` _object (keys:string, values:string)_ | Deprecated: Replacement images for the database instance. nullon(samwise-fleet,samwise-local)  
`port` _integer_ | Port is the port number that the database is listening on. nullon(dbs-fleet,dbs-local)  
`component` _object (keys:InstanceComponentName, values:InstanceComponentSpec)_ | The list of instance components An instance is composed of dataplane and controlPlaneAgent components  
`dbLoadBalancerOptions` _DBLoadBalancerOptions_ | DBNetworkServiceOptions allows to override some details of kubernetes Service created to expose a connection to database.  
`sourceCidrRanges` _string array_ | Source IP CIDR ranges allowed for a client.  
`parameters` _object (keys:string, values:string)_ | Parameters allows to set database parameters for the database cluster. This field is optional. Parameters will take a key/value pair corresponding to the parameter name/value as defined by the database engine.  
`services` _object (keys:Service, values:boolean)_ | Services list the optional semi-managed services that the customers can choose from.  
`resources` _Resource_ | Resource specification for the database container. When any of the fields inside the resource changes, the operator restarts the database instance with the new resource specification.  
`mode` _InstanceMode_ | Mode specifies how this instance will be managed by the operator.  
`databasePatchingTimeout` _[Duration](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#duration-v1-meta)_ | The maximum duration allowed for patching the StatefulSet during container image updates. This threshold ensures that the database pods are updated within a specific time frame. If this field is unset, it will fall back to using the default maximum duration.  
`adminUser` _AdminUserSpec_ | AdminUser represents the admin user specification. This field is required. This is the initial database user that the control plane creates. Additional database users are managed by the end-user directly. This field can also be used to reset the password of the initial user.  
`systemUserPasswordRefs` _object (keys:string, values:string)_ | SystemUserPasswordRefs is a list of system users and the corresponding secrets containing the password for those accounts nullon(dbs-fleet,dbs-local)  
`isStopped` _boolean_ | IsStopped stops the instance when set to true. This field is optional and default to false. When stopped, the compute resources (CPU, memory) of the instance are released. However, the instance still keeps the storage resource and network endpoints so that restarting is transparent to the downstream services. See the status field for success or failures, if any.  
`availabilityOptions` _AvailabilityOptions_ | AvailabilityOptions contains adjustable settings for HA features  
`allowExternalIncomingTrafficToInstance` _boolean_ |   
`auditLogTarget` _AuditLogTargetSpec_ | AuditLogTarget configures the sink for the database audit logs  
`replication` _ReplicationSpec_ | Replication configures replication connections to other db instances nullon(samwise-fleet)  
`tls` _TLSSpec_ | TLS is the desired server certificate configuration for the instance. This field is optional. When this field is changed, the instance pods will restart to load the specified certificate  
`schedulingconfig` _SchedulingConfig_ | SchedulingConfig specifies how the instance should be scheduled on Kubernetes nodes. When any field inside the scheduling config changes, it can lead to rescheduling of the k8s pod onto a different node based on the config.  
`features` _Features_ | Specify AlloyDB Omni specific features  
  
### Backup

Backup is the Schema for the backups API

_Appears in:_ \- BackupList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `Backup`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupSpec_ |   
`status` _BackupStatus_ |   
  
### BackupList

BackupList contains a list of Backup

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `BackupList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Backup array_ |   
  
### BackupPlan

BackupPlan is the Schema for the backupplans API

_Appears in:_ \- BackupPlanList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `BackupPlan`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _BackupPlanSpec_ |   
`status` _BackupPlanStatus_ |   
  
### BackupPlanList

BackupPlanList contains a list of BackupPlan

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `BackupPlanList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _BackupPlan array_ |   
  
### BackupPlanSpec

BackupPlanSpec defines the desired state of BackupPlan.

_Appears in:_ \- BackupPlan

Field | Description  
---|---  
`dbclusterRef` _DBClusterRef_ | The DBCluster name this backupplan configures. This field is required and immutable.  
`backupRetainDays` _integer_ | Number of days after which the service will delete a Backup. If specified, a Backup created under this BackupPlan will be automatically deleted after its age reaches create_time + backup_retain_days. The valid values are from 1 to 90 days. Default to 14 retain days if not specified.  
`paused` _boolean_ | A flag to indicate if the backup creation under this BackupPlan is paused. If set to true, the service will pause the scheduling of new Backups under this BackupPlan. Default to False.  
`PITREnabled` _boolean_ | A flag to indicate whether logs replication is enabled to support point-in-time recovery. Default to False. nullon(samwise-fleet)  
  
### BackupPlanStatus

BackupPlanStatus defines the observed state of BackupPlan.

_Appears in:_ \- BackupPlan

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _BackupPlanPhase_ |   
`lastBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | LastBackupTime is the timestamp for the most recently executed backup.  
`nextBackupTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | NextBackupTime is the timestamp for the next scheduled backup.  
`recoveryWindow` _TimeWindow_ | RecoveryWindow is the currently available recovery window.  
`readWriteBackupRepositoryZone` _string_ | ReadWriteBackupRepositoryZone is the currently availability zone of the backup repository with ReadWrite import policy. nullon(samwise-fleet)  
  
### BackupSpec

BackupSpec defines the desired state of Backup.

_Appears in:_ \- Backup

Field | Description  
---|---  
`dbclusterRef` _DBClusterRef_ | The DBCluster name this backup belongs to. This field is required.  
`backupPlanRef` _BackupPlanRef_ | Name of the BackupPlan from which this backup was created. This field is required.  
`manual` _boolean_ | Indicate whether this backup is a scheduled or manual backup. This field is optional. Default to false (scheduled backup) if not specified.  
  
### BackupStatus

BackupStatus defines the observed state of Backup.

_Appears in:_ \- Backup

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _BackupPhase_ |   
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Creation time of the Backup  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Completion time of the Backup  
  
### CreateStandbyJob

CreateStandbyJob is an internal workflow tracking object. Users should not directly interact with this.

_Appears in:_ \- CreateStandbyJobList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `CreateStandbyJob`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _WorkflowSpec_ |   
`status` _EntityStatus_ |   
  
### CreateStandbyJobList

CreateStandbyJobList contains a list of CreateStandbyJobs

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `CreateStandbyJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _CreateStandbyJob array_ |   
  
### DBCluster

DBCluster is the Schema for the dbclusters API

_Appears in:_ \- DBClusterList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DBCluster`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _DBClusterSpec_ |   
`status` _DBClusterStatus_ |   
  
### DBClusterHealth

_Appears in:_ \- DBClusterHealthList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DBClusterHealth`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`status` _DBClusterHealthStatus_ |   
  
### DBClusterHealthList

DBClusterHealthList contains a list of DBClusterHealth

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DBClusterHealthList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DBClusterHealth array_ |   
  
### DBClusterHealthStatus

DBClusterHealthStatus represents the current health state of a DBCluster's instances.

_Appears in:_ \- DBClusterHealth

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`instances` _object (keys:string, values:InstanceHealthStatus)_ | Instances is a map keeping track of each of the health statuses of each instance.  
  
### DBClusterList

DBClusterList contains a list of DBCluster

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DBClusterList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DBCluster array_ |   
  
### DBClusterSpec

DBClusterSpec defines the desired state of DBCluster

_Appears in:_ \- DBCluster

Field | Description  
---|---  
`primaryCluster` _string_ | nullon(samwise-fleet)  
`isDeleted` _boolean_ | IsDeleted indicates a request to delete the DBCluster. This field is optional, and by default it is false. This fields applies to all instances of the database cluster. When set this to true, the control plane will attempt to release the related resources, including network endpoints. See the status fields for indication of success or failures, if any.  
`mode` _string_ | Indicate the mode of this DBCluster.  
`availability` _Availability_ | Availability contains adjustable settings for DBCluster HA features  
`allowExternalIncomingTraffic` _boolean_ | AllowExternalIncomingTraffic is used to toggle external load balancer creation.  
`tls` _TLSSpec_ | TLS is the desired server certificate configuration for the cluster. This field is optional. By default, this field is empty and a new self-signed CA and leaf certificate are generated for the cluster. When this field is changed, the database cluster pods will restart to load the specified certificate. The field `status.certificateReference` indicates the current CA certificate secret and key.  
`databaseVersion` _string_ | DatabaseVersion is the desired database version for the cluster for example, "15.4.5". This field is required. This version is applied to all instances of the database cluster. In the case of a new database cluster, the instance is created using the specified version. In the case of an existing database cluster, the operator attempts to upgrade or downgrade to the specified `databaseVersion`. The field `status.currentDatabaseVersion` indicates the current database version. See the list of available versions in {https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/choose-compatible-versions}. nullon(dbs-fleet)  
`databaseImageOSType` _ImageOSType_ | databaseImageOSType is an optional field to explicitly select the base operating system of the AlloyDBOmni database container image (e.g., Debian or UBI9). nullon(dbs-fleet)  
`controlPlaneAgentsVersion` _string_ | ControlPlaneAgentsVersion is the desired control plane agents version for the cluster for example, "0.5.2". This field is required. The `controlPlaneAgentsVersion` must be compatible with the chosen `databaseVersion`. To know what versions are compatible, check the list of available versions in {link}. This version is applied to all instances of the database cluster. In the case of a new database cluster, the instance is be created using the specified version. In the case of an existing database cluster, the operator will aptempt to upgrade or downgrade to the specified `controlPlaneAgentsVersion`. The field `status.currentControlPlaneAgentsVersion` indicates the current version for control plane agents. TODO(b/320311538): replace link with the list of available versions. nullon(dbs-fleet)  
`databaseImage` _string_ | DatabaseImage is the URI of a customized database image within the container registry, for example, "gcr.io/foo/bar/alloydbomni:15-7-2-customized". This field is optional. If `databaseImage` is specified, then the operator uses this container image for the database instead of the default database container image of the specified `databaseVersion`. We recommend that the `databaseImage` container will be based on the default database image used of the chosen `databaseVersion`. For more information about using a customized database image visit {link}. TODO(b/320311538): replace link with the guide for customizing database image. nullon(dbs-fleet)  
`primarySpec` _AlInstanceSpec_ |   
  
### DBClusterStatus

DBClusterStatus defines the observed state of DBCluster

_Appears in:_ \- DBCluster

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _DBClusterPhase_ |   
`primary` _PrimaryStatus_ | Primary contains the status of the primary Instance.  
`restoredFrom` _RestoredFrom_ |   
`upgradeScheduledAt` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | UpgradeScheduledAt is a timestamp that indicates when the next upgrade is scheduled to start. If it is nil, it means there is no upcoming upgrade scheduled. nullon(samwise-fleet)  
`serviceAccounts` _object (keys:OpType, values:ServiceAccountRef)_ | ServiceAccounts contains the service accounts created by the control plane to be used by different operations. By granting permissions to these service accounts, the database can interact with other services within the kubernetes ecosystem. For further information, including what permissions is required, refer to the documentation of each operation.  
`certificateReference` _CertificateRef_ | CertificateReference refers to a secret and a key of the server CA certificate that can be used to connect to the database. If `spec.TLS` is provided, this value should refer to the same secret after the database has been configured to use the provided server certificate.  
`tls` _TLSStatus_ | TLS is the current server certificate configuration for the database cluster.  
`latestFailoverStatus` _FailoverStatus_ | LatestFailoverStatus is the status of the most recently updated failover for the database cluster This status is a copy of the status of the current or most recently updated failover operation for the database cluster. This can be used to conveniently monitor the status of a currently running failover operation.  
`migrationStatus` _MigrationStatus_ | MigrationStatus represents the status of migration for the database cluster. nullon(samwise-fleet)  
`availabilityZones` _AvailabilityZones_ | AvailabilityZones represents the zone status for a multi-zone HA database cluster. nullon(samwise-fleet)  
`previousAvailabilityZones` _AvailabilityZones_ | PreviousAvailabilityZones represents the zone status for a multi-zone HA database cluster before a HA operation. nullon(samwise-fleet)  
  
### DeleteStandbyJob

DeleteStandbyJob is an internal workflow tracking object. Users should not directly interact with this.

_Appears in:_ \- DeleteStandbyJobList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DeleteStandbyJob`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _WorkflowSpec_ |   
`status` _EntityStatus_ |   
  
### DeleteStandbyJobList

DeleteStandbyJobList contains a list of DeleteStandbyJobs

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `DeleteStandbyJobList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _DeleteStandbyJob array_ |   
  
### Export

Export is the Schema for the export API.

_Appears in:_ \- ExportList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `Export`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ExportSpec_ |   
`status` _ExportStatus_ |   
  
### ExportList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `ExportList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Export array_ |   
  
### ExportSpec

ExportSpec defines the desired state of Export.

_Appears in:_ \- Export

Field | Description  
---|---  
`dbclusterRef` _DBClusterRef_ | DBClusterRef is the dbcluster name within the same namespace to export from.  
`exportLocation` _StorageSpec_ | ExportLocation specifies a storage location for the export files. A user is to ensure proper write access to the storage bucket from within the Operator.  
  
### ExportStatus

ExportStatus defines the observed state of Export.

_Appears in:_ \- Export

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _ExportPhase_ | Phase is a summary of current state of the export.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | StartTime is the time export started.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | CompleteTime is the time export completed.  
`exportSubDirectory` _string_ | ExportSubDirectory is the subdirectory appended to ExportLocation to store exported files.  
  
### ExternalServer

ExternalServer is the Schema for the ExternalServer API.

_Appears in:_ \- ExternalServerList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `ExternalServer`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ExternalServerSpec_ |   
`status` _ExternalServerStatus_ |   
  
### ExternalServerList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `ExternalServerList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _ExternalServer array_ |   
  
### ExternalServerSpec

ExternalServerSpec defines metadata of an external database server used for migration.

_Appears in:_ \- ExternalServer

Field | Description  
---|---  
`host` _string_ | Host is the host ip of the external database server.  
`port` _integer_ | Port is the port of the external database server.  
`username` _string_ | UserName is the name of the user used to connect to the external database.  
`password` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | Password is the reference to the secret storing external database server password.  
`certRef` _[SecretReference](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#secretreference-v1-core)_ | CertRef is the reference to the secret storing external database server certificate.  
  
### ExternalServerStatus

_Appears in:_ \- ExternalServer

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
  
### Import

Import is the Schema for the import API.

_Appears in:_ \- ImportList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `Import`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _ImportSpec_ |   
`status` _ImportStatus_ |   
  
### ImportList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `ImportList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Import array_ |   
  
### ImportSpec

ImportSpec defines the desired state of Import.

_Appears in:_ \- Import

Field | Description  
---|---  
`dbclusterRef` _DBClusterRef_ | DBClusterRef is the dbcluster name within the same namespace to import into.  
`databaseName` _string_ | DatabaseName is the database resource name within Instance to import into.  
`dumpStorage` _StorageSpec_ | DumpStorage specifies a storage location for the import dump files. A user is to ensure proper read access to the storage bucket from within the Operator.  
`logStorage` _StorageSpec_ | LogStorage optionally specifies a storage location to copy import log to. A user is to ensure proper write access to the storage bucket from within the Operator.  
`downloadOnly` _boolean_ | DownloadOnly when set to true means dump file will be downloaded but not imported into DB. Default is false.  
`tableExistAction` _string_ | TableExistAction is the action to take when importing into an existing table. The default is to skip.  
  
### ImportStatus

ImportStatus defines the observed state of Import.

_Appears in:_ \- Import

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _ImportPhase_ | Phase is a summary of current state of the import.  
`startTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | StartTime is the time import started.  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | CompleteTime is the time import completed.  
`dumpPath` _string_ | DumpPath is the path of the downloaded dump file for download only import.  
  
### Migration

Migration is the Schema for the migration API.

_Appears in:_ \- MigrationList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `Migration`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _MigrationSpec_ |   
`status` _MigrationStatus_ |   
  
### MigrationList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `MigrationList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Migration array_ |   
  
### MigrationSpec

MigrationSpec defines the spec of the migration job.

_Appears in:_ \- Migration

Field | Description  
---|---  
`source` _SourceDatabaseServer_ | Source is a database server that acts as the source for migration.  
`target` _TargetDatabaseServer_ | Target is a database server that acts as the target of migration.  
`control` _MigrationControl_ | Control is used to control the state of a migration job.  
  
### MigrationStatus

MigrationStatus defines the status of the migration job.

_Appears in:_ \- Migration

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
  
### Restore

Restore is the Schema for the restores API

_Appears in:_ \- RestoreList

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `Restore`  
`metadata` _[ObjectMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#objectmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`spec` _RestoreSpec_ |   
`status` _RestoreStatus_ |   
  
### RestoreList

RestoreList contains a list of Restores

Field | Description  
---|---  
`apiVersion` _string_ | `alloydbomni.dbadmin.gdc.goog/v1`  
`kind` _string_ | `RestoreList`  
`metadata` _[ListMeta](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#listmeta-v1-meta)_ | Refer to Kubernetes API documentation for fields of `metadata`.  
`items` _Restore array_ |   
  
### RestoreSpec

RestoreSpec defines the desired state of Restore.

_Appears in:_ \- Restore

Field | Description  
---|---  
`sourceDBCluster` _DBClusterRef_ | The name of the source DBCluster to restore from. This field is required.  
`pointInTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Previous point in time to restore to. This field is optional. Default to restore the latest available time point if not specified.  
`clonedDBClusterConfig` _ClonedDBClusterConfig_ | Settings for the cloned DBCluster. This lets you specify the name for the cloned DBCluster. This field is optional. Default to restore the source DBCluster if not specified.  
  
### RestoreStatus

RestoreStatus defines the observed state of Restore.

_Appears in:_ \- Restore

Field | Description  
---|---  
`observedGeneration` _integer_ | Internal: The generation observed by the controller.  
`reconciled` _boolean_ | Internal: Whether the resource was reconciled by the controller.  
`criticalIncidents` _CriticalIncident array_ | CriticalIncidents is a flat list of all active Critical Incidents.  
`conditions` _[Condition](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#condition-v1-meta) array_ | Conditions represents the latest available observations of the Entity's current state.  
`phase` _RestorePhase_ |   
`createTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Creation time of the Restore  
`completeTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Completion time of the Restore  
`restoredPointInTime` _[Time](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.25/#time-v1-meta)_ | Actual point-in-time this restore brings the target DBCluster into. Might be different from value specified in spec.PointInTime. nullon(samwise-fleet)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
