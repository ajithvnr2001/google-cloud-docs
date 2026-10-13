---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionQuery/
title: Method: projects.instances.databases.sessions.partitionQuery \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:11.992270+00:00
---

# Method: projects.instances.databases.sessions.partitionQuery  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionQuery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.partitionQuery Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Creates a set of partition tokens that can be used to execute a query operation in parallel. Each of the returned partition tokens can be used by `[sessions.executeStreamingSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeStreamingSql#google.spanner.v1.Spanner.ExecuteStreamingSql)` to specify a subset of the query result to read. The same session and read-only transaction must be used by the `PartitionQueryRequest` used to create the partition tokens and the `ExecuteSqlRequests` that use the partition tokens.

Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it isn't possible to resume the query, and the whole operation must be restarted from the beginning.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:partitionQuery`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session used to create the partitions. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.partitionQuery`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transaction": {
        object ([TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector))
      },
      "sql": string,
      "params": {
        object
      },
      "paramTypes": {
        string: {
          object ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type))
        },
        ...
      },
      "partitionOptions": {
        object ([PartitionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/PartitionOptions))
      }
    }  
  
Fields  
---  
`transaction` |  `object (`[TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector)`)` sessions.read-only snapshot transactions are supported, read and write and single-use transactions are not.  
`sql` |  `string` Required. The query request to generate partitions for. The request fails if the query isn't root partitionable. For a query to be root partitionable, it needs to satisfy a few conditions. For example, if the query execution plan contains a distributed union operator, then it must be the first operator in the plan. For more information about other conditions, see [sessions.read data in parallel](https://cloud.google.com/spanner/docs/reads#read_data_in_parallel).The query request must not contain DML commands, such as `INSERT`, `UPDATE`, or `DELETE`. Use `[`sessions.executeStreamingSql`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeStreamingSql#google.spanner.v1.Spanner.ExecuteStreamingSql)` with a `PartitionedDml` transaction for large, partition-friendly DML operations.  
`params` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Parameter names and values that bind to placeholders in the SQL string.A parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`). Parameter names can contain letters, numbers, and underscores.Parameters can appear anywhere that a literal value is expected. The same parameter name can be used more than once, for example:`"WHERE id > @msg_id AND id < @msg_id + 100"`It's an error to execute a SQL statement with unbound parameters.  
`paramTypes` |  `map (key: string, value: object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)`))` Optional. It isn't always possible for Cloud Spanner to infer the right SQL type from a JSON value. For example, values of type `BYTES` and values of type `STRING` both appear in `[params](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionQuery#body.request_body.FIELDS.params)` as JSON strings.In these cases, `paramTypes` can be used to specify the exact SQL type for some or all of the SQL query parameters. See the definition of `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` for more information about SQL types.  
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

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
