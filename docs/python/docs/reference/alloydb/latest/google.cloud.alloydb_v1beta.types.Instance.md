---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance
title: Class Instance (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:54.608717+00:00
---

# Class Instance (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Instance (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    Instance(mapping=None, *, ignore_unknown_fields=False, **kwargs)

An Instance is a computing unit that an end customer can connect to. It's the main unit of computing resources in AlloyDB.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The name of the instance resource with the format: \- projects/{project}/locations/{region}/clusters/{cluster_id}/instances/{instance_id} where the cluster and instance ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the instance resource name is the name of the parent resource: \- projects/{project}/locations/{region}/clusters/{cluster_id}   
`display_name` |  `str`   
User-settable and human-readable display name for the Instance.   
`uid` |  `str`   
Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time stamp   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Delete time stamp   
`labels` |  `MutableMapping[str, str]`   
Labels as key value pairs   
`state` |  `[google.cloud.alloydb_v1beta.types.Instance.State](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.State)`   
Output only. The current serving state of the instance.   
`instance_type` |  `[google.cloud.alloydb_v1beta.types.Instance.InstanceType](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.InstanceType)`   
Required. The type of the instance. Specified at creation time.   
`machine_config` |  `[google.cloud.alloydb_v1beta.types.Instance.MachineConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.MachineConfig)`   
Configurations for the machines that host the underlying database engine.   
`availability_type` |  `[google.cloud.alloydb_v1beta.types.Instance.AvailabilityType](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.AvailabilityType)`   
Availability type of an Instance. If empty, defaults to REGIONAL for primary instances. For read pools, availability_type is always UNSPECIFIED. Instances in the read pools are evenly distributed across available zones within the region (i.e. read pools with more than one node will have a node in at least two zones).   
`gce_zone` |  `str`   
The Compute Engine zone that the instance should serve from, per https://cloud.google.com/compute/docs/regions-zones This can ONLY be specified for ZONAL instances. If present for a REGIONAL instance, an error will be thrown. If this is absent for a ZONAL instance, instance is created in a random zone with available capacity.   
`database_flags` |  `MutableMapping[str, str]`   
Database flags. Set at the instance level. They are copied from the primary instance on secondary instance creation. Flags that have restrictions default to the value at primary instance on read instances during creation. Read instances can set new flags or override existing flags that are relevant for reads, for example, for enabling columnar cache on a read instance. Flags set on read instance might or might not be present on the primary instance. This is a list of "key": "value" pairs. "key": The name of the flag. These flags are passed at instance setup time, so include both server options and system variables for Postgres. Flags are specified with underscores, not hyphens. "value": The value of the flag. Booleans are set to **on** for true and **off** for false. This field must be omitted if the flag doesn't take a value.   
`writable_node` |  `[google.cloud.alloydb_v1beta.types.Instance.Node](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.Node)`   
Output only. This is set for the read-write VM of the PRIMARY instance only.   
`nodes` |  `MutableSequence[[google.cloud.alloydb_v1beta.types.Instance.Node](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.Node)]`   
Output only. List of available read-only VMs in this instance, including the standby for a PRIMARY instance.   
`query_insights_config` |  `[google.cloud.alloydb_v1beta.types.Instance.QueryInsightsInstanceConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.QueryInsightsInstanceConfig)`   
Configuration for query insights.   
`observability_config` |  `[google.cloud.alloydb_v1beta.types.Instance.ObservabilityInstanceConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.ObservabilityInstanceConfig)`   
Configuration for observability.   
`read_pool_config` |  `[google.cloud.alloydb_v1beta.types.Instance.ReadPoolConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.ReadPoolConfig)`   
Read pool instance configuration. This is required if the value of instanceType is READ_POOL.   
`ip_address` |  `str`   
Output only. The IP address for the Instance. This is the connection endpoint for an end-user application.   
`public_ip_address` |  `str`   
Output only. The public IP addresses for the Instance. This is available ONLY when enable_public_ip is set. This is the connection endpoint for an end-user application.   
`reconciling` |  `bool`   
Output only. Reconciling (https://google.aip.dev/128#reconciliation). Set to true if the current state of Instance does not match the user's intended state, and the service is actively updating the resource to reconcile them. This can happen due to user-triggered updates or system actions like failover or maintenance.   
`etag` |  `str`   
For Resource freshness validation (https://google.aip.dev/154)   
`annotations` |  `MutableMapping[str, str]`   
Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128   
`update_policy` |  `[google.cloud.alloydb_v1beta.types.Instance.UpdatePolicy](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.UpdatePolicy)`   
Update policy that will be applied during instance update. This field is not persisted when you update the instance. To use a non-default update policy, you must specify explicitly specify the value in each update request.   
`client_connection_config` |  `[google.cloud.alloydb_v1beta.types.Instance.ClientConnectionConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.ClientConnectionConfig)`   
Optional. Client connection specific configurations   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use.   
`psc_instance_config` |  `[google.cloud.alloydb_v1beta.types.Instance.PscInstanceConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.PscInstanceConfig)`   
Optional. The configuration for Private Service Connect (PSC) for the instance.   
`psc_instance_info` |  `[google.cloud.alloydb_v1beta.types.Instance.PscInstanceInfo](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.PscInstanceInfo)`   
Output only. Information about the Private Service Connect (PSC) for the instance.   
`network_config` |  `[google.cloud.alloydb_v1beta.types.Instance.InstanceNetworkConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.InstanceNetworkConfig)`   
Optional. Instance-level network configuration.   
`gemini_config` |  `[google.cloud.alloydb_v1beta.types.GeminiInstanceConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.GeminiInstanceConfig)`   
Optional. Deprecated and unused. This field will be removed in the near future.   
`outbound_public_ip_addresses` |  `MutableSequence[str]`   
Output only. All outbound public IP addresses configured for the instance.   
`activation_policy` |  `[google.cloud.alloydb_v1beta.types.Instance.ActivationPolicy](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.ActivationPolicy)`   
Optional. Specifies whether an instance needs to spin up. Once the instance is active, the activation policy can be updated to the `NEVER` to stop the instance. Likewise, the activation policy can be updated to `ALWAYS` to start the instance. There are restrictions around when an instance can/cannot be activated (for example, a read pool instance should be stopped before stopping primary etc.). Please refer to the API documentation for more details.   
`connection_pool_config` |  `[google.cloud.alloydb_v1beta.types.Instance.ConnectionPoolConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.Instance.ConnectionPoolConfig)`   
Optional. The configuration for Managed Connection Pool (MCP).   
`gca_config` |  `[google.cloud.alloydb_v1beta.types.GCAInstanceConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1beta.types.GCAInstanceConfig)`   
Output only. Configuration parameters related to Gemini Cloud Assist.   
  
## Classes 

### ActivationPolicy
    
    
    ActivationPolicy(value)

Specifies whether an instance needs to spin up.

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### AvailabilityType
    
    
    AvailabilityType(value)

The Availability type of an instance. Potential values:

  * ZONAL: The instance serves data from only one zone. Outages in that zone affect instance availability.
  * REGIONAL: The instance can serve data from more than one zone in a region (it is highly available).



### ClientConnectionConfig
    
    
    ClientConnectionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Client connection configuration

### ConnectionPoolConfig
    
    
    ConnectionPoolConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for Managed Connection Pool (MCP).

### DatabaseFlagsEntry
    
    
    DatabaseFlagsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### InstanceNetworkConfig
    
    
    InstanceNetworkConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Metadata related to instance-level network configuration.

### InstanceType
    
    
    InstanceType(value)

Type of an Instance
    
    
        - Read pool of size 1 can only have zonal availability.
        - Read pools with node count of 2 or more can have regional
          availability (nodes are present in 2 or more zones in a
          region).
    SECONDARY (3):
        SECONDARY instances support read operations
        only. SECONDARY instance is a cross-region read
        replica
    

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### MachineConfig
    
    
    MachineConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

MachineConfig describes the configuration of a machine.

### Node
    
    
    Node(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Details of a single node in the instance. Nodes in an AlloyDB instance are ephemeral, they can change during update, failover, autohealing and resize operations.

### ObservabilityInstanceConfig
    
    
    ObservabilityInstanceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Observability Instance specific configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### PscAutoConnectionConfig
    
    
    PscAutoConnectionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for setting up PSC service automation. Consumer projects in the configs will be allowlisted automatically for the instance.

### PscAutoDnsState
    
    
    PscAutoDnsState(value)

The state of the PSC auto DNS.

### PscInstanceConfig
    
    
    PscInstanceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

PscInstanceConfig contains PSC related configuration at an instance level.

### PscInstanceInfo
    
    
    PscInstanceInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Information about the Private Service Connect (PSC) for the instance.

### PscInterfaceConfig
    
    
    PscInterfaceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for setting up a PSC interface to enable outbound connectivity.

### QueryInsightsInstanceConfig
    
    
    QueryInsightsInstanceConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

QueryInsights Instance specific configuration.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### ReadPoolConfig
    
    
    ReadPoolConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Configuration for a read pool instance.

### State
    
    
    State(value)

Instance State

### UpdatePolicy
    
    
    UpdatePolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Policy to be used while updating the instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
