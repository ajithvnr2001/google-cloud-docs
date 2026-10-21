---
url: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens
title: REST Resource: projects.locations.clusters.tokenAuthUsers.authTokens \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:51.179817+00:00
---

# REST Resource: projects.locations.clusters.tokenAuthUsers.authTokens  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Reference ](https://docs.cloud.google.com/memorystore/docs/cluster/apis)



Send feedback 

#  REST Resource: projects.locations.clusters.tokenAuthUsers.authTokens Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AuthToken
    * JSON representation
  * State
  * Methods



## Resource: AuthToken

Auth token for the cluster.

JSON representation  
---  
      
    
    {
      "name": string,
      "token": string,
      "createTime": string,
      "state": enum ([State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens#State))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the auth token. Format: projects/{project}/locations/{location}/clusters/{cluster}/tokenAuthUsers/{tokenAuthUser}/authTokens/{authToken}  
`token` |  `string` Output only. The service generated authentication token used to connect to the Redis cluster.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time of the auth token.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens#State)`)` Output only. State of the auth token.  
  
## State

Represents the different states of an auth token. New values may be added in the future.

Enums  
---  
`STATE_UNSPECIFIED` | Not set.  
`ACTIVE` | The auth token is active.  
`CREATING` | The auth token is being created.  
`DELETING` | The auth token is being deleted.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/delete)`

|  Removes a auth token for a user of a token based auth enabled instance.  
  
### `[get](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/get)`

|  Gets a specific auth token for a specific token auth user.  
  
### `[list](https://docs.cloud.google.com/memorystore/docs/cluster/reference/rest/v1alpha1/projects.locations.clusters.tokenAuthUsers.authTokens/list)`

|  Lists all the auth tokens for a specific token auth user.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
