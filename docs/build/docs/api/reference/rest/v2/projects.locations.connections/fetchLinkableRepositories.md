---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/fetchLinkableRepositories/
title: Method: projects.locations.connections.fetchLinkableRepositories \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:27.133863+00:00
---

# Method: projects.locations.connections.fetchLinkableRepositories  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections/fetchLinkableRepositories/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: projects.locations.connections.fetchLinkableRepositories Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



connections.fetchLinkableRepositories get repositories from SCM that are accessible and could be added to the connection.

### HTTP request

`GET https://cloudbuild.googleapis.com/v2/{connection=projects/*/locations/*/connections/*}:fetchLinkableRepositories`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`connection` |  `string` Required. The name of the Connection. Format: `projects/*/locations/*/connections/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Number of results to return in the list. Default to 20.  
`pageToken` |  `string` Page start.  
  
### Request body

The request body must be empty.

### Response body

Response message for connections.fetchLinkableRepositories.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "repositories": [
        {
          object ([Repository](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories#Repository))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`repositories[]` |  `object (`[Repository](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories#Repository)`)` repositories ready to be created.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `connection` resource:

  * `cloudbuild.connections.fetchLinkableRepositories`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
