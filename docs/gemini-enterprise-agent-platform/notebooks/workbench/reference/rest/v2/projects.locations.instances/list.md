---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/list/
title: Method: projects.locations.instances.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:27:23.058787+00:00
---

# Method: projects.locations.instances.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.instances.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists instances in a given project and location.

### HTTP request

`GET https://notebooks.googleapis.com/v2/{parent}/instances`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the instance. Formats: - `projects/{projectId}/locations/{location}` to list instances in a specific zone. - `projects/{projectId}/locations/-` to list instances in all locations. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `notebooks.instances.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Maximum return size of the list call.  
`pageToken` |  `string` Optional. A previous returned page token that can be used to continue listing from the last result.  
`orderBy` |  `string` Optional. Sort results. Supported values are "name", "name desc" or "" (unsorted).  
`filter` |  `string` Optional. List filter.  
  
### Request body

The request body must be empty.

### Response body

Response for listing notebook instances.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instances": [
        {
          object ([Instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances#Instance))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`instances[]` |  `object (`[Instance](https://docs.cloud.google.com/gemini-enterprise-agent-platform/notebooks/workbench/reference/rest/v2/projects.locations.instances#Instance)`)` A list of returned instances.  
`nextPageToken` |  `string` Page token that can be used to continue listing from the last result in the next list call.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached. For example, ['projects/{projectId}/locations/us-west1-a', 'projects/{projectId}/locations/us-central1-b']. A ListInstancesResponse will only contain either instances or unreachables,  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/notebooks`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
