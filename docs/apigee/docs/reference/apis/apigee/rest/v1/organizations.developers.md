---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers
title: REST Resource: organizations.developers \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:33.611429+00:00
---

# REST Resource: organizations.developers  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.developers Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Developer
    * JSON representation
  * Methods



## Resource: Developer

JSON representation  
---  
      
    
    {
      "email": string,
      "firstName": string,
      "lastName": string,
      "userName": string,
      "attributes": [
        {
          object ([Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute))
        }
      ],
      "apps": [
        string
      ],
      "companies": [
        string
      ],
      "developerId": string,
      "organizationName": string,
      "status": string,
      "createdAt": string,
      "lastModifiedAt": string,
      "accessType": string,
      "appFamily": string
    }  
  
Fields  
---  
`email` |  `string` Required. Email address of the developer. This value is used to uniquely identify the developer in Apigee hybrid. Note that the email address has to be in lowercase only.  
`firstName` |  `string` Required. First name of the developer.  
`lastName` |  `string` Required. Last name of the developer.  
`userName` |  `string` Required. User name of the developer. Not used by Apigee hybrid.  
`attributes[]` |  `object (`[Attribute](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.apiproducts.attributes#Attribute)`)` Optional. Developer attributes (name/value pairs). The custom attribute limit is 18.  
`apps[]` |  `string` List of apps associated with the developer.  
`companies[]` |  `string` List of companies associated with the developer.  
`developerId` |  `string` ID of the developer.**Note** : IDs are generated internally by Apigee and are not guaranteed to stay the same over time.  
`organizationName` |  `string` Output only. Name of the Apigee organization in which the developer resides.  
`status` |  `string` Output only. Status of the developer. Valid values are `active` and `inactive`.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time at which the developer was created in milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time at which the developer was last modified in milliseconds since epoch.  
`accessType` |  `string` Access type.  
`appFamily` |  `string` Developer app family.  
  
## Methods  
  
---  
  
### `[attributes](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/attributes)`

|  Updates developer attributes.  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/create)`

|  Creates a developer.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/delete)`

|  Deletes a developer.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/get)`

|  Returns the developer details, including the developer's name, email address, apps, and other information.  
  
### `[getBalance](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getBalance)`

|  Gets the account balance for the developer.  
  
### `[getMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/getMonetizationConfig)`

|  Gets the monetization configuration for the developer.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/list)`

|  Lists all developers in an organization by email address.  
  
### `[setDeveloperStatus](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/setDeveloperStatus)`

|  Sets the status of a developer.  
  
### `[update](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/update)`

|  Updates a developer.  
  
### `[updateMonetizationConfig](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers/updateMonetizationConfig)`

|  Updates the monetization configuration for the developer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
