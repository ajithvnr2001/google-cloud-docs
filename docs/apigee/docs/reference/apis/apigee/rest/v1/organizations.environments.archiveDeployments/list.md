---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/list/
title: Method: organizations.environments.archiveDeployments.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:51.727244+00:00
---

# Method: organizations.environments.archiveDeployments.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.environments.archiveDeployments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists the ArchiveDeployments in the specified Environment.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/environments/*}/archiveDeployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the Environment for which to list Archive Deployments in the format: `organizations/{org}/environments/{env}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.archivedeployments.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Optional. An optional query used to return a subset of Archive Deployments using the semantics defined in <https://google.aip.dev/160>.  
`pageSize` |  `integer` Optional. Maximum number of Archive Deployments to return. If unspecified, at most 25 deployments will be returned.  
`pageToken` |  `string` Optional. Page token, returned from a previous archiveDeployments.list call, that you can use to retrieve the next page.  
  
### Request body

The request body must be empty.

### Response body

Response for archiveDeployments.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "archiveDeployments": [
        {
          object ([ArchiveDeployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments#ArchiveDeployment))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`archiveDeployments[]` |  `object (`[ArchiveDeployment](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.environments.archiveDeployments#ArchiveDeployment)`)` Archive Deployments in the specified environment.  
`nextPageToken` |  `string` Page token that you can include in a archiveDeployments.list request to retrieve the next page. If omitted, no subsequent pages exist.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
