---
url: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list/
title: Method: projects.instances.backups.list \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:03.673354+00:00
---

# Method: projects.instances.backups.list  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Method: projects.instances.backups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists completed and pending backups. Backups returned are ordered by `createTime` in descending order, starting from the most recent `createTime`.

### HTTP request

Choose a location:

global europe-west8 me-central2 us-central1 us-central2 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4 us-west8 us-east7

  
`GET https://spanner.googleapis.com/v1/{parent=projects/*/instances/*}/backups`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The instance to list backups from. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backups.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` An expression that filters the list of returned backups.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup)` are eligible for filtering:

  * `name`
  * `database`
  * `state`
  * `createTime` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `expireTime` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `versionTime` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `sizeBytes`
  * `backupSchedules`

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `name:Howl` \- The backup's name contains the string "howl".
  * `database:prod` \- The database's name contains the string "prod".
  * `state:CREATING` \- The backup is pending creation.
  * `state:READY` \- The backup is fully created and ready for use.
  * `(name:howl) AND (createTime < \"2018-03-28T14:50:00Z\")` \- The backup name contains the string "howl" and `createTime` of the backup is before 2018-03-28T14:50:00Z.
  * `expireTime < \"2018-03-28T14:50:00Z\"` \- The backup `expireTime` is before 2018-03-28T14:50:00Z.
  * `sizeBytes > 10000000000` \- The backup's size is greater than 10GB
  * `backupSchedules:daily` \- The backup is created from a schedule with "daily" in its name.

  
`pageSize` |  `integer` Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`pageToken` |  `string` If non-empty, `pageToken` should contain a `[nextPageToken](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list#body.ListBackupsResponse.FIELDS.next_page_token)` from a previous `[ListBackupsResponse](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list#body.ListBackupsResponse)` to the same `parent` and with the same `filter`.  
  
### Request body

The request body must be empty.

### Response body

The response for `[backups.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list#google.spanner.admin.database.v1.DatabaseAdmin.ListBackups)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups#Backup)`)` The list of matching backups. Backups returned are ordered by `createTime` in descending order, starting from the most recent `createTime`.  
`nextPageToken` |  `string` `nextPageToken` can be sent in a subsequent `[backups.list](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups/list#google.spanner.admin.database.v1.DatabaseAdmin.ListBackups)` call to fetch more of the matching backups.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-12 UTC."],[],[]] 
