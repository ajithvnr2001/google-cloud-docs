---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/list/
title: Method: projects.locations.publishers.list \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:42.395842+00:00
---

# Method: projects.locations.publishers.list  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.publishers.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists all Publishers in a location.

### HTTP request

`GET https://agentregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/publishers`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent location to query. Format: `projects/{project}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Page limit size.  
`pageToken` |  `string` Optional. Page offset token.  
  
### Request body

The request body must be empty.

### Response body

Response listing Publishers.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "publishers": [
        {
          object ([Publisher](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers#Publisher))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`publishers[]` |  `object (`[Publisher](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.publishers#Publisher)`)` The returned list of Publishers.  
`nextPageToken` |  `string` Page offset continuation token.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.publishers.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-24 UTC."],[],[]] 
