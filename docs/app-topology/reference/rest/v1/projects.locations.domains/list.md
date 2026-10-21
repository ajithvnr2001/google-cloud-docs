---
url: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/list/
title: Method: projects.locations.domains.list \u00a0|\u00a0 App Topology \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:28:13.151801+00:00
---

# Method: projects.locations.domains.list  |  App Topology  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ App Topology ](https://docs.cloud.google.com/app-topology)
  * [ APIs & Reference ](https://docs.cloud.google.com/app-topology/apis)



Send feedback 

#  Method: projects.locations.domains.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists the topology domains available in a specific location. Only `global` location is supported.

### HTTP request

`GET https://apptopology.googleapis.com/v1/{parent=projects/*/locations/*}/domains`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent location to list domains for. Format: `projects/{project}/locations/{location}` Only `global` location is supported.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of domains to return. The service may return fewer than this value. If unspecified, at most 50 domains will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `domains.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `domains.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response for domains.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "domains": [
        {
          object ([Domain](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains#Domain))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`domains[]` |  `object (`[Domain](https://docs.cloud.google.com/app-topology/reference/rest/v1/projects.locations.domains#Domain)`)` The domains in the specified location.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/apptopology.read-write`
  * `https://www.googleapis.com/auth/apptopology.read-only`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `apptopology.domains.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
