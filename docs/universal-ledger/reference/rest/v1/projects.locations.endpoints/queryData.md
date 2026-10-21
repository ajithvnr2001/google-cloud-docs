---
url: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData/
title: Method: projects.locations.endpoints.queryData \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:53:05.050091+00:00
---

# Method: projects.locations.endpoints.queryData  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Reference ](https://docs.cloud.google.com/universal-ledger/reference/rpc)



Send feedback 

#  Method: projects.locations.endpoints.queryData Stay organized with collections  Save and categorize content based on your preferences. 

Queries the network for information stored on the ledger, such as accounts and transactions.

Access to certain sensitive fields, such as account balances, may be restricted based on the identity of the sender derived from the signature in the request. If the sender lacks permission, sensitive fields will be redacted from the response and reported in the `redactedFields` field.

### HTTP request

Choose an endpoint:

globalus-central1us-east1us-east4us-east5us-west1europe-west2europe-west3

  
`POST https://universalledger.googleapis.com/v1/{endpoint=projects/*/locations/*/endpoints/*}:queryData`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`endpoint` |  `string` Required. The endpoint to serve the request. Format: `projects/{project}/locations/{location}/endpoints/{endpoint}` The location is a region.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "serializedSignedQueryRequest": string
    }  
  
Fields  
---  
`serializedSignedQueryRequest` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. A protobuf serialized `SignedQueryRequest` to query the Universal Ledger network.A base64-encoded string.  
  
### Response body

Response message for endpoints.queryData.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "redactedFields": [
        {
          object ([RedactedField](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#RedactedField))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "account": {
        object ([Account](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account))
      },
      "transactionState": {
        object ([TransactionState](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#TransactionState))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`redactedFields[]` |  `object (`[RedactedField](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#RedactedField)`)` Indicates which fields have been redacted from the response due to permission restrictions.  
The query-specific result. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`account` |  `object (`[Account](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/Account)`)` The account information, if the query was for an account.  
`transactionState` |  `object (`[TransactionState](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#TransactionState)`)` The state of a transaction, if the query was for a transaction.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## TransactionState

The state of a transaction.

JSON representation  
---  
      
    
    {
      "transactionAttempts": [
        {
          object ([TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt))
        }
      ]
    }  
  
Fields  
---  
`transactionAttempts[]` |  `object (`[TransactionAttempt](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/TransactionAttempt)`)` One entry per each known submission of the transaction to the validator handling the request.  
  
## RedactedField

Information about a redacted field in the response.

JSON representation  
---  
      
    
    {
      "redactedPath": string,
      "reason": string,
      "reasonCode": enum ([Code](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#Code))
    }  
  
Fields  
---  
`redactedPath` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Output only. The fully qualified field paths that were redacted from the payload.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`reason` |  `string` Output only. A human-readable explanation of why the fields were redacted.  
`reasonCode` |  `enum (`[Code](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/queryData#Code)`)` Output only. A machine readable code for why the fields were redacted.  
  
## Code

The canonical error codes for gRPC APIs.

Sometimes multiple error codes may apply. Services should return the most specific error code that applies. For example, prefer `OUT_OF_RANGE` over `FAILED_PRECONDITION` if both codes apply. Similarly prefer `NOT_FOUND` or `ALREADY_EXISTS` over `FAILED_PRECONDITION`.

Enums  
---  
`OK` | Not an error; returned on success.HTTP Mapping: 200 OK  
`CANCELLED` | The operation was cancelled, typically by the caller.HTTP Mapping: 499 Client Closed Request  
`UNKNOWN` | Unknown error. For example, this error may be returned when a `Status` value received from another address space belongs to an error space that is not known in this address space. Also errors raised by APIs that do not return enough error information may be converted to this error.HTTP Mapping: 500 Internal Server Error  
`INVALID_ARGUMENT` | The client specified an invalid argument. Note that this differs from `FAILED_PRECONDITION`. `INVALID_ARGUMENT` indicates arguments that are problematic regardless of the state of the system (e.g., a malformed file name).HTTP Mapping: 400 Bad Request  
`DEADLINE_EXCEEDED` | The deadline expired before the operation could complete. For operations that change the state of the system, this error may be returned even if the operation has completed successfully. For example, a successful response from a server could have been delayed long enough for the deadline to expire.HTTP Mapping: 504 Gateway Timeout  
`NOT_FOUND` | Some requested entity (e.g., file or directory) was not found.Note to server developers: if a request is denied for an entire class of users, such as gradual feature rollout or undocumented allowlist, `NOT_FOUND` may be used. If a request is denied for some users within a class of users, such as user-based access control, `PERMISSION_DENIED` must be used.HTTP Mapping: 404 Not Found  
`ALREADY_EXISTS` | The entity that a client attempted to create (e.g., file or directory) already exists.HTTP Mapping: 409 Conflict  
`PERMISSION_DENIED` | The caller does not have permission to execute the specified operation. `PERMISSION_DENIED` must not be used for rejections caused by exhausting some resource (use `RESOURCE_EXHAUSTED` instead for those errors). `PERMISSION_DENIED` must not be used if the caller can not be identified (use `UNAUTHENTICATED` instead for those errors). This error code does not imply the request is valid or the requested entity exists or satisfies other pre-conditions.HTTP Mapping: 403 Forbidden  
`UNAUTHENTICATED` | The request does not have valid authentication credentials for the operation.HTTP Mapping: 401 Unauthorized  
`RESOURCE_EXHAUSTED` | Some resource has been exhausted, perhaps a per-user quota, or perhaps the entire file system is out of space.HTTP Mapping: 429 Too Many Requests  
`FAILED_PRECONDITION` | The operation was rejected because the system is not in a state required for the operation's execution. For example, the directory to be deleted is non-empty, an rmdir operation is applied to a non-directory, etc.Service implementors can use the following guidelines to decide between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`: (a) Use `UNAVAILABLE` if the client can retry just the failing call. (b) Use `ABORTED` if the client should retry at a higher level. For example, when a client-specified test-and-set fails, indicating the client should restart a read-modify-write sequence. (c) Use `FAILED_PRECONDITION` if the client should not retry until the system state has been explicitly fixed. For example, if an "rmdir" fails because the directory is non-empty, `FAILED_PRECONDITION` should be returned since the client should not retry unless the files are deleted from the directory.HTTP Mapping: 400 Bad Request  
`ABORTED` | The operation was aborted, typically due to a concurrency issue such as a sequencer check failure or transaction abort.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 409 Conflict  
`OUT_OF_RANGE` | The operation was attempted past the valid range. E.g., seeking or reading past end-of-file.Unlike `INVALID_ARGUMENT`, this error indicates a problem that may be fixed if the system state changes. For example, a 32-bit file system will generate `INVALID_ARGUMENT` if asked to read at an offset that is not in the range [0,2^32-1], but it will generate `OUT_OF_RANGE` if asked to read from an offset past the current file size.There is a fair bit of overlap between `FAILED_PRECONDITION` and `OUT_OF_RANGE`. We recommend using `OUT_OF_RANGE` (the more specific error) when it applies so that callers who are iterating through a space can easily look for an `OUT_OF_RANGE` error to detect when they are done.HTTP Mapping: 400 Bad Request  
`UNIMPLEMENTED` | The operation is not implemented or is not supported/enabled in this service.HTTP Mapping: 501 Not Implemented  
`INTERNAL` | Internal errors. This means that some invariants expected by the underlying system have been broken. This error code is reserved for serious errors.HTTP Mapping: 500 Internal Server Error  
`UNAVAILABLE` | The service is currently unavailable. This is most likely a transient condition, which can be corrected by retrying with a backoff. Note that it is not always safe to retry non-idempotent operations.See the guidelines above for deciding between `FAILED_PRECONDITION`, `ABORTED`, and `UNAVAILABLE`.HTTP Mapping: 503 Service Unavailable  
`DATA_LOSS` | Unrecoverable data loss or corruption.HTTP Mapping: 500 Internal Server Error  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-27 UTC."],[],[]] 
