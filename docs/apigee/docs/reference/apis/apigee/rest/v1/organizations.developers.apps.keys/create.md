---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create/
title: Method: organizations.developers.apps.keys.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:37.031302+00:00
---

# Method: organizations.developers.apps.keys.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.apps.keys.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Creates a custom consumer key and secret for a developer app. This is particularly useful if you want to migrate existing consumer keys and secrets to Apigee from another system.

Consumer keys and secrets can contain letters, numbers, underscores, and hyphens. No other special characters are allowed. To avoid service disruptions, a consumer key and secret should not exceed 2 KBs each.

**Note** : When creating the consumer key and secret, an association to API products will not be made. Therefore, you should not specify the associated API products in your request. Instead, use the `[keys.updateDeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey#google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey)` API to make the association after the consumer key and secret are created.

If a consumer key and secret already exist, you can keep them or delete them using the `[keys.delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/delete#google.cloud.apigee.v1.DeveloperAppKeys.DeleteDeveloperAppKey)` API.

**Note** : All keys start out with status=approved, even if status=revoked is passed when the key is created. To revoke a key, use the `[keys.updateDeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey#google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey)` API.

### HTTP request

`POST https://apigee.googleapis.com/v1/{parent=organizations/*/developers/*/apps/*}/keys`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Parent of the developer app key. Use the following structure in your request: 'organizations/{org}/developers/{developerEmail}/apps/{appName}' Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `apigee.appkeys.create`

  
  
### Request body

The request body contains an instance of `[DeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys#DeveloperAppKey)`.

### Response body

If successful, the response body contains a newly created instance of `[DeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys#DeveloperAppKey)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
