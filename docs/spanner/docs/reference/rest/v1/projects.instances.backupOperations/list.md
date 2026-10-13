---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list/
title: Method: projects.instances.backupOperations.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:02.682881+00:00
---

# Method: projects.instances.backupOperations.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.backupOperations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the backup long-running operations in the given instance. A backup operation has a name of the form `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/backupOperations`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backupOperations.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` An expression that filters the list of returned backup operations.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.@type` \- the type of metadata. For example, the type string for `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata)` is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `done:true` \- The operation is complete.
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where: 
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata)`.
    * The source database name of backup contains the string "prod".
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata)`.
    * The backup name contains the string "howl".
    * The operation started before 2018-03-28T14:50:00Z.
    * The operation resulted in an error.
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata type is `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CopyBackupMetadata)`.
    * The source backup name contains the string "test".
    * The operation started before 2022-01-18T14:50:00Z.
    * The operation resulted in an error.
  * `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata matches either of criteria:
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CreateBackupMetadata)` AND the source database name of the backup contains the string "test_db"
    * The operation's metadata type is `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/CopyBackupMetadata)` AND the source backup name contains the string "test_bkp"
    * The operation resulted in an error.

  
`pageSize` |  `integer` Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list#body.ListBackupOperationsResponse.FIELDS.next_page_token)` from a previous `[ListBackupOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list#body.ListBackupOperationsResponse)` to the same `parent` and with the same `filter`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[backupOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "operations": [
        {
          object ([Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`operations[]` |  `object (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instanceConfigs.operations#Operation)`)` The list of matching backup long-running operations. Each operation's name will be prefixed by the backup's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that are pending or have completed/failed/canceled within the last 7 days. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[backupOperations.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backupOperations/list#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations)` call to fetch more of the matching metadata.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
