---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/changequorum/
title: Method: projects.instances.databases.changequorum \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:04.889064+00:00
---

# Method: projects.instances.databases.changequorum  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/changequorum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.changequorum Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



`databases.changequorum` is strictly restricted to databases that use dual-region instance configurations.

Initiates a background operation to change the quorum of a database from dual-region mode to single-region mode or vice versa.

The returned long-running operation has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operationId>` and can be used to track execution of the `databases.changequorum`. The metadata field type is `[ChangeQuorumMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ChangeQuorumMetadata)`.

Authorization requires `spanner.databases.changequorum` permission on the resource database.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{name=projects/*/instances/*/databases/*}:changequorum`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the database in which to apply `databases.changequorum`. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.databases.changequorum`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "quorumType": {
        object ([QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#QuorumType))
      },
      "etag": string
    }  
  
Fields  
---  
`quorumType` |  `object (`[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#QuorumType)`)` Required. The type of this quorum.  
`etag` |  `string` Optional. The etag is the hash of the `QuorumInfo`. The `databases.changequorum` operation is only performed if the etag matches that of the `QuorumInfo` in the current database resource. Otherwise the API returns an `ABORTED` error.The etag is used for optimistic concurrency control as a way to help prevent simultaneous change quorum requests that could create a race condition.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
