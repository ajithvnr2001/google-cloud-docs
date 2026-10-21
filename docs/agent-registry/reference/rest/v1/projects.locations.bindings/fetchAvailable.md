---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/fetchAvailable/
title: Method: projects.locations.bindings.fetchAvailable \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:31.526187+00:00
---

# Method: projects.locations.bindings.fetchAvailable  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings/fetchAvailable/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.bindings.fetchAvailable Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetches available Bindings.

### HTTP request

`GET https://agentregistry.googleapis.com/v1/{parent=projects/*/locations/*}/bindings:fetchAvailable`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, in the format `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. Page size is 500 if unspecified and is capped at `500` even if a larger value is given.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
Required. The reference of the source Agent Registry resource. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`sourceIdentifier` |  `string` The identifier of the source Agent. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`

  
End of mutually exclusive fields.  
The reference of the target Agent Registry resource. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`targetIdentifier` |  `string` Optional. The identifier of the target Agent, MCP Server, or Endpoint. Format:

  * `urn:agent:{publisher}:{namespace}:{name}`
  * `urn:mcp:{publisher}:{namespace}:{name}`
  * `urn:endpoint:{publisher}:{namespace}:{name}`

  
End of mutually exclusive fields.  
  
### Request body

The request body must be empty.

### Response body

Message for response to fetching available Bindings.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "bindings": [
        {
          object ([Binding](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Binding))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`bindings[]` |  `object (`[Binding](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.bindings#Binding)`)` The list of Bindings.  
`nextPageToken` |  `string` A token identifying a page of results the server should return.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.bindings.fetchAvailable`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
