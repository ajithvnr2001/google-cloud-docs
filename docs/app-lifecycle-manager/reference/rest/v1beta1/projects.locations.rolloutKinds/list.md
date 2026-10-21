---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/list/
title: Method: projects.locations.rolloutKinds.list \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:05.674950+00:00
---

# Method: projects.locations.rolloutKinds.list  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds/list/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  Method: projects.locations.rolloutKinds.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Retrieve a collection of rollout kinds.

### HTTP request

`GET https://saasservicemgmt.googleapis.com/v1beta1/{parent=projects/*/locations/*}/rolloutKinds`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent of the rollout kind.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of rollout kinds to send per page.  
`pageToken` |  `string` The page token: If the nextPageToken from a previous response is provided, this request will send the subsequent page.  
`filter` |  `string` Filter the list as specified in <https://google.aip.dev/160>.  
`orderBy` |  `string` Order results as specified in <https://google.aip.dev/132>.  
  
### Request body

The request body must be empty.

### Response body

The response structure for the rolloutKinds.list method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "rolloutKinds": [
        {
          object ([RolloutKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds#RolloutKind))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`rolloutKinds[]` |  `object (`[RolloutKind](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rolloutKinds#RolloutKind)`)` The resulting rollout kinds.  
`nextPageToken` |  `string` If present, the next page token can be provided to a subsequent rolloutKinds.list call to list the next page. If empty, there are no more pages.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `saasservicemgmt.rolloutKinds.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
