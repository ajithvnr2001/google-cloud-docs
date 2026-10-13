---
url: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms/list/
title: Method: projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms.list \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:05:02.270333+00:00
---

# Method: projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms.list  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms/list/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Reference ](https://docs.cloud.google.com/gemini/enterprise/docs/apis)



Send feedback 

#  Method: projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



List all `[AlphaEvolveProgram](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms#AlphaEvolveProgram)`s in a given experiment that follow the criteria provided in the request.

### HTTP request

Choose an endpoint:

globalus

  
`GET https://discoveryengine.googleapis.com/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*/sessions/*/alphaEvolveExperiments/*}/alphaEvolvePrograms`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name (AlphaEvolveExperiment) of the experiment. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}/alphaEvolveExperiments/{alphaEvolveExperiment}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of programs to return. The service may return fewer than this value.  
`pageToken` |  `string` Optional. A page token, received from a previous `alphaEvolvePrograms.list` call. Provide this to retrieve the subsequent page.  
`orderBy` |  `string` Optional. Sorting criterion for the programs. Comma separated list of metrics to sort by and optionally sort order, e.g. "score1 desc, score2". The criteria are applied in the order listed in the field. An implicit criterion of sorting by createTime descending is always applied as the final tie-breaker after all other specified criteria.  
`stateFilter` |  `enum (`[ProgramState](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms#ProgramState)`)` Optional. Filter to apply to the programs. Examples: "stateFilter = 'COMPLETED'" "stateFilter = 'INITIALIZED' OR "stateFilter = 'EVALUATING'"If empty, the behavior defaults to listing programs in REGISTRATION_COMPLETE state or processing state is NULL.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[AlphaEvolveService.ListAlphaEvolvePrograms](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms/list#google.cloud.discoveryengine.v1alpha.AlphaEvolveService.ListAlphaEvolvePrograms)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "alphaEvolvePrograms": [
        {
          object ([AlphaEvolveProgram](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms#AlphaEvolveProgram))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`alphaEvolvePrograms[]` |  `object (`[AlphaEvolveProgram](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1alpha/projects.locations.collections.engines.sessions.alphaEvolveExperiments.alphaEvolvePrograms#AlphaEvolveProgram)`)` Output only. List of programs matching the criteria provided in the request.  
`nextPageToken` |  `string` Output only. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/discoveryengine.readwrite`
  * `https://www.googleapis.com/auth/discoveryengine.serving.readwrite`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
