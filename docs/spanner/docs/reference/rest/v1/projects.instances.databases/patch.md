---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/patch/
title: Method: projects.instances.databases.patch \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:06.882984+00:00
---

# Method: projects.instances.databases.patch  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.databases.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Updates a Cloud Spanner database. The returned long-running operation can be used to track the progress of updating the database. If the named database does not exist, returns `NOT_FOUND`.

While the operation is pending:

  * The database's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database.FIELDS.reconciling)` field is set to true.
  * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata's `[cancelTime](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateDatabaseMetadata#FIELDS.cancel_time)` is set, the updates are reverted, and the operation terminates with a `CANCELLED` status.
  * New databases.patch requests will return a `FAILED_PRECONDITION` error until the pending operation is done (returns successfully or with error).
  * Reading the database via the API continues to give the pre-request values.



Upon completion of the returned operation:

  * The new values are in effect and readable via the API.
  * The database's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database.FIELDS.reconciling)` field becomes false.



The returned long-running operation will have a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operationId>` and can be used to track the database modification. The metadata field type is `[UpdateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/UpdateDatabaseMetadata)`. The response field type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database)`, if successful.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`PATCH https://spanner.googleapis.com/v1/{database.name=projects/*/instances/*/databases/*}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`database.name` |  `string` Required. The name of the database. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`, where `<database>` is as specified in the `CREATE DATABASE` statement. This name can be passed to other API methods to identify the database.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Required. The list of fields to update. Currently, only `enableDropProtection` field can be updated.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[Database](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases#Database)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
