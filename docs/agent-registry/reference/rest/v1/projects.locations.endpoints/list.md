---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list/
title: Method: projects.locations.endpoints.list \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:33.077693+00:00
---

# Method: projects.locations.endpoints.list  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  Method: projects.locations.endpoints.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists Endpoints in a given project and location.

### HTTP request

`GET https://agentregistry.googleapis.com/v1/{parent=projects/*/locations/*}/endpoints`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location to list endpoints in. Expected format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. A query string used to filter the list of endpoints returned. The filter expression must follow AIP-160 syntax.Filtering is supported on the `name`, `displayName`, `description`, `version`, and `interfaces` fields.Some examples:

  * `name = "projects/p1/locations/l1/endpoints/e1"`
  * `displayName = "my-endpoint"`
  * `description = "my-endpoint-description"`
  * `version = "v1"`
  * `interfaces.transport = "HTTP_JSON"`

  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing Endpoints

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "endpoints": [
        {
          object ([Endpoint](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints#Endpoint))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`endpoints[]` |  `object (`[Endpoint](https://docs.cloud.google.com/agent-registry/reference/rest/v1/projects.locations.endpoints#Endpoint)`)` The list of Endpoint resources matching the parent and filter criteria in the request. Each Endpoint resource follows the format: `projects/{project}/locations/{location}/endpoints/{endpoint}`.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. Used in `pageToken`.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/cloud-platform.read-only`
  * `https://www.googleapis.com/auth/agentregistry.read-write`
  * `https://www.googleapis.com/auth/agentregistry.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentregistry.endpoints.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-24 UTC."],[],[]] 
