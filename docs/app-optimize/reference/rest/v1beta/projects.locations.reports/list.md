---
url: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/list/
title: Method: projects.locations.reports.list \u00a0|\u00a0 App Optimize \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:16:14.803529+00:00
---

# Method: projects.locations.reports.list  |  App Optimize  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ App Optimize ](https://docs.cloud.google.com/app-optimize)
  * [ Reference ](https://docs.cloud.google.com/app-optimize/apis)



Send feedback 

#  Method: projects.locations.reports.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists reports within a given project.

### HTTP request

`GET https://appoptimize.googleapis.com/v1beta/{parent=projects/*/locations/*}/reports`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent project whose reports are to be listed.Format: `projects/{project}/locations/{location}`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of reports to return. The service may return fewer than this value. If unspecified, the server will determine the number of results to return.  
`pageToken` |  `string` Optional. A page token, received from a previous `reports.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `reports.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for the `reports.list` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "reports": [
        {
          object ([Report](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports#Report))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`reports[]` |  `object (`[Report](https://docs.cloud.google.com/app-optimize/reference/rest/v1beta/projects.locations.reports#Report)`)` The list of reports.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is empty, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/appoptimize`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `appoptimize.reports.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
