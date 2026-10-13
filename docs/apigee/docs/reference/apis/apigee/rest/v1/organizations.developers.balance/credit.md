---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/credit/
title: Method: organizations.developers.balance.credit \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:39.826012+00:00
---

# Method: organizations.developers.balance.credit  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.balance/credit/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.balance.credit Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Credits the account balance for the developer.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/developers/*/balance}:credit`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Account balance for the developer. Use the following structure in your request: `organizations/{org}/developers/{developer}/balance` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.developerbalances.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "transactionAmount": {
        object ([Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money))
      },
      "transactionId": string
    }  
  
Fields  
---  
`transactionAmount` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)` The amount of money to be credited. The wallet corresponding to the currency specified within `transactionAmount` will be updated. For example, if you specified `currencyCode` within `transactionAmount` as "USD", then the amount would be added to the wallet which has the "USD" currency or if no such wallet exists, a new wallet will be created with the "USD" currency.  
`transactionId` |  `string` Each transactionId uniquely identifies a credit balance request. If multiple requests are received with the same transactionId, only one of them will be considered.  
  
### Response body

If successful, the response body contains an instance of `[DeveloperBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/DeveloperBalance)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
