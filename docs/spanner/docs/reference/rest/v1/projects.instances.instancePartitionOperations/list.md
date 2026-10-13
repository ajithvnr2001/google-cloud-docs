---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list/
title: Method: projects.instances.instancePartitionOperations.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:13.329579+00:00
---

# Method: projects.instances.instancePartitionOperations.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.instancePartitionOperations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists instance partition long-running operations in the given instance. An instance partition operation has a name of the form `projects/<project>/instances/<instance>/instancePartitions/<instancePartition>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.start_time` in descending order starting from the most recently started operation.

Authorization requires `spanner.instancePartitionOperations.list` permission on the resource `[parent](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.PATH_PARAMETERS.parent)`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/instancePartitionOperations`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent instance of the instance partition operations. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instancePartitionOperations.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. An expression that filters the list of returned operations.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the Operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.@type` \- the type of metadata. For example, the type string for `[CreateInstancePartitionMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstancePartitionMetadata)` is `type.googleapis.com/google.spanner.admin.instance.v1.CreateInstancePartitionMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first, if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `done:true` \- The operation is complete.
  * `(metadata.@type=` \ `type.googleapis.com/google.spanner.admin.instance.v1.CreateInstancePartitionMetadata) AND` \ `(metadata.instance_partition.name:custom-instance-partition) AND` \ `(metadata.start_time < \"2021-03-28T14:50:00Z\") AND` \ `(error:*)` \- Return operations where: 
    * The operation's metadata type is `[CreateInstancePartitionMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstancePartitionMetadata)`.
    * The instance partition name contains "custom-instance-partition".
    * The operation started before 2021-03-28T14:50:00Z.
    * The operation resulted in an error.

  
`pageSize` |  `integer` Optional. Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` Optional. If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.ListInstancePartitionOperationsResponse.FIELDS.next_page_token)` from a previous `[ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.ListInstancePartitionOperationsResponse)` to the same `parent` and with the same `filter`.  
`instancePartitionDeadline` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Deadline used while retrieving metadata for instance partition operations. Instance partitions whose operation metadata cannot be retrieved within this deadline will be added to `[unreachableInstancePartitions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.ListInstancePartitionOperationsResponse.FIELDS.unreachable_instance_partitions)` in `[ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.ListInstancePartitionOperationsResponse)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[instancePartitionOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation))
        }
      ],
      "nextPageToken": string,
      "unreachableInstancePartitions": [
        string
      ]
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`)` The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[instancePartitionOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations)` call to fetch more of the matching metadata.  
`unreachableInstancePartitions[]` |  `string` The list of unreachable instance partitions. It includes the names of instance partitions whose operation metadata could not be retrieved within `[instancePartitionDeadline](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitionOperations/list#body.QUERY_PARAMETERS.instance_partition_deadline)`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
