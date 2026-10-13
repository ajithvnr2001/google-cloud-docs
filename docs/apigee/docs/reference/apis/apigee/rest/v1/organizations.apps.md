---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps
title: REST Resource: organizations.apps \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:30.550270+00:00
---

# REST Resource: organizations.apps  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.apps Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: App
    * JSON representation
  * Methods



## Resource: App

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
      "companyName": string,
      "developerId": string,
      "lastModifiedAt": string,
      "name": string,
      "scopes": [
        string
      ],
      "status": string,
      "apiProducts": [
        {
          object ([ApiProductRef](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProductRef))
        }
      ],
      "keyExpiresIn": string,
      "developerEmail": string,
      "appGroup": string
    }  
  
Fields  
---  
`appId` |  `string` ID of the app.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` List of attributes.  
`callbackUrl` |  `string` Callback URL used by OAuth 2.0 authorization servers to communicate authorization codes back to apps.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Unix time when the app was created.  
`credentials[]` |  `object (`[Credential](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/Credential)`)` Output only. Set of credentials for the app. Credentials are API key/secret pairs associated with API products.  
`companyName` |  `string` Name of the company that owns the app.  
`developerId` |  `string` ID of the developer.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Last modified time as milliseconds since epoch.  
`name` |  `string` Name of the app.  
`scopes[]` |  `string` Scopes to apply to the app. The specified scope names must already exist on the API product that you associate with the app.  
`status` |  `string` Status of the credential.  
`apiProducts[]` |  `object (`[ApiProductRef](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/ApiProductRef)`)` List of API products associated with the app.  
`keyExpiresIn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Duration, in milliseconds, of the consumer key that will be generated for the app. The default value, -1, indicates an infinite validity period. Once set, the expiration can't be updated. json key: keyExpiresIn  
`developerEmail` |  `string` Email of the developer.  
`appGroup` |  `string` Name of the AppGroup  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/get)`

|  Gets the app profile for the specified app ID.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apps/list)`

|  Lists IDs of apps within an organization that have the specified app status (approved or revoked) or are of the specified app type (developer or company).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
