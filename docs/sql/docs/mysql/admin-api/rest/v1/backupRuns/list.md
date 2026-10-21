---
url: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list/
title: Method: backupRuns.list \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:40:49.873919+00:00
---

# Method: backupRuns.list  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Method: backupRuns.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.

### HTTP request

`GET https://sqladmin.googleapis.com/v1/projects/{project}/instances/{instance}/backupRuns`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID of the project that contains the instance.  
`instance` |  `string` Cloud SQL instance ID, or "-" for all instances. This does not include the project ID.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer` Maximum number of backup runs per response.  
`pageToken` |  `string` A previously-returned page token representing part of the larger set of results to view.  
  
### Request body

The request body must be empty.

### Response body

Backup run list results.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "items": [
        {
          object ([BackupRun](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns#BackupRun))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#backupRunsList`.  
`items[]` |  `object (`[BackupRun](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1/backupRuns#BackupRun)`)` A list of backup runs in reverse chronological order of the enqueued time.  
`nextPageToken` |  `string` The continuation token, used to page through large result sets. Provide this value in a subsequent request to return the next page of results.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloudsql`
  * ` https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/sqlservice.admin`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-10 UTC."],[],[]] 
