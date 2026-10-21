---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories/
title: Method: projects.locations.connections.fetchLinkableGitRepositories \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:13.139383+00:00
---

# Method: projects.locations.connections.fetchLinkableGitRepositories  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.fetchLinkableGitRepositories Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * LinkableGitRepository
    * JSON representation
  * Try it!



connections.fetchLinkableGitRepositories returns a list of git repositories from an SCM that are available to be added to a Connection.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{connection=projects/*/locations/*/connections/*}:fetchLinkableGitRepositories`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`connection` |  `string` Required. The name of the Connection. Format: `projects/*/locations/*/connections/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Number of results to return in the list. Defaults to 20.  
`pageToken` |  `string` Optional. Page start.  
  
### Request body

The request body must be empty.

### Response body

Response message for connections.fetchLinkableGitRepositories.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "linkableGitRepositories": [
        {
          object ([LinkableGitRepository](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories#LinkableGitRepository))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`linkableGitRepositories[]` |  `object (`[LinkableGitRepository](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchLinkableGitRepositories#LinkableGitRepository)`)` The git repositories that can be linked to the connection.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `connection` resource:

  * `developerconnect.connections.fetchLinkableGitRepositories`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## LinkableGitRepository

LinkableGitRepository represents a git repository that can be linked to a connection.

JSON representation  
---  
      
    
    {
      "cloneUri": string
    }  
  
Fields  
---  
`cloneUri` |  `string` The clone uri of the repository.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
