---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead/
title: Method: projects.instances.databases.sessions.partitionRead \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:12.432901+00:00
---

# Method: projects.instances.databases.sessions.partitionRead  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.partitionRead Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates a set of partition tokens that can be used to execute a read operation in parallel. Each of the returned partition tokens can be used by `[sessions.streamingRead](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/streamingRead#google.spanner.v1.Spanner.StreamingRead)` to specify a subset of the read result to read. The same session and read-only transaction must be used by the `PartitionReadRequest` used to create the partition tokens and the `ReadRequests` that use the partition tokens. There are no ordering guarantees on rows returned among the returned partition tokens, or even within each individual `sessions.streamingRead` call issued with a `partitionToken`.

Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it isn't possible to resume the read, and the whole operation must be restarted from the beginning.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionRead`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session used to create the partitions. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.partitionRead`

  
  
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
      "partitionOptions": {
        object ([PartitionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionOptions))
      }
    }  
  
Fields  
---  
`transaction` |  `object (`[TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector)`)` sessions.read only snapshot transactions are supported, read/write and single use transactions are not.  
`table` |  `string` Required. The name of the table in the database to be read.  
`index` |  `string` If non-empty, the name of an index on `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.table)`. This index is used instead of the table primary key when interpreting `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.key_set)` and sorting result rows. See `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.key_set)` for further information.  
`columns[]` |  `string` The columns of `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.table)` to be returned for each row matching this request.  
`keySet` |  `object (`[KeySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/KeySet)`)` Required. `keySet` identifies the rows to be yielded. `keySet` names the primary keys of the rows in `[table](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.table)` to be yielded, unless `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.index)` is present. If `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.index)` is present, then `[keySet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.key_set)` instead names index keys in `[index](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead#body.request_body.FIELDS.index)`.It isn't an error for the `keySet` to name rows that don't exist in the database. sessions.read yields nothing for nonexistent rows.  
`partitionOptions` |  `object (`[PartitionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionOptions)`)` Additional options that affect how many partitions are created.  
  
### Response body

If successful, the response body contains an instance of `[PartitionResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionResponse)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
