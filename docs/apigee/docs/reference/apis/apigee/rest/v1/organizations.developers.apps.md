---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps
title: REST Resource: organizations.developers.apps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:34.753578+00:00
---

# REST Resource: organizations.developers.apps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.developers.apps Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeveloperApp
    * JSON representation
  * Methods



## Resource: DeveloperApp

JSON representation  
---  
      
    
    {
      "appId": string,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "callbackUrl": string,
      "createdAt": string,
      "credentials": [
        {
          object ([Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Credential))
        }
      ],
      "developerId": string,
      "lastModifiedAt": string,
      "name": string,
      "scopes": [
        string
      ],
      "status": string,
      "keyExpiresIn": string,
      "appFamily": string,
      "apiProducts": [
        string
      ]
    }  
  
Fields  
---  
`appId` |  `string` ID of the developer app. This ID is not user specified but is automatically generated on app creation. appId is a UUID.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` List of attributes for the developer app.  
`callbackUrl` |  `string` Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to developer apps.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time the developer app was created in milliseconds since epoch.  
`credentials[]` |  `object (`[Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Credential)`)` Output only. Set of credentials for the developer app consisting of the consumer key/secret pairs associated with the API products.  
`developerId` |  `string` ID of the developer.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time the developer app was modified in milliseconds since epoch.  
`name` |  `string` Name of the developer app.  
`scopes[]` |  `string` Scopes to apply to the developer app. The specified scopes must already exist for the API product that you associate with the developer app.  
`status` |  `string` Status of the credential. Valid values include `approved` or `revoked`.  
`keyExpiresIn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Expiration time, in milliseconds, for the consumer key that is generated for the developer app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.  
`appFamily` |  `string` Developer app family.  
`apiProducts[]` |  `string` List of API products associated with the developer app.  
  
## Methods  
  
---  
  
### `[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/attributes)`

|  Updates attributes for a developer app.  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/create)`

|  Creates an app associated with a developer.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/delete)`

|  Deletes a developer app.  
  
### `[generateKeyPairOrUpdateDeveloperAppStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/generateKeyPairOrUpdateDeveloperAppStatus)`

|  Manages access to a developer app by enabling you to:

  * Approve or revoke a developer app
  * Generate a new consumer key and secret for a developer app

To approve or revoke a developer app, set the `action` query parameter to `approve` or `revoke`, respectively, and the `Content-Type` header to `application/octet-stream`.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/get)`

|  Returns the details for a developer app.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/list)`

|  Lists all apps created by a developer in an Apigee organization.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps/update)`

|  Updates the details for a developer app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
