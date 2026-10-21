---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/addAuthToken/
title: Method: projects.locations.clusters.tokenAuthUsers.addAuthToken \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:38.045781+00:00
---

# Method: projects.locations.clusters.tokenAuthUsers.addAuthToken  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/addAuthToken/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  Method: projects.locations.clusters.tokenAuthUsers.addAuthToken Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Adds a auth token for a user of a token based auth enabled cluster.

### HTTP request

`POST https://redis.googleapis.com/v1/{tokenAuthUser=projects/*/locations/*/clusters/*/tokenAuthUsers/*}:addAuthToken`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`tokenAuthUser` |  `string` Required. The name of the token auth user resource that this auth token will be added for. Format: projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{tokenAuthUser}  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authToken": {
        object ([AuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens#AuthToken))
      }
    }  
  
Fields  
---  
`authToken` |  `object (`[AuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers.authTokens#AuthToken)`)` Required. The auth token to add.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/redis.read-write`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
