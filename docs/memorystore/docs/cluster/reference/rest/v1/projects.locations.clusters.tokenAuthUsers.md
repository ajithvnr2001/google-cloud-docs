---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers
title: REST Resource: projects.locations.clusters.tokenAuthUsers \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:37.606183+00:00
---

# REST Resource: projects.locations.clusters.tokenAuthUsers  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.clusters.tokenAuthUsers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TokenAuthUser
    * JSON representation
  * State
  * Methods



## Resource: TokenAuthUser

Represents a token based auth user for the cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the token based auth user. Format: projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{tokenAuthUser}  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers#State)`)` Output only. The state of the token based auth user.  
  
## State

Represents the different states of a token based auth user. New values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`ACTIVE` | The auth user is active.  
`CREATING` | The auth user is being created.  
`UPDATING` | The auth user is being updated.  
`DELETING` | The auth user is being deleted.  
  
## Methods  
  
---  
  
### `[addAuthToken](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/addAuthToken)`

|  Adds a auth token for a user of a token based auth enabled cluster.  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/delete)`

|  Deletes a token auth user for a token based auth enabled cluster.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/get)`

|  Gets a specific token auth user for a basic auth enabled cluster.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1/projects.locations.clusters.tokenAuthUsers/list)`

|  Lists all the token auth users for a token based auth enabled cluster.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
