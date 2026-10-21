---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections/list/
title: Method: projects.locations.backupCollections.list \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:35.213802+00:00
---

# Method: projects.locations.backupCollections.list  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Method: projects.locations.backupCollections.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all backup collections owned by a consumer project in either the specified location (region) or all locations.

If `locationId` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

### HTTP request

`GET https://redis.googleapis.com/v1/{parent=projects/*/locations/*}/backupCollections`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the backupCollection location using the form: `projects/{projectId}/locations/{locationId}` where `locationId` refers to a Google Cloud region.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's `[`nextPageToken`](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections/list#body.ListBackupCollectionsResponse.FIELDS.next_page_token)` to determine if there are more clusters left to be queried.  
`pageToken` |  `string` Optional. The `nextPageToken` value returned from a previous [backupCollections.list] request, if any.  
  
### Request body

The request body must be empty.

### Response body

Response for `backupCollections.list`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "backupCollections": [
        {
          object ([BackupCollection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections#BackupCollection))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`backupCollections[]` |  `object (`[BackupCollection](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.backupCollections#BackupCollection)`)` A list of backupCollections in the project.If the `locationId` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder backupCollection entry is included in the response with the `name` field set to a value of the form `projects/{projectId}/locations/{locationId}/backupCollections/`\- and the `status` field set to ERROR and `statusMessage` field set to "location not available for backupCollections.list".  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/redis.read-write`
  * `https://www.googleapis.com/auth/redis.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
