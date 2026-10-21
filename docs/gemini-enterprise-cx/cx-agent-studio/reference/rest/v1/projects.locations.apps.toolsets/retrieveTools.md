---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/retrieveTools/
title: Method: projects.locations.apps.toolsets.retrieveTools \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:37.203209+00:00
---

# Method: projects.locations.apps.toolsets.retrieveTools  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/retrieveTools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Method: projects.locations.apps.toolsets.retrieveTools Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Retrieve the list of tools included in the specified toolset.

### HTTP request

`POST https://ces.googleapis.com/v1/{toolset=projects/*/locations/*/apps/*/toolsets/*}:retrieveTools`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`toolset` |  `string` Required. The name of the toolset to retrieve the tools for. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "toolIds": [
        string
      ],
      "bypassPersistenceConfig": boolean
    }  
  
Fields  
---  
`toolIds[]` |  `string` Optional. The identifiers of the tools to retrieve from the toolset. If empty, all tools in the toolset will be returned.  
`bypassPersistenceConfig` |  `boolean` Optional. If true, the returned tools will contain raw descriptions and schemas directly from the server, bypassing any stored persistence configurations (overrides/snapshots).  
  
### Response body

Response message for `[ToolService.RetrieveTools](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.toolsets/retrieveTools#google.cloud.ces.v1.ToolService.RetrieveTools)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "tools": [
        {
          object ([Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools#Tool))
        }
      ]
    }  
  
Fields  
---  
`tools[]` |  `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.tools#Tool)`)` The list of tools that are included in the specified toolset.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/ces`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `toolset` resource:

  * `ces.toolsets.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
