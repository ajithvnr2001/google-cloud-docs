---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/adjust/
title: Method: organizations.appgroups.balance.adjust \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:29.691113+00:00
---

# Method: organizations.appgroups.balance.adjust  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.balance/adjust/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.appgroups.balance.adjust Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Adjust the prepaid balance for the AppGroup.

This API will be used in scenarios where the AppGroup has been under-charged or over-charged.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/appgroups/*/balance}:adjust`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Account balance for the AppGroup. Use the following structure in your request: `organizations/{org}/appgroups/{appGroup}/balance` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.appgroupbalances.adjust`

  
  
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
`adjustment` |  `object (`[Money](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.rateplans#Money)`)` Required. * A positive value of `adjustment` means that that the API provider wants to adjust the balance for an under-charged AppGroup i.e. the balance of the AppGroup will decrease. * A negative value of `adjustment` is not supported. Use credit balance API instead.  
  
### Response body

If successful, the response body contains an instance of `[AppGroupBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/AppGroupBalance)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
