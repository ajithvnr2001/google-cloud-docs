---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions
title: REST Resource: projects.instances.databases.sessions \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:09.681589+00:00
---

# REST Resource: projects.instances.databases.sessions  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  REST Resource: projects.instances.databases.sessions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Session
    * JSON representation
  * Methods



## Resource: Session

A session in the Cloud Spanner API.

JSON representation  
---  
      
    
    {
      "name": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "approximateLastUseTime": string,
      "creatorRole": string,
      "multiplexed": boolean
    }  
  
Fields  
---  
`name` |  `string` Output only. The name of the session. This is always system-assigned.  
`labels` |  `map (key: string, value: string)` The labels for the session.

  * Label keys must be between 1 and 63 characters long and must conform to the following regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`.
  * Label values must be between 0 and 63 characters long and must conform to the regular expression `([a-z]([-a-z0-9]*[a-z0-9])?)?`.
  * No more than 64 labels can be associated with a given session.

See <https://goo.gl/xmQnxf> for more information on and examples of labels.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the session is created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`approximateLastUseTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The approximate timestamp when the session is last used. It's typically earlier than the actual last use time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`creatorRole` |  `string` The database role which created this session.  
`multiplexed` |  `boolean` Optional. If `true`, specifies a multiplexed session. Use a multiplexed session for multiple, concurrent operations including any combination of read-only and read-write transactions. Use `[`sessions.create`](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/create#google.spanner.v1.Spanner.CreateSession)` to create multiplexed sessions. Don't use `[sessions.batchCreate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate#google.spanner.v1.Spanner.BatchCreateSessions)` to create a multiplexed session. You can't delete or list multiplexed sessions.  
  
## Methods  
  
---  
  
### `[adaptMessage](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/adaptMessage)`

|  Handles a single message from the client and returns the result as a stream.  
  
### `[adapter](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/adapter)`

|  Creates a new session to be used for requests made by the adapter.  
  
### `[batchCreate](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchCreate)`

|  Creates multiple new sessions.  
  
### `[batchWrite](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/batchWrite)`

|  Batches the supplied mutation groups in a collection of efficient transactions.  
  
### `[beginTransaction](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/beginTransaction)`

|  Begins a new transaction.  
  
### `[commit](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/commit)`

|  Commits a transaction.  
  
### `[create](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/create)`

|  Creates a new session.  
  
### `[delete](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/delete)`

|  Ends a session, releasing server resources associated with it.  
  
### `[executeBatchDml](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeBatchDml)`

|  Executes a batch of SQL DML statements.  
  
### `[executeSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql)`

|  Executes an SQL statement, returning all results in a single reply.  
  
### `[executeStreamingSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeStreamingSql)`

|  Like `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)`, except returns the result set as a stream.  
  
### `[get](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/get)`

|  Gets a session.  
  
### `[list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/list)`

|  Lists all sessions in a given database.  
  
### `[partitionQuery](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionQuery)`

|  Creates a set of partition tokens that can be used to execute a query operation in parallel.  
  
### `[partitionRead](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/partitionRead)`

|  Creates a set of partition tokens that can be used to execute a read operation in parallel.  
  
### `[read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read)`

|  Reads rows from the database using key lookups and scans, as a simple key/value style alternative to `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/executeSql#google.spanner.v1.Spanner.ExecuteSql)`.  
  
### `[rollback](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/rollback)`

|  Rolls back a transaction, releasing any locks it holds.  
  
### `[streamingRead](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/streamingRead)`

|  Like `[Read](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases.sessions/read#google.spanner.v1.Spanner.Read)`, except returns the result set as a stream.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
