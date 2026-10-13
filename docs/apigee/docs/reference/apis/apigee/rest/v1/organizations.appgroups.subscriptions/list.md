---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/list/
title: Method: organizations.appgroups.subscriptions.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:30.903820+00:00
---

# Method: organizations.appgroups.subscriptions.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.appgroups.subscriptions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



List all api product subscriptions for an appgroup.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/appgroups/*}/subscriptions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Name of the appgroup. Use the following structure in your request: `organizations/{org}/appgroups/{appgroup}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.appgroupsubscriptions.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of subscriptions to return. The service may return fewer than this value.If unspecified, at most 100 subscriptions will be returned. The maximum value is 1000; values above 1000 will be coerced to 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `subscriptions.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `subscriptions.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response for `[subscriptions.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions/list#google.cloud.apigee.v1.AppGroupSubscriptions.ListAppGroupSubscriptions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "appGroupSubscriptions": [
        {
          object ([AppGroupSubscription](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions#AppGroupSubscription))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`appGroupSubscriptions[]` |  `object (`[AppGroupSubscription](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.subscriptions#AppGroupSubscription)`)` The list of subscriptions for an AppGroup.  
`nextPageToken` |  `string` Value that can be sent as `pageToken` to retrieve the next page of content. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
