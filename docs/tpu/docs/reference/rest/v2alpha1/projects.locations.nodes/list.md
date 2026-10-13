---
url: https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations.nodes/list/
title: Method: projects.locations.nodes.list \u00a0|\u00a0 Cloud TPU \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:00.778188+00:00
---

# Method: projects.locations.nodes.list  |  Cloud TPU  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations.nodes/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Reference ](https://docs.cloud.google.com/tpu/docs/reference)



Send feedback 

#  Method: projects.locations.nodes.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists nodes.

### HTTP request

`GET https://tpu.googleapis.com/v2alpha1/{parent=projects/*/locations/*}/nodes`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of items to return.  
`pageToken` |  `string` The nextPageToken value returned from a previous List request, if any.  
  
### Request body

The request body must be empty.

### Response body

Response for `[nodes.list](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations.nodes/list#google.cloud.tpu.v2alpha1.Tpu.ListNodes)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "nodes": [
        {
          object ([Node](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations.nodes#Node))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`nodes[]` |  `object (`[Node](https://docs.cloud.google.com/tpu/docs/reference/rest/v2alpha1/projects.locations.nodes#Node)`)` The listed nodes.  
`nextPageToken` |  `string` The next page token or empty if none.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud.tpu`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `tpu.nodes.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-15 UTC."],[],[]] 
