---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/rollback/
title: Method: projects.instances.databases.sessions.rollback \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:12.797524+00:00
---

# Method: projects.instances.databases.sessions.rollback  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/rollback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.sessions.rollback Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Rolls back a transaction, releasing any locks it holds. It's a good idea to call this for any transaction that includes one or more `[sessions.read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)` or `[sessions.executeSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)` requests and ultimately decides not to commit.

`sessions.rollback` returns `OK` if it successfully aborts the transaction, the transaction was already aborted, or the transaction isn't found. `sessions.rollback` never returns `ABORTED`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`POST https://spanner.googleapis.com/v1/{session=projects/*/instances/*/databases/*/sessions/*}:rollback`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`session` |  `string` Required. The session in which the transaction to roll back is running. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `session`:

  * `spanner.databases.beginOrRollbackReadWriteTransaction`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionId": string
    }  
  
Fields  
---  
`transactionId` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The transaction to roll back.A base64-encoded string.  
  
### Response body

If successful, the response body is an empty JSON object.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.data`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
