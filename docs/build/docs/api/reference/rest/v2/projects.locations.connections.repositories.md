---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories
title: REST Resource: projects.locations.connections.repositories \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:27.256841+00:00
---

# REST Resource: projects.locations.connections.repositories  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  REST Resource: projects.locations.connections.repositories Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Repository
    * JSON representation
  * Methods



## Resource: Repository

A repository associated to a parent connection.

JSON representation  
---  
      
    
    {
      "name": string,
      "remoteUri": string,
      "createTime": string,
      "updateTime": string,
      "annotations": {
        string: string,
        ...
      },
      "etag": string,
      "webhookId": string
    }  
  
Fields  
---  
`name` |  `string` Immutable. Resource name of the repository, in the format `projects/*/locations/*/connections/*/repositories/*`.  
`remoteUri` |  `string` Required. Git Clone HTTPS URI.  
`createTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Server assigned timestamp for when the connection was created.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Timestamp)` format)` Output only. Server assigned timestamp for when the connection was updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`annotations` |  `map (key: string, value: string)` Optional. Allows clients to store small amounts of arbitrary data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`webhookId` |  `string` Output only. External ID of the webhook created for the repository.  
  
## Methods  
  
---  
  
### `[accessReadToken](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/accessReadToken)`

|  Fetches read token of a given repository.  
  
### `[accessReadWriteToken](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/accessReadWriteToken)`

|  Fetches read/write token of a given repository.  
  
### `[batchCreate](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/batchCreate)`

|  Creates multiple repositories inside a connection.  
  
### `[create](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/create)`

|  Creates a Repository.  
  
### `[delete](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/delete)`

|  Deletes a single repository.  
  
### `[fetchGitRefs](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/fetchGitRefs)`

|  Fetch the list of branches or tags for a given repository.  
  
### `[get](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/get)`

|  Gets details of a single repository.  
  
### `[list](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/list)`

|  Lists Repositories in a given connection.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
