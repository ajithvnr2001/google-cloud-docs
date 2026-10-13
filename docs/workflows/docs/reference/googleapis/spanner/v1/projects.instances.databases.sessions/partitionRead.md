---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.databases.sessions/partitionRead/
title: Method: googleapis.spanner.v1.projects.instances.databases.sessions.partitionRead \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:13.381498+00:00
---

# Method: googleapis.spanner.v1.projects.instances.databases.sessions.partitionRead  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.databases.sessions/partitionRead/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.spanner.v1.projects.instances.databases.sessions.partitionRead Stay organized with collections  Save and categorize content based on your preferences. 

Creates a set of partition tokens that can be used to execute a read operation in parallel. Each of the returned partition tokens can be used by StreamingRead to specify a subset of the read result to read. The same session and read-only transaction must be used by the `PartitionReadRequest` used to create the partition tokens and the `ReadRequests` that use the partition tokens. There are no ordering guarantees on rows returned among the returned partition tokens, or even within each individual `StreamingRead` call issued with a `partition_token`. Partition tokens become invalid when the session used to create them is deleted, is idle for too long, begins a new transaction, or becomes too old. When any of these happen, it isn't possible to resume the read, and the whole operation must be restarted from the beginning.

For more information about retries and long-running operations, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/projects.instances.databases.sessions/partitionRead/).

## Arguments

Parameters  
---  
`session` |  `string` Required. The session used to create the partitions.  
`body` |  `object ([PartitionReadRequest](https://cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/Overview#PartitionReadRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`PartitionResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/spanner/v1/Overview#PartitionResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead).

### YAML
    
    
    - partitionRead:
        call: googleapis.spanner.v1.projects.instances.databases.sessions.partitionRead
        args:
            session: ...
            body:
                columns: ...
                index: ...
                keySet:
                    all: ...
                    keys: ...
                    ranges: ...
                partitionOptions:
                    maxPartitions: ...
                    partitionSizeBytes: ...
                table: ...
                transaction:
                    begin:
                        excludeTxnFromChangeStreams: ...
                        isolationLevel: ...
                        partitionedDml: ...
                        readOnly:
                            exactStaleness: ...
                            maxStaleness: ...
                            minReadTimestamp: ...
                            readTimestamp: ...
                            returnReadTimestamp: ...
                            strong: ...
                        readWrite:
                            multiplexedSessionPreviousTransactionId: ...
                            readLockMode: ...
                    id: ...
                    singleUse: ...
        result: partitionReadResult

### JSON
    
    
    [
      {
        "partitionRead": {
          "call": "googleapis.spanner.v1.projects.instances.databases.sessions.partitionRead",
          "args": {
            "session": "...",
            "body": {
              "columns": "...",
              "index": "...",
              "keySet": {
                "all": "...",
                "keys": "...",
                "ranges": "..."
              },
              "partitionOptions": {
                "maxPartitions": "...",
                "partitionSizeBytes": "..."
              },
              "table": "...",
              "transaction": {
                "begin": {
                  "excludeTxnFromChangeStreams": "...",
                  "isolationLevel": "...",
                  "partitionedDml": "...",
                  "readOnly": {
                    "exactStaleness": "...",
                    "maxStaleness": "...",
                    "minReadTimestamp": "...",
                    "readTimestamp": "...",
                    "returnReadTimestamp": "...",
                    "strong": "..."
                  },
                  "readWrite": {
                    "multiplexedSessionPreviousTransactionId": "...",
                    "readLockMode": "..."
                  }
                },
                "id": "...",
                "singleUse": "..."
              }
            }
          },
          "result": "partitionReadResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
