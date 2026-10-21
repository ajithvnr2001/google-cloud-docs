---
url: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list/
title: Method: projects.configs.variables.list \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:28:19.510741+00:00
---

# Method: projects.configs.variables.list  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager)
  * [ Reference ](https://docs.cloud.google.com/deployment-manager/docs/apis)



Send feedback 

#  Method: projects.configs.variables.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization Scopes
  * Try it!



Lists variables within given a configuration, matching any provided filters. This only lists variable names, not the values, unless `returnValues` is true, in which case only variables that user has IAM permission to variables.get will be returned.

### HTTP request

`GET https://runtimeconfig.googleapis.com/v1beta1/{parent=projects/*/configs/*}/variables`

The URL uses [gRPC Transcoding](https://github.com/googleapis/googleapis/blob/master/google/api/http.proto) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` The path to the RuntimeConfig resource for which you want to list variables. The configuration must exist beforehand; the path must be in the format:`projects/[PROJECT_ID]/configs/[CONFIG_NAME]` Authorization requires the following [Google IAM](https://cloud.google.com/iam) permission on the specified resource `parent`:

  * `runtimeconfig.variables.list`

  
  
### Query parameters

Parameters  
---  
`filter` |  `string` Filters variables by matching the specified filter. For example:`projects/example-project/config/[CONFIG_NAME]/variables/example-variable`.  
`pageSize` |  `number` Specifies the number of results to return per page. If there are fewer elements than the specified number, returns all elements.   
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to a `nextPageToken` returned by a previous list request to get the next page of results.   
`returnValues` |  `boolean` The flag indicates whether the user wants to return values of variables. If true, then only those variables that user has IAM variables.get permission will be returned along with their values.   
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

Response for the `variables.list()` method.

JSON representation  
---  
      
    
    {
      "variables": [
        {
          object([Variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#Variable))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`variables[]` |  `object(`[Variable](https://docs.cloud.google.com/deployment-manager/runtime-configurator/reference/rest/v1beta1/projects.configs.variables#Variable)`)` A list of variables and their values. The order of returned variable objects is arbitrary.   
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
