---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/query/
title: Method: googleapis.bigquery.v2.jobs.query \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:39.153652+00:00
---

# Method: googleapis.bigquery.v2.jobs.query  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/jobs/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquery.v2.jobs.query Stay organized with collections  Save and categorize content based on your preferences. 

Runs a BigQuery SQL query synchronously and returns query results if the query completes within a specified timeout. # IAM Permissions Requires the `bigquery.jobs.create` permission on the project resource. Data-level permissions are highly dependent on the SQL statement being executed. While standard queries require data access (such as `bigquery.tables.getData`), complex operations like DDL or DCL may require permissions to manage reservations, IAM policies, or project settings.

For example, you can [create a workflow that runs multiple BigQuery query jobs in parallel](https://docs.cloud.google.com/workflows/docs/tutorials/bigquery-parallel-jobs).

## Arguments

Parameters  
---  
`projectId` |  `string` Required. Project ID of the query request.  
`body` |  `object ([QueryRequest](https://cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#QueryRequest))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`QueryResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#QueryResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/jobs/query).

### YAML
    
    
    - query:
        call: googleapis.bigquery.v2.jobs.query
        args:
            projectId: ...
            body:
                arrowSerializationOptions:
                    bufferCompression: ...
                    picosTimestampPrecision: ...
                connectionProperties: ...
                continuous: ...
                createSession: ...
                defaultDataset:
                    datasetId: ...
                    projectId: ...
                destinationEncryptionConfiguration:
                    kmsKeyName: ...
                dryRun: ...
                formatOptions:
                    timestampOutputFormat: ...
                    useInt64Timestamp: ...
                jobCreationMode: ...
                jobTimeoutMs: ...
                kind: ...
                labels: ...
                location: ...
                maxResults: ...
                maxSlots: ...
                maximumBytesBilled: ...
                parameterMode: ...
                preserveNulls: ...
                query: ...
                queryParameters: ...
                queryResultsFormat: ...
                requestId: ...
                reservation: ...
                secureContext:
                    secureParameterEntries: ...
                timeoutMs: ...
                useLegacySql: ...
                useQueryCache: ...
                writeIncrementalResults: ...
        result: queryResult

### JSON
    
    
    [
      {
        "query": {
          "call": "googleapis.bigquery.v2.jobs.query",
          "args": {
            "projectId": "...",
            "body": {
              "arrowSerializationOptions": {
                "bufferCompression": "...",
                "picosTimestampPrecision": "..."
              },
              "connectionProperties": "...",
              "continuous": "...",
              "createSession": "...",
              "defaultDataset": {
                "datasetId": "...",
                "projectId": "..."
              },
              "destinationEncryptionConfiguration": {
                "kmsKeyName": "..."
              },
              "dryRun": "...",
              "formatOptions": {
                "timestampOutputFormat": "...",
                "useInt64Timestamp": "..."
              },
              "jobCreationMode": "...",
              "jobTimeoutMs": "...",
              "kind": "...",
              "labels": "...",
              "location": "...",
              "maxResults": "...",
              "maxSlots": "...",
              "maximumBytesBilled": "...",
              "parameterMode": "...",
              "preserveNulls": "...",
              "query": "...",
              "queryParameters": "...",
              "queryResultsFormat": "...",
              "requestId": "...",
              "reservation": "...",
              "secureContext": {
                "secureParameterEntries": "..."
              },
              "timeoutMs": "...",
              "useLegacySql": "...",
              "useQueryCache": "...",
              "writeIncrementalResults": "..."
            }
          },
          "result": "queryResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
