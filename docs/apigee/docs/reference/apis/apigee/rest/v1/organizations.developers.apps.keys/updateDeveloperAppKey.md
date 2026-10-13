---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey/
title: Method: organizations.developers.apps.keys.updateDeveloperAppKey \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:37.752895+00:00
---

# Method: organizations.developers.apps.keys.updateDeveloperAppKey  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.apps.keys.updateDeveloperAppKey Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Adds an API product to a developer app key, enabling the app that holds the key to access the API resources bundled in the API product.

In addition, you can add attributes and scopes associated with the API product to the developer app key. The status of the key can be updated via "action" Query Parameter. None of the other fields can be updated via this API. This API replaces the existing attributes with those specified in the request. Include or exclude any existing attributes that you want to retain or delete, respectively. None of the other fields can be updated.

You can use the same key to access all API products associated with the app.

### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/developers/*/apps/*/keys/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Name of the developer app key. Use the following structure in your request: `organizations/{org}/developers/{developerEmail}/apps/{app}/keys/{key}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.appkeys.manage`

  
  
### Query parameters

Parameters  
---  
`action` |  `string` Approve or revoke the consumer key by setting this value to `approve` or `revoke`, respectively. The `Content-Type` header must be set to `application/octet-stream`.  
  
### Request body

The request body contains an instance of `[DeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys#DeveloperAppKey)`.

### Response body

If successful, the response body contains an instance of `[DeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys#DeveloperAppKey)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
