---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster
title: AlloyDB v1beta API - Class Cluster (1.0.0-beta19) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:09:10.422151+00:00
---

# AlloyDB v1beta API - Class Cluster (1.0.0-beta19)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  AlloyDB v1beta API - Class Cluster (1.0.0-beta19) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta19 (latest)  1.0.0-beta18 
    
    
    public sealed class Cluster : IMessage<Cluster>, IEquatable<Cluster>, IDeepCloneable<Cluster>, IBufferMessage, IMessage

Reference documentation and code samples for the AlloyDB v1beta API class Cluster.

A cluster is a collection of regional AlloyDB resources. It can include a primary instance and one or more read pool instances. All cluster resources share a storage layer, which scales as needed.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Cluster

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.AlloyDb.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta)

## Assembly

Google.Cloud.AlloyDb.V1Beta.dll

## Constructors 

### Cluster()
    
    
    public Cluster()

### Cluster(Cluster)
    
    
    public Cluster(Cluster other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)`  
  
  
## Properties 

### Annotations
    
    
    public MapField<string, string> Annotations { get; }

Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. <https://google.aip.dev/128>

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AutomatedBackupPolicy
    
    
    public AutomatedBackupPolicy AutomatedBackupPolicy { get; set; }

The automated backup policy for this cluster.

If no policy is provided then the default policy will be used. If backups are supported for the cluster, the default policy takes one backup a day, has a backup window of 1 hour, and retains backups for 14 days. For more information on the defaults, consult the documentation for the message type.

**Property Value**  
---  
**Type** | **Description**  
`[AutomatedBackupPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.AutomatedBackupPolicy)` |   
  
### BackupSource
    
    
    public BackupSource BackupSource { get; set; }

Output only. Cluster created from backup.

**Property Value**  
---  
**Type** | **Description**  
`[BackupSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.BackupSource)` |   
  
### CloudsqlBackupRunSource
    
    
    public CloudSQLBackupRunSource CloudsqlBackupRunSource { get; set; }

Output only. Cluster created from CloudSQL snapshot.

**Property Value**  
---  
**Type** | **Description**  
`[CloudSQLBackupRunSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.CloudSQLBackupRunSource)` |   
  
### ClusterName
    
    
    public ClusterName ClusterName { get; set; }

[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster#Google_Cloud_AlloyDb_V1Beta_Cluster_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ClusterName)` |   
  
### ClusterType
    
    
    public Cluster.Types.ClusterType ClusterType { get; set; }

Output only. The type of the cluster. This is an output-only field and it's populated at the Cluster creation time or the Cluster promotion time. The cluster type is determined by which RPC was used to create the cluster (i.e. `CreateCluster` vs. `CreateSecondaryCluster`

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[ClusterType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.ClusterType)` |   
  
### ContinuousBackupConfig
    
    
    public ContinuousBackupConfig ContinuousBackupConfig { get; set; }

Optional. Continuous backup configuration for this cluster.

**Property Value**  
---  
**Type** | **Description**  
`[ContinuousBackupConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ContinuousBackupConfig)` |   
  
### ContinuousBackupInfo
    
    
    public ContinuousBackupInfo ContinuousBackupInfo { get; set; }

Output only. Continuous backup properties for this cluster.

**Property Value**  
---  
**Type** | **Description**  
`[ContinuousBackupInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.ContinuousBackupInfo)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. Create time stamp

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DatabaseVersion
    
    
    public DatabaseVersion DatabaseVersion { get; set; }

Optional. The database engine major version. This is an optional field and it is populated at the Cluster creation time. If a database version is not supplied at cluster creation time, then a default database version will be used.

**Property Value**  
---  
**Type** | **Description**  
`[DatabaseVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.DatabaseVersion)` |   
  
### DataplexConfig
    
    
    public Cluster.Types.DataplexConfig DataplexConfig { get; set; }

Optional. Configuration for Dataplex integration.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[DataplexConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.DataplexConfig)` |   
  
### DeleteTime
    
    
    public Timestamp DeleteTime { get; set; }

Output only. Delete time stamp

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

User-settable and human-readable display name for the Cluster.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### EncryptionConfig
    
    
    public EncryptionConfig EncryptionConfig { get; set; }

Optional. The encryption config can be specified to encrypt the data disks and other persistent data resources of a cluster with a customer-managed encryption key (CMEK). When this field is not specified, the cluster will then use default encryption scheme to protect the user data.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.EncryptionConfig)` |   
  
### EncryptionInfo
    
    
    public EncryptionInfo EncryptionInfo { get; set; }

Output only. The encryption information for the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[EncryptionInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.EncryptionInfo)` |   
  
### Etag
    
    
    public string Etag { get; set; }

For Resource freshness validation (<https://google.aip.dev/154>)

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### GeminiConfig
    
    
    [Obsolete]
    public GeminiClusterConfig GeminiConfig { get; set; }

Optional. Deprecated and unused. This field will be removed in the near future.

**Property Value**  
---  
**Type** | **Description**  
`[GeminiClusterConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.GeminiClusterConfig)` |   
  
### InitialUser
    
    
    public UserPassword InitialUser { get; set; }

Input only. Initial user to setup during cluster creation. Required. If used in `RestoreCluster` this is ignored.

**Property Value**  
---  
**Type** | **Description**  
`[UserPassword](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.UserPassword)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels as key value pairs

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaintenanceSchedule
    
    
    public MaintenanceSchedule MaintenanceSchedule { get; set; }

Output only. The maintenance schedule for the cluster, generated for a specific rollout if a maintenance window is set.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceSchedule)` |   
  
### MaintenanceUpdatePolicy
    
    
    public MaintenanceUpdatePolicy MaintenanceUpdatePolicy { get; set; }

Optional. The maintenance update policy determines when to allow or deny updates.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceUpdatePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MaintenanceUpdatePolicy)` |   
  
### MigrationSource
    
    
    public MigrationSource MigrationSource { get; set; }

Output only. Cluster created via DMS migration.

**Property Value**  
---  
**Type** | **Description**  
`[MigrationSource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.MigrationSource)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The name of the cluster resource with the format:

  * projects/{project}/locations/{region}/clusters/{cluster_id} where the cluster ID segment should satisfy the regex expression `[a-z0-9-]+`. For more details see <https://google.aip.dev/122>. The prefix of the cluster resource name is the name of the parent resource:
  * projects/{project}/locations/{region}



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Network
    
    
    [Obsolete]
    public string Network { get; set; }

Required. The resource link for the VPC network in which cluster resources are created and from which they are accessible via Private IP. The network must belong to the same project as the cluster. It is specified in the form: `projects/{project}/global/networks/{network_id}`. This is required to create a cluster. Deprecated, use network_config.network instead.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NetworkAsNetworkName
    
    
    [Obsolete]
    public NetworkName NetworkAsNetworkName { get; set; }

[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.NetworkName)-typed view over the [Network](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster#Google_Cloud_AlloyDb_V1Beta_Cluster_Network) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[NetworkName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.NetworkName)` |   
  
### NetworkConfig
    
    
    public Cluster.Types.NetworkConfig NetworkConfig { get; set; }

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[NetworkConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.NetworkConfig)` |   
  
### PrimaryConfig
    
    
    public Cluster.Types.PrimaryConfig PrimaryConfig { get; set; }

Output only. Cross Region replication config specific to PRIMARY cluster.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[PrimaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.PrimaryConfig)` |   
  
### PscConfig
    
    
    public Cluster.Types.PscConfig PscConfig { get; set; }

Optional. The configuration for Private Service Connect (PSC) for the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[PscConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.PscConfig)` |   
  
### Reconciling
    
    
    public bool Reconciling { get; set; }

Output only. Reconciling (<https://google.aip.dev/128#reconciliation>). Set to true if the current state of Cluster does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SatisfiesPzs
    
    
    public bool SatisfiesPzs { get; set; }

Output only. Reserved for future use.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### SecondaryConfig
    
    
    public Cluster.Types.SecondaryConfig SecondaryConfig { get; set; }

Cross Region replication config specific to SECONDARY cluster.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[SecondaryConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.SecondaryConfig)` |   
  
### ServiceAccountEmail
    
    
    public string ServiceAccountEmail { get; set; }

Output only. AlloyDB per-cluster service account. This service account is created per-cluster per-project, and is different from the per-project service account. The per-cluster service account naming format is subject to change.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SourceCase
    
    
    public Cluster.SourceOneofCase SourceCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[SourceOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.SourceOneofCase)` |   
  
### SslConfig
    
    
    [Obsolete]
    public SslConfig SslConfig { get; set; }

SSL configuration for this AlloyDB cluster.

**Property Value**  
---  
**Type** | **Description**  
`[SslConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SslConfig)` |   
  
### State
    
    
    public Cluster.Types.State State { get; set; }

Output only. The current serving state of the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.State)` |   
  
### SubscriptionType
    
    
    public SubscriptionType SubscriptionType { get; set; }

Optional. Subscription type of the cluster.

**Property Value**  
---  
**Type** | **Description**  
`[SubscriptionType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.SubscriptionType)` |   
  
### Tags
    
    
    public MapField<string, string> Tags { get; }

Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example:
    
    
    "123/environment": "production",
    "123/costCenter": "marketing"
    

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TrialMetadata
    
    
    public Cluster.Types.TrialMetadata TrialMetadata { get; set; }

Output only. Metadata for free trial clusters

**Property Value**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types)[TrialMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AlloyDb.V1Beta/latest/Google.Cloud.AlloyDb.V1Beta.Cluster.Types.TrialMetadata)` |   
  
### Uid
    
    
    public string Uid { get; set; }

Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdateTime
    
    
    public Timestamp UpdateTime { get; set; }

Output only. Update time stamp

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
