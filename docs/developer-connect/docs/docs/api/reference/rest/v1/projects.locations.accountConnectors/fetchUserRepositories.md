---
url: https://docs.cloud.google.com/developer-connect/docs/docs/api/reference/rest/v1/projects.locations.accountConnectors/fetchUserRepositories/
title: Method: projects.locations.accountConnectors.fetchUserRepositories \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:44:17.343275+00:00
---

# Method: projects.locations.accountConnectors.fetchUserRepositories  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/docs/api/reference/rest/v1/projects.locations.accountConnectors/fetchUserRepositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)



Send feedback 

#  Method: projects.locations.accountConnectors.fetchUserRepositories Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * UserRepository
    * JSON representation
  * Try it!



accountConnectors.fetchUserRepositories returns a list of UserRepos that are available for an account connector resource.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{accountConnector=projects/*/locations/*/accountConnectors/*}:fetchUserRepositories`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`accountConnector` |  `string` Required. The name of the Account Connector resource in the format: `projects/*/locations/*/accountConnectors/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Number of results to return in the list. Defaults to 20.  
`pageToken` |  `string` Optional. Page start.  
`repository` |  `string` Optional. The name of the repository. When specified, only the UserRepository with this name will be returned if the repository is accessible under this Account Connector for the calling user.  
  
### Request body

The request body must be empty.

### Response body

Response message for accountConnectors.fetchUserRepositories.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "userRepos": [
        {
          object ([UserRepository](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/fetchUserRepositories#UserRepository))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`userRepos[]` |  `object (`[UserRepository](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.accountConnectors/fetchUserRepositories#UserRepository)`)` The repositories that the user can access with this account connector.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## UserRepository

A user repository that can be linked to the account connector. Consists of the repo name and the git proxy URL to forward requests to this repo.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "gitProxyUri": string,
      "cloneUri": string
    }  
  
Fields  
---  
`displayName` |  `string` Output only. The user friendly repo name (e.g., myuser/myrepo)  
`gitProxyUri` |  `string` Output only. The Git proxy URL for this repo. For example: <https://us-west1-git.developerconnect.dev/a/my-proj/my-ac/myuser/myrepo.git>. Populated only when `proxyConfig.enabled` is set to `true` in the Account Connector. This URL is used by other Google services that integrate with Developer Connect.  
`cloneUri` |  `string` Output only. The git clone URL of the repo. For example: <https://github.com/myuser/myrepo.git>  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
