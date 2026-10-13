---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/create/
title: Method: projects.instances.instancePartitions.create \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:13.467464+00:00
---

# Method: projects.instances.instancePartitions.create  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.instancePartitions.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates an instance partition and begins preparing it to be used. The returned long-running operation can be used to track the progress of preparing the new instance partition. The instance partition name is assigned by the caller. If the named instance partition already exists, `instancePartitions.create` returns `ALREADY_EXISTS`.

Immediately upon completion of this request:

  * The instance partition is readable via the API, with all requested attributes but no allocated resources. Its state is `CREATING`.



Until completion of the returned operation:

  * Cancelling the operation renders the instance partition immediately unreadable via the API.
  * The instance partition can be deleted.
  * All other attempts to modify the instance partition are rejected.



Upon completion of the returned operation:

  * Billing for all successfully-allocated resources begins (some types may have lower than the requested levels).
  * Databases can start using this instance partition.
  * The instance partition's allocated resource levels are readable via the API.
  * The instance partition's state becomes `READY`.



The returned long-running operation will have a name of the format `<instance_partition_name>/operations/<operationId>` and can be used to track creation of the instance partition. The metadata field type is `[CreateInstancePartitionMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateInstancePartitionMetadata)`. The response field type is `[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)`, if successful.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/instancePartitions`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the instance in which to create the instance partition. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.instancePartitions.create`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instancePartitionId": string,
      "instancePartition": {
        object ([InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition))
      }
    }  
  
Fields  
---  
`instancePartitionId` |  `string` Required. The ID of the instance partition to create. Valid identifiers are of the form `[a-z][-a-z0-9]*[a-z0-9]` and must be between 2 and 64 characters in length.  
`instancePartition` |  `object (`[InstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.instancePartitions#InstancePartition)`)` Required. The instance partition to create. The instancePartition.name may be omitted, but if specified must be `<parent>/instancePartitions/<instancePartitionId>`.  
  
### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
