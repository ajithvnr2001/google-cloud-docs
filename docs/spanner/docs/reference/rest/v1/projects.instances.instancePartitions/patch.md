---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/patch/
title: Method: projects.instances.instancePartitions.patch \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:14.027336+00:00
---

# Method: projects.instances.instancePartitions.patch  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.instancePartitions.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
      * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Updates an instance partition, and begins allocating or releasing resources as requested. The returned long-running operation can be used to track the progress of updating the instance partition. If the named instance partition does not exist, returns `NOT_FOUND`.

Immediately upon completion of this request:

  * For resource types for which a decrease in the instance partition's allocation has been requested, billing is based on the newly-requested level.



Until completion of the returned operation:

  * Cancelling the operation sets its metadata's `[cancelTime](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateInstancePartitionMetadata#FIELDS.cancel_time)`, and begins restoring resources to their pre-request values. The operation is guaranteed to succeed at undoing all resource changes, after which point it terminates with a `CANCELLED` status.
  * All other attempts to modify the instance partition are rejected.
  * Reading the instance partition via the API continues to give the pre-request resource levels.



Upon completion of the returned operation:

  * Billing begins for all successfully-allocated resources (some types may have lower than the requested levels).
  * All newly-reserved resources are available for serving the instance partition's tables.
  * The instance partition's new resource levels are readable via the API.



The returned long-running operation will have a name of the format `<instance_partition_name>/operations/<operationId>` and can be used to track the instance partition modification. The metadata field type is `[UpdateInstancePartitionMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateInstancePartitionMetadata)`. The response field type is `[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)`, if successful.

Authorization requires `spanner.instancePartitions.update` permission on the resource `[name](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition.FIELDS.name)`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`PATCH https://spanner.googleapis.com/v1/{instancePartition.name=projects/*/instances/*/instancePartitions/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`instancePartition.name` |  `string` Required. A unique identifier for the instance partition. Values are of the form `projects/<project>/instances/<instance>/instancePartitions/[a-z][-a-z0-9]*[a-z0-9]`. The final segment of the name must be between 2 and 64 characters in length. An instance partition's name cannot be changed after the instance partition is created.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instancePartition": {
        "name": string,
        "config": string,
        "displayName": string,
        "nodeCount": integer,
        "processingUnits": integer,
        "autoscalingConfig": {
          "autoscalingLimits": {
            object ([AutoscalingLimits](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig#AutoscalingLimits))
          },
          "autoscalingTargets": {
            object ([AutoscalingTargets](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig#AutoscalingTargets))
          },
          "asymmetricAutoscalingOptions": [
            {
              object ([AsymmetricAutoscalingOption](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig#AsymmetricAutoscalingOption))
            }
          ]
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
        "etag": string
      },
      "fieldMask": string
    }  
  
Fields  
---  
`instancePartition.config` |  `string` Required. The name of the instance partition's configuration. Values are of the form `projects/<project>/instanceConfigs/<configuration>`. See also `[InstanceConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs#InstanceConfig)` and `[ListInstanceConfigs](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs)`.  
`instancePartition.displayName` |  `string` Required. The descriptive name for this instance partition as it appears in UIs. Must be unique per project and between 4 and 30 characters in length.  
`instancePartition.autoscalingConfig` |  `object (`[AutoscalingConfig](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/AutoscalingConfig)`)` Optional. The autoscaling configuration. Autoscaling is enabled if this field is set. When autoscaling is enabled, fields in compute_capacity are treated as OUTPUT_ONLY fields and reflect the current compute capacity allocated to the instance partition.  
`instancePartition.state` |  `enum (`[State](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#State)`)` Output only. The current instance partition state.  
`instancePartition.createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the instance partition was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`instancePartition.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which the instance partition was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`instancePartition.referencingDatabases[]` |  `string` Output only. The names of the databases that reference this instance partition. Referencing databases should share the parent instance. The existence of any referencing database prevents the instance partition from being deleted.  
`instancePartition.referencingBackups[]  
**(deprecated)**` |  `string` Output only. Deprecated: This field is not populated. Output only. The names of the backups that reference this instance partition. Referencing backups should share the parent instance. The existence of any referencing backup prevents the instance partition from being deleted.  
`instancePartition.etag` |  `string` Used for optimistic concurrency control as a way to help prevent simultaneous updates of a instance partition from overwriting each other. It is strongly suggested that systems make use of the etag in the read-modify-write cycle to perform instance partition updates in order to avoid race conditions: An etag is returned in the response which contains instance partitions, and systems are expected to put that etag in the request to update instance partitions to ensure that their change will be applied to the same version of the instance partition. If no etag is provided in the call to update instance partition, then the existing instance partition is overwritten blindly.  
`fieldMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. A mask specifying which fields in `[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)` should be updated. The field mask must always be specified; this prevents any future fields in `[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)` from being erased accidentally by clients that do not know about them.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
Union field `compute_capacity`. Compute capacity defines amount of server and storage resources that are available to the databases in an instance partition. At most, one of either `node_count` or`processing_units` should be present in the message. For more information, see [Compute capacity, nodes, and processing units](https://cloud.google.com/spanner/docs/compute-capacity). `compute_capacity` can be only one of the following:  
`instancePartition.nodeCount` |  `integer` The number of nodes allocated to this instance partition.Users can set the `nodeCount` field to specify the target number of nodes allocated to the instance partition.This may be zero in API responses for instance partitions that are not yet in state `READY`.  
`instancePartition.processingUnits` |  `integer` The number of processing units allocated to this instance partition.Users can set the `processingUnits` field to specify the target number of processing units allocated to the instance partition.This might be zero in API responses for instance partitions that are not yet in the `READY` state.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-06 UTC."],[],[]] 
