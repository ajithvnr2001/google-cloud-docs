---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/list/
title: Method: projects.configs.list \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:32:33.403969+00:00
---

# Method: projects.configs.list  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Method: projects.configs.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists all the RuntimeConfig resources within project.

### HTTP request

`GET https://runtimeconfig.googleapis.com/v1beta1/{parent=projects/*}/configs`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The [project ID](https://support.google.com/cloud/answer/6158840?hl=en&ref_topic=6158848) for this request, in the format `projects/[PROJECT_ID]`. Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `parent`:

  * `runtimeconfig.configs.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `number` Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements.   
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.   
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

`configs.list()` returns the following response. The order of returned objects is arbitrary; that is, it is not ordered in any particular way.

JSON representation  
---  
      
    
    {
      "configs": [
        {
          object([RuntimeConfig](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs#RuntimeConfig))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`configs[]` |  `object(`[RuntimeConfig](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs#RuntimeConfig)`)` A list of the configurations in the project. The order of returned objects is arbitrary; that is, it is not ordered in any particular way.   
`nextPageToken` |  `string` This token allows you to get the next page of results for list requests. If the number of results is larger than `pageSize`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results   
  
### Authorization Scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloudruntimeconfig`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

## Try it!

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
