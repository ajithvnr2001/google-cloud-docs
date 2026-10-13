---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines/list/
title: Method: projects.locations.collections.engines.list \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:15.483524+00:00
---

# Method: projects.locations.collections.engines.list  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines/list/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.engines.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists all the `[Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines#Engine)`s associated with the project.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1beta/{parent=projects/*/locations/*/collections/*}/engines`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collectionId}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Not supported.  
`pageToken` |  `string` Optional. Not supported.  
`filter` |  `string` Optional. Filter by solution type. For example: solutionType=SOLUTION_TYPE_SEARCH  
  
### Request body

The request body must be empty.

### Response body

Response message for `[EngineService.ListEngines](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines/list#google.cloud.discoveryengine.v1beta.EngineService.ListEngines)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "engines": [
        {
          object ([Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines#Engine))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`engines[]` |  `object (`[Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines#Engine)`)` All the customer's `[Engine](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1beta/projects.locations.collections.engines#Engine)`s.  
`nextPageToken` |  `string` Not supported.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `discoveryengine.engines.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
