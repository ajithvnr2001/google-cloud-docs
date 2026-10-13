---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit/
title: Method: projects.instances.databases.sessions.commit \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:11.881394+00:00
---

# Method: projects.instances.databases.sessions.commit  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.commit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * CommitStats
    * JSON representation
  * Try it!



Commits a transaction. The request includes the mutations to be applied to rows in the database.

`sessions.commit` might return an `ABORTED` error. This can occur at any time; commonly, the cause is conflicts with concurrent transactions. However, it can also happen for a variety of other reasons. If `sessions.commit` returns `ABORTED`, the caller should retry the transaction from the beginning, reusing the same session.

On very rare occasions, `sessions.commit` might return `UNKNOWN`. This can happen, for example, if the client job experiences a 1+ hour networking failure. At that point, Cloud Spanner has lost track of the transaction outcome and we recommend that you perform another read from the database to see the state of things as they are now.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:commit`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session in which the transaction to be committed is running. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.write`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mutations": [
        {
          object ([Mutation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation))
        }
      ],
      "returnCommitStats": boolean,
      "maxCommitDelay": string,
      "requestOptions": {
        object ([RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions))
      },
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken))
      },
    
      // Union field transaction can be only one of the following:
      "transactionId": string,
      "singleUseTransaction": {
        object ([TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions))
      }
      // End of list of possible types for union field transaction.
    }  
  
Fields  
---  
`mutations[]` |  `object (`[Mutation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/Mutation)`)` The mutations to be executed when this transaction commits. All mutations are applied atomically, in the order they appear in this list.  
`returnCommitStats` |  `boolean` If `true`, then statistics related to the transaction is included in the `[CommitResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#body.CommitResponse.FIELDS.commit_stats)`. Default value is `false`.  
`maxCommitDelay` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The amount of latency this request is configured to incur in order to improve throughput. If this field isn't set, Spanner assumes requests are relatively latency sensitive and automatically determines an appropriate delay time. You can specify a commit delay value between 0 and 500 ms.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`requestOptions` |  `object (`[RequestOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/RequestOptions)`)` Common options for this request.  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken)`)` Optional. If the read-write transaction was executed on a multiplexed session, then you must include the precommit token with the highest sequence number received in this transaction attempt. Failing to do so results in a `FailedPrecondition` error.  
Union field `transaction`. Required. The transaction in which to commit. `transaction` can be only one of the following:  
`transactionId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` sessions.commit a previously-started transaction.A base64-encoded string.  
`singleUseTransaction` |  `object (`[TransactionOptions](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/TransactionOptions)`)` Execute mutations in a temporary transaction. Note that unlike commit of a previously-started transaction, commit with a temporary transaction is non-idempotent. That is, if the `CommitRequest` is sent to Cloud Spanner more than once (for instance, due to retries in the application, or in the transport library), it's possible that the mutations are executed more than once. If this is undesirable, use `[sessions.beginTransaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/beginTransaction#google.spanner.v1.Spanner.BeginTransaction)` and `[sessions.commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)` instead.  
  
### Response body

The response for `[sessions.commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#google.spanner.v1.Spanner.Commit)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commitTimestamp": string,
      "commitStats": {
        object ([CommitStats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#CommitStats))
      },
    
      // Union field MultiplexedSessionRetry can be only one of the following:
      "precommitToken": {
        object ([MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken))
      }
      // End of list of possible types for union field MultiplexedSessionRetry.
    }  
  
Fields  
---  
`commitTimestamp` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The Cloud Spanner timestamp at which the transaction committed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitStats` |  `object (`[CommitStats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#CommitStats)`)` The statistics about this `sessions.commit`. Not returned by default. For more information, see `[CommitRequest.return_commit_stats](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit#body.request_body.FIELDS.return_commit_stats)`.  
Union field `MultiplexedSessionRetry`. You must examine and retry the commit if the following is populated. `MultiplexedSessionRetry` can be only one of the following:  
`precommitToken` |  `object (`[MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/MultiplexedSessionPrecommitToken)`)` If specified, transaction has not committed yet. You must retry the commit with the new precommit token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CommitStats

Additional statistics about a commit.

JSON representation  
---  
      
    
    {
      "mutationCount": string
    }  
  
Fields  
---  
`mutationCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The total number of mutations for the transaction. Knowing the `mutationCount` value can help you maximize the number of mutations in a transaction and minimize the number of API round trips. You can also monitor this value to prevent transactions from exceeding the system [limit](https://cloud.google.com/spanner/quotas#limits_for_creating_reading_updating_and_deleting_data). If the number of mutations exceeds the limit, the server returns [INVALID_ARGUMENT](https://cloud.google.com/spanner/docs/reference/rest/v1/Code#ENUM_VALUES.INVALID_ARGUMENT).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
