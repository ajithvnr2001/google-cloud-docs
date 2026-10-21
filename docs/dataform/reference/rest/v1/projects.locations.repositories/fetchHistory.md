---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchHistory/
title: Method: projects.locations.repositories.fetchHistory \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:03.202508+00:00
---

# Method: projects.locations.repositories.fetchHistory  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchHistory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Method: projects.locations.repositories.fetchHistory Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * CommitLogEntry
    * JSON representation
  * Try it!



Fetches a Repository's history of commits. The Repository must not have a value for `gitRemoteSettings.url`.

### HTTP request

Choose a location:

global africa-south1 asia-east1 asia-east2 asia-northeast1 asia-northeast2 asia-northeast3 asia-south1 asia-south2 asia-southeast1 asia-southeast2 australia-southeast1 australia-southeast2 europe-central2 europe-north1 europe-southwest1 europe-west1 europe-west10 europe-west12 europe-west2 europe-west3 europe-west4 europe-west6 europe-west8 europe-west9 me-central1 me-central2 me-west1 northamerica-northeast1 northamerica-northeast2 southamerica-east1 southamerica-west1 us-central1 us-east1 us-east4 us-east5 us-south1 us-west1 us-west2 us-west3 us-west4

  
`GET https://dataform.googleapis.com/v1/{name=projects/*/locations/*/repositories/*}:fetchHistory`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The repository's name. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `dataform.repositories.fetchHistory`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum number of commits to return. The server may return fewer items than requested. If unspecified, the server will pick an appropriate default.  
`pageToken` |  `string` Optional. Page token received from a previous `repositories.fetchHistory` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `repositories.fetchHistory`, with the exception of `pageSize`, must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

`repositories.fetchHistory` response message.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "commits": [
        {
          object ([CommitLogEntry](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchHistory#CommitLogEntry))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`commits[]` |  `object (`[CommitLogEntry](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/fetchHistory#CommitLogEntry)`)` A list of commit logs, ordered by 'git log' default order.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/bigquery`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `dataform.repositories.fetchHistory`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CommitLogEntry

Represents a single commit log.

JSON representation  
---  
      
    
    {
      "commitTime": string,
      "commitSha": string,
      "author": {
        object ([CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1/CommitAuthor))
      },
      "commitMessage": string
    }  
  
Fields  
---  
`commitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Commit timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`commitSha` |  `string` The commit SHA for this commit log entry.  
`author` |  `object (`[CommitAuthor](https://docs.cloud.google.com/dataform/reference/rest/v1/CommitAuthor)`)` The commit author for this commit log entry.  
`commitMessage` |  `string` The commit message for this commit log entry.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-27 UTC."],[],[]] 
