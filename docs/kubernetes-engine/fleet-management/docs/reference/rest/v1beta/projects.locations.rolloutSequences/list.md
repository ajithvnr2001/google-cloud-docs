---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/list/
title: Method: projects.locations.rolloutSequences.list \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:19.779629+00:00
---

# Method: projects.locations.rolloutSequences.list  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences/list/

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  Method: projects.locations.rolloutSequences.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Retrieve the list of all rollout sequences.

### HTTP request

`GET https://gkehub.googleapis.com/v1beta/{parent=projects/*/locations/*}/rolloutSequences`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of rollout sequences. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of rollout sequences to return. The service may return fewer than this value. If unspecified, at most 50 rollout sequences will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `rolloutSequences.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `rolloutSequences.list` must match the call that provided the page token.  
`filter` |  `string` Optional. Lists Rollout Sequences that match the filter expression, following the syntax outlined in <https://google.aip.dev/160>.  
  
### Request body

The request body must be empty.

### Response body

Response message for listing rollout sequences.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rolloutSequences": [
        {
          object ([RolloutSequence](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences#RolloutSequence))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`rolloutSequences[]` |  `object (`[RolloutSequence](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1beta/projects.locations.rolloutSequences#RolloutSequence)`)` The rollout sequences from the specified parent resource.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-13 UTC."],[],[]] 
