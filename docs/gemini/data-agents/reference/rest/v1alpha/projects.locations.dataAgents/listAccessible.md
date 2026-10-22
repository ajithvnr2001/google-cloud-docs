---
url: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/listAccessible/
title: Method: projects.locations.dataAgents.listAccessible \u00a0|\u00a0 Data Agents \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:58.320526+00:00
---

# Method: projects.locations.dataAgents.listAccessible  |  Data Agents  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/listAccessible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Reference ](https://docs.cloud.google.com/gemini/data-agents/reference/rest)



Send feedback 

#  Method: projects.locations.dataAgents.listAccessible Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * CreatorFilter



Lists DataAgents that are accessible to the caller in a given project and location.

### HTTP request

`GET https://geminidataanalytics.googleapis.com/v1alpha/{parent=projects/*/locations/*}/dataAgents:listAccessible`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent value for ListAccessibleDataAgentsRequest.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A page token, received from a previous `dataAgents.listAccessible` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `dataAgents.listAccessible` must match the call that provided the page token. The service may return fewer than this value.  
`filter` |  `string` Optional. Filtering results. See [AIP-160](https://google.aip.dev/160) for syntax.  
`orderBy` |  `string` Optional. User specification for how to order the results.  
`showDeleted` |  `boolean` Optional. If true, the list results will include soft-deleted DataAgents. Defaults to false.  
`creatorFilter` |  `enum (`[CreatorFilter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents/listAccessible#CreatorFilter)`)` Optional. Filter for the creator of the agent.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing accessible DataAgents.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "dataAgents": [
        {
          object ([DataAgent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#DataAgent))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`dataAgents[]` |  `object (`[DataAgent](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1alpha/projects.locations.dataAgents#DataAgent)`)` The list of accessible DataAgent.  
`nextPageToken` |  `string` The next page token or empty if none.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## CreatorFilter

Filter for the creator of the agent.

Enums  
---  
`CREATOR_FILTER_UNSPECIFIED` | Default value.  
`NONE` | No creator-specific filter will be applied. All agents will be returned.  
`CREATOR_ONLY` | Only agents created by the user calling the API will be returned.  
`NOT_CREATOR_ONLY` | Only agents not created by the user calling the API will be returned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
