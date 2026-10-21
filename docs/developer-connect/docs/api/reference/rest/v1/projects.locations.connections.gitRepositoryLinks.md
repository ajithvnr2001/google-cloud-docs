---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks
title: REST Resource: projects.locations.connections.gitRepositoryLinks \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:07.488126+00:00
---

# REST Resource: projects.locations.connections.gitRepositoryLinks  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.connections.gitRepositoryLinks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GitRepositoryLink
    * JSON representation
  * Methods



## Resource: GitRepositoryLink

Message describing the GitRepositoryLink object

JSON representation  
---  
      
    
    {
      "name": string,
      "cloneUri": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "labels": {
        string: string,
        ...
      },
      "etag": string,
      "reconciling": boolean,
      "annotations": {
        string: string,
        ...
      },
      "uid": string,
      "webhookId": string,
      "gitProxyUri": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the repository, in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
`cloneUri` |  `string` Required. Git Clone URI.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Delete timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairsAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Optional. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`reconciling` |  `boolean` Output only. Set to true when the connection is being set up or updated in the background.  
`annotations` |  `map (key: string, value: string)` Optional. Allows clients to store small amounts of arbitrary data.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. A system-assigned unique identifier for the GitRepositoryLink.  
`webhookId` |  `string` Output only. External ID of the webhook created for the repository.  
`gitProxyUri` |  `string` Output only. URI to access the linked repository through the Git Proxy. This field is only populated if the git proxy is enabled for the connection.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/create)`

|  Creates a GitRepositoryLink.  
  
### `[delete](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/delete)`

|  Deletes a single GitRepositoryLink.  
  
### `[fetchGitRefs](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs)`

|  Fetch the list of branches or tags for a given repository.  
  
### `[fetchReadToken](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadToken)`

|  Fetches read token of a given gitRepositoryLink.  
  
### `[fetchReadWriteToken](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchReadWriteToken)`

|  Fetches read/write token of a given gitRepositoryLink.  
  
### `[get](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/get)`

|  Gets details of a single GitRepositoryLink.  
  
### `[list](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/list)`

|  Lists GitRepositoryLinks in a given project, location, and connection.  
  
### `[processBitbucketCloudWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketCloudWebhook)`

|  ProcessBitbucketCloudWebhook is called by the external Bitbucket Cloud instances for notifying events.  
  
### `[processBitbucketDataCenterWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processBitbucketDataCenterWebhook)`

|  ProcessBitbucketDataCenterWebhook is called by the external Bitbucket Data Center instances for notifying events.  
  
### `[processGitLabEnterpriseWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabEnterpriseWebhook)`

|  ProcessGitLabEnterpriseWebhook is called by the external GitLab Enterprise instances for notifying events.  
  
### `[processGitLabWebhook](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/processGitLabWebhook)`

|  ProcessGitLabWebhook is called by the GitLab.com for notifying events.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
