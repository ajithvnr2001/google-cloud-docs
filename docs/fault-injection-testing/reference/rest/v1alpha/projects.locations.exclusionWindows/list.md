---
url: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/list/
title: Method: projects.locations.exclusionWindows.list \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:11:42.012402+00:00
---

# Method: projects.locations.exclusionWindows.list  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/list/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Reference ](https://docs.cloud.google.com/fault-injection-testing/apis)



Send feedback 

#  Method: projects.locations.exclusionWindows.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes



Lists all exclusion windows in a project and region, or all exclusion windows in a project in all regions if the location is given as "-".

### HTTP request

`GET https://faulttesting.googleapis.com/v1alpha/{parent=projects/*/locations/*}/exclusionWindows`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The project and location from which to list exclusion windows. Format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of exclusion windows to return from this call. The service may return fewer than this value. If unspecified, at most 1000 will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `exclusionWindows.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `exclusionWindows.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[FaultTesting.ListExclusionWindows](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows/list#google.cloud.faulttesting.v1alpha.FaultTesting.ListExclusionWindows)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "exclusionWindows": [
        {
          object ([ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows#ExclusionWindow))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`exclusionWindows[]` |  `object (`[ExclusionWindow](https://docs.cloud.google.com/fault-injection-testing/reference/rest/v1alpha/projects.locations.exclusionWindows#ExclusionWindow)`)` The exclusion windows from the specified project.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached, each with the format `projects/{project}/locations/{location}`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
