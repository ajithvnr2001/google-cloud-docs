---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions
title: REST Resource: projects.instances.instancePartitions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:13.109412+00:00
---

# REST Resource: projects.instances.instancePartitions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  REST Resource: projects.instances.instancePartitions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InstancePartition
    * JSON representation
  * State
  * Methods



## Resource: InstancePartition

An isolated set of Cloud Spanner resources that databases can define placements on.

JSON representation  
---  
      
    
    {
      "name": string,
      "config": string,
      "displayName": string,
      "autoscalingConfig": {
        object ([AutoscalingConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig))
      },
      "state": enum ([State](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#State)),
      "createTime": string,
      "updateTime": string,
      "referencingDatabases": [
        string
      ],
      "referencingBackups": [
        string
      ],
      "etag": string,
    
      // Union field compute_capacity can be only one of the following:
      "nodeCount": integer,
      "processingUnits": integer
      // End of list of possible types for union field compute_capacity.
    }  
  
Fields  
---  
`name` |  `string` Required. A unique identifier for the instance partition. Values are of the form `projects/<project>/instances/<instance>/instancePartitions/[a-z][-a-z0-9]*[a-z0-9]`. The final segment of the name must be between 2 and 64 characters in length. An instance partition's name cannot be changed after the instance partition is created.  
`config` |  `string` Required. The name of the instance partition's configuration. Values are of the form `projects/<project>/instanceConfigs/<configuration>`. See also `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)` and `[ListInstanceConfigs](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs)`.  
`displayName` |  `string` Required. The descriptive name for this instance partition as it appears in UIs. Must be unique per project and between 4 and 30 characters in length.  
`autoscalingConfig` |  `object (`[AutoscalingConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig)`)` Optional. The autoscaling configuration. Autoscaling is enabled if this field is set. When autoscaling is enabled, fields in compute_capacity are treated as OUTPUT_ONLY fields and reflect the current compute capacity allocated to the instance partition.  
`state` |  `enum (`[State](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#State)`)` Output only. The current instance partition state.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the instance partition was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the instance partition was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`referencingDatabases[]` |  `string` Output only. The names of the databases that reference this instance partition. Referencing databases should share the parent instance. The existence of any referencing database prevents the instance partition from being deleted.  
`referencingBackups[]  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated: This field is not populated. Output only. The names of the backups that reference this instance partition. Referencing backups should share the parent instance. The existence of any referencing backup prevents the instance partition from being deleted.  
`etag` |  `string` Used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance partition from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance partition updates in order to avoid race conditions: An etag is returned in the response which contains instance partitions, and systems are expected to put that etag in the request to update instance partitions to ensure that their change will be applied to the same version of the instance partition. If no etag is provided in the call to update instance partition, then the existing instance partition is overwritten blindly.  
Union field `compute_capacity`. Compute capacity defines amount of server and storage resources that are available to the databases in an instance partition. At most, one of either `node_count` or`processing_units` should be present in the message. For more information, see [Compute capacity, nodes, and processing units](https://cloud.google.com/spanner/docs/compute-capacity). `compute_capacity` can be only one of the following:  
`nodeCount` |  `integer` The number of nodes allocated to this instance partition.Users can set the `nodeCount` field to specify the target number of nodes allocated to the instance partition.This may be zero in API responses for instance partitions that are not yet in state `READY`.  
`processingUnits` |  `integer` The number of processing units allocated to this instance partition.Users can set the `processingUnits` field to specify the target number of processing units allocated to the instance partition.This might be zero in API responses for instance partitions that are not yet in the `READY` state.  
  
## State

Indicates the current state of the instance partition.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | The instance partition is still being created. Resources may not be available yet, and operations such as creating placements using this instance partition may not work.  
`READY` | The instance partition is fully created and ready to do work such as creating placements and using in databases.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/create)`

|  Creates an instance partition and begins preparing it to be used.  
  
### `[delete](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/delete)`

|  Deletes an existing instance partition.  
  
### `[get](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/get)`

|  Gets information about a particular instance partition.  
  
### `[list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list)`

|  Lists all instance partitions for the given instance.  
  
### `[patch](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/patch)`

|  Updates an instance partition, and begins allocating or releasing resources as requested.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
