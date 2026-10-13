---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite/
title: Method: projects.instances.databases.sessions.batchWrite \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:10.099160+00:00
---

# Method: projects.instances.databases.sessions.batchWrite  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.batchWrite Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * MutationGroup
    * JSON representation
  * Try it!



Batches the supplied mutation groups in a collection of efficient transactions. All mutations in a group are committed atomically. However, mutations across groups can be committed non-atomically in an unspecified order and thus, they must be independent of each other. Partial failure is possible, that is, some groups might have been committed successfully, while some might have failed. The results of individual batches are streamed into the response as the batches are applied.

`sessions.batchWrite` requests are not replay protected, meaning that each mutation group can be applied more than once. Replays of non-idempotent mutations can have undesirable effects. For example, replays of an insert mutation can produce an already exists error or if you use generated or commit timestamp-based keys, it can result in additional rows being added to the mutation's table. We recommend structuring your mutation groups to be idempotent to avoid this issue.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:batchWrite`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session in which the batch request is to be run. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.write`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requestOptions": {
        object ([RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions))
      },
      "mutationGroups": [
        {
          object ([MutationGroup](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite#MutationGroup))
        }
      ],
      "excludeTxnFromChangeStreams": boolean
    }  
  
Fields  
---  
`requestOptions` |  `object (`[RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions)`)` Common options for this request.  
`mutationGroups[]` |  `object (`[MutationGroup](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite#MutationGroup)`)` Required. The groups of mutations to be applied.  
`excludeTxnFromChangeStreams` |  `boolean` Optional. If you don't set the `excludeTxnFromChangeStreams` option or if it's set to `false`, then any change streams monitoring columns modified by transactions will capture the updates made within that transaction.  
  
### Response body

The result of applying a batch of mutations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "indexes": [
        integer
      ],
      "status": {
        object ([Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status))
      },
      "commitTimestamp": string
    }  
  
Fields  
---  
`indexes[]` |  `integer` The mutation groups applied in this batch. The values index into the `mutationGroups` field in the corresponding `BatchWriteRequest`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status)`)` An `OK` status indicates success. Any other status indicates a failure.  
`commitTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The commit timestamp of the transaction that applied this batch. Present if status is OK and the mutation groups were applied, absent otherwise.For mutation groups with conditions, a status=OK and missing commitTimestamp means that the mutation groups were not applied due to the condition not being satisfied after evaluation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## MutationGroup

A group of mutations to be committed together. Related mutations should be placed in a group. For example, two mutations inserting rows with the same primary key prefix in both parent and child tables are related.

JSON representation  
---  
      
    
    {
      "mutations": [
        {
          object ([Mutation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation))
        }
      ]
    }  
  
Fields  
---  
`mutations[]` |  `object (`[Mutation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation)`)` Required. The mutations in this group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
