---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/list/
title: Method: projects.locations.customRanges.list \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:02:30.531133+00:00
---

# Method: projects.locations.customRanges.list  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Method: projects.locations.customRanges.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists CustomRanges in a given project and location.

### HTTP request

`GET https://cloudnumberregistry.googleapis.com/v1alpha/{parent=projects/*/locations/*}/customRanges`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name, for example `projects/*/locations/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
`filter` |  `string` Optional. Filter expression to filter the results.  
`orderBy` |  `string` Optional. Hint for how to order the results.  
  
### Request body

The request body must be empty.

### Response body

Response message for the `[CloudNumberRegistry.ListCustomRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/list#google.cloud.numberregistry.v1alpha.CloudNumberRegistry.ListCustomRanges)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "customRanges": [
        {
          object ([CustomRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges#CustomRange))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`customRanges[]` |  `object (`[CustomRange](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges#CustomRange)`)` The list of CustomRanges.  
`nextPageToken` |  `string` A token to retrieve the next page of results, or empty if there are no more results in the list.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `cloudnumberregistry.customRanges.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
