---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.create
title: REST Resource: organizations.developers.apps.keys.create \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:38.186794+00:00
---

# REST Resource: organizations.developers.apps.keys.create  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.create

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.developers.apps.keys.create Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeveloperAppKey
    * JSON representation
  * Methods



## Resource: DeveloperAppKey

JSON representation  
---  
      
    
    {
      "apiProducts": array,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "consumerKey": string,
      "consumerSecret": string,
      "expiresAt": string,
      "issuedAt": string,
      "scopes": [
        string
      ],
      "status": string,
      "expiresInSeconds": string
    }  
  
Fields  
---  
`apiProducts` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` List of API products for which the credential can be used.**Note** : Do not specify the list of API products when creating a consumer key and secret for a developer app. Instead, use the `[keys.updateDeveloperAppKey](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys/updateDeveloperAppKey#google.cloud.apigee.v1.DeveloperAppKeys.UpdateDeveloperAppKey)` API to make the association after the consumer key and secret are created.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` List of attributes associated with the credential.  
`consumerKey` |  `string` Consumer key.  
`consumerSecret` |  `string` Secret key.  
`expiresAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the developer app expires in milliseconds since epoch.  
`issuedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time the developer app was created in milliseconds since epoch.  
`scopes[]` |  `string` Scopes to apply to the app. The specified scope names must already be defined for the API product that you associate with the app.  
`status` |  `string` Status of the credential. Valid values include `approved` or `revoked`.  
`expiresInSeconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Input only. Expiration time, in seconds, for the consumer key. If not set or left to the default value of `-1`, the API key never expires. The expiration time can't be updated after it is set.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.apps.keys.create/create)`

|  Creates a custom consumer key and secret for a developer app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
