---
url: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/batchCreate/
title: Method: projects.locations.connections.repositories.batchCreate \u00a0|\u00a0 Cloud Build \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:59.784892+00:00
---

# Method: projects.locations.connections.repositories.batchCreate  |  Cloud Build  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/batchCreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Reference ](https://docs.cloud.google.com/build/docs/api)



Send feedback 

#  Method: projects.locations.connections.repositories.batchCreate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * CreateRepositoryRequest
    * JSON representation
  * Try it!



Creates multiple repositories inside a connection.

### HTTP request

`POST https://cloudbuild.googleapis.com/v2/{parent=projects/*/locations/*/connections/*}/repositories:batchCreate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The connection to contain all the repositories being created. Format: projects/*/locations/*/connections/* The parent field in the CreateRepositoryRequest messages must either be empty or match this field.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "requests": [
        {
          object ([CreateRepositoryRequest](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/batchCreate#CreateRepositoryRequest))
        }
      ]
    }  
  
Fields  
---  
`requests[]` |  `object (`[CreateRepositoryRequest](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories/batchCreate#CreateRepositoryRequest)`)` Required. The request messages specifying the repositories to create.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/build/docs/api/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudbuild.repositories.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## CreateRepositoryRequest

Message for creating a Repository.

JSON representation  
---  
      
    
    {
      "parent": string,
      "repository": {
        object ([Repository](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories#Repository))
      },
      "repositoryId": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The connection to contain the repository. If the request is part of a BatchCreateRepositoriesRequest, this field should be empty or match the parent specified there.  
`repository` |  `object (`[Repository](https://docs.cloud.google.com/build/docs/api/reference/rest/v2/projects.locations.connections.repositories#Repository)`)` Required. The repository to create.  
`repositoryId` |  `string` Required. The ID to use for the repository, which will become the final component of the repository's resource name. This ID should be unique in the connection. Allows alphanumeric characters and any of -._~%!$&'()*+,;=@.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
