---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs/
title: Method: projects.locations.connections.gitRepositoryLinks.fetchGitRefs \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:37:36.061834+00:00
---

# Method: projects.locations.connections.gitRepositoryLinks.fetchGitRefs  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.gitRepositoryLinks.fetchGitRefs Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * RefType
  * Try it!



Fetch the list of branches or tags for a given repository.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{gitRepositoryLink=projects/*/locations/*/connections/*/gitRepositoryLinks/*}:fetchGitRefs`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`gitRepositoryLink` |  `string` Required. The resource name of GitRepositoryLink in the format `projects/*/locations/*/connections/*/gitRepositoryLinks/*`.  
  
### Query parameters

Parameters  
---  
`refType` |  `enum (`[RefType](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections.gitRepositoryLinks/fetchGitRefs#RefType)`)` Required. Type of refs to fetch.  
`pageSize` |  `integer` Optional. Number of results to return in the list. Default to 20.  
`pageToken` |  `string` Optional. Page start.  
  
### Request body

The request body must be empty.

### Response body

Response for fetching git refs.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "refNames": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`refNames[]` |  `string` Name of the refs fetched.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `gitRepositoryLink` resource:

  * `developerconnect.gitRepositoryLinks.fetchGitRefs`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## RefType

Type of refs.

Enums  
---  
`REF_TYPE_UNSPECIFIED` | No type specified.  
`TAG` | To fetch tags.  
`BRANCH` | To fetch branches.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
