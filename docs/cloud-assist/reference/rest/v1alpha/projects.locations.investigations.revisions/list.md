---
url: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/list/
title: Method: projects.locations.investigations.revisions.list \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:40:53.986744+00:00
---

# Method: projects.locations.investigations.revisions.list  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  Method: projects.locations.investigations.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists Investigations in a given project.

### HTTP request

`GET https://geminicloudassist.googleapis.com/v1alpha/{parent=projects/*/locations/*/investigations/*}/revisions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent to return Investigation revisions for. Within the parent, the location must be set to "global".  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested number of items to return. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. A token identifying a page of results the server should return.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing revisions of a given Investigation

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "revisions": [
        {
          object ([InvestigationRevision](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions#InvestigationRevision))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`revisions[]` |  `object (`[InvestigationRevision](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions#InvestigationRevision)`)` The list of Investigation revisions  
`nextPageToken` |  `string` A token to use in subsequent requests in order to return the next set of results.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `geminicloudassist.investigationRevisions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-07 UTC."],[],[]] 
