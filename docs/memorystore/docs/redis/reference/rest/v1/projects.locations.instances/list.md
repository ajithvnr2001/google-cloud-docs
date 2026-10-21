---
url: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list/
title: Method: projects.locations.instances.list \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:47.829320+00:00
---

# Method: projects.locations.instances.list  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/redis/apis)



Send feedback 

#  Method: projects.locations.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all Redis instances owned by a project in either the specified location (region) or all locations.

The location should have the following format:

  * `projects/{projectId}/locations/{locationId}`



If `locationId` is specified as `-` (wildcard), then all regions available to the project are queried, and the results are aggregated.

### HTTP request

`GET https://redis.googleapis.com/v1/{parent=projects/*/locations/*}/instances`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the instance location using the form: `projects/{projectId}/locations/{locationId}` where `locationId` refers to a GCP region.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.If not specified, a default value of 1000 will be used by the service. Regardless of the pageSize value, the response may include a partial list and a caller should only rely on response's `[`nextPageToken`](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list#body.ListInstancesResponse.FIELDS.next_page_token)` to determine if there are more instances left to be queried.  
`pageToken` |  `string` The `nextPageToken` value returned from a previous `[instances.list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list#google.cloud.redis.v1.CloudRedis.ListInstances)` request, if any.  
  
### Request body

The request body must be empty.

### Response body

Response for `[instances.list](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances/list#google.cloud.redis.v1.CloudRedis.ListInstances)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/memorystore/docs/redis/reference/rest/v1/projects.locations.instances#Instance)`)` A list of Redis instances in the project in the specified location, or across all locations.If the `locationId` in the parent field of the request is "-", all regions available to the project are queried, and the results aggregated. If in such an aggregated query a location is unavailable, a placeholder Redis entry is included in the response with the `name` field set to a value of the form `projects/{projectId}/locations/{locationId}/instances/`\- and the `status` field set to ERROR and `statusMessage` field set to "location not available for instances.list".  
`nextPageToken` |  `string` Token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-30 UTC."],[],[]] 
