---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions
title: REST Resource: organizations.developers.subscriptions \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:40.082524+00:00
---

# REST Resource: organizations.developers.subscriptions  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.developers.subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: DeveloperSubscription
    * JSON representation
  * Methods



## Resource: DeveloperSubscription

Structure of a DeveloperSubscription.

JSON representation  
---  
      
    
    {
      "name": string,
      "apiproduct": string,
      "startTime": string,
      "endTime": string,
      "createdAt": string,
      "lastModifiedAt": string
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the API product subscription.  
`apiproduct` |  `string` Name of the API product for which the developer is purchasing a subscription.  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time when the API product subscription starts in milliseconds since epoch.  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Time when the API product subscription ends in milliseconds since epoch.  
`createdAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time when the API product subscription was created in milliseconds since epoch.  
`lastModifiedAt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Time when the API product subscription was last modified in milliseconds since epoch.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/create)`

|  Creates a subscription to an API product.  
  
### `[expire](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/expire)`

|  Expires an API product subscription immediately.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/get)`

|  Gets details for an API product subscription.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.developers.subscriptions/list)`

|  Lists all API product subscriptions for a developer.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
