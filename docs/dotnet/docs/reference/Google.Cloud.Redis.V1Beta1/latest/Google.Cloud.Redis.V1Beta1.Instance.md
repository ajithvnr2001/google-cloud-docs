---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance
title: Google Cloud Memorystore for Redis v1beta1 API - Class Instance (3.0.0-beta06) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:00.779423+00:00
---

# Google Cloud Memorystore for Redis v1beta1 API - Class Instance (3.0.0-beta06)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Memorystore for Redis v1beta1 API - Class Instance (3.0.0-beta06) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 3.0.0-beta06 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)
  * [ 3.0.0-beta05 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/3.0.0-beta05/Google.Cloud.Redis.V1Beta1.Instance)
  * [ 2.0.0-beta09 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/2.0.0-beta09/Google.Cloud.Redis.V1Beta1.Instance)


    
    
    public sealed class Instance : IMessage<Instance>, IEquatable<Instance>, IDeepCloneable<Instance>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Memorystore for Redis v1beta1 API class Instance.

A Memorystore for Redis instance.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Instance

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Redis.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1)

## Assembly

Google.Cloud.Redis.V1Beta1.dll

## Constructors 

### Instance()
    
    
    public Instance()

### Instance(Instance)
    
    
    public Instance(Instance other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)`  
  
  
## Properties 

### AlternativeLocationId
    
    
    public string AlternativeLocationId { get; set; }

Optional. If specified, at least one node will be provisioned in this zone in addition to the zone specified in location_id. Only applicable to standard tier. If provided, it must be a different zone from the one provided in [location_id]. Additional nodes beyond the first 2 will be placed in zones selected by the service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### AuthEnabled
    
    
    public bool AuthEnabled { get; set; }

Optional. Indicates whether OSS Redis AUTH is enabled for the instance. If set to "true" AUTH is enabled on the instance. Default value is "false" meaning AUTH is disabled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### AuthorizedNetwork
    
    
    public string AuthorizedNetwork { get; set; }

Optional. The full name of the Google Compute Engine [network](https://cloud.google.com/vpc/docs/vpc) to which the instance is connected. If left unspecified, the `default` network will be used.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ConnectMode
    
    
    public Instance.Types.ConnectMode ConnectMode { get; set; }

Optional. The network connect mode of the Redis instance. If not provided, the connect mode defaults to DIRECT_PEERING.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)[ConnectMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.ConnectMode)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time the instance was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CurrentLocationId
    
    
    public string CurrentLocationId { get; set; }

Output only. The current zone where the Redis primary node is located. In basic tier, this will always be the same as [location_id]. In standard tier, this can be the zone of any node in the instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DisplayName
    
    
    public string DisplayName { get; set; }

An arbitrary and optional user-provided name for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Host
    
    
    public string Host { get; set; }

Output only. Hostname or IP address of the exposed Redis endpoint used by clients to connect to the service.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### InstanceName
    
    
    public InstanceName InstanceName { get; set; }

[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance#Google_Cloud_Redis_V1Beta1_Instance_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[InstanceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.InstanceName)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Resource labels to represent user provided metadata

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### LocationId
    
    
    public string LocationId { get; set; }

Optional. The zone where the instance will be provisioned. If not provided, the service will choose a zone from the specified region for the instance. For standard tier, additional nodes will be added across multiple zones for protection against zonal failures. If specified, at least one node will be provisioned in this zone.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### MaintenancePolicy
    
    
    public MaintenancePolicy MaintenancePolicy { get; set; }

Optional. The maintenance policy for the instance. If not provided, maintenance events can be performed at any time.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenancePolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenancePolicy)` |   
  
### MaintenanceSchedule
    
    
    public MaintenanceSchedule MaintenanceSchedule { get; set; }

Output only. Date and time of upcoming maintenance events which have been scheduled.

**Property Value**  
---  
**Type** | **Description**  
`[MaintenanceSchedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.MaintenanceSchedule)` |   
  
### MemorySizeGb
    
    
    public int MemorySizeGb { get; set; }

Required. Redis memory size in GiB.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. Unique name of the resource in this scope including project and location using the form: `projects/{project_id}/locations/{location_id}/instances/{instance_id}`

Note: Redis instances are managed and addressed at regional level so location_id here refers to a GCP region; however, users may choose which specific zone (or collection of zones for cross-zone instances) an instance should be provisioned in. Refer to [location_id][google.cloud.redis.v1beta1.Instance.location_id] and [alternative_location_id][google.cloud.redis.v1beta1.Instance.alternative_location_id] fields for more details.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Nodes
    
    
    public RepeatedField<NodeInfo> Nodes { get; }

Output only. Info per node.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[NodeInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.NodeInfo)` |   
  
### PersistenceConfig
    
    
    public PersistenceConfig PersistenceConfig { get; set; }

Optional. Persistence configuration parameters

**Property Value**  
---  
**Type** | **Description**  
`[PersistenceConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.PersistenceConfig)` |   
  
### PersistenceIamIdentity
    
    
    public string PersistenceIamIdentity { get; set; }

Output only. Cloud IAM identity used by import / export operations to transfer data to/from Cloud Storage. Format is "serviceAccount:<service_account_email>". The value may change over time for a given instance so should be checked before each import/export operation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Port
    
    
    public int Port { get; set; }

Output only. The port number of the exposed Redis endpoint.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReadEndpoint
    
    
    public string ReadEndpoint { get; set; }

Output only. Hostname or IP address of the exposed readonly Redis endpoint. Standard tier only. Targets all healthy replica nodes in instance. Replication is asynchronous and replica nodes will exhibit some lag behind the primary. Write requests must target 'host'.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReadEndpointPort
    
    
    public int ReadEndpointPort { get; set; }

Output only. The port number of the exposed readonly redis endpoint. Standard tier only. Write requests should target 'port'.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReadReplicasMode
    
    
    public Instance.Types.ReadReplicasMode ReadReplicasMode { get; set; }

Optional. Read replicas mode for the instance. Defaults to READ_REPLICAS_DISABLED.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)[ReadReplicasMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.ReadReplicasMode)` |   
  
### RedisConfigs
    
    
    public MapField<string, string> RedisConfigs { get; }

Optional. Redis configuration parameters, according to <http://redis.io/topics/config>. Currently, the only supported parameters are:

Redis version 3.2 and newer:

  * maxmemory-policy
  * notify-keyspace-events

Redis version 4.0 and newer:

  * activedefrag

  * lfu-decay-time
  * lfu-log-factor
  * maxmemory-gb

Redis version 5.0 and newer:

  * stream-node-max-bytes

  * stream-node-max-entries



**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RedisVersion
    
    
    public string RedisVersion { get; set; }

Optional. The version of Redis software. If not provided, latest supported version will be used. Currently, the supported values are:

  * `REDIS_3_2` for Redis 3.2 compatibility
  * `REDIS_4_0` for Redis 4.0 compatibility (default)
  * `REDIS_5_0` for Redis 5.0 compatibility
  * `REDIS_6_X` for Redis 6.x compatibility



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ReplicaCount
    
    
    public int ReplicaCount { get; set; }

Optional. The number of replica nodes. The valid range for the Standard Tier with read replicas enabled is [1-5] and defaults to 2. If read replicas are not enabled for a Standard Tier instance, the only valid value is 1 and the default is 1. The valid value for basic tier is 0 and the default is also 0.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ReservedIpRange
    
    
    public string ReservedIpRange { get; set; }

Optional. For DIRECT_PEERING mode, the CIDR range of internal addresses that are reserved for this instance. Range must be unique and non-overlapping with existing subnets in an authorized network. For PRIVATE_SERVICE_ACCESS mode, the name of one allocated IP address ranges associated with this private service access connection. If not provided, the service will choose an unused /29 block, for example, 10.0.0.0/29 or 192.168.0.0/29. For READ_REPLICAS_ENABLED the default block size is /28.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### SecondaryIpRange
    
    
    public string SecondaryIpRange { get; set; }

Optional. Additional IP range for node placement. Required when enabling read replicas on an existing instance. For DIRECT_PEERING mode value must be a CIDR range of size /28, or "auto". For PRIVATE_SERVICE_ACCESS mode value must be the name of an allocated address range associated with the private service access connection, or "auto".

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerCaCerts
    
    
    public RepeatedField<TlsCertificate> ServerCaCerts { get; }

Output only. List of server CA certificates for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[TlsCertificate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.TlsCertificate)` |   
  
### State
    
    
    public Instance.Types.State State { get; set; }

Output only. The current state of this instance.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)[State](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.State)` |   
  
### StatusMessage
    
    
    public string StatusMessage { get; set; }

Output only. Additional information about the current status of this instance, if available.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Tier
    
    
    public Instance.Types.Tier Tier { get; set; }

Required. The service tier of the instance.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)[Tier](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.Tier)` |   
  
### TransitEncryptionMode
    
    
    public Instance.Types.TransitEncryptionMode TransitEncryptionMode { get; set; }

Optional. The TLS mode of the Redis instance. If not provided, TLS is disabled for the instance.

**Property Value**  
---  
**Type** | **Description**  
`[Instance](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types)[TransitEncryptionMode](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.V1Beta1/latest/Google.Cloud.Redis.V1Beta1.Instance.Types.TransitEncryptionMode)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
