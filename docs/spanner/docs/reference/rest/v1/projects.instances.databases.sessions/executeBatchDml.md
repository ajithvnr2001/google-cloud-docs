---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml/
title: Method: projects.instances.databases.sessions.executeBatchDml \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:10.857297+00:00
---

# Method: projects.instances.databases.sessions.executeBatchDml  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.executeBatchDml Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * Statement
    * JSON representation
  * Try it!



Executes a batch of SQL DML statements. This method allows many statements to be run with lower latency than submitting them sequentially with `[sessions.executeSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)`.

Statements are executed in sequential order. A request can succeed even if a statement fails. The `[ExecuteBatchDmlResponse.status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml#body.ExecuteBatchDmlResponse.FIELDS.status)` field in the response provides information about the statement that failed. Clients must inspect this field to determine whether an error occurred.

Execution stops after the first failed statement; the remaining statements are not executed.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:executeBatchDml`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session in which the DML statements should be performed. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.write`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transaction": {
        object ([TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector))
      },
      "statements": [
        {
          object ([Statement](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml#Statement))
        }
      ],
      "seqno": string,
      "requestOptions": {
        object ([RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions))
      },
      "lastStatements": boolean
    }  
  
Fields  
---  
`transaction` |  `object (`[TransactionSelector](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionSelector)`)` Required. The transaction to use. Must be a read-write transaction.To protect against replays, single-use transactions are not supported. The caller must either supply an existing transaction ID or begin a new transaction.  
`statements[]` |  `object (`[Statement](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml#Statement)`)` Required. The list of statements to execute in this batch. Statements are executed serially, such that the effects of statement `i` are visible to statement `i+1`. Each statement must be a DML statement. Execution stops at the first failed statement; the remaining statements are not executed.Callers must provide at least one statement.  
`seqno` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. A per-transaction sequence number used to identify this request. This field makes each request idempotent such that if the request is received multiple times, at most one succeeds.The sequence number must be monotonically increasing within the transaction. If a request arrives for the first time with an out-of-order sequence number, the transaction might be aborted. Replays of previously handled requests yield the same response as the first execution.  
`requestOptions` |  `object (`[RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions)`)` Common options for this request.  
`lastStatements` |  `boolean` Optional. If set to `true`, this request marks the end of the transaction. After these statements execute, you must commit or abort the transaction. Attempts to execute any other requests against this transaction (including reads and queries) are rejected.Setting this option might cause some error reporting to be deferred until commit time (for example, validation of unique constraints). Given this, successful execution of statements shouldn't be assumed until a subsequent `sessions.commit` call completes successfully.  
  
### Response body

The response for `[sessions.executeBatchDml](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml#google.spanner.v1.Spanner.ExecuteBatchDml)`. Contains a list of `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` messages, one for each DML statement that has successfully executed, in the same order as the statements in the request. If a statement fails, the status in the response body identifies the cause of the failure.

To check for DML statements that failed, use the following approach:

  1. Check the status in the response message. The `[google.rpc.Code](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Code)` enum value `OK` indicates that all statements were executed successfully.
  2. If the status was not `OK`, check the number of result sets in the response. If the response contains `N` `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` messages, then statement `N+1` in the request failed.



Example 1:

  * Request: 5 DML statements, all executed successfully.
  * Response: 5 `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` messages, with the status `OK`.



Example 2:

  * Request: 5 DML statements. The third statement has a syntax error.
  * Response: 2 `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` messages, and a syntax error (`INVALID_ARGUMENT`) status. The number of `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` messages indicates that the third statement failed, and the fourth and fifth statements were not executed.



If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resultSets": [
        {
          object ([ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet))
        }
      ],
      "status": {
        object ([Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status))
      },
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken))
      }
    }  
  
Fields  
---  
`resultSets[]` |  `object (`[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)`)` One `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` for each statement in the request that ran successfully, in the same order as the statements in the request. Each `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` does not contain any rows. The `[ResultSetStats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetStats)` in each `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` contain the number of rows modified by the statement.Only the first `[ResultSet](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSet)` in the response contains valid `[ResultSetMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/ResultSetMetadata)`.  
`status` |  `object (`[Status](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Status)`)` If all DML statements are executed successfully, the status is `OK`. Otherwise, the error status of the first failed statement.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken)`)` Optional. A precommit token is included if the read-write transaction is on a multiplexed session. Pass the precommit token with the highest sequence number from this transaction attempt should be passed to the `[sessions.commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)` request for this transaction.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Statement

A single DML statement.

JSON representation  
---  
      
    
    {
      "sql": string,
      "params": {
        object
      },
      "paramTypes": {
        string: {
          object ([Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type))
        },
        ...
      }
    }  
  
Fields  
---  
`sql` |  `string` Required. The DML string.  
`params` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Parameter names and values that bind to placeholders in the DML string.A parameter placeholder consists of the `@` character followed by the parameter name (for example, `@firstName`). Parameter names can contain letters, numbers, and underscores.Parameters can appear anywhere that a literal value is expected. The same parameter name can be used more than once, for example:`"WHERE id > @msg_id AND id < @msg_id + 100"`It's an error to execute a SQL statement with unbound parameters.  
`paramTypes` |  `map (key: string, value: object (`[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)`))` It isn't always possible for Cloud Spanner to infer the right SQL type from a JSON value. For example, values of type `BYTES` and values of type `STRING` both appear in `[params](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml#Statement.FIELDS.params)` as JSON strings.In these cases, `paramTypes` can be used to specify the exact SQL type for some or all of the SQL statement parameters. See the definition of `[Type](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Type)` for more information about SQL types.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
