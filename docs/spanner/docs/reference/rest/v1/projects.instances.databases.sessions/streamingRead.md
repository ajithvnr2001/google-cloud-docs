---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/streamingRead/
title: Method: projects.instances.databases.sessions.streamingRead \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:13.008272+00:00
---

# Method: projects.instances.databases.sessions.streamingRead  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/streamingRead/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.streamingRead Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Like `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)`, except returns the result set as a stream. Unlike `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)`, there is no limit on the size of the returned result set. However, no individual row in the result set can exceed 100 MiB, and no column value can exceed 10 MiB.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:streamingRead`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session in which the read should be performed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.read`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transaction": {
        object ([TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector))
      },
      "table": string,
      "index": string,
      "columns": [
        string
      ],
      "keySet": {
        object ([KeySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/KeySet))
      },
      "limit": string,
      "resumeToken": string,
      "partitionToken": string,
      "requestOptions": {
        object ([RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions))
      },
      "directedReadOptions": {
        object ([DirectedReadOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions))
      },
      "dataBoostEnabled": boolean
    }  
  
Fields  
---  
`transaction` |  `object (`[TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector)`)` The transaction to use. If none is provided, the default is a temporary read-only transaction with strong concurrency.  
`table` |  `string` Required. The name of the table in the database to be read.  
`index` |  `string` If non-empty, the name of an index on `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.table)`. This index is used instead of the table primary key when interpreting `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.key_set)` and sorting result rows. See `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.key_set)` for further information.  
`columns[]` |  `string` Required. The columns of `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.table)` to be returned for each row matching this request.  
`keySet` |  `object (`[KeySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/KeySet)`)` Required. `keySet` identifies the rows to be yielded. `keySet` names the primary keys of the rows in `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.table)` to be yielded, unless `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.index)` is present. If `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.index)` is present, then `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.key_set)` instead names index keys in `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.index)`.If the `[partitionToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.partition_token)` field is empty, rows are yielded in table primary key order (if `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.index)` is empty) or index key order (if `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.index)` is non-empty). If the `[partitionToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#body.request_body.FIELDS.partition_token)` field isn't empty, rows are yielded in an unspecified order.It isn't an error for the `keySet` to name rows that don't exist in the database. sessions.read yields nothing for nonexistent rows.  
`limit` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` If greater than zero, only the first `limit` rows are yielded. If `limit` is zero, the default is no limit. A limit can't be specified if `partitionToken` is set.  
`resumeToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` If this request is resuming a previously interrupted read, `resumeToken` should be copied from the last `[PartialResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartialResultSet)` yielded before the interruption. Doing this enables the new read to resume where the last read left off. The rest of the request parameters must exactly match the request that yielded this token.A base64-encoded string.  
`partitionToken` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` If present, results are restricted to the specified partition previously created using `sessions.partitionRead`. There must be an exact match for the values of fields common to this message and the PartitionReadRequest message used to create this partitionToken.A base64-encoded string.  
`requestOptions` |  `object (`[RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions)`)` Common options for this request.  
`directedReadOptions` |  `object (`[DirectedReadOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/DirectedReadOptions)`)` Directed read options for this request.  
`dataBoostEnabled` |  `boolean` If this is for a partitioned read and this field is set to `true`, the request is executed with Spanner Data Boost independent compute resources.If the field is set to `true` but the request doesn't set `partitionToken`, the API returns an `INVALID_ARGUMENT` error.  
  
### Response body

If successful, the response body contains a stream of `[PartialResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartialResultSet)` instances.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
