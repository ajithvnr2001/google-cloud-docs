---
url: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/list/
title: Method: projects.locations.deployments.list \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:37.864623+00:00
---

# Method: projects.locations.deployments.list  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)
  * [ Reference ](https://docs.cloud.google.com/workload-manager/docs/authentication)



Send feedback 

#  Method: projects.locations.deployments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists Deployments in a given project and location.

### HTTP request

`GET https://workloadmanager.googleapis.com/v1/{parent=projects/*/locations/*}/deployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource prefix of the Deployment using the form: `projects/{projectId}/locations/{locationId}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filter resource following <https://google.aip.dev/160>.  
`orderBy` |  `string` Optional. Field to sort by. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing deployments.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "deployments": [
        {
          object ([Deployment](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Deployment))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`deployments[]` |  `object (`[Deployment](https://docs.cloud.google.com/workload-manager/docs/reference/rest/v1/projects.locations.deployments#Deployment)`)` The list of deployments.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-30 UTC."],[],[]] 
