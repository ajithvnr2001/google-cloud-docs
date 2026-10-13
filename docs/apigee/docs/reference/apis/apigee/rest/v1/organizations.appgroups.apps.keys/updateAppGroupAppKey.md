---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey/
title: Method: organizations.appgroups.apps.keys.updateAppGroupAppKey \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:28.813124+00:00
---

# Method: organizations.appgroups.apps.keys.updateAppGroupAppKey  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys/updateAppGroupAppKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.appgroups.apps.keys.updateAppGroupAppKey Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * Try it!



Adds an API product to an AppGroupAppKey, enabling the app that holds the key to access the API resources bundled in the API product.

In addition, you can add attributes and scopes to the AppGroupAppKey. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively.

You can use the same key to access all API products associated with the app.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/appgroups/*/apps/*/keys/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the AppGroup app key. Use the following structure in your request: `organizations/{org}/appgroups/{app_group_name}/apps/{app}/keys/{key}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.appkeys.manage`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "action": string,
      "appGroupAppKey": {
        object ([AppGroupAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys#AppGroupAppKey))
      },
      "apiProducts": [
        string
      ]
    }  
  
Fields  
---  
`action` |  `string` Approve or revoke the consumer key by setting this value to `approve` or `revoke` respectively. The `Content-Type` header, if set, must be set to `application/octet-stream`, with empty body.  
`appGroupAppKey` |  `object (`[AppGroupAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys#AppGroupAppKey)`)` Note that only Scopes and Attributes of the AppGroupAppKey can be amended. Scopes and Attributes mentioned in the request will be inserted and the existing scopes and attributes will be removed.  
`apiProducts[]` |  `string` The list of API products that will be associated with the credential. This list will be appended to the existing list of associated API Products for this App Key. Duplicates will be ignored.  
  
### Response body

If successful, the response body contains an instance of `[AppGroupAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps.keys#AppGroupAppKey)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
