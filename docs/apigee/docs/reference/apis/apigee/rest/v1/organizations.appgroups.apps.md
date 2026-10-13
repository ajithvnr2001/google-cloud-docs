---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps
title: REST Resource: organizations.appgroups.apps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:27.342923+00:00
---

# REST Resource: organizations.appgroups.apps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.appgroups.apps Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AppGroupApp
    * JSON representation
  * Methods



## Resource: AppGroupApp

Response for [apps.get].[AppGroupApps.GetAppGroupApp], [CreateAppGroupAppRequest].[AppGroupApp.CreateAppGroupAppRequest] and [apps.delete].[AppGroupApp.DeleteAppGroupApp]

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
      "lastModifiedAt": string,
      "name": string,
      "scopes": [
        string
      ],
      "status": string,
      "keyExpiresIn": string,
      "apiProducts": [
        string
      ],
      "appGroup": string
    }  
  
Fields  
---  
`appId` |  `string` Immutable. ID of the AppGroup app.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` List of attributes for the AppGroup app.  
`callbackUrl` |  `string` Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to AppGroup apps.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time the AppGroup app was created in milliseconds since epoch.  
`credentials[]` |  `object (`[Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Credential)`)` Output only. Set of credentials for the AppGroup app consisting of the consumer key/secret pairs associated with the API products.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time the AppGroup app was modified in milliseconds since epoch.  
`name` |  `string` Immutable. Name of the AppGroup app whose resource name format is of syntax (organizations/*/appgroups/*/apps/*).  
`scopes[]` |  `string` Scopes to apply to the AppGroup app. The specified scopes must already exist for the API product that you associate with the AppGroup app.  
`status` |  `string` Status of the App. Valid values include `approved` or `revoked`.  
`keyExpiresIn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Immutable. Expiration time, in seconds, for the consumer key that is generated for the AppGroup app. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.  
`apiProducts[]` |  `string` List of API products associated with the AppGroup app.  
`appGroup` |  `string` Immutable. Name of the parent AppGroup whose resource name format is of syntax (organizations/*/appgroups/*).  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/create)`

|  Creates an app and associates it with an AppGroup.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/delete)`

|  Deletes an AppGroup app.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/get)`

|  Returns the details for an AppGroup app.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/list)`

|  Lists all apps created by an AppGroup in an Apigee organization.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.appgroups.apps/update)`

|  Updates the details for an AppGroup app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
