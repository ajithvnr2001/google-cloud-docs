---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry/
title: Method: projects.getAncestry \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:20.650154+00:00
---

# Method: projects.getAncestry  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Method: projects.getAncestry Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Ancestor
    * JSON representation
  * Try it!



Gets a list of ancestors in the resource hierarchy for the Project identified by the specified `projectId` (for example, `my-project-123`).

The caller must have read permissions for this Project.

### HTTP request

`POST https://cloudresourcemanager.googleapis.com/v1/projects/{projectId}:getAncestry`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`projectId` |  `string` Required. The Project ID (for example, `my-project-123`). Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `projectId`:

  * `resourcemanager.projects.get`

  
  
### Request body

The request body must be empty.

### Response body

Response from the `[projects.getAncestry](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry#google.cloudresourcemanager.v1.Projects.GetAncestry)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "ancestor": [
        {
          object ([Ancestor](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry#Ancestor))
        }
      ]
    }  
  
Fields  
---  
`ancestor[]` |  `object (`[Ancestor](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry#Ancestor)`)` Ancestors are ordered from bottom to top of the resource hierarchy. The first ancestor is the project itself, followed by the project's parent, etc..  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/cloudplatformprojects`
  * `https://www.googleapis.com/auth/cloudplatformprojects.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## Ancestor

Identifying information for a single ancestor of a project.

JSON representation  
---  
      
    
    {
      "resourceId": {
        object ([ResourceId](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#ResourceId))
      }
    }  
  
Fields  
---  
`resourceId` |  `object (`[ResourceId](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#ResourceId)`)` Resource id of the ancestor.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-11 UTC."],[],[]] 
