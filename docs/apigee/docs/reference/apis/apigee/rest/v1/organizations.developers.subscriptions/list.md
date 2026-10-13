---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list/
title: Method: organizations.developers.subscriptions.list \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:40.700446+00:00
---

# Method: organizations.developers.subscriptions.list  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.subscriptions.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Try it!



Lists all API product subscriptions for a developer.

### HTTP request

`GET https://apigee.googleapis.com/v1/{parent=organizations/*/developers/*}/subscriptions`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Email address of the developer. Use the following structure in your request: `organizations/{org}/developers/{developerEmail}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.developersubscriptions.list`

  
  
### Query parameters

Parameters  
---  
`startKey` |  `string` Name of the API product subscription from which to start displaying the list of subscriptions. If omitted, the list starts from the first item.For example, to view the API product subscriptions from 51-150, set the value of `startKey` to the name of the 51st subscription and set the value of `count` to 100.  
`count` |  `integer` Number of API product subscriptions to return in the API call. Use with `startKey` to provide more targeted filtering. Defaults to 100. The maximum limit is 1000.  
  
### Request body

The request body must be empty.

### Response body

Response for `[subscriptions.list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list#google.cloud.apigee.v1.DeveloperSubscriptions.ListDeveloperSubscriptions)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "developerSubscriptions": [
        {
          object ([DeveloperSubscription](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions#DeveloperSubscription))
        }
      ],
      "nextStartKey": string
    }  
  
Fields  
---  
`developerSubscriptions[]` |  `object (`[DeveloperSubscription](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions#DeveloperSubscription)`)` List of all subscriptions.  
`nextStartKey` |  `string` Value that can be sent as `startKey` to retrieve the next page of content. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
