---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/list/
title: Method: projects.locations.spaces.sharedTemplates.revisions.list \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:19.425870+00:00
---

# Method: projects.locations.spaces.sharedTemplates.revisions.list  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.spaces.sharedTemplates.revisions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Lists shared template revisions in a given space.

### HTTP request

`GET https://designcenter.googleapis.com/v1/{parent=projects/*/locations/*/spaces/*/sharedTemplates/*}/revisions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource from which to list shared template revisions, in the following format: `projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of nextPageToken in the response indicates that more results might be available.  
`pageToken` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. pageToken must be the value of nextPageToken from the previous response. The values of other method parameters should be identical to those in the previous call.  
`filter` |  `string` Optional. A filter that chooses which shared template revisions to return.  
`orderBy` |  `string` Optional. How the results should be sorted.  
  
### Request body

The request body must be empty.

### Response body

Message for response to listing shared templates.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "sharedTemplateRevisions": [
        {
          object ([SharedTemplateRevision](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions#SharedTemplateRevision))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`sharedTemplateRevisions[]` |  `object (`[SharedTemplateRevision](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates.revisions#SharedTemplateRevision)`)` The list of shared templates.  
`nextPageToken` |  `string` If there might be more results than those appearing in this response, then nextPageToken is included. To get the next set of results, call this method again using the value of nextPageToken as pageToken.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `designcenter.sharedTemplateRevisions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
