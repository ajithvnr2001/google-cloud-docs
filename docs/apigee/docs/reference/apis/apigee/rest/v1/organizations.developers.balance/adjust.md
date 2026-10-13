---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/adjust/
title: Method: organizations.developers.balance.adjust \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:39.711343+00:00
---

# Method: organizations.developers.balance.adjust  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/adjust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.balance.adjust Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Adjust the prepaid balance for the developer.

This API will be used in scenarios where the developer has been under-charged or over-charged.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/developers/*/balance}:adjust`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Account balance for the developer. Use the following structure in your request: `organizations/{org}/developers/{developer}/balance` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.developerbalances.adjust`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "adjustment": {
        object ([Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money))
      }
    }  
  
Fields  
---  
`adjustment` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)`

  * A positive value of `adjustment` means that that the API provider wants to adjust the balance for an under-charged developer i.e. the balance of the developer will decrease.
  * A negative value of `adjustment` means that that the API provider wants to adjust the balance for an over-charged developer i.e. the balance of the developer will increase.

NOTE: An adjustment cannot increase the balance of the developer beyond the balance as of the most recent credit. For example, if a developer's balance is updated to be $100, and they spend $10, a negative adjustment can only increase the balance of the developer to $100.  
  
### Response body

If successful, the response body contains an instance of `[DeveloperBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/DeveloperBalance)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
