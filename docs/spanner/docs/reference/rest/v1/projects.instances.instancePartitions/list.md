---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list/
title: Method: projects.instances.instancePartitions.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:13.800006+00:00
---

# Method: projects.instances.instancePartitions.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.instancePartitions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all instance partitions for the given instance.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/instancePartitions`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance whose instance partitions should be listed. Values are of the form `projects/<project>/instances/<instance>`. Use `{instance} = '-'` to list instance partitions for all Instances in a project, e.g., `projects/myproject/instances/-`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instancePartitions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Number of instance partitions to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#body.ListInstancePartitionsResponse.FIELDS.next_page_token)` from a previous `[ListInstancePartitionsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#body.ListInstancePartitionsResponse)`.  
`instancePartitionDeadline` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Deadline used while retrieving metadata for instance partitions. Instance partitions whose metadata cannot be retrieved within this deadline will be added to `[unreachable](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#body.ListInstancePartitionsResponse.FIELDS.unreachable)` in `[ListInstancePartitionsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#body.ListInstancePartitionsResponse)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[instancePartitions.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instancePartitions": [
        {
          object ([InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instancePartitions[]` |  `object (`[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)`)` The list of requested instancePartitions.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[instancePartitions.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions)` call to fetch more of the matching instance partitions.  
`unreachable[]` |  `string` The list of unreachable instances or instance partitions. It includes the names of instances or instance partitions whose metadata could not be retrieved within `[instancePartitionDeadline](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/list#body.QUERY_PARAMETERS.instance_partition_deadline)`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
