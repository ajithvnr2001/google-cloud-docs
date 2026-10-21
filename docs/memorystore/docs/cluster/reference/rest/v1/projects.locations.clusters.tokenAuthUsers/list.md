---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/list/
title: Method: projects.locations.clusters.tokenAuthUsers.list \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:25:52.885497+00:00
---

# Method: projects.locations.clusters.tokenAuthUsers.list  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Method: projects.locations.clusters.tokenAuthUsers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all the token auth users for a token based auth enabled cluster.

### HTTP request

`GET https://redis.googleapis.com/v1/{parent=projects/*/locations/*/clusters/*}/tokenAuthUsers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource that this token based auth user will be listed for. Format: projects/{project}/locations/{location}/clusters/{cluster}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's The maximum value is 1000; values above 1000 will be coerced to 1000. `[`nextPageToken`](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/list#body.ListTokenAuthUsersResponse.FIELDS.next_page_token)` to determine if there are more clusters left to be queried.  
`pageToken` |  `string` Optional. The `nextPageToken` value returned from a previous [tokenAuthUsers.list] request, if any.  
`filter` |  `string` Optional. Expression for filtering results.  
`orderBy` |  `string` Optional. Sort results by a defined order.  
  
### Request body

The request body must be empty.

### Response body

Response message for [tokenAuthUsers.list][].

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tokenAuthUsers": [
        {
          object ([TokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers#TokenAuthUser))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`tokenAuthUsers[]` |  `object (`[TokenAuthUser](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers#TokenAuthUser)`)` A list of token auth users in the project.  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Unordered list. Token auth users that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/redis.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
