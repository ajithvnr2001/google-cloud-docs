---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/list/
title: Method: projects.locations.backupCollections.backups.list \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:40:49.754211+00:00
---

# Method: projects.locations.backupCollections.backups.list  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Method: projects.locations.backupCollections.backups.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all backups owned by a backup collection.

### HTTP request

`GET https://redis.googleapis.com/v1alpha1/{parent=projects/*/locations/*/backupCollections/*}/backups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the backupCollection using the form: `projects/{projectId}/locations/{locationId}/backupCollections/{backup_collection_id}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's `[`nextPageToken`](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups/list#body.ListBackupsResponse.FIELDS.next_page_token)` to determine if there are more clusters left to be queried.  
`pageToken` |  `string` Optional. The `nextPageToken` value returned from a previous [ListBackupCollections] request, if any.  
  
### Request body

The request body must be empty.

### Response body

Response for `backups.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backups": [
        {
          object ([Backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups#Backup))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backups[]` |  `object (`[Backup](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.backupCollections.backups#Backup)`)` A list of backups in the project.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Backups that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/redis.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
