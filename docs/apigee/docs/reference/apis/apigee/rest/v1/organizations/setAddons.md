---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons/
title: Method: organizations.setAddons \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:14.702171+00:00
---

# Method: organizations.setAddons  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setAddons/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.setAddons Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Configures the add-ons for the Apigee organization. The existing add-on configuration will be fully replaced.

### HTTP request

`POST https://apigee.googleapis.com/v1/{org=organizations/*}:setAddons`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`org` |  `string` Required. Name of the organization. Use the following structure in your request: `organizations/{org}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `org`:

  * `apigee.organizations.update`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "addonsConfig": {
        object ([AddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonsConfig))
      }
    }  
  
Fields  
---  
`addonsConfig` |  `object (`[AddonsConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations#AddonsConfig)`)` Required. Add-on configurations.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
