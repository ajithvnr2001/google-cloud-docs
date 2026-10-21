---
url: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations/
title: Method: projects.locations.connections.fetchGitHubInstallations \u00a0|\u00a0 Developer Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:37:07.541674+00:00
---

# Method: projects.locations.connections.fetchGitHubInstallations  |  Developer Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Connect ](https://docs.cloud.google.com/developer-connect/docs)
  * [ Reference ](https://docs.cloud.google.com/developer-connect/docs/authentication)



Send feedback 

#  Method: projects.locations.connections.fetchGitHubInstallations Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Installation
    * JSON representation
  * Try it!



connections.fetchGitHubInstallations returns the list of GitHub Installations that are available to be added to a Connection. For github.com, only installations accessible to the authorizer token are returned. For GitHub Enterprise, all installations are returned.

### HTTP request

`GET https://developerconnect.googleapis.com/v1/{connection=projects/*/locations/*/connections/*}:fetchGitHubInstallations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`connection` |  `string` Required. The resource name of the connection in the format `projects/*/locations/*/connections/*`.  
  
### Request body

The request body must be empty.

### Response body

Response of fetching github installations.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "installations": [
        {
          object ([Installation](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations#Installation))
        }
      ]
    }  
  
Fields  
---  
`installations[]` |  `object (`[Installation](https://docs.cloud.google.com/developer-connect/docs/api/reference/rest/v1/projects.locations.connections/fetchGitHubInstallations#Installation)`)` List of installations available to the OAuth user (for github.com) or all the installations (for GitHub enterprise).  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `connection` resource:

  * `developerconnect.connections.fetchGitHubInstallations`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Installation

Represents an installation of the GitHub App.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "type": string
    }  
  
Fields  
---  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` ID of the installation in GitHub.  
`name` |  `string` Name of the GitHub user or organization that owns this installation.  
`type` |  `string` Either "user" or "organization".  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-09 UTC."],[],[]] 
