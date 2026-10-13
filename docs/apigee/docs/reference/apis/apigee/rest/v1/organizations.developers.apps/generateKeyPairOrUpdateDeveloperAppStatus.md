---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/generateKeyPairOrUpdateDeveloperAppStatus/
title: Method: organizations.developers.apps.generateKeyPairOrUpdateDeveloperAppStatus \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:35.666900+00:00
---

# Method: organizations.developers.apps.generateKeyPairOrUpdateDeveloperAppStatus  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/generateKeyPairOrUpdateDeveloperAppStatus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Method: organizations.developers.apps.generateKeyPairOrUpdateDeveloperAppStatus Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Manages access to a developer app by enabling you to:

  * Approve or revoke a developer app
  * Generate a new consumer key and secret for a developer app



To approve or revoke a developer app, set the `action` query parameter to `approve` or `revoke`, respectively, and the `Content-Type` header to `application/octet-stream`. If a developer app is revoked, none of its API keys are valid for API calls even though the keys are still approved. If successful, the API call returns the following HTTP status code: `204 No Content`

To generate a new consumer key and secret for a developer app, pass the new key/secret details. Rather than replace an existing key, this API generates a new key. In this case, multiple key pairs may be associated with a single developer app. Each key pair has an independent status (`approve` or `revoke`) and expiration time. Any approved, non-expired key can be used in an API call.

For example, if you're using API key rotation, you can generate new keys with expiration times that overlap keys that are going to expire. You might also generate a new consumer key/secret if the security of the original key/secret is compromised.

The `keyExpiresIn` property defines the expiration time for the API key in milliseconds. If you don't set this property or set it to `-1`, the API key never expires.

**Notes** :

  * When generating a new key/secret, this API replaces the existing attributes, notes, and callback URLs with those specified in the request. Include or exclude any existing information that you want to retain or delete, respectively.
  * To migrate existing consumer keys and secrets to hybrid from another system, see the `[keys.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/create#google.cloud.apigee.v1.DeveloperAppKeys.CreateDeveloperAppKey)` API.



### HTTP request

`POST https://apigee.googleapis.com/v1/{name=organizations/*/developers/*/apps/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the developer app. Use the following structure in your request: `organizations/{org}/developers/{developerEmail}/apps/{app}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `apigee.developerapps.manage`

  
  
### Query parameters

Parameters  
---  
`action` |  `string` Action. Valid values are `approve` or `revoke`.  
  
### Request body

The request body contains an instance of `[DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps#DeveloperApp)`.

### Response body

If successful, the response body contains an instance of `[DeveloperApp](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps#DeveloperApp)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
